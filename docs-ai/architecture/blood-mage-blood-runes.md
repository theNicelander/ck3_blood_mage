# Blood Runes, Galdrastafir and Blood Architecture

Living technical specification for body runes, Galdrastafir staves, and blood architecture in the Blood Mage mod.

## Executive Summary

- **What:** Decoupled rune architecture separating **Rune Depth** (`minor/major/superior_blood_rune_modifier`) from **Galdrastafir Stave Identity** (`bm_stave_<key>`).
  - **Rune Depth (3 modifiers):** Sequential body runes (Minor -> Major -> Superior) that provide **no flat stat bonuses** themselves, solely governing the passive yearly Lifeforce pulse (`blood_mage_yearly_events.003`) and acting as the unlock gate for the capstone stave.
  - **Capstone Staves (5 modifiers):** Granted exclusively at **Superior** rune depth via the standalone option-list decision `bm_carve_galdrastafir_decision`. Each stave grants flat static attributes and an active occult capstone mechanic.
- **Self-Inscription (Ancient XP):** Inscribed sequentially via Cast Blood Magic Decision Widgets (`bm_cast_blood_magic_minor_decision`, `major_decision`, `superior_decision`). Requires Devotion Rank 2 / 3 / 4 (`piety_level >= 2 / 3 / 4`), sets a 5-year character cooldown flag (`bm_blood_rune_cooldown`), and awards `+4 / +5 / +10` `ancient` XP. Both **Blood Mages** and **Blood Knights** can self-inscribe up to Superior.
- **Inscribe on Others (Benediction XP):** Character interaction `bm_inscribe_rune_other_interaction` available to both classes. Upgrades target depth in-place (does not inscribe staves; target must use the decision once reaching Superior). Sets a 5-year cooldown (`bm_blood_rune_other_cooldown`) and awards `+4 / +5 / +10` `benediction` XP to caster. Inscribing **Superior** runes on others is exclusive to `lifestyle_blood_mage`.
- **Capstone Stave Selection & Swapping:** Handled via the standalone decision `bm_carve_galdrastafir_decision` (`common/decisions/cast_magic/bm_carve_galdrastafir_decision.txt`), shown only to characters holding `superior_blood_rune_modifier`. Costs **500 Piety** (`bm_carve_galdrastafir_piety_cost`) and **1 Major Lifeforce** (`blood_magic_used_major`), with a 5-year decision cooldown. All 5 staves are displayed; the currently worn stave is grayed out.
- **University Buildings:** `bm_university_0` through `bm_university_3`. Duchy capital holdings built by rulers with `lifestyle_blood_mage`, `lifestyle_blood_knight`, or whose faith belongs to `blodtru_religion`.

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
| 3 | **Feingur** (`feingur`)<br/>*(Awakened Seed)* | • `fertility = 0.20`<br/>• `years_of_fertility = 10`<br/>• `positive_random_genetic_chance = 0.20`<br/>• `health = 0.40`<br/>• `epidemic_resistance = 10` | **Awakened Seed**: Doubles XP gained on childbirth (`bm_on_birth_bloodline_xp` in `common/on_action/bm_blood_mage_prevalence_on_actions.txt`: `+4` base, `+8` if child inherits `lifestyle_blood_mage`; grants `bloodline` XP for Mages or `vanguard` XP for Knights). Unlocks character interaction `bm_feingur_bless_dynasty_interaction` (cost: 50 Piety + 1 Minor Lifeforce) applying permanent modifier `bm_feingur_blessed_blood_modifier` (`diplomacy = 1`, `martial = 1`, `stewardship = 1`, `intrigue = 1`, `learning = 1`, `prowess = 2`, `fertility = 0.15`, `health = 0.35`, `positive_random_genetic_chance = 0.15`) to any child or dynasty kin. |
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

## Blood Universities Table

Duchy capital buildings constructible by rulers with `lifestyle_blood_mage`, `lifestyle_blood_knight`, or a `blodtru_religion` faith:

| Tier | Building ID | Cost | Time | Upkeep | Province & Realm Bonuses |
| --- | --- | --- | --- | --- | --- |
| **0** | `bm_university_0` | 250g | 1 yr | -0.1 income | +0.5 piety, +5% piety mult, +0.1 dev growth, +5% cultural fascination |
| **1** | `bm_university_1` | 500g | 2 yrs | -0.25 income | +1.0 piety, +10% piety mult, +0.15 dev growth, +10% cultural fascination, +0.1 prestige, +3% lifestyle XP |
| **2** | `bm_university_2` | 750g | 3 yrs | -0.5 income | +1.75 piety, +15% piety mult, +0.2 dev growth, +15% cultural fascination, +0.2 prestige, +6% lifestyle XP |
| **3** | `bm_university_3` | 1000g | 5 yrs | -1.0 income | +2.5 piety, +25% piety mult, +0.3 dev growth, +25% cultural fascination, +0.3 prestige, +10% lifestyle XP |

## Where the Details Live

| Piece | File |
| --- | --- |
| Stave, terror & Feingur bloodline modifiers | `common/modifiers/bm_blood_runes_modifiers.txt` |
| Stave modifier DDS icons (120x120) | `gfx/interface/icons/modifiers/bm_stave_<key>.dds` |
| Stave application & upgrade effects | `common/scripted_effects/bm_blood_runes_effects.txt` |
| Capstone stave decision | `common/decisions/cast_magic/bm_carve_galdrastafir_decision.txt` |
| Cast Blood Magic decisions | `common/decisions/cast_magic/bm_cast_blood_magic.txt` |
| Inscribe rune on other interaction | `common/character_interactions/bm_inscribe_rune_other.txt` |
| Feingur bless dynasty interaction | `common/character_interactions/bm_feingur_bless_dynasty.txt` |
| Interaction icons | `gfx/interface/icons/character_interactions/bm_inscribe_rune_other_interaction.dds`, `bm_feingur_bless_dynasty_interaction.dds` |
| Yearly rune pulse & Hulinhjálmur Attunement hook | `events/bm_yearly_events.txt` (`.001`, `.003`, `.004`) |
| Vegvísir Blood Hunt cooldown & hazard hooks | `common/decisions/get_lifeforce/bm_seek_power_decision.txt`, `events/bm_seek_power_events.txt` |
| Feingur childbirth XP hook | `common/on_action/bm_blood_mage_prevalence_on_actions.txt` (`bm_on_birth_bloodline_xp`) |
| Travel POI hook (Nábrókarstafur) | `common/on_action/bm_travel_on_actions.txt` |
| Combat & duel Capstone hooks | `common/on_action/bm_combat_on_actions.txt`, `common/on_action/bm_duel_on_actions.txt` |
| Scheme murder Capstone hook (Hulinhjálmur) | `common/on_action/bm_scheme_on_actions.txt` |
| Story custom localization | `common/customizable_localization/bm_blood_mage_story_custom_loc.txt` |
| Localization | `localization/english/bm_blood_runes_l_english.yml`, `bm_modifiers_l_english.yml`, `bm_blood_mage_story_l_english.yml` |
| Duchy capital buildings | `common/buildings/bm_duchy_buildings.txt` |
