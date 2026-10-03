#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""
Blood Mages CK3 Mod - Repository & Game File Integrity Checker
Enforces the format rules documented in AGENTS.md:
- .txt, .gui, .yml: UTF-8 with BOM, trailing newline, balanced braces.
- Preserves line endings and indentation.
- Checks #tiger-ignore justification comments.
- Supports --staged (for git pre-commit hooks) and --fix (auto-fix BOM/newlines).
"""

import argparse
import os
import subprocess
import sys
from pathlib import Path

GAME_DIRS = {"common", "events", "gui", "localization", "gfx"}
GAME_EXTENSIONS = {".txt", ".gui", ".yml"}
EXCLUDE_DIRS = {
    ".git",
    ".agents",
    "docs",
    "docs-ai",
    "llm_context",
    "steam-workshop",
    "tests",
    "scratch",
}


def is_game_file(path: Path) -> bool:
    """Check if the given path is a game file subject to CK3 engine formatting rules."""
    parts = path.parts
    if any(part in EXCLUDE_DIRS for part in parts):
        return False
    if path.suffix.lower() not in GAME_EXTENSIONS:
        return False
    if len(parts) > 1 and parts[0] in GAME_DIRS:
        return True
    # Files directly in root like descriptor.mod are excluded from BOM unless specified
    return False


def get_staged_files(repo_root: Path) -> list[Path]:
    """Retrieve all added, copied, or modified files currently staged in git."""
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
            if line:
                p = repo_root / line
                if p.is_file() and is_game_file(p.relative_to(repo_root)):
                    files.append(p)
        return files
    except subprocess.CalledProcessError as e:
        print(f"Error querying staged files from git: {e}", file=sys.stderr)
        return []


def get_all_game_files(repo_root: Path) -> list[Path]:
    """Scan the repository for all game script, GUI, and localization files."""
    files = []
    for d in GAME_DIRS:
        dir_path = repo_root / d
        if not dir_path.is_dir():
            continue
        for p in dir_path.rglob("*"):
            if p.is_file() and is_game_file(p.relative_to(repo_root)):
                files.append(p)
    return sorted(files)


def check_balanced_braces(text: str) -> tuple[bool, int, int]:
    """
    Check if curly braces { and } are balanced, ignoring comments (#) and quotes.
    Returns (is_balanced, open_count, close_count).
    """
    in_string = False
    open_count = 0
    close_count = 0

    for line in text.splitlines():
        i = 0
        while i < len(line):
            ch = line[i]
            if ch == '"':
                in_string = not in_string
            elif ch == '#' and not in_string:
                break  # Comment begins, ignore remainder of line
            elif not in_string:
                if ch == '{':
                    open_count += 1
                elif ch == '}':
                    close_count += 1
            i += 1

    return (open_count == close_count, open_count, close_count)


def check_tiger_ignores(text: str) -> list[tuple[int, str]]:
    """
    Check that any #tiger-ignore(...) comment has an accompanying justification comment.
    According to AGENTS.md: "#tiger-ignore(...) needs a justification comment."
    """
    issues = []
    lines = text.splitlines()
    for idx, line in enumerate(lines, start=1):
        if "#tiger-ignore" in line:
            # Check if there is explanation text after the ignore tag or on an adjacent line
            # e.g. #tiger-ignore(foo) - reason here, or followed/preceded by comment
            stripped = line.strip()
            # If line is just `#tiger-ignore(...)` with no reason
            after_comment = stripped[stripped.find("#tiger-ignore") :]
            has_inline_comment = False
            if ")" in after_comment:
                rest = after_comment[after_comment.find(")") + 1 :].strip()
                if rest.startswith("-") or rest.startswith(":") or len(rest) > 3:
                    has_inline_comment = True

            has_prev_comment = (
                idx > 1 and lines[idx - 2].strip().startswith("#") and not "#tiger-ignore" in lines[idx - 2]
            )
            has_next_comment = (
                idx < len(lines)
                and lines[idx].strip().startswith("#")
                and not "#tiger-ignore" in lines[idx]
            )

            if not (has_inline_comment or has_prev_comment or has_next_comment):
                issues.append((idx, line.strip()))
    return issues


def check_file(path: Path, auto_fix: bool = False) -> list[str]:
    """Validate a single file and optionally fix BOM and trailing newline."""
    errors = []
    try:
        with open(path, "rb") as f:
            raw = f.read()
    except OSError as e:
        return [f"Could not read file: {e}"]

    has_bom = raw.startswith(b"\xef\xbb\xbf")
    has_trailing_nl = raw.endswith(b"\n")

    if auto_fix and (not has_bom or not has_trailing_nl):
        fixed_raw = raw
        if not has_bom:
            fixed_raw = b"\xef\xbb\xbf" + fixed_raw
        if not has_trailing_nl:
            fixed_raw = fixed_raw + b"\n"
        try:
            with open(path, "wb") as f:
                f.write(fixed_raw)
            print(f"Fixed formatting for: {path}")
            raw = fixed_raw
            has_bom = True
            has_trailing_nl = True
        except OSError as e:
            errors.append(f"Failed to auto-fix {path}: {e}")

    if not has_bom:
        errors.append("Missing UTF-8 BOM (required for CK3 .txt, .gui, .yml)")
    if not has_trailing_nl:
        errors.append("Missing trailing newline at end of file")

    try:
        text = raw.decode("utf-8-sig")
    except UnicodeDecodeError as e:
        errors.append(f"File is not valid UTF-8: {e}")
        return errors

    # Check balanced braces for script and gui files (YAML uses indentation)
    if path.suffix.lower() in {".txt", ".gui"}:
        balanced, opens, closes = check_balanced_braces(text)
        if not balanced:
            errors.append(
                f"Unbalanced braces: {opens} opening '{{' vs {closes} closing '}}'"
            )

    # Check tiger-ignore justification
    tiger_issues = check_tiger_ignores(text)
    for line_num, line_text in tiger_issues:
        errors.append(
            f"Line {line_num}: #tiger-ignore requires a justification comment ('{line_text}')"
        )

    return errors


def install_pre_commit_hook(repo_root: Path) -> bool:
    """Install the pre-commit git hook into .git/hooks/pre-commit."""
    hook_dir = repo_root / ".git" / "hooks"
    if not hook_dir.is_dir():
        print(f"Error: .git/hooks directory not found at {hook_dir}", file=sys.stderr)
        return False

    hook_file = hook_dir / "pre-commit"
    hook_content = """#!/bin/sh
# Blood Mages CK3 Mod - Pre-commit Hook
# Runs git whitespace checks and file format validations on staged files.

# 1. Check for conflict markers, whitespace issues, etc.
if ! git diff --cached --check; then
    echo "\\033[1;31m[PRE-COMMIT ERROR] Git whitespace or conflict marker check failed!\\033[0m" >&2
    exit 1
fi

# 2. Check game file formatting on staged files (BOM, balanced braces, trailing newline)
if command -v uv > /dev/null 2>&1; then
    CHECK_CMD="uv run scripts/check_repo.py"
else
    CHECK_CMD="python3 scripts/check_repo.py"
fi

if ! $CHECK_CMD --staged; then
    echo "\\033[1;31m[PRE-COMMIT ERROR] Game file integrity checks failed. Commit aborted.\\033[0m" >&2
    echo "\\033[1;33mTip: Run '$CHECK_CMD --fix' to automatically resolve BOM and newline issues.\\033[0m" >&2
    exit 1
fi

exit 0
"""
    try:
        with open(hook_file, "w", encoding="utf-8", newline="\n") as f:
            f.write(hook_content)
        os.chmod(hook_file, 0o755)
        print(f"Pre-commit hook successfully installed at: {hook_file}")
        return True
    except OSError as e:
        print(f"Failed to install pre-commit hook: {e}", file=sys.stderr)
        return False


def main():
    parser = argparse.ArgumentParser(
        description="Verify CK3 mod repository file formats, BOMs, and balanced braces."
    )
    parser.add_argument(
        "--staged",
        action="store_true",
        help="Check only files currently staged in git (used by pre-commit hook)",
    )
    parser.add_argument(
        "--fix",
        action="store_true",
        help="Automatically fix missing UTF-8 BOM and trailing newlines",
    )
    parser.add_argument(
        "--install-hook",
        action="store_true",
        help="Install the pre-commit hook into .git/hooks/pre-commit",
    )
    parser.add_argument(
        "files",
        nargs="*",
        help="Optional specific file paths to check. If omitted, checks all or staged.",
    )

    args = parser.parse_args()
    repo_root = Path(__file__).resolve().parent.parent

    if args.install_hook:
        success = install_pre_commit_hook(repo_root)
        sys.exit(0 if success else 1)

    if args.files:
        target_files = []
        for f in args.files:
            p = Path(f).resolve()
            if p.is_file():
                try:
                    rel = p.relative_to(repo_root)
                except ValueError:
                    rel = p
                if is_game_file(rel):
                    target_files.append(p)
        if not target_files:
            sys.exit(0)
    elif args.staged:
        target_files = get_staged_files(repo_root)
        if not target_files:
            # No game files staged
            sys.exit(0)
    else:
        target_files = get_all_game_files(repo_root)

    total_files = len(target_files)
    total_errors = 0

    for path in target_files:
        rel_path = path.relative_to(repo_root) if path.is_relative_to(repo_root) else path
        errors = check_file(path, auto_fix=args.fix)
        if errors:
            total_errors += len(errors)
            print(f"\033[1;31m[ERROR]\033[0m {rel_path}:")
            for err in errors:
                print(f"  - {err}")

    if total_errors > 0:
        print(
            f"\n\033[1;31mFAILED\033[0m: Found {total_errors} error(s) across {total_files} file(s).",
            file=sys.stderr,
        )
        if not args.fix:
            print("Tip: Run with --fix to automatically correct missing BOM and newlines.", file=sys.stderr)
        sys.exit(1)
    else:
        print(f"\033[1;32mPASSED\033[0m: All {total_files} checked file(s) meet CK3 format requirements.")
        sys.exit(0)


if __name__ == "__main__":
    main()
