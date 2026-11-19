---
name: manage-pr
description: >-
  Finish change: branch doc, release note, commit, push, PR create/edit/merge.
  Use when updating docs-ai/branch-context/<branch>.md, PR title/body, or commit.
---

# Finish change / manage PR

## Checklist

1. Sync matching `docs-ai/architecture/` doc to current state.
2. Update `docs-ai/branch-context/<branch>.md` (create if missing) to net branch state.
3. Player-facing change → update `RELEASE_NOTES.md` (skill `update-release-notes`).
4. Run `python3 scripts/check_repo.py` (`--fix` only for BOM/newline) and `git diff --check`.
5. Stage only your files (never `git add .`/`-A`/`-a`), commit, push `<branch>`. Follow-ups = new commit.
6. Ensure PR exists: if branch doc lacks `PR: #<N>`, create/find PR and record it. Update PR body (`gh pr edit`) on fundamental changes.
7. Summary: flag unverified runtime UI/AI behavior; audit `error.log`.

## Branch doc = PR body (`.github/pull_request_template.md`)

```md
# <branch>: <outcome title>
PR: #<N>
## Motivation
- 1-3 bullets: problem/balance/constraint (nested: mechanical impact, no script details).
## Changes
### Key changes
- Bullet per gameplay/system outcome (nested: costs, cooldowns, math, XP, AI; `bm_*` IDs only to locate code; omit unchanged).
### Other changes
- Docs sync, icons/GUI, refactors, renames. Omit if none. Never list loc or incidental BOM cleanup.
```

- **Style**: diff first; net state for fresh reviewer (fold superseded work); bullets only, <2 KB; player-facing title `<branch>: <outcome title>` (no raw filenames/PDXscript); no extra sections, test plans, or changelogs.

## PR commands

- Audit: `git log origin/main..HEAD --oneline` vs doc.
- Create: `gh pr create --title "<branch>: <outcome title>" --body-file docs-ai/branch-context/<branch>.md`
- Edit: `gh pr edit <PR> --title ... --body-file docs-ai/branch-context/<branch>.md`
- **Stop after PR**: never auto-merge; show PR link and wait for explicit user approval.
- Merge (ONLY on user ask): `gh pr merge <PR> --squash --body-file <file> --delete-branch` (never local; omit `--subject` to keep `(#<PR>)`).
- Next branch: pull `main`, checkout `v1.21.<N+1>`, `git push -u origin <branch>`, archive old doc to `docs-ai/archive/`, init new branch doc.
