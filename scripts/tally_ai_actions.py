#!/usr/bin/env python3
"""Tally AI Blood Mage actions from debug.log (BloodMageInteraction lines)."""
import re
import sys
from collections import Counter

LINE = re.compile(r"BloodMageInteraction: (\w+) \((\w+)\) \| Actor: .*?, (Player|AI)\) -> Recipient: .*?, (Player|AI)\) \| Rel: (.*?) \| Tag:")


def main(path):
    by_action = Counter()
    by_rel = Counter()
    with open(path, encoding="utf-8-sig", errors="replace") as f:
        for line in f:
            m = LINE.search(line)
            if not m or m.group(3) != "AI" or m.group(2) == "NO OPTION":
                continue
            name, opt, _, _, rel = m.groups()
            by_action[(name, opt)] += 1
            by_rel[(name, "self" if rel.strip() in ("", "Self", "self") else rel.strip())] += 1
    total = sum(by_action.values()) or 1
    print("AI actions (interaction, option): count, share")
    for k, v in by_action.most_common():
        print(f"  {k[0]} ({k[1]}): {v} ({100 * v / total:.0f}%)")
    print("By target relation:")
    for k, v in by_rel.most_common(25):
        print(f"  {k[0]} -> {k[1]}: {v}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("usage: tally_ai_actions.py <debug.log>")
    main(sys.argv[1])
