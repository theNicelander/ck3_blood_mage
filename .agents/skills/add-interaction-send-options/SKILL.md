---
name: add-interaction-send-options
description: >-
  Add or refactor character interaction with exclusive modal send_option choices in CK3 1.20.
---

# Add interaction send options

Canonical mod ref: `common/character_interactions/bm_blood_blessing.txt` (vanilla: `00_diarch_interactions.txt`).

`send_options_exclusive = yes` opens a modal radio-choice window before sending.

## Rules

- Each `send_option` needs: `flag = <id>` (checked as `scope:<id> = yes` in `cost`/`on_send`/`on_accept`), `can_invalidate_interaction = yes`, `localization = <key>`, `current_description = <key_desc>`, `is_shown`, `is_valid`, `starts_enabled` (pre-select most relevant unlocked option).
- Variable `cost`: guard per option with `if = { limit = { scope:<id> = yes } value = ... }`.
- **AI option scoring + empty-set veto (mandatory)**: CK3 AI evaluates flag combinations including `{}` (all `no`). Score each option in `ai_will_do` (`modifier = { scope:<id> = yes add = N }`) and **end** `ai_will_do` with:
```ck3
modifier = {
	NOR = { scope:opt_a = yes  scope:opt_b = yes }
	factor = 0
}
```
- **Branch logs in `on_accept`**: emit structured `debug_log` (see `common/character_interactions/AGENTS.md`) inside each `if`/`else_if` branch, plus `else` logging `(NO OPTION)` fallback.
