---
name: single-combat
description: Single Combat Engine (SCE) vs skill duels (duel = {}), fatality on_death hooks, runtime variables, and 100-weight duel scaling in CK3.
---

# Single Combat & Duels

Two systems: **Skill duel (`duel = {}`)** (1-tick stat check, no rounds/fatalities) vs **SCE** (`00_single_combat_effects.txt`, `single_combat_events.txt`: rounds, wounds, death).

## SCE (`configure_start_single_combat_effect`)

```ck3
configure_start_single_combat_effect = {
	SC_INITIATOR = <char>  SC_ATTACKER = <char>  SC_DEFENDER = <char>
	FATALITY = <no|possible|default|always|practice>  FIXED = <no|sc_attacker|sc_defender>
	LOCALE = <terrain|battlefield|courtyard|throne_room>
	OUTPUT_EVENT = <id>  INVALIDATION_EVENT = <id>
}
```
- **Fatality**: `always` (fatal), `possible` (critical injury/`wounded_3`), `default` (`fatality_default_will_die_trigger` / tribal), `no` (wounds), `practice` (safe).
- **Runtime vars**: both `engaged_in_single_combat`; attacker `sc_attacker_{duel_success_score,injury_bonus,injury_risk_score}`; defender `sc_defender_duel_success_score`, `success_threshold`, `current_round`.
- **Resolution** (`finalise_combat_results_effect`): sets `scope:sc_victor`/`sc_loser` → fires `single_combat.0031`/`0041` → if fatal, `death = { killer = scope:sc_victor death_reason = death_duel }` (runs `on_death` synchronously **before** wiping vars) → `remove_single_combat_info_effect` → `OUTPUT_EVENT`.
- **Fatal hook trap**: never override `single_combat_events.txt`. Hook `on_death`: `root` (victim) + `scope:killer` still have `engaged_in_single_combat`, **but** `root.is_alive = yes` and `death_reason = death_duel` errors (post-mortem only). Check `has_variable = engaged_in_single_combat` in `on_death`, or fire `delayed = yes` event for `death_reason`.
- **Practice grudge trap**: `FATALITY = practice` only prevents death/wounds; vanilla `single_combat.0031` option `c` (~50% AI chance) still calls `progress_towards_rival_effect`, setting `grudge` (low-tier, breaks friendships via `opposites`) or `potential_rival`/`rival`. For friendly sparring, snapshot pre-bout relations with `bm_spar_snapshot_relations_effect` and restore in `OUTPUT_EVENT` `immediate` via `bm_spar_restore_relations_effect` (`bm_duel_effects.txt`).

## Skill duel (`duel = {}`)

`scope:duel_value = actor_skill - target_value`. Convention: base weights sum to **100** at skill 0 (e.g. 17/33/33/17); pair `+M`/`-M` slopes so skill ~50 floors failure at **~5–10%** (`min = -(base - desired_floor)`) and caps positives with `max` to keep total weight 100.

```ck3
duel = {
	skill = learning  value = 0
	17 = { desc = crit_succ_tt compare_modifier = { value = scope:duel_value multiplier = 0.32 max = 16 } }
	33 = { desc = succ_tt      compare_modifier = { value = scope:duel_value multiplier = 0.68 max = 30 } }
	33 = { desc = fail_tt      compare_modifier = { value = scope:duel_value multiplier = -0.68 min = -30 } } # floor 3
	17 = { desc = crit_fail_tt compare_modifier = { value = scope:duel_value multiplier = -0.32 min = -16 } } # floor 1
}
```
