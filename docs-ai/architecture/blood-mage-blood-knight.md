# Blood Mage: Blood Knight

Living technical specification for the Blood Knight subsystem.

## Executive Summary

- **What:** Evolving martial combat lifestyle trait `lifestyle_blood_knight` with 3 tracks (max 100 XP each).
- **Base stats:** `health = -1`, `life_expectancy = -5`, `prowess = -5`. Ruler designer cost: 50. Non-inheritable (`genetic = no`).
- **How to acquire:**
  - `make_blood_knight_interaction`: Cast by a Blood Mage on a sworn knight/courtier or self. Cost: `blood_knight_creation_piety_cost` (100 Piety) + `lifeforce_modifier_major`.
  - **Geyser Duel Initiation (`bm_geyser_duel.0001`):** Travel to Reykjavik or Tsushima and confront Egill Skallagrímsson via `bm_blood_cultist_become_blood_mage_decision` or `bm_enhance_blood_ritual_decision` (requires Piety or Prestige level >= 2 to open decision). Choosing the Prowess duel requires Prestige level >= 2, costs 1 Fame level (`add_prestige_level = -1`), and bestows `lifestyle_blood_knight` upon victory.
- **Universal rank progression:** Every trait rank across all 3 tracks awards `health = 0.2`, `life_expectancy = 1`, and `monthly_prestige = 0.1`, ensuring characters can offset the base trait negatives no matter which track they advance.
- **How to level:**
  - **Empower Blood Knight Interaction (`empower_blood_knight_interaction`):** Direct interaction popup (modal with options, no event):
    - **Major Lifeforce:** Consumes `lifeforce_modifier_major`, awards **+10 XP** to all 3 tracks (`vanguard`, `slaughter`, `resilience`).
    - **Minor Lifeforce:** Consumes `lifeforce_modifier_minor`, awards **+5 XP** to all 3 tracks (`vanguard`, `slaughter`, `resilience`).
    - **Back out:** Zero cost, cancels action.
  - **Battle Victory (`on_combat_end_winner`):** Side knights gain +5 XP (`vanguard`); side commanders gain +6 XP (`vanguard`). Both have a 33% chance to harvest 1 Minor Lifeforce from the battlefield.
  - **Battle Defeat (`on_combat_end_loser`):** Surviving side knights and commanders gain +1 XP (`vanguard`) and +1 XP (`resilience`).
  - **Duel Victory (`on_death` / single combat):** Slaying opponent in single combat grants victor +6 XP (`slaughter`) and awards 1 Minor Lifeforce (if not already holding `lifestyle_blood_mage`).
  - **Tournament Participation/Victory (`on_travel_activity_complete`):** Completing a tournament activity grants +3 XP (`slaughter`).
  - **Yearly Survival Pulse (`blood_mage_yearly_events.004`):** Passive +1 XP per year in `resilience`. Active knight attunement (`vanguard_attuned`, `slaughter_attuned`, `resilience_attuned`) grants a 50% roll for +1 additional XP in that track.
  - **Minor Blood Magic Channeling (`bm_channel_lifeforce_enlightenment_minor`):** Spending Minor Lifeforce to boost Martial grants +1 `vanguard` XP, Prowess grants +1 `slaughter` XP, and all other boosts grant +1 `resilience` XP.
  - **Minor Restorative Magic (`heal_disease_minor`):** Blood Knights can expend Minor Lifeforce to heal minor wounds and illnesses on self or courtiers, gaining +2 `resilience` XP.

### Tracks Master Table

Each track has 10 tiers (10, 20, 30, ..., 100 XP). Every tier across all tracks includes the universal `health = 0.2`, `life_expectancy = 1`, and `monthly_prestige = 0.1`:

| Track | Theme & XP Sources | Tier Progression | Cap Total (Rank 10) |
| --- | --- | --- | --- |
| **`vanguard`** | Army battle command, participation & martial channeling | `advantage = 1` per tier<br>`martial = 1` every 2 tiers (20, 40, 60, 80, 100)<br>`martial_per_prestige_level = 1` at tier 50 & 100<br>`health = 0.2`<br>`life_expectancy = 1`<br>`monthly_prestige = 0.1` | +10 Advantage<br>+5 Martial<br>+2 Martial per Prestige level<br>+2.0 Health<br>+10 Life Expectancy<br>+1.0 Monthly Prestige |
| **`slaughter`** | Duels, tournament contests & prowess channeling | `prowess = 2` per tier<br>`prowess_per_prestige_level = 1` at tier 50 & 100<br>`health = 0.2`<br>`life_expectancy = 1`<br>`monthly_prestige = 0.1` | +20 Prowess (Net +15 with base)<br>+2 Prowess per Prestige level<br>+2.0 Health<br>+10 Life Expectancy<br>+1.0 Monthly Prestige |
| **`resilience`** | Yearly survival, battle recovery, minor healing & channeling | `years_of_fertility = 1`<br>`epidemic_resistance = 1`<br>`health = 0.2`<br>`life_expectancy = 1`<br>`monthly_prestige = 0.1` | +10 Years of Fertility<br>+10 Epidemic Resistance<br>+2.0 Health<br>+10 Life Expectancy<br>+1.0 Monthly Prestige |

Combined cap across all 3 tracks (30 tiers total):
- **Health:** +6.0 total (Net **+5.0** after -1 base penalty)
- **Life Expectancy:** +30 total (Net **+25** after -5 base penalty)
- **Monthly Prestige:** +3.0 total

## Key Mechanics

- **Minor Blood Magic & Lifeforce Decisions:**
  - `bm_cast_blood_magic_minor_decision`: Shown to characters holding `lifestyle_blood_mage` OR `lifestyle_blood_knight`. Requires Minor Lifeforce.
  - `bm_manifest_lifeforce_decision`: Available to Blood Knights (Piety rank >= 2, 100 Piety). Learning duel awards Minor Lifeforce on success and +3 `resilience` XP.
  - `seek_power_decision_blood_knight`: Pure Blood Knights (`NOT = { has_trait = lifestyle_blood_mage }`) can seek power in the wilderness once per year (1-year cooldown). In the encounter chain, Blood Knights can harvest Minor Lifeforce from beasts and ancient sources, or test martial prowess against wanderers (+slaughter/+vanguard XP). Blood Knights are strictly blocked from lifedraining and trait-draining travelers.
  - Channel Minor Lifeforce grants 5-year attribute enhancements and awards Blood Knight track XP without granting the Blood Mage trait.
  - Lifeforce Attunement offers parallel martial attunements: `vanguard_attuned` (+2 Advantage, +5% Knight Effectiveness), `slaughter_attuned` (+2 Prowess, +10% Dread Gain), and `resilience_attuned` (+0.25 Health, +2 Epidemic Resistance).
  - `heal_disease_minor`: Available to Blood Knights, expending Minor Lifeforce to cure `wounded_1`, `ill`, `scarred`, `lovers_pox`, and `gout_ridden` on self or courtiers (+2 `resilience` XP).
- **Trait Hierarchy & Safeguards:**
  - `lifestyle_blood_mage` is the superior trait and takes strict precedence. Characters holding both traits see Blood Mage decision variants and full ritual options.
  - Foundational scripted effects (`bm_add_blood_mage_xp_effect`, `bm_add_blood_empowerment_xp_effect`, `bm_add_blood_knight_xp_effect`) are strictly guarded with `has_trait` checks, preventing non-mages from acquiring the Blood Mage trait via track XP calls.
  - Blood Knights are strictly barred from high-tier rites: cannot lifedrain prisoners/courtiers, cannot trait-drain, cannot cast Major/Superior Blood Magic, and cannot forge blood golems.
- **Interactions (`bm_blood_knight_interactions.txt`):**
  - `make_blood_knight_interaction`: Bestows base trait at 0 XP. Actor must hold `lifestyle_blood_mage` and Major Lifeforce. Costs 100 Piety.
  - `empower_blood_knight_interaction`: Direct popup modal allowing choice between Major Lifeforce (+10 XP to all tracks), Minor Lifeforce (+5 XP to all tracks), or backing out.
- **Story Panel Integration:** Roster list effect `bm_refresh_blood_magic_rosters_effect` populates `bm_blood_retinue` using `has_trait = lifestyle_blood_knight`.
- **Zero Legacy Modifiers:** Pure trait implementation; `lifeforce_modifier_crimson_warrior` and `lifeforce_modifier_crimson_champion` are completely removed.

## Where the details live

| Concept | File |
| --- | --- |
| Trait definition & tracks | `common/traits/bm_blood_knight_trait.txt` |
| Trait XP helper macros | `common/scripted_effects/bm_trait_track_xp_gain_effects.txt` |
| Bestow & empower interactions | `common/character_interactions/bm_blood_knight_interactions.txt` |
| Battle progression hooks | `common/on_action/bm_combat_on_actions.txt` |
| Duel victory XP hook | `common/on_action/bm_duel_on_actions.txt` |
| Yearly survival XP pulse | `common/on_action/bm_yearly_pulse.txt`<br>`events/bm_yearly_events.txt` |
| Story retinue list population | `common/scripted_effects/bm_blood_mage_story_list_effects.txt` |
| English localization | `localization/english/bm_traits_l_english.yml`<br>`localization/english/bm_interactions_l_english.yml`<br>`localization/english/bm_debug_l_english.yml` |
| Debug XP decision | `common/decisions/bm_debug_decisions.txt` |

## Gotchas

- **Combat Side Iterators:** `every_side_knight` and `every_side_commander` evaluate in combat side scope (`on_combat_end_winner`, `on_combat_end_loser`).
- **Tournament Detection:** `on_travel_activity_complete` checks `involved_activity ?= { has_activity_type = activity_tournament }` when returning from tournament.
- **Self-Targeting:** Blood Mages who also possess `lifestyle_blood_knight` can empower themselves via the interactions or gain XP from battle/duel hooks directly.

## Not verified

- AI frequency of repeatedly infusing the same knight with major lifeforce under high AI wealth and piety.
