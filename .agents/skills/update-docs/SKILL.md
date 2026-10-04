---
name: update-docs
description: >-
  Use this skill after changing script, localization or behaviour, to keep the
  architecture docs and the branch context file true to the current state.
---

# Update docs

## Steps

1. Map changed paths to docs with [the index](../../../docs-ai/architecture/README.md).
2. Rewrite the affected text to describe the current state: no history, no tunable numbers. Format rules are in [architecture AGENTS.md](../../../docs-ai/architecture/AGENTS.md).
3. If a doc was added or removed, update the doc table in that `AGENTS.md` and the `README.md` index.
4. Update `docs-ai/branch-context/<branch>.md` (Summary & Motivation, Core Concepts, Key Decisions) per [pr-context](../../rules/pr-context.md). Skip renames and minor fixes.

## Verify

- Every identifier named in the edited docs exists: `grep -rn "<identifier>" common events gui localization/english`.
- No numbers for costs, chances or thresholds were added.
