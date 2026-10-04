---
name: add-game-rule
description: >-
  Use this skill when adding a game rule or a rule setting to the Blood Mages
  mod.
---

# Add a game rule

Read first: `docs-ai/architecture/blood-mage-game-rules.md` and [ck3-scripting](../../rules/ck3-scripting.md).

## Steps

1. Add the rule and its settings in `common/game_rules/bm_game_rules.txt`.
2. Existing behaviour is the default setting.
3. Check it with `has_game_rule = bm_<rule>_<setting>`, inside a scripted trigger.
4. English loc for the rule and each setting (`setting_..._desc`) in `bm_game_rules_l_english.yml`.
5. Update the game-rules doc (`update-docs`), then `validate-change`.

## Verify

- Each setting name used in script appears in the rule file and the loc file.
