# CK3 scripting (`common/`)

- **Percentages**: `random = { chance = N }` and trait `birth`/`random_creation` take percents (`0.25` = 0.25%).
- **Scopes**: `prev` walks 1 level; use `save_scope_as` for deep refs. Guard nullable scopes (`liege`, `spouse`, `scope:x`) with `?=` or `exists`.
- **Traits/diseases**: verify keys in vanilla 1.20 before `has_trait`.
- **Game rules**: non-default behavior needs game rule; existing behavior stays default.
- **Script values** (`common/script_values/`): centralize numbers used 2+ places; comment caller scope; keep UI values cheap (`save_temporary_value_as`, no iterators/triggers); never use random ranges in costs (re-evaluated per tick); loc `[GetPlayer.MakeScope.ScriptValue('x')|0]`.
- **Toasts**: omit `custom_tooltip` inside `send_interface_toast` when native effects exist (overrides auto-format).
- **No multi-stack modifier triggers**: `has_character_modifier` only checks presence (`>= 1`). Never write `>= 2` stack checks; gate repeatables with modifier tiers, piety, and timed flags (`add_character_flag = { flag = ... days = 180 }`).
