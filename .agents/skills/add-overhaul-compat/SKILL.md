---
name: add-overhaul-compat
description: >-
  Add built-in trait draining or compatibility modules for CK3 overhaul mods (AGOT, LotR, EK2, PoD).
  Use when inspecting Steam Workshop mods or adding/extending bm_compat_<overhaul>_* files.
---

# Overhaul Mod Compatibility (`bm_compat_<overhaul>_*`)

## Principles

- **Built-in, zero submods**: Keep overhaul compat inside `ck3_blood_mage` in isolated `bm_compat_<overhaul>_*` files gated by Day-1 `on_game_start` global variables. Benign parse-time `error.log` warnings in vanilla are acceptable when isolated and documented in `debug-ck3-logs`.
- **Popular/major mods only**: Only add built-in compat for major overhauls (AGOT, LotR, EK2, PoD) or widely used mods (e.g. Commander+ 1.21, Inheritable Traits++). Skip niche/uncommon trait packs (unguarded trait keys add startup `error.log` noise and name-collision risk for few users).
- **Verify in workshop files first**: Never guess trait IDs, `opposites`, or startup globals. Inspect `/Users/clarabotet/Library/Application Support/Steam/steamapps/workshop/content/1158310/<id>/` (needs `BypassSandbox: true`).
- **Installed overhauls & guards**:
  - AGOT (`2962333032`): `bm_is_agot_loaded_trigger` (`AGOT_is_loaded`)
  - LotR: Realms in Exile (`2291024373`): `bm_is_lotr_loaded_trigger` (`tedjin_reactionaries_triggered` / `sauron_destroyed`)
  - Elder Kings 2 (`2887120253`): `bm_is_ek2_loaded_trigger` (`morrowind_high_councilor` / `almsivi_*_power`)
  - Inheritable Traits++ (`3714256909`): warning-free via vanilla trait groups + `has_trait_rank`/`change_trait_rank` (`max = 5`)
  - Commander+ 1.21 (`3716251917`): unguarded 29 single-track commander traits in `bm_compat_memory_*` (watch generic keys like `zealot`/`patriot`/`navigator`/`mapper`)

## Recipe: Add a New Overhaul Module (`<mod>`, e.g. `pod`)

1. **Detect**: Find an unconditional `set_global_variable` in `<mod>/common/on_action/*game_start*.txt`. Add `bm_is_<mod>_loaded_trigger` in `common/scripted_triggers/bm_triggers.txt` and include it in `is_playing_overhaul_mod`.
2. **Audit traits**: Scan `<mod>/common/traits/*.txt` for `genetic = yes`, `good = yes`, `group =`, `level =`, and `opposites = { ... }`. Always block opposite transformations (e.g. EK2 vampire/lycan/lich) and immortals on lifespan drains.
3. **Create isolated module**:
   - `common/scripted_triggers/bm_compat_<mod>_triggers.txt`: per-trait triggers + `bm_compat_<mod>_can_drain_traits_from_target_trigger` (all gated by `bm_is_<mod>_loaded_trigger = yes`).
   - `events/bm_compat_<mod>_trait_drain_events.txt`: `bm_compat_<mod>_trait_drain.0001` (reuse parameterized helpers in `bm_drain_trait_effects.txt`: `bm_trait_drain_execute_single_effect`, `bm_trait_drain_execute_single_dual_xp_effect`, or `bm_trait_drain_duel_fail_effects` for custom tiered curves - macro expansion keeps external trait IDs isolated at `bm_compat_*` call sites; use `bm_ai_trait_drain_safety_modifier` / `bm_ai_trait_drain_decline_modifier`, and guard `"Back"` return to `bm_trait_drain.001` with `is_ai = no` to prevent AI loops).
   - `localization/english/event_localization/bm_compat_<mod>_l_english.yml`.
4. **Wire router (2 lines)**:
   - Add `bm_compat_<mod>_can_drain_traits_from_target_trigger = yes` to `bm_compat_can_drain_traits_from_target_trigger` (`common/scripted_triggers/bm_trait_triggers.txt`) - automatically enables both `bm_blood_drain_interaction` and `bm_action_can_trait_drain_prisoner`.
   - Add `else_if` branch in `bm_compat_open_trait_drain_event_effect` (`common/scripted_effects/bm_drain_trait_effects.txt`).
   - **Blood Memory Drain (lifestyles/commanders/fame)**: Add triggers to `common/scripted_triggers/bm_compat_memory_triggers.txt` (including `bm_compat_has_xp_drainable_memory_trait_trigger` for tracked traits; use `quad_track` helpers for 4-track traits), a picker event in `events/bm_compat_memory_drain_events.txt`, and an `else_if` branch in `bm_compat_open_memory_drain_event_effect` (`common/scripted_effects/bm_memory_drain_effects.txt`).
5. **Docs & validate**: Add benign parse warning signatures to `.agents/skills/debug-ck3-logs/SKILL.md`, update `docs-ai/architecture/blood-mage-interactions.md`, run `python3 scripts/check_repo.py --fix`.

## CK3 Cross-Mod Gotchas

- **Warning-free tricks**: Vanilla trait group + integer rank (`has_trait_rank`/`change_trait_rank`) and untyped character flags / global variable lists (`add_to_global_variable_list`, e.g. AGOT `historical_dragonseed`) cause zero parse warnings.
- **Dynamic trait scoping limit**: `any_character_trait`/`add_trait = scope:target_trait` works, but trait scopes only filter by `has_trait_category` or `has_trait_flag` (unusable if overhaul traits lack custom flags).
- **Buildings/Districts**: Check overhaul `descriptor.mod` `supported_version` before adding buildings (pre-1.21 overhauls use `type = duchy_capital` instead of `common/districts/`).
