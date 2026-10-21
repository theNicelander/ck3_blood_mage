---
trigger: always_on
description: Core CK3 script rules, script values, and safe engine patterns (1.20).
---

# CK3 scripting

1. **No invented syntax**: CK3 fails silently. Confirm triggers, effects, scopes in vanilla 1.20 (`/Users/clarabotet/Petur/ck3-full`) or `script_docs`.
2. **Percentages**: `random = { chance = N }` and trait `birth` / `random_creation` use percent values (`0.25` = 0.25%).
3. **Scope navigation**: `prev` traverses one level only. Use `save_scope_as` for deep targets.
4. **Null safety**: Guard nullable targets (`liege`, `spouse`, `scope:x`) with `?=` or `exists`.
5. **Mod compatibility**: Non-vanilla keys error without target mod. Guard via global variables (`AGOT_is_loaded`) or doctrine parameters.
6. **Trait audit**: Verify traits and diseases against vanilla 1.20 before writing `has_trait`.
7. **Game rules**: Any non-default behavior requires a game rule. Existing behavior remains default.
8. **Script values**:
   - Centralize numbers used in 2+ locations in `common/script_values/`.
   - Values evaluate in caller's scope. Document scope dependencies in comments.
   - UI-bound values must stay cheap (no iterators/triggers). Use `save_temporary_value_as`.
   - Never use random ranges in costs: re-evaluated every tick.
   - Loc formatting: `[GetPlayer.MakeScope.ScriptValue('x')|0]`.
9. **Inspection**:
   - Files require UTF-8 with BOM (`utf-8-sig`).
   - Use `python3 scripts/read_ck3.py {read|block|search}` to inspect vanilla 1.20 and mod files safely.
10. **Interface Toasts (`send_interface_toast`)**:
   - In events and decisions, anything that grants or alters modifiers (character, house, county, lifeforce stacks), traits (lifestyles, education, congenital, injury/illness), XP, or stats MUST be enclosed inside `send_interface_toast = { ... }`.
   - When rolling outcomes (duels, `random_list`, random chance) that grant lifeforce, traits, or modifiers, the rewards must be granted inside the interface toast so the player sees what was rolled and awarded.
   - Never grant lifeforce modifiers, traits, or stat gains nakedly in event `option` blocks or decision `effect` blocks without `send_interface_toast`.
   - Effects placed outside the toast block are invisible in the popup toast. Always include `hidden_effect = { bm_recount_lifeforce_stacks_effect = yes }` inside the toast when lifeforce changes.
   - Avoid `custom_tooltip` inside toasts when native effects are present, as `custom_tooltip` overrides and hides the game's automatic effect formatting.
11. **Option Visibility (`show_as_unavailable`)**:
   - Keep options visible and grayed out (`show_as_unavailable = { ... }`) whenever possible so players see what exists and what requirements (Lifeforce, Piety, Devotion, Cooldown) are needed to unlock them.
   - Only hide an option completely if its prerequisite tier/stage has not been reached or if it has been permanently completed or superseded.

## Common Engine Errors & Pitfalls

> [!IMPORTANT]
> **Living Catalog Requirement**: Whenever you identify or resolve a new engine error, silent script failure, data-binding error, or syntax pitfall during log reviews or playtests, **you must update this catalog** with the exact error signature, cause, and required fix pattern so future agents do not repeat it.

1. **Trigger `custom_description` Scoping & Loc (`Failed to find type 'recipient'`)**:
   - *Error*: `[pdx_data_localize.cpp:146]: Data error in loc string ...` with `Failed to find type 'recipient'`.
   - *Cause*: In trigger evaluation (`is_valid`, `is_shown`, `is_valid_showing_failures_only`), `recipient` is not a promoted root type in the data system.
   - *Fix*: Always pass `subject = scope:recipient` (or `scope:actor`) in `custom_description = { ... }`. In the localization string, reference `[CHARACTER.GetShortUIName]` (which binds to `subject`) or `[TARGET_CHARACTER.GetShortUIName]` (which binds to `object`). Never use bare `[recipient.GetShortUIName]` in trigger tooltips.
2. **Event Option Block Keywords vs Triggers (`Unknown trigger: show_as_unavailable`)**:
   - *Error*: `[pdx_persistent_reader.cpp:216]: Error: "Unknown trigger: show_as_unavailable"`.
   - *Cause*: Nesting `show_as_unavailable = { ... }` inside `trigger = { ... }`.
   - *Fix*: In CK3 events, `show_as_unavailable = { ... }` is an option-level directive, a sibling to `trigger = { ... }` directly inside `option = { ... }`. Never put it inside the `trigger` block.
3. **Event Themes (`Theme key X does not exist in event theme database`)**:
   - *Error*: `[event_theme_database.cpp:56]: Theme key X in event Y does not exist in the event theme database`.
   - *Cause*: Inventing theme names (e.g. `romance`, `occult`).
   - *Fix*: Confirm theme keys against vanilla `common/event_themes/00_event_themes.txt`. Valid themes include: `love`, `seduction`, `marriage`, `family`, `dynasty`, `friendly`, `unfriendly`, `war`, `dread`, `corruption`, `witchcraft`, `physical_health`, `mental_health`, `skull`, `medicine`, `plague`, `faith`, `dungeon`, `travel`.
4. **Unsafe Object/Scope Navigation (`primary_heir returned an unset scope`)**:
   - *Error*: `[jomini_script_system.cpp:304]: Event target link 'primary_heir' returned an unset scope`.
   - *Cause*: Direct comparison `this = scope:actor.primary_heir` when `scope:actor` is unlanded or has no primary heir.
   - *Fix*: Use the native CK3 character trigger `is_primary_heir_of = scope:actor` or null-safe check `scope:actor ?= { primary_heir ?= { this = scope:recipient } }`.
5. **Debug Log Execution in Tooltip Mode (`Character '(no character)' is not valid`)**:
   - *Error*: `[character.cpp:750]: Character '(no character)' is not valid in '...'` triggered from `debug_log`.
   - *Cause*: Scripted effects evaluate during option tooltip generation or empty loops (e.g. `every_prisoner`) where `scope:victim` or targets may be null or unset, executing data functions like `SCOPE.sC('victim').Custom2(...)`.
   - *Fix*: Always wrap `debug_log` blocks involving targeted characters inside `if = { limit = { exists = scope:victim exists = scope:executioner } ... }`.
6. **No Hexadecimal Escapes in Localization (`Illegal localization break character ('x')`)**:
   - *Error*: `[localization_reader.cpp:111]: Illegal localization break character ('x')`.
   - *Cause*: Pasting Python raw escape sequences like `\x27` into `.yml` files.
   - *Fix*: CK3 YAML does not interpret hex escape sequences. Use literal `'` for apostrophes.
7. **Dangling Modifier & Database Object References (`Invalid database object 'x'`)**:
   - *Error*: `[jomini_script_system.cpp:304]: Script system error! Error: has_character_modifier trigger [ Invalid database object 'x' ]`.
   - *Cause*: Deleting a modifier from `common/modifiers/` while leaving lingering checks in scripted triggers (`bm_attunement_triggers.txt`), effects (`remove_character_modifier`), or customizable localization.
   - *Fix*: When deprecating or removing any database object (modifier, trait, flag, variable), grep the entire repository and cleanly purge all references across triggers, effects, custom loc, and localization in the same commit.

Mod architecture: see `docs-ai/architecture/README.md`.
