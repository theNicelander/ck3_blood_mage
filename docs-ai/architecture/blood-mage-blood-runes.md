# Blood Runes and Blood Architecture

## Executive Summary

- **What:** Personal body rune modifiers granting passive yearly Lifeforce, plus Duchy Capital blood university buildings.
- **Rune Inscription:** Minor and Major runes inscribed via `bm_cast_blood_magic_major_decision` (event `bm_cast_blood_magic_major.001`), consuming `lifeforce_modifier_major` and `lifeforce_modifier_minor`. Superior Blood Rune inscribed via `bm_cast_blood_magic_superior_decision` (event `bm_cast_blood_magic_superior.001`), consuming `lifeforce_modifier_superior`. Gated on Devotion Ranks 2/3/4. 5-year cooldown (`bm_blood_rune_cooldown`). Option is completely hidden once maxed (`superior_blood_rune_modifier`).
- **University Buildings:** `bm_university_0` through `bm_university_3`. Duchy capital holdings. Built by rulers with `lifestyle_blood_mage`.

### Blood Runes Table

Runes are sequential. Higher tiers replace lower tiers:

| Rune Tier | Modifier | Req Devotion Rank | Piety Cost | Yearly Passive Lifeforce Roll |
| --- | --- | --- | --- | --- |
| **Minor** | `minor_blood_rune_modifier` | Rank 2 (Devoted) | 0 | 20% chance minor lifeforce |
| **Major** | `major_blood_rune_modifier` | Rank 3 (Paragon of Virtue) | 200 | 20% minor, 10% major, 5% both |
| **Superior** | `superior_blood_rune_modifier` | Rank 4 (Religious Icon) | 400 | 10% minor, 20% major, 10% both |

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
| Major magic decision | `common/decisions/cast_magic/bm_cast_blood_magic_major.txt` (`bm_cast_blood_magic_major_decision`) |
| Rune inscription options | `events/bm_cast_blood_magic_major_events.txt` (`bm_cast_blood_magic_major.001`) |
| Yearly rune pulse | `events/bm_yearly_events.txt` (`blood_mage_yearly_events.003`) |
| Rune modifiers | `common/modifiers/bm_blood_runes_modifiers.txt` |
| Rune piety cost values | `common/script_values/bm_blood_rune_cost.txt` (`bm_blood_rune_piety_cost`) |
| Duchy capital buildings | `common/buildings/bm_duchy_buildings.txt` |

## Key Mechanics & Gotchas

- **Sequential Only:** Runes do not stack. Major replaces Minor; Superior replaces Major.
- **Holder Requirement:** Blood Universities require holder to have `lifestyle_blood_mage`. If non-mage inherits or takes holding, building is disabled.
