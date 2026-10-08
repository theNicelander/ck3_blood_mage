# Blood Runes and Blood Architecture

## Executive Summary

- **What:** Personal body rune modifiers granting passive yearly Lifeforce, plus Duchy Capital blood university buildings.
- **Rune Decision:** `bm_inscribe_blood_runes_decision` in Situation panel -> Event `bm_crimson_rune.001`. Consumes `lifeforce_modifier_major`. Costs piety, checks total `lifestyle_crimson_empowerment` XP.
- **University Buildings:** `bm_university_0` through `bm_university_3`. Duchy capital holdings. Built by rulers with `lifestyle_blood_mage`.

### Crimson Runes Table

Runes are sequential. Higher tiers replace lower tiers:

| Rune Tier | Modifier | Req CE XP | Piety Cost | Yearly Passive Lifeforce Roll |
| --- | --- | --- | --- | --- |
| **Minor** | `minor_crimson_rune_modifier` | 25 | Base (0) | 20% chance minor lifeforce |
| **Major** | `major_crimson_rune_modifier` | 50 | Base + 200 | 20% minor, 10% major, 5% both |
| **Superior** | `superior_crimson_rune_modifier` | 100 | Base + 400 | 10% minor, 20% major, 10% both |

*Yearly rolls handled by hidden pulse `blood_mage_yearly_events.003`.*

### Blood Universities Table

Duchy capital buildings constructible only if holder has `lifestyle_blood_mage`:

| Tier | Building ID | Cost | Time | Penalties | Province & Realm Bonuses |
| --- | --- | --- | --- | --- | --- |
| **0** | `bm_university_0` | 250g, 250p | 3 yrs | -0.1 income, -0.1 piety | +0.1 dev growth, +5% cultural fascination |
| **1** | `bm_university_1` | 500g, 500p | 5 yrs | -0.2 income, -0.2 piety | +0.2 dev growth, +10% cultural fascination |
| **2** | `bm_university_2` | 750g, 750p | 7 yrs | -0.3 income, -0.3 piety | +0.3 dev growth, +15% cultural fascination |
| **3** | `bm_university_3` | 1000g, 1000p | 10 yrs | -0.4 income, -0.4 piety | +0.4 dev growth, +20% cultural fascination |

## Where the details live

| Piece | File |
| --- | --- |
| Inscription decision | `common/decisions/bm_inscribe_blood_runes_decision.txt` (`bm_inscribe_blood_runes_decision`) |
| Rune inscription events | `events/bm_blood_rune_events.txt` (`bm_crimson_rune.001`) |
| Yearly rune pulse | `events/bm_yearly_events.txt` (`blood_mage_yearly_events.003`) |
| Rune modifiers | `common/modifiers/bm_blood_runes_modifiers.txt` |
| Rune piety cost values | `common/script_values/bm_blood_rune_cost.txt` (`bm_blood_rune_piety_cost`) |
| Rune XP requirement values | `common/script_values/bm_xp_requirement_values.txt` (`bm_blood_rune_minimum_xp`) |
| Duchy capital buildings | `common/buildings/bm_dutchy_buildings.txt` |

## Key Mechanics & Gotchas

- **Sequential Only:** Runes do not stack. Major replaces Minor; Superior replaces Major.
- **Holder Requirement:** Blood Universities require holder to have `lifestyle_blood_mage`. If non-mage inherits or takes holding, building is disabled.
