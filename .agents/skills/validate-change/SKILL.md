---
name: validate-change
description: >-
  Run repository format checks and state unverified runtime behaviors.
---

# Validate a change

Run checks on every change.

## Steps

1. Run format check: `python3 scripts/check_repo.py`. Pass `--fix` only for missing BOM or trailing newline. Branch-context failure: write the file per [pr-context](../../rules/pr-context.md).
2. Check whitespace and git status: `git diff --check`.
3. In final summary, list what was not verified (runtime UI, AI behavior, portraits) and check `~/Documents/Paradox\ Interactive/Crusader\ Kings\ III/logs/error.log`.
4. Commit relevant files: stage and commit ONLY files modified in this task (`git add <file1> <file2> && git commit -m "..."`). Plans must always conclude with committing; subsequent feedback or modifications belong in separate commits.

## Verify

- `python3 scripts/check_repo.py` passes with exit code 0.
- `descriptor.mod` untouched.
