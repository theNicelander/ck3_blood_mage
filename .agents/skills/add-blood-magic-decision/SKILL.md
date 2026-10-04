---
name: add-blood-magic-decision
description: >-
  Use this skill when adding a new blood magic decision or self-cast
  interaction to the Blood Mages mod.
---

# Add a blood magic decision

Read first: `docs-ai/architecture/` docs `blood-mage-decisions.md`, `blood-mage-interactions.md`, `blood-mage-progression.md`, `blood-mage-story.md`, `blood-mage-lifeforce.md`, and rules [ck3-decisions](../../rules/ck3-decisions.md), [ck3-ai](../../rules/ck3-ai.md).

## Steps

1. Copy the nearest decision in `common/decisions/` (or interaction in `common/character_interactions/`) for structure.
2. Declare cost once, in a script value file if reused.
3. Use the shared effects and XP helpers named in the docs, never a raw `add_trait`.
4. Add it to the story's decision list in `common/story_cycles/bm_blood_mage_story.txt` so it shows in the panel.
5. Add `ai_*` blocks deliberately.
6. English loc: title, `_desc`, `_tooltip`, `_confirm`.
7. XP gate and requirement values follow `blood-mage-progression.md`.
8. Run `update-docs`, then `validate-change`.

## Verify

- `grep` each new loc key and the new decision id in the story list.
- `validate-change` passes.
