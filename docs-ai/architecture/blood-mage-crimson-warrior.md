# Blood Mage: Crimson Warrior

Living technical specification for the Crimson Warrior subsystem.

## Executive Summary

- **What:** Evolving martial combat lifestyle trait `lifestyle_crimson_warrior` with 4 tracks (max 100 XP each).
- **Base stats:** `health = -0.2`, `life_expectancy = -2`, `prowess = 5`. Non-inheritable (`genetic = no`).
- **How to acquire:** `grant_crimson_warrior_interaction` cast by a Blood Mage on a sworn knight/courtier or self. Cost: `lifedrain_piety_cost_minor` (75 Piety) + `lifeforce_modifier_minor`.
- **How to level:**
  - **Minor Lifeforce Infusion:** `empower_crimson_warrior_minor_interaction`. Cost: 75 Piety + Minor Lifeforce. Gain: +3 XP in chosen track (via event `bm_crimson_warrior_event.0001`).
  - **Major Lifeforce Infusion:** `empower_crimson_warrior_major_interaction`. Cost: 75 Piety + Major Lifeforce. Gain: +10 XP in chosen track (via event `bm_crimson_warrior_event.0002`).
  - **Battle Victory (`on_combat_end_winner`):** Side knights gain +5 XP (`slaughter`); side commanders gain +6 XP (`vanguard`).
  - **Battle Defeat (`on_combat_end_loser`):** Surviving side knights and commanders gain +2 XP (`resilience`).
  - **Duel Kill (`on_death` / single combat):** Slaying opponent in single combat grants victor +12 XP (`slaughter`).

### Tracks Master Table

Each track has 10 tiers (10, 20, 30, ..., 100 XP). Per-level benefits repeat linearly:

| Track | Theme | Per-Tier Bonus (x10 at 100 XP) | Cap Total (Rank 10) |
| --- | --- | --- | --- |
| **`slaughter`** | Single combat & dueling | `prowess = 1.5`<br>`wound_recovery_mult = 0.05` | +15 Prowess<br>+50% Wound Recovery |
| **`vanguard`** | Army command & knight shock | `knight_effectiveness_mult = 0.08`<br>`enemy_fatal_casualties_mult = 0.05` | +80% Knight Effectiveness<br>+50% Fatal Casualties |
| **`blood_frenzy`** | Dread & troop lethality | `dread_baseline_add = 4`<br>`maa_damage_mult = 0.03` | +40 Dread Baseline<br>+30% Men-at-Arms Damage |
| **`resilience`** | Somatic decay mitigation | `health = 0.08`<br>`life_expectancy = 1` | +0.8 Health<br>+10 Life Expectancy |

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
| Duel fatality XP hook | `common/on_action/bm_duel_on_actions.txt` |
| Story retinue list population | `common/scripted_effects/bm_blood_mage_story_list_effects.txt` |
| English localization | `localization/english/bm_traits_l_english.yml`<br>`localization/english/bm_interactions_l_english.yml`<br>`localization/english/bm_crimson_warrior_events_l_english.yml` |

## Gotchas

- **Combat Side Iterators:** `every_side_knight` and `every_side_commander` evaluate in combat side scope (`on_combat_end_winner`, `on_combat_end_loser`).
- **Engaged in Single Combat:** `has_variable = engaged_in_single_combat` is stripped on death finalization; duel kill XP must trigger synchronously inside `on_death` before `remove_single_combat_info_effect`.
- **Self-Targeting:** Blood Mages who also possess `lifestyle_crimson_warrior` can empower themselves via the interactions or gain XP from battle/duel hooks directly.

## Not verified

- AI frequency of repeatedly infusing the same knight with major lifeforce under high AI wealth and piety.
