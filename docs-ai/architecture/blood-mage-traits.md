# Blood Mage Traits

Living technical specification for the Blood Mage, Blood Knight, and Blood Empowerment lifestyle traits subsystem.

## Executive Summary

- **How to get it:** Acquired through `bm_become_blood_mage_effect` (or `bm_become_blood_knight_effect`) via self-initiation against Egill Skallagrímsson in Reykjavik or Tsushima (`bm_geyser_duel.0001`), mentoring from a friend/lover/liege (`ask_for_blood_magic_interaction`), initiation by an existing Blood Mage (`grant_blood_magic_interaction`) or Blood Knight (`make_blood_knight_interaction`), siphoning an imprisoned mage (`bm_get_blood_magic_from_prisoner_interaction`), witch conversion (`convert_to_blood_magic_from_witch`), or hereditary birth (`25%` single parent, `100%` both parents, `0.20%` spontaneous birth).
- **What it does:** Marks the character as an occult **Blood Mage** (`lifestyle_blood_mage`) or martial **Blood Knight** (`lifestyle_blood_knight`), granting base `+10` Same Trait Opinion (`same_opinion = 10`), unlocking the Blood Magic Situation panel (`bm_blood_mage_story`), enabling Minor/Major/Superior Lifeforce spellcasting, and progressing across 5 lifestyle tracks (max 100 XP each).
- **How to level it up:** Spending Lifeforce on spells, interactions, or combat hooks awards XP in the corresponding track (`add_xp_bm_dynamic`, `add_shared_bm_bk_xp`, `add_blood_knight_xp`, `add_blood_empowerment_xp`). Passive yearly growth comes from the yearly pulse (`ancient`, plus `enlightenment` for Knights), active house blood modifiers (`bloodline`), and yearly attunements (`50%` chance of `+1` XP, raised to `100%` by Superior **Brýnslustafur**).

### Master Cumulative Track Benefits (10 XP / 50 XP / 100 XP)

Each track has 10 progression levels (10 to 100 XP). In CK3, each unlocked tier applies additively.
*Vitality Baseline:* In `lifestyle_blood_mage` and `lifestyle_blood_knight`, tiers 10–40 and 60–90 grant the standard **Vitality Step** (`+0.1` Health, `+2` Life Expectancy, `+1` Year Fertility, `+1` Epidemic Resistance). Tiers 50 and 100 skip the vitality step in favor of Devotion-scaling milestones and capstones (**4× Vitality** at 50 XP = `+0.4` Health, `+8` Life Exp, `+4` Fertility Yrs, `+4` Epidemic Res; **8× Vitality** at 100 XP = `+0.8` Health, `+16` Life Exp, `+8` Fertility Yrs, `+8` Epidemic Res).

#### 1. Blood Mage (`lifestyle_blood_mage`)
Base: `same_opinion = 10`, `ruler_designer_cost = 100`.

| Track | 10 XP (1st Step) | 50 XP (Cumulative Milestone) | 100 XP (Cumulative Capstone) |
| --- | --- | --- | --- |
| `ancient` *(shared)* | Vitality + `+0.1` Monthly Dynasty Prestige, `+5%` Lifestyle XP Gain Mult | 4× Vitality + `+0.5` Monthly Dynasty Prestige, `+25%` Lifestyle XP Gain Mult, `+0.25` Negate Health Penalty, `+1` Prowess per Piety level | 8× Vitality + `+1.0` Monthly Dynasty Prestige, `+50%` Lifestyle XP Gain Mult, `+0.50` Negate Health Penalty, `+1` Prowess per Piety level, `character_max_piety_level_add = 1`, `no_prowess_loss_from_age = yes` |
| `enlightenment` *(shared)* | Vitality + `+0.2` Monthly Piety, `+5%` Monthly Piety Gain Mult | 4× Vitality + `+1.0` Monthly Piety, `+25%` Monthly Piety Gain Mult, `+1` Learning per Piety level, `+1` Prowess per Piety level | 8× Vitality + `+2.0` Monthly Piety, `+50%` Monthly Piety Gain Mult, `+2` Learning per Piety level, `+1` Prowess per Piety level, `character_max_piety_level_add = 1`, `no_prowess_loss_from_age = yes` |
| `benediction` *(shared)* | Vitality + `+1.5` General Opinion, `+1` Vassal Opinion, `+0.2` Monthly Prestige, `+5%` Monthly Prestige Mult | 4× Vitality + `+7.5` General Opinion, `+5` Vassal Opinion, `+1.0` Monthly Prestige, `+25%` Monthly Prestige Mult, `+1` Diplomacy per Piety level, `+1` Prowess per Piety level | 8× Vitality + `+15` General Opinion, `+10` Vassal Opinion, `+2.0` Monthly Prestige, `+50%` Monthly Prestige Mult, `+2` Diplomacy per Piety level, `+1` Prowess per Piety level, `character_max_piety_level_add = 1`, `no_prowess_loss_from_age = yes` |
| `bloodline` *(Mage only)* | Vitality + `+0.2` Monthly Dynasty Prestige, `-2%` Build Gold Cost, `+2%` Domain Tax | 4× Vitality + `+1.0` Monthly Dynasty Prestige, `+1` Domain Limit, `+10%` Gold Gain Mult, `+1` Stewardship per Piety level, `+1` Prowess per Piety level, `+5` Vassal Limit, `-8%` Build Gold Cost, `+8%` Domain Tax, `+10%` Development Growth, `-5%` Holding Build Speed | 8× Vitality + `+2.0` Monthly Dynasty Prestige, `+3` Domain Limit, `+30%` Gold Gain Mult, `+2` Stewardship per Piety level, `+1` Prowess per Piety level, `+15` Vassal Limit, `-20%` Build Gold Cost, `+20%` Domain Tax, `+25%` Development Growth, `-15%` Holding Build Speed, `no_prowess_loss_from_age = yes` |
| `hematurgy` *(Mage only)* | Vitality + `+3` Hostile Scheme Success, `+3` Scheme Secrecy, `+2` Dread Baseline, `-2%` Tyranny Gain Mult | 4× Vitality + `+15` Hostile Scheme Success, `+15` Scheme Secrecy, `+1` Max Hostile Schemes, `-10` Days Scheme Phase, `+10` Dread Baseline, `+15%` Dread Gain Mult, `-10%` Tyranny Gain Mult, `+1` Intrigue per Piety level, `+1` Prowess per Piety level | 8× Vitality + `+30` Hostile Scheme Success, `+30` Scheme Secrecy, `+2` Max Hostile Schemes, `-20` Days Scheme Phase, `+20` Dread Baseline, `+25%` Dread Gain Mult, `-20%` Tyranny Gain Mult, `+2` Intrigue per Piety level, `+1` Prowess per Piety level, `no_prowess_loss_from_age = yes` |

#### 2. Blood Knight (`lifestyle_blood_knight`)
Base: `same_opinion = 10`, `ruler_designer_cost = 50`. Vitality baseline applied at tiers 10–40 and 60–90; skipped at 50 & 100 XP milestones.

| Track | 10 XP (1st Step) | 50 XP (Cumulative Milestone) | 100 XP (Cumulative Capstone) |
| --- | --- | --- | --- |
| `vanguard` *(Knight only)* | Vitality + `+1` Advantage, `+2%` Army Speed (`+1` Martial at even tiers 20/40/60/80/100) | 4× Vitality + `+5` Advantage, `+10%` Army Speed, `+2` Martial, `+1` Martial per Piety Level | 8× Vitality + `+10` Advantage, `+20%` Army Speed, `+5` Martial, `+2` Martial per Piety Level, `no_prowess_loss_from_age = yes` |
| `slaughter` *(Knight only)* | Vitality + `+2` Prowess, `+1` Knight Limit, `+10%` Knight Effectiveness | 4× Vitality + `+10` Prowess, `+5` Knight Limit, `+50%` Knight Effectiveness, `+1` Prowess per Piety Level | 8× Vitality + `+20` Prowess, `+10` Knight Limit, `+100%` Knight Effectiveness, `+2` Prowess per Piety Level, `no_prowess_loss_from_age = yes` |
| `ancient` *(shared)* | Identical to Blood Mage `ancient` | Identical to Blood Mage `ancient` | Identical to Blood Mage `ancient` (`character_max_piety_level_add = 1`, `no_prowess_loss_from_age = yes`) |
| `enlightenment` *(shared)* | Identical to Blood Mage `enlightenment` | Identical to Blood Mage `enlightenment` | Identical to Blood Mage `enlightenment` (`character_max_piety_level_add = 1`, `no_prowess_loss_from_age = yes`) |
| `benediction` *(shared)* | Identical to Blood Mage `benediction` | Identical to Blood Mage `benediction` | Identical to Blood Mage `benediction` (`character_max_piety_level_add = 1`, `no_prowess_loss_from_age = yes`) |

#### 3. Blood Empowerment (`lifestyle_blood_empowerment`)
Base: None. Vitality baseline applied across tiers 10–90 (**5× Vitality** at 50 XP, **9× Vitality** at 100 XP); skipped at 100 XP in favor of `+5%` Devotion Impact (`piety_level_impact_mult = 0.05`) and `no_prowess_loss_from_age = yes`.

| Track | 10 XP (1st Step) | 50 XP (Cumulative Milestone) | 100 XP (Cumulative Capstone) |
| --- | --- | --- | --- |
| `dynasty` | Vitality + `+4%` Fertility, `+2.5%` Congenital Chance, `+2.5%` Inactive Inheritance | 5× Vitality + `+20%` Fertility, `+12.5%` Congenital Chance, `+12.5%` Inactive Inheritance | 9× Vitality + `+40%` Fertility, `+25%` Congenital Chance, `+25%` Inactive Inheritance, `+5%` Devotion Impact (`piety_level_impact_mult = 0.05`), `no_prowess_loss_from_age = yes` |
| `mastery` | Vitality + `+4%` Lifestyle XP Mult, `-10`d Language Phase, `+3%` Personal Scheme Success | 5× Vitality + `+20%` Lifestyle XP Mult, `-50`d Language Phase, `+15%` Personal Scheme Success, `+1` Language Slot | 9× Vitality + `+40%` Lifestyle XP Mult, `-100`d Language Phase, `+30%` Personal Scheme Success, `+4` Language Slots, `+5%` Devotion Impact (`piety_level_impact_mult = 0.05`), `no_prowess_loss_from_age = yes` |
| `presence` | Vitality + `+1.5` General Opinion, `+1.0` Vassal Opinion, `+5%` Stress Loss Mult | 5× Vitality + `+7.5` General Opinion, `+5.0` Vassal Opinion, `+25%` Stress Loss Mult | 9× Vitality + `+15.0` General Opinion, `+10.0` Vassal Opinion, `+50%` Stress Loss Mult, `+5%` Devotion Impact (`piety_level_impact_mult = 0.05`), `no_prowess_loss_from_age = yes` |
| `prosperity` | Vitality + `+0.1` Income, `+2.5%` Income Mult | 5× Vitality + `+0.5` Income, `+12.5%` Income Mult | 9× Vitality + `+1.0` Income, `+25%` Income Mult, `+5%` Devotion Impact (`piety_level_impact_mult = 0.05`), `no_prowess_loss_from_age = yes` |
| `shadows` | Vitality + `+5` Scheme Secrecy, `-3%` Enemy Scheme Success Chance | 5× Vitality + `+25` Scheme Secrecy, `-15%` Enemy Scheme Success Chance | 9× Vitality + `+50` Scheme Secrecy, `-30%` Enemy Scheme Success Chance, `+5%` Devotion Impact (`piety_level_impact_mult = 0.05`), `no_prowess_loss_from_age = yes` |

## Core Concepts

### Mutual Exclusivity & Devotion Apex
- **Permanent Class Choice:** `lifestyle_blood_mage` and `lifestyle_blood_knight` are mutually exclusive lifestyle paths (`bm_become_blood_mage_effect` and `bm_become_blood_knight_effect` block acquisition if the character already holds the counterpart trait; only historical Egill Skallagrímsson holds both).
- **Inheritable Non-Genetic Traits:** Both `lifestyle_blood_mage` and `lifestyle_blood_knight` use `inheritable = yes` (without `genetic = yes`) for deterministic `25%` single-parent (`50%` with Superior **Feingur**) and `100%` dual-parent inheritance, plus `0.20%` spontaneous birth/creation rolls audited by campaign prevalence rules.
- **Devotion Apex (Levels 6–8):** Capstones at 100 XP in the 3 shared tracks (`ancient`, `enlightenment`, `benediction`) each grant `character_max_piety_level_add = 1` on both Blood Mage and Blood Knight, unlocking Devotion Levels 6–8 (*Divine*, *Demigod*, *Godlike*).
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
