---
trigger: model_decision
description: Capturing and reading high-level branch/PR context, core concepts, and key decisions in docs-ai/branch-context/<pr-name>.md. Read when starting work on a branch or PR, or when updating branch state and decisions.
---

# Branch and PR Context Tracking

This rule ensures that high-level context, core concepts, and key decisions persist across branches and fresh context windows.

## Rule Guidelines

1. **Read First on Every Session**:

   - Before starting work on any branch or PR, always check `docs-ai/branch-context/<pr-name>.md` (named after the pull request or branch, e.g. `docs-ai/branch-context/PR94_CHANGES.md` or `docs-ai/branch-context/<branch_name>.md`).
   - Use this file to understand the current state, goals, and previous decisions before making any changes.

2. **Capture High-Level State on Changes**:

   - When making changes on a branch or PR, keep `docs-ai/branch-context/<pr-name>.md` updated with the current state.
   - Focus on **high-level concept changes**, new additions, and core mechanics.
   - **Ignore trivial edits**: Do not log minor things like renames, moves, formatting, or minor fixes.

3. **Required Document Structure**:
   Every PR/branch doc in `docs-ai/branch-context/` must include:
   - **Summary & Motivation** (at the top): A quick summary of what the PR is and the general motivation behind it.
   - **Changes & Core Concepts**: A list of high-level additions, altered concepts, and system changes.
   - **Key Decisions**: Explicit bullet points recording decisions made (e.g., "We decided to do X because Y") to prevent losing context between sessions.

## Template for `docs-ai/branch-context/<pr-name>.md`

```markdown
# [PR Name / Branch Name]

## Summary & Motivation

A quick summary of what this PR/branch is and the general motivation behind it.

## Core Concepts & High-Level Changes

- **Feature/Concept Added**: High-level explanation of what was introduced.
- **System Change**: Major functional adjustment (omit small renames/moves).

## Key Decisions

- **Decision 1**: We decided X because Y.
- **Decision 2**: We decided A instead of B because C.
```
