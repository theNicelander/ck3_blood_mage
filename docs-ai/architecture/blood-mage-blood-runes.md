# Blood Runes, Galdrastafir and Blood Architecture

Living technical specification for body runes, Galdrastafir staves, and Duchy Blood Temples.

## Overview

Decoupled architecture separating **Rune Depth** (`minor/major/superior_blood_rune_modifier`) from **Galdrastafir Stave Identity** (`bm_stave_<key>`).
- **Rune Depth:** Sequential body runes (Minor -> Major -> Superior) governing the passive yearly Lifeforce pulse (`blood_mage_yearly_events.003`) and unlocking the capstone stave.
- **Capstone Staves:** Granted at **Superior** depth via `bm_carve_galdrastafir_decision` (500 Piety, 1 Major LF, 5-yr CD). Grants static attributes and an active occult capstone mechanic.
- **Self-Inscription (`ancient` XP):** Inscribed sequentially via Cast Blood Magic widgets (`minor/major/superior`). Requires Devotion Rank 2 / 3 / 4, 5-yr CD (`bm_blood_rune_cooldown`), awards `+4 / +5 / +10` `ancient` XP. Both Mages and Knights can self-inscribe up to Superior.
- **Inscribe on Others (`benediction` XP):** Interaction `bm_inscribe_rune_other_interaction` upgrades target depth in-place. 5-yr CD (`bm_blood_rune_other_cooldown`), awards `+4 / +5 / +10` `benediction` XP. Superior on others is Mage exclusive.
- **Duchy Blood Temples:** 7-tier Duchy Capital building line (`common/buildings/bm_duchy_buildings.txt`, `type = duchy_capital`), constructible in duchy capital slots by Blood Mages, Blood Knights, or Blóðtrú faithful. Tiers I–IV open to all governments (Tier IV tribal capstone); Tiers V–VII require non-tribal feudalized holdings.

## Tier Progression, Costs & XP Table

| Rune Tier | Base Tracker | Self-Cast Gates (`minor/major/superior_decision`) | Cast-on-Other Gates (`bm_inscribe_rune_other_interaction`) | Cost (Self & Other) | Self-Cast XP | Cast on Other XP | Yearly Lifeforce Pulse (`blood_mage_yearly_events.003`) | Capstone Stave Access (`bm_carve_galdrastafir_decision`) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Minor** | `minor_blood_rune_modifier` | Mage or Knight, Rank 2 (`piety_level >= 2`), 5-yr CD (`bm_blood_rune_cooldown`) | Mage or Knight, Rank 2 (`piety_level >= 2`), `>= 25` total XP, 5-yr CD (`bm_blood_rune_other_cooldown`) | 0 Piety + 1 Minor Lifeforce | `+4` `ancient` | `+4` `benediction` | 20% Minor | Locked |
| **Major** | `major_blood_rune_modifier` | Mage or Knight, Rank 3 (`piety_level >= 3`), Minor Rune, 5-yr CD (`bm_blood_rune_cooldown`) | Mage or Knight, Rank 3 (`piety_level >= 3`), `>= 50` total XP, Minor Rune, 5-yr CD (`bm_blood_rune_other_cooldown`) | 200 Piety + 1 Major Lifeforce | `+5` `ancient` | `+5` `benediction` | 20% Minor, 10% Major, 5% Both | Locked |
| **Superior** | `superior_blood_rune_modifier` | Mage or Knight, Rank 4 (`piety_level >= 4`), Major Rune, 5-yr CD (`bm_blood_rune_cooldown`) | **Mage only**, Rank 4 (`piety_level >= 4`), `>= 100` total XP, Major Rune, 5-yr CD (`bm_blood_rune_other_cooldown`) | 400 Piety + 1 Superior Lifeforce | `+10` `ancient` | `+10` `benediction` | 10% Minor, 20% Major, 10% Both | **Unlocked**: First pick free; 5-yr swap for 500 Piety + 1 Major Lifeforce in Major Grimoire |

*Yearly rolls handled by hidden pulse `blood_mage_yearly_events.003` (triggers on rune modifiers, no trait restriction).*

## Galdrastafir Catalog (Flat Modifiers & Superior Capstones)

| # | Stave (`bm_stave_<key>`) | Flat Modifiers | Superior Capstone Effect (Active on `bm_stave_<key>` with Superior depth) |
| --- | --- | --- | --- |
| 1 | **Vegvísir** (`vegvisir`)<br/>*(The Wayfinder)* | • `character_travel_speed_mult = 0.25`<br/>• `character_travel_safety = 20`<br/>• `movement_speed = 0.10` | **Storm-Walker**: Halves `seek_power_decision` (Blood Hunt) cooldown (`bm_seek_power_cooldown_days`: landed `365 -> 182.5` days; landless/wanderer `1095 -> 547.5` days) and eliminates escape/witness hazard rolls when pursuing travelers in `events/bm_seek_power_events.txt` (`seek_power.003`). |
| 2 | **Ægishjálmur** (`aegishjalmur`)<br/>*(Helm of Awe)* | • `prowess = 6`<br/>• `advantage = 4`<br/>• `knight_effectiveness_mult = 0.20` | **Terror of the Slain**: On battle start (`on_combat_start` -> `bm_on_combat_start_aegishjalmur_terror` in `common/on_action/bm_duel_on_actions.txt`), if any commander or knight holds Ægishjálmur at Superior depth, inflicts `bm_aegishjalmur_terror_modifier` (`prowess = -5`, `health = -0.5`, 1 year) on the opposing commander and all opposing knights. |
| 3 | **Feingur** (`feingur`)<br/>*(Awakened Seed)* | • `fertility = 0.20`<br/>• `years_of_fertility = 10`<br/>• `positive_random_genetic_chance = 0.20`<br/>• `health = 0.40`<br/>• `epidemic_resistance = 10` | **Awakened Seed**: Doubles XP gained on childbirth (`bm_on_birth_bloodline_xp` in `common/on_action/bm_blood_mage_prevalence_on_actions.txt`: `+2` base, `+4` if child inherits `lifestyle_blood_mage`; grants `bloodline` XP for Mages or `ancient` XP for Knights). Unlocks the `bless_feingur` option in `bm_bless_bloodline_interaction` (cost: 50 Piety + 1 Minor Lifeforce) applying permanent modifier `bm_feingur_blessed_blood_modifier` (`fertility = 0.25`, `positive_random_genetic_chance = 0.20`, `health = 0.50`, `life_expectancy = 5`) to any child or dynasty kin. |
| 4 | **Nábrókarstafur** (`nabrokarstafur`)<br/>*(Flayed Tithe)* | • `domain_tax_mult = 0.10`<br/>• `men_at_arms_maintenance = -0.10`<br/>• `general_opinion = -10` | **Flayed Tithe**: Visiting Points of Interest during travel (`on_travel_plan_movement` -> `bm_on_visited_point_of_interest` in `common/on_action/bm_travel_on_actions.txt`) awards **+20 Gold** once per POI province (`bm_nabrokarstafur_visited_poi`). Winning battles (`on_combat_end_winner` -> `bm_on_combat_end_winner` in `common/on_action/bm_combat_on_actions.txt`) as commander or knight plunders **10% of enemy fatal casualties** as Gold (`bm_nabrokarstafur_battle_gold_value`), clamped between **25** and **250 Gold**. |
| 5 | **Hulinhjálmur** (`hulinhjalmur`)<br/>*(Unseen Shroud)* | • `owned_hostile_scheme_success_chance_add = 20`<br/>• `enemy_hostile_scheme_success_chance_add = -20`<br/>• `monthly_lifestyle_xp_gain_mult = 0.20` | **Unseen Shroud**: Doubles guaranteed yearly discipline Attunement XP gain from **+1 XP to +2 XP per year** (`blood_mage_yearly_events.001` for Mages, `.004` for Knights). Successfully executing a Murder scheme (`murder_success_pre_filter_on_action` -> `bm_on_murder_success_hulinhjalmur` in `common/on_action/bm_scheme_on_actions.txt`) reaps **1 Major Lifeforce** (`lifeforce_modifier_major`). |

## Inscribing Runes on Others (`bm_inscribe_rune_other_interaction`)

- **Initiation:** Available to both `lifestyle_blood_mage` and `lifestyle_blood_knight`.
- **Target Eligibility:** Living, non-imprisoned adults (`is_adult = yes`, `is_imprisoned = no`) who are courtiers, children, dynasty kin, spouses/consorts, sworn knights, Blood Golems (`house = house:bm_house_golem`), or the caster's liege.
- **Sequential Progression:**
  - Target has no rune -> Inscribes `minor_blood_rune_modifier` directly in interaction effect.
  - Target has Minor rune -> Upgrades depth to Major (`bm_upgrade_blood_rune_to_major_effect`).
  - Target has Major rune -> Upgrades depth to Superior (`bm_upgrade_blood_rune_to_superior_effect`; requires caster to have `lifestyle_blood_mage`).
- **XP Yield:** Grants `benediction` track XP (`+4 / +5 / +10`) to the caster.
- **Cooldown & Opinion:** Sets 5-year cooldown flag `bm_blood_rune_other_cooldown` on caster; adds `magic_opinion_positive` (`+20`) from recipient toward caster.

## Blood Temples Table

Duchy Capital buildings (`type = duchy_capital`) constructible in duchy capital holdings by rulers holding the duchy title. Always visible in the duchy building slot (shown grayed out with clear failure tooltips when requirements are not yet met). Constructible by characters with `lifestyle_blood_mage`, `lifestyle_blood_knight`, or a `blodtru_religion` faith. Tribal rulers can construct up to Tier IV (`Blood Temple`), while Tiers V–VII require a non-tribal government and a feudalized holding (Castle, City, or Temple):

| Tier | Building ID | Name | Devotion Gate (`piety_level`) & Government | Cost | Time | Holder Bonuses (`character_modifier`) | County & Holding Bonuses (`duchy_capital_county_modifier` / `province_modifier`) |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- | :--- |
| **I** | `bm_blood_temple_01` | **Blood Altar** | None (All Govs) | 150g | 1 yr | +0.5 piety, +5% piety mult, +0.2 health, +2 life expectancy | +0.1 dev growth, +5% dev factor, +0.1 control growth |
| **II** | `bm_blood_temple_02` | **Blood Shrine** | 1+ (All Govs) | 250g | 1.5 yrs | +1.0 piety, +10% piety mult, +0.1 dynasty prestige, +0.4 health, +4 life expectancy | +0.2 dev growth, +10% dev factor, +0.2 control growth |
| **III** | `bm_blood_temple_03` | **Blood Monument** | 2+ (All Govs) | 400g | 2 yrs | +1.5 piety, +15% piety mult, +0.2 dynasty prestige, +0.6 health, +6 life expectancy | +0.3 dev growth, +15% dev factor, +0.3 control growth |
| **IV** | `bm_blood_temple_04` | **Blood Temple** | 3+ (Tribal Capstone) | 600g | 2.5 yrs | +2.0 piety, +20% piety mult, +0.3 dynasty prestige, +0.8 health, +8 life expectancy | +0.4 dev growth, +20% dev factor, +0.4 control growth |
| **V** | `bm_blood_temple_05` | **Great Blood Temple** | 3+ (Non-Tribal) | 850g | 3 yrs | +2.5 piety, +25% piety mult, +0.5 dynasty prestige, +1.0 health, +10 life expectancy, +5% genetic inheritance & random chance | +0.5 dev growth, +25% dev factor, +0.5 control growth |
| **VI** | `bm_blood_temple_06` | **Blood Pantheon** | 4+ (Non-Tribal) | 1200g | 4 yrs | +3.0 piety, +30% piety mult, +0.75 dynasty prestige, +1.2 health, +12 life expectancy, +10% genetic inheritance & random chance | +0.6 dev growth, +30% dev factor, +0.6 control growth |
| **VII** | `bm_blood_temple_07` | **Blood Acropolis** | 5 (Non-Tribal) | 1600g | 5 yrs | +4.0 piety, +40% piety mult, +1.0 dynasty prestige, +1.4 health, +14 life expectancy, +15% genetic inheritance & random chance, +2 prowess | +0.8 dev growth, +40% dev factor, +0.8 control growth, +2 fort level, +5 defender advantage |

## Where the Details Live

| Piece | File |
| --- | --- |
| Stave, terror & Feingur bloodline modifiers | `common/modifiers/bm_blood_runes_modifiers.txt` |
| Stave modifier DDS icons (120x120) | `gfx/interface/icons/modifiers/bm_stave_<key>.dds` |
| Stave application & upgrade effects | `common/scripted_effects/bm_blood_runes_effects.txt` |
| Capstone stave decision | `common/decisions/cast_magic/bm_carve_galdrastafir_decision.txt` |
| Cast Blood Magic decisions | `common/decisions/cast_magic/bm_cast_blood_magic.txt` |
| Inscribe rune on other interaction | `common/character_interactions/bm_inscribe_rune_other.txt` |
| Bless Blood interaction (`bless_feingur` option) | `common/character_interactions/bm_bless_bloodline.txt` |
| Interaction icon | `gfx/interface/icons/character_interactions/bm_inscribe_rune_other_interaction.dds` |
| Yearly rune pulse & Hulinhjálmur Attunement hook | `events/bm_yearly_events.txt` (`.001`, `.003`, `.004`) |
| Vegvísir Blood Hunt cooldown & hazard hooks | `common/decisions/get_lifeforce/bm_seek_power_decision.txt`, `events/bm_seek_power_events.txt` |
| Feingur childbirth XP hook | `common/on_action/bm_blood_mage_prevalence_on_actions.txt` (`bm_on_birth_bloodline_xp`) |
| Travel POI hook (Nábrókarstafur) | `common/on_action/bm_travel_on_actions.txt` |
| Combat & duel Capstone hooks | `common/on_action/bm_combat_on_actions.txt`, `common/on_action/bm_duel_on_actions.txt` |
| Scheme murder Capstone hook (Hulinhjálmur) | `common/on_action/bm_scheme_on_actions.txt` |
| Story custom localization | `common/customizable_localization/bm_blood_mage_story_custom_loc.txt` |
| Localization | `localization/english/bm_blood_runes_l_english.yml`, `bm_modifiers_l_english.yml`, `bm_blood_mage_story_l_english.yml` |
| Blood Temple buildings | `common/buildings/bm_duchy_buildings.txt`, `localization/english/bm_buildings_l_english.yml`, `gfx/interface/icons/building_types/bm_blood_temple.dds` |
