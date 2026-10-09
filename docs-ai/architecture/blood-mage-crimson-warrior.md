# Blood Mage: Crimson Warrior

Living technical specification for the Crimson Warrior subsystem.

## Executive Summary

- **What:** Evolving martial combat lifestyle trait `lifestyle_crimson_warrior` with 3 tracks (max 100 XP each).
- **Base stats:** `health = -0.2`, `life_expectancy = -2`, `prowess = 5`. Non-inheritable (`genetic = no`).
- **How to acquire:** `grant_crimson_warrior_interaction` cast by a Blood Mage on a sworn knight/courtier or self. Cost: `lifedrain_piety_cost_minor` (75 Piety) + `lifeforce_modifier_minor`.
- **How to level:**
  - **Minor Lifeforce Infusion:** `empower_crimson_warrior_minor_interaction`. Cost: 75 Piety + Minor Lifeforce. Gain: +3 XP in chosen track (via event `bm_crimson_warrior_event.0001`).
  - **Major Lifeforce Infusion:** `empower_crimson_warrior_major_interaction`. Cost: 75 Piety + Major Lifeforce. Gain: +10 XP in chosen track (via event `bm_crimson_warrior_event.0002`).
  - **Battle Victory (`on_combat_end_winner`):** Side knights gain +5 XP (`vanguard`); side commanders gain +6 XP (`vanguard`).
  - **Battle Defeat (`on_combat_end_loser`):** Surviving side knights and commanders gain +1 XP (`vanguard`) and +1 XP (`resilience`).
  - **Duel Victory (`on_death` / single combat):** Slaying opponent in single combat grants victor +6 XP (`slaughter`).
  - **Tournament Participation/Victory (`on_travel_activity_complete`):** Completing a tournament activity grants +3 XP (`slaughter`).
  - **Yearly Survival Pulse (`blood_mage_yearly_events.004`):** Passive +1 XP per year in `resilience`.

### Tracks Master Table

Each track has 10 tiers (10, 20, 30, ..., 100 XP):

| Track | Theme & XP Sources | Tier Progression | Cap Total (Rank 10) |
| --- | --- | --- | --- |
| **`vanguard`** | Army battle command & participation | `advantage = 1` per tier<br>`martial = 1` every 2 tiers (20, 40, 60, 80, 100)<br>`martial_per_piety_level = 1` at tier 50 & 100<br>`monthly_prestige = 0.1` per tier | +10 Advantage<br>+5 Martial<br>+2 Martial per Piety level<br>+1.0 Monthly Prestige |
| **`slaughter`** | Duels & tournament contests | `prowess = 1` per tier<br>`prowess_per_piety_level = 1` at tier 50 & 100<br>`monthly_prestige = 0.1` per tier | +10 Prowess (+15 total with base)<br>+2 Prowess per Piety level<br>+1.0 Monthly Prestige |
| **`resilience`** | Yearly survival & battle recovery | `life_expectancy = 1`<br>`health = 0.05`<br>`fertility = 0.02`<br>`epidemic_resistance = 1`<br>`monthly_prestige = 0.1` per tier | +10 Life Expectancy (Net +8)<br>+0.5 Health (Net +0.3)<br>+20% Fertility<br>+10 Epidemic Resistance<br>+1.0 Monthly Prestige |

## Key Mechanics

- **Interactions (`bm_grant_blood_infused_prowess.txt`):**
  - `grant_crimson_warrior_interaction`: Bestows base trait at 0 XP. Actor must hold `lifestyle_blood_mage` and Minor Lifeforce.
  - `empower_crimson_warrior_minor_interaction`: Consumes Minor Lifeforce, grants +3 XP to target in track picked via event.
  - `empower_crimson_warrior_major_interaction`: Consumes Major Lifeforce, grants +10 XP to target in track picked via event.
- **Story Panel Integration:** Roster list effect `bm_refresh_blood_magic_rosters_effect` populates `bm_crimson_retinue` using `has_trait = lifestyle_crimson_warrior`.
- **Zero Legacy Modifiers:** Pure trait implementation; `lifeforce_modifier_crimson_warrior` and `lifeforce_modifier_crimson_champion` are completely removed.

## Where the details live

| Concept | File |
| --- | --- |
| Trait definition & tracks | `common/traits/bm_crimson_warrior_trait.txt` |
| Trait XP helper macros | `common/scripted_effects/bm_trait_track_xp_gain_effects.txt` |
| Bestow & empower interactions | `common/character_interactions/bm_grant_blood_infused_prowess.txt` |
| Track selection events | `events/bm_crimson_warrior_events.txt` |
| Battle progression hooks | `common/on_action/bm_combat_on_actions.txt` |
| Duel victory XP hook | `common/on_action/bm_duel_on_actions.txt` |
| Yearly survival XP pulse | `common/on_action/bm_yearly_pulse.txt`<br>`events/bm_yearly_events.txt` |
| Story retinue list population | `common/scripted_effects/bm_blood_mage_story_list_effects.txt` |
| English localization | `localization/english/bm_traits_l_english.yml`<br>`localization/english/bm_interactions_l_english.yml`<br>`localization/english/bm_crimson_warrior_events_l_english.yml` |

## Gotchas

- **Combat Side Iterators:** `every_side_knight` and `every_side_commander` evaluate in combat side scope (`on_combat_end_winner`, `on_combat_end_loser`).
- **Tournament Detection:** `on_travel_activity_complete` checks `involved_activity ?= { has_activity_type = activity_tournament }` when returning from tournament.
- **Self-Targeting:** Blood Mages who also possess `lifestyle_crimson_warrior` can empower themselves via the interactions or gain XP from battle/duel hooks directly.

## Not verified

- AI frequency of repeatedly infusing the same knight with major lifeforce under high AI wealth and piety.
