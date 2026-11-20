# Blood Runes, Galdrastafir and Blood Architecture

Living technical specification for body runes, Galdrastafir staves, and Duchy Blood Temples.

## Overview

Decoupled architecture separating **Rune Depth** (`minor/major/superior_blood_rune_modifier`) from **Galdrastafir Stave Identity** (`bm_stave_<key>`).
- **Rune Depth:** Sequential body runes (Minor -> Major -> Superior) governing the passive yearly Lifeforce pulse (`blood_mage_yearly_events.003`) and unlocking the capstone stave.
- **Capstone Staves:** Granted at **Superior** depth via `bm_carve_galdrastafir_decision` (500 Piety, 1 Major LF, 5-yr CD). Grants static attributes and an active occult capstone mechanic.
- **Self-Inscription (`ancient` XP):** Inscribed sequentially via Cast Blood Magic widgets (`minor/major/superior`). Requires Devotion Rank 2 / 3 / 4, 3-yr CD (`bm_blood_rune_cooldown`), awards `+4 / +5 / +10` `ancient` XP. Blood Mages can self-inscribe up to Superior.
- **Inscribe on Others (`radiance` XP):** Interaction `bm_inscribe_rune_other_interaction` upgrades target depth in-place. 3-yr CD (`bm_blood_rune_other_cooldown`), awards `+4 / +5 / +10` `radiance` XP. Superior on others is Mage exclusive.
- **Duchy Blood Temple District:** 4-tier Duchy Capital district (`bm_blood_temple_district` in `common/districts/bm_duchy_districts.txt`, `type = duchy_capital`) with primary Blood Temple (`bm_blood_temple_01..04`, unlocking 1–4 sub-building slots) and 6 specialized 4-tier Blood Mage sub-buildings (`common/buildings/bm_duchy_district_buildings.txt`), constructible in duchy capital slots by Blood Mages or Blóðtrú faithful. Tiers I–II open to all governments; Tiers III–IV require non-tribal feudalized holdings.

## Tier Progression, Costs & XP Table

| Rune Tier | Base Tracker | Self-Cast Gates (`minor/major/superior_decision`) | Cast-on-Other Gates (`bm_inscribe_rune_other_interaction`) | Cost (Self & Other) | Self-Cast XP | Cast on Other XP | Yearly Lifeforce Pulse (`blood_mage_yearly_events.003`) | Capstone Stave Access (`bm_carve_galdrastafir_decision`) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Minor** | `minor_blood_rune_modifier` | Mage, Rank 2 (`piety_level >= 2`), 3-yr CD (`bm_blood_rune_cooldown`) | Mage, Rank 2 (`piety_level >= 2`), `>= 25` total XP, 3-yr CD (`bm_blood_rune_other_cooldown`) | 0 Piety + 1 Minor Lifeforce | `+4` `ancient` | `+4` `radiance` | 20% Minor | Locked |
| **Major** | `major_blood_rune_modifier` | Mage, Rank 3 (`piety_level >= 3`), Minor Rune, 3-yr CD (`bm_blood_rune_cooldown`) | Mage, Rank 3 (`piety_level >= 3`), `>= 50` total XP, Minor Rune, 3-yr CD (`bm_blood_rune_other_cooldown`) | 200 Piety + 1 Major Lifeforce | `+5` `ancient` | `+5` `radiance` | 20% Minor, 10% Major, 5% Both | Locked |
| **Superior** | `superior_blood_rune_modifier` | Mage, Rank 4 (`piety_level >= 4`), Major Rune, 3-yr CD (`bm_blood_rune_cooldown`) | **Mage only**, Rank 4 (`piety_level >= 4`), `>= 100` total XP, Major Rune, 3-yr CD (`bm_blood_rune_other_cooldown`) | 400 Piety + 1 Superior Lifeforce | `+10` `ancient` | `+10` `radiance` | 10% Minor, 20% Major, 10% Both | **Unlocked**: First pick free; 5-yr swap for 500 Piety + 1 Major Lifeforce in Major Grimoire |

*Yearly rolls handled by hidden pulse `blood_mage_yearly_events.003` (triggers on rune modifiers, no trait restriction).*

## Galdrastafir Catalog (Flat Modifiers & Superior Capstones)

| # | Stave (`bm_stave_<key>`) | Flat Modifiers | Superior Capstone Effect (Active on `bm_stave_<key>` with Superior depth) |
| --- | --- | --- | --- |
| 1 | **Vegvísir** (`vegvisir`)<br/>*(The Wayfinder)* | • `character_travel_speed_mult = 0.25`<br/>• `character_travel_safety = 20`<br/>• `movement_speed = 0.10` | **Storm-Walker**: Halves `seek_power_decision` (Blood Hunt) cooldown (`bm_seek_power_cooldown_days`: `365 -> 182.5` days / 6 months) and eliminates escape/witness hazard rolls when pursuing travelers in `events/bm_seek_power_events.txt` (`seek_power.003`). |
| 2 | **Ægishjálmur** (`aegishjalmur`)<br/>*(Helm of Awe)* | • `prowess = 6`<br/>• `advantage = 4`<br/>• `knight_effectiveness_mult = 0.20` | **Terror of the Slain**: On battle start (`on_combat_start` -> `bm_on_combat_start_aegishjalmur_terror` in `common/on_action/bm_duel_on_actions.txt`), if any commander or knight holds Ægishjálmur at Superior depth, inflicts `bm_aegishjalmur_terror_modifier` (`prowess = -5`, `health = -0.5`, 1 year) on the opposing commander and all opposing knights. |
| 3 | **Feingur** (`feingur`)<br/>*(Awakened Seed)* | • `fertility = 0.20`<br/>• `years_of_fertility = 10`<br/>• `positive_random_genetic_chance = 0.20`<br/>• `health = 0.40`<br/>• `epidemic_resistance = 10` | **Awakened Seed**: Doubles XP gained on childbirth (`bm_on_birth_fortune_xp` in `common/on_action/bm_blood_mage_prevalence_on_actions.txt`: `+2` base, `+4` if child inherits `lifestyle_blood_mage`; grants `fortune` XP). Unlocks the `bless_feingur` option in `bm_bless_bloodline_interaction` (cost: 50 Piety + 1 Minor Lifeforce) applying permanent modifier `bm_feingur_blessed_blood_modifier` (`fertility = 0.25`, `positive_random_genetic_chance = 0.20`, `health = 0.50`, `life_expectancy = 5`) to any child or dynasty kin. |
| 4 | **Nábrókarstafur** (`nabrokarstafur`)<br/>*(Flayed Tithe)* | • `monthly_income_mult = 0.10`<br/>• `monthly_income_from_trade_mult = 0.10`<br/>• `trade_competitiveness_mult = 0.10`<br/>• `men_at_arms_maintenance = -0.10`<br/>• `general_opinion = -10` | **Flayed Tithe**: Visiting Points of Interest during travel (`on_travel_plan_movement` -> `bm_on_visited_point_of_interest` in `common/on_action/bm_travel_on_actions.txt`) awards **+20 Gold** once per POI province (`bm_nabrokarstafur_visited_poi`). Winning battles (`on_combat_end_winner` -> `bm_on_combat_end_winner` in `common/on_action/bm_combat_on_actions.txt`) as commander or knight plunders **10% of enemy fatal casualties** as Gold (`bm_nabrokarstafur_battle_gold_value`), clamped between **25** and **250 Gold**. |
| 5 | **Hulinhjálmur** (`hulinhjalmur`)<br/>*(Unseen Shroud)* | • `owned_hostile_scheme_success_chance_add = 20`<br/>• `enemy_hostile_scheme_success_chance_add = -20`<br/>• `monthly_lifestyle_xp_gain_mult = 0.20` | **Unseen Shroud**: Doubles guaranteed yearly discipline Attunement XP gain from **+1 XP to +2 XP per year** (`blood_mage_yearly_events.001` for Mages, `.004` for Knights). Successfully executing a Murder scheme (`murder_success_pre_filter_on_action` -> `bm_on_murder_success_hulinhjalmur` in `common/on_action/bm_scheme_on_actions.txt`) reaps **1 Major Lifeforce** (`lifeforce_modifier_major`). |

## Inscribing Runes on Others (`bm_inscribe_rune_other_interaction`)

- **Initiation:** Available to `lifestyle_blood_mage`.
- **Target Eligibility:** Living, non-imprisoned adults (`is_adult = yes`, `is_imprisoned = no`) who are courtiers, children, dynasty kin, spouses/consorts, sworn knights, Blood Golems (`house = house:bm_house_golem`), or the caster's liege.
- **Sequential Progression:**
  - Target has no rune -> Inscribes `minor_blood_rune_modifier` directly in interaction effect.
  - Target has Minor rune -> Upgrades depth to Major (`bm_upgrade_blood_rune_to_major_effect`).
  - Target has Major rune -> Upgrades depth to Superior (`bm_upgrade_blood_rune_to_superior_effect`; requires caster to have `lifestyle_blood_mage`).
- **XP Yield:** Grants `radiance` track XP (`+4 / +5 / +10`) to the caster.
- **Cooldown & Opinion:** Sets 3-year cooldown flag `bm_blood_rune_other_cooldown` on caster; adds `magic_opinion_positive` (`+20`) from recipient toward caster.

## Blood Temple District Tables

Duchy Capital district (`bm_blood_temple_district` in `common/districts/bm_duchy_districts.txt`, `type = duchy_capital`) housing the 4-tier primary Blood Temple (`bm_blood_temple_01..04`), 6 specialized 4-tier Blood Mage sub-buildings (`common/buildings/bm_duchy_district_buildings.txt`), and shared vanilla religious/burial sub-buildings (`consistory_01`, `almonry_general_01`, `pilgrimage_office_01`, `burial_site_01`, `charnel_grounds_01`, `great_megalith_01`, `tower_of_silence_01`; max 4 slots per duchy). Constructible by rulers holding the duchy title with `lifestyle_blood_mage` or a `blodtru_religion` faith. Tiers I–II are open to all governments; Tiers III–IV require a non-tribal government and feudalized holding.

### Primary Building (`bm_blood_temple_01..04`)

| Tier | Building ID | Name | Devotion & Gov | Cost | Time | Province (`province_modifier`) | Holder (`character_modifier`) | Duchy County (`duchy_capital_county_modifier`) |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- | :--- | :--- |
| **I** | `bm_blood_temple_01` | **Blood Altar** | None (All) | 200g | 1 yr | 1 slot, +10 settlement size baseline | +0.5 piety, +5% piety mult | +0.05 prosperity growth, +5% levy size |
| **II** | `bm_blood_temple_02` | **Blood Shrine** | 1+ (All) | 400g | 1.5 yrs | 2 slots, +30 settlement size baseline | +1.0 piety, +10% piety mult | +0.10 prosperity growth, +10% levy size |
| **III** | `bm_blood_temple_03` | **Blood Temple** | 2+ (Feudalized) | 700g | 2 yrs | 3 slots, +50 settlement size baseline | +1.5 piety, +15% piety mult | +0.15 prosperity growth, +15% levy size |
| **IV** | `bm_blood_temple_04` | **Blood Acropolis** | 3+ (Feudalized) | 1100g | 3 yrs | 4 slots, +80 settlement size baseline, +2 fort level, +5 defender advantage | +2.0 piety, +20% piety mult | +0.20 prosperity growth, +20% levy size |

### Sub-Buildings (`bm_duchy_district_buildings.txt`, 250 / 450 / 750 / 1100g, 365 / 545 / 730 / 910d, `district_level_requirement = 2..4` on T2–T4)

| Sub-Building | Keys (`01..04`) | Tier I → IV Bonuses |
| :--- | :--- | :--- |
| **Blood Sanctuary** | `bm_blood_sanctuary_01..04` | Health +0.5/+1.0/+1.5/+2.0, Life Expectancy +4/+8/+12/+16, Duchy Epidemic Resistance +5/+10/+15/+20 |
| **Bloodline Vault** | `bm_bloodline_vault_01..04` | Positive Inactive Inheritance, Random Genetic & Strengthening Chance +4%/+8%/+12%/+16% each, Inbreeding Chance -5%/-10%/-15%/-20% |
| **Blood Academy** | `bm_blood_academy_01..04` | Learning +1/+2/+3/+4 (+1/+2 per Piety Level at T3/T4), General Lifestyle XP +4%/+8%/+12%/+16% & +2/+4/+7/+10 flat monthly, Cultural Fascination +5%/+10%/+15%/+20% |
| **Hall of Blood Ancestors** | `bm_blood_ancestors_hall_01..04` | Dynasty Prestige +0.25/+0.50/+0.75/+1.0 & +5%/+10%/+15%/+20% mult, Legitimacy Gain +5%/+10%/+15%/+20% |
| **Blood Basin** | `bm_blood_basin_01..04` | Duchy Prosperity Growth +0.15/+0.30/+0.50/+0.75 & +5%/+10%/+15%/+25% factor, Control Baseline +3/+6/+10/+15, Control Growth +0.15/+0.30/+0.50/+0.75 |
| **Ritual Vaults** | `bm_ritual_vaults_01..04` | Monthly Piety +0.5/+1.0/+1.5/+2.0 & +5%/+10%/+15%/+25% mult, Piety/Knight +0.04/+0.08/+0.12/+0.18, Dread Baseline +5/+10/+15/+20 |

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
| Feingur childbirth XP hook | `common/on_action/bm_blood_mage_prevalence_on_actions.txt` (`bm_on_birth_fortune_xp`) |
| Travel POI hook (Nábrókarstafur) | `common/on_action/bm_travel_on_actions.txt` |
| Combat & duel Capstone hooks | `common/on_action/bm_combat_on_actions.txt`, `common/on_action/bm_duel_on_actions.txt` |
| Scheme murder Capstone hook (Hulinhjálmur) | `common/on_action/bm_scheme_on_actions.txt` |
| Story custom localization | `common/customizable_localization/bm_blood_mage_story_custom_loc.txt` |
| Localization | `localization/english/bm_blood_runes_l_english.yml`, `bm_modifiers_l_english.yml`, `bm_blood_mage_story_l_english.yml` |
| Blood Temple district & buildings | `common/districts/bm_duchy_districts.txt`, `common/buildings/bm_duchy_buildings.txt`, `common/buildings/bm_duchy_district_buildings.txt`, `localization/english/bm_buildings_l_english.yml`, `gfx/interface/icons/building_types/bm_blood_temple.dds` |
