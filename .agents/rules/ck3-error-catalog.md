---
trigger: model_decision
description: Known CK3 engine errors and fixes. Read when auditing error.log or debugging silent script failures.
---

# Engine error catalog

Living list: when you resolve a new error, add one line: signature → cause → fix.

| Signature | Cause → Fix |
| --- | --- |
| `Failed to find type 'recipient'` (loc in trigger tooltip) | `recipient` is not a root type in trigger loc. Pass `subject = scope:recipient` in `custom_description`; use `[CHARACTER.GetShortUIName]` (or `[TARGET_CHARACTER...]` with `object`). |
| `Unknown trigger: show_as_unavailable` | Nested inside `trigger`. In events it is a sibling of `trigger` directly in `option`. |
| `Theme key X ... does not exist in the event theme database` | Invented theme. Use vanilla `common/event_themes/00_event_themes.txt` keys (`love`, `family`, `war`, `faith`, `dread`, `witchcraft`, `medicine`, ...). |
| `Event target link 'primary_heir' returned an unset scope` | `this = scope:actor.primary_heir` on heirless actor. Use `is_primary_heir_of = scope:actor` or `scope:actor ?= { primary_heir ?= { ... } }`. |
| `Character '(no character)' is not valid in ...` (`debug_log`) | Effect runs in tooltip/empty loop with unset scopes. Wrap `debug_log` in `if = { limit = { exists = scope:x } }`. |
| `Illegal localization break character ('x')` | `\x27` escapes in `.yml`. Use literal `'`. |
| `Invalid database object 'x'` | Deleted modifier/trait still referenced. Grep and purge triggers, effects, custom loc, loc in the same commit. |
| `Trait X is marked as good but is not a genetic trait` / `random creation chance, but is not genetic` | Remove `good = yes` / `random_creation` from lifestyle traits; use `random_creation_weight = 0`. |
| AI does forbidden interactions despite `factor = 0` | `ai_will_do` evaluates in order; later `add` resurrects the score. Put additive modifiers first, `factor = 0` vetoes last, and add a hard `is_ai` fail in `is_valid_showing_failures_only`. |
| `trigger_else_if with no trigger_else` | End every `trigger_if` chain containing `trigger_else_if` with `trigger_else = { always = no }`. |
| `Unknown trigger: min` (in `modifier`/`ai_will_do`) | `min`/`max` only work in script values. Use `base` + `modifier = { add = ... }` or a script value. |
| `Unknown trigger: employed_as_court_position_of` | Invented. Use `any_court_position_employer = { this = scope:actor }`, `has_court_position`, `has_any_court_position`. |
| `Cannot find blood_golem in trait database` | Golems are `house ?= house:bm_house_golem`, not a trait. |
| `Modifier 'x' was not used by the script or code but exists in the database` | Unused modifier in `common/modifiers/`. Hook it into an effect or delete it and its loc. |
