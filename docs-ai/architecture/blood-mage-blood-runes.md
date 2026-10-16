# Blood Runes, Galdrastafir and Blood Architecture

Living technical specification for body runes, Galdrastafir staves, and blood architecture in the Blood Mage mod.

## Executive Summary

- **What:** Single-slot, sequential body rune system (Minor -> Major -> Superior) carved into flesh, pairing a base tier tracker (`minor/major/superior_blood_rune_modifier`) with 1 of 10 Galdrastafir staves (`bm_rune_<stave>_minor/major/superior`). Grants passive yearly Lifeforce rolls (`blood_mage_yearly_events.003`), scaling flat modifiers across all 3 tiers, and a Superior Capstone Hook unlocked exclusively at the Superior tier.
- **Self-Inscription (Ancient XP):** Cast via `bm_cast_blood_magic_minor_decision` (`bm_cast_blood_magic_minor.001`), upgraded via `major.001` and `superior.001`. Awards strictly base `ancient` XP (+4 / +5 / +10). Blood Knights cap at Major self-casts; Blood Mages reach Superior.
- **Inscribe on Others (Benediction XP):** Character interaction `bm_inscribe_rune_other_interaction` available to both `lifestyle_blood_mage` and `lifestyle_blood_knight`. Carves or upgrades a stave on a valid target (courtier, family, child, spouse/consort, sworn knight, Blood Golem, liege) for identical Piety, Lifeforce, Devotion Rank, and Track XP gates as self-inscription, but awards `benediction` XP (+4 / +5 / +10) to the caster.
- **Flay Blood Rune (Swap Rite):** Agony rite (`bm_blood_runes.002`) burning `ancient` XP, Piety, and Lifeforce (plus inflicting wounds and casting exhaustion) to strip the active stave and re-inscribe a new one at the character's current tier.
- **University Buildings:** `bm_university_0` through `bm_university_3`. Duchy capital holdings built by rulers with `lifestyle_blood_mage`.

## Tier Progression, Costs & XP Table

| Rune Tier | Base Tracker | Caster Gates (Devotion & Track XP) | Cost (Self & Other) | Self-Cast XP | Cast on Other XP (`bm_inscribe_rune_other_interaction`) | Yearly Lifeforce Pulse (`blood_mage_yearly_events.003`) | Flay & Swap Cost (Self) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Minor** | `minor_blood_rune_modifier` | Rank 2 (`piety_level >= 2`), 25 XP | 0 Piety + 1 Minor Lifeforce | +4 ancient | +4 benediction | 20% Minor | 250 Piety, -5 ancient XP, 1 Minor LF, `wounded_1` |
| **Major** | `major_blood_rune_modifier` | Rank 3 (`piety_level >= 3`), 50 XP | 200 Piety + 1 Major Lifeforce | +5 ancient | +5 benediction | 20% Minor, 10% Major, 5% Both | 500 Piety, -10 ancient XP, 1 Major LF, `wounded_1`, Major Exhaustion (1 yr) |
| **Superior** | `superior_blood_rune_modifier` | Rank 4 (`piety_level >= 4`), 100 XP (Mage only) | 400 Piety + 1 Superior Lifeforce | +10 ancient | +10 benediction | 10% Minor, 20% Major, 10% Both | 1000 Piety, -15 ancient XP, 1 Superior LF, `wounded_2`, Superior Exhaustion (5 yrs) |

*Yearly rolls handled by hidden pulse `blood_mage_yearly_events.003` (triggers on rune modifiers, no trait restriction). Recipients of all classes receive passive Lifeforce generation.*

## Galdrastafir Catalog (Flat Modifiers & Superior Capstones)

| # | Stave (`bm_rune_<key>_*`) | Flat Modifiers (Minor / Major / Superior) | Superior Capstone Effect (Active on `bm_rune_<key>_superior` only) |
| --- | --- | --- | --- |
| 1 | **Vegvísir** (`vegvisir`) | • +15% / +25% / +40% Character Travel Speed<br/>• +10 / +20 / +30 Travel Safety<br/>• +5% / +10% / +15% Army Movement Speed | **Storm-Walker**: Halves `seek_power_decision` cooldown (730d -> 365d landed, 365d -> 180d wanderer) and eliminates negative hazard rolls (escape / witnessed) in `bm_seek_power_events.txt`. |
| 2 | **Hólastafur** (`holastafur`) | • -10% / -20% / -30% Embarkation Cost<br/>• -10% / -20% / -30% Provisions Use<br/>• +1 / +2 / +3 Stewardship | **Earth-Opener**: Visiting any Point of Interest (`on_travel_plan_movement` -> `bm_on_visited_point_of_interest`) awards a flat #P +10 Gold#! once per POI province. |
| 3 | **Feingur** (`feingur`) | • +10% / +20% / +30% Fertility<br/>• +10% / +20% / +30% Good Genetic Chance<br/>• +5 / +10 / +15 Years of Fertility<br/>• +10 / +20 / +30 Attraction Opinion<br/>• +0.2 / +0.4 / +0.6 Health | **Awakened Seed**: On `on_birth_child`, boosts single-parent `lifestyle_blood_mage` inheritance chance from 25% to 50% and doubles childbirth bloodline XP (+4 -> +8 XP). |
| 4 | **Ægishjálmur** (`aegishjalmur`) | • +3 / +6 / +9 Prowess<br/>• +10 / +20 / +30 Natural Dread<br/>• +10% / +20% / +30% Knight Effectiveness | **Terror of the Slain**: Unlocks battlefield and single-combat Lifeforce harvesting (`bm_on_character_death_duel` and `bm_on_combat_end_winner`) even if bearer is a pure Blood Mage. |
| 5 | **Gapaldur & Ginfaxi** (`gapaldur`) | • +1 / +2 / +4 Max Knights<br/>• +2 / +4 / +6 Advantage<br/>• +0.25 / +0.50 / +0.75 Negate Health Penalty | **Unbroken Heel**: Adds +15 victory weight in all mod skill duels (`bm_trait_drain.001`, `bm_geyser_duel.0001`, `golem_duel_effect`) and wards fatal blows by consuming 1 Minor Lifeforce to convert fatal `wounded_3` / duel defeat into `wounded_2`. |
| 6 | **Nábrókarstafur** (`nabrokarstafur`) | • +5% / +15% / +25% Domain Tax<br/>• -5% / -10% / -15% Men-at-Arms Maintenance<br/>• -5 / -10 / -15 General Opinion | **Flayed Tithe**: Executing any prisoner via single `lifedrain_prisoner_event_interaction` or `mass_lifedrain_prisoners_decision` yields #P +25 Gold#! per victim. |
| 7 | **Hulinhjálmur & Lásabrjótur** (`hulinhjalmur`) | • +15 / +25 / +40 Hostile Scheme Success<br/>• +15 / +30 / +50 Scheme Secrecy<br/>• -15% / -30% / -50% Enemy Scheme Success | **Unseen Siphon**: Eliminates discovery and opinion penalties on failed `bm_curse_blood_interaction` and `lifedrain_courtier_event_interaction`, and slashes `trait_drain_prisoner_event_interaction` cooldown from 60 days to 15 days. |
| 8 | **Brýnslustafur** (`brynslustafur`) | • +10% / +20% / +35% Lifestyle XP Gain<br/>• -15 / -30 / -50 Language Phase Duration | **Honed Mind**: In `blood_mage_yearly_events.001` and `.004`, raises yearly Attunement discipline bonus XP proc chance from 50% to a guaranteed #P 100%#! (+1 XP every year). |
| 9 | **Draumstafir** (`draumstafir`) | • -20% / -35% / -50% Stress Gain<br/>• +20% / +35% / +50% Stress Loss<br/>• +0.3 / +0.6 / +1.0 Monthly Piety<br/>• +5% / +10% / +15% Piety Level Impact | **Lucid Pulse**: Whenever `blood_mage_yearly_events.003` procs a passive Lifeforce harvest, the bearer also loses #P -25 Stress#!. |
| 10 | **Drepsóttarstafur** (`drepsottarstafur`) | • +10 / +20 / +35 Epidemic Resistance<br/>• +0.25 / +0.50 / +1.0 Health | **Plague-Ward**: Halves the Piety cost (-50%) of all `bm_heal_ailment` rites (`cure_illness_cost_*`). |

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
| Interaction icon | `gfx/interface/icons/character_interactions/bm_inscribe_rune_other_interaction.dds` |
| Yearly rune pulse & Capstone hooks | `events/bm_yearly_events.txt` (`.001`, `.003`, `.004`) |
| Travel POI hook (Hólastafur) | `common/on_action/bm_travel_on_actions.txt` |
| Combat & duel Capstone hooks | `common/on_action/bm_combat_on_actions.txt`, `bm_duel_on_actions.txt`, `bm_golem_duel_effect.txt`, `bm_geyser_duel_events.txt` |
| Flay & heal cost script values | `common/script_values/bm_blood_rune_cost.txt`, `bm_cure_illness_values.txt` |
| Story custom localization | `common/customizable_localization/bm_blood_mage_story_custom_loc.txt` |
| Localization | `localization/english/bm_blood_runes_l_english.yml`, `bm_modifiers_l_english.yml`, `bm_blood_mage_story_l_english.yml` |
| Duchy capital buildings | `common/buildings/bm_duchy_buildings.txt` |
