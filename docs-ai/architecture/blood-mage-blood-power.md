# Blood Power

Living technical specification for the Blood Power subsystem.

## Executive Summary

- **What:** Secondary lifestyle trait `lifestyle_blood_power`. 6 progression tracks (`dynasty`, `warband`, `mastery`, `presence`, `prosperity`, `shadows`), max 100 XP each.
- **Universal Piety Baseline:** Every track grants **+0.1 Monthly Piety** per 10 XP tier (10–100 XP), totaling **+1.0 Monthly Piety** per maxed track (up to **+6.0 Monthly Piety** across all 6 maxed tracks).
- **1:1 Devotion Scaling:** Each track grants **+1 [Stat] per Devotion Level** at 50 XP and another **+1** at 100 XP (**+2 Total** per maxed track).
- **Flat Monthly Lifestyle XP:** Every 10 XP in a track yields **+5 flat monthly Lifestyle XP** (paid silently every quarter via `quarterly_playable_pulse` as **+15 XP per quarter**, up to **+50/mo = +150/quarter** at 100 XP).
  - `presence` -> **Diplomacy** Lifestyle XP
  - `warband` -> **Martial** Lifestyle XP
  - `prosperity` -> **Stewardship** Lifestyle XP
  - `shadows` -> **Intrigue** Lifestyle XP
  - `mastery` -> **Learning** Lifestyle XP
  - `dynasty` -> **Active Lifestyle Focus** (or random core lifestyle if unfocused)
- **Acquisition:** Automatically granted at base rank (0 XP) simultaneously when acquiring `lifestyle_blood_mage` or `lifestyle_blood_knight`, ensuring both traits sit adjacent in the character interface.
- **Advancement:** Cast Major Blood Magic Grimoire (`bm_cast_blood_magic_major_decision` -> `bm_cast_blood_magic_major.001` -> `bm_blood_power_event.001`).
  - Cost: 150 Piety + consumes `lifeforce_modifier_major`. Req: `piety_level >= 1`. Cooldown: none. Zero-cost backout allows returning to Grimoire freely.
  - XP Gain: +3 `enlightenment` XP (Blood Mage & Blood Knight) + 10 XP in chosen power track (via `add_blood_power_xp`).
  - Fallback: Once all 6 tracks reach 100 XP, unlocks `Versatility` option granting 10-year `temporary_buff_self` and rolls for permanent skill/prowess increases.

## Track Benefits Table

Each track spans 10 levels (10 to 100 XP, +10 XP per channel). Modifiers stack additively. Universal Vitality is omitted to prevent tooltip clutter since `lifestyle_blood_mage` and `lifestyle_blood_knight` already grant vitality:

| Track | Specialization | 10 XP Steps (10–40, 60–90 XP) | 20 XP Stepping Stones (20, 40, 60, 80 XP) | 50 XP Milestone | 100 XP Capstone (Cumulative) | Flat Monthly Lifestyle XP |
| --- | --- | --- | --- | --- | --- | --- |
| `dynasty` | Sanguine Eugenics & Kinship | `+0.1` Monthly Piety, `+5%` Pos. Genetic Chance, `+5%` Inactive Inheritance, `+5%` Trait Strengthen | `+5` Years of Fertility (`years_of_fertility = 5`) | `+1` Prowess per Devotion, `-50%` Inbreeding Chance | **`+1.0` Monthly Piety**, **`+2` Prowess per Devotion**, **`+40%` Pos. Genetic Chance**, **`+40%` Inactive Inheritance**, **`+40%` Trait Strengthen**, **`+20` Years of Fertility**, **Complete Inbreeding Immunity (`-100%`)**, `no_prowess_loss_from_age = yes` | `+5` to `+50` Active Lifestyle XP |
| `warband` | Warfare & Knights | `+0.1` Monthly Piety, `+2.5` Dread Baseline, `+5%` Knight Effectiveness, `+2%` MaA Damage | `+1` Advantage, `+3%` Army Movement Speed | `+1` Martial per Devotion, `+1` MaA Regiment Size | **`+1.0` Monthly Piety**, **`+2` Martial per Devotion**, **`+25` Dread Baseline**, **`+40%` Knight Effectiveness**, **`+16%` MaA Damage**, **`+12%` Army Movement Speed**, **`+4` Advantage**, **`+2` MaA Regiment Size**, `no_prowess_loss_from_age = yes` | `+5` to `+50` Martial Lifestyle XP |
| `mastery` | Scholarship & Schemes | `+0.1` Monthly Piety, `+5%` Lifestyle XP Mult, `-5%` Stress Gain | `+5%` Monthly Piety Mult, `-5` Days Learn Language Phase | `+1` Learning per Devotion, `+1` Language Slot | **`+1.0` Monthly Piety**, **`+2` Learning per Devotion**, **`+40%` Lifestyle XP**, **`+20%` Monthly Piety Mult**, **`-40%` Stress Gain**, **`-20` Days Learn Language Phase**, **`+2` Language Slots**, **Ignore Negative Culture Opinion**, `no_prowess_loss_from_age = yes` | `+5` to `+50` Learning Lifestyle XP |
| `presence` | Mesmeric Majesty | `+0.1` Monthly Piety, `+3` General Opinion | `+5%` Fame Impact, `+5` Personal Scheme Success, `-5` Days Personal Scheme Phase | `+1` Diplomacy per Devotion, `+1` Max Personal Schemes, `+10%` Monthly Renown | **`+1.0` Monthly Piety**, **`+2` Diplomacy per Devotion**, **`+24` General Opinion**, **`+20%` Fame Impact**, **`+20` Personal Scheme Success**, **`-20` Days Scheme Phase**, **`+2` Max Personal Schemes**, **`+25%` Monthly Renown**, `no_prowess_loss_from_age = yes` | `+5` to `+50` Diplomacy Lifestyle XP |
| `prosperity` | Wealth & Domain | `+0.1` Monthly Piety, `+5%` Monthly Income, `-3%` Holding & Domicile Build Cost | `-5%` Men-at-Arms Maintenance | `+1` Stewardship per Devotion, `+1` Domain Limit | **`+1.0` Monthly Piety**, **`+2` Stewardship per Devotion**, **`+40%` Monthly Income**, **`-24%` Holding & Domicile Build Cost**, **`-20%` MaA Maintenance**, **`+2` Domain Limit**, `no_prowess_loss_from_age = yes` | `+5` to `+50` Stewardship Lifestyle XP |
| `shadows` | Occult Warding & Intrigue | `+0.1` Monthly Piety, `+5` Hostile Scheme Success, `-5` Enemy Hostile Scheme Success | `-5%` Enemy Hostile Scheme Max Success Cap | `+1` Intrigue per Devotion, `+1` Max Hostile Schemes | **`+1.0` Monthly Piety**, **`+2` Intrigue per Devotion**, **`+40` Hostile Scheme Success**, **`-40` Enemy Hostile Scheme Success**, **`-20%` Enemy Hostile Max Cap**, **`+15%` Own Hostile Max Cap**, **`+2` Max Hostile Schemes**, `no_prowess_loss_from_age = yes` | `+5` to `+50` Intrigue Lifestyle XP |
| *Versatility* | Capped Fallback | N/A | N/A | 10-year buff `temporary_buff_self` (`+2` all stats, `+4` Prowess) + rolls for perm stats (`+1` skill, `+2` Prowess) | Granted when all 6 tracks are at 100 XP | N/A |

## Key Mechanics

- **Advancement Ritual:** Housed inside the Cast Major Blood Magic Grimoire (`bm_cast_blood_magic_major.001` -> `bm_blood_power_event.001`). Displays active bonuses, milestones, and capstone breakdowns. Consumes 150 Piety + Major Lifeforce only when a discipline is chosen, granting `+3` `enlightenment` XP and `+10` track XP, with a zero-cost return to the Grimoire.
- **Quarterly Pulse (`quarterly_playable_pulse`):** Ticks silently every 3 months for playable characters with Blood Power XP, calculating flat lifestyle experience (`floor(track_xp / 10) * 15`) and adding it directly to character lifestyle perk progression without toast spam.
- **Roster:** Retinue automatically tracked in Blood Magic story panel via `bm_refresh_blood_magic_rosters_effect`.
