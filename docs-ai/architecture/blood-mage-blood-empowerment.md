# Blood Empowerment

Living technical specification for the Blood Empowerment subsystem.

## Executive Summary

- **What:** Secondary lifestyle trait `lifestyle_blood_empowerment`. 5 progression tracks (`dynasty`, `mastery`, `presence`, `prosperity`, `shadows`), max 100 XP each.
- **Acquisition:** Automatically granted at base rank (0 XP) simultaneously when acquiring `lifestyle_blood_mage` or `lifestyle_blood_knight`, ensuring both traits sit adjacent in the character interface.
- **Advancement:** Cast Major Blood Magic Grimoire (`bm_cast_blood_magic_major_decision` -> `bm_cast_blood_magic_major.001` -> `bm_blood_empowerment_event.001`).
  - Cost: 150 Piety + consumes `lifeforce_modifier_major`. Req: `piety_level >= 1`. Cooldown: none. Zero-cost backout allows returning to Grimoire freely.
  - XP Gain: +3 `enlightenment` XP (Blood Mage & Blood Knight) + 10 XP in chosen empowerment track (via `add_blood_empowerment_xp`).
  - Fallback: Once all 5 tracks reach 100 XP, unlocks `Versatility` option granting 10-year `temporary_buff_self` and rolls for permanent skill/prowess increases.

## Track Benefits Table

Each track spans 10 levels (10 to 100 XP, +10 XP per channel). Modifiers stack additively. Universal Vitality is omitted to prevent tooltip clutter since `lifestyle_blood_mage` and `lifestyle_blood_knight` already grant vitality:

| Track | Specialization | Step Benefits (Tiers 10–40, 60–90) | 50 XP Milestone | 100 XP Capstone (Cumulative) |
| --- | --- | --- | --- | --- |
| `dynasty` | Sanguine Eugenics & Kinship | `+5%` Fertility, `+3%`/`+3.5%` Pos. Congenital Chance, `+3%`/`+3.5%` Inactive Inheritance | `+10` Years of Fertility (`years_of_fertility = 10`) | `+40%` Fertility, `+25` Years of Fertility, `+25%` Pos. Congenital, `+25%` Inactive Inheritance, `no_prowess_loss_from_age = yes` |
| `mastery` | World-Walker & Schemes | `+4%` Lifestyle XP Mult (`monthly_lifestyle_xp_gain_mult = 0.04`) | `+1` Max Personal Schemes (`max_personal_schemes_add = 1`) | `+32%` Lifestyle XP, `+2` Max Personal Schemes, `no_prowess_loss_from_age = yes` |
| `presence` | Mesmeric Allure & Living Legend | `+2.5` Courtier & Guest Opinion, `+5%` Stress Loss Mult, `-5%` Short Reign Duration, `+5%` Long Reign Bonus | `+15%` Fame Impact (`prestige_level_impact_mult = 0.15`) | `+20` Courtier/Guest Opinion, `+40%` Stress Loss, `-40%` Short Reign, `+40%` Long Reign Bonus, `+30%` Fame Impact, **Ignore Different Faith Opinion** (`ignore_different_faith_opinion = yes`), `no_prowess_loss_from_age = yes` |
| `prosperity` | War Chest & Logistics | `+4%` Monthly Income Mult (`+1` Domain Limit at 30, 60, 90 XP) | `+1` Stewardship per Fame level (`stewardship_per_prestige_level = 1`) | `+32%` Income Mult, **`+3` Domain Limit**, `+1.5` Stewardship per Fame level, `no_prowess_loss_from_age = yes` |
| `shadows` | Occult Warding & Premonition | `+4` Personal Scheme Success Chance | `-15%` Enemy Hostile Scheme Max Success Cap (`enemy_hostile_scheme_success_chance_max_add = -15`) | `+32` Personal Scheme Success, `-30%` Enemy Hostile Scheme Max Success Cap, `+1` Max Hostile Schemes (`max_hostile_schemes_add = 1`), `no_prowess_loss_from_age = yes` |
| *Versatility* | Capped Fallback | 10-year buff `temporary_buff_self` (`+2` all stats, `+4` Prowess) + rolls for perm stats (`+1` skill, `+2` Prowess) | N/A | Granted when all 5 tracks are at 100 XP |

## Key Mechanics

- **Advancement Ritual:** Housed inside the Cast Major Blood Magic Grimoire (`bm_cast_blood_magic_major.001` -> `bm_blood_empowerment_event.001`). Displays active bonuses, milestones, and capstone breakdowns. Consumes 150 Piety + Major Lifeforce only when a discipline is chosen, granting `+3` `enlightenment` XP and `+10` track XP, with a zero-cost return to the Grimoire.
- **Roster:** Retinue automatically tracked in Blood Magic story panel via `bm_refresh_blood_magic_rosters_effect`.
