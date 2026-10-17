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
Base: None. Automatically acquired alongside `lifestyle_blood_mage` or `lifestyle_blood_knight` with 0 XP across all tracks so both traits appear adjacent in the UI character sheet. Omits universal Vitality to keep tooltips concise (vitality is granted by primary traits). 50 and 100 XP milestones provide signature power capstones.

| Track | 10 XP (1st Step) | 50 XP (Cumulative Milestone) | 100 XP (Cumulative Capstone) |
| --- | --- | --- | --- |
| `dynasty` | `+5%` Fertility, `+3%` New Good Congenital Chance, `+3%` Inherit Good Congenital Chance | `+20%` Fertility, `+12%` New Good Congenital Chance, `+12%` Inherit Good Congenital Chance, **`+10` Years of Fertility** | `+40%` Fertility, `+25%` New Good Congenital Chance, `+25%` Inherit Good Congenital Chance, **`+25` Years of Fertility**, `no_prowess_loss_from_age = yes` |
| `mastery` | `+4%` Lifestyle XP Mult | `+16%` Lifestyle XP Mult, **`+1` Max Personal Schemes** | `+32%` Lifestyle XP Mult, **`+2` Max Personal Schemes**, `no_prowess_loss_from_age = yes` |
| `presence` | `+2.5` Courtier/Guest Opinion, `+5%` Stress Loss, `-5%` Short Reign, `+5%` Long Reign Bonus | `+10` Courtier/Guest Opinion, `+20%` Stress Loss, `-20%` Short Reign, `+20%` Long Reign Bonus, **`+15%` Fame Impact** | `+20` Courtier/Guest Opinion, `+40%` Stress Loss, `-40%` Short Reign, `+40%` Long Reign Bonus, **`+30%` Fame Impact**, **Ignore Different Faith Opinion**, `no_prowess_loss_from_age = yes` |
| `prosperity` | `+4%` Monthly Income Mult | `+16%` Monthly Income Mult, `+1` Domain Limit (at 30 XP), **`+1` Stewardship per Fame Level** | `+32%` Monthly Income Mult, **`+3` Domain Limit**, **`+1.5` Stewardship per Fame Level**, `no_prowess_loss_from_age = yes` |
| `shadows` | `+4` Personal Scheme Success | `+16` Personal Scheme Success, **`-15%` Enemy Hostile Scheme Max Success Cap** | `+32` Personal Scheme Success, **`-30%` Enemy Hostile Scheme Max Success Cap**, **`+1` Max Hostile Schemes**, `no_prowess_loss_from_age = yes` |

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
