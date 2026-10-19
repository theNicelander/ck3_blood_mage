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

| Track | Specialization | 10 XP Steps (10–40, 60–90 XP) | 20 XP Stepping Stones (20, 40, 60, 80 XP) | 50 XP Milestone | 100 XP Capstone (Cumulative) |
| --- | --- | --- | --- | --- | --- |
| `dynasty` | Sanguine Eugenics & Kinship | `+5%` Pos. Inactive Inheritance, `+5%` Trait Strengthen | `+5` Years of Fertility (`years_of_fertility = 5`) | `-50%` Inbreeding Chance, `+10%` Monthly Renown | **`+40%` Inactive Inheritance**, **`+40%` Trait Strengthen**, **`+20` Years of Fertility**, **Complete Inbreeding Immunity (`-100%`)**, **`+25%` Monthly Renown**, `no_prowess_loss_from_age = yes` |
| `mastery` | World-Walker & Schemes | `+5%` Lifestyle XP Mult | `+5` Personal Scheme Success, `-5` Days Personal Scheme Phase | `+1` Learning per Devotion, `+1` Max Personal Schemes | **`+40%` Lifestyle XP**, **`+20` Personal Scheme Success**, **`-20` Days Scheme Phase**, **`+2` Learning per Devotion** *(+2 Language Cap)*, **`+2` Max Personal Schemes**, **Ignore Negative Culture Opinion**, `no_prowess_loss_from_age = yes` |
| `presence` | Mesmeric Majesty | `+3` General Opinion, `-5%` Stress Gain | `+5%` Fame Impact (`prestige_level_impact_mult = 0.05`) | `+1` Diplomacy per Devotion, `-10%` Short Reign, `+10%` Long Reign | **`+24` General Opinion**, **`-40%` Stress Gain**, **`+20%` Fame Impact**, **`+2` Diplomacy per Devotion**, **`-20%` Short Reign Duration**, **`+20%` Long Reign Bonus**, `no_prowess_loss_from_age = yes` |
| `prosperity` | Wealth & Architecture | `+5%` Monthly Income, `-3%` Holding & Domicile Build Cost | `-5%` Men-at-Arms Maintenance | `+1` Stewardship per Devotion, `+1` Domain Limit | **`+40%` Income Mult**, **`-24%` Holding & Domicile Build Cost**, **`-20%` MaA Maintenance**, **`+2` Stewardship per Devotion**, **`+2` Domain Limit**, `no_prowess_loss_from_age = yes` |
| `shadows` | Occult Warding & Intrigue | `+5` Hostile Scheme Success, `-5` Enemy Hostile Scheme Success | `-5%` Enemy Hostile Scheme Max Success Cap | `+1` Intrigue per Devotion, `+1` Max Hostile Schemes | **`+40` Hostile Scheme Success**, **`-40` Enemy Hostile Scheme Success**, **`-20%` Enemy Hostile Scheme Max Cap**, **`+15%` Own Hostile Scheme Max Cap**, **`+2` Intrigue per Devotion**, **`+2` Max Hostile Schemes**, `no_prowess_loss_from_age = yes` |
| *Versatility* | Capped Fallback | N/A | N/A | 10-year buff `temporary_buff_self` (`+2` all stats, `+4` Prowess) + rolls for perm stats (`+1` skill, `+2` Prowess) | Granted when all 5 tracks are at 100 XP |

## Key Mechanics

- **Advancement Ritual:** Housed inside the Cast Major Blood Magic Grimoire (`bm_cast_blood_magic_major.001` -> `bm_blood_power_event.001`). Displays active bonuses, milestones, and capstone breakdowns. Consumes 150 Piety + Major Lifeforce only when a discipline is chosen, granting `+3` `enlightenment` XP and `+10` track XP, with a zero-cost return to the Grimoire.
- **Roster:** Retinue automatically tracked in Blood Magic story panel via `bm_refresh_blood_magic_rosters_effect`.
