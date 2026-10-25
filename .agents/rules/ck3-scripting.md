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

Error signatures and fixes: `ck3-error-catalog.md` (read when auditing `error.log`). Mod architecture: `docs-ai/architecture/README.md`.
