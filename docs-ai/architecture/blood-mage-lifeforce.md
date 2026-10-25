# Blood Mage Lifeforce

Living technical specification for the Lifeforce resource economy, character modifiers, battlefield harvesting brackets, and spellcasting consumption.

## Overview

Core spellcasting resource stored as stacking character modifiers (`lifeforce_modifier_minor`, `lifeforce_modifier_major`, `lifeforce_modifier_superior`).
- **Passive Vitality vs Fuel:** Unspent positive stacks grant permanent buffs (Health, Life Exp, Fertility, Epidemic Res, Prowess). Casting consumes 1 positive stack and applies temporary exhaustion (`lifeforce_modifier_negative_minor/major/superior`).
- **Harvesting Asymmetry:**
  - **Blood Mages:** Childbirth (+1 Major per child), wilderness blood hunts (`seek_power_decision`), prisoner execution (`lifedrain_prisoner_event_interaction`, `mass_lifedrain_prisoners_decision`), courtier siphoning, murder schemes with Superior **Hulinhjálmur**, and spiritual distillation (`bm_manifest_lifeforce_decision`).
  - **Blood Knights:** Wilderness blood hunts (`seek_power_decision`), battlefield troop-bracket harvesting, lethal single combat kills (Major LF + 25% Superior chance vs worthy foes), and ambient yearly pulse (`blood_mage_yearly_events.004`).

### Lifeforce & Exhaustion Modifiers Table (`common/modifiers/bm_lifeforce.txt`)
| Modifier Key | Role | Stacking | Duration | Mechanical Effects per Stack |
| --- | --- | --- | --- | --- |
| `lifeforce_modifier_minor` | Tier 1 Fuel | Yes | Permanent until spent | `+0.1` Health, `+1` Life Exp, `+1` Fertility Yr, `+1` Epidemic Res, `+0.1` Negate Health Penalty |
| `lifeforce_modifier_major` | Tier 2 Fuel | Yes | Permanent until spent | `+0.3` Health, `+3` Life Exp, `+3` Fertility Yrs, `+3` Epidemic Res, `+0.3` Negate Health Penalty |
| `lifeforce_modifier_superior` | Tier 3 Fuel | Yes | Permanent until spent | `+0.6` Health, `+6` Life Exp, `+6` Fertility Yrs, `+6` Epidemic Res, `+0.6` Negate Health Penalty, `+3` Prowess |
| `lifeforce_modifier_negative_minor` | Minor Exhaustion | Yes | **1 Year** (`365` days) | `-0.1` Health, `-1` Life Exp, `-1` Fertility Yr, `-1` Epidemic Res, `-0.1` Negate Health Penalty, `-1` Prowess |
| `lifeforce_modifier_negative_major` | Major Exhaustion | Yes | **3 Years** (`1095` days; `365`d on Flay/Distill) | `-0.3` Health, `-3` Life Exp, `-3` Fertility Yrs, `-3` Epidemic Res, `-0.3` Negate Health Penalty, `-2` Prowess |
| `lifeforce_modifier_negative_superior` | Superior Exhaustion | Yes | **3 Years** (`1095` days; `5` yrs on Flay) | `-0.6` Health, `-6` Life Exp, `-6` Fertility Yrs, `-6` Epidemic Res, `-0.6` Negate Health Penalty, `-4` Prowess |
| `lifedrained_modifier` | Victim Siphon Toll | Yes | Permanent (until restored) | `-0.5` Health, `-10` Life Exp, `-5` Fertility Yrs, `-5` Epidemic Res, `-0.5` Negate Health Penalty, `-5` Prowess |
| `recently_lifedrained_modifier` | Victim Cooldown | No | **1 Year** (`years = 1`) | Blocks repeat `lifedrain_courtier_event_interaction` on the same victim |

---

## Battlefield Lifeforce & XP Scaling (`common/scripted_effects/bm_combat_effects.txt`)

Triggered on `on_combat_end_winner` (`bm_on_combat_end_winner`) for surviving side commanders and knights who have `lifestyle_blood_knight`:

| Battle Size (`num_total_troops` OR `num_enemies_killed`) | Minor Lifeforce Chance | Major Lifeforce Chance | Commander `vanguard` XP | Knight `vanguard` XP |
| --- | --- | --- | --- | --- |
| **10,000+ troops** (or 5,000+ killed) | **100%** (Guaranteed) | **100%** (Guaranteed) | `+5` XP | `+5` XP |
| **8,000 – 9,999 troops** (or 4,000+ killed) | **100%** (Guaranteed) | **90%** | `+5` XP | `+5` XP |
| **6,000 – 7,999 troops** (or 3,000+ killed) | **100%** (Guaranteed) | **75%** | `+5` XP | `+4` XP |
| **4,000 – 5,999 troops** (or 2,000+ killed) | **100%** (Guaranteed) | **50%** | `+5` XP | `+4` XP |
| **2,000 – 3,999 troops** (or 1,000+ killed) | **85%** | **25%** | `+4` XP | `+3` XP |
| **1,000 – 1,999 troops** (or 500+ killed) | **75%** | **10%** | `+4` XP | `+3` XP |
| **500 – 999 troops** (or 200+ killed) | **50%** | 0% | `+3` XP | `+2` XP |
| **100 – 499 troops** (or 50+ killed) | **25%** | 0% | `+2` XP | `+1` XP |
| **< 100 troops** (< 50 killed) | **10%** | 0% | `+2` XP | `+1` XP |

*Note: Surviving a battle defeat (`bm_on_combat_end_loser`) grants Blood Knights `+1` to `+3` `vanguard` XP and `0` to `+2` `enlightenment` XP based on battle size, with no Lifeforce harvest.*

---

## Master Lifeforce Sources & Sinks Matrix

| Action / Hook | Class Access | Cost / Requirements | Lifeforce Delta | Track XP Gain |
| --- | --- | --- | --- | --- |
| **Execute Prisoner (`lifedrain_prisoner_event_interaction`)** | Mage | 50 Piety (`lifedrain_piety_cost_major`), un-drained prisoner | **+1 Major** (executes victim) | `+2` `hematurgy` |
| **Mass Lifedrain (`mass_lifedrain_prisoners_decision`)** | Mage & Knight | Piety per prisoner, dungeon prisoners | **+Minor / +Major** per prisoner executed | Scaled `hematurgy` |
| **Siphon Courtier/Prisoner (`lifedrain_courtier_event_interaction`)** | Mage & Knight | 25 Piety (`lifedrain_piety_cost_minor`), 3-mo CD | **+1 Minor** (victim gets `lifedrained_modifier`) | `+1` `hematurgy` (Mage) / `+1` `slaughter` (Knight) |
| **Single Combat Lethal Kill (`bm_on_character_death_duel`)** | Knight only | Slay opponent in single combat | **+1 Major** (+ **25% chance +1 Superior** if victim `prowess >= 20` or blood mage/knight) | `+5` `slaughter` (Knight) |
| **Battlefield Victory (`bm_on_combat_end_winner`)** | Knight only | Win battle as commander or knight | **10%–100% Minor** & **0%–100% Major** (scales by troop bracket) | `+1` to `+5` `vanguard` (Knight) |
| **Murder Scheme Execution (`bm_on_murder_success_hulinhjalmur`)** | Superior Hulinhjálmur | Execute successful Murder scheme | **+1 Major** | None |
| **Manifest Lifeforce (`bm_manifest_lifeforce_decision`)** | Mage & Knight | 100–1000 Piety, `piety_level >= 2`, 1-yr CD | Interaction modal popup (`bm_manifest_lifeforce_interaction`): 100p (+1 XP, 50% fail -> 4% floor, Minor/Major success), 250p (+3 XP, 25% fail -> 3% floor, 1x/2x Major success), 500p (+5 XP, guaranteed Minor upfront, 1x/2x Major or Minor consolation, zero fail), 1000p (+7 XP, guaranteed Minor & 1 Major upfront, 1x/2x Major or Superior, zero fail) | `+1` / `+3` / `+5` / `+7` `enlightenment` |
| **Condense Lifeforce (`bm_cast_blood_magic_minor_decision`)** | Mage & Knight | 100 Piety + 1 Minor Lifeforce | **-1 Minor -> +1 Major** (no exhaustion debuff) | `+2` `ancient` |
| **Condense Superior Lifeforce (`bm_cast_blood_magic_major_decision`)** | Mage & Knight | 250 Piety + 1 Minor + 1 Major, `piety_level >= 3`, 2-yr CD | **-1 Minor, -1 Major -> +1 Superior** on Learning duel (L0: 50% fail split into 33% fail / 17% crit fail, 33% succ / 17% crit succ; L10: 40% fail; L20: 30% fail; L50+: floored at 3% fail / 1% crit fail; fail refunds Major with 3-yr exhaustion) | `+3` (crit/win) / `+1` (fail) `ancient` |
| **Childbirth Milestone (`bm_on_birth_bloodline_xp`)** | Mage only | Child born to blood mage parent | **+1 Major** per child born | `+2` (`+4` inheriting; doubled by Superior Feingur) `bloodline` |
| **Go on a Blood Hunt (`seek_power_decision`)** | Mage & Knight | Free, 1-yr CD landed / 3-yr wanderer (halved by Superior Vegvísir) | **+1 Minor**, **+1 Major**, or **+1 Major + 25% +1 Superior** (Single Combat battlefield duel against escort knight or 20+ prowess traveler) | `+1` to `+5` `slaughter` / `vanguard` (Knight) or `+1` to `+5` `hematurgy` / `+1` `bloodline` / `+2` `ancient` (Mage) / `+1`–`+2` `enlightenment` / `+1` `benediction` |
| **Cast Minor Blood Magic Rites (`bm_cast_blood_magic_minor_decision`)** | Mage & Knight | `0–75` Piety + 1 Minor Lifeforce | **-1 Minor** (+ 1-yr Minor exhaustion) | `+1` `enlightenment` / `+2` `bloodline` / `+4` `ancient` |
| **Cast Major Blood Magic Rites (`bm_cast_blood_magic_major_decision`)** | Mage & Knight | `75–600` Piety + 1 Major Lifeforce | **-1 Major** (+ 3-yr Major exhaustion) | `+3` to `+5` track XP (`+10` Power XP) |
| **Cast Superior Blood Magic Rites (`bm_cast_blood_magic_superior_decision`)** | Mage & Knight | `350–1500` Piety + 1 Superior Lifeforce | **-1 Superior** (+ 3-yr Superior exhaustion) | `+5` to `+20` track XP |
| **Heal Ailments (`bm_heal_ailment`)** | Mage & Knight | `15 / 35 / 100` Piety (halved by Superior Drepsóttarstafur) | Minor: **-1 Minor**; Major: **-1 Major**; Deadly: **-1 Minor & -1 Major** | `+2` / `+4` / `+8` `benediction` (or `enlightenment`/`vanguard` on Knight) |
| **Heal Old Age (`bm_heal_old_age_trait`)** | Mage & Knight | `50 / 150` Piety | Minor (-20 XP): **-1 Minor**; Major (-50 XP / Cure): **-1 Major** | `+1` / `+2` `benediction` |
| **Inscribe Rune on Other (`bm_inscribe_rune_other_interaction`)** | Mage & Knight (Superior: Mage only) | `0 / 200 / 400` Piety + Minor/Major/Superior Lifeforce, 5-yr CD | **-1 Minor / Major / Superior** | `+4` / `+5` / `+10` `benediction` |
| **Initiate Mage / Knight (`grant_blood_magic` / `make_blood_knight`)** | Mage / Knight | `100`p + Major OR `250`p + Minor Lifeforce | **-1 Major** or **-1 Minor** | `+4` (`+5` kin) or `+2` `bloodline` / `vanguard` |
| **Ask for Blood Magic (`ask_for_blood_magic_interaction`)** | Non-Mage Actor | Actor pays `250` Piety; Teacher holds Superior Lifeforce | Teacher: **-1 Superior** | None |
| **Empower Blood Knight (`empower_blood_knight_interaction`)** | Knight only | 0 Piety + 1 Major or 1 Minor Lifeforce | Caster: **-1 Major** or **-1 Minor** | Caster: `+4`/`+2` `benediction`; Target: `+10`/`+5` `vanguard` & `slaughter` |
| **Bless Bloodline (`bm_bless_bloodline_interaction`)** | Mage & Knight | 35 Piety + 1 Minor Lifeforce | **-1 Minor** | `+2` `bloodline` (Mage) / `+2` `vanguard` (Knight) |
| **Cast Blood Curse (`bm_curse_blood_interaction`)** | Mage (>=10 Hematurgy) | 50 Piety + 1 Minor Lifeforce | **-1 Minor** (Crit success siphons **+1 Minor** back from victim) | `+2` (win) / `+4` (crit) / `+1` (fail) `hematurgy` |
| **Grant / Restore Lifeforce (`grant_lifeforce_interaction*`)** | Mage & Knight | `25–50` Piety + Minor/Major Lifeforce | Transfers stack to target or clears `lifedrained_modifier` on self or any target | `+1`/`+2` `enlightenment` or `+4` `benediction` |
| **Bleed Own Vein (`bm_bleed_own_vein_interaction`)** | Mage & Knight | Health/Stress toll, 1-yr CD | Minor: **+1 Minor** (wounded); Major: **+1 Major** (wounded_2, lifedrained_modifier, 25 stress) | Minor: `+2` `hematurgy` (Mage) / `+2` `slaughter` (Knight); Major: `+4` `hematurgy` (Mage) / `+4` `slaughter` (Knight) |
| **Purge Stress Vices (`bm_purge_coping_traits_interaction`)** | Mage & Knight | 250 Piety + 1 Major Lifeforce | **-1 Major** | `+4` `enlightenment` (self) or `+4` `benediction` (other) |

## Where the details live

| Piece | File |
| --- | --- |
| Lifeforce character modifiers | `common/modifiers/bm_lifeforce.txt` |
| Temporary exhaustion effects | `common/scripted_effects/bm_blood_magic_temporary_effects.txt` |
| Cast consumption effects (`blood_magic_used_*`) | `common/scripted_effects/bm_blood_magic_used_effects.txt` |
| Prisoner & courtier harvesting interactions | `common/character_interactions/bm_drain_lifeforce.txt` |
| Self & coping rites (`bm_bleed_own_vein_interaction`, `bm_purge_coping_traits_interaction`) | `common/character_interactions/bm_self_rites.txt` |
| Battlefield victory/defeat XP & Lifeforce effects | `common/on_action/bm_combat_on_actions.txt`, `common/scripted_effects/bm_combat_effects.txt` |
| Single combat fatality Lifeforce hook | `common/on_action/bm_duel_on_actions.txt` |
| Manifestation & distillation decisions | `common/decisions/get_lifeforce/bm_manifest_lifeforce.txt`, `events/bm_cast_blood_magic_major_events.txt` |
| Mass dungeon harvesting decision | `common/decisions/bm_mass_lifedrain_prisoners.txt` |
| Story panel Lifeforce stack recount | `common/scripted_effects/bm_blood_mage_story_list_effects.txt` (`bm_recount_lifeforce_stacks_effect`) |

## Gotchas

- **Permanent Positive Stacks:** Positive Lifeforce modifiers never expire on their own; they are only removed when consumed by `blood_magic_used_minor/major/superior` or `bm_recount_lifeforce_stacks_effect`.
- **Recounting Stacks:** Because CK3 script cannot directly query dynamic modifier stack counts, `bm_recount_lifeforce_stacks_effect` strips and re-adds positive Lifeforce modifiers in a `while` loop to update the Story Panel variables (`bm_lifeforce_minor/major/superior_stacks`). Always call `bm_recount_lifeforce_stacks_effect = yes` after directly adding or removing Lifeforce modifiers outside standard `blood_magic_used_*` macros.
