#!/usr/bin/env python3
"""Validate CK3 Russian localization against the English source, without dependencies."""

from collections import Counter
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
ENTRY = re.compile(r'^\s*([\w.]+):\s*(?:\d+\s*)?"((?:\\.|[^"\\])*)"\s*$')
TOKENS = re.compile(r'\[[^\]]*\]|\$[^$]+\$|@[\w]+!|#!|#[A-Za-z_]+(?::[^\s]+)?')
# The game provides this alias; every other $alias$ must exist in this mod.
VANILLA_ALIASES = {"EFFECT_LIST_BULLET"}


def read_language(language, errors):
    files = {}
    all_entries = {}
    directory = ROOT / "localization" / language
    for path in sorted(directory.rglob("*.yml")):
        raw = path.read_bytes()
        if not raw.startswith(b"\xef\xbb\xbf") or not raw.endswith(b"\n"):
            errors.append(f"{path.relative_to(ROOT)}: requires BOM and trailing newline")
        text = raw.decode("utf-8-sig")
        if not text.startswith(f"l_{language}:\n") and not text.startswith(f"l_{language}:\r\n"):
            errors.append(f"{path.relative_to(ROOT)}: incorrect language header")
        if not path.name.endswith(f"_l_{language}.yml"):
            errors.append(f"{path.relative_to(ROOT)}: incorrect language filename")
        entries = {}
        for number, line in enumerate(text.splitlines()[1:], 2):
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            match = ENTRY.fullmatch(line)
            if not match:
                errors.append(f"{path.relative_to(ROOT)}:{number}: malformed localization")
                continue
            key, value = match.groups()
            if key in all_entries:
                errors.append(f"{language}: duplicate key {key}")
            entries[key] = value
            all_entries[key] = value
        relative = str(path.relative_to(directory)).replace(f"_l_{language}", "_l_LANGUAGE")
        files[relative] = entries
    if not files:
        errors.append(f"{language}: no localization files")
    for key, value in all_entries.items():
        for alias in re.findall(r'\$([^$]+)\$', value):
            if alias not in all_entries and alias not in VANILLA_ALIASES:
                errors.append(f"{language}: {key} references missing alias {alias}")
    return files, all_entries


def main():
    errors = []
    english, english_keys = read_language("english", errors)
    russian, russian_keys = read_language("russian", errors)
    if english.keys() != russian.keys():
        errors.append(f"File coverage mismatch: {english.keys() ^ russian.keys()}")
    for filename in english.keys() & russian.keys():
        source, translated = english[filename], russian[filename]
        if source.keys() != translated.keys():
            errors.append(f"{filename}: key coverage mismatch {source.keys() ^ translated.keys()}")
        for key in source.keys() & translated.keys():
            if Counter(TOKENS.findall(source[key])) != Counter(TOKENS.findall(translated[key])):
                errors.append(f"{key}: altered dynamic substitution or formatting token")
            # Token-only strings (including aliases and the discipline grid) need no prose translation.
            prose = re.sub(r'\\[nrt"\\]', "", TOKENS.sub("", source[key]))
            if source[key] == translated[key] and re.search(r'[A-Za-z]', prose):
                errors.append(f"{key}: untranslated English prose")
    # Audit explicit mod-local UI references; vanilla keys and script variable names are excluded.
    for directory in ("common", "events"):
        for path in (ROOT / directory).rglob("*.txt"):
            text = path.read_text(encoding="utf-8-sig")
            for line in text.splitlines():
                line = line.split("#", 1)[0]
                for key in re.findall(
                    r'\b(?:desc|title|text|tooltip|custom_tooltip|localization_key|send_name)\s*=\s*"?(bm_[\w.]+)',
                    line,
                ):
                    if key not in english_keys or key not in russian_keys:
                        errors.append(f"{path.relative_to(ROOT)}: missing UI key {key}")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"PASS: {len(russian_keys)} Russian keys across {len(russian)} files; "
          "coverage, syntax, substitutions, formatting, aliases, and explicit bm_ UI references verified.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
