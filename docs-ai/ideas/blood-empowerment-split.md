# Ideas: Blood Empowerment Two-Trait Split (Transcendence vs. Sovereignty)

Living proposal for overhauling Blood Empowerment by splitting it into two mutually exclusive sister traits:

1. **`lifestyle_blood_transcendence`** (The Inner Vessel — Self / Adventurer / Personal Mastery)
2. **`lifestyle_blood_sovereignty`** (The Outer Dominion — Landed Overlord / Realm Projection)

Characters may only possess **one** of these two traits (`opposites = { ... }`), chosen upon first casting the major empowerment ritual. Both traits share the baseline progression, 4 universal core tracks, and contribute seamlessly toward high-tier spell unlocks (Education Enhancement, Blood Runes).

---

## 1. Problem Statement & Motivation

- **High Cost vs. Low Reward**: Currently, Blood Empowerment consumes 150 Piety + a **Major Lifeforce** per rank (10 XP). The returns (`+0.05` control, `+0.05` development, `+2.5%` domain tax per rank) feel marginal compared to other blood magic rituals.
- **Strictly Landed Bias**:
  - County control growth and capital development growth are useless for landless wanderers, mercenary bands, and traveling scholars.
  - Cultural fascination mult is 100% useless unless the character is the Cultural Head.
- **Missing Travel & Adventurer Integration**: Vanilla 1.20 (Roads to Power) introduced camp logistics, travel hazards, and adventurer contracts. Blood Empowerment currently ignores these systems entirely.
- **The Solution: 4 Shared Core Tracks + 3 Route-Specific Tracks (7 Tracks Total)**:
  - Consolidate universal blood magic disciplines (Dynasty, Martial, Experience, Charisma) into 4 shared tracks present on both traits.
  - Specialize the remaining 3 tracks around distinct playstyles: Bodily Mastery & Wilderness (Transcendence) vs. Realm & Dynastic Rule (Sovereignty).

---

## 2. Universal Baseline Buffs

Currently, every rank of every empowerment track grants:

- `+1 Life Expectancy`
- `+0.1 Monthly Piety`

To ensure every rank feels immediately impactful regardless of playstyle, consider adding one of the following to the **universal baseline** per rank:

- `character_travel_safety = 0.5` (+5 Travel Safety at track cap; empowered blood resists road hazards, exhaustion, and illness).
- _Alternative_: `prowess = 0.5` (+5 Prowess at track cap).

---

## 3. Structural Overview: The 4 + 3 Architecture

Each trait contains **7 tracks total** (10 ranks / up to 100 XP per track):

- **4 Shared Core Tracks**: Universal blood magic applications beneficial to both landless and landed characters.
- **3 Route-Specific Tracks**: Tailored explicitly to the chosen specialization.

```
                            [ Blood Empowerment ]
                                      │
            ┌─────────────────────────┴─────────────────────────┐
    [ 4 Shared Core Tracks ]                            [ 4 Shared Core Tracks ]
    • Dynasty (Genetics & Renown)                       • Dynasty (Genetics & Renown)
    • Martial (Knights & Advantage)                     • Martial (Knights & Advantage)
    • Experience (XP & Languages)                       • Experience (XP & Languages)
    • Charisma (Opinion & Sways)                        • Charisma (Opinion & Sways)
            │                                                   │
    [ 3 Transcendence Tracks ]                          [ 3 Sovereignty Tracks ]
    • Wayfarer (Travel & Movement)                      • Dominion (Control & Dread)
    • Sustenance (Camp & Provisions)                    • Prosperity (Taxes & Dev)
    • Occult Veil (Schemes & Duels)                     • Majesty (Vassals & Courts)
            │                                                   │
    lifestyle_blood_transcendence                       lifestyle_blood_sovereignty
       (Self / Adventurer / Wanderer)                      (Landed Overlord / Empire)
```

---

## 4. The 4 Shared Core Tracks (Both Traits)

These 4 tracks are identically available to both `lifestyle_blood_transcendence` and `lifestyle_blood_sovereignty`. Modifiers are listed **per rank** (10 ranks / up to 100 XP per track) and stack with the universal baseline.

|   #   | Track            | Theme                                     | Target Modifiers per Rank (10 Ranks Total)                                                                                                                          | Full Track Cap (100 XP)                                                                            |
| :---: | :--------------- | :---------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------- |
| **1** | **`dynasty`**    | Genetics, Kin Opinion & Renown            | • `positive_random_genetic_chance = 0.05`<br>• `positive_inactive_inheritance_chance = 0.05`<br>• `dynasty_opinion = 3`<br>• `monthly_dynasty_prestige_mult = 0.04` | +50% Positive Congenital<br>+50% Inactive Trait Inheritance<br>+30 Kin Opinion<br>+40% Renown Gain |
| **2** | **`martial`**    | Knights, Command & Battlefield Dominance  | • `knight_limit = 1` _(ranks 3, 6, 9)_<br>• `knight_effectiveness_mult = 0.06`<br>• `advantage = 1`                                                                 | +3 Knight Capacity<br>+60% Knight Effectiveness<br>+10 Commander Advantage                         |
| **3** | **`experience`** | Omniscience, Lifestyle Mastery & Tongues  | • `monthly_lifestyle_xp_gain_mult = 0.04`<br>• `learn_language_scheme_phase_duration_add = -5`<br>• `max_learn_language_schemes_add = 1` _(at rank 5)_              | +40% Lifestyle XP Gain<br>-50 Days Language Scheme Phase<br>+1 Max Language Schemes                |
| **4** | **`charisma`**   | Personal Aura, Seduction & Stress Control | • `stress_loss_mult = 0.05`<br>• `general_opinion = 2.5`<br>• `sway_scheme_power_mult = 0.05`                                                                       | +50% Stress Loss Rate<br>+25 General Opinion<br>+50% Sway Scheme Power                             |

---

## 5. Trait A: `lifestyle_blood_transcendence` (3 Specific Tracks)

> _"The blood mage turns their power inward, purifying their mortal biology into an enduring, terrifying vessel that thrives in the wilderness, single combat, and foreign lands."_

Tailored for **landless adventurers, traveling scholars, duelists, martial commanders, and sovereign rulers who prioritize personal invulnerability**.

|   #   | Track             | Theme                                     | Target Modifiers per Rank (10 Ranks Total)                                                                                                            | Full Track Cap (100 XP)                                                                         |
| :---: | :---------------- | :---------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------- |
| **1** | **`wayfarer`**    | Wilderness, Travel & Mobility             | • `character_travel_speed_mult = 0.04`<br>• `character_travel_safety = 2.5`<br>• `travel_attrition_reduction_mult = 0.05`                             | +40% Travel Speed Mult<br>+25 Flat Travel Safety<br>-50% Danger Attrition                       |
| **2** | **`sustenance`**  | Camp Logistics, Provisions & Independence | • `provisions_gain_mult = 0.05`<br>• `provisions_capacity_add = 40`<br>• `domicile_building_cost_mult = -0.03`<br>• `men_at_arms_maintenance = -0.03` | +50% Provisions Gain<br>+400 Max Provisions<br>-30% Camp Upgrade Cost<br>-30% MaA Maintenance   |
| **3** | **`occult_veil`** | Survival, Duels & Occult Subterfuge       | • `hostile_scheme_resistance_add = 3`<br>• `owned_scheme_secrecy_add = 5`<br>• `prowess = 1`<br>• `wound_recovery_mult = 0.05`                        | +30 Hostile Scheme Resistance<br>+50 Owned Scheme Secrecy<br>+10 Prowess<br>+50% Wound Recovery |

---

## 6. Trait B: `lifestyle_blood_sovereignty` (3 Specific Tracks)

> _"The blood mage projects their will upon the world around them, saturating their realm, subjects, institutions, and armies in imperial occult authority."_

Tailored for **landed kings, emperors, administrative governors, feudal overlords, and dynastic heads**.

|   #   | Track            | Theme                              | Target Modifiers per Rank (10 Ranks Total)                                                                                                                              | Full Track Cap (100 XP)                                                                                     |
| :---: | :--------------- | :--------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------- |
| **1** | **`dominion`**   | Territorial Iron Grip & Authority  | • `monthly_county_control_growth_add = 0.08`<br>• `dread_baseline_add = 4`<br>• `monthly_tyranny = -0.015`                                                              | +0.80 Monthly Control Growth<br>+40 Dread Baseline<br>-0.15 Tyranny Decay Rate                              |
| **2** | **`prosperity`** | Domain Extravagance & Construction | • `domain_tax_mult = 0.03`<br>• `gold_construction_cost = -0.03`<br>• `development_growth = 0.05`<br>• `character_capital_county_monthly_development_growth_add = 0.06` | +30% Domain Tax Mult<br>-30% Building & Holding Cost<br>+50% Development Growth<br>+0.60 Capital Dev Growth |
| **3** | **`majesty`**    | Imperial Court & Vassal Hierarchy  | • `vassal_opinion = 2.5`<br>• `short_reign_duration_mult = -0.05`<br>• `monthly_prestige_gain_mult = 0.05`<br>• `siege_phase_time = -0.03`                              | +25 Vassal Opinion<br>-50% Short Reign Duration<br>+50% Monthly Prestige<br>-30% Siege Phase Duration       |

---

## 7. Ritual Architecture & Selection Flow

```
                     [ Cast Major Blood Magic: Blood Empowerment ]
                                          │
                         Has Either Empowerment Trait?
                                 ├── NO  ──> Event: Fork in the Road
                                 │               ├── "Focus inward"   ──> Gains lifestyle_blood_transcendence
                                 │               └── "Focus outward"  ──> Gains lifestyle_blood_sovereignty
                                 │
                                 └── YES ──> Open Track Choice (Matching Trait Only)
                                                 └── Add +10 XP to Chosen Track
```

### Mutually Exclusive Logic

- The two traits define each other in `opposites = { ... }`.
- Once chosen, a blood mage cannot switch without an exceptionally costly or dangerous respec ritual (or never, locking in the character's metaphysical specialization).

---

## 4. Trait A: `lifestyle_blood_transcendence` (The Inner Vessel)

> _"The blood mage turns their power inward, purifying their mortal biology into an enduring, terrifying vessel that thrives in the wilderness, single combat, and foreign lands."_

Tailored for **landless adventurers, traveling scholars, duelists, martial commanders, and sovereign rulers who prioritize personal invulnerability**.

### 8 Proposed Tracks (5 Benefit Options per Track)

All candidate modifiers use verified vanilla 1.20 script keys. Values are listed **per rank** (10 ranks / up to 100 XP per track).

|   #   | Track Name & Theme                                | Option 1                                                               | Option 2                                                                      | Option 3                                                             | Option 4                                                                  | Option 5                                                                       |
| :---: | :------------------------------------------------ | :--------------------------------------------------------------------- | :---------------------------------------------------------------------------- | :------------------------------------------------------------------- | :------------------------------------------------------------------------ | :----------------------------------------------------------------------------- |
| **1** | **`vitality`**<br>_(Physical Perfection & Duels)_ | `prowess = 1`<br>_(+1 Prowess per 2 ranks)_                            | `health = 0.08`<br>_(+0.08 Base Health)_                                      | `wound_recovery_mult = 0.05`<br>_(+5% Wound Recovery)_               | `disease_resistance = 0.1`<br>_(+10% Illness Resistance)_                 | `prowess_per_prestige_level = 0.2`<br>_(Fame converts to Prowess)_             |
| **2** | **`wayfarer`**<br>_(Wilderness & Movement)_       | `character_travel_speed_mult = 0.04`<br>_(+4% Travel Speed Mult)_      | `character_travel_safety = 2.5`<br>_(+2.5 Travel Safety)_                     | `travel_attrition_reduction_mult = 0.05`<br>_(-5% Danger Attrition)_ | `character_travel_speed = 2`<br>_(+2 Flat Travel Speed)_                  | `movement_speed = 0.02`<br>_(+2% Army Movement Speed)_                         |
| **3** | **`sustenance`**<br>_(Logistics & Survival)_      | `provisions_gain_mult = 0.05`<br>_(+5% Provisions Gained)_             | `provisions_capacity_add = 40`<br>_(+40 Max Provisions)_                      | `provisions_loss_mult = -0.03`<br>_(-3% Provision Loss Rate)_        | `domicile_building_cost_mult = -0.03`<br>_(-3% Camp Upgrade Cost)_        | `men_at_arms_maintenance = -0.03`<br>_(-3% MaA Upkeep Cost)_                   |
| **4** | **`occult_veil`**<br>_(Survival & Subterfuge)_    | `hostile_scheme_resistance_add = 3`<br>_(+3 Scheme Resist)_            | `character_travel_safety = 2`<br>_(+2 Travel Safety)_                         | `owned_scheme_secrecy_add = 5`<br>_(+5 Scheme Secrecy)_              | `hostile_scheme_phase_duration_mult = -0.03`<br>_(-3% Scheme Phase Time)_ | `enemy_hostile_scheme_success_chance_add = -3`<br>_(-3% Enemy Success Chance)_ |
| **5** | **`mesmerism`**<br>_(Personal Magnetism)_         | `adventurer_contract_reward_mult = 0.05`<br>_(+5% Contract Rewards)_   | `sway_scheme_power_mult = 0.05`<br>_(+5% Sway Scheme Power)_                  | `courtier_and_guest_opinion = 3`<br>_(+3 Follower/Guest Opinion)_    | `general_opinion = 2.5`<br>_(+2.5 General Opinion)_                       | `mercenary_hire_cost_mult = -0.03`<br>_(-3% Sellsword Cost)_                   |
| **6** | **`transmutation`**<br>_(Bodily Alchemy & Mind)_  | `stress_loss_mult = 0.05`<br>_(+5% Stress Relief)_                     | `stress_gain_mult = -0.03`<br>_(-3% Stress Incurred)_                         | `monthly_lifestyle_xp_gain_mult = 0.03`<br>_(+3% All Lifestyle XP)_  | `all_skills = 0.5`<br>_(+1 All Stats per 2 ranks)_                        | `fertility = 0.02`<br>_(+2% Fertility)_                                        |
| **7** | **`blood_instinct`**<br>_(Combat Ferocity)_       | `maa_damage_mult = 0.03`<br>_(+3% MaA Damage)_                         | `knight_effectiveness_mult = 0.05`<br>_(+5% Knight Effectiveness)_            | `knight_limit = 1`<br>_(+1 Knight Cap at ranks 3, 6, 9)_             | `advantage = 1`<br>_(+1 Commander Advantage)_                             | `maa_pursuit_mult = 0.05`<br>_(+5% Fatal Casualties/Pursuit)_                  |
| **8** | **`lineage`**<br>_(Genetics & Kin Resonance)_     | `positive_random_genetic_chance = 0.05`<br>_(+5% Positive Congenital)_ | `positive_inactive_inheritance_chance = 0.05`<br>_(+5% Inactive Inheritance)_ | `dynasty_opinion = 3`<br>_(+3 Kin Opinion)_                          | `fertility = 0.03`<br>_(+3% Fertility)_                                   | `child_education_aptitude = 2`<br>_(+2 Ward Education Success)_                |

---

## 5. Trait B: `lifestyle_blood_sovereignty` (The Outer Dominion)

> _"The blood mage projects their will upon the world around them, saturating their realm, subjects, institutions, and armies in imperial occult authority."_

Tailored for **landed kings, emperors, administrative governors, feudal overlords, and dynastic heads**.

### 8 Proposed Tracks (5 Benefit Options per Track)

All candidate modifiers use verified vanilla 1.20 script keys. Values are listed **per rank** (10 ranks / up to 100 XP per track).

|   #   | Track Name & Theme                                   | Option 1                                                                | Option 2                                                        | Option 3                                                               | Option 4                                                                      | Option 5                                                                                         |
| :---: | :--------------------------------------------------- | :---------------------------------------------------------------------- | :-------------------------------------------------------------- | :--------------------------------------------------------------------- | :---------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------- |
| **1** | **`dominion`**<br>_(Territorial Iron Grip)_          | `monthly_county_control_growth_add = 0.08`<br>_(+0.08 Control Growth)_  | `dread_baseline_add = 4`<br>_(+4 Dread Baseline)_               | `monthly_tyranny = -0.015`<br>_(-0.015 Tyranny Decay)_                 | `garrison_size = 0.05`<br>_(+5% Holding Garrison)_                            | `county_opinion_add = 2`<br>_(+2 Popular Opinion)_                                               |
| **2** | **`prosperity`**<br>_(Domain & Fiscal Extravagance)_ | `domain_tax_mult = 0.03`<br>_(+3% Domain Tax)_                          | `gold_construction_cost = -0.03`<br>_(-3% Building Cost)_       | `holding_build_speed = 0.05`<br>_(+5% Build Speed)_                    | `development_growth = 0.05`<br>_(+5% Domain Development)_                     | `character_capital_county_monthly_development_growth_add = 0.06`<br>_(+0.06 Capital Dev Growth)_ |
| **3** | **`majesty`**<br>_(Imperial Court & Aura)_           | `vassal_opinion = 2.5`<br>_(+2.5 Vassal Opinion)_                       | `monthly_prestige_gain_mult = 0.05`<br>_(+5% Monthly Prestige)_ | `general_opinion = 2.5`<br>_(+2.5 General Opinion)_                    | `short_reign_duration_mult = -0.05`<br>_(-5% Short Reign Penalty)_            | `courtier_and_guest_opinion = 3`<br>_(+3 Courtier Opinion)_                                      |
| **4** | **`hegemony`**<br>_(Armies & Battlefield Command)_   | `knight_effectiveness_mult = 0.06`<br>_(+6% Knight Effectiveness)_      | `levy_size = 0.04`<br>_(+4% Realm Levy Size)_                   | `advantage = 1`<br>_(+1 Commander Advantage)_                          | `siege_phase_time = -0.03`<br>_(-3% Siege Phase Duration)_                    | `offensive_war_opinion_mult = -0.05`<br>_(-5% War Malus)_                                        |
| **5** | **`shadow_throne`**<br>_(Court Intrigue & Terror)_   | `dread_gain_mult = 0.06`<br>_(+6% Dread Gain)_                          | `owned_scheme_secrecy_add = 6`<br>_(+6 Scheme Secrecy)_         | `hostile_scheme_power_mult = 0.04`<br>_(+4% Hostile Scheme Power)_     | `dread_baseline_add = 4`<br>_(+4 Dread Baseline)_                             | `agent_join_chance = 3`<br>_(+3 Agent Invitation)_                                               |
| **6** | **`sacred_rule`**<br>_(Religious Hierarchy & Zeal)_  | `monthly_piety_gain_mult = 0.06`<br>_(+6% Monthly Piety Mult)_          | `same_faith_opinion = 3`<br>_(+3 Faithful Opinion)_             | `holy_order_hire_cost_mult = -0.04`<br>_(-4% Holy Order Cost)_         | `clergy_opinion = 3`<br>_(+3 Clergy Opinion)_                                 | `county_faith_conversion_speed_mult = 0.05`<br>_(+5% County Conversion)_                         |
| **7** | **`renaissance`**<br>_(Cultural Golden Age)_         | `cultural_head_fascination_mult = 0.06`<br>_(+6% Cultural Fascination)_ | `development_growth = 0.05`<br>_(+5% Realm Development)_        | `monthly_lifestyle_xp_gain_mult = 0.03`<br>_(+3% Lifestyle XP Mult)_   | `different_culture_opinion = 2.5`<br>_(+2.5 Foreign Culture Opinion)_         | `cultural_acceptance_gain_mult = 0.05`<br>_(+5% Acceptance Gain)_                                |
| **8** | **`dynasty`**<br>_(Noble Bloodline & Renown)_        | `monthly_dynasty_prestige_mult = 0.04`<br>_(+4% Renown Gain)_           | `dynasty_opinion = 3`<br>_(+3 Kin Opinion)_                     | `positive_random_genetic_chance = 0.05`<br>_(+5% Positive Congenital)_ | `positive_inactive_inheritance_chance = 0.05`<br>_(+5% Inactive Inheritance)_ | `child_education_aptitude = 2`<br>_(+2 Ward Education Success)_                                  |

---

## 6. Shared Engine & Spell Integration

Both traits plug into the mod's existing ritual gates without duplicate logic or orphaned checks.

### Centralized XP Gate Script Value

Any ritual checking empowerment XP (e.g. `bm_enhance_education_decision` or `bm_blood_rune_minimum_xp`) evaluates total earned empowerment XP across all 7 tracks via a single script value:

```pdx
bm_blood_empowerment_total_xp = {
    value = 0
    if = {
        limit = { has_trait = lifestyle_blood_transcendence }
        add = "lifestyle_blood_transcendence_xp_sum"
    }
    if = {
        limit = { has_trait = lifestyle_blood_sovereignty }
        add = "lifestyle_blood_sovereignty_xp_sum"
    }
}
```

### Max-Cap Fallback Buff

When all 7 tracks of the chosen trait reach the 100 XP cap (700 XP total), casting the Major Blood Empowerment ritual grants:

- `temporary_buff_self` (+2 all stats, +4 prowess for 10 years).
- Roll chance for permanent attribute gains (+1 to a random attribute).
