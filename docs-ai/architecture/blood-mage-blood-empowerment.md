# Blood Empowerment

> Living document. Follow `AGENTS.md` in this folder: concepts only, no numbers. Update it when the trait, tracks, empowerment events or retinue modifiers change.

## Executive Summary

- **What:** Secondary lifestyle trait `lifestyle_blood_empowerment`. 7 progression tracks (max 100 XP each). Gates education upgrades and blood runes.
- **Get / Level:** `bm_cast_blood_magic_major_decision` (Blood Empowerment option) -> Event `bm_blood_empowerment_event.001`.
  - Cost: 150 piety + consumes `lifeforce_modifier_major`. Req: `piety_level >= 1`. Cooldown: none.
  - XP Gain: +3 `enlightenment` XP + 10 XP in chosen empowerment track (via `add_blood_empowerment_xp`).

### Track Benefits Table

Each track spans 10 levels (10 to 100 XP, +10 XP per channel). All 10 levels in each track share the same active modifiers, including a **Universal Baseline** (`+1` Life Expectancy, `+0.1` Monthly Piety) per active tier:

| Track | Specialization | Benefits per Level (All Levels 10–100) |
| --- | --- | --- |
| `charisma` | Diplomacy | Baseline + `+2.5` General Opinion, `+5%` Monthly Prestige Gain Mult |
| `fury` | Martial | Baseline + `+5%` Knight Effectiveness, `+0.05` Monthly County Control Growth |
| `prosperity` | Stewardship | Baseline + `+2.5%` Domain Tax, `+0.05` Capital County Monthly Development Growth |
| `shadows` | Intrigue | Baseline + `+3` Dread Baseline, `-0.01` Monthly Tyranny (decay), `+5` Scheme Secrecy |
| `insight` | Learning | Baseline + `+5%` Development Growth (all holdings), `+5%` Monthly Piety Gain Mult |
| `legacy` | Bloodline | Baseline + `+5%` Positive Congenital Chance, `+5%` Inactive Positive Inheritance |
| `expertise` | Versatility | Baseline + `+2.5%` Lifestyle XP Gain Mult, `+5%` Cultural Fascination Mult |
| *Versatility* | Capped Fallback | 10-year buff `temporary_buff_self` (`+2` all stats, `+4` Prowess) + rolls for perm stats (`+1` skill, `+2` Prowess) |

## Key Mechanics

- **Advancement:** `bm_cast_blood_magic_major_decision` fires `bm_cast_blood_magic_major.001` which triggers `bm_blood_empowerment_event.001`. Adds trait if missing. Capped tracks (100 XP) hidden from selection.
- **High-Tier Spell Gates:** Total XP across `lifestyle_blood_empowerment` tracks gates rituals:
  - Improve Education tier: Req 50 total XP (`required_xp_improve_education`).
  - Add Second Education: Req 70 total XP (`required_xp_new_education`).
  - Inscribe Blood Runes: Req 50 total XP (`bm_blood_rune_minimum_xp`).
- **Empowered Retinue:** Blood Knights are martial vessels empowered via blood magic:
  - `grant_blood_knight_interaction`: Cost: 100 piety + major Lifeforce. Gives `lifestyle_blood_knight` trait with 3 evolutive tracks (Vanguard, Slaughter, Resilience).
  - See `blood-mage-blood-knight.md` for full specification.
- **Roster:** Retinue automatically tracked in Blood Magic story panel via `bm_refresh_blood_magic_rosters_effect`.

## Gotchas

- `lifestyle_blood_empowerment` does not grant passive XP over time; it only advances when the player or AI explicitly invests major Lifeforce into the empowerment decision.
- All seven empowerment tracks share baseline increases to life expectancy and monthly piety, so advancing multiple tracks compounds longevity and spiritual power.

## Not verified

AI rulers balancing the heavy physical drain of sustaining multiple Blood Champions against the military advantage provided in ongoing wars.
