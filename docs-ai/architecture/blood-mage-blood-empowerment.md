# Blood Empowerment

Living technical specification for the Blood Empowerment subsystem.

## Executive Summary

- **What:** Secondary lifestyle trait `lifestyle_blood_empowerment`. 5 progression tracks (`dynasty`, `mastery`, `presence`, `prosperity`, `shadows`), max 100 XP each.
- **Acquisition:** Automatically granted at base rank (0 XP) simultaneously when acquiring `lifestyle_blood_mage` or `lifestyle_blood_knight`, ensuring both traits sit adjacent in the character interface.
- **Advancement:** `bm_cast_blood_magic_major_decision` (Blood Empowerment option) -> Event `bm_blood_empowerment_event.001`.
  - Cost: 150 piety + consumes `lifeforce_modifier_major`. Req: `piety_level >= 1`. Cooldown: none.
  - XP Gain: +3 `enlightenment` XP (Blood Mage & Blood Knight) + 10 XP in chosen empowerment track (via `add_blood_empowerment_xp`).

## Universal Baseline Modifiers

Levels 10 to 90 across all 5 tracks incorporate the universal baseline defined via Clausewitz script preprocessor variables (`@` syntax) in `common/traits/bm_blood_empowerment_trait.txt`:
- `@bm_common_health = 0.1` (+0.9 Health at 90 XP)
- `@bm_common_life_expectancy = 2` (+18 years Life Expectancy at 90 XP)
- `@bm_common_years_of_fertility = 1` (+9 years Fertility at 90 XP)
- `@bm_common_epidemic_resistance = 1` (+9 Epidemic Resistance at 90 XP)

At 100 XP, the vitality baseline is skipped in favor of the track capstones: `piety_level_impact_mult = 0.05` (+5% Devotion impact per track, stacking up to +25% total across all 5 tracks) and `no_prowess_loss_from_age = yes`.

## Track Benefits Table

Each track spans 10 levels (10 to 100 XP, +10 XP per channel). Modifiers stack additively:

| Track | Specialization | Benefits per Level (Levels 10–90) | Full Track Cap (100 XP) |
| --- | --- | --- | --- |
| `dynasty` | Genetics & Fertility | Baseline + `+2.5%` Positive Congenital Chance, `+2.5%` Inactive Trait Inheritance, `+4%` Fertility | `+25%` Congenital, `+25%` Inactive Inheritance, `+40%` Fertility, `+5%` Devotion Impact (`piety_level_impact_mult = 0.05`), `no_prowess_loss_from_age = yes` |
| `mastery` | Lifestyle & Tongues | Baseline + `+4%` Lifestyle XP Gain Mult, `-10` Days Language Scheme Phase, `+3%` Personal Scheme Power; `+1` Max Language Schemes at levels 30, 60, 90 | `+40%` Lifestyle XP, `-100` Days Phase Duration, `+30%` Personal Scheme Power, `+4` Max Language Schemes, `+5%` Devotion Impact (`piety_level_impact_mult = 0.05`), `no_prowess_loss_from_age = yes` |
| `presence` | Diplomacy & Magnetism | Baseline + `+5%` Stress Loss Mult, `+1.5` General Opinion, `+1.0` Vassal Opinion | `+50%` Stress Loss, `+15` General Opinion, `+10` Vassal Opinion, `+5%` Devotion Impact (`piety_level_impact_mult = 0.05`), `no_prowess_loss_from_age = yes` |
| `prosperity` | Domain & Treasury | Baseline + `+0.1` Monthly Income, `+2.5%` Monthly Income Mult | `+1.0` Monthly Income, `+25%` Monthly Income Mult, `+5%` Devotion Impact (`piety_level_impact_mult = 0.05`), `no_prowess_loss_from_age = yes` |
| `shadows` | Subterfuge & Warding | Baseline + `+5` Owned Scheme Secrecy, `-3%` Enemy Scheme Success Chance | `+50` Scheme Secrecy, `-30%` Enemy Plot Success Chance, `+5%` Devotion Impact (`piety_level_impact_mult = 0.05`), `no_prowess_loss_from_age = yes` |
| *Versatility* | Capped Fallback | 10-year buff `temporary_buff_self` (`+2` all stats, `+4` Prowess) + rolls for perm stats (`+1` skill, `+2` Prowess) | Granted when all 5 tracks are at 100 XP |

## Key Mechanics

- **Advancement:** `bm_cast_blood_magic_major_decision` fires `bm_cast_blood_magic_major.001` which triggers `bm_blood_empowerment_event.001`. Adds trait if missing. Capped tracks (100 XP) hidden from selection.
- **Spell Integration:** High-tier spells (Improve Education, Add Second Education, Inscribe Blood Runes) do not require Blood Empowerment XP; they evaluate independent piety and lifeforce costs.
- **Roster:** Retinue automatically tracked in Blood Magic story panel via `bm_refresh_blood_magic_rosters_effect`.
