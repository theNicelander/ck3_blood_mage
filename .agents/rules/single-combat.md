---
trigger: model_decision
description: Understanding and hooking into CK3 vanilla single combat duels and skill duels. Read before touching duels or combat fatality hooks.
---

# CK3 Single Combat and Duels

CK3 has two fundamentally distinct mechanics termed "duels". Never confuse them:

1. **Skill Duels (`duel = { ... }`):**
   - A single-tick scripted effect comparing stats (e.g. `skill = learning`, `skill = diplomacy`, `skill = prowess`).
   - Abstract dice roll / stat comparison. No physical combat, no rounds, no stances, no weapons, no fatality.
2. **The Single Combat Engine (SCE):**
   - The interactive martial combat system implemented across `common/scripted_effects/00_single_combat_effects.txt` and `events/single_combat_events.txt`.
   - Features tactical combat rounds (`single_combat.0001`), move selection (attacks, parries, dirty tricks), weapon interactions, injury accumulation, and lethal finishes.

## Initiating Single Combat

Single combat is initialized via `configure_start_single_combat_effect`:

```ck3
configure_start_single_combat_effect = {
    SC_INITIATOR = <character>       # Who started the duel / interaction
    SC_ATTACKER = <character>        # Attacking combatant
    SC_DEFENDER = <character>        # Defending combatant
    FATALITY = <no|possible|default|always|practice>
    FIXED = <no|sc_attacker|sc_defender>
    LOCALE = <terrain_scope|battlefield|courtyard|throne_room|...>
    OUTPUT_EVENT = <event_id>        # Fired for initiator/survivor on completion
    INVALIDATION_EVENT = <event_id>  # Fired if combat invalidates
}
```

### Fatality Levels
- `always`: Losing is always fatal.
- `possible`: Death occurs only if the loser is already critically wounded (`wounded_3`) or takes critical injury.
- `default`: Fatal if the initiator's government is tribal (`fatality_default_will_die_trigger`), non-fatal otherwise.
- `no`: Wounds only; death disabled.
- `practice`: No death, no wounds.

## Variables and Lifecycle

During active single combat, the engine sets specific variables on the participants:
- Both participants receive: `set_variable = { name = engaged_in_single_combat value = yes }`.
- Attacker receives: `sc_attacker_duel_success_score`, `sc_attacker_injury_bonus`, `sc_attacker_injury_risk_score`.
- Defender receives: `sc_defender_duel_success_score`, `success_threshold`, `current_round`.

## Combat Resolution & Fatality Timing

When single combat concludes, `finalise_combat_results_effect` runs:
1. Assigns `scope:sc_victor` and `scope:sc_loser`.
2. Triggers results events: `single_combat.0031` (loser) and `single_combat.0041` (victor).
3. If fatal, executes `work_out_wounds_or_death_effect`:
   ```ck3
   scope:sc_loser = {
       death = {
           killer = scope:sc_victor
           death_reason = death_duel
       }
   }
   ```
4. Executes `remove_single_combat_info_effect`, stripping all temporary single combat variables and removing `engaged_in_single_combat`.
5. Fires `OUTPUT_EVENT` on the initiator or surviving combatant.

## Hooking into Fatal Duels

- **Never override `events/single_combat_events.txt`**: Overriding this 12,000+ line file destroys compatibility with vanilla updates and other mods.
- **Hook via `on_death`**: When `death = { killer = scope:sc_victor death_reason = death_duel }` executes in `work_out_wounds_or_death_effect`, the game engine triggers `on_death` synchronously **before** `remove_single_combat_info_effect` runs.
- **Variable Window**: During `on_death`:
  - `root` (dying loser) and `scope:killer` (victor) still have `has_variable = engaged_in_single_combat`.
  - Attacker still has `sc_attacker_duel_success_score`; defender still has `sc_defender_duel_success_score`.
- **Trigger Warning (`death_reason`)**: In `on_death`, `root.is_alive` is still `yes` ("about to die"). Calling `death_reason = death_duel` directly in `on_death` logs a script error because `death_reason` is only populated on deceased characters. Rely on `has_variable = engaged_in_single_combat` during `on_death`, or dispatch an event with `delayed = yes` to inspect `death_reason` post-death.
