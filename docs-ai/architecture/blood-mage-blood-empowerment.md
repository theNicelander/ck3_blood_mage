# Blood Empowerment

Living technical specification for the Blood Empowerment subsystem.

## Executive Summary

- **What:** Secondary lifestyle trait `lifestyle_blood_empowerment`. 5 progression tracks (`dynasty`, `mastery`, `presence`, `prosperity`, `shadows`), max 100 XP each.
- **Acquisition:** Automatically granted at base rank (0 XP) simultaneously when acquiring `lifestyle_blood_mage` or `lifestyle_blood_knight`, ensuring both traits sit adjacent in the character interface.
- **Advancement:** Dedicated inline option-list decision `bm_channel_blood_empowerment_decision` in the Blood Magic Situation panel (`bm_blood_mage_story`) and Decisions tab.
  - Cost: 150 Piety + consumes `lifeforce_modifier_major`. Req: `piety_level >= 1`. Cooldown: none.
  - XP Gain: +3 `enlightenment` XP (Blood Mage & Blood Knight) + 10 XP in chosen empowerment track (via `add_blood_empowerment_xp`).
  - Fallback: Once all 5 tracks reach 100 XP, unlocks `Versatility` option granting 10-year `temporary_buff_self` and rolls for permanent skill/prowess increases.

## Universal Baseline Modifiers

Levels 10 to 40 and 60 to 90 across all 5 tracks (8 steps total) incorporate the universal baseline defined via Clausewitz script preprocessor variables (`@` syntax) in `common/traits/bm_blood_empowerment_trait.txt`, matching `lifestyle_blood_mage` and `lifestyle_blood_knight`:
- `@bm_common_health = 0.1` (+0.8 Health at 100 XP per track / +4.0 across all 5 tracks)
- `@bm_common_life_expectancy = 2.5` (+20 years Life Expectancy at 100 XP per track / +100 years across all 5 tracks)
- `@bm_common_years_of_fertility = 1.25` (+10 years Fertility at 100 XP per track / +50 years across all 5 tracks)
- `@bm_common_epidemic_resistance = 1` (+8 Epidemic Resistance at 100 XP per track / +40 across all 5 tracks)

At 50 XP and 100 XP, the vitality baseline is skipped in favor of distinct thematic milestones and capstones. Every track capstone at 100 XP grants `no_prowess_loss_from_age = yes`.

## Track Benefits Table

Each track spans 10 levels (10 to 100 XP, +10 XP per channel). Modifiers stack additively:

| Track | Specialization | Step Benefits (Tiers 10–40, 60–90) | 50 XP Milestone | 100 XP Capstone (Cumulative incl. Vitality) |
| --- | --- | --- | --- | --- |
| `dynasty` | Sanguine Eugenics & Kinship | Baseline + `+5%` Fertility, `+3%`/`+3.5%` Pos. Congenital Chance, `+3%`/`+3.5%` Inactive Inheritance, `+2.5%` Strengthen Congenital Traits, `+2.5` Close Relative Opinion, `+1.25` Dynasty Opinion | `-50%` Inbreeding Chance (`inbreeding_chance = -0.5`), `+25%` Negate Fertility Penalty, `+5%` Monthly Renown (`monthly_dynasty_prestige_mult = 0.05`) | 8× Vitality + `+40%` Fertility, `+25%` Pos. Congenital, `+25%` Inactive Inheritance, `+20%` Strengthen Congenital, `+20` Close Relative Opinion, `+10` Dynasty Opinion, **`-100%` Inbreeding Chance (Immunity)**, **`+50%` Negate Fertility Penalty**, **`+15%` Monthly Renown**, `no_prowess_loss_from_age = yes` |
| `mastery` | World-Walker, Polyglot & Schemes | Baseline + `+3%` Lifestyle XP Mult, `+2.5%` Travel Speed Mult, `+2.5` Travel Safety, `+4` Personal Scheme Success, `-3`d Personal Scheme Phase Duration, `+1` Language Slot (tiers 20, 40, 60, 80) | **`+1` Max Personal Schemes** (`max_personal_schemes_add = 1`), `+1` Learning per Fame level, `+15%` Cultural Acceptance Gain | 8× Vitality + `+24%` Lifestyle XP, `+20%` Travel Speed, `+20` Travel Safety, `+32` Personal Scheme Success, `-24`d Personal Scheme Phase, `+4` Language Slots, **`+2` Max Personal Schemes**, **`+2` Learning per Fame level**, `+15%` Cultural Acceptance, **Ignore Negative Culture Opinion** (`ignore_negative_culture_opinion = yes`), `no_prowess_loss_from_age = yes` |
| `presence` | Mesmeric Allure & Living Legend | Baseline + `+3.75` Attraction Opinion, `+2.5` Courtier & Guest Opinion, `+5%` Stress Loss Mult, `-3%` Stress Gain Mult, `-5%` Short Reign Duration, `+5%` Long Reign Bonus | `+1` Diplomacy & `+1` Martial per Fame level, `+15%` Fame Impact (`prestige_level_impact_mult = 0.15`) | 8× Vitality + `+30` Attraction Opinion, `+20` Courtier/Guest Opinion, `+40%` Stress Loss, `-24%` Stress Gain, `-40%` Short Reign, `+40%` Long Reign Bonus, `+15%` Fame Impact, **`+1.5` Diplomacy & `+1.5` Martial per Fame level**, **`+1` Max Fame Level** (`character_max_prestige_level_add = 1`), **Ignore Different Faith Opinion** (`ignore_different_faith_opinion = yes`), `no_prowess_loss_from_age = yes` |
| `prosperity` | War Chest & Logistics | Baseline + `+0.20` Monthly Income, `+3%` Monthly Income Mult, `-2.5%` MaA Maintenance, `-2.5%` MaA Recruitment Cost, `-2.5%` Camp/Domicile Build Cost | **`+1` MaA Regiment Size** (`men_at_arms_cap = 1`), `+1` Stewardship per Fame level, `+0.25` Gold/mo per Devotion level | 8× Vitality + `+1.60` Monthly Gold, `+24%` Income Mult, `-20%` MaA Maintenance, `-20%` MaA Recruitment Cost, `-20%` Domicile Build Cost, `+0.25` Gold/mo per Devotion level, **`+1.5` Stewardship per Fame level**, **`+2` MaA Regiment Size**, **`+1` MaA Regiment Slot** (`men_at_arms_limit = 1`), **`+1` Domain Limit**, `no_prowess_loss_from_age = yes` |
| `shadows` | Occult Warding & Premonition | Baseline + `-4` Enemy Hostile Scheme Success, `+5`d Enemy Hostile Scheme Phase Duration, `+5` Owned Scheme Secrecy, `+0.05` Negate Health Penalty | **`-15%` Enemy Hostile Scheme Max Success Cap** (`enemy_hostile_scheme_success_chance_max_add = -15`), `+1` Intrigue & `+1` Prowess per Fame level | 8× Vitality + `-32` Enemy Scheme Success, `+40`d Enemy Scheme Phase Duration, `+40` Scheme Secrecy, `+0.40` Negate Health Penalty, **`-30%` Enemy Hostile Scheme Max Success Cap**, **`+1` Max Hostile Schemes** (`max_hostile_schemes_add = 1`), **`+1.5` Intrigue & `+1.5` Prowess per Fame level**, `no_prowess_loss_from_age = yes` |
| *Versatility* | Capped Fallback | 10-year buff `temporary_buff_self` (`+2` all stats, `+4` Prowess) + rolls for perm stats (`+1` skill, `+2` Prowess) | N/A | Granted when all 5 tracks are at 100 XP |

## Key Mechanics

- **Advancement Decision:** Handled by `bm_channel_blood_empowerment_decision` using CK3 1.20's `decision_view_widget_option_list_generic`. Displays each track's dedicated `.dds` icon and milestone breakdown. Consumes 150 Piety + Major Lifeforce, granting `+3` `enlightenment` XP and `+10` track XP.
- **Roster:** Retinue automatically tracked in Blood Magic story panel via `bm_refresh_blood_magic_rosters_effect`.
