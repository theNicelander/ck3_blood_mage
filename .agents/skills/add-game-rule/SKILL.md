---
name: add-game-rule
description: >-
  Add campaign game rule or setting.
---

# Add game rule

Context: `docs-ai/architecture/blood-mage-game-rules.md`, [ck3-scripting](../../rules/ck3-scripting.md).

## Steps

1. Declare rule and settings in `common/game_rules/bm_game_rules.txt`. Existing behavior is default setting.
2. Check in scripted trigger via `has_game_rule = bm_<rule>_<setting>`.
3. English loc: rule title/desc and setting titles/descs (`setting_..._desc`) in `bm_game_rules_l_english.yml`.
4. Update `blood-mage-game-rules.md` and validate.

## Verify

- Settings match script triggers: `grep -rn "bm_<rule>_" common/`.
- Run `python3 scripts/check_repo.py`.
