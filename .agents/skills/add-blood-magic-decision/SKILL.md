---
name: add-blood-magic-decision
description: >-
  Add blood magic decision or self-cast interaction.
---

# Add blood magic decision

Context: `docs-ai/architecture/blood-mage-decisions.md`, `blood-mage-interactions.md`, `blood-mage-progression.md`, `blood-mage-story.md`, `blood-mage-lifeforce.md`, [ck3-decisions](../../rules/ck3-decisions.md), [ck3-ai](../../rules/ck3-ai.md).

## Steps

1. Copy neighboring decision in `common/decisions/` or interaction in `common/character_interactions/`.
2. Declare cost once in script value (`common/script_values/`). Never deduct cost in `effect`.
3. Use shared XP/trait effects (`common/scripted_effects/`), never bare `add_trait`.
4. Register in `common/story_cycles/bm_blood_mage_story.txt` for panel display.
5. Set `ai_*` blocks deliberately (`ai_check_interval = 0` if player-only).
6. Add English loc keys: title, `_desc`, `_tooltip`, `_confirm`.
7. Set XP gate and requirements per `blood-mage-progression.md`.
8. Update docs and validate.

## Verify

- Grep new loc keys and decision ID in story cycle list.
- Run `python3 scripts/check_repo.py`.
