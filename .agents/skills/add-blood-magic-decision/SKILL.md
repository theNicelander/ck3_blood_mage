---
name: add-blood-magic-decision
description: >-
  Add blood magic decision or self-cast interaction.
---

# Add blood magic decision

Context: `docs-ai/architecture/blood-mage-decisions.md`, `blood-mage-interactions.md`, `blood-mage-track-xp*.md`, `blood-mage-story.md`, `blood-mage-lifeforce.md`, [ck3-decisions](../../rules/ck3-decisions.md), [add-decision-option-widget](../add-decision-option-widget/SKILL.md).

## Steps

1. Copy neighboring decision in `common/decisions/` or interaction in `common/character_interactions/` (for multi-choice inline option-list UI widgets, follow [add-decision-option-widget](../add-decision-option-widget/SKILL.md)).
2. Declare cost once in script value (`common/script_values/`). Never deduct cost in `effect`.
3. Use shared XP/trait effects (`common/scripted_effects/`), never bare `add_trait`.
4. Register in `common/story_cycles/bm_blood_mage_story.txt` for panel display.
5. Set `ai_*` blocks deliberately (`ai_check_interval = 0` if player-only).
6. Add English loc keys: title, `_desc`, `_tooltip`, `_confirm`. Keep text concise and direct: use concrete terms like "Lifeforce" instead of vague flavour ("vitality", "life essence"). Confine flavour text strictly to narrative descriptions.
7. For interactions, copy the category's standard fiery blood drop DDS (`grant_blood_magic_interaction.dds`) to `gfx/interface/icons/character_interactions/<name>.dds`. If removing or renaming an interaction, remove/rename the matching `.dds`.
8. Set XP gate and requirements per `blood-mage-track-xp*.md`. For options in events and decisions, follow the 'Nothing hidden, but often unavailable' philosophy: use `show_as_unavailable` so players can see options and unmet requirements grayed out, rather than hiding them silently (hide only if a prerequisite tier is unreached or an option has been permanently completed).
9. Finish via skill `manage-pr`.

## Verify

- Grep new loc keys and decision ID in story cycle list.
- Run `python3 scripts/check_repo.py`.
