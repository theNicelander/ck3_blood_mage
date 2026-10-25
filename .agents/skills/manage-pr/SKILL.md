---
name: manage-pr
description: >-
  Finish a change: write the branch doc, release note, commit, push, and create/update/merge the PR.
  Use when writing docs-ai/branch-context/<branch>.md, a PR title/body, or a commit message.
---

# Finish a change / manage PR

## Finish checklist (every task)

1. Architecture doc for the touched subsystem (`docs-ai/architecture/README.md` index) matches the new current state.
2. `docs-ai/branch-context/<branch>.md` reflects net branch state (format below). Create if missing.
3. Player-facing change: one line in `RELEASE_NOTES.md` (skill `update-release-notes`).
4. `python3 scripts/check_repo.py` (`--fix` only for BOM/newline) and `git diff --check`.
5. Stage only files you changed (never `git add .`/`-A`/`-a`), commit, `git push origin <branch>`. Follow-up work = separate commit.
6. Final summary: say what was not verified (runtime UI, AI behaviour). Check `error.log` when relevant.

## Branch doc = PR body

`docs-ai/branch-context/<branch>.md` is the PR description. Shape follows `.github/pull_request_template.md`:

```md
# <branch>: <outcome title>

## Motivation

- 1–3 bullets: problem or goal.

## Changes

- One sentence per bullet: behaviour, not files.
```

- Net state for a reviewer who has not seen the conversation; fold superseded work, drop reverts.
- No mechanic numbers (they live in architecture docs), no file-by-file account, no extra sections.
- Name files/identifiers only when they help locate the code.
- Include material compatibility, migration, or limitation notes as a bullet.
- Keep under ~2 KB; scale to complexity.

## PR

- Before create/update/merge: compare the doc with `git log origin/main..HEAD --oneline`; fix the doc if a feature is missing.
- Title: short imperative outcome, player-facing (`Rework Blood Temples as duchy buildings`). No version prefix, theme lists, or file names. Docs/tooling-only branches may say so.
- Body: the branch doc minus its `#` heading line.
- `gh pr create --title "<Title>" --body-file <file>` / `gh pr edit <N> --title ... --body-file ...`.
- Merge commit message: PR title plus the Changes bullets.
- State validation only if actually performed.
