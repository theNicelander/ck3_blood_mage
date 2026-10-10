# Blood Mage: Trait Track Cumulative Benefits

> Living architecture document. Outlines the exact cumulative total benefits of the three main levelable lifestyle traits (`lifestyle_blood_mage`, `lifestyle_blood_knight`, and `lifestyle_blood_empowerment`) at **10 XP**, **50 XP**, and **100 XP**.

## Executive Summary

- **Cumulative Track Mechanic:** In CK3 trait tracks, each tier unlocked (every 10 XP) applies its modifier block additively. Characters at 50 XP receive the sum of all benefits from tiers 10, 20, 30, 40, and 50. Characters at 100 XP receive the sum of all 10 tiers (10 through 100).
- **Format:** 4 columns (`Track | 10 XP | 50 XP | 100 XP`), one row per track.
- **Scope:** Covers all 15 tracks across the 3 core levelable traits:
  1. **Blood Mage (`lifestyle_blood_mage`):** 5 schools (`ancient`, `enlightenment`, `bloodline`, `benediction`, `hematurgy`).
  2. **Blood Knight (`lifestyle_blood_knight`):** 3 martial tracks (`vanguard`, `slaughter`, `resilience`) + 2 shared tracks (`ancient`, `benediction`).
  3. **Blood Empowerment (`lifestyle_blood_empowerment`):** 5 domain tracks (`dynasty`, `mastery`, `presence`, `prosperity`, `shadows`).

---

## 1. Blood Mage (`lifestyle_blood_mage`)

**Base Trait Modifiers:**
- `+2` Learning per Piety level
- `+10` Same Trait Opinion (`lifestyle_blood_mage`)

*Note: In `lifestyle_blood_mage`, tiers 10–40 and 60–90 grant the standard Vitality Baseline (`+0.1` Health, `+2` Life Expectancy, `+1` Year Fertility, `+1` Epidemic Resistance). Tiers 50 and 100 grant capstones instead of the vitality step (granting 4 total vitality steps at 50 XP and 8 total vitality steps at 100 XP).*

| Track | 10 XP | 50 XP | 100 XP |
| --- | --- | --- | --- |
| `ancient` | • `+0.1` Health<br>• `+2` Life Expectancy<br>• `+1` Year of Fertility<br>• `+1` Epidemic Resistance<br>• `+0.2` Monthly Piety<br>• `+5%` Monthly Piety Gain Mult | • `+0.4` Health<br>• `+8` Life Expectancy<br>• `+4` Years of Fertility<br>• `+4` Epidemic Resistance<br>• `+1.0` Monthly Piety<br>• `+25%` Monthly Piety Gain Mult<br>• `+1` Learning per Piety level<br>• `+1` Prowess per Piety level | • `+0.8` Health<br>• `+16` Life Expectancy<br>• `+8` Years of Fertility<br>• `+8` Epidemic Resistance<br>• `+2.0` Monthly Piety<br>• `+50%` Monthly Piety Gain Mult<br>• `+2` Learning per Piety level<br>• `+1` Prowess per Piety level<br>• Full age prowess lock (`no_prowess_loss_from_age = yes`) |
| `enlightenment` | • `+0.1` Health<br>• `+2` Life Expectancy<br>• `+1` Year of Fertility<br>• `+1` Epidemic Resistance<br>• `+5%` Monthly Lifestyle XP Gain Mult | • `+0.4` Health<br>• `+8` Life Expectancy<br>• `+4` Years of Fertility<br>• `+4` Epidemic Resistance<br>• `+25%` Monthly Lifestyle XP Gain Mult<br>• `+1` Martial per Piety level<br>• `+1` Prowess per Piety level | • `+0.8` Health<br>• `+16` Life Expectancy<br>• `+8` Years of Fertility<br>• `+8` Epidemic Resistance<br>• `+50%` Monthly Lifestyle XP Gain Mult<br>• `+2` Martial per Piety level<br>• `+1` Prowess per Piety level<br>• Full age prowess lock (`no_prowess_loss_from_age = yes`) |
| `bloodline` | • `+0.1` Health<br>• `+2` Life Expectancy<br>• `+1` Year of Fertility<br>• `+1` Epidemic Resistance<br>• `+0.1` Monthly Dynasty Prestige | • `+0.4` Health<br>• `+8` Life Expectancy<br>• `+4` Years of Fertility<br>• `+4` Epidemic Resistance<br>• `+0.5` Monthly Dynasty Prestige<br>• `+1` Stewardship per Piety level<br>• `+1` Prowess per Piety level | • `+0.8` Health<br>• `+16` Life Expectancy<br>• `+8` Years of Fertility<br>• `+8` Epidemic Resistance<br>• `+1.0` Monthly Dynasty Prestige<br>• `+2` Stewardship per Piety level<br>• `+1` Prowess per Piety level<br>• Full age prowess lock (`no_prowess_loss_from_age = yes`) |
| `benediction` | • `+0.1` Health<br>• `+2` Life Expectancy<br>• `+1` Year of Fertility<br>• `+1` Epidemic Resistance<br>• `+1.5` General Opinion<br>• `+1.0` Vassal Opinion<br>• `+0.2` Monthly Prestige<br>• `+5%` Monthly Prestige Gain Mult | • `+0.4` Health<br>• `+8` Life Expectancy<br>• `+4` Years of Fertility<br>• `+4` Epidemic Resistance<br>• `+7.5` General Opinion<br>• `+5.0` Vassal Opinion<br>• `+1.0` Monthly Prestige<br>• `+25%` Monthly Prestige Gain Mult<br>• `+1` Diplomacy per Piety level<br>• `+1` Prowess per Piety level | • `+0.8` Health<br>• `+16` Life Expectancy<br>• `+8` Years of Fertility<br>• `+8` Epidemic Resistance<br>• `+15.0` General Opinion<br>• `+10.0` Vassal Opinion<br>• `+2.0` Monthly Prestige<br>• `+50%` Monthly Prestige Gain Mult<br>• `+2` Diplomacy per Piety level<br>• `+1` Prowess per Piety level<br>• Full age prowess lock (`no_prowess_loss_from_age = yes`) |
| `hematurgy` | • `+0.1` Health<br>• `+2` Life Expectancy<br>• `+1` Year of Fertility<br>• `+1` Epidemic Resistance<br>• `-5` Enemy Hostile Scheme Success Chance | • `+0.4` Health<br>• `+8` Life Expectancy<br>• `+4` Years of Fertility<br>• `+4` Epidemic Resistance<br>• `-25` Enemy Hostile Scheme Success Chance<br>• `+1` Intrigue per Piety level<br>• `+1` Prowess per Piety level | • `+0.8` Health<br>• `+16` Life Expectancy<br>• `+8` Years of Fertility<br>• `+8` Epidemic Resistance<br>• `-50` Enemy Hostile Scheme Success Chance<br>• `+2` Intrigue per Piety level<br>• `+1` Prowess per Piety level<br>• Full age prowess lock (`no_prowess_loss_from_age = yes`) |

---

## 2. Blood Knight (`lifestyle_blood_knight`)

**Base Trait Modifiers:**
- `-1.0` Health
- `-5` Life Expectancy
- `-5` Prowess

*Note: In `lifestyle_blood_knight`, `vanguard` and `slaughter` include the full common vitality and monthly prestige step across all 10 tiers (10–100). `resilience` defines `health = 0.05` per tier. `ancient` and `benediction` follow the Blood Mage vitality profile (skipping vitality at 50 and 100 XP).*

| Track | 10 XP | 50 XP | 100 XP |
| --- | --- | --- | --- |
| `vanguard` | • `+0.1` Health<br>• `+2` Life Expectancy<br>• `+1` Year of Fertility<br>• `+1` Epidemic Resistance<br>• `+0.1` Monthly Prestige<br>• `+1` Advantage<br>• `+2%` Army Movement Speed<br>• `+3%` Army Pursuit Mult | • `+0.5` Health<br>• `+10` Life Expectancy<br>• `+5` Years of Fertility<br>• `+5` Epidemic Resistance<br>• `+0.5` Monthly Prestige<br>• `+5` Advantage<br>• `+2` Martial (from tiers 20, 40)<br>• `+10%` Army Movement Speed<br>• `+15%` Army Pursuit Mult<br>• `+1` Martial per Prestige level | • `+1.0` Health<br>• `+20` Life Expectancy<br>• `+10` Years of Fertility<br>• `+10` Epidemic Resistance<br>• `+1.0` Monthly Prestige<br>• `+10` Advantage<br>• `+5` Martial (from tiers 20, 40, 60, 80, 100)<br>• `+20%` Army Movement Speed<br>• `+30%` Army Pursuit Mult<br>• `+2` Martial per Prestige level |
| `slaughter` | • `+0.1` Health<br>• `+2` Life Expectancy<br>• `+1` Year of Fertility<br>• `+1` Epidemic Resistance<br>• `+0.1` Monthly Prestige<br>• `+2` Prowess<br>• `+10%` Knight Effectiveness Mult<br>• `+5%` Dread Gain Mult | • `+0.5` Health<br>• `+10` Life Expectancy<br>• `+5` Years of Fertility<br>• `+5` Epidemic Resistance<br>• `+0.5` Monthly Prestige<br>• `+10` Prowess<br>• `+50%` Knight Effectiveness Mult<br>• `+25%` Dread Gain Mult<br>• `+1` Prowess per Prestige level | • `+1.0` Health<br>• `+20` Life Expectancy<br>• `+10` Years of Fertility<br>• `+10` Epidemic Resistance<br>• `+1.0` Monthly Prestige<br>• `+20` Prowess<br>• `+100%` Knight Effectiveness Mult<br>• `+50%` Dread Gain Mult<br>• `+2` Prowess per Prestige level |
| `resilience` | • `+0.05` Health<br>• `+2` Life Expectancy<br>• `+1` Year of Fertility<br>• `+1` Epidemic Resistance<br>• `+0.1` Monthly Prestige<br>• `+3%` Stress Loss Mult | • `+0.25` Health<br>• `+10` Life Expectancy<br>• `+5` Years of Fertility<br>• `+5` Epidemic Resistance<br>• `+0.5` Monthly Prestige<br>• `+15%` Stress Loss Mult<br>• `+0.25` Negate Health Penalty | • `+0.5` Health<br>• `+20` Life Expectancy<br>• `+10` Years of Fertility<br>• `+10` Epidemic Resistance<br>• `+1.0` Monthly Prestige<br>• `+30%` Stress Loss Mult<br>• `+0.75` Negate Health Penalty (`+0.25` at 50 XP + `+0.5` at 100 XP)<br>• Full age prowess lock (`no_prowess_loss_from_age = yes`) |
| `ancient` | • `+0.1` Health<br>• `+2` Life Expectancy<br>• `+1` Year of Fertility<br>• `+1` Epidemic Resistance<br>• `+0.2` Monthly Piety<br>• `+5%` Monthly Piety Gain Mult | • `+0.4` Health<br>• `+8` Life Expectancy<br>• `+4` Years of Fertility<br>• `+4` Epidemic Resistance<br>• `+1.0` Monthly Piety<br>• `+25%` Monthly Piety Gain Mult<br>• `+1` Learning per Piety level<br>• `+1` Prowess per Piety level | • `+0.8` Health<br>• `+16` Life Expectancy<br>• `+8` Years of Fertility<br>• `+8` Epidemic Resistance<br>• `+2.0` Monthly Piety<br>• `+50%` Monthly Piety Gain Mult<br>• `+2` Learning per Piety level<br>• `+1` Prowess per Piety level<br>• Full age prowess lock (`no_prowess_loss_from_age = yes`) |
| `benediction` | • `+0.1` Health<br>• `+2` Life Expectancy<br>• `+1` Year of Fertility<br>• `+1` Epidemic Resistance<br>• `+1.5` General Opinion<br>• `+1.0` Vassal Opinion<br>• `+0.2` Monthly Prestige<br>• `+5%` Monthly Prestige Gain Mult | • `+0.4` Health<br>• `+8` Life Expectancy<br>• `+4` Years of Fertility<br>• `+4` Epidemic Resistance<br>• `+7.5` General Opinion<br>• `+5.0` Vassal Opinion<br>• `+1.0` Monthly Prestige<br>• `+25%` Monthly Prestige Gain Mult<br>• `+1` Diplomacy per Piety level<br>• `+1` Prowess per Piety level | • `+0.8` Health<br>• `+16` Life Expectancy<br>• `+8` Years of Fertility<br>• `+8` Epidemic Resistance<br>• `+15.0` General Opinion<br>• `+10.0` Vassal Opinion<br>• `+2.0` Monthly Prestige<br>• `+50%` Monthly Prestige Gain Mult<br>• `+2` Diplomacy per Piety level<br>• `+1` Prowess per Piety level<br>• Full age prowess lock (`no_prowess_loss_from_age = yes`) |

---

## 3. Blood Empowerment (`lifestyle_blood_empowerment`)

**Base Trait Modifiers:** None.

*Note: All 5 tracks in `lifestyle_blood_empowerment` include the full universal vitality baseline (`+0.1` Health, `+2` Life Expectancy, `+1` Year Fertility, `+1` Epidemic Resistance) across every single tier from 10 to 100.*

| Track | 10 XP | 50 XP | 100 XP |
| --- | --- | --- | --- |
| `dynasty` | • `+0.1` Health<br>• `+2` Life Expectancy<br>• `+1` Year of Fertility<br>• `+1` Epidemic Resistance<br>• `+4%` Fertility<br>• `+2.5%` Positive Congenital / Genetic Trait Chance<br>• `+2.5%` Inactive Trait Inheritance Chance | • `+0.5` Health<br>• `+10` Life Expectancy<br>• `+5` Years of Fertility<br>• `+5` Epidemic Resistance<br>• `+20%` Fertility<br>• `+12.5%` Positive Congenital / Genetic Trait Chance<br>• `+12.5%` Inactive Trait Inheritance Chance | • `+1.0` Health<br>• `+20` Life Expectancy<br>• `+10` Years of Fertility<br>• `+10` Epidemic Resistance<br>• `+40%` Fertility<br>• `+25%` Positive Congenital / Genetic Trait Chance<br>• `+25%` Inactive Trait Inheritance Chance |
| `mastery` | • `+0.1` Health<br>• `+2` Life Expectancy<br>• `+1` Year of Fertility<br>• `+1` Epidemic Resistance<br>• `+4%` Monthly Lifestyle XP Gain Mult<br>• `-10` Days Learn Language Scheme Phase Duration<br>• `+3%` Personal Scheme Success Chance | • `+0.5` Health<br>• `+10` Life Expectancy<br>• `+5` Years of Fertility<br>• `+5` Epidemic Resistance<br>• `+20%` Monthly Lifestyle XP Gain Mult<br>• `-50` Days Learn Language Scheme Phase Duration<br>• `+15%` Personal Scheme Success Chance<br>• `+1` Max Learn Language Schemes (unlocked at 30 XP) | • `+1.0` Health<br>• `+20` Life Expectancy<br>• `+10` Years of Fertility<br>• `+10` Epidemic Resistance<br>• `+40%` Monthly Lifestyle XP Gain Mult<br>• `-100` Days Learn Language Scheme Phase Duration<br>• `+30%` Personal Scheme Success Chance<br>• `+4` Max Learn Language Schemes (unlocked at 30, 60, 90, 100 XP) |
| `presence` | • `+0.1` Health<br>• `+2` Life Expectancy<br>• `+1` Year of Fertility<br>• `+1` Epidemic Resistance<br>• `+1.5` General Opinion<br>• `+1.0` Vassal Opinion<br>• `+5%` Stress Loss Mult<br>• `+5%` Personal Scheme Success Chance | • `+0.5` Health<br>• `+10` Life Expectancy<br>• `+5` Years of Fertility<br>• `+5` Epidemic Resistance<br>• `+7.5` General Opinion<br>• `+5.0` Vassal Opinion<br>• `+25%` Stress Loss Mult<br>• `+25%` Personal Scheme Success Chance | • `+1.0` Health<br>• `+20` Life Expectancy<br>• `+10` Years of Fertility<br>• `+10` Epidemic Resistance<br>• `+15.0` General Opinion<br>• `+10.0` Vassal Opinion<br>• `+50%` Stress Loss Mult<br>• `+50%` Personal Scheme Success Chance |
| `prosperity` | • `+0.1` Health<br>• `+2` Life Expectancy<br>• `+1` Year of Fertility<br>• `+1` Epidemic Resistance<br>• `+2%` Monthly Income Mult<br>• `+2%` Domain Tax Mult<br>• `-2%` Men-at-Arms Maintenance<br>• `-2%` Holding Construction Gold Cost<br>• `-2%` Domicile Construction Gold Cost | • `+0.5` Health<br>• `+10` Life Expectancy<br>• `+5` Years of Fertility<br>• `+5` Epidemic Resistance<br>• `+10%` Monthly Income Mult<br>• `+10%` Domain Tax Mult<br>• `-10%` Men-at-Arms Maintenance<br>• `-10%` Holding Construction Gold Cost<br>• `-10%` Domicile Construction Gold Cost | • `+1.0` Health<br>• `+20` Life Expectancy<br>• `+10` Years of Fertility<br>• `+10` Epidemic Resistance<br>• `+20%` Monthly Income Mult<br>• `+20%` Domain Tax Mult<br>• `-20%` Men-at-Arms Maintenance<br>• `-20%` Holding Construction Gold Cost<br>• `-20%` Domicile Construction Gold Cost |
| `shadows` | • `+0.1` Health<br>• `+2` Life Expectancy<br>• `+1` Year of Fertility<br>• `+1` Epidemic Resistance<br>• `+3` Hostile Scheme Resistance<br>• `+5` Owned Scheme Secrecy<br>• `-3%` Enemy Hostile Scheme Success Chance | • `+0.5` Health<br>• `+10` Life Expectancy<br>• `+5` Years of Fertility<br>• `+5` Epidemic Resistance<br>• `+15` Hostile Scheme Resistance<br>• `+25` Owned Scheme Secrecy<br>• `-15%` Enemy Hostile Scheme Success Chance | • `+1.0` Health<br>• `+20` Life Expectancy<br>• `+10` Years of Fertility<br>• `+10` Epidemic Resistance<br>• `+30` Hostile Scheme Resistance<br>• `+50` Owned Scheme Secrecy<br>• `-30%` Enemy Hostile Scheme Success Chance |

---

## Where the details live

| Trait | Script File | Associated Docs |
| --- | --- | --- |
| `lifestyle_blood_mage` | `common/traits/bm_blood_mage_trait.txt` | [blood-mage-traits.md](blood-mage-traits.md), [blood-mage-track-xp.md](blood-mage-track-xp.md) |
| `lifestyle_blood_knight` | `common/traits/bm_blood_knight_trait.txt` | [blood-mage-blood-knight.md](blood-mage-blood-knight.md), [blood-mage-track-xp.md](blood-mage-track-xp.md) |
| `lifestyle_blood_empowerment` | `common/traits/bm_blood_empowerment_trait.txt` | [blood-mage-blood-empowerment.md](blood-mage-blood-empowerment.md), [blood-mage-track-xp.md](blood-mage-track-xp.md) |

## Gotchas

- **Vitality Step Discrepancy:** Blood Mage (and BK Ancient/Benediction) intentionally omit the vitality baseline at tiers 50 and 100 to budget for powerful scaling capstones (`+1` stat/prowess per piety level, age prowess lock). Blood Empowerment and martial BK tracks retain vitality at every tier.
- **Resilience Health Scaling:** `resilience` defines `health = 0.05` per tier alongside `stress_loss_mult = 0.03`, rather than `0.1` health, scaling to `+0.25` health at 50 XP and `+0.5` health at 100 XP.
- **Mastery Scheme Slots:** `max_learn_language_schemes_add` does not advance uniformly every 10 XP; it triggers strictly at levels 30, 60, 90, and 100 XP (`+1` slot at 50 XP, `+4` slots at 100 XP).
- **Additive Compounding Across Traits:** A character who holds both `lifestyle_blood_mage` (or `lifestyle_blood_knight`) and `lifestyle_blood_empowerment` stacks all unlocked track benefits additively across both traits.
