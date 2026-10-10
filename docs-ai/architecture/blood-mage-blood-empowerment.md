# Blood Empowerment

> Living document describing current state. Follow `AGENTS.md`: high-density technical specs, zero roleplay fluff.

## Executive Summary

- **What:** Secondary lifestyle trait `lifestyle_blood_empowerment`. 5 progression tracks (`dynasty`, `mastery`, `presence`, `prosperity`, `shadows`), max 100 XP each.
- **Get / Level:** `bm_cast_blood_magic_major_decision` (Blood Empowerment option) -> Event `bm_blood_empowerment_event.001`.
  - Cost: 150 piety + consumes `lifeforce_modifier_major`. Req: `piety_level >= 1`. Cooldown: none.
  - XP Gain: +3 `enlightenment` XP (Blood Mage) or +3 `resilience` XP (Blood Knight) + 10 XP in chosen empowerment track (via `add_blood_empowerment_xp`).

## Universal Baseline Modifiers

Every level (10 to 100 XP) across all 5 tracks incorporates the universal baseline defined once via Clausewitz script preprocessor variables (`@` syntax) in `common/traits/bm_blood_empowerment_trait.txt`:
- `@bm_common_health = 0.1` (+1.0 Health at track cap)
- `@bm_common_life_expectancy = 2` (+20 years Life Expectancy at track cap)
- `@bm_common_years_of_fertility = 1` (+10 years Fertility at track cap)
- `@bm_common_epidemic_resistance = 1` (+10 Epidemic Resistance at track cap)

## Track Benefits Table

Each track spans 10 levels (10 to 100 XP, +10 XP per channel). Modifiers stack additively:

| Track | Specialization | Benefits per Level (Levels 10–100) | Full Track Cap (100 XP) |
| --- | --- | --- | --- |
| `dynasty` | Genetics & Fertility | Baseline + `+2.5%` Positive Congenital Chance, `+2.5%` Inactive Trait Inheritance, `+4%` Fertility | Baseline ×10, `+25%` Congenital, `+25%` Inactive Inheritance, `+40%` Fertility |
| `mastery` | Lifestyle & Tongues | Baseline + `+4%` Lifestyle XP Gain Mult, `-10` Days Language Scheme Phase, `+3%` Personal Scheme Power; `+1` Max Language Schemes at levels 30, 60, 90, 100 | Baseline ×10, `+40%` Lifestyle XP, `-100` Days Phase Duration, `+30%` Personal Scheme Power, `+4` Max Language Schemes |
| `presence` | Diplomacy & Magnetism | Baseline + `+5%` Stress Loss Mult, `+1.5` General Opinion, `+1.0` Vassal Opinion, `+5%` Sway Scheme Power | Baseline ×10, `+50%` Stress Loss, `+15` General Opinion, `+10` Vassal Opinion, `+50%` Sway Power |
| `prosperity` | Domain & Treasury | Baseline + `+2%` Monthly Income Mult, `-2%` Men-at-Arms Maintenance, `+2%` Domain Tax Mult, `-2%` Holding Construction Gold Cost, `-2%` Domicile/Camp Building Cost Mult | Baseline ×10, `+20%` Monthly Income, `-20%` MaA Upkeep, `+20%` Domain Taxes, `-20%` Holding Build Cost, `-20%` Domicile Build Cost |
| `shadows` | Subterfuge & Warding | Baseline + `+3` Hostile Scheme Resistance, `+5` Owned Scheme Secrecy, `-3%` Enemy Scheme Success Chance | Baseline ×10, `+30` Scheme Resistance, `+50` Scheme Secrecy, `-30%` Enemy Plot Success Chance |
| *Versatility* | Capped Fallback | 10-year buff `temporary_buff_self` (`+2` all stats, `+4` Prowess) + rolls for perm stats (`+1` skill, `+2` Prowess) | Granted when all 5 tracks are at 100 XP |

## Key Mechanics

- **Advancement:** `bm_cast_blood_magic_major_decision` fires `bm_cast_blood_magic_major.001` which triggers `bm_blood_empowerment_event.001`. Adds trait if missing. Capped tracks (100 XP) hidden from selection.
- **Spell Integration:** High-tier spells (Improve Education, Add Second Education, Inscribe Blood Runes) do not require Blood Empowerment XP; they evaluate independent piety and lifeforce costs.
- **Empowered Retinue:** Blood Knights are martial vessels empowered via blood magic:
  - `make_blood_knight_interaction`: Cost: 100 piety + major Lifeforce. Gives `lifestyle_blood_knight` trait with 3 evolutive tracks (Vanguard, Slaughter, Resilience).
  - See `blood-mage-blood-knight.md` for full specification.
- **Roster:** Retinue automatically tracked in Blood Magic story panel via `bm_refresh_blood_magic_rosters_effect`.

## Gotchas

- `lifestyle_blood_empowerment` does not grant passive XP over time; it only advances when the character explicitly invests major Lifeforce into the empowerment decision.
- All five empowerment tracks share baseline increases to health, life expectancy, years of fertility, and epidemic resistance, compounding longevity across specializations.
