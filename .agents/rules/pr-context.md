---
trigger: always_on
description: MANDATORY docs-ai/branch-context/<branch>.md on every non-main branch. Create if missing, update every task.
---

# Branch context (MANDATORY)

File: `docs-ai/branch-context/<branch>.md` (`<branch>` = `git branch --show-current`). Survives context resets. `scripts/check_repo.py` fails if missing, or unchanged while the branch changes mod files.

1. **Task start**: read it. Missing? Create from template before coding.
2. **Task end**: update it with `CHANGELOG.md` (and `RELEASE_NOTES.md` if player-facing features or bugfixes changed). One branch = one changelog line = one file.
3. **Content**: mechanics, numbers, trade-offs, decisions. Net branch state only: fold superseded, drop reverted.
4. **Never skip**: not for small changes, not if unasked. Fix stale parts.
5. **Stay in branch**: never create or switch branches unless explicitly ordered. Other AIs edit other files concurrently in the workspace: stage and commit ONLY files modified in your active conversation. Leave other files untouched and uncommitted; never create separate branches to isolate work.
6. **Plans and commits**: Plans must always include committing as the final step. Since plans are well thought out, commit the completed implementation upon finishing the plan. Any subsequent modifications or user feedback iterations must be in a separate commit. Stage and commit ONLY files modified in your active conversation (`git add <file1> <file2>`), never blanket staging, because multiple agents operate in parallel.
7. **Creating, Updating, and Merging PRs**:
   - **Mandatory Branch Document Verification**: Anytime you create a PR, update a PR, or merge a PR, you MUST first inspect `docs-ai/branch-context/<branch>.md` and verify it against `git log origin/main..HEAD --oneline` (and `git diff --stat origin/main..HEAD`).
   - **Ensure Accuracy & Completeness Before Touching PR**: Confirm that `docs-ai/branch-context/<branch>.md` accurately and comprehensively covers ALL features, reworks, mechanics, and bugfixes introduced across all commits in the branch. If incomplete or stale, update the branch context document first.
   - **Full Branch Scope Synthesis**: The PR title, description, and merge commit message MUST synthesize all changes across the branch's complete lifetime as recorded in `docs-ai/branch-context/<branch>.md`. Never truncate or summarize only the most recent commit or sub-task. Every major feature, interaction, trait addition, and mechanic overhaul on the branch must be clearly represented.
   - **Gameplay Focus (No Meta Fluff in Titles/Headings)**: Unless a branch is **EXCLUSIVELY** about documentation, agent rules, or tooling, PR titles, main headings, and merge commit titles MUST focus strictly on **player-facing gameplay content**. Ignore PR workflow, branch verification, AI rules, and documentation meta in titles and headings—that is unimportant fluff. (E.g. exclude "PR Workflow & Branch Verification" from titles). Meta details belong strictly in bullet points within the description body, never in the heading.
   - **High-Impact Presentation**: Follow skill `manage-pr` (`.agents/skills/manage-pr/SKILL.md`). Use the `caveman` skill (`.agents/skills/caveman/SKILL.md`) for dense presentation: lead with high-impact gameplay overhauls (traits, events, rites, core mechanics), while keeping all parallel work streams and technical facts intact.

```markdown
# <branch>: <title>

## Summary & Motivation

## Core Concepts & Changes
- **Feature**: behavior, integration points.

## Key Decisions
- **Decision**: chose X over Y because Z.
```
