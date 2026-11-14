# Character Modifiers & Dynamic Scaling

Living technical specification for character-scoped dynamic modifiers in CK3 1.20, their scaling targets, and engine scope boundaries (Character vs Province/Holding/Domicile).

## Executive Summary

CK3 calculates character sheets and holding economies at different internal engine scopes. Modifiers scaling dynamically per resource level (Devotion, Fame, Stress, Knights, Attributes) only function if scripted within their supported scope. Modifiers intended for holdings or provinces fail silently when applied to characters or traits.

---

## 1. Per Piety Level Modifiers (`_per_piety_level`)

Modifiers that scale based on the character's current Level of Devotion (`piety_level`: `0` Sinner, `1` Dutiful, `2` Faithful, `3` Devoted Servant, `4` Paragon of Virtue, `5` Religious Icon, up to `8` for Mandala governments).

| Modifier | Valid Scope | Valid on Traits? | Engine Benefit |
| :--- | :---: | :---: | :--- |
| `diplomacy_per_piety_level` | Character | **Yes** | Adds Diplomacy attribute per Level of Devotion |
| `martial_per_piety_level` | Character | **Yes** | Adds Martial attribute per Level of Devotion |
| `stewardship_per_piety_level` | Character | **Yes** | Adds Stewardship attribute per Level of Devotion |
| `intrigue_per_piety_level` | Character | **Yes** | Adds Intrigue attribute per Level of Devotion |
| `learning_per_piety_level` | Character | **Yes** | Adds Learning attribute per Level of Devotion |
| `prowess_per_piety_level` | Character | **Yes** | Adds Prowess attribute per Level of Devotion |
| `stress_loss_per_piety_level` | Character | **Yes** | Increases stress loss multiplier per Level of Devotion |
| `character_max_piety_level_add` | Character | **Yes** | Raises maximum Level of Devotion cap beyond baseline 5 |
| `piety_level_impact_mult` | Character | **Yes** | Multiplies the opinion and grandeur benefits of Level of Devotion |
| `monthly_income_per_piety_level` | Holding / Domicile | **No** (Fails silently) | Scales holding base gold income by ruler's devotion level |
| `tax_per_piety_level` | Holding / County | **No** (Fails silently) | Scales settlement base holding tax by ruler's devotion level |
| `stationed_maa_damage_mult_per_piety_level` | Holding | **No** (Fails silently) | Increases damage % of MaA regiments stationed in that holding |
| `stationed_maa_toughness_mult_per_piety_level` | Holding | **No** (Fails silently) | Increases toughness % of MaA regiments stationed in that holding |

---

## 2. Per Prestige Level Modifiers (`_per_prestige_level`)

Modifiers that scale based on the character's Level of Fame (`prestige_level`: `0` Disgraced, `1` Established, `2` Distinguished, `3` Illustrious, `4` Exalted Among Men, `5` Legendary Figure). Unlike Piety, there are **no holding-only variants** for prestige.

| Modifier | Valid Scope | Valid on Traits? | Engine Benefit |
| :--- | :---: | :---: | :--- |
| `diplomacy_per_prestige_level` | Character | **Yes** | Adds Diplomacy attribute per Level of Fame |
| `martial_per_prestige_level` | Character | **Yes** | Adds Martial attribute per Level of Fame |
| `stewardship_per_prestige_level` | Character | **Yes** | Adds Stewardship attribute per Level of Fame |
| `intrigue_per_prestige_level` | Character | **Yes** | Adds Intrigue attribute per Level of Fame |
| `learning_per_prestige_level` | Character | **Yes** | Adds Learning attribute per Level of Fame |
| `prowess_per_prestige_level` | Character | **Yes** | Adds Prowess attribute per Level of Fame |
| `stress_loss_per_prestige_level` | Character | **Yes** | Increases stress loss multiplier per Level of Fame |
| `prestige_level_impact_mult` | Character | **Yes** | Multiplies the opinion and realm benefits of Level of Fame |

---

## 3. Knight Scaling Modifiers (`_per_knight`)

Modifiers that scale dynamically based on the number of active Knights/Champions sworn to the ruler.

| Modifier | Valid Scope | Valid on Traits? | Engine Benefit |
| :--- | :---: | :---: | :--- |
| `monthly_piety_gain_per_knight_add` | Character | **Yes** | Flat monthly piety gained for each sworn knight |
| `monthly_piety_gain_per_knight_mult` | Character | **Yes** | % monthly piety gain multiplier for each sworn knight |
| `monthly_prestige_gain_per_knight_add` | Character | **Yes** | Flat monthly prestige gained for each sworn knight |
| `monthly_prestige_gain_per_knight_mult` | Character | **Yes** | % monthly prestige gain multiplier for each sworn knight |

---

## 4. Knight Effectiveness Per Stat Modifiers (`knight_effectiveness_per_<stat>`)

Modifiers that increase the combat effectiveness percentage of all sworn knights based on the ruler's personal attributes or status.

| Modifier | Valid Scope | Valid on Traits? | Engine Benefit |
| :--- | :---: | :---: | :--- |
| `knight_effectiveness_per_prowess` | Character | **Yes** | Knight effectiveness % per point of ruler's Prowess |
| `knight_effectiveness_per_martial` | Character | **Yes** | Knight effectiveness % per point of ruler's Martial |
| `knight_effectiveness_per_diplomacy` | Character | **Yes** | Knight effectiveness % per point of ruler's Diplomacy |
| `knight_effectiveness_per_stewardship` | Character | **Yes** | Knight effectiveness % per point of ruler's Stewardship |
| `knight_effectiveness_per_intrigue` | Character | **Yes** | Knight effectiveness % per point of ruler's Intrigue |
| `knight_effectiveness_per_learning` | Character | **Yes** | Knight effectiveness % per point of ruler's Learning |
| `knight_effectiveness_per_dread` | Character | **Yes** | Knight effectiveness % per point of ruler's Dread |
| `knight_effectiveness_per_tyranny` | Character | **Yes** | Knight effectiveness % per point of ruler's Tyranny |

---

## 5. Other Notable Character Dynamic Scaling Modifiers

Additional vanilla character-scoped modifiers that scale dynamically with character resources or status:

| Modifier | Target Resource | Engine Benefit |
| :--- | :--- | :--- |
| `monthly_income_per_stress_level_mult` | Stress Level (0–3) | % monthly gold multiplier per stress level |
| `stress_loss_per_dread` | Dread (0–100) | Increases stress loss rate based on current dread |
| `monthly_piety_gain_per_dread_add` / `mult` | Dread (0–100) | Flat or % piety gain based on current dread |
| `monthly_prestige_gain_per_dread_add` / `mult` | Dread (0–100) | Flat or % prestige gain based on current dread |
| `monthly_piety_gain_per_legitimacy_level_add` / `mult` | Legitimacy Level (0–5) | Flat or % piety gain based on ruler legitimacy |
| `monthly_prestige_gain_per_legitimacy_level_add` / `mult` | Legitimacy Level (0–5) | Flat or % prestige gain based on ruler legitimacy |
| `monthly_piety_gain_per_court_position_add` / `mult` | Employed Court Positions | Flat or % piety gain per active courtier position |
| `monthly_prestige_gain_per_court_position_add` / `mult` | Employed Court Positions | Flat or % prestige gain per active courtier position |
| `monthly_piety_gain_per_happy_powerful_vassal_add` / `mult` | Satisfied Powerful Vassals | Flat or % piety gain per powerful vassal with positive opinion |
| `monthly_prestige_gain_per_happy_powerful_vassal_add` / `mult` | Satisfied Powerful Vassals | Flat or % prestige gain per powerful vassal with positive opinion |

---

## 6. Scope Pitfalls & Character Safe Replacements

When designing traits or character modifiers, holding/province modifiers fail silently without script warnings. Use the corresponding character-safe alternatives:

| Invalid on Characters / Traits | Why It Fails | Character-Safe Alternative |
| :--- | :--- | :--- |
| `monthly_income_per_piety_level` | Holding economy calculation; requires barony settlement scope | `monthly_income = X` (flat gold allowance)<br>`domain_limit = X` (extra demesne holdings)<br>`monthly_income_mult = X` (% income boost) |
| `tax_per_piety_level` | Holding base tax property; requires settlement scope | `domain_tax_mult = X` (% domain holding taxes)<br>`vassal_tax_mult = X` (% vassal tax contributions) |
| `stationed_maa_damage_mult_per_piety_level` | Men-at-Arms stationing slot; requires barony holding scope | `army_damage_mult = X` (all army regiments)<br>`men_at_arms_damage = X` |
| `stationed_maa_toughness_mult_per_piety_level` | Men-at-Arms stationing slot; requires barony holding scope | `army_toughness_mult = X`<br>`men_at_arms_toughness = X` |

---

## Where the Details Live

| Concept | File Path |
| :--- | :--- |
| Attribute & stress scaling definitions | `/Users/clarabotet/Petur/ck3-full/common/modifier_definition_formats/00_definitions.txt` |
| Stationed Men-at-Arms unit definitions | `/Users/clarabotet/Petur/ck3-full/common/modifier_definition_formats/00_unit_definitions.txt` |
| Allowlist validation | `scripts/modifiers_allowlist.json` |
| Trait milestone usage (`lifestyle_blood_mage`) | `common/traits/bm_blood_mage_trait.txt` |
| Dynasty channel modifiers | `common/modifiers/bm_channel_dynasty_modifiers.txt` |

---

## Gotchas

- **Silent Zero Evaluation:** Applying `monthly_income_per_piety_level` or `tax_per_piety_level` to a character trait does not crash or log an error in `error.log`. The engine simply resolves holding base income to zero, awarding no gold.
- **Prestige vs Piety Asymmetry:** The engine implements `tax_per_piety_level` and `monthly_income_per_piety_level` because temples and religious holdings tie into the clergy tax system. Prestige has no holding-level equivalents.
- **Allowlist Gate:** Every modifier used in mod traits, modifiers, and buildings must exist in `scripts/modifiers_allowlist.json`. If adding an allowed vanilla modifier, verify with `python3 scripts/check_modifiers.py --add <mod>`.

---

## Not Verified

- Whether AI rulers factor `_per_piety_level` attribute scaling into marriage evaluation and council appointment weights dynamically or only evaluate static baseline skill levels.
