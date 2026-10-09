---
trigger: model_decision
description: Track branch and PR state, core concepts, and key decisions in docs-ai/branch-context/<branch>.md.
---

# Branch and PR context tracking

High-level context and decision log across context resets.

## Guidelines

1. **Read first**: Check `docs-ai/branch-context/<branch>.md` before modifying code.
2. **Track major state only**: Record mechanics, features, trade-offs, and decisions. Ignore renames, formatting, and trivial bug fixes.
3. **Keep current**: Update file when adding features or making design choices.

## Structure

```markdown
# [Branch Name / PR Name]

## Summary & Motivation
Core purpose and goals.

## Core Concepts & Changes
- **Feature/Concept**: Functional behavior and integration points.
- **System Change**: Rebalanced systems or rewritten flows.

## Key Decisions
- **Decision 1**: Chose X over Y because Z.
- **Decision 2**: Restricted A to B because C.
```
