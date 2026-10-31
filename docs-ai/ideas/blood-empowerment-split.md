# Ideas: Blood Power Two-Trait Split (Transcendence vs. Sovereignty)

> **Status:** Speculative / Future Roadmap. The core 6 disciplines (`presence`, `warband`, `prosperity`, `shadows`, `mastery`, `dynasty`) have been consolidated and implemented directly onto `lifestyle_blood_power` in the active codebase. This document preserves the architectural proposal and route-specific track specifications for a future expansion into specialized branch traits (`lifestyle_blood_transcendence` vs. `lifestyle_blood_sovereignty`).

Living proposal for overhauling Blood Power by splitting it into two mutually exclusive sister traits:
1. **`lifestyle_blood_transcendence`** (The Inner Vessel — Self / Adventurer / Personal Mastery)
2. **`lifestyle_blood_sovereignty`** (The Outer Dominion — Landed Overlord / Realm Projection)

Characters may only possess **one** of these two traits (`opposites = { ... }`), chosen upon first casting the major empowerment ritual. Both traits share the baseline progression and contribute seamlessly toward high-tier spell unlocks (Education Enhancement, Blood Runes).

---

## 1. Problem Statement & Motivation

- **High Cost vs. Low Reward**: Currently, Blood Power consumes 150 Piety + a **Major Lifeforce** per rank (10 XP).
- **Strictly Landed Bias**:
  - County control growth and capital development growth are useless for landless wanderers, mercenary bands, and traveling scholars.
  - Cultural fascination mult is 100% useless unless the character is the Cultural Head.
- **Missing Travel & Adventurer Integration**: Vanilla 1.20 (Roads to Power) introduced camp logistics, travel hazards, and adventurer contracts.
- **The Solution: 6 Shared Core Disciplines + 3 Route-Specific Tracks**:
  - Keep the universal disciplines (Presence, Warband, Prosperity, Shadows, Mastery, Dynasty) shared.
  - Specialize 3 route-specific tracks around distinct playstyles: Bodily Mastery & Wilderness (Transcendence) vs. Realm & Dynastic Rule (Sovereignty).

---

## 2. Structural Overview

Each specialized trait would branch from the core disciplines with **3 Route-Specific Tracks** tailored explicitly to the chosen specialization:

```
                            [ Blood Power ]
                                   │
         ┌─────────────────────────┴─────────────────────────┐
         │                                                   │
 [ 3 Transcendence Tracks ]                          [ 3 Sovereignty Tracks ]
 • Wayfarer (Travel & Movement)                      • Dominion (Control & Dread)
 • Sustenance (Camp & Provisions)                    • Development (Infrastructure)
 • Vitality (Prowess & Bodily Mastery)               • Majesty (Vassals & Imperial Aura)
         │                                                   │
 lifestyle_blood_transcendence                       lifestyle_blood_sovereignty
    (Self / Adventurer / Wanderer)                      (Landed Overlord / Empire)
```

---

## 3. Trait A: `lifestyle_blood_transcendence` (3 Specific Tracks)

> *"The blood mage turns their power inward, purifying their mortal biology into an enduring, terrifying vessel that thrives in the wilderness, single combat, and foreign lands."*

Tailored for **landless adventurers, traveling scholars, duelists, and rulers prioritizing personal invulnerability**.

| # | Track | Theme | Target Modifiers per Rank (10 Ranks Total) | Full Track Cap (100 XP) |
| :-: | :--- | :--- | :--- | :--- |
| **1** | **`wayfarer`** | Wilderness, Travel & Mobility | • `character_travel_speed_mult = 0.04`<br>• `character_travel_safety = 2.5`<br>• `travel_attrition_reduction_mult = 0.05` | +40% Travel Speed Mult<br>+25 Flat Travel Safety<br>-50% Danger Attrition |
| **2** | **`sustenance`** | Camp Logistics, Provisions & Independence | • `provisions_gain_mult = 0.05`<br>• `provisions_capacity_add = 40`<br>• `provisions_loss_mult = -0.03` | +50% Provisions Gain Rate<br>+400 Max Provisions Capacity<br>-30% Provision Loss / Spoilage |
| **3** | **`vitality`** | Bodily Alchemy, Prowess & Duels | • `prowess = 1`<br>• `wound_recovery_mult = 0.05`<br>• `prowess_per_prestige_level = 0.2` | +10 Prowess<br>+50% Wound Recovery<br>Fame scales Prowess |

---

## 4. Trait B: `lifestyle_blood_sovereignty` (3 Specific Tracks)

> *"The blood mage projects their will upon the world around them, saturating their realm, subjects, institutions, and armies in imperial occult authority."*

Tailored for **landed kings, emperors, administrative governors, feudal overlords, and realm builders**.

| # | Track | Theme | Target Modifiers per Rank (10 Ranks Total) | Full Track Cap (100 XP) |
| :-: | :--- | :--- | :--- | :--- |
| **1** | **`dominion`** | Territorial Iron Grip & Authority | • `monthly_county_control_growth_add = 0.08`<br>• `dread_baseline_add = 4`<br>• `monthly_tyranny = -0.015` | +0.80 Monthly Control Growth<br>+40 Dread Baseline<br>-0.15 Tyranny Decay Rate |
| **2** | **`prosperity`** | Realm Development & Infrastructure | • `development_growth = 0.05`<br>• `character_capital_county_monthly_development_growth_add = 0.06`<br>• `holding_build_speed = 0.05`<br>• `county_opinion_add = 2` | +50% Realm Development Growth<br>+0.60 Capital Dev Growth<br>+50% Holding Build Speed<br>+20 Popular Opinion |
| **3** | **`majesty`** | Imperial Court & Vassal Hierarchy | • `vassal_opinion = 2.5`<br>• `short_reign_duration_mult = -0.05`<br>• `monthly_prestige_gain_mult = 0.05`<br>• `siege_phase_time = -0.03` | +25 Vassal Opinion<br>-50% Short Reign Duration<br>+50% Monthly Prestige<br>-30% Siege Phase Duration |

---

## 5. Ritual Architecture & Selection Flow

```
                      [ Cast Major Blood Magic: Channel Blood Power ]
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

## 6. Shared Engine & Spell Integration

Both traits plug into the mod's existing ritual gates without duplicate logic or orphaned checks.

### Centralized XP Gate Script Value
Any ritual checking empowerment XP (e.g. `bm_enhance_education_decision` or `bm_blood_rune_minimum_xp`) evaluates total earned empowerment XP across all tracks via a single script value:
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
When all tracks of the chosen trait reach the 100 XP cap, casting the Major Blood Power ritual grants:
- `temporary_buff_self` (+2 all stats, +4 prowess for 10 years).
- Roll chance for permanent attribute gains (+1 to a random attribute).
