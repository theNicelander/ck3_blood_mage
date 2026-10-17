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
5. **Stay in branch**: never create or switch branches unless explicitly ordered. Other AIs edit other files concurrently in the workspace: stage and commit ONLY files modified in your active conversation. Leave other files untouched and uncommitted; never create separate branches to isolate work.
6. **Plans and commits**: Plans must always include committing as the final step. Since plans are well thought out, commit the completed implementation upon finishing the plan. Any subsequent modifications or user feedback iterations must be in a separate commit. Stage and commit ONLY files modified in your active conversation (`git add <file1> <file2>`), never blanket staging, because multiple agents operate in parallel.

```markdown
# <branch>: <title>

## Summary & Motivation

## Core Concepts & Changes
- **Feature**: behavior, integration points.

## Key Decisions
- **Decision**: chose X over Y because Z.
```
