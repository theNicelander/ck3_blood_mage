# Ideas: Blood Empowerment Two-Trait Split (Transcendence vs. Sovereignty)

> **Status:** Speculative / Future Roadmap. The core 5 disciplines (`dynasty`, `mastery`, `presence`, `prosperity`, `shadows`) and universal baseline (`@bm_common_*`) have been implemented directly onto `lifestyle_blood_empowerment` in the active codebase. This document preserves the architectural proposal and track specifications for a future expansion into specialized branch traits (`lifestyle_blood_transcendence` vs. `lifestyle_blood_sovereignty`).

Living proposal for overhauling Blood Empowerment by splitting it into two mutually exclusive sister traits:
1. **`lifestyle_blood_transcendence`** (The Inner Vessel — Self / Adventurer / Personal Mastery)
2. **`lifestyle_blood_sovereignty`** (The Outer Dominion — Landed Overlord / Realm Projection)

Characters may only possess **one** of these two traits (`opposites = { ... }`), chosen upon first casting the major empowerment ritual. Both traits share the baseline progression, 5 universal core tracks, and contribute seamlessly toward high-tier spell unlocks (Education Enhancement, Blood Runes).

---

## 1. Problem Statement & Motivation

- **High Cost vs. Low Reward**: Currently, Blood Empowerment consumes 150 Piety + a **Major Lifeforce** per rank (10 XP). The returns (`+0.05` control, `+0.05` development, `+2.5%` domain tax per rank) feel marginal compared to other blood magic rituals.
- **Strictly Landed Bias**:
  - County control growth and capital development growth are useless for landless wanderers, mercenary bands, and traveling scholars.
  - Cultural fascination mult is 100% useless unless the character is the Cultural Head.
- **Missing Travel & Adventurer Integration**: Vanilla 1.20 (Roads to Power) introduced camp logistics, travel hazards, and adventurer contracts. Blood Empowerment currently ignores these systems entirely.
- **Overlap with Blood Knight**: Dedicated military command (knights, combat advantage, MaA lethality) belongs properly in `lifestyle_blood_knight`, not Blood Empowerment.
- **The Solution: 5 Shared Core Tracks + 3 Route-Specific Tracks (8 Tracks Total per Trait)**:
  - Consolidate universal disciplines (Dynasty, Mastery, Presence, Prosperity/Stewardship, Shadows/Occult Veil) into 5 shared tracks present on both traits.
  - Specialize the remaining 3 tracks around distinct playstyles: Bodily Mastery & Wilderness (Transcendence) vs. Realm & Dynastic Rule (Sovereignty).

---

## 2. Universal Baseline Buffs & Single Source of Truth

Every rank (tick) of every empowerment track provides the exact same core physiological baseline benefits as the `lifestyle_blood_mage` trait:
- `health = 0.1` (+0.1 Health per rank / +1.0 per full track of 10 ranks)
- `life_expectancy = 2` (+2 Life Expectancy per rank / +20 years per full track)
- `years_of_fertility = 1` (+1 Year of Fertility per rank / +10 years per full track)
- `epidemic_resistance = 1` (+1 Epidemic Resistance per rank / +10 per full track)

### Design Rationale
- **Immediate Return on Investment**: Consuming Piety and Major Lifeforce guarantees meaningful bodily empowerment (vitality, longevity, fertility, plague resistance) on *every single purchase*, regardless of which track is chosen.
- **Thematic Consistency**: Directly mirrors the ancient/enlightenment baseline from `lifestyle_blood_mage` (`ancient` track ranks grant these exact four parameters), reinforcing that deep blood mastery continually preserves and refines mortal biology.
- **Compounding Immortality Arc**: Completing tracks rewards the player with substantial longevity and resilience (+20 to +160 years life expectancy across all 8 tracks), perfectly aligning with the mod's philosophy of *earned power over godmode*.

### Defining Once (Single Source of Truth)
To eliminate duplicate numbers across dozens of track rank blocks and keep balance adjustments centralized in a single location, we define these once using Clausewitz script preprocessor variables (`@` syntax), following the proven pattern in `common/traits/bm_blood_knight_trait.txt`:

#### 1. Central Definition
Defined once at the head of the trait file(s) or in a shared trait definitions header:
```pdx
# Universal Blood Empowerment baseline modifiers per rank (matches lifestyle_blood_mage)
@bm_common_health = 0.1
@bm_common_life_expectancy = 2
@bm_common_years_of_fertility = 1
@bm_common_epidemic_resistance = 1
```

#### 2. Track Rank Reference
Each rank milestone (10, 20, 30... 100) across all tracks references the variables directly alongside its track-specific modifiers:
```pdx
tracks = {
    wayfarer = {
        10 = {
            # common
            health = @bm_common_health
            life_expectancy = @bm_common_life_expectancy
            years_of_fertility = @bm_common_years_of_fertility
            epidemic_resistance = @bm_common_epidemic_resistance

            # specific
            character_travel_safety = 2.5
        }
        ...
    }
}
```

---

## 3. Structural Overview: The 5 + 3 Architecture

Each trait contains **8 tracks total** (10 ranks / up to 100 XP per track):
- **5 Shared Core Tracks**: Universal blood magic applications beneficial to both landless and landed characters.
- **3 Route-Specific Tracks**: Tailored explicitly to the chosen specialization.

```
                            [ Blood Empowerment ]
                                      │
            ┌─────────────────────────┴─────────────────────────┐
    [ 5 Shared Core Tracks ]                            [ 5 Shared Core Tracks ]
    • Dynasty (Genetics & Fertility)                    • Dynasty (Genetics & Fertility)
    • Mastery (XP & Languages)                          • Mastery (XP & Languages)
    • Presence (Opinion, Stress & Sways)                • Presence (Opinion, Stress & Sways)
    • Prosperity (Gold Gain & Cost Reduction)           • Prosperity (Gold Gain & Cost Reduction)
    • Shadows (Plot Defense & Secrecy)                  • Shadows (Plot Defense & Secrecy)
            │                                                   │
    [ 3 Transcendence Tracks ]                          [ 3 Sovereignty Tracks ]
    • Wayfarer (Travel & Movement)                      • Dominion (Control & Dread)
    • Sustenance (Camp & Provisions)                    • Prosperity (Development & Infrastructure)
    • Vitality (Prowess & Bodily Mastery)               • Majesty (Vassals & Imperial Aura)
            │                                                   │
    lifestyle_blood_transcendence                       lifestyle_blood_sovereignty
       (Self / Adventurer / Wanderer)                      (Landed Overlord / Empire)
```

---

## 4. The 5 Shared Core Tracks (Both Traits)

These 5 tracks are identically available to both `lifestyle_blood_transcendence` and `lifestyle_blood_sovereignty`. Modifiers are listed **per rank** (10 ranks / up to 100 XP per track) and stack with the universal baseline.

| # | Track | Theme | Target Modifiers per Rank (10 Ranks Total) | Full Track Cap (100 XP) |
| :-: | :--- | :--- | :--- | :--- |
| **1** | **`dynasty`** | Genetics & Reproductive Vitality | • `positive_random_genetic_chance = 0.05`<br>• `positive_inactive_inheritance_chance = 0.05`<br>• `fertility = 0.04` | +50% Positive Congenital<br>+50% Inactive Trait Inheritance<br>+40% Fertility |
| **2** | **`mastery`** | Omniscience, Lifestyle Mastery & Tongues | • `monthly_lifestyle_xp_gain_mult = 0.04`<br>• `learn_language_scheme_phase_duration_add = -10`<br>• `personal_scheme_power_mult = 0.03`<br>• `max_learn_language_schemes_add = 1` *(ranks 30, 60, 90, 100)* | +40% Lifestyle XP Gain<br>-100 Days Language Scheme Phase<br>+30% Personal Scheme Power<br>+4 Max Language Schemes |
| **3** | **`presence`** | Personal Aura, Seduction & Stress Control | • `stress_loss_mult = 0.05`<br>• `general_opinion = 2.5`<br>• `sway_scheme_power_mult = 0.05` | +50% Stress Loss Rate<br>+25 General Opinion<br>+50% Sway Scheme Power |
| **4** | **`prosperity`** | Gold Generation & Expense Reduction<br>*(Adaptive across Landed & Landless)* | • `monthly_income_mult = 0.03`<br>• `men_at_arms_maintenance = -0.03`<br>• `domain_tax_mult = 0.02`<br>• `holding_build_gold_cost = -0.02`<br>• `domicile_building_cost_mult = -0.03` | +30% Monthly Income (All Sources)<br>-30% Men-at-Arms Maintenance<br>+20% Domain Taxes *(if Landed)*<br>-20% Holding Build Cost<br>-30% Camp Upgrade Cost *(if Landless)* |
| **5** | **`shadows`** | Plot Defense, Camouflage & Occult Secrecy | • `hostile_scheme_resistance_add = 3`<br>• `owned_scheme_secrecy_add = 5`<br>• `enemy_hostile_scheme_success_chance_add = -3` | +30 Hostile Scheme Resistance<br>+50 Owned Scheme Secrecy<br>-30% Enemy Plot Success Chance |

> **Adaptive Stewardship Design**:
> - `monthly_income_mult` and `men_at_arms_maintenance` apply to **all** character types (landed rulers, mercenary captains, traveling scholars).
> - `domain_tax_mult` seamlessly empowers landed rulers holding castles and cities.
> - `domicile_building_cost_mult` discounts camp upgrades for landless adventurers and family estates for administrative rulers.

---

## 5. Trait A: `lifestyle_blood_transcendence` (3 Specific Tracks)

> *"The blood mage turns their power inward, purifying their mortal biology into an enduring, terrifying vessel that thrives in the wilderness, single combat, and foreign lands."*

Tailored for **landless adventurers, traveling scholars, duelists, and rulers prioritizing personal invulnerability**.

| # | Track | Theme | Target Modifiers per Rank (10 Ranks Total) | Full Track Cap (100 XP) |
| :-: | :--- | :--- | :--- | :--- |
| **1** | **`wayfarer`** | Wilderness, Travel & Mobility | • `character_travel_speed_mult = 0.04`<br>• `character_travel_safety = 2.5`<br>• `travel_attrition_reduction_mult = 0.05` | +40% Travel Speed Mult<br>+25 Flat Travel Safety<br>-50% Danger Attrition |
| **2** | **`sustenance`** | Camp Logistics, Provisions & Independence | • `provisions_gain_mult = 0.05`<br>• `provisions_capacity_add = 40`<br>• `provisions_loss_mult = -0.03` | +50% Provisions Gain Rate<br>+400 Max Provisions Capacity<br>-30% Provision Loss / Spoilage |
| **3** | **`vitality`** | Bodily Alchemy, Prowess & Duels | • `prowess = 1`<br>• `wound_recovery_mult = 0.05`<br>• `prowess_per_prestige_level = 0.2`<br>• `no_prowess_loss_from_age = yes` *(at rank 10)* | +10 Prowess<br>+50% Wound Recovery<br>Fame scales Prowess<br>No Prowess Loss from Age |

---

## 6. Trait B: `lifestyle_blood_sovereignty` (3 Specific Tracks)

> *"The blood mage projects their will upon the world around them, saturating their realm, subjects, institutions, and armies in imperial occult authority."*

Tailored for **landed kings, emperors, administrative governors, feudal overlords, and realm builders**.

| # | Track | Theme | Target Modifiers per Rank (10 Ranks Total) | Full Track Cap (100 XP) |
| :-: | :--- | :--- | :--- | :--- |
| **1** | **`dominion`** | Territorial Iron Grip & Authority | • `monthly_county_control_growth_add = 0.08`<br>• `dread_baseline_add = 4`<br>• `monthly_tyranny = -0.015` | +0.80 Monthly Control Growth<br>+40 Dread Baseline<br>-0.15 Tyranny Decay Rate |
| **2** | **`prosperity`** | Realm Development & Infrastructure | • `development_growth = 0.05`<br>• `character_capital_county_monthly_development_growth_add = 0.06`<br>• `holding_build_speed = 0.05`<br>• `county_opinion_add = 2` | +50% Realm Development Growth<br>+0.60 Capital Dev Growth<br>+50% Holding Build Speed<br>+20 Popular Opinion |
| **3** | **`majesty`** | Imperial Court & Vassal Hierarchy | • `vassal_opinion = 2.5`<br>• `short_reign_duration_mult = -0.05`<br>• `monthly_prestige_gain_mult = 0.05`<br>• `siege_phase_time = -0.03` | +25 Vassal Opinion<br>-50% Short Reign Duration<br>+50% Monthly Prestige<br>-30% Siege Phase Duration |

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

## 8. Shared Engine & Spell Integration

Both traits plug into the mod's existing ritual gates without duplicate logic or orphaned checks.

### Centralized XP Gate Script Value
Any ritual checking empowerment XP (e.g. `bm_enhance_education_decision` or `bm_blood_rune_minimum_xp`) evaluates total earned empowerment XP across all 8 tracks via a single script value:
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
When all 8 tracks of the chosen trait reach the 100 XP cap (800 XP total), casting the Major Blood Empowerment ritual grants:
- `temporary_buff_self` (+2 all stats, +4 prowess for 10 years).
- Roll chance for permanent attribute gains (+1 to a random attribute).

---

## 9. Historical Reference: The Original 7 Empowerment Tracks

For future balance comparisons and reference if elements need to be revived or cross-referenced, the original pre-overhaul `lifestyle_blood_empowerment` trait used a 7-track architecture. Each rank (10 XP) provided flat `life_expectancy = 1` and `monthly_piety = 0.1` plus fixed track perks across 10 ranks (100 XP total).

### Legacy Baseline (Per Rank, Pre-Overhaul)
- `life_expectancy = 1` (+10 years cap per track)
- `monthly_piety = 0.1` (+1.0 monthly piety cap per track)

### Legacy Tracks Summary

| Track Name | Legacy Theme | Target Modifiers Per Rank (10 XP) | Full Track Cap (100 XP) | Current Status / Successor |
| :--- | :--- | :--- | :--- | :--- |
| **`charisma`** | Diplomacy & Prestige | • `general_opinion = 2.5`<br>• `monthly_prestige_gain_mult = 0.05` | +25 General Opinion<br>+50% Monthly Prestige | Evolved into **`presence`** (+ stress loss & sway power). Prestige gain moved to Sovereignty candidate **`majesty`**. |
| **`fury`** | Military & County Control | • `knight_effectiveness_mult = 0.05`<br>• `monthly_county_control_growth_add = 0.05` | +50% Knight Effectiveness<br>+0.50 Monthly County Control | **Removed from core** to prevent overlap with `lifestyle_blood_knight`. Control growth moved to Sovereignty candidate **`dominion`**. |
| **`prosperity`** | Domain Tax & Capital Dev | • `domain_tax_mult = 0.025`<br>• `character_capital_county_monthly_development_growth_add = 0.05` | +25% Domain Taxes<br>+0.50 Capital Development Growth | Generalized in core **`prosperity`** (added MaA upkeep reduction, holding discount, adventurer camp discount). |
| **`shadows`** | Dread, Tyranny & Secrecy | • `dread_baseline_add = 3`<br>• `monthly_tyranny = -0.01`<br>• `owned_scheme_secrecy_add = 5` | +30 Dread Baseline<br>-0.10 Tyranny Decay<br>+50 Owned Scheme Secrecy | Refocused core **`shadows`** into defensive subterfuge (hostile scheme resistance, enemy success reduction). Dread & tyranny moved to Sovereignty candidate **`dominion`**. |
| **`insight`** | Realm Dev & Piety Multiplier | • `development_growth = 0.05`<br>• `monthly_piety_gain_mult = 0.05` | +50% Realm Development Growth<br>+50% Monthly Piety Gain | Piety gain folded into baseline piety loops. Dev growth moved to Sovereignty candidate **`prosperity`**. |
| **`legacy`** | Congenital Genetics | • `positive_random_genetic_chance = 0.05`<br>• `positive_inactive_inheritance_chance = 0.05` | +50% Positive Congenital Chance<br>+50% Positive Inactive Inheritance | Retained & expanded as core **`dynasty`** (+ fertility). |
| **`expertise`** | Lifestyle XP & Cultural Speed | • `monthly_lifestyle_xp_gain_mult = 0.025`<br>• `cultural_head_fascination_mult = 0.05` | +25% Lifestyle XP Gain<br>+50% Cultural Fascination Progress | Excised cultural fascination (useless when not cultural head). Expanded as core **`mastery`** (+ Learn Language schemes & capacity). |
