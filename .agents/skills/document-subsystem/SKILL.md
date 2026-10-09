---
name: document-subsystem
description: >-
  Create or rewrite an architecture doc in docs-ai/architecture/.
---

# Document a subsystem

Format: [architecture AGENTS.md](../../../docs-ai/architecture/AGENTS.md). High-density technical spec. No roleplay, no fluff.

## Steps

1. Target file: `docs-ai/architecture/blood-mage-<subsystem>.md`.
2. Required sections in order:
   - **Executive Summary**: 1–2 line core definition, acquisition method, advancement rules, compact data table (tracks/levels, costs, base step, milestones).
   - **Key Mechanics**: Decisions, interactions, rosters, gates. Include explicit costs, cooldowns, requirements, XP gains, benefits.
   - **Where the details live**: Concept-to-file path table.
   - **Gotchas**: Script edge cases, engine traps, ordering bugs.
   - **Not verified**: Unverified runtime/AI behaviors.
3. Check `localization/english/` for identifiers before writing.
4. Register doc in `docs-ai/architecture/AGENTS.md` and `README.md`.

## Verify

- Identifiers and paths exist: `grep -rn "<id>" common/ events/ gui/ localization/english/`.
- Doc listed in `AGENTS.md` table and `README.md` index.
