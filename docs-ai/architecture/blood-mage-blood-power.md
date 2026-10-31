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

| Track | +10 (Per 10 XP Step) | +20 (Every 20 XP Step) | +50 (Milestone) | +100 (Cumulative Total) |
| :--- | :--- | :--- | :--- | :--- |
| **Presence** (`presence`) | `+0.1` Piety/mo, `+5` Diplomacy XP/mo | `+5` Personal Scheme Success, `-5d` Scheme Phase | `+1` Max Personal Schemes, `+15%` Monthly Renown | **`+1.0` Piety/mo**, **`+20` Personal Scheme Success**, **`-20d` Scheme Phase**, **`+1` Max Personal Schemes**, **`+35%` Monthly Renown**, **`+50` Diplomacy XP/mo**, `no_prowess_loss_from_age = yes` |
| **Warband** (`warband`) | `+0.1` Piety/mo, `+7%` Knight Eff, `+5` Martial XP/mo | `+1` Advantage (20/40/70/80), `+1` Knight Limit (30/60/90) | (advancement steps) | **`+1.0` Piety/mo**, **`+56%` Knight Eff**, **`+3` Knight Limit**, **`+4` Advantage**, **`+50` Martial XP/mo**, `no_prowess_loss_from_age = yes` |
| **Prosperity** (`prosperity`) | `+0.1` Piety/mo, `+8%` Income Mult, `+5` Stewardship XP/mo | `-5%` Men-at-Arms Maintenance | `+0.5` Gold/mo | **`+1.0` Piety/mo**, **`+64%` Income Mult**, **`+1.0` Gold/mo**, **`-20%` MaA Maintenance**, **`+50` Stewardship XP/mo**, `no_prowess_loss_from_age = yes` |
| **Shadows** (`shadows`) | `+0.1` Piety/mo, `+2.5` Dread Baseline, `+5` Hostile Scheme Success, `+5` Intrigue XP/mo | (steady progression) | `+1` Max Hostile Schemes | **`+1.0` Piety/mo**, **`+25` Dread Baseline**, **`+40` Hostile Scheme Success**, **`+2` Max Hostile Schemes**, **`+15%` Own Max Cap**, **`+50` Intrigue XP/mo**, `no_prowess_loss_from_age = yes` |
| **Mastery** (`mastery`) | `+0.1` Piety/mo, `+5%` Lifestyle XP Mult, `-5%` Stress Gain, `+5` Learning XP/mo | `+5%` Piety Mult | `+0.25` Health | **`+1.0` Piety/mo**, **`+40%` Lifestyle XP Mult**, **`+20%` Piety Mult**, **`-40%` Stress Gain**, **`+0.50` Health**, **`+50` Learning XP/mo**, `no_prowess_loss_from_age = yes` |
| **Legacy** (`dynasty`) | `+0.1` Piety/mo, `+8%` Strengthen, `+5` Focus XP/mo | `+5` Years of Fertility | `-50%` Inbreeding Chance | **`+1.0` Piety/mo**, **`+64%` Strengthen**, **`+20` Years of Fertility**, **Inbreeding Immunity (`-100%`)**, **`+50` Focus XP/mo**, `no_prowess_loss_from_age = yes` |
| *Versatility* | N/A | N/A | N/A | Granted when all 6 tracks are at 100 XP: 10-year buff `temporary_buff_self` (`+2` all stats, `+4` Prowess) + rolls for permanent stat/prowess increases |

## Key Mechanics

- **Advancement Ritual:** Housed inside the Cast Major Blood Magic Grimoire (`bm_cast_blood_magic_major.001` -> `bm_blood_power_event.001`). Displays active bonuses, milestones, and capstone breakdowns. Consumes 150 Piety + Major Lifeforce only when a discipline is chosen, granting `+3` `enlightenment` XP and `+10` track XP, with a zero-cost return to the Grimoire.
- **Quarterly Pulse (`quarterly_playable_pulse`):** Ticks silently every 3 months for playable characters with Blood Power XP, calculating flat lifestyle experience (`floor(track_xp / 10) * 15`) and adding it directly to character lifestyle perk progression without toast spam.
- **Roster:** Retinue automatically tracked in Blood Magic story panel via `bm_refresh_blood_magic_rosters_effect`.
