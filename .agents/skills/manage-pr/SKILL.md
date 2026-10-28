---
name: manage-pr
description: >-
  Finish change: branch doc, release note, commit, push, PR create/edit/merge.
  Use when updating docs-ai/branch-context/<branch>.md, PR title/body, or commit.
---

# Finish change / manage PR

## Finish checklist

1. Architecture doc (`docs-ai/architecture/README.md`) matches current state.
2. `docs-ai/branch-context/<branch>.md` reflects net branch state (format below). Create if missing.
3. Player-facing change: one line in `RELEASE_NOTES.md` (skill `update-release-notes`).
4. `python3 scripts/check_repo.py` (`--fix` only for BOM/newline) and `git diff --check`.
5. Stage only changed files (never `git add .`/`-A`/`-a`), commit, push to `<branch>`. Commit immediately when task done. Follow-ups = separate commit.
6. Summary: state unverified runtime UI/AI behavior. Audit `error.log`.

## Branch doc = PR body

`docs-ai/branch-context/<branch>.md` is PR description. Shape follows `.github/pull_request_template.md`:

```md
# <branch>: <outcome title>

## Motivation

- 1–3 bullets: problem, balance issue, engine limit, overhaul constraint.
  - Nested: mechanical impact, in-game example. No script details here.

## Changes

### Key changes

- Top-level bullet per gameplay/system outcome (traits, XP, Lifeforce, decisions, interactions, events, faiths).
  - Nested: costs, cooldowns, math, XP yields, AI weights. Name `bm_*` ids only to locate code.
  - Never list unchanged mechanics.

### Other changes

- Supporting work: `docs-ai/architecture/` syncs, icon/GUI, refactors, script renames.
- Omit section if no supporting changes.
- Never mention localization (always expected). Skip incidental formatting/BOM cleanup.
```

## Rules & style

- **Diff first**: review final diff before writing; describe net state for fresh reviewer; fold superseded work.
- **Bullets only**: short lines, nested details. Scale detail to complexity. Keep under ~2 KB.
- **Title**: `<branch>: <outcome title>`. Player-facing imperative/noun phrase. No raw script filenames or low-level PDXscript.
- **Avoid**: extra sections, test plans, changelogs, file-by-file accounts, conversational history.

## PR lifecycle

- Audit: `git log origin/main..HEAD --oneline` vs doc before PR.
- Body: branch doc minus `#` title line.
- Create: `gh pr create --title "<branch>: <outcome title>" --body-file docs-ai/branch-context/<branch>.md`
- Edit: `gh pr edit <PR> --title ... --body-file docs-ai/branch-context/<branch>.md`
- Merge: `gh pr merge <PR> --squash --body-file <file> --delete-branch`. Never merge locally; omit `--subject` so GitHub preserves `(#<PR>)`.
- Next branch: pull `main`, checkout sequential `v1.20.<N+1>`, push `-u origin <branch>`, archive old doc to `docs-ai/archive/`, init new branch doc.
