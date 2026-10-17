---
trigger: model_decision
description: Single Combat Engine (SCE) vs skill duels, fatality hooks, and variables.
---

# CK3 Single Combat and duels

Two distinct engine duel systems:
1. **Skill duel (`duel = { ... }`)**: Single-tick stat comparison (`skill = prowess|learning|...`). No rounds, no stances, no fatalities.
2. **Single Combat Engine (SCE)**: Martial duel system (`common/scripted_effects/00_single_combat_effects.txt`, `events/single_combat_events.txt`). Interactive rounds (`single_combat.0001`), attacks, parries, injuries, fatalities.

## Initiating Single Combat

```ck3
configure_start_single_combat_effect = {
    SC_INITIATOR = <character>       # Interaction initiator
    SC_ATTACKER = <character>        # Attacker
    SC_DEFENDER = <character>        # Defender
    FATALITY = <no|possible|default|always|practice>
    FIXED = <no|sc_attacker|sc_defender>
    LOCALE = <terrain_scope|battlefield|courtyard|throne_room|...>
    OUTPUT_EVENT = <event_id>        # Fired for initiator/survivor on completion
    INVALIDATION_EVENT = <event_id>  # Fired if combat invalidates
}
```

### Fatality levels
- `always`: Loss is fatal.
- `possible`: Death only if critically injured (`wounded_3` or critical wound roll).
- `default`: Fatal if initiator tribal (`fatality_default_will_die_trigger`), else non-fatal.
- `no`: Wounds only.
- `practice`: No wounds, no death.

## Runtime variables

During combat, engine sets on participants:
- Both: `has_variable = engaged_in_single_combat`.
- Attacker: `sc_attacker_duel_success_score`, `sc_attacker_injury_bonus`, `sc_attacker_injury_risk_score`.
- Defender: `sc_defender_duel_success_score`, `success_threshold`, `current_round`.

## Resolution & fatality sequence

At conclusion, `finalise_combat_results_effect` runs:
1. Assigns `scope:sc_victor` and `scope:sc_loser`.
2. Triggers results events: `single_combat.0031` (loser), `single_combat.0041` (victor).
3. If fatal, executes `work_out_wounds_or_death_effect`:
   ```ck3
   scope:sc_loser = {
       death = {
           killer = scope:sc_victor
           death_reason = death_duel
       }
   }
   ```
4. Executes `remove_single_combat_info_effect`, wiping all combat variables and `engaged_in_single_combat`.
5. Fires `OUTPUT_EVENT`.

## Fatal duel hooking

- **Never override `events/single_combat_events.txt`**: Breaks compatibility.
- **Hook via `on_death`**: `death = { killer = scope:sc_victor death_reason = death_duel }` fires `on_death` synchronously **before** `remove_single_combat_info_effect`.
- **Variable state in `on_death`**:
  - `root` (victim) and `scope:killer` (victor) still hold `has_variable = engaged_in_single_combat`.
  - Attacker/defender duel scores still present.
- **Engine trap**: In `on_death`, `root.is_alive` is `yes` ("about to die"). Calling `death_reason = death_duel` logs script error (`death_reason` populates only post-mortem). Check `has_variable = engaged_in_single_combat` in `on_death`, or dispatch `delayed = yes` event to inspect `death_reason`.

## Skill duels (`duel = { ... }`)

Single-tick stat checks (`scope:duel_value = actor_skill - target_value`). Use `compare_modifier`:

```ck3
duel = {
    skill = learning
    value = 0
    # Outcomes: base weights sum to 100 at skill 0
    17 = { # Crit Success (scales up)
        desc = outcome_crit_succ_tt
        compare_modifier = { value = scope:duel_value multiplier = 0.32 max = 16 }
    }
    33 = { # Success (scales up)
        desc = outcome_succ_tt
        compare_modifier = { value = scope:duel_value multiplier = 0.68 max = 30 }
    }
    33 = { # Failure (scales down)
        desc = outcome_fail_tt
        compare_modifier = { value = scope:duel_value multiplier = -0.68 min = -30 } # floor weight: 3
    }
    17 = { # Crit Failure (scales down)
        desc = outcome_crit_fail_tt
        compare_modifier = { value = scope:duel_value multiplier = -0.32 min = -16 } # floor weight: 1
    }
}
```

### Preferred weighting convention
- **Baseline (skill 0)**: Base weights sum to 100 (e.g. 1/3 success, 1/3 failure, 1/6 crit success, 1/6 crit failure).
- **Skill ~50 target**: Most negative outcomes are negated by skill ~50, with failure floored at **~5–10%** (e.g. 3–8% failure, 1–2% crit failure).
- **Hard floors via `min`**: `min` in `compare_modifier` is the delta added to base (`min = -(base - desired_floor)`).
- **Constant 100 total weight**: Pair positive/negative slopes (`+M` / `-M`) and cap positive outcomes with `max` when negative outcomes hit their floors.
