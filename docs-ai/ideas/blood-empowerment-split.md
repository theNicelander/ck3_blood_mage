# Ideas: Blood Empowerment Two-Trait Split (Transcendence vs. Sovereignty)

Living proposal for overhauling Blood Empowerment by splitting it into two mutually exclusive sister traits:
1. **`lifestyle_blood_transcendence`** (The Inner Vessel — Self / Adventurer / Personal Mastery)
2. **`lifestyle_blood_sovereignty`** (The Outer Dominion — Exterior / Landed Overlord / Realm Projection)

Characters may only possess **one** of these two traits (`opposites = { ... }`), chosen upon first casting the major empowerment ritual. Both traits share the baseline progression and contribute seamlessly toward high-tier spell unlocks (Education Enhancement, Blood Runes).

---

## 1. Problem Statement & Motivation

- **High Cost vs. Low Reward**: Currently, Blood Empowerment consumes 150 Piety + a **Major Lifeforce** per rank (10 XP). The returns (`+0.05` control, `+0.05` development, `+2.5%` domain tax per rank) feel marginal compared to other blood magic rituals.
- **Strictly Landed Bias**:
  - County control growth and capital development growth are useless for landless wanderers, mercenary bands, and traveling scholars.
  - Cultural fascination mult is 100% useless unless the character is the Cultural Head.
- **Missing Travel & Adventurer Integration**: Vanilla 1.20 (Roads to Power) introduced camp logistics, travel hazards, and adventurer contracts. Blood Empowerment currently ignores these systems entirely.
- **The Solution**: Rather than compromising every track with hybrid compromises, cleanly fork the fantasy into **Internal Bodily Mastery** (Transcendence) and **External Realm Domination** (Sovereignty).

---

## 2. Universal Baseline Buffs

Currently, every rank of every empowerment track grants:
- `+1 Life Expectancy`
- `+0.1 Monthly Piety`

To ensure every rank feels immediately impactful regardless of playstyle, consider adding one of the following to the **universal baseline** per rank:
- `character_travel_safety = 0.5` (+5 Travel Safety at track cap; empowered blood resists road hazards, exhaustion, and illness).
- *Alternative*: `prowess = 0.5` (+5 Prowess at track cap).

---

## 3. Ritual Architecture & Selection Flow

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

> *"The blood mage turns their power inward, purifying their mortal biology into an enduring, terrifying vessel that thrives in the wilderness, single combat, and foreign lands."*

Tailored for **landless adventurers, traveling scholars, duelists, martial commanders, and sovereign rulers who prioritize personal invulnerability**.

### 8 Proposed Tracks (5 Benefit Options per Track)
All candidate modifiers use verified vanilla 1.20 script keys. Values are listed **per rank** (10 ranks / up to 100 XP per track).

| # | Track Name & Theme | Option 1 | Option 2 | Option 3 | Option 4 | Option 5 |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | **`vitality`**<br>*(Physical Perfection & Duels)* | `prowess = 1`<br>*(+1 Prowess per 2 ranks)* | `health = 0.08`<br>*(+0.08 Base Health)* | `wound_recovery_mult = 0.05`<br>*(+5% Wound Recovery)* | `disease_resistance = 0.1`<br>*(+10% Illness Resistance)* | `prowess_per_prestige_level = 0.2`<br>*(Fame converts to Prowess)* |
| **2** | **`wayfarer`**<br>*(Wilderness & Movement)* | `character_travel_speed_mult = 0.04`<br>*(+4% Travel Speed Mult)* | `character_travel_safety = 2.5`<br>*(+2.5 Travel Safety)* | `travel_attrition_reduction_mult = 0.05`<br>*(-5% Danger Attrition)* | `character_travel_speed = 2`<br>*(+2 Flat Travel Speed)* | `movement_speed = 0.02`<br>*(+2% Army Movement Speed)* |
| **3** | **`sustenance`**<br>*(Logistics & Survival)* | `provisions_gain_mult = 0.05`<br>*(+5% Provisions Gained)* | `provisions_capacity_add = 40`<br>*(+40 Max Provisions)* | `provisions_loss_mult = -0.03`<br>*(-3% Provision Loss Rate)* | `domicile_building_cost_mult = -0.03`<br>*(-3% Camp Upgrade Cost)* | `men_at_arms_maintenance = -0.03`<br>*(-3% MaA Upkeep Cost)* |
| **4** | **`occult_veil`**<br>*(Survival & Subterfuge)* | `hostile_scheme_resistance_add = 3`<br>*(+3 Scheme Resist)* | `character_travel_safety = 2`<br>*(+2 Travel Safety)* | `owned_scheme_secrecy_add = 5`<br>*(+5 Scheme Secrecy)* | `hostile_scheme_phase_duration_mult = -0.03`<br>*(-3% Scheme Phase Time)* | `enemy_hostile_scheme_success_chance_add = -3`<br>*(-3% Enemy Success Chance)* |
| **5** | **`mesmerism`**<br>*(Personal Magnetism)* | `adventurer_contract_reward_mult = 0.05`<br>*(+5% Contract Rewards)* | `sway_scheme_power_mult = 0.05`<br>*(+5% Sway Scheme Power)* | `courtier_and_guest_opinion = 3`<br>*(+3 Follower/Guest Opinion)* | `general_opinion = 2.5`<br>*(+2.5 General Opinion)* | `mercenary_hire_cost_mult = -0.03`<br>*(-3% Sellsword Cost)* |
| **6** | **`transmutation`**<br>*(Bodily Alchemy & Mind)* | `stress_loss_mult = 0.05`<br>*(+5% Stress Relief)* | `stress_gain_mult = -0.03`<br>*(-3% Stress Incurred)* | `monthly_lifestyle_xp_gain_mult = 0.03`<br>*(+3% All Lifestyle XP)* | `all_skills = 0.5`<br>*(+1 All Stats per 2 ranks)* | `fertility = 0.02`<br>*(+2% Fertility)* |
| **7** | **`blood_instinct`**<br>*(Combat Ferocity)* | `maa_damage_mult = 0.03`<br>*(+3% MaA Damage)* | `knight_effectiveness_mult = 0.05`<br>*(+5% Knight Effectiveness)* | `knight_limit = 1`<br>*(+1 Knight Cap at ranks 3, 6, 9)* | `advantage = 1`<br>*(+1 Commander Advantage)* | `maa_pursuit_mult = 0.05`<br>*(+5% Fatal Casualties/Pursuit)* |
| **8** | **`lineage`**<br>*(Genetics & Kin Resonance)* | `positive_random_genetic_chance = 0.05`<br>*(+5% Positive Congenital)* | `positive_inactive_inheritance_chance = 0.05`<br>*(+5% Inactive Inheritance)* | `dynasty_opinion = 3`<br>*(+3 Kin Opinion)* | `fertility = 0.03`<br>*(+3% Fertility)* | `child_education_aptitude = 2`<br>*(+2 Ward Education Success)* |

---

## 5. Trait B: `lifestyle_blood_sovereignty` (The Outer Dominion)

> *"The blood mage projects their will upon the world around them, saturating their realm, subjects, institutions, and armies in imperial occult authority."*

Tailored for **landed kings, emperors, administrative governors, feudal overlords, and dynastic heads**.

### 8 Proposed Tracks (5 Benefit Options per Track)
All candidate modifiers use verified vanilla 1.20 script keys. Values are listed **per rank** (10 ranks / up to 100 XP per track).

| # | Track Name & Theme | Option 1 | Option 2 | Option 3 | Option 4 | Option 5 |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | **`dominion`**<br>*(Territorial Iron Grip)* | `monthly_county_control_growth_add = 0.08`<br>*(+0.08 Control Growth)* | `dread_baseline_add = 4`<br>*(+4 Dread Baseline)* | `monthly_tyranny = -0.015`<br>*(-0.015 Tyranny Decay)* | `garrison_size = 0.05`<br>*(+5% Holding Garrison)* | `county_opinion_add = 2`<br>*(+2 Popular Opinion)* |
| **2** | **`prosperity`**<br>*(Domain & Fiscal Extravagance)* | `domain_tax_mult = 0.03`<br>*(+3% Domain Tax)* | `gold_construction_cost = -0.03`<br>*(-3% Building Cost)* | `holding_build_speed = 0.05`<br>*(+5% Build Speed)* | `development_growth = 0.05`<br>*(+5% Domain Development)* | `character_capital_county_monthly_development_growth_add = 0.06`<br>*(+0.06 Capital Dev Growth)* |
| **3** | **`majesty`**<br>*(Imperial Court & Aura)* | `vassal_opinion = 2.5`<br>*(+2.5 Vassal Opinion)* | `monthly_prestige_gain_mult = 0.05`<br>*(+5% Monthly Prestige)* | `general_opinion = 2.5`<br>*(+2.5 General Opinion)* | `short_reign_duration_mult = -0.05`<br>*(-5% Short Reign Penalty)* | `courtier_and_guest_opinion = 3`<br>*(+3 Courtier Opinion)* |
| **4** | **`hegemony`**<br>*(Armies & Battlefield Command)* | `knight_effectiveness_mult = 0.06`<br>*(+6% Knight Effectiveness)* | `levy_size = 0.04`<br>*(+4% Realm Levy Size)* | `advantage = 1`<br>*(+1 Commander Advantage)* | `siege_phase_time = -0.03`<br>*(-3% Siege Phase Duration)* | `offensive_war_opinion_mult = -0.05`<br>*(-5% War Malus)* |
| **5** | **`shadow_throne`**<br>*(Court Intrigue & Terror)* | `dread_gain_mult = 0.06`<br>*(+6% Dread Gain)* | `owned_scheme_secrecy_add = 6`<br>*(+6 Scheme Secrecy)* | `hostile_scheme_power_mult = 0.04`<br>*(+4% Hostile Scheme Power)* | `dread_baseline_add = 4`<br>*(+4 Dread Baseline)* | `agent_join_chance = 3`<br>*(+3 Agent Invitation)* |
| **6** | **`sacred_rule`**<br>*(Religious Hierarchy & Zeal)* | `monthly_piety_gain_mult = 0.06`<br>*(+6% Monthly Piety Mult)* | `same_faith_opinion = 3`<br>*(+3 Faithful Opinion)* | `holy_order_hire_cost_mult = -0.04`<br>*(-4% Holy Order Cost)* | `clergy_opinion = 3`<br>*(+3 Clergy Opinion)* | `county_faith_conversion_speed_mult = 0.05`<br>*(+5% County Conversion)* |
| **7** | **`renaissance`**<br>*(Cultural Golden Age)* | `cultural_head_fascination_mult = 0.06`<br>*(+6% Cultural Fascination)* | `development_growth = 0.05`<br>*(+5% Realm Development)* | `monthly_lifestyle_xp_gain_mult = 0.03`<br>*(+3% Lifestyle XP Mult)* | `different_culture_opinion = 2.5`<br>*(+2.5 Foreign Culture Opinion)* | `cultural_acceptance_gain_mult = 0.05`<br>*(+5% Acceptance Gain)* |
| **8** | **`dynasty`**<br>*(Noble Bloodline & Renown)* | `monthly_dynasty_prestige_mult = 0.04`<br>*(+4% Renown Gain)* | `dynasty_opinion = 3`<br>*(+3 Kin Opinion)* | `positive_random_genetic_chance = 0.05`<br>*(+5% Positive Congenital)* | `positive_inactive_inheritance_chance = 0.05`<br>*(+5% Inactive Inheritance)* | `child_education_aptitude = 2`<br>*(+2 Ward Education Success)* |

---

## 6. Shared Engine & Spell Integration

Both traits plug into the mod's existing ritual gates without duplicate logic or orphaned checks.

### Centralized XP Gate Script Value
Any ritual checking empowerment XP (e.g. `bm_enhance_education_decision` or `bm_blood_rune_minimum_xp`) evaluates total earned empowerment XP via a single script value:
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
When all 8 tracks of the chosen trait reach the 100 XP cap, casting the Major Blood Empowerment ritual grants:
- `temporary_buff_self` (+2 all stats, +4 prowess for 10 years).
- Roll chance for permanent attribute gains (+1 to a random attribute).
