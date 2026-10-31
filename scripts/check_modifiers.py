#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""
CK3 Blood Mage Mod - Modifier Usage & Allowlist Validator
Enforces that:
1. All modifiers used across the mod (in modifiers, traits, holy sites, doctrines,
   buildings, and domiciles) belong to the approved allowlist in scripts/modifiers_allowlist.json.
2. No modifier can be added to the allowlist unless verified to exist in vanilla CK3 1.20
   definition formats (common/modifier_definition_formats/ + C++ custom code overwrites).
3. Provides --add <modifier> to safely confirm and append new modifiers to the allowlist.
"""

from __future__ import annotations

import argparse
import difflib
import json
import os
import re
import subprocess
import sys
from pathlib import Path

DEFAULT_VANILLA_PATH = Path("/Users/clarabotet/Petur/ck3-full")
SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
ALLOWLIST_FILE = SCRIPT_DIR / "modifiers_allowlist.json"
VANILLA_DEFS_FALLBACK = SCRIPT_DIR / "vanilla_all_definitions.json"

MODIFIER_BLOCK_NAMES = {
    "character_modifier",
    "county_modifier",
    "province_modifier",
    "duchy_capital_county_modifier",
    "domicile_modifier",
    "doctrine_character_modifier",
    "clergy_modifier",
    "holder_modifier",
    "owner_modifier",
}

MODIFIER_FILE_METADATA = {
    "icon",
    "desc",
    "stacking",
    "name",
    "soundeffect",
    "scale",
    "value",
    "decay",
    "show_as_positive",
    "major",
}

TRAIT_METADATA = {
    "category",
    "flag",
    "icon",
    "desc",
    "ruler_designer_cost",
    "index",
    "tracks",
    "shown_in_ruler_designer",
    "potential",
    "same_opinion",
    "same_opinion_if_same_faith",
    "opposite_opinion",
    "birth",
    "random_creation",
    "inherit_chance",
    "genetic",
    "enables_inbred",
    "good",
    "trait_exclusive_if_realm_has_dlc",
    "name",
    "group",
}

# Modifiers with custom C++ engine overwrites documented in vanilla 00_definitions.txt
ENGINE_CUSTOM_OVERWRITES = {
    "health": "00_definitions.txt (custom code overwrite)",
    "child_health": "00_definitions.txt (custom code overwrite)",
    "adult_health": "00_definitions.txt (custom code overwrite)",
    "elderly_health": "00_definitions.txt (custom code overwrite)",
    "negate_health_penalty_add": "00_definitions.txt (custom code overwrite)",
}


def load_vanilla_definitions(vanilla_root: Path | None = None) -> dict[str, str]:
    """
    Load all vanilla modifier definitions from common/modifier_definition_formats/*.txt.
    Falls back to scripts/vanilla_all_definitions.json if the vanilla folder is absent.
    """
    target_root = vanilla_root or DEFAULT_VANILLA_PATH
    formats_dir = target_root / "common" / "modifier_definition_formats"

    defs: dict[str, str] = {}

    if formats_dir.is_dir():
        for txt_file in sorted(formats_dir.glob("*.txt")):
            fname = txt_file.name
            try:
                with open(txt_file, "r", encoding="utf-8-sig", errors="ignore") as fp:
                    for line in fp:
                        m = re.match(r"^([a-zA-Z0-9_]+)\s*=", line.strip())
                        if m:
                            defs[m.group(1)] = fname
            except OSError as e:
                print(f"[WARN] Failed to read {txt_file}: {e}", file=sys.stderr)
        defs.update(ENGINE_CUSTOM_OVERWRITES)
        return defs

    if VANILLA_DEFS_FALLBACK.is_file():
        try:
            with open(VANILLA_DEFS_FALLBACK, "r", encoding="utf-8") as fp:
                loaded = json.load(fp)
                if isinstance(loaded, dict):
                    defs.update(loaded)
                    return defs
        except (OSError, json.JSONDecodeError) as e:
            print(f"[WARN] Failed to read fallback vanilla definitions: {e}", file=sys.stderr)

    defs.update(ENGINE_CUSTOM_OVERWRITES)
    return defs


def load_allowlist() -> dict[str, dict]:
    """Load the approved modifiers allowlist."""
    if not ALLOWLIST_FILE.is_file():
        return {}
    try:
        with open(ALLOWLIST_FILE, "r", encoding="utf-8") as fp:
            data = json.load(fp)
            return data.get("modifiers", {})
    except (OSError, json.JSONDecodeError) as e:
        print(f"[ERROR] Failed to read allowlist at {ALLOWLIST_FILE}: {e}", file=sys.stderr)
        return {}


def save_allowlist(modifiers: dict[str, dict]) -> None:
    """Save sorted modifiers to allowlist."""
    data = {
        "version": "1.20",
        "description": "Allowlist of vanilla CK3 modifiers currently permitted in ck3_blood_mage.",
        "modifiers": dict(sorted(modifiers.items())),
    }
    with open(ALLOWLIST_FILE, "w", encoding="utf-8") as fp:
        json.dump(data, fp, indent=2)
        fp.write("\n")


def check_allowlist_integrity(vanilla_defs: dict[str, str], allowlist: dict[str, dict]) -> list[str]:
    """Ensure every modifier in the allowlist is confirmed to exist in vanilla."""
    errors = []
    for mod_key in allowlist:
        if mod_key not in vanilla_defs:
            errors.append(f"Modifier '{mod_key}' in allowlist is not a valid vanilla 1.20 modifier definition.")
    return errors


def parse_file_modifiers(file_path: Path) -> list[tuple[int, str, str, str]]:
    """
    Parse a CK3 script file and return list of (line_num, key, value, scope_stack)
    for items located inside modifier contexts.
    """
    try:
        with open(file_path, "r", encoding="utf-8-sig", errors="ignore") as fp:
            lines = fp.readlines()
    except OSError:
        return []

    tokens: list[tuple[str, int]] = []
    token_pattern = re.compile(r'#[^\n]*|(\"[^\"]*\")|([a-zA-Z0-9_@\.:\-]+)|([{}=])')
    for line_idx, line in enumerate(lines, 1):
        for m in token_pattern.finditer(line):
            s = m.group(0)
            if s.startswith("#"):
                continue
            tokens.append((s, line_idx))

    events: list[tuple[str, list[str], str, str, int]] = []
    stack: list[str] = []
    i = 0
    while i < len(tokens):
        tok, line_num = tokens[i]
        if i + 1 < len(tokens) and tokens[i + 1][0] == "=":
            key = tok
            if i + 2 < len(tokens) and tokens[i + 2][0] == "{":
                stack.append(key)
                events.append(("push", list(stack), "", "", line_num))
                i += 3
                continue
            elif i + 2 < len(tokens):
                val = tokens[i + 2][0]
                events.append(("kv", list(stack), key, val, line_num))
                i += 3
                continue
        if tok == "}":
            if stack:
                stack.pop()
            events.append(("pop", list(stack), "", "", line_num))
            i += 1
            continue
        i += 1

    rel_path_str = str(file_path)
    is_modifier_file = "common/modifiers" in rel_path_str
    is_trait_file = "common/traits" in rel_path_str

    extracted = []
    for ev_type, st, key, val, line_num in events:
        if ev_type != "kv":
            continue

        in_modifier_context = False
        if is_modifier_file and len(st) >= 1:
            if key in MODIFIER_FILE_METADATA:
                continue
            in_modifier_context = True
        elif any(s in MODIFIER_BLOCK_NAMES for s in st):
            in_modifier_context = True
        elif is_trait_file and any(s.isdigit() for s in st):
            in_modifier_context = True
        elif is_trait_file and len(st) == 1 and st[0].startswith("lifestyle_"):
            if key in TRAIT_METADATA:
                continue
            in_modifier_context = True

        if in_modifier_context:
            extracted.append((line_num, key, val, "/".join(st)))

    return extracted


def get_staged_game_files(repo_root: Path) -> list[Path]:
    """Retrieve staged game text files in common/ and events/."""
    try:
        res = subprocess.run(
            ["git", "diff", "--cached", "--name-only", "--diff-filter=ACM"],
            cwd=repo_root,
            capture_output=True,
            text=True,
            check=True,
        )
        files = []
        for line in res.stdout.splitlines():
            line = line.strip()
            if not line:
                continue
            p = repo_root / line
            if p.is_file() and p.suffix.lower() == ".txt":
                parts = p.relative_to(repo_root).parts
                if len(parts) > 1 and parts[0] in {"common", "events"}:
                    files.append(p)
        return files
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Failed to query git staged files: {e}", file=sys.stderr)
        return []


def get_all_game_txt_files(repo_root: Path) -> list[Path]:
    """Retrieve all .txt files in common/ and events/."""
    files = []
    for d in ("common", "events"):
        target_dir = repo_root / d
        if target_dir.is_dir():
            for p in sorted(target_dir.rglob("*.txt")):
                if p.is_file():
                    files.append(p)
    return files


def handle_add_modifier(mod_name: str, vanilla_defs: dict[str, str], allowlist: dict[str, dict]) -> int:
    """Validate existence in vanilla and add to allowlist."""
    mod_name = mod_name.strip()
    if not mod_name:
        print("[ERROR] No modifier name provided to --add.", file=sys.stderr)
        return 1

    if mod_name in allowlist:
        print(f"Modifier '{mod_name}' is already in the allowlist ({allowlist[mod_name].get('vanilla_definition')}).")
        return 0

    if mod_name not in vanilla_defs:
        print(f"[ERROR] Modifier '{mod_name}' does not exist in vanilla CK3 1.20 definitions!", file=sys.stderr)
        close_matches = difflib.get_close_matches(mod_name, vanilla_defs.keys(), n=5, cutoff=0.6)
        if close_matches:
            print(f"Did you mean one of these vanilla modifiers?", file=sys.stderr)
            for match in close_matches:
                print(f"  - {match} ({vanilla_defs[match]})", file=sys.stderr)
        return 1

    src_file = vanilla_defs[mod_name]
    allowlist[mod_name] = {
        "category": "Added",
        "vanilla_definition": src_file,
    }
    save_allowlist(allowlist)
    print(f"SUCCESS: Confirmed existence in vanilla '{src_file}' and added '{mod_name}' to {ALLOWLIST_FILE.name}.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="CK3 Blood Mage Modifier Allowlist & Usage Checker")
    parser.add_argument("--staged", action="store_true", help="Only inspect git staged files in common/ and events/")
    parser.add_argument("--add", metavar="MODIFIER", help="Confirm existence in vanilla 1.20 and add to allowlist")
    parser.add_argument("--check-allowlist", action="store_true", help="Only verify that allowlist entries exist in vanilla")
    parser.add_argument("--vanilla-path", type=Path, default=DEFAULT_VANILLA_PATH, help="Path to vanilla CK3 game directory")
    parser.add_argument("files", nargs="*", type=Path, help="Specific files to check")

    args = parser.parse_args()

    vanilla_defs = load_vanilla_definitions(args.vanilla_path)
    allowlist = load_allowlist()

    # Handle adding a new modifier
    if args.add:
        return handle_add_modifier(args.add, vanilla_defs, allowlist)

    # Validate the allowlist itself first
    allowlist_errors = check_allowlist_integrity(vanilla_defs, allowlist)
    if allowlist_errors:
        print("=" * 70, file=sys.stderr)
        print("[ERROR] Allowlist integrity check failed!", file=sys.stderr)
        print("=" * 70, file=sys.stderr)
        for err in allowlist_errors:
            print(f"  - {err}", file=sys.stderr)
        return 1

    if args.check_allowlist:
        print(f"PASS: All {len(allowlist)} allowlist modifiers confirmed in vanilla definitions.")
        return 0

    # Determine files to scan
    if args.files:
        files_to_check = [f.resolve() for f in args.files if f.is_file() and f.suffix.lower() == ".txt"]
    elif args.staged:
        files_to_check = get_staged_game_files(REPO_ROOT)
    else:
        files_to_check = get_all_game_txt_files(REPO_ROOT)

    if not files_to_check:
        return 0

    violations = []
    for f in files_to_check:
        items = parse_file_modifiers(f)
        for line_num, key, val, stack in items:
            if key not in allowlist:
                violations.append((f, line_num, key, val, stack))

    if violations:
        print("=" * 70, file=sys.stderr)
        print(f"[FAIL] Found {len(violations)} unallowed modifier usage(s) in mod files!", file=sys.stderr)
        print("=" * 70, file=sys.stderr)
        for f, line_num, key, val, stack in violations:
            rel = f.relative_to(REPO_ROOT) if f.is_relative_to(REPO_ROOT) else f
            print(f"  {rel}:{line_num} -> '{key} = {val}' (inside {stack})", file=sys.stderr)
            if key in vanilla_defs:
                print(f"      [NOTE] '{key}' is a valid vanilla modifier ({vanilla_defs[key]}).", file=sys.stderr)
                print(f"      To permit it, run: python3 scripts/check_modifiers.py --add {key}", file=sys.stderr)
            else:
                close = difflib.get_close_matches(key, vanilla_defs.keys(), n=3, cutoff=0.6)
                if close:
                    print(f"      [HINT] Did you mean one of: {', '.join(close)}?", file=sys.stderr)
        return 1

    if not args.staged:
        print(f"PASS: All {len(allowlist)} allowlist entries verified; 0 unallowed modifiers in {len(files_to_check)} files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
