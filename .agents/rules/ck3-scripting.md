---
trigger: model_decision
description: Repo-specific CK3 scripting rules (shared effects, trait/story, script values, common traps). Read before editing common/ or events/.
---

# CK3 scripting (repo-specific)

Generic syntax is assumed known. If a name's existence is uncertain, grep vanilla `game/` or `script_docs`. Don't guess.

## Always use the shared effects

- Grant the trait with `bm_become_blood_mage_effect = yes`, never bare `add_trait = lifestyle_blood_mage` (it also creates the story cycle behind the Blood Magic panel).
- Anything creating a golem or retinue member goes through the shared golem effects for the same reason.
- XP: `add_trait_xp = { trait = lifestyle_blood_mage track = <discipline> value = N }`.

## Known traps

- `random = { chance = N }` and trait `birth` / `random_creation` are percentages (`0.25` = 0.25%).
- `prev` goes one level back only in this repo's usage. Save scopes (`save_scope_as`) when you need more.
- Dereferencing a possibly empty link (`liege`, `spouse`, `scope:x`): guard with `?=` or `exists`.
- Optional-mod faith/title/trait keys are script errors without that mod. Guard with global variables or doctrine parameters.
- Verify trait and ailment names against vanilla 1.19 before using them in `has_trait`.
- New default-changing behaviour needs a game rule, with existing behaviour as default.

## Script values

- Make one for any number used in 2+ places. Files: `bm_*_piety_cost.txt`, `bm_xp_requirement_values.txt`, `bm_drain_duel_values.txt`, `bm_blood_mage_story_values.txt`.
- Evaluated in the scope of the caller. Values reading `scope:recipient` / `scope:actor` only work where those exist; say so in a comment.
- Keep UI-bound values cheap (no iterators). Use `save_temporary_value_as` for repeated sub-expressions.
- No random ranges in costs: they re-roll on every read.
- Localization display: `[GetPlayer.MakeScope.ScriptValue('bm_x')|0]`. See `bm_blood_mage_story_l_english.yml`.

## Story / roster UI

When adding a story field, update in order: story effects → scripted GUI → localization → `window_situation_list.gui` (Blood Mage sections only).

## Events

- One namespace per file; match neighbouring files.
- Every event needs a source (`trigger_event`, `on_action`, decision, interaction). Dead events aren't errors, so check.
