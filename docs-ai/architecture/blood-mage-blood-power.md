# Blood Power

Living technical specification for the Blood Power subsystem.

## Executive Summary

- **What:** Secondary lifestyle trait `lifestyle_blood_power`. 5 progression tracks (`dynasty`, `mastery`, `presence`, `prosperity`, `shadows`), max 100 XP each.
- **Acquisition:** Automatically granted at base rank (0 XP) simultaneously when acquiring `lifestyle_blood_mage` or `lifestyle_blood_knight`, ensuring both traits sit adjacent in the character interface.
- **Advancement:** Cast Major Blood Magic Grimoire (`bm_cast_blood_magic_major_decision` -> `bm_cast_blood_magic_major.001` -> `bm_blood_power_event.001`).
  - Cost: 150 Piety + consumes `lifeforce_modifier_major`. Req: `piety_level >= 1`. Cooldown: none. Zero-cost backout allows returning to Grimoire freely.
  - XP Gain: +3 `enlightenment` XP (Blood Mage & Blood Knight) + 10 XP in chosen power track (via `add_blood_power_xp`).
  - Fallback: Once all 5 tracks reach 100 XP, unlocks `Versatility` option granting 10-year `temporary_buff_self` and rolls for permanent skill/prowess increases.

## Track Benefits Table

Each track spans 10 levels (10 to 100 XP, +10 XP per channel). Modifiers stack additively. Universal Vitality is omitted to prevent tooltip clutter since `lifestyle_blood_mage` and `lifestyle_blood_knight` already grant vitality:

| `dynasty` | Sanguine Eugenics & Kinship | `+5%` Pos. Inactive Inheritance, `+5%` Genetic Trait Strengthen Chance, `+3` Years of Fertility (`years_of_fertility = 3`) | `-50%` Inbreeding Chance, `+10%` Monthly Renown (`monthly_dynasty_prestige_mult = 0.10`) | **`+40%` Inactive Inheritance**, **`+40%` Trait Strengthen**, **`+24` Years of Fertility**, **Complete Inbreeding Immunity (`-100%`)**, **`+25%` Monthly Renown**, `no_prowess_loss_from_age = yes` |
| `mastery` | World-Walker & Schemes | `+5%` Lifestyle XP Mult (`monthly_lifestyle_xp_gain_mult = 0.05`), `+1` Max Language Schemes at 30, 60, 90 XP | `+1` Max Personal Schemes (`max_personal_schemes_add = 1`) | **`+40%` Lifestyle XP**, **`+3` Max Language Schemes**, **`+2` Max Personal Schemes**, **Ignore Negative Culture Opinion** (`ignore_negative_culture_opinion = yes`), `no_prowess_loss_from_age = yes` |
| `presence` | Mesmeric Allure & Sovereign Majesty | `+3` General Opinion (`general_opinion = 3`), `-5%` Stress Gain Mult (`stress_gain_mult = -0.05`) | `+25%` Fame Impact (`prestige_level_impact_mult = 0.25`) | **`+24` General Opinion**, **`-40%` Stress Gain**, **`+25%` Fame Impact**, **`-25%` Short Reign Duration**, **`+25%` Long Reign Bonus**, `no_prowess_loss_from_age = yes` |
| `prosperity` | War Chest & Logistics | `+5%` Monthly Income Mult (`monthly_income_mult = 0.05`), `-4%` Men-at-Arms Maintenance (`men_at_arms_maintenance = -0.04`) | `+2` Domain Limit (`domain_limit = 2`), `+1` Men-at-Arms Regiment Size (`men_at_arms_cap = 1`) | **`+40%` Income Mult**, **`-32%` MaA Maintenance**, **`+4` Domain Limit**, **`+3` Men-at-Arms Regiment Size**, `no_prowess_loss_from_age = yes` |
| `shadows` | Occult Warding & Premonition | `+5` Hostile Scheme Success, `-5` Enemy Hostile Scheme Success | `-25%` Enemy Hostile Scheme Max Success Cap, `+1` Max Hostile Schemes (`max_hostile_schemes_add = 1`) | **`+40` Hostile Scheme Success**, **`-40` Enemy Hostile Scheme Success**, **`-50%` Enemy Hostile Scheme Max Cap**, **`+15%` Own Hostile Scheme Max Cap**, **`+2` Max Hostile Schemes**, `no_prowess_loss_from_age = yes` |
| *Versatility* | Capped Fallback | 10-year buff `temporary_buff_self` (`+2` all stats, `+4` Prowess) + rolls for perm stats (`+1` skill, `+2` Prowess) | N/A | Granted when all 5 tracks are at 100 XP |

## Key Mechanics

- **Advancement Ritual:** Housed inside the Cast Major Blood Magic Grimoire (`bm_cast_blood_magic_major.001` -> `bm_blood_power_event.001`). Displays active bonuses, milestones, and capstone breakdowns. Consumes 150 Piety + Major Lifeforce only when a discipline is chosen, granting `+3` `enlightenment` XP and `+10` track XP, with a zero-cost return to the Grimoire.
- **Roster:** Retinue automatically tracked in Blood Magic story panel via `bm_refresh_blood_magic_rosters_effect`.
