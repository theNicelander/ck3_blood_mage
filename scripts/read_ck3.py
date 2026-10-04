#!/usr/bin/env python3
"""
Blood Mages CK3 Mod - File Reader & Inspector Helper

Safely reads and inspects CK3 mod files (.txt, .gui, .yml) handling:
- UTF-8 with BOM (utf-8-sig) transparently
- Both LF and CRLF line endings
- CK3 block/scope search (extracting blocks like 'site = { ... }' or 'tenets = { ... }')
- Looking up definitions across mod folders and vanilla game sources (ck3-full)
"""

import argparse
import os
import re
import sys
from pathlib import Path
from typing import List, Tuple, Union

DEFAULT_VANILLA_DIRS = [
    Path("/Users/clarabotet/Petur/ck3-full"),
    Path("/Users/clarabotet/Library/Application Support/Steam/steamapps/common/Crusader Kings III/game"),
]


def read_ck3_file(filepath: Union[Path, str]) -> str:
    """Reads a CK3 file with proper BOM and encoding handling."""
    path = Path(filepath)
    if not path.is_file():
        raise FileNotFoundError(f"File not found: {path}")
    # utf-8-sig automatically strips BOM if present, and decodes standard UTF-8 without errors
    with open(path, "r", encoding="utf-8-sig", errors="replace") as f:
        return f.read()


def write_ck3_file(filepath: Union[Path, str], content: str) -> None:
    """Writes a CK3 file preserving UTF-8 BOM encoding."""
    path = Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8-sig", newline="", errors="replace") as f:
        f.write(content)


def find_block(text: str, block_name: str) -> List[str]:
    """
    Extracts complete balanced { ... } blocks matching 'block_name = {'.
    Handles arbitrary nesting cleanly.
    """
    pattern = re.compile(rf"(?:^|\s)({re.escape(block_name)}\s*=\s*\{{)", re.MULTILINE)
    blocks = []
    for match in pattern.finditer(text):
        start_idx = match.start(1)
        open_brace_idx = text.find("{", start_idx)
        if open_brace_idx == -1:
            continue
        depth = 0
        end_idx = open_brace_idx
        for i in range(open_brace_idx, len(text)):
            ch = text[i]
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    end_idx = i + 1
                    break
        if depth == 0:
            blocks.append(text[start_idx:end_idx])
    return blocks


def search_files(
    directories: List[Path],
    pattern: str,
    extensions: Tuple[str, ...] = (".txt", ".yml", ".gui"),
    max_results: int = 50,
) -> List[Tuple[Path, int, str]]:
    """Searches files for a regex pattern and returns (path, line_no, line_content)."""
    regex = re.compile(pattern, re.IGNORECASE)
    results = []
    for d in directories:
        if not d.exists():
            continue
        for root, _, files in os.walk(d):
            for file in files:
                if any(file.endswith(ext) for ext in extensions):
                    file_path = Path(root) / file
                    try:
                        content = read_ck3_file(file_path)
                        for line_no, line in enumerate(content.splitlines(), start=1):
                            if regex.search(line):
                                results.append((file_path, line_no, line.strip()))
                                if len(results) >= max_results:
                                    return results
                    except Exception:
                        continue
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description="CK3 source file reader & inspector")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Read sub-command
    read_p = subparsers.add_parser("read", help="Read and print a CK3 file")
    read_p.add_argument("file", type=str, help="Path to CK3 file")
    read_p.add_argument("--lines", type=str, default="", help="Line range, e.g. 10:50")

    # Block sub-command
    block_p = subparsers.add_parser("block", help="Extract balanced block from a file")
    block_p.add_argument("file", type=str, help="Path to CK3 file")
    block_p.add_argument("block_name", type=str, help="Name of block key before ' = {'")

    # Search sub-command
    search_p = subparsers.add_parser("search", help="Search pattern in repo or vanilla")
    search_p.add_argument("pattern", type=str, help="Regex pattern to search")
    search_p.add_argument("--vanilla", action="store_true", help="Search vanilla (ck3-full) instead of mod repo")
    search_p.add_argument("--subpath", type=str, default="", help="Subdirectory inside vanilla/repo to search")
    search_p.add_argument("--max", type=int, default=30, help="Max results")

    args = parser.parse_args()

    if args.command == "read":
        content = read_ck3_file(args.file)
        lines = content.splitlines()
        if args.lines:
            start_str, _, end_str = args.lines.partition(":")
            start = int(start_str) if start_str else 1
            end = int(end_str) if end_str else len(lines)
            selected = lines[max(0, start - 1) : end]
            for idx, line in enumerate(selected, start=start):
                print(f"{idx}: {line}")
        else:
            print(content)

    elif args.command == "block":
        content = read_ck3_file(args.file)
        blocks = find_block(content, args.block_name)
        if not blocks:
            print(f"No block found for '{args.block_name}' in {args.file}", file=sys.stderr)
            return 1
        for idx, b in enumerate(blocks, start=1):
            if len(blocks) > 1:
                print(f"# Block {idx} of {len(blocks)}:")
            print(b)

    elif args.command == "search":
        if args.vanilla:
            dirs = [d / args.subpath if args.subpath else d for d in DEFAULT_VANILLA_DIRS if d.exists()]
            if not dirs:
                print("Vanilla directory not found.", file=sys.stderr)
                return 1
        else:
            repo_root = Path(__file__).resolve().parent.parent
            target_dir = repo_root / args.subpath if args.subpath else repo_root
            dirs = [target_dir]

        results = search_files(dirs, args.pattern, max_results=args.max)
        if not results:
            print(f"No matches for pattern '{args.pattern}'", file=sys.stderr)
            return 1
        for fpath, lno, line in results:
            print(f"{fpath}:{lno}: {line}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
