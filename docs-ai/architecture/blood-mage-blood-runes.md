# Blood Runes, Galdrastafir and Blood Architecture

Living technical specification for body runes, Galdrastafir staves, and blood architecture in the Blood Mage mod.

## Executive Summary

- **What:** Single-slot, sequential body rune system (Minor -> Major -> Superior) carved into flesh, pairing a base tier tracker (`minor/major/superior_blood_rune_modifier`) with 1 of 5 Galdrastafir staves (`bm_rune_<stave>_minor/major/superior`). Grants passive yearly Lifeforce rolls (`blood_mage_yearly_events.003`), scaling flat modifiers across all 3 tiers, and a Superior Capstone Hook unlocked exclusively at the Superior tier.
- **Self-Inscription (Ancient XP):** Cast via `bm_cast_blood_magic_minor_decision` (`bm_cast_blood_magic_minor.001`), upgraded via `major.001` and `superior.001`. Requires Devotion Rank 2 / 3 / 4 (`piety_level >= 2 / 3 / 4`; no track XP gate on self) and awards `+4 / +5 / +10` `ancient` XP. Both **Blood Mages** and **Blood Knights** can self-inscribe up to Superior.
- **Inscribe on Others (Benediction XP):** Character interaction `bm_inscribe_rune_other_interaction` available to both `lifestyle_blood_mage` and `lifestyle_blood_knight`. Carves or upgrades a stave on a valid adult target (courtier, family, child, spouse/consort, sworn knight, Blood Golem, liege) for the same Piety, Lifeforce, and Devotion Rank costs, plus a total Track XP gate (`25 / 50 / 100` XP). Awards `+4 / +5 / +10` `benediction` XP to the caster. Inscribing **Superior** runes on others is exclusive to `lifestyle_blood_mage`.
- **Flay Blood Rune (Swap Rite):** Agony rite (`bm_blood_runes.002`) burning `ancient` XP, Piety, and Lifeforce (plus inflicting wounds and casting exhaustion) to strip the active stave and re-inscribe a new one at the character's current tier.
- **University Buildings:** `bm_university_0` through `bm_university_3`. Duchy capital holdings built by rulers with `lifestyle_blood_mage`.

## Tier Progression, Costs & XP Table

| Rune Tier | Base Tracker | Self-Cast Gates (`minor/major/superior.001`) | Cast-on-Other Gates (`bm_inscribe_rune_other_interaction`) | Cost (Self & Other) | Self-Cast XP | Cast on Other XP | Yearly Lifeforce Pulse (`blood_mage_yearly_events.003`) | Flay & Swap Cost (Self) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Minor** | `minor_blood_rune_modifier` | Mage or Knight, Rank 2 (`piety_level >= 2`) | Mage or Knight, Rank 2 (`piety_level >= 2`), `>= 25` total XP | 0 Piety + 1 Minor Lifeforce | `+4` `ancient` | `+4` `benediction` | 20% Minor | 250 Piety, `-5` `ancient` XP, 1 Minor LF, `wounded_1` |
| **Major** | `major_blood_rune_modifier` | Mage or Knight, Rank 3 (`piety_level >= 3`), Minor Rune | Mage or Knight, Rank 3 (`piety_level >= 3`), `>= 50` total XP, Minor Rune | 200 Piety + 1 Major Lifeforce | `+5` `ancient` | `+5` `benediction` | 20% Minor, 10% Major, 5% Both | 500 Piety, `-10` `ancient` XP, 1 Major LF, `wounded_1`, Major Exhaustion (1 yr) |
| **Superior** | `superior_blood_rune_modifier` | Mage or Knight, Rank 4 (`piety_level >= 4`), Major Rune | **Mage only**, Rank 4 (`piety_level >= 4`), `>= 100` total XP, Major Rune | 400 Piety + 1 Superior Lifeforce | `+10` `ancient` | `+10` `benediction` | 10% Minor, 20% Major, 10% Both | 1000 Piety, `-15` `ancient` XP, 1 Superior LF, `wounded_2`, Superior Exhaustion (5 yrs) |

*Yearly rolls handled by hidden pulse `blood_mage_yearly_events.003` (triggers on rune modifiers, no trait restriction). Recipients of all classes receive passive Lifeforce generation.*

## Galdrastafir Catalog (Flat Modifiers & Superior Capstones)

| # | Stave (`bm_rune_<key>_*`) | Flat Modifiers (Minor / Major / Superior) | Superior Capstone Effect (Active on `bm_rune_<key>_superior` only) |
| --- | --- | --- | --- |
| 1 | **Vegvísir** (`vegvisir`)<br/>*(The Wayfinder)* | • `character_travel_speed_mult = 0.15 / 0.25 / 0.40`<br/>• `character_travel_safety = 10 / 20 / 30`<br/>• `movement_speed = 0.05 / 0.10 / 0.15` | **Storm-Walker**: Halves `seek_power_decision` cooldowns (`seek_power_decision` to 1 yr; `seek_power_decision_wanderer` and `seek_power_decision_blood_knight` to 6 months) and eliminates negative hazard rolls (escape / witnessed) in `bm_seek_power_events.txt`. |
| 2 | **Ægishjálmur** (`aegishjalmur`)<br/>*(Helm of Awe)* | • `prowess = 3 / 6 / 9`<br/>• `advantage = 2 / 4 / 6`<br/>• `knight_effectiveness_mult = 0.10 / 0.20 / 0.30` | **Terror of the Slain**: On combat start / battle clash (`bm_duel_on_actions.txt`), strikes dread into enemies by applying `bm_aegishjalmur_terror_modifier` (`prowess = -5`, `health = -0.5`, 1 year) to opposing commanders and knights. |
| 3 | **Feingur** (`feingur`)<br/>*(Awakened Seed)* | • `fertility = 0.10 / 0.20 / 0.30`<br/>• `years_of_fertility = 5 / 10 / 20`<br/>• `positive_random_genetic_chance = 0.10 / 0.20 / 0.30`<br/>• `health = 0.20 / 0.40 / 0.60`<br/>• `epidemic_resistance = 5 / 10 / 20` | **Awakened Seed**: Doubles XP gained on childbirth (`bm_on_birth_bloodline_xp`: `+4` base, `+8` if inherited; grants `bloodline` XP for Mages or `vanguard` XP for Knights). Unlocks character interaction `bm_feingur_bless_dynasty_interaction` applying permanent modifier `bm_feingur_blessed_blood_modifier` (`fertility = 0.10`, `health = 0.25`, `years_of_fertility = 5`, `aging_attrition_mult = -0.25`) to child or dynasty kin. |
| 4 | **Nábrókarstafur** (`nabrokarstafur`)<br/>*(Flayed Tithe)* | • `domain_tax_mult = 0.05 / 0.10 / 0.20`<br/>• `men_at_arms_maintenance = -0.05 / -0.10 / -0.15`<br/>• `general_opinion = -5 / -10 / -15` | **Flayed Tithe**: Visiting Points of Interest during travel awards **+20 Gold** once per POI province (`bm_travel_on_actions.txt`). Winning battles (`bm_on_combat_end_winner`) plunders **10% of enemy fatal casualties** as Gold, clamped between **25** and **250 Gold** (`bm_combat_on_actions.txt`). |
| 5 | **Hulinhjálmur** (`hulinhjalmur`)<br/>*(Unseen Shroud)* | • `owned_hostile_scheme_success_chance_add = 10 / 20 / 30`<br/>• `enemy_hostile_scheme_success_chance_add = -10 / -20 / -30`<br/>• `monthly_lifestyle_xp_gain_mult = 0.10 / 0.20 / 0.30` | **Unseen Shroud**: Guarantees **100%** success on yearly Attunement discipline bonus XP rolls (`blood_mage_yearly_events.001` / `.004`). Successfully executing a Murder scheme (`murder_success_pre_filter_on_action`) reaps **1 Major Lifeforce** (`lifeforce_modifier_major`). |

## Inscribing Runes on Others (`bm_inscribe_rune_other_interaction`)

- **Initiation:** Available to both `lifestyle_blood_mage` and `lifestyle_blood_knight`.
- **Target Eligibility:** Adults who are courtiers, children, dynasty kin, spouses/consorts, sworn knights, Blood Golems, or liege.
- **Progression:** Follows exact same tiers, Piety costs, Lifeforce consumption, and caster devotion/XP gates as self-inscription.
- **XP Yield:** Grants `benediction` track XP (+4 / +5 / +10) to the caster instead of `ancient` XP.
- **Cooldown & Opinion:** Sets 5-year cooldown flag `bm_blood_rune_other_cooldown` on caster; adds `magic_opinion_positive` (+20) from recipient toward caster.

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
| Stave & base modifiers | `common/modifiers/bm_blood_runes_modifiers.txt` |
| Stave application & upgrade effects | `common/scripted_effects/bm_blood_runes_effects.txt` |
| Galdrastafir selector & flay events | `events/bm_blood_runes_events.txt` (`bm_blood_runes.001`, `.002`) |
| Self-cast rune events | `events/bm_cast_blood_magic_minor_events.txt`, `major_events.txt`, `superior_events.txt` |
| Inscribe rune on other interaction | `common/character_interactions/bm_inscribe_rune_other.txt` |
| Feingur bless dynasty interaction | `common/character_interactions/bm_feingur_bless_dynasty.txt` |
| Interaction icons | `gfx/interface/icons/character_interactions/bm_inscribe_rune_other_interaction.dds`, `bm_feingur_bless_dynasty_interaction.dds` |
| Yearly rune pulse & Capstone hooks | `events/bm_yearly_events.txt` (`.001`, `.003`, `.004`) |
| Travel POI hook (Nábrókarstafur) | `common/on_action/bm_travel_on_actions.txt` |
| Combat & duel Capstone hooks | `common/on_action/bm_combat_on_actions.txt`, `bm_duel_on_actions.txt` |
| Scheme murder Capstone hook | `common/on_action/bm_scheme_on_actions.txt` |
| Flay & battle gold script values | `common/script_values/bm_blood_rune_cost.txt`, `bm_blood_mage_story_values.txt` |
| Story custom localization | `common/customizable_localization/bm_blood_mage_story_custom_loc.txt` |
| Localization | `localization/english/bm_blood_runes_l_english.yml`, `bm_modifiers_l_english.yml`, `bm_blood_mage_story_l_english.yml` |
| Duchy capital buildings | `common/buildings/bm_duchy_buildings.txt` |
