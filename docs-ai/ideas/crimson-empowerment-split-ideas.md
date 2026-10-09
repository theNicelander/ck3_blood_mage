# Ideas: Crimson Empowerment Two-Trait Split (Internal vs. External)

Living proposal for splitting `lifestyle_crimson_empowerment` into two mutually exclusive sister traits:
1. **`lifestyle_crimson_transcendence`** (The Inner Vessel — Self / Adventurer / Personal Mastery)
2. **`lifestyle_crimson_sovereignty`** (The Outer Dominion — Exterior / Landed Overlord / Realm Projection)

Characters may only possess **one** of these two traits (`opposites = { ... }`), chosen upon first casting the major empowerment ritual. Both traits share the baseline (+1 Life Expectancy, +0.1 Piety per rank) and contribute toward high-tier spell unlocks (Education Enhancement, Blood Runes).

---

## Part 1: Trait A — `lifestyle_crimson_transcendence` (The Inner Vessel)

> *"The blood mage turns their power inward, purifying their mortal biology into an enduring, terrifying vessel that thrives in the wilderness, single combat, and foreign lands."*

### 8 Proposed Tracks (5 Benefit Ideas per Track)

| # | Track Name & Theme | Option 1 | Option 2 | Option 3 | Option 4 | Option 5 |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | **`vitality`**<br>*(Physical Perfection & Duels)* | `prowess = 1`<br>*(+1 Prowess every 2 ranks)* | `health = 0.08`<br>*(+0.08 Base Health)* | `wound_recovery_mult = 0.05`<br>*(+5% Wound Recovery)* | `disease_resistance = 0.1`<br>*(+10% Illness Resistance)* | `prowess_per_prestige_level = 0.2`<br>*(Fame converts to Prowess)* |
| **2** | **`wayfarer`**<br>*(Wilderness & Movement)* | `character_travel_speed_mult = 0.04`<br>*(+4% Travel Speed Mult)* | `character_travel_safety = 2.5`<br>*(+2.5 Travel Safety)* | `travel_attrition_reduction_mult = 0.05`<br>*(-5% Travel Danger Attrition)* | `character_travel_speed = 2`<br>*(+2 Flat Travel Speed)* | `movement_speed = 0.02`<br>*(+2% Army Movement Speed)* |
| **3** | **`sustenance`**<br>*(Logistics & Survival)* | `provisions_gain_mult = 0.05`<br>*(+5% Provisions Gained)* | `provisions_capacity_add = 40`<br>*(+40 Max Provisions)* | `provisions_loss_mult = -0.03`<br>*(-3% Provision Loss Rate)* | `domicile_building_cost_mult = -0.03`<br>*(-3% Camp Improvement Cost)* | `men_at_arms_maintenance = -0.03`<br>*(-3% MaA Upkeep Cost)* |
| **4** | **`occult_veil`**<br>*(Survival & Subterfuge)* | `hostile_scheme_resistance_add = 3`<br>*(+3 Hostile Scheme Resist)* | `character_travel_safety = 2`<br>*(+2 Travel Safety)* | `owned_scheme_secrecy_add = 5`<br>*(+5 Scheme Secrecy)* | `hostile_scheme_phase_duration_mult = -0.03`<br>*(-3% Scheme Phase Time)* | `enemy_hostile_scheme_success_chance_add = -3`<br>*(-3% Enemy Success Chance)* |
| **5** | **`mesmerism`**<br>*(Personal Magnetism)* | `adventurer_contract_reward_mult = 0.05`<br>*(+5% Contract Rewards)* | `sway_scheme_power_mult = 0.05`<br>*(+5% Sway Scheme Power)* | `courtier_and_guest_opinion = 3`<br>*(+3 Follower / Guest Opinion)* | `general_opinion = 2.5`<br>*(+2.5 General Opinion)* | `mercenary_hire_cost_mult = -0.03`<br>*(-3% Sellsword Cost)* |
| **6** | **`transmutation`**<br>*(Bodily Alchemy & Mind)* | `stress_loss_mult = 0.05`<br>*(+5% Stress Relief)* | `stress_gain_mult = -0.03`<br>*(-3% Stress Incurred)* | `monthly_lifestyle_xp_gain_mult = 0.03`<br>*(+3% All Lifestyle XP)* | `all_skills = 0.5`<br>*(+1 All Stats every 2 ranks)* | `fertility = 0.02`<br>*(+2% Fertility)* |
| **7** | **`blood_instinct`**<br>*(Combat Ferocity)* | `maa_damage_mult = 0.03`<br>*(+3% Men-at-Arms Damage)* | `knight_effectiveness_mult = 0.05`<br>*(+5% Knight Effectiveness)* | `knight_limit = 1`<br>*(+1 Knight Cap at ranks 3, 6, 9)* | `advantage = 1`<br>*(+1 Commander Advantage)* | `maa_pursuit_mult = 0.05`<br>*(+5% Pursuit / Fatal Casualties)* |
| **8** | **`lineage`**<br>*(Genetics & Kin Resonance)* | `positive_random_genetic_chance = 0.05`<br>*(+5% Positive Congenital)* | `positive_inactive_inheritance_chance = 0.05`<br>*(+5% Inactive Inheritance)* | `dynasty_opinion = 3`<br>*(+3 Dynasty / Kin Opinion)* | `fertility = 0.03`<br>*(+3% Fertility)* | `child_education_aptitude = 2`<br>*(+2 Ward / Child Education)* |

---

## Part 2: Trait B — `lifestyle_crimson_sovereignty` (The Outer Dominion)

> *"The blood mage projects their will upon the world around them, saturating their realm, subjects, institutions, and armies in imperial occult authority."*

### 8 Proposed Tracks (5 Benefit Ideas per Track)

| # | Track Name & Theme | Option 1 | Option 2 | Option 3 | Option 4 | Option 5 |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | **`dominion`**<br>*(Territorial Iron Grip)* | `monthly_county_control_growth_add = 0.08`<br>*(+0.08 County Control Growth)* | `dread_baseline_add = 4`<br>*(+4 Dread Baseline)* | `monthly_tyranny = -0.015`<br>*(-0.015 Tyranny Decay)* | `garrison_size = 0.05`<br>*(+5% Holding Garrison Size)* | `county_opinion_add = 2`<br>*(+2 Popular Opinion)* |
| **2** | **`prosperity`**<br>*(Domain & Fiscal Extravagance)* | `domain_tax_mult = 0.03`<br>*(+3% Domain Tax)* | `gold_construction_cost = -0.03`<br>*(-3% Building Cost)* | `holding_build_speed = 0.05`<br>*(+5% Construction Speed)* | `development_growth = 0.05`<br>*(+5% Domain Development)* | `character_capital_county_monthly_development_growth_add = 0.06`<br>*(+0.06 Capital Dev Growth)* |
| **3** | **`majesty`**<br>*(Imperial Court & Aura)* | `vassal_opinion = 2.5`<br>*(+2.5 Direct Vassal Opinion)* | `monthly_prestige_gain_mult = 0.05`<br>*(+5% Monthly Prestige)* | `general_opinion = 2.5`<br>*(+2.5 General Opinion)* | `short_reign_duration_mult = -0.05`<br>*(-5% Short Reign Penalty)* | `courtier_and_guest_opinion = 3`<br>*(+3 Courtier Opinion)* |
| **4** | **`hegemony`**<br>*(Armies & Battlefield Command)* | `knight_effectiveness_mult = 0.06`<br>*(+6% Knight Effectiveness)* | `levy_size = 0.04`<br>*(+4% Realm Levy Size)* | `advantage = 1`<br>*(+1 Commander Advantage)* | `siege_phase_time = -0.03`<br>*(-3% Siege Phase Duration)* | `offensive_war_opinion_mult = -0.05`<br>*(-5% Offensive War Malus)* |
| **5** | **`shadow_throne`**<br>*(Court Intrigue & State Terror)* | `dread_gain_mult = 0.06`<br>*(+6% Dread Gain)* | `owned_scheme_secrecy_add = 6`<br>*(+6 Scheme Secrecy)* | `hostile_scheme_power_mult = 0.04`<br>*(+4% Hostile Scheme Power)* | `dread_baseline_add = 4`<br>*(+4 Dread Baseline)* | `agent_join_chance = 3`<br>*(+3 Agent Invitation Acceptance)* |
| **6** | **`sacred_rule`**<br>*(Religious Hierarchy & Zeal)* | `monthly_piety_gain_mult = 0.06`<br>*(+6% Monthly Piety Mult)* | `same_faith_opinion = 3`<br>*(+3 Faithful Opinion)* | `holy_order_hire_cost_mult = -0.04`<br>*(-4% Holy Order Cost)* | `clergy_opinion = 3`<br>*(+3 Clergy Opinion)* | `county_faith_conversion_speed_mult = 0.05`<br>*(+5% County Conversion Speed)* |
| **7** | **`renaissance`**<br>*(Cultural Golden Age)* | `cultural_head_fascination_mult = 0.06`<br>*(+6% Cultural Fascination)* | `development_growth = 0.05`<br>*(+5% All Holdings Development)* | `monthly_lifestyle_xp_gain_mult = 0.03`<br>*(+3% Lifestyle XP Mult)* | `different_culture_opinion = 2.5`<br>*(+2.5 Foreign Culture Opinion)* | `cultural_acceptance_gain_mult = 0.05`<br>*(+5% Cultural Acceptance Gain)* |
| **8** | **`dynasty`**<br>*(Noble Bloodline & Renown)* | `monthly_dynasty_prestige_mult = 0.04`<br>*(+4% Dynasty Renown Gain)* | `dynasty_opinion = 3`<br>*(+3 Dynasty Opinion)* | `positive_random_genetic_chance = 0.05`<br>*(+5% Positive Congenital)* | `positive_inactive_inheritance_chance = 0.05`<br>*(+5% Inactive Inheritance)* | `child_education_aptitude = 2`<br>*(+2 Ward Education Success)* |

---

## Part 3: Architecture & Flow

```
                     [ Cast Major Blood Magic: Self-Empowerment ]
                                          │
                         Has Either Empowerment Trait?
                                ├── NO  ──> Event: Fork in the Road
                                │               ├── "Focus inward"   ──> Gains lifestyle_crimson_transcendence
                                │               └── "Focus outward"  ──> Gains lifestyle_crimson_sovereignty
                                │
                                └── YES ──> Open Track Choice (Matching Trait Only)
                                                └── Add +10 XP to Chosen Track
```

### Shared Engine Integration
- **Spell Gate Unlocks**: Both traits share the same thresholds. Any ritual checking `required_xp_improve_education` or `bm_blood_rune_minimum_xp` checks the combined XP sum:
  ```pdx
  bm_crimson_empowerment_total_xp = {
      value = 0
      add = "lifestyle_crimson_transcendence_xp_sum"
      add = "lifestyle_crimson_sovereignty_xp_sum"
  }
  ```
- **Fallback Buff**: If all 8 tracks of the chosen trait are at 100 XP, the fallback option grants `temporary_buff_self` (+2 all stats, +4 prowess for 10 years) plus roll chances for permanent attributes.
