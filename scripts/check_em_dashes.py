#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""
Blood Mages CK3 Mod - Em-Dash Checker
Forbids the Unicode em-dash character (U+2014) in tracked text files.
Supports --staged (for git pre-commit hooks) and full-repo scan (default).
"""

import argparse
import subprocess
import sys
from pathlib import Path

EM_DASH = "\u2014"


def get_staged_files(repo_root: Path) -> list[Path]:
    """Return added, copied, or modified files currently staged in git."""
    res = subprocess.run(
        ["git", "diff", "--cached", "--name-only", "--diff-filter=ACM", "-z"],
        cwd=repo_root,
        capture_output=True,
        check=True,
    )
    files: list[Path] = []
    for raw in res.stdout.split(b"\x00"):
        if not raw:
            continue
        p = repo_root / raw.decode("utf-8", errors="surrogateescape")
        if p.is_file():
            files.append(p)
    return files


def get_tracked_files(repo_root: Path) -> list[Path]:
    """Return all git-tracked files in the repository."""
    res = subprocess.run(
        ["git", "ls-files", "-z"],
        cwd=repo_root,
        capture_output=True,
        check=True,
    )
    files: list[Path] = []
    for raw in res.stdout.split(b"\x00"):
        if not raw:
            continue
        p = repo_root / raw.decode("utf-8", errors="surrogateescape")
        if p.is_file():
            files.append(p)
    return sorted(files)


def check_file(path: Path, repo_root: Path) -> list[str]:
    """Check a single file for em-dash occurrences. Skips binary files."""
    try:
        raw = path.read_bytes()
    except OSError:
        return []
    if b"\x00" in raw:
        return []
    try:
        text = raw.decode("utf-8-sig")
    except UnicodeDecodeError:
        return []

    if EM_DASH not in text:
        return []

    rel = path.relative_to(repo_root)
    violations: list[str] = []
    for line_no, line in enumerate(text.splitlines(), start=1):
        col = line.find(EM_DASH)
        while col != -1:
            snippet = line.strip()
            if len(snippet) > 120:
                snippet = snippet[:117] + "..."
            violations.append(f"{rel}:{line_no}:{col + 1}: {snippet}")
            col = line.find(EM_DASH, col + 1)
    return violations


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Forbid em-dash characters (U+2014) in tracked text files."
    )
    parser.add_argument(
        "--staged",
        action="store_true",
        help="Check only staged files (for git pre-commit hooks).",
    )
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parent.parent
    files = get_staged_files(repo_root) if args.staged else get_tracked_files(repo_root)

    all_violations: list[str] = []
    for path in files:
        all_violations.extend(check_file(path, repo_root))

    if all_violations:
        for v in all_violations:
            print(v, file=sys.stderr)
        print(
            f"\nFound {len(all_violations)} em-dash (U+2014) violation(s).",
            file=sys.stderr,
        )
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
