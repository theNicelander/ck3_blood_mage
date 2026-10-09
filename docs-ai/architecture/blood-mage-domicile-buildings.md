# Blood Mage Domicile Buildings

Technical architecture for blood magic domicile structures in Adventurer Camps (`camp`), Noble Family Estates (`estate`), and related domiciles.

---

## 1. Executive Summary

- **What it is:** A single 5-tier external domicile building line named **Blood Shrine** (`bm_domicile_blood_shrine_01` through `05`) that empowers blood mage adventurers and noble families, radiating piety, health, lifespan, and positive genetic inheritance bonuses to both the owner and everyone in their camp or court.
- **How to get it:** Visible and constructible by characters with `lifestyle_blood_mage` or whose faith belongs to `bm_blodtru_religion`. Built in any external domicile slot.
- **How to level / advance:** Linear upgrade path (`01` -> `02` -> `03` -> `04` -> `05`) with gold costs and construction durations.
- **Data Table:**

| Tier | Building Key | Gold Cost | Build Time | Owner Cumulative Stats (`character_modifier`) | Court / Camp Follower Aura (`bm_blood_shrine_aura`) | Domicile Parameter |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **I** | `bm_domicile_blood_shrine_01` | 75 | 180 d | +0.2 Piety, +0.2 Health, +2 Lifespan, +5% Genetics | +0.2 Piety, +0.2 Health, +2 Lifespan, +5% Genetics | `bm_blood_shrine_tier_1` |
| **II** | `bm_domicile_blood_shrine_02` | 150 | 240 d | +0.4 Piety, +0.4 Health, +4 Lifespan, +10% Genetics | +0.4 Piety, +0.4 Health, +4 Lifespan, +10% Genetics | `bm_blood_shrine_tier_2` |
| **III** | `bm_domicile_blood_shrine_03` | 300 | 360 d | +0.6 Piety, +0.6 Health, +6 Lifespan, +15% Genetics | +0.6 Piety, +0.6 Health, +6 Lifespan, +15% Genetics | `bm_blood_shrine_tier_3` |
| **IV** | `bm_domicile_blood_shrine_04` | 500 | 480 d | +0.8 Piety, +0.8 Health, +8 Lifespan, +20% Genetics | +0.8 Piety, +0.8 Health, +8 Lifespan, +20% Genetics | `bm_blood_shrine_tier_4` |
| **V** | `bm_domicile_blood_shrine_05` | 800 | 600 d | +1.0 Piety, +1.0 Health, +10 Lifespan, +25% Genetics | +1.0 Piety, +1.0 Health, +10 Lifespan, +25% Genetics | `bm_blood_shrine_tier_5` |

*Genetics bonuses: `positive_random_genetic_chance` and `positive_inactive_inheritance_chance` (+0.05 per tier).*

---

## 2. Key Mechanics

- **Owner Modifiers & Inheritance:** Domicile building tracks automatically inherit all `character_modifier` blocks from prior tiers. Each tier adds an incremental `+0.2` piety, `+0.2` health, `+2` lifespan, and `+0.05` genetic inheritance chances, accumulating to the exact tier maximum on the domicile owner.
- **Camp & Court-Wide Aura:**
  - Because CK3 domicile buildings natively support only owner and province modifiers, courtiers and camp followers receive the bonuses via companion character modifiers (`bm_blood_shrine_aura_tier_1..5`).
  - Upon building completion (`on_complete`), `bm_update_blood_shrine_aura_effect` sweeps `every_courtier` (which covers camp followers for unlanded adventurers, and courtiers for landed/estate rulers).
  - When new courtiers or followers join, `on_join_court` checks `liege_or_court_owner` and immediately applies the active tier modifier.
  - Yearly maintenance pulse (`random_yearly_everyone_pulse`) refreshes active courtiers and prunes stale modifiers if the court owner loses or dismantles the font.

---

## 3. Where the Details Live

| Concept | File |
| :--- | :--- |
| Building Definitions (5 tiers, costs, inheritance) | `common/domiciles/buildings/bm_domicile_buildings.txt` |
| Courtier / Follower Companion Modifiers | `common/modifiers/bm_domicile_modifiers.txt` |
| Scripted Effects (`update`, `apply`, `clear`) | `common/scripted_effects/bm_domicile_effects.txt` |
| Scripted Trigger (`bm_has_blood_shrine_trigger`) | `common/scripted_triggers/bm_domicile_triggers.txt` |
| On-Action Hooks (`on_join_court`, `random_yearly_everyone_pulse`) | `common/on_action/bm_domicile_on_actions.txt` |
| English Localization (buildings, params, modifiers) | `localization/english/bm_domicile_buildings_l_english.yml` |

---

## 4. Gotchas

- **Building Modifier Stacking:** CK3 domicile building tracks inherit previous tier modifiers. Never declare the full cumulative modifier in higher tiers (e.g., writing `health = 0.4` in tier 2 would stack with tier 1's `0.2` to yield `0.6`).
- **Parameter Non-Inheritance:** Building parameters do NOT inherit from previous buildings. Each tier explicitly sets its own active tier parameter (`bm_blood_shrine_tier_X`).
- **Follower vs Courtier Scope:** For landless adventurers, all camp followers reside in the `every_courtier` scope. Targeting `every_courtier` ensures identical functioning across camp adventurers and estate rulers.

---

## 5. Not Verified

- Exact UI texture rendering in atypical non-western culture camp backgrounds when DLC Roads to Power is disabled or absent (building falls back to valid vanilla DDS assets).
