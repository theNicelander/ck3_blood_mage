---
name: validate-change
description: >-
  Use this skill after any change to this mod to run the repo checks (format
  script, whitespace, ck3-tiger) and to write a final summary that states what
  could not be verified.
---

# Validate a change

## Steps

1. `python3 scripts/check_repo.py`. Add `--fix` only for missing BOM or trailing newline.
2. `git diff --check`.
3. `ck3-tiger` if installed. New errors are blockers. Existing deprecated `ai_potential` and legacy religion loc warnings are known.
4. Final summary lists what could not be verified (in-game UI, AI behaviour, portraits) and asks the user to check `error.log` after a test run.

## Verify

- `check_repo.py` exits 0 and `git diff --check` prints nothing.
- `descriptor.mod` is not in `git status` because of you.
