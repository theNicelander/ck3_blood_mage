# Blood Power

Living technical specification for the Blood Power subsystem.

## Executive Summary

- **What:** Secondary lifestyle trait `lifestyle_blood_power`. 6 progression tracks (`dynasty`, `warband`, `mastery`, `presence`, `prosperity`, `shadows`), max 100 XP each.
- **5-Tier Progression Structure:** Each track consolidates into 5 distinct milestones at **10, 30, 50, 70, and 100 XP** (instead of 10 incremental steps), with maximum 3–4 thematic modifiers per discipline.
- **Universal Piety Baseline:** Tracks grant scaling Monthly Piety at every tier: **+0.1** (10 XP), **+0.3** (30 XP), **+0.5** (50 XP), **+0.7** (70 XP), and **+1.0** (100 XP), totaling up to **+6.0 Monthly Piety** across all 6 maxed disciplines.
- **Shared 50 & 100 XP Milestones:** Every track awards **+10% Monthly Piety Mult, +5 Life Expectancy, +0.25 Health, and +0.02 Monthly Piety per Knight** at 50 XP and again at 100 XP (+20% Piety Mult, +10 Life Expectancy, +0.50 Health, and +0.04 Piety/Knight per track; up to +120% Piety Mult, +60 Life Expectancy, +3.0 Health, and +0.24 Piety/Knight when all 6 tracks are maxed).
- **Age Prowess Lock:** Every maxed track at 100 XP grants `no_prowess_loss_from_age = yes`.
- **Flat Monthly Lifestyle XP:** Every 10 XP in a track yields **+5 flat monthly Lifestyle XP** (paid silently every quarter via `quarterly_playable_pulse` as **+15 XP per quarter**, scaling from **+5/mo** at 10 XP up to **+50/mo = +150/quarter** at 100 XP):
  - `presence` -> **Diplomacy** Lifestyle XP
  - `warband` -> **Martial** Lifestyle XP
  - `prosperity` -> **Stewardship** Lifestyle XP
  - `shadows` -> **Intrigue** Lifestyle XP
  - `mastery` -> **Learning** Lifestyle XP
  - `dynasty` -> **Active Lifestyle Focus** (or random core lifestyle if unfocused)

## Track Benefits Table

Each track spans 5 distinct progression tiers (10, 30, 50, 70, 100 XP). In CK3 engine mechanics, trait track thresholds stack additively (all reached tiers add together). The table below lists the cumulative total active benefits at each milestone (common 50/100 bonuses omitted from table columns for clarity):

| Track | 10 XP (Starter) | 30 XP (Medium) | 50 XP (Milestone) | 70 XP (Major) | 100 XP (Capstone) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Presence** (`presence`) | `+0.1` Piety/mo, `+5` Gen Opinion, `+0.2` Prestige/mo, `+5%` Legitimacy Mult, `+8` Scheme Success | `+0.3` Piety/mo, `+10` Gen Opinion, `+0.4` Prestige/mo, `+10%` Legitimacy Mult, `+16` Scheme Success | `+0.5` Piety/mo, `+15` Gen Opinion, `+0.7` Prestige/mo, `+16%` Legitimacy Mult, `+24` Scheme Success, `+1` Max Schemes | `+0.7` Piety/mo, `+20` Gen Opinion, `+1.0` Prestige/mo, `+23%` Legitimacy Mult, `+32` Scheme Success, `+1` Max Schemes | **`+1.0` Piety/mo**, **`+25` Gen Opinion**, **`+1.5` Prestige/mo**, **`+30%` Legitimacy Mult**, **`+40` Scheme Success**, **`+2` Max Schemes**, `Age Prowess Lock` |
| **Warband** (`warband`) | `+0.1` Piety/mo, `+1` Knight Limit, `+15%` Knight Eff, `+2` Advantage, `+5%` Move Speed | `+0.3` Piety/mo, `+2` Knight Limit, `+30%` Knight Eff, `+4` Advantage, `+10%` Move Speed | `+0.5` Piety/mo, `+4` Knight Limit, `+45%` Knight Eff, `+6` Advantage, `+15%` Move Speed | `+0.7` Piety/mo, `+6` Knight Limit, `+60%` Knight Eff, `+8` Advantage, `+20%` Move Speed | **`+1.0` Piety/mo**, **`+8` Knight Limit**, **`+75%` Knight Eff**, **`+10` Advantage**, **`+25%` Move Speed**, `Age Prowess Lock` |
| **Prosperity** (`prosperity`) | `+0.1` Piety/mo, `+0.3` Gold/mo, `+6%` Income Mult, `-6%` MaA Maint | `+0.3` Piety/mo, `+0.6` Gold/mo, `+12%` Income Mult, `-12%` MaA Maint | `+0.5` Piety/mo, `+1.0` Gold/mo, `+18%` Income Mult, `-18%` MaA Maint | `+0.7` Piety/mo, `+1.4` Gold/mo, `+24%` Income Mult, `-24%` MaA Maint | **`+1.0` Piety/mo**, **`+2.0` Gold/mo**, **`+30%` Income Mult**, **`-30%` MaA Maint**, `Age Prowess Lock` |
| **Shadows** (`shadows`) | `+0.1` Piety/mo, `+8` Hostile Success, `-10` Enemy Success, `+6` Dread Base | `+0.3` Piety/mo, `+16` Hostile Success, `-20` Enemy Success, `+12` Dread Base | `+0.5` Piety/mo, `+24` Hostile Success, `-30` Enemy Success, `+18` Dread Base, `+1` Max Schemes | `+0.7` Piety/mo, `+32` Hostile Success, `-40` Enemy Success, `+24` Dread Base, `+1` Max Schemes | **`+1.0` Piety/mo**, **`+40` Hostile Success**, **`-50` Enemy Success**, **`+30` Dread Base**, **`+2` Max Schemes**, `Age Prowess Lock` |
| **Mastery** (`mastery`) | `+0.1` Piety/mo, `+10%` Lifestyle XP, `-10%` Stress Gain, `+10%` Stress Loss | `+0.3` Piety/mo, `+20%` Lifestyle XP, `-20%` Stress Gain, `+20%` Stress Loss | `+0.5` Piety/mo, `+30%` Lifestyle XP, `-30%` Stress Gain, `+30%` Stress Loss | `+0.7` Piety/mo, `+40%` Lifestyle XP, `-40%` Stress Gain, `+40%` Stress Loss | **`+1.0` Piety/mo**, **`+50%` Lifestyle XP**, **`-50%` Stress Gain**, **`+50%` Stress Loss**, `Age Prowess Lock` |
| **Legacy** (`dynasty`) | `+0.1` Piety/mo, `+10%` Strengthen, `+5` Fertile Yrs | `+0.3` Piety/mo, `+20%` Strengthen, `+10` Fertile Yrs | `+0.5` Piety/mo, `+30%` Strengthen, `+15` Fertile Yrs, `-50%` Inbreeding | `+0.7` Piety/mo, `+40%` Strengthen, `+20` Fertile Yrs, `-50%` Inbreeding | **`+1.0` Piety/mo**, **`+50%` Strengthen**, **`+25` Fertile Yrs**, **Inbreeding Immunity (`-100%`)**, `Age Prowess Lock` |
| *Versatility* | N/A | N/A | N/A | N/A | Granted when all 6 tracks are at 100 XP: 10-year buff `temporary_buff_self` (`+2` all stats, `+4` Prowess) + rolls for permanent stat/prowess increases |

## Key Mechanics

- **Advancement Ritual:** Housed inside the Cast Major Blood Magic Grimoire (`bm_cast_blood_magic_major.001` -> `bm_blood_power_event.001`). Displays active bonuses, milestones, and capstone breakdowns. Consumes 150 Piety + Major Lifeforce only when a discipline is chosen, granting `+3` `enlightenment` XP and `+10` track XP, with a zero-cost return to the Grimoire.
- **Quarterly Pulse (`quarterly_playable_pulse`):** Ticks silently every 3 months for playable characters with Blood Power XP, calculating flat lifestyle experience (`floor(track_xp / 10) * 15`) and adding it directly to character lifestyle perk progression without toast spam.
- **Roster:** Retinue automatically tracked in Blood Magic story panel via `bm_refresh_blood_magic_rosters_effect`.
