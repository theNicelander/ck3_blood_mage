---
trigger: always_on
description: MANDATORY docs-ai/branch-context/<branch>.md on every non-main branch. Create if missing, update every task.
---

# Branch context (MANDATORY)

File: `docs-ai/branch-context/<branch>.md` (`<branch>` = `git branch --show-current`). Survives context resets. `scripts/check_repo.py` fails if missing, or unchanged while the branch changes mod files.

1. **Task start**: read it. Missing? Create from template before coding.
2. **Task end**: update it with `CHANGELOG.md`. One branch = one changelog line = one file.
3. **Content**: mechanics, numbers, trade-offs, decisions. Net branch state only: fold superseded, drop reverted.
4. **Never skip**: not for small changes, not if unasked. Fix stale parts.

```markdown
# <branch>: <title>

## Summary & Motivation

## Core Concepts & Changes
- **Feature**: behavior, integration points.

## Key Decisions
- **Decision**: chose X over Y because Z.
```
