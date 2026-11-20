---
name: nice-pr
description: >-
  Create or update the GitHub PR for the current branch from docs-ai/branch-context/<branch>.md.
disable-model-invocation: true
---

# nice-pr

Create or update the GitHub PR for the current branch using `docs-ai/branch-context/<branch>.md`.

## Steps

1. **Branch check**: run `git branch --show-current`. Abort if on `main` or detached `HEAD`.
2. **Check PR status**: run `gh pr view --json number,url,title,state` (or `gh pr list --head <branch> --state open --json number,url`).
3. **If PR exists**:
   - Read `docs-ai/branch-context/<branch>.md`. If missing, stop and tell the user.
   - Extract title from line 1 (`# <branch>: <outcome title>` → strip `# `).
   - Ensure `PR: #<N>` is on line 2 if missing; if edited, `git add docs-ai/branch-context/<branch>.md`, commit, and push.
   - Run `gh pr edit <N> --title "<title>" --body-file docs-ai/branch-context/<branch>.md`.
4. **If no PR exists**:
   - Ensure branch is pushed (`git push -u origin <branch>` if needed).
   - Read `docs-ai/branch-context/<branch>.md`; if missing, create it from `git log origin/main..HEAD --oneline` and `git diff origin/main...HEAD` following `.github/pull_request_template.md` (`<2 KB`, bullets only, net branch state).
   - Extract title from line 1 (`# <branch>: <outcome title>` → strip `# `).
   - Run `gh pr create --base main --title "<title>" --body-file docs-ai/branch-context/<branch>.md`.
   - Record `PR: #<N>` on line 2 of `docs-ai/branch-context/<branch>.md` if missing, then `git add docs-ai/branch-context/<branch>.md`, commit, and push.
5. **Finish**: output the PR URL. Never auto-merge.
