---
trigger: model_decision
description: Core CK3 script patterns (scopes, effects, triggers, iterators, scripted effects/triggers, script values, tooltips). Read before writing or editing any file under common/ or events/.
---

# CK3 scripting patterns

Sources: CK3 wiki (Scripting, Scopes, Effects, Triggers) plus patterns already used in this repo. Where the wiki and vanilla 1.19 disagree, **vanilla 1.19 wins**. Several wiki pages are tagged "potentially outdated". When unsure whether a name exists, grep vanilla `game/` or the `script_docs` logs. Never guess.

## Syntax basics

- Everything is `key = value` or `key = { ... }`. Comparison operators are `=`, `!=`, `<`, `<=`, `>`, `>=`. `?=` means "scope exists and the condition holds".
- Math and values: `value = 5`, or a block (`value = { add = 5 multiply = scope:x.age }`) in script values only. Do not write inline math in effects. Use `set_variable`, a script value, or `change_variable`.
- A block is an implicit `AND`. Use `OR`, `NOT`, `NOR`, `NAND` explicitly. `NOT = { A B }` means NOT (A AND B). Use `NOR` for "none of".
- The same name can be a trigger or an effect depending on context (`add_trait` is an effect, `has_trait` is a trigger). If the game logs "wrong scope" or "unexpected token", you are in the wrong block type.

## Scopes

- Scope types: character, title, province, faith, religion, culture, dynasty, house, secret, scheme, activity, story, and so on. Every trigger and effect declares which scope it runs in.
- `root` is the scope the script started in (the event/decision/interaction owner). `this` is the current scope. `prev` is the scope you came from, and only one level back (`prev.prev` is invalid). When you need something further back, **save it**.
- **Saved scopes**: `save_scope_as = name` (effect) and `scope:name` to read. Use `save_temporary_scope_as` for values only needed during the current trigger or effect block. In an interaction, `scope:actor` and `scope:recipient` are provided. In an event, `scope:` values passed by `trigger_event` / `on_action` are available in that event.
- **Scope chaining** with dots: `scope:recipient.father.primary_title.holder`. Each link must exist. Guard possibly-missing links with `?=` (triggers) or `exists = scope:x` before using them.
- **Switching scope** is done by naming a link, `liege = { ... }`, or `scope:x = { ... }`. Inside, `root` is unchanged but `this` and `prev` have moved.
- **Scope existence**: `exists = scope:x`, `scope:x ?= { ... }`. Use `is_alive`/`is_ai` checks before touching a character you looked up.
- **Faith, religion and title keys** are scopes too: `faith:quintessence_faith`, `religion:x`, `title:k_france`, `culture:norse`. They only work if the key is defined, so an unknown key from an optional mod is a script error.

## Iterators

| Prefix | Context | Notes |
|---|---|---|
| `every_X` | effect | runs on all matches; `limit = { }` filters |
| `random_X` | effect | one random match; add `weight = { }` for weighting |
| `ordered_X` | effect | sort with `order_by`, cap with `max`/`position`; `check_range_bounds = no` if fewer exist |
| `any_X` | trigger | true if some/count/percent match; **no `limit`**. Put conditions directly in the block, with `count = N` or `percent = 0.5` to tighten |

- `limit` goes **first** inside `every_/random_/ordered_`. `random_` and `ordered_` are silent no-ops if nothing matches. Use `alternative_limit` for a fallback filter.
- Prefer `has_trait`/`has_relation_*`/`is_*_of` triggers over a large `any_living_character`. Scanning every character is slow.
- Run an iterator over a saved list with `add_to_list` / `every_in_list = { list = name }` / `any_in_list`. Scope-based lists clear at the end of the event/effect.
- `while = { limit = { ... } ... }` or `while = { count = N ... }` needs a guaranteed exit. Mind infinite loops.

## Control flow

- Effects: `if = { limit = { ... } ... }`, `else_if = { limit = { ... } ... }`, `else = { ... }`. `limit` is mandatory on `if` and `else_if`.
- Triggers: `trigger_if = { limit = { ... } ... }`, `trigger_else_if`, `trigger_else`. Never use plain `if` in a trigger block.
- `switch = { trigger = has_trait  <value> = { ... }  fallback = { ... } }` for many-way branches on the same trigger.
- `random = { chance = N effect... }` takes a percentage, as does `random_list = { 10 = { ... } 30 = { ... } }`, whose weights need not total 100. Use `modifier = { add/factor/... trigger... }` inside a weighted entry.

## Effects

- Hide noise from tooltips with `hidden_effect = { ... }`. Give a readable line instead with `custom_tooltip = { text = bm_key }` (put hidden effects in a sibling `hidden_effect`).
- Scripted-effect style: `bm_do_thing_effect = yes`, or with parameters `bm_do_thing_effect = { AMOUNT = 5 TARGET = scope:x }`.
- Common effect patterns:
  - `add_character_modifier = { modifier = x years = 5 }` / `remove_character_modifier = x`
  - `add_character_flag = { flag = x years = 1 }` / `has_character_flag`
  - Variables: `set_variable = { name = x value = 1 }` / `change_variable` / `var:x` / `has_variable`. Use `global_var:`, `local_var:` for the other lifetimes.
  - `send_interface_toast = { title = key left_icon = root ... effects }` for feedback messages.
  - `trigger_event = { id = ns.1 days = 3 }` (or `on_action = x`, or `trigger_event = ns.1`).
- Do not chain effects that depend on state that an earlier effect changes without re-checking in a new `if`.

## Triggers

- Triggers run inside `trigger`, `limit`, `is_shown`, `is_valid`, `potential`, `ai_potential`, `trigger_if` blocks, and so on. `custom_description = { text = key subject = scope:x ... }` and `custom_tooltip` rewrite the shown text.
- Be cheap in `is_shown` / `potential`. They run every frame or on every pulse. Put the cheapest, most excluding checks first.
- `always = yes/no`, `is_ai = yes/no`, `has_game_rule = x`, and `exists` are the standard guards.
- Scripted triggers (`common/scripted_triggers/`) are called `my_trigger = yes` (or `= no` to negate). They can take `$PARAM$` arguments the same way scripted effects do.

## Scripted effects, triggers, modifiers, script values

- **Scripted effects/triggers**: for reuse. Use `$PARAM$` placeholders, which are plain **text substitution** (not typed). Call with `name = { PARAM = value }`. Escape nothing. If a parameter is optional, use `$PARAM|default$` syntax.
- **Script values** (`common/script_values/`): named numbers, usable anywhere a number is accepted, with scope access (`scope:recipient.age`). Structure: `my_value = { value = 10 if = { limit = { ... } add = 5 } multiply = 2 }`. Prefer them to repeated magic numbers.
- **Scripted modifiers** (`common/scripted_modifiers/`) hold reusable `modifier` blocks for weights, called as `my_modifier = yes` inside an `ai_will_do`, `weight` or script value.
- **Script values in costs/AI** are evaluated in the scope of the thing being evaluated. Check the scope before using `scope:` names.

## AI weights

- `ai_will_do = { base = N modifier = { add = X <triggers> } }`. The final number is a percent chance (for decisions, 100 means "always when checked"). Negative `base` means "rare".
- `ai_check_interval = N` months between checks. `0` disables AI use. Choose a larger N for expensive checks.
- `ai_potential` is deprecated in some contexts in 1.19 (Tiger warns, as the repo already knows). Do not mass-convert it.

## Event patterns (for events/ files)

- Header: `namespace = my_ns`, then `my_ns.0001 = { type = character_event title = ... desc = ... theme = ... left_portrait = root immediate = { } option = { name = my_ns.0001.a ... } }`. `hidden = yes` events do not need a title, desc or option.
- `trigger` on the event is checked before firing. `immediate` runs before the window opens. `after` runs after the option.
- Events must be fired by something (`trigger_event`, `on_action`, an interaction/decision). A dead event is not an error, so check where it is fired.
- Multiple options each need their own localized `name`, and must not rely on effects from a sibling option.

## Debugging

- Run with `-debug_mode`, read `Documents/Paradox Interactive/Crusader Kings III/logs/error.log`.
- Use `debug_log`, `debug_log_scopes = yes`, and `script_docs` (`effects.log`, `triggers.log`, `event_scopes.log`) for ground truth on available names and valid scopes.
- Run `ck3-tiger` after every change, and treat new errors as blockers.
