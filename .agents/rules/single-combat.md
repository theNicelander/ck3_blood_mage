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

## Skill Duel Probability & Scaling Architecture (`duel = { ... }`)

Skill duels resolve instantly via weighted random selection modified by stat comparisons.

### Syntax & Mechanics

```ck3
duel = {
    skill = <learning|prowess|martial|stewardship|intrigue|diplomacy>
    value = <target_value|0>   # Target skill value to compare against; scope:duel_value = actor_skill - target_value
    [target = <character>]    # Optional opponent; if omitted, self-test against static 'value'

    <base_weight> = {
        desc = <outcome_loc_tt>
        compare_modifier = {
            value = scope:duel_value
            multiplier = <float>  # Weight delta per point of skill above/below target
            [min = <float>]       # Hard floor on the modifier delta (weight cannot drop below base + min)
            [max = <float>]       # Hard cap on the modifier delta (weight cannot exceed base + max)
        }
        # Outcome effects, toasts, XP awards...
    }
}
```

### Exact Probability Design Pattern (Summing to 100)

To achieve precise, non-distorting percentages that scale smoothly and respect minimum/maximum floors:
1. **Base weights sum to 100** at baseline skill ($L = 0$). For example, 1/6 critical success (17), 1/3 success (33), 1/3 failure (33), 1/6 critical failure (17).
2. **Symmetric slope pairs**: When success scales up by `+M`, failure scales down by `-M`. This keeps total weight constant at 100 across the entire active scaling range.
3. **Hard Floors via `min`**:
   - In CK3, `min` in `compare_modifier` is the **minimum adjustment added to the base weight**, not the absolute weight itself.
   - To floor an outcome of base weight `B` at minimum weight `W_min`, set:
     $$\text{min} = -(B - W_{\text{min}})$$
     *(Example: base 33 floored at 3% $\implies$ `min = -30`; base 17 floored at 1% $\implies$ `min = -16`)*.
4. **Capping Complementary Outcomes via `max`**:
   - When negative outcomes hit their floors at a target skill milestone (e.g. $L = 50$), positive weights must also cap at `max` so the total pool remains exactly 100.
   - If total floored failure weight is $3 + 1 = 4$, cap successes at $63 + 33 = 96$ (`max = 30` and `max = 16`). Beyond $L = 50$, probabilities remain permanently locked at exactly 3% and 1%.
