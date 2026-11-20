# Game Rules (`common/game_rules/`)

Spec: `docs-ai/architecture/blood-mage-game-rules.md`.

- Declare rule/settings in `bm_game_rules.txt`; existing behavior = default setting.
- Check via `has_game_rule = bm_<rule>_<setting>` in scripted triggers.
- English loc in `bm_game_rules_l_english.yml` (rule title/desc + setting titles/`setting_..._desc`).
- Update `blood-mage-game-rules.md`; verify via `grep -rn "bm_<rule>_" common/` + `scripts/check_repo.py`.
