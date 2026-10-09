# Ideas: Blood Mage Domicile Building (The Sanguine Font)

Proposal for a single, 5-level upgradeable domicile building line tailored for **Adventurer Camps** (`camp`) and **Noble Estates** (`estate`) belonging to Blood Mages or followers of the Blóðtrú religion.

Introduced in CK3 1.20 (Roads to Power), the domicile system allows unlanded adventurers and administrative noble families to upgrade their permanent base of operations.

---

## 1. Design Overview

- **Single Building Line**: Replaces fragmented multi-slot modules with a unified 5-tier upgrade chain (`bm_domicile_sanguine_font_01` through `05`).
- **Target Domiciles**: Adventurer Camps (`camp`) and Noble Estates (`estate`).
- **Core Benefits**: Grants scaling **Piety**, **Lifespan** (`life_expectancy`), and **Health** (`health`).
- **Beneficiaries**:
  - Domicile Owner (direct building `character_modifier`).
  - **Everyone in the Camp / Court** (followers for adventurers; courtiers for landed/estate rulers) via a companion aura modifier refreshed dynamically.

---

## 2. Gating & Requirements

### Domicile Visibility & Construction Trigger

The building line appears and can be constructed only by Blood Mages or Blóðtrú adherents:

```pdx
can_construct_potential = {
    OR = {
        has_trait = lifestyle_blood_mage
        faith = { religion = religion:bm_blodtru_religion }
    }
}

can_construct = {
    # Standard gold and tier prerequisites
}
```

---

## 3. The 5-Tier Building Line: `bm_domicile_sanguine_font`

- **Slot Type**: `external`
- **Allowed Domicile Types**: `{ camp estate }`
- **Previous Building**: Linear progression (`01` -> `02` -> `03` -> `04` -> `05`).

### Tier Summary Table

| Level | Key | Cost | Build Time | Owner Modifiers (`character_modifier`) | Camp / Court Aura Modifiers (`bm_sanguine_font_aura`) | Domicile Parameter |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **I** | `bm_domicile_sanguine_font_01` | 75 Gold | 180 Days | `domicile_monthly_piety_add = 0.2`<br>`health = 0.1`<br>`life_expectancy = 2` | `monthly_piety = 0.1`<br>`health = 0.1`<br>`life_expectancy = 2` | `bm_sanguine_font_tier_1 = yes` |
| **II** | `bm_domicile_sanguine_font_02` | 150 Gold | 240 Days | `domicile_monthly_piety_add = 0.4`<br>`health = 0.25`<br>`life_expectancy = 4` | `monthly_piety = 0.2`<br>`health = 0.2`<br>`life_expectancy = 4` | `bm_sanguine_font_tier_2 = yes` |
| **III** | `bm_domicile_sanguine_font_03` | 300 Gold | 360 Days | `domicile_monthly_piety_add = 0.6`<br>`health = 0.4`<br>`life_expectancy = 6` | `monthly_piety = 0.3`<br>`health = 0.3`<br>`life_expectancy = 6` | `bm_sanguine_font_tier_3 = yes` |
| **IV** | `bm_domicile_sanguine_font_04` | 500 Gold | 480 Days | `domicile_monthly_piety_add = 0.8`<br>`health = 0.6`<br>`life_expectancy = 8` | `monthly_piety = 0.4`<br>`health = 0.4`<br>`life_expectancy = 8` | `bm_sanguine_font_tier_4 = yes` |
| **V** | `bm_domicile_sanguine_font_05` | 800 Gold | 600 Days | `domicile_monthly_piety_add = 1.0`<br>`health = 0.8`<br>`life_expectancy = 10` | `monthly_piety = 0.5`<br>`health = 0.5`<br>`life_expectancy = 10` | `bm_sanguine_font_tier_5 = yes` |

*Note: In CK3 domicile buildings, `character_modifier` applies directly to the domicile owner. For monthly piety from domiciles, vanilla uses `domicile_monthly_piety_add` on owners, whereas courtiers use standard `monthly_piety`.*

---

## 4. Camp & Court-Wide Propagation Architecture

### The Engine Constraint

Domicile buildings only support:
- `character_modifier = { ... }`: applies strictly to `scope:owner` (the domicile owner).
- `province_modifier = { ... }`: applies to the domicile's physical barony/province location.

Vanilla domicile buildings have no native `courtier_modifier` block. To extend health, lifespan, and piety to **everyone in the camp** (followers) and **everyone in the court** (for landed/estate rulers), a companion script architecture is required.

### Implementation Blueprint

#### 1. Domicile Parameters
Each building tier exposes a unique domicile parameter:
```pdx
# Example for Tier 3:
parameters = {
    bm_sanguine_font_tier_3 = yes
}
```

#### 2. Companion Character Modifiers
Define 5 character modifiers in `common/modifiers/bm_domicile_modifiers.txt`:
```pdx
bm_sanguine_font_aura_tier_1 = {
    icon = blood_positive
    monthly_piety = 0.1
    health = 0.1
    life_expectancy = 2
}

bm_sanguine_font_aura_tier_2 = {
    icon = blood_positive
    monthly_piety = 0.2
    health = 0.2
    life_expectancy = 4
}

bm_sanguine_font_aura_tier_3 = {
    icon = blood_positive
    monthly_piety = 0.3
    health = 0.3
    life_expectancy = 6
}

bm_sanguine_font_aura_tier_4 = {
    icon = blood_positive
    monthly_piety = 0.4
    health = 0.4
    life_expectancy = 8
}

bm_sanguine_font_aura_tier_5 = {
    icon = blood_positive
    monthly_piety = 0.5
    health = 0.5
    life_expectancy = 10
}
```

#### 3. Scripted Effect: `bm_update_sanguine_font_aura_effect`
A scoped effect on a ruler/camp leader that sweeps `every_courtier` (in CK3 adventurer camps, all camp followers are in `every_courtier`):

```pdx
bm_update_sanguine_font_aura_effect = {
    # Determine active tier from domicile parameters
    save_scope_as = aura_source
    every_courtier = {
        # Clear obsolete aura tiers
        remove_character_modifier = bm_sanguine_font_aura_tier_1
        remove_character_modifier = bm_sanguine_font_aura_tier_2
        remove_character_modifier = bm_sanguine_font_aura_tier_3
        remove_character_modifier = bm_sanguine_font_aura_tier_4
        remove_character_modifier = bm_sanguine_font_aura_tier_5

        if = {
            limit = {
                scope:aura_source.domicile ?= { has_domicile_parameter = bm_sanguine_font_tier_5 }
            }
            add_character_modifier = {
                modifier = bm_sanguine_font_aura_tier_5
                years = 2
            }
        }
        else_if = {
            limit = {
                scope:aura_source.domicile ?= { has_domicile_parameter = bm_sanguine_font_tier_4 }
            }
            add_character_modifier = {
                modifier = bm_sanguine_font_aura_tier_4
                years = 2
            }
        }
        else_if = {
            limit = {
                scope:aura_source.domicile ?= { has_domicile_parameter = bm_sanguine_font_tier_3 }
            }
            add_character_modifier = {
                modifier = bm_sanguine_font_aura_tier_3
                years = 2
            }
        }
        else_if = {
            limit = {
                scope:aura_source.domicile ?= { has_domicile_parameter = bm_sanguine_font_tier_2 }
            }
            add_character_modifier = {
                modifier = bm_sanguine_font_aura_tier_2
                years = 2
            }
        }
        else_if = {
            limit = {
                scope:aura_source.domicile ?= { has_domicile_parameter = bm_sanguine_font_tier_1 }
            }
            add_character_modifier = {
                modifier = bm_sanguine_font_aura_tier_1
                years = 2
            }
        }
    }
}
```

#### 4. Event & Pulse Hooks
- **On Construction Complete**: In the building definition's `on_complete = { ... }`, call `scope:owner = { bm_update_sanguine_font_aura_effect = yes }`.
- **On Joining Court / Camp**: Hook `on_join_court` to check if `scope:new_employer.domicile` has `bm_sanguine_font_tier_*` and grant the modifier.
- **Maintenance Pulse**: The 2-year modifier expiration combined with `random_yearly_everyone_pulse` or a yearly court maintenance check ensures dead/departed courtiers shed the modifier cleanly without bloat.

---

## 5. File Layout for Eventual Implementation

- `common/domiciles/buildings/bm_domicile_buildings.txt` (the 5 building tiers, upgrade chains, costs, triggers)
- `common/modifiers/bm_domicile_modifiers.txt` (the 5 aura character modifiers)
- `common/scripted_effects/bm_domicile_effects.txt` (`bm_update_sanguine_font_aura_effect`)
- `common/on_action/bm_domicile_on_actions.txt` (`on_join_court` hook and yearly maintenance pulse)
- `localization/english/bm_domicile_buildings_l_english.yml` (building names, descriptions, and aura loc)
