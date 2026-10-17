# Blood Mage Traits

Living technical specification for the Blood Mage, Blood Knight, and Blood Empowerment lifestyle traits subsystem.

## Executive Summary

- **How to get it:** Acquired through `bm_become_blood_mage_effect` (or `bm_become_blood_knight_effect`) via self-initiation against Egill Skallagrímsson in Reykjavik or Tsushima (`bm_geyser_duel.0001`), mentoring from a friend/lover/liege (`ask_for_blood_magic_interaction`), initiation by an existing Blood Mage (`grant_blood_magic_interaction`) or Blood Knight (`make_blood_knight_interaction`), siphoning an imprisoned mage (`bm_get_blood_magic_from_prisoner_interaction`), witch conversion (`convert_to_blood_magic_from_witch`), or hereditary birth (`25%` single parent, `100%` both parents, `0.20%` spontaneous birth).
- **What it does:** Marks the character as an occult **Blood Mage** (`lifestyle_blood_mage`) or martial **Blood Knight** (`lifestyle_blood_knight`), granting base `+10` Same Trait Opinion (`same_opinion = 10`), unlocking the Blood Magic Situation panel (`bm_blood_mage_story`), enabling Minor/Major/Superior Lifeforce spellcasting, and progressing across 5 lifestyle tracks (max 100 XP each).
- **How to level it up:** Spending Lifeforce on spells, interactions, or combat hooks awards XP in the corresponding track (`add_xp_bm_dynamic`, `add_shared_bm_bk_xp`, `add_blood_knight_xp`, `add_blood_empowerment_xp`). Passive yearly growth comes from the yearly pulse (`ancient`, plus `enlightenment` for Knights), active house blood modifiers (`bloodline`), and yearly attunements (guaranteed `+1` XP, doubled to `+2` XP by Superior **Hulinhjálmur**).

### Master Cumulative Track Benefits (10 XP / 50 XP / 100 XP)

Each track has 10 progression levels (10 to 100 XP). In CK3, each unlocked tier applies additively.
*Vitality Baseline & Milestones:* In `lifestyle_blood_mage` and `lifestyle_blood_knight`, tiers 10–40 and 60–90 grant the standard **Vitality Step** (`+0.1` Health, `+2.5` Life Expectancy, `+1.25` Year Fertility, `+1` Epidemic Resistance; total 8 steps = `+0.8` Health, `+20` Life Exp, `+10` Fertility Yrs, `+8` Epidemic Res per track; across 5 tracks: `+4.0` Health, `+100` Life Exp, `+50` Fertility Yrs, `+40` Epidemic Res) alongside track-specific incremental benefits. (For `lifestyle_blood_empowerment`, vitality step remains `+2` Life Exp / `+1` Fertility Yr).
Tiers 50 and 100 contain **no incremental per-track bonuses**, functioning purely as milestones and capstones: Tier 50 focuses on Devotion-scaling powers (`<stat>_per_piety_level = 1`) or milestone abilities; Tier 100 provides the Devotion Apex (`character_max_piety_level_add = 1` for shared tracks) and universal age-lock (`no_prowess_loss_from_age = yes`).

#### 1. Blood Mage (`lifestyle_blood_mage`)
Base: `same_opinion = 10`, `ruler_designer_cost = 100`.

| Track | 10 XP (1st Step) | 50 XP (Cumulative Milestone) | 100 XP (Cumulative Capstone) |
| --- | --- | --- | --- |
| `ancient` *(shared)* | Vitality + `+0.10` Monthly Dynasty Prestige, `+4%` Lifestyle XP Gain Mult | 4× Vitality + `+0.4` Monthly Dynasty Prestige, `+16%` Lifestyle XP Gain Mult, `+17.5%` Devotion Impact (`piety_level_impact_mult = 0.175`) | 8× Vitality + `+0.8` Monthly Dynasty Prestige, `+32%` Lifestyle XP Gain Mult, `+17.5%` Devotion Impact, `character_max_piety_level_add = 1`, `no_prowess_loss_from_age = yes` |
| `enlightenment` *(shared)* | Vitality + `+0.175` Monthly Piety, `+4%` Monthly Piety Gain Mult | 4× Vitality + `+0.7` Monthly Piety, `+16%` Monthly Piety Gain Mult, `+1` Learning per Piety level | 8× Vitality + `+1.4` Monthly Piety, `+32%` Monthly Piety Gain Mult, `+1.5` Learning per Piety level, `character_max_piety_level_add = 1`, `no_prowess_loss_from_age = yes` |
| `benediction` *(shared)* | Vitality + `+1.5` General Opinion, `+1` Vassal Opinion, `+0.175` Monthly Prestige, `+4%` Monthly Prestige Mult | 4× Vitality + `+6` General Opinion, `+4` Vassal Opinion, `+0.7` Monthly Prestige, `+16%` Monthly Prestige Mult, `+1` Diplomacy per Piety level | 8× Vitality + `+12` General Opinion, `+8` Vassal Opinion, `+1.4` Monthly Prestige, `+32%` Monthly Prestige Mult, `+1.5` Diplomacy per Piety level, `character_max_piety_level_add = 1`, `no_prowess_loss_from_age = yes` |
| `bloodline` *(Mage only)* | Vitality + `-2.5%` Build Gold Cost, `+2.5%` Domain Tax | 4× Vitality + `+1` Domain Limit, `+10%` Gold Gain Mult, `+1` Stewardship per Piety level, `+5` Vassal Limit, `+10%` Dynasty Renown Mult (`monthly_dynasty_prestige_mult = 0.10`), `+10` Dynasty Opinion, `-10%` Build Gold Cost, `+10%` Domain Tax, `+10%` Development Growth, `-5%` Holding Build Speed | 8× Vitality + `+3` Domain Limit, `+30%` Gold Gain Mult, `+1.5` Stewardship per Piety level, `+15` Vassal Limit, `+10%` Dynasty Renown Mult, `+10` Dynasty Opinion, `-20%` Build Gold Cost, `+20%` Domain Tax, `+25%` Development Growth, `-15%` Holding Build Speed, `no_prowess_loss_from_age = yes` |
| `hematurgy` *(Mage only)* | Vitality + `+4` Hostile Scheme Success, `+4` Scheme Secrecy, `+2` Dread Baseline, `-2.5%` Tyranny Gain Mult | 4× Vitality + `+16` Hostile Scheme Success, `+16` Scheme Secrecy, `+1` Max Hostile Schemes, `-6` Days Scheme Phase, `+10` Dread Baseline, `+5%` Dread Gain Mult, `-10%` Tyranny Gain Mult, `+1` Intrigue per Piety level | 8× Vitality + `+32` Hostile Scheme Success, `+32` Scheme Secrecy, `+2` Max Hostile Schemes, `-20` Days Scheme Phase, `+20` Dread Baseline, `+25%` Dread Gain Mult, `-20%` Tyranny Gain Mult, `+1.5` Intrigue per Piety level, `no_prowess_loss_from_age = yes` |

#### 2. Blood Knight (`lifestyle_blood_knight`)
Base: `same_opinion = 10`, `ruler_designer_cost = 50`. Vitality baseline applied at tiers 10–40 and 60–90; skipped at 50 & 100 XP milestones.

| Track | 10 XP (1st Step) | 50 XP (Cumulative Milestone) | 100 XP (Cumulative Capstone) |
| --- | --- | --- | --- |
| `vanguard` *(Knight only)* | Vitality + `+1.75%` Army Speed (`+1` Martial and `+1` Advantage at tiers 20, 40, 60, 80; `+1` Advantage at 30, 70, 90) | 4× Vitality + `+3` Advantage, `+7%` Army Speed, `+2` Martial, `+1` Martial per Piety Level, `+1` Prowess per Piety Level | 8× Vitality + `+7` Advantage, `+14%` Army Speed, `+4` Martial, `+1.5` Martial per Piety Level, `+1` Prowess per Piety Level, `no_prowess_loss_from_age = yes` |
| `slaughter` *(Knight only)* | Vitality + `+1.5` Prowess, `+8.75%` Knight Effectiveness (`+1` Knight Limit at tiers 20–40, 60–90) | 4× Vitality + `+7` Prowess, `+3` Knight Limit, `+35%` Knight Effectiveness, `+1` Prowess per Piety Level | 8× Vitality + `+14` Prowess, `+7` Knight Limit, `+70%` Knight Effectiveness, `+2` Prowess per Piety Level, `no_prowess_loss_from_age = yes` |
| `ancient` *(shared)* | Identical to Blood Mage `ancient` | Identical to Blood Mage `ancient` | Identical to Blood Mage `ancient` (`+50%` Devotion Impact, `no_prowess_loss_from_age = yes`) |
| `enlightenment` *(shared)* | Identical to Blood Mage `enlightenment` | Identical to Blood Mage `enlightenment` | Identical to Blood Mage `enlightenment` (`+2` Learning per Piety Level, `no_prowess_loss_from_age = yes`) |
| `benediction` *(shared)* | Identical to Blood Mage `benediction` | Identical to Blood Mage `benediction` | Identical to Blood Mage `benediction` (`+2` Diplomacy per Piety Level, `no_prowess_loss_from_age = yes`) |

#### 3. Blood Empowerment (`lifestyle_blood_empowerment`)
Base: None. Automatically acquired alongside `lifestyle_blood_mage` or `lifestyle_blood_knight` with 0 XP across all tracks so both traits appear adjacent in the UI character sheet. Vitality baseline applied across tiers 10–40 and 60–90 (8× Vitality total = `+0.8` Health, `+20` Life Exp, `+10` Fertility Yrs, `+8` Epidemic Res per track); 50 and 100 XP milestones provide distinct Fame-anchored and somatic/realm capabilities.

| Track | 10 XP (1st Step) | 50 XP (Cumulative Milestone) | 100 XP (Cumulative Capstone) |
| --- | --- | --- | --- |
| `dynasty` | Vitality + `+5%` Fertility, `+3%` Congenital Chance, `+3%` Inactive Inheritance, `+2.5%` Strengthen Congenital Traits, `+2.5` Close Rel. Op, `+1.25` Dyn. Op | 4× Vitality + `+20%` Fertility, `+12%` Congenital Chance, `+12%` Inactive Inheritance, `+10%` Strengthen Congenital, `+10` Close Rel. Op, `+5` Dyn. Op, **`-50%` Inbreeding Chance**, `+25%` Negate Fertility Penalty, `+5%` Renown Mult | 8× Vitality + `+40%` Fertility, `+25%` Congenital Chance, `+25%` Inactive Inheritance, `+20%` Strengthen Congenital, `+20` Close Rel. Op, `+10` Dyn. Op, **`-100%` Inbreeding Chance (Immunity)**, **`+50%` Negate Fertility Penalty**, **`+15%` Renown Mult**, `no_prowess_loss_from_age = yes` |
| `mastery` | Vitality + `+3%` Lifestyle XP Mult, `+2.5%` Travel Speed, `+2.5` Travel Safety, `+4` Personal Scheme Success, `-3`d Scheme Phase | 4× Vitality + `+12%` Lifestyle XP Mult, `+10%` Travel Speed, `+10` Travel Safety, `+16` Personal Scheme Success, `-12`d Scheme Phase, `+2` Language Slots, **`+1` Max Personal Schemes**, `+1` Learning per Fame Level, `+15%` Cultural Acceptance | 8× Vitality + `+24%` Lifestyle XP Mult, `+20%` Travel Speed, `+20` Travel Safety, `+32` Personal Scheme Success, `-24`d Scheme Phase, `+4` Language Slots, **`+2` Max Personal Schemes**, **`+2` Learning per Fame Level**, `+15%` Cultural Acceptance, **Ignore Negative Culture Opinion**, `no_prowess_loss_from_age = yes` |
| `presence` | Vitality + `+3.75` Attraction Opinion, `+2.5` Courtier/Guest Opinion, `+5%` Stress Loss, `-3%` Stress Gain, `-5%` Short Reign, `+5%` Long Reign Bonus | 4× Vitality + `+15` Attraction Opinion, `+10` Courtier/Guest Opinion, `+20%` Stress Loss, `-12%` Stress Gain, `-20%` Short Reign, `+20%` Long Reign Bonus, `+15%` Fame Impact, `+1` Diplomacy & `+1` Martial per Fame Level | 8× Vitality + `+30` Attraction Opinion, `+20` Courtier/Guest Opinion, `+40%` Stress Loss, `-24%` Stress Gain, `-40%` Short Reign, `+40%` Long Reign Bonus, `+15%` Fame Impact, **`+1.5` Diplomacy & `+1.5` Martial per Fame Level**, **`+1` Max Fame Level**, **Ignore Different Faith Opinion**, `no_prowess_loss_from_age = yes` |
| `prosperity` | Vitality + `+0.20` Monthly Gold, `+3%` Income Mult, `-2.5%` MaA Upkeep, `-2.5%` MaA Recruitment, `-2.5%` Domicile/Camp Build Cost | 4× Vitality + `+0.80` Monthly Gold, `+12%` Income Mult, `-10%` MaA Upkeep, `-10%` MaA Recruitment, `-10%` Domicile Build Cost, **`+1` MaA Regiment Size**, `+1` Stewardship per Fame Level, `+0.25` Gold/mo per Devotion Level | 8× Vitality + `+1.60` Monthly Gold, `+24%` Income Mult, `-20%` MaA Upkeep, `-20%` MaA Recruitment, `-20%` Domicile Build Cost, `+0.25` Gold/mo per Devotion Level, **`+1.5` Stewardship per Fame Level**, **`+2` MaA Regiment Size**, **`+1` MaA Regiment Slot**, **`+1` Domain Limit**, `no_prowess_loss_from_age = yes` |
| `shadows` | Vitality + `-4` Enemy Scheme Success, `+5`d Enemy Scheme Phase, `+5` Scheme Secrecy, `+0.05` Negate Health Penalty | 4× Vitality + `-16` Enemy Scheme Success, `+20`d Enemy Scheme Phase, `+20` Scheme Secrecy, `+0.20` Negate Health Penalty, **`-15%` Enemy Hostile Scheme Max Success Cap**, `+1` Intrigue & `+1` Prowess per Fame Level | 8× Vitality + `-32` Enemy Scheme Success, `+40`d Enemy Scheme Phase, `+40` Scheme Secrecy, `+0.40` Negate Health Penalty, **`-30%` Enemy Hostile Scheme Max Success Cap**, **`+1` Max Hostile Schemes**, **`+1.5` Intrigue & `+1.5` Prowess per Fame Level**, `no_prowess_loss_from_age = yes` |

## Core Concepts

### Mutual Exclusivity & Devotion Apex
- **Permanent Class Choice:** `lifestyle_blood_mage` and `lifestyle_blood_knight` are mutually exclusive lifestyle paths (`bm_become_blood_mage_effect` and `bm_become_blood_knight_effect` block acquisition if the character already holds the counterpart trait; only historical Egill Skallagrímsson holds both). Both paths automatically grant base `lifestyle_blood_empowerment` concurrently to position the icons adjacent in the character UI.
- **Inheritable Non-Genetic Traits:** Both `lifestyle_blood_mage` and `lifestyle_blood_knight` use `inheritable = yes` (without `genetic = yes`) for deterministic `25%` single-parent (`50%` with Superior **Feingur**) and `100%` dual-parent inheritance, plus `0.20%` spontaneous birth/creation rolls audited by campaign prevalence rules.
- **Devotion Apex Capstones:** Capstones at 100 XP in the 3 shared tracks (`ancient`, `enlightenment`, `benediction`) grant massive Devotion-scaling powers (`+50%` Devotion Impact on `ancient`, `+2` Learning per Devotion level on `enlightenment`, and `+2` Diplomacy per Devotion level on `benediction`) on both Blood Mage and Blood Knight.
- **Prowess Age Lock:** Every track capstone at 100 XP across all 12 tracks grants `no_prowess_loss_from_age = yes`.

### Acquisition Triggers
All routes invoke `bm_become_blood_mage_effect` or `bm_become_blood_knight_effect`:
- `bm_blood_cultist_become_blood_mage_decision`: Decision for Blóðtrú faithful; initiation duel against Egill Skallagrímsson (`bm_geyser_duel.0001`) in Reykjavik or Tsushima (`piety_level >= 2`, costs 1 Devotion level; Learning duel -> Blood Mage, Prowess duel -> Blood Knight).
- `bm_enhance_blood_ritual_decision`: Decision for non-faithful with qualifying occult traits/stats; identical Geyser duel in Reykjavik or Tsushima (`piety_level >= 2`, costs 1 Devotion level).
- `grant_blood_magic_interaction`: Blood Mage initiates courtier/kin (`100` Piety + Major Lifeforce OR `250` Piety + Minor Lifeforce; awards `+4`/`+5` or `+2` `bloodline` XP).
- `make_blood_knight_interaction`: Blood Knight initiates sworn knight/courtier (`100` Piety + Major Lifeforce OR `250` Piety + Minor Lifeforce; awards `+4` or `+2` `vanguard` XP).
- `ask_for_blood_magic_interaction`: Non-mage asks friend/lover/soulmate/liege Blood Mage to teach them (actor pays `250` Piety; teacher consumes 1 Superior Lifeforce).
- `bm_get_blood_magic_from_prisoner_interaction`: Non-mage forcibly steals `lifestyle_blood_mage` from an imprisoned Blood Mage (`100` Piety, skill duel).
- `convert_to_blood_magic_from_witch`: Player witch swaps witch trait/secret for `lifestyle_blood_mage`.
- **Birth Inheritance:** Rolled on newborn children via `on_birth_child` (`bm_blood_mage_prevalence_on_actions.txt`).

## Where the details live

| Piece | File |
| --- | --- |
| Blood Mage trait | `common/traits/bm_blood_mage_trait.txt` |
| Blood Knight trait | `common/traits/bm_blood_knight_trait.txt` |
| Blood Empowerment trait | `common/traits/bm_blood_empowerment_trait.txt` |
| XP helpers (`add_xp_bm_dynamic`, `add_shared_bm_bk_xp`, `add_blood_knight_xp`, `add_blood_empowerment_xp`) | `common/scripted_effects/bm_trait_track_xp_gain_effects.txt` |
| Lifecycle & acquisition effects | `common/scripted_effects/bm_blood_mage_lifecycle_effects.txt` |
| Total trait progression value | `common/script_values/bm_blood_mage_portrait_values.txt` |
| Geyser initiation duels | `events/bm_geyser_duel_events.txt` |
| Blood Empowerment event | `events/bm_blood_empowerment_event.txt` |
