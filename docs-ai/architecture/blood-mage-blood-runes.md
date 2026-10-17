# Blood Runes, Galdrastafir and Blood Architecture

Living technical specification for body runes, Galdrastafir staves, and blood architecture in the Blood Mage mod.

## Executive Summary

- **What:** Single-slot, sequential body rune system (Minor -> Major -> Superior) carved into flesh, pairing a base tier tracker (`minor/major/superior_blood_rune_modifier`) with 1 of 5 Galdrastafir staves (`bm_rune_<stave>_minor/major/superior`). Grants passive yearly Lifeforce rolls (`blood_mage_yearly_events.003`), scaling flat modifiers across all 3 tiers, and a Superior Capstone Hook unlocked exclusively at the Superior tier.
- **Self-Inscription (Ancient XP):** Cast via `bm_cast_blood_magic_minor_decision` (`bm_cast_blood_magic_minor.001`), upgraded sequentially via `bm_cast_blood_magic_major_decision` (`bm_cast_blood_magic_major.001`) and `bm_cast_blood_magic_superior_decision` (`bm_cast_blood_magic_superior.001`). Requires Devotion Rank 2 / 3 / 4 (`piety_level >= 2 / 3 / 4`; no track XP gate on self), sets a 5-year character cooldown flag (`bm_blood_rune_cooldown`), and awards `+4 / +5 / +10` `ancient` XP. Both **Blood Mages** (`lifestyle_blood_mage`) and **Blood Knights** (`lifestyle_blood_knight`) can self-inscribe up to Superior.
- **Inscribe on Others (Benediction XP):** Character interaction `bm_inscribe_rune_other_interaction` available to both `lifestyle_blood_mage` and `lifestyle_blood_knight`. Carves or upgrades a stave on a valid non-imprisoned adult target (courtier, family, child, spouse/consort, sworn knight, Blood Golem, liege) for the same Piety, Lifeforce, and Devotion Rank costs, plus a total Track XP gate (`25 / 50 / 100` XP via `bm_total_blood_mage_xp` / `bm_total_blood_knight_xp`). Sets a 5-year caster cooldown flag (`bm_blood_rune_other_cooldown`) and awards `+4 / +5 / +10` `benediction` XP to the caster. Inscribing **Superior** runes on others is exclusive to `lifestyle_blood_mage` (Blood Knights cap at Major when inscribing on others).
- **Flay Blood Rune (Swap Rite):** Agony rite (`bm_blood_runes.002`, triggered from `bm_cast_blood_magic_minor/major/superior.001`) burning `ancient` XP, Piety, and Lifeforce (plus inflicting wounds and casting exhaustion) to strip the active stave and immediately open `bm_blood_runes.001` to re-inscribe a new stave at the character's current rune tier.
- **University Buildings:** `bm_university_0` through `bm_university_3`. Duchy capital holdings built by rulers with `lifestyle_blood_mage`.

## Tier Progression, Costs & XP Table

| Rune Tier | Base Tracker | Self-Cast Gates (`minor/major/superior.001`) | Cast-on-Other Gates (`bm_inscribe_rune_other_interaction`) | Cost (Self & Other) | Self-Cast XP | Cast on Other XP | Yearly Lifeforce Pulse (`blood_mage_yearly_events.003`) | Flay & Swap Cost (`bm_blood_runes.002`) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Minor** | `minor_blood_rune_modifier` | Mage or Knight, Rank 2 (`piety_level >= 2`), 5-yr CD (`bm_blood_rune_cooldown`) | Mage or Knight, Rank 2 (`piety_level >= 2`), `>= 25` total XP, 5-yr CD (`bm_blood_rune_other_cooldown`) | 0 Piety + 1 Minor Lifeforce | `+4` `ancient` | `+4` `benediction` | 20% Minor | 250 Piety, `-5` `ancient` XP, 1 Minor LF + Minor Exhaustion (1 yr), `wounded_1` |
| **Major** | `major_blood_rune_modifier` | Mage or Knight, Rank 3 (`piety_level >= 3`), Minor Rune, 5-yr CD (`bm_blood_rune_cooldown`) | Mage or Knight, Rank 3 (`piety_level >= 3`), `>= 50` total XP, Minor Rune, 5-yr CD (`bm_blood_rune_other_cooldown`) | 200 Piety + 1 Major Lifeforce | `+5` `ancient` | `+5` `benediction` | 20% Minor, 10% Major, 5% Both | 500 Piety, `-10` `ancient` XP, 1 Major LF + Major Exhaustion (3 yrs + 1 yr extra stack), `wounded_1` |
| **Superior** | `superior_blood_rune_modifier` | Mage or Knight, Rank 4 (`piety_level >= 4`), Major Rune, 5-yr CD (`bm_blood_rune_cooldown`) | **Mage only**, Rank 4 (`piety_level >= 4`), `>= 100` total XP, Major Rune, 5-yr CD (`bm_blood_rune_other_cooldown`) | 400 Piety + 1 Superior Lifeforce | `+10` `ancient` | `+10` `benediction` | 10% Minor, 20% Major, 10% Both | 1000 Piety, `-15` `ancient` XP, 1 Superior LF + Superior Exhaustion (3 yrs), `wounded_2` |

*Yearly rolls handled by hidden pulse `blood_mage_yearly_events.003` (triggers on rune modifiers, no trait restriction). Recipients of all classes receive passive Lifeforce generation.*

## Galdrastafir Catalog (Flat Modifiers & Superior Capstones)

| # | Stave (`bm_rune_<key>_*`) | Flat Modifiers (Minor / Major / Superior) | Superior Capstone Effect (Active on `bm_rune_<key>_superior` only) |
| --- | --- | --- | --- |
| 1 | **Vegvísir** (`vegvisir`)<br/>*(The Wayfinder)* | • `character_travel_speed_mult = 0.15 / 0.25 / 0.40`<br/>• `character_travel_safety = 10 / 20 / 30`<br/>• `movement_speed = 0.05 / 0.10 / 0.15` | **Storm-Walker**: Halves `seek_power_decision` cooldown (`bm_seek_power_cooldown_days`: landed `730 -> 365` days; landless/adventurer `365 -> 182.5` days; note `seek_power_decision` is exclusive to Blood Knights) and eliminates negative hazard/escape rolls in `events/bm_seek_power_events.txt` (`seek_power.002`, `.003`, `.004`, `.005`). |
| 2 | **Ægishjálmur** (`aegishjalmur`)<br/>*(Helm of Awe)* | • `prowess = 3 / 6 / 9`<br/>• `advantage = 2 / 4 / 6`<br/>• `knight_effectiveness_mult = 0.10 / 0.20 / 0.30` | **Terror of the Slain**: On battle start (`on_combat_start` -> `bm_on_combat_start_aegishjalmur_terror` in `common/on_action/bm_duel_on_actions.txt`), if any commander or knight on a side holds `bm_rune_aegishjalmur_superior`, inflicts `bm_aegishjalmur_terror_modifier` (`prowess = -5`, `health = -0.5`, 1 year) on the opposing side's commander and all opposing knights. |
| 3 | **Feingur** (`feingur`)<br/>*(Awakened Seed)* | • `fertility = 0.10 / 0.20 / 0.30`<br/>• `years_of_fertility = 5 / 10 / 20`<br/>• `positive_random_genetic_chance = 0.10 / 0.20 / 0.30`<br/>• `health = 0.20 / 0.40 / 0.60`<br/>• `epidemic_resistance = 5 / 10 / 20` | **Awakened Seed**: Doubles XP gained on childbirth (`bm_on_birth_bloodline_xp` in `common/on_action/bm_blood_mage_prevalence_on_actions.txt`: `+4` base, `+8` if child inherits `lifestyle_blood_mage`; grants `bloodline` XP for Mages or `vanguard` XP for Knights). Unlocks character interaction `bm_feingur_bless_dynasty_interaction` (cost: 50 Piety + 1 Minor Lifeforce; grants `+2` `bloodline` XP for Mages or `+2` `vanguard` XP for Knights, plus `+40` opinion) applying permanent modifier `bm_feingur_blessed_blood_modifier` (`diplomacy = 1`, `martial = 1`, `stewardship = 1`, `intrigue = 1`, `learning = 1`, `prowess = 2`, `fertility = 0.15`, `health = 0.35`, `positive_random_genetic_chance = 0.15`; stacks alongside 10-yr `bm_blessed_blood_modifier`) to any child or dynasty kin. |
| 4 | **Nábrókarstafur** (`nabrokarstafur`)<br/>*(Flayed Tithe)* | • `domain_tax_mult = 0.05 / 0.10 / 0.20`<br/>• `men_at_arms_maintenance = -0.05 / -0.10 / -0.15`<br/>• `general_opinion = -5 / -10 / -15` | **Flayed Tithe**: Visiting Points of Interest during travel (`on_travel_plan_movement` -> `bm_on_visited_point_of_interest` in `common/on_action/bm_travel_on_actions.txt`) awards **+20 Gold** once per POI province (tracked via `bm_nabrokarstafur_visited_poi` variable list). Winning battles (`on_combat_end_winner` -> `bm_on_combat_end_winner` in `common/on_action/bm_combat_on_actions.txt`) as commander or knight plunders **10% of enemy fatal casualties** as Gold (`bm_nabrokarstafur_battle_gold_value`), clamped between **25** and **250 Gold**. |
| 5 | **Hulinhjálmur** (`hulinhjalmur`)<br/>*(Unseen Shroud)* | • `owned_hostile_scheme_success_chance_add = 10 / 20 / 30`<br/>• `enemy_hostile_scheme_success_chance_add = -10 / -20 / -30`<br/>• `monthly_lifestyle_xp_gain_mult = 0.10 / 0.20 / 0.30` | **Unseen Shroud**: Doubles guaranteed yearly discipline Attunement XP gain from **+1 XP to +2 XP per year** (`blood_mage_yearly_events.001` for Mages, `.004` for Knights). Successfully executing a Murder scheme (`murder_success_pre_filter_on_action` -> `bm_on_murder_success_hulinhjalmur` in `common/on_action/bm_scheme_on_actions.txt`) reaps **1 Major Lifeforce** (`lifeforce_modifier_major`). |

## Inscribing Runes on Others (`bm_inscribe_rune_other_interaction`)

- **Initiation:** Available to both `lifestyle_blood_mage` and `lifestyle_blood_knight`.
- **Target Eligibility:** Living, non-imprisoned adults (`is_adult = yes`, `is_imprisoned = no`) who are courtiers, children, dynasty kin, spouses/consorts, sworn knights, Blood Golems (`blood_golem`), or the caster's liege.
- **Sequential Progression:**
  - Target has no rune -> Inscribes `minor_blood_rune_modifier` and opens 5-stave selector (`bm_blood_runes.001` with `scope:recipient` saved as `scope:rune_target`).
  - Target has Minor rune -> Upgrades active stave in-place to Major (`bm_upgrade_blood_rune_to_major_effect`).
  - Target has Major rune -> Upgrades active stave in-place to Superior (`bm_upgrade_blood_rune_to_superior_effect`; requires caster to have `lifestyle_blood_mage`).
- **XP Yield:** Grants `benediction` track XP (`+4 / +5 / +10`) to the caster instead of `ancient` XP.
- **Cooldown & Opinion:** Sets 5-year cooldown flag `bm_blood_rune_other_cooldown` on caster; adds `magic_opinion_positive` (`+20`) from recipient toward caster.

## Blood Universities Table

Duchy capital buildings constructible only if holder has `lifestyle_blood_mage`:

| Tier | Building ID | Cost | Time | Penalties | Province & Realm Bonuses |
| --- | --- | --- | --- | --- | --- |
| **0** | `bm_university_0` | 250g, 250p | 3 yrs | -0.1 income, -0.1 piety | +0.1 dev growth, +5% cultural fascination |
| **1** | `bm_university_1` | 500g, 500p | 5 yrs | -0.2 income, -0.2 piety | +0.2 dev growth, +10% cultural fascination |
| **2** | `bm_university_2` | 750g, 750p | 7 yrs | -0.3 income, -0.3 piety | +0.3 dev growth, +15% cultural fascination |
| **3** | `bm_university_3` | 1000g, 1000p | 10 yrs | -0.4 income, -0.4 piety | +0.4 dev growth, +20% cultural fascination |

## Where the Details Live

| Piece | File |
| --- | --- |
| Stave, terror & Feingur bloodline modifiers | `common/modifiers/bm_blood_runes_modifiers.txt` |
| Stave application & upgrade effects | `common/scripted_effects/bm_blood_runes_effects.txt` |
| Galdrastafir selector & flay events | `events/bm_blood_runes_events.txt` (`bm_blood_runes.001`, `.002`) |
| Cast Blood Magic decisions | `common/decisions/cast_magic/bm_cast_blood_magic.txt` |
| Self-cast rune events | `events/bm_cast_blood_magic_minor_events.txt`, `major_events.txt`, `superior_events.txt` |
| Inscribe rune on other interaction | `common/character_interactions/bm_inscribe_rune_other.txt` |
| Feingur bless dynasty interaction | `common/character_interactions/bm_feingur_bless_dynasty.txt` |
| Interaction icons | `gfx/interface/icons/character_interactions/bm_inscribe_rune_other_interaction.dds`, `bm_feingur_bless_dynasty_interaction.dds` |
| Yearly rune pulse & Hulinhjálmur Attunement hook | `events/bm_yearly_events.txt` (`.001`, `.003`, `.004`) |
| Vegvísir Seek Power cooldown & hazard hooks | `common/decisions/get_lifeforce/bm_seek_power_decision.txt`, `events/bm_seek_power_events.txt` |
| Feingur childbirth XP hook | `common/on_action/bm_blood_mage_prevalence_on_actions.txt` (`bm_on_birth_bloodline_xp`) |
| Travel POI hook (Nábrókarstafur) | `common/on_action/bm_travel_on_actions.txt` |
| Combat & duel Capstone hooks | `common/on_action/bm_combat_on_actions.txt`, `common/on_action/bm_duel_on_actions.txt` |
| Scheme murder Capstone hook (Hulinhjálmur) | `common/on_action/bm_scheme_on_actions.txt` |
| Flay & battle gold script values | `common/script_values/bm_blood_rune_cost.txt`, `common/script_values/bm_blood_mage_story_values.txt` |
| Story custom localization | `common/customizable_localization/bm_blood_mage_story_custom_loc.txt` |
| Localization | `localization/english/bm_blood_runes_l_english.yml`, `bm_modifiers_l_english.yml`, `bm_blood_mage_story_l_english.yml` |
| Duchy capital buildings | `common/buildings/bm_duchy_buildings.txt` |
