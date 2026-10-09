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
