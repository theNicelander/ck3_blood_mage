---
name: manage-pr
description: >-
  Create, update, or merge PRs and compose commit messages while verifying branch context documents.
---

# Manage PR

Ensure pull requests, updates, and merge commit messages comprehensively reflect the full scope of work across the branch history without dropping parallel features.

## When to use

- Creating a new PR (`gh pr create`).
- Updating an existing PR title or description (`gh pr edit`).
- Merging a PR and authoring the merge commit message.

## Procedure

### 1. Audit Branch Context & Git History
- Identify current branch: `git branch --show-current`.
- Read the branch document: `docs-ai/branch-context/<branch>.md`.
- Inspect git history against base branch: `git log origin/main..HEAD --oneline` and `git diff --stat origin/main..HEAD`.
- Verify: Does `docs-ai/branch-context/<branch>.md` account for EVERY commit and feature introduced in this branch?
- If the branch document is missing any changes, update `docs-ai/branch-context/<branch>.md` to reflect the complete net state before touching the PR.

### 2. Formulate Comprehensive PR Title and Body
- **Title**: High-level, high-impact summary covering all core gameplay themes of the branch (e.g., `v1.20.51: Empower Dynasty Bloodline Overhaul, Blood Knight Parity, 4-Tier Blood Hunts & Audit Fixes`). Do not focus on only a single commit if multiple areas were modified.
  - **Gameplay Content Only (No Meta Fluff)**: Unless the branch is **EXCLUSIVELY** about documentation, AI rules, or dev tooling, PR titles and merge commit headers must focus strictly on **player-facing gameplay changes**. Never include PR workflow, branch verification, AI rule updates, or documentation meta in the title/heading (e.g. exclude "PR Workflow & Branch Verification" from headers). What matters in PR titles is gameplay content; meta changes belong strictly in bullet points within the body.
- **Description / Body**:
  - Pull directly from `docs-ai/branch-context/<branch>.md`.
  - Group into clear structural sections (e.g., Summary & Motivation, Core Concepts & Changes by subsystem/theme, Key Decisions, Audit & Bug Fixes).
  - Terse, dense presentation (`.agents/skills/caveman/SKILL.md`): all facts and mechanics kept, zero fluff.
  - Never omit parallel commits, sub-features, or earlier work streams on the branch.

### 3. Creating or Updating PR
- Create: `gh pr create --title "<Title>" --body "<Body>"`
- Update: `gh pr edit <PR_NUMBER> --title "<Title>" --body "<Body>"`

### 4. Authoring Merge Commit Messages
- When merging to `main` (squash merge or merge commit), the commit message body must incorporate the synthesized branch summary from `docs-ai/branch-context/<branch>.md`.
- Never allow GitHub or git CLI default truncated 1-line messages to wipe out branch context.
