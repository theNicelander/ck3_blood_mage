---
name: update-docs
description: >-
  Keep architecture docs and branch context current after code or balance changes.
---

# Update docs

Keep docs true to current state. No history or changelogs in architecture docs.

## Steps

1. Find affected doc via [index](../../../docs-ai/architecture/README.md).
2. Update specs: costs, requirements, cooldowns, XP gains, benefits. Format per [architecture AGENTS.md](../../../docs-ai/architecture/AGENTS.md).
3. If adding or removing doc, update `AGENTS.md` table and `README.md` index.
4. Update `docs-ai/branch-context/<branch>.md` (Summary, Concepts, Decisions) per [pr-context](../../rules/pr-context.md). Ignore minor edits.

## Verify

- Identifiers exist: `grep -rn "<id>" common/ events/ gui/ localization/english/`.
- Docs reflect current script values and triggers exactly.
