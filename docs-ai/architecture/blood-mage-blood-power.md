# Blood Power

Living technical specification for the Blood Power subsystem.

## Executive Summary

- **What:** Secondary lifestyle trait `lifestyle_blood_power`. 6 progression tracks (`dynasty`, `warband`, `mastery`, `presence`, `prosperity`, `shadows`), max 100 XP each.
- **5-Tier Progression Structure:** Each track consolidates into 5 distinct milestones at **10, 30, 50, 70, and 100 XP** (instead of 10 incremental steps), with maximum 3–4 thematic modifiers per discipline.
- **Universal Piety Baseline:** Tracks grant scaling Monthly Piety at every tier: **+0.1** (10 XP), **+0.3** (30 XP), **+0.5** (50 XP), **+0.7** (70 XP), and **+1.0** (100 XP), totaling up to **+6.0 Monthly Piety** across all 6 maxed disciplines.
- **Age Prowess Lock:** Every maxed track at 100 XP grants `no_prowess_loss_from_age = yes`.
- **Flat Monthly Lifestyle XP:** Every 10 XP in a track yields **+5 flat monthly Lifestyle XP** (paid silently every quarter via `quarterly_playable_pulse` as **+15 XP per quarter**, scaling from **+5/mo** at 10 XP up to **+50/mo = +150/quarter** at 100 XP):
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
  - Dynasty Synergy: Active House Covenants grant a yearly roll (50% / 67% / 100% chance based on covenant tier) to award +1 XP in the matching track.
  - Fallback: Once all 6 tracks reach 100 XP, unlocks `Versatility` option granting 10-year `temporary_buff_self` and rolls for permanent skill/prowess increases.

## Track Benefits Table

Each track spans 5 distinct progression tiers (10, 30, 50, 70, 100 XP). In CK3 engine mechanics, each tier block defines the complete set of active modifiers for that rank:

| Track | 10 XP (Starter) | 30 XP (Medium) | 50 XP (Milestone) | 70 XP (Major) | 100 XP (Capstone) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Presence** (`presence`) | `+0.1` Piety/mo, `+5` Scheme Success, `-5d` Scheme Phase | `+0.3` Piety/mo, `+10` Scheme Success, `-10d` Scheme Phase | `+0.5` Piety/mo, `+15` Scheme Success, `-15d` Scheme Phase, `+15%` Renown | `+0.7` Piety/mo, `+20` Scheme Success, `-20d` Scheme Phase, `+15%` Renown | **`+1.0` Piety/mo**, **`+25` Scheme Success**, **`-25d` Scheme Phase**, **`+35%` Renown**, **`+1` Max Personal Schemes**, `no_prowess_loss_from_age = yes` |
| **Warband** (`warband`) | `+0.1` Piety/mo, `+15%` Knight Eff, `+1` Knight Limit | `+0.3` Piety/mo, `+30%` Knight Eff, `+2` Knight Limit | `+0.5` Piety/mo, `+45%` Knight Eff, `+2` Knight Limit, `+2` Advantage | `+0.7` Piety/mo, `+60%` Knight Eff, `+3` Knight Limit, `+2` Advantage | **`+1.0` Piety/mo**, **`+75%` Knight Eff**, **`+4` Knight Limit**, **`+5` Advantage**, `no_prowess_loss_from_age = yes` |
| **Prosperity** (`prosperity`) | `+0.1` Piety/mo, `+15%` Income Mult, `-5%` MaA Maint | `+0.3` Piety/mo, `+30%` Income Mult, `-10%` MaA Maint | `+0.5` Piety/mo, `+45%` Income Mult, `-15%` MaA Maint, `+0.5` Gold/mo | `+0.7` Piety/mo, `+60%` Income Mult, `-20%` MaA Maint, `+0.5` Gold/mo | **`+1.0` Piety/mo**, **`+75%` Income Mult**, **`-25%` MaA Maint**, **`+1.5` Gold/mo**, `no_prowess_loss_from_age = yes` |
| **Shadows** (`shadows`) | `+0.1` Piety/mo, `+8` Hostile Success, `+5` Dread Base | `+0.3` Piety/mo, `+16` Hostile Success, `+10` Dread Base | `+0.5` Piety/mo, `+24` Hostile Success, `+15` Dread Base, `+1` Max Hostile Schemes | `+0.7` Piety/mo, `+32` Hostile Success, `+20` Dread Base, `+1` Max Hostile Schemes | **`+1.0` Piety/mo**, **`+40` Hostile Success**, **`+25` Dread Base**, **`+2` Max Hostile Schemes**, **`+15` Own Max Cap**, `no_prowess_loss_from_age = yes` |
| **Mastery** (`mastery`) | `+0.1` Piety/mo, `+8%` Lifestyle XP, `-8%` Stress Gain | `+0.3` Piety/mo, `+16%` Lifestyle XP, `-16%` Stress Gain | `+0.5` Piety/mo, `+24%` Lifestyle XP, `-24%` Stress Gain, `+0.25` Health | `+0.7` Piety/mo, `+32%` Lifestyle XP, `-32%` Stress Gain, `+0.25` Health | **`+1.0` Piety/mo**, **`+40%` Lifestyle XP**, **`-40%` Stress Gain**, **`+0.50` Health**, **`+20%` Piety Mult**, `no_prowess_loss_from_age = yes` |
| **Legacy** (`dynasty`) | `+0.1` Piety/mo, `+15%` Strengthen, `+4` Fertile Yrs | `+0.3` Piety/mo, `+30%` Strengthen, `+8` Fertile Yrs | `+0.5` Piety/mo, `+45%` Strengthen, `+12` Fertile Yrs, `-50%` Inbreeding | `+0.7` Piety/mo, `+60%` Strengthen, `+16` Fertile Yrs, `-50%` Inbreeding | **`+1.0` Piety/mo**, **`+75%` Strengthen**, **`+20` Fertile Yrs**, **Inbreeding Immunity (`-100%`)**, `no_prowess_loss_from_age = yes` |
| *Versatility* | N/A | N/A | N/A | N/A | Granted when all 6 tracks are at 100 XP: 10-year buff `temporary_buff_self` (`+2` all stats, `+4` Prowess) + rolls for permanent stat/prowess increases |

## Key Mechanics

- **Advancement Ritual:** Housed inside the Cast Major Blood Magic Grimoire (`bm_cast_blood_magic_major.001` -> `bm_blood_power_event.001`). Displays active bonuses, milestones, and capstone breakdowns. Consumes 150 Piety + Major Lifeforce only when a discipline is chosen, granting `+3` `enlightenment` XP and `+10` track XP, with a zero-cost return to the Grimoire.
- **Quarterly Pulse (`quarterly_playable_pulse`):** Ticks silently every 3 months for playable characters with Blood Power XP, calculating flat lifestyle experience (`floor(track_xp / 10) * 15`) and adding it directly to character lifestyle perk progression without toast spam.
- **Roster:** Retinue automatically tracked in Blood Magic story panel via `bm_refresh_blood_magic_rosters_effect`.
