# Decisions (`common/decisions/`)

Copy neighbor. For inline multi-choice option-list widgets, use skill `add-decision-option-widget`.

- **Cost & validity**: declare `cost` once in `common/script_values/`; never deduct in `effect`. Cheap checks first in `is_shown`. Prefer native `cooldown`. Put affordability in `is_valid`; never skip with `is_ai = yes`. Effects must be idempotent/null-safe.
- **Mod hooks**: use shared XP/trait scripted effects (`common/scripted_effects/`), never bare `add_trait`. Register in `common/story_cycles/bm_blood_mage_story.txt` for panel display.
- **AI**: `ai_check_interval` (months; `0` = player-only), `ai_potential` (hard gate), `ai_will_do` (% chance): put additive `add` first, `factor = 0` vetoes last. Personality: `ai_value_modifier = { ai_greed = 0.5 }` (`ai_boldness|compassion|energy|greed|honor|rationality|sociability|vengefulness|zeal`). Don't raise `base`/shorten intervals without reason; check health/Lifeforce/piety/opinion before harmful acts. State unverified AI frequency in summary.
- **Debug log**: loc promotes on `root` fail in decision `debug_log`. Use plain string + `debug_log_scopes = yes` inside `hidden_effect`.
- **Verify**: grep loc sibling keys (`_desc`, `_tooltip`, `_confirm`) + story cycle entry; run `scripts/check_repo.py`.
