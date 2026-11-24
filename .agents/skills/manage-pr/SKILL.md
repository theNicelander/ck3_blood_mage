---
name: manage-pr
description: >-
  Finish change: branch doc, release note, commit, push, PR create/edit/merge.
  Use when updating docs-ai/branch-context/<branch>.md, PR title/body, or commit.
---

# Finish change / manage PR

## Checklist

1. Sync matching `docs-ai/architecture/` doc to current state.
2. Capture any non-obvious discovery (vanilla/engine quirk, silent failure, error signature, mod gotcha) into the owning localized `AGENTS.md`, `docs-ai/architecture/` doc, `.agents/rules/`, or `.agents/skills/` (or propose a new skill if none fits).
3. Update `docs-ai/branch-context/<branch>.md` (create if missing) to net branch state.
4. Player-facing change → update `RELEASE_NOTES.md` (skill `update-release-notes`).
5. Run `python3 scripts/check_repo.py` (`--fix` only for BOM/newline) and `git diff --check`.
6. **Commit & push every turn**: stage only your files (never `git add .`/`-A`/`-a`), commit, and push `<branch>` before ending any turn that edited files (parallel agents share tree; follow-ups = new commit).
7. Ensure PR exists: if branch doc lacks `PR: #<N>`, create/find PR and record it. Before creating/editing PR, audit `git log origin/main..HEAD --oneline` + branch doc so PR **title and body** cover *all* commits on the branch (including parallel agents' work).
8. Summary: flag unverified runtime UI/AI behavior; audit logs via skill `debug-ck3-logs`.

## Branch doc = PR body (`.github/pull_request_template.md`)

```md
# <branch>: <outcome title>
PR: #<N>
## Motivation
- 1-3 bullets: problem/balance/constraint
  - Nest mechanical impact (no script details).
## Changes
### Key changes
- **Feature / system** (`bm_id` only to locate code): 1-line summary
  - Nest each distinct sub-change, option, cost, cooldown, math, XP, or AI rule (use 2-space indent; omit unchanged).
### Other changes
- Group supporting work (docs sync, icons/GUI, refactors, renames); nest items when >1. Omit if none. Never list loc or incidental BOM cleanup.
```

- **Style**: diff first; net state for fresh reviewer (fold superseded work); **nested bullets only**: break multi-part items into short top-level headlines + indented sub-bullets (1–2 lines/bullet, no wall-of-text bullets); concise; player-facing title `<branch>: <outcome title>` (no raw filenames/PDXscript); no extra sections, test plans, or changelogs.

## PR commands

- Audit: `git log origin/main..HEAD --oneline` vs doc.
- Create: `gh pr create --title "<branch>: <outcome title>" --body-file docs-ai/branch-context/<branch>.md`
- Edit: `gh pr edit <PR> --title ... --body-file docs-ai/branch-context/<branch>.md`
- **Stop after PR**: never auto-merge; show PR link and wait for explicit user approval.
- Merge (ONLY on user ask): `gh pr merge <PR> --squash --body-file <file> --delete-branch` (never local; omit `--subject` to keep `(#<PR>)`).
- Next branch: pull `main`, checkout `v1.21.<N+1>`, `git push -u origin <branch>`, archive old doc to `docs-ai/archive/`, init new branch doc.
