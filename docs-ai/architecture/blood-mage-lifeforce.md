# Blood Mage Lifeforce

Living technical specification for the Lifeforce resource economy, character modifiers, battlefield harvesting brackets, and spellcasting consumption.

## Overview

Core spellcasting resource stored as stacking character modifiers (`lifeforce_modifier_minor`, `lifeforce_modifier_major`, `lifeforce_modifier_superior`).
- **Passive Vitality vs Fuel:** Unspent positive stacks grant permanent buffs (Health, Life Exp, Fertility, Epidemic Res, Prowess). Casting consumes 1 positive stack and applies temporary exhaustion (`lifeforce_modifier_negative_minor/major/superior`).
- **Harvesting Asymmetry:**
  - **Blood Mages:** Childbirth (+1 Major per child), wilderness blood hunts (`seek_power_decision`), prisoner execution (`lifedrain_prisoner_event_interaction`, `mass_lifedrain_prisoners_decision`), courtier siphoning, murder schemes with Superior **Hulinhjálmur**, and spiritual distillation (`bm_manifest_lifeforce_decision`).
  - **Blood Mages (martial):** battlefield troop-bracket harvesting and lethal single combat kills (Major LF + 25% Superior chance vs worthy foes).

### Lifeforce & Exhaustion Modifiers Table (`common/modifiers/bm_lifeforce.txt`)
| Modifier Key | Role | Stacking | Duration | Mechanical Effects per Stack |
| --- | --- | --- | --- | --- |
| `lifeforce_modifier_minor` | Tier 1 Fuel | Yes | Permanent until spent | `+0.1` Health, `+1` Life Exp, `+2` Epidemic Res, `+0.1` Negate Health Penalty |
| `lifeforce_modifier_major` | Tier 2 Fuel | Yes | Permanent until spent | `+0.3` Health, `+3` Life Exp, `+6` Epidemic Res, `+0.3` Negate Health Penalty |
| `lifeforce_modifier_superior` | Tier 3 Fuel | Yes | Permanent until spent | `+0.6` Health, `+6` Life Exp, `+12` Epidemic Res, `+0.6` Negate Health Penalty |
| `lifeforce_modifier_mojo` | Lineage / Fertility Reservoir | Yes | Permanent until spent | `+10%` Fertility, `+5` Fertility Yrs, `+5%` Inactive Inheritance Chance, `+5%` Genetic Trait Chance, `+5%` Strengthen Blood Chance, `+5` Attraction Opinion |
| `lifeforce_modifier_fury` | Combat / Martial Reservoir | Yes | Permanent until spent | `+2` Prowess, `+10%` Knight Effectiveness, `+2%` Army Movement Speed, `+2` Travel Safety |
| `lifeforce_modifier_focus` | Study / Intellectual Reservoir | Yes | Permanent until spent | `+1` Learning, `-10%` Stress Gain, `+5%` Monthly Lifestyle XP Gain |
| `lifeforce_modifier_negative_minor` | Minor Exhaustion | Yes | **1 Year** (`365` days) | `-0.1` Health, `-1` Life Exp, `-2` Epidemic Res, `-0.1` Negate Health Penalty, `-1` Prowess |
| `lifeforce_modifier_negative_major` | Major Exhaustion | Yes | **3 Years** (`1095` days; `365`d on Flay/Distill) | `-0.3` Health, `-3` Life Exp, `-6` Epidemic Res, `-0.3` Negate Health Penalty, `-2` Prowess |
| `lifeforce_modifier_negative_superior` | Superior Exhaustion | Yes | **3 Years** (`1095` days; `5` yrs on Flay) | `-0.6` Health, `-6` Life Exp, `-12` Epidemic Res, `-0.6` Negate Health Penalty, `-4` Prowess |
| `lifedrained_modifier` | Victim Siphon Toll | Yes | Permanent (until restored) | `-0.5` Health, `-10` Life Exp, `-5` Epidemic Res, `-0.5` Negate Health Penalty, `-5` Prowess |
| `recently_lifedrained_modifier` | Victim Cooldown | No | **1 Year** (`years = 1`) | Blocks repeat `lifedrain_courtier_event_interaction` on the same victim |

---

## Battlefield Lifeforce & XP Scaling (`common/scripted_effects/bm_combat_effects.txt`)

Triggered on `on_combat_end_winner` (`bm_on_combat_end_winner`) for surviving side commanders and knights who have `lifestyle_blood_mage`:

| Battle Size (`num_total_troops` OR `num_enemies_killed`) | Minor Lifeforce Chance | Major Lifeforce Chance | Commander `bloodlust` XP | Knight `bloodlust` XP |
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

*Note: Surviving a battle defeat (`bm_on_combat_end_loser`) grants `+1` to `+3` `bloodlust` XP and `0` to `+2` `enlightenment` XP based on battle size, with no Lifeforce harvest.*

---

## Master Lifeforce Sources & Sinks Matrix

| Action / Hook | Class Access | Cost / Requirements | Lifeforce Delta | Track XP Gain |
| --- | --- | --- | --- | --- |
| **Execute Prisoner (`lifedrain_prisoner_event_interaction`)** | Mage | 50 Piety (`lifedrain_piety_cost_major`), un-drained prisoner | **+1 Major** (executes victim) | `+2` `hematurgy` |
| **Mass Lifedrain (`mass_lifedrain_prisoners_decision`)** | Mage | Piety per prisoner, dungeon prisoners | **+Minor / +Major** per prisoner executed | Scaled `hematurgy` |
| **Siphon Courtier/Prisoner (`lifedrain_courtier_event_interaction`)** | Mage | 25 Piety (`lifedrain_piety_cost_minor`), 3-mo CD | **+1 Minor** (victim gets `lifedrained_modifier`) | `+1` `hematurgy` |
| **Single Combat Lethal Kill (`bm_on_character_death_duel`)** | Mage | Slay opponent in single combat | **+1 Major** (+ **25% chance +1 Superior** if victim `prowess >= 20` or blood mage) | `+5` `bloodlust` |
| **Battlefield Victory (`bm_on_combat_end_winner`)** | Mage | Win battle as commander or knight | **10%–100% Minor** & **0%–100% Major** (scales by troop bracket) | `+1` to `+5` `bloodlust` |
| **Murder Scheme Execution (`bm_on_murder_success_hulinhjalmur`)** | Superior Hulinhjálmur | Execute successful Murder scheme | **+1 Major** | None |
| **Manifest Lifeforce (`bm_manifest_lifeforce_decision`)** | Mage | 100–1000 Piety, `piety_level >= 2`, 1-yr CD | Interaction modal popup (`bm_manifest_lifeforce_interaction`): 100p (+1 XP, 50% fail -> 4% floor, Minor/Major success), 250p (+3 XP, 25% fail -> 3% floor, 1x/2x Major success), 500p (+5 XP, guaranteed Minor upfront, 1x/2x Major or Minor consolation, zero fail), 1000p (+7 XP, guaranteed Minor & 1 Major upfront, 1x/2x Major or Superior, zero fail) | `+1` / `+3` / `+5` / `+7` `enlightenment` |
| **Condense Minor Lifeforce (`bm_minor_condense`)** | Mage | 150 Piety + 1 Minor Lifeforce, 6-mo CD | **-1 Minor -> +1 Major** (no exhaustion debuff) | `+2` `ancient` |
| **Condense Major Lifeforce (`bm_major_condense`)** | Mage | 350 Piety + 1 Major Lifeforce, `piety_level >= 2`, 6-mo CD | **-1 Major -> +1 Superior** (no exhaustion debuff) | `+3` `ancient` |
| **Split Superior Lifeforce (`bm_superior_split`)** | Mage | 350 Piety + 1 Superior Lifeforce, `piety_level >= 2`, 6-mo CD | **-1 Superior -> +2 Major** (no exhaustion debuff) | `+3` `ancient` |
| **Split Major Lifeforce (`bm_major_split`)** | Mage | 150 Piety + 1 Major Lifeforce, 6-mo CD | **-1 Major -> +2 Minor** (no exhaustion debuff) | `+2` `ancient` |
| **Childbirth Milestone (`bm_on_birth_bloodline_xp`)** | Mage only | Child born to blood mage parent | **+1 Major** per child born; burns 1 Mojo per parent | `+2` (`+4` inheriting; doubled by Superior Feingur) `bloodline`; `+3` per Mojo burned |
| **Channel Minor into Mojo (`bm_minor_channel_mojo`)** | Mage | 50 Piety + 1 Minor Lifeforce | **-1 Minor -> +1 Mojo** | `+1` `bloodline` |
| **Channel Major into Mojo (`bm_major_channel_mojo`)** | Mage | 100 Piety + 1 Major Lifeforce | **-1 Major -> +3 Mojo** | `+2` `bloodline` |
| **Reclaim Minor from Mojo (`bm_minor_reclaim_mojo`)** | Mage | 75 Piety + 1 Mojo Lifeforce | **-1 Mojo -> +1 Minor** | `+1` `bloodline` |
| **Channel Minor into Fury (`bm_minor_channel_fury`)** | Mage | 50 Piety + 1 Minor Lifeforce | **-1 Minor -> +1 Fury** | `+1` `bloodlust` |
| **Channel Major into Fury (`bm_major_channel_fury`)** | Mage | 100 Piety + 1 Major Lifeforce | **-1 Major -> +3 Fury** | `+2` `bloodlust` |
| **Reclaim Minor from Fury (`bm_minor_reclaim_fury`)** | Mage | 75 Piety + 1 Fury Lifeforce | **-1 Fury -> +1 Minor** | `+1` `bloodlust` |
| **Channel Minor into Focus (`bm_minor_channel_focus`)** | Mage | 50 Piety + 1 Minor Lifeforce | **-1 Minor -> +1 Focus** | `+1` `enlightenment` |
| **Channel Major into Focus (`bm_major_channel_focus`)** | Mage | 100 Piety + 1 Major Lifeforce | **-1 Major -> +3 Focus** | `+2` `enlightenment` |
| **Reclaim Minor from Focus (`bm_minor_reclaim_focus`)** | Mage | 75 Piety + 1 Focus Lifeforce | **-1 Focus -> +1 Minor** | `+1` `enlightenment` |
| **Go on a Blood Hunt (`seek_power_decision`)** | Mage | Free, 1-yr CD (halved to 6 months by Superior Vegvísir) | **+1 Minor**, **+1 Major**, or **+1 Major + 25% +1 Superior** (Single Combat battlefield duel against escort knight or 20+ prowess traveler) | `+1` to `+5` `bloodlust` / `+1` to `+5` `hematurgy` / `+1` `bloodline` / `+2` `ancient` / `+1`–`+2` `enlightenment` / `+1` `benediction` |
| **Cast Minor Blood Magic Rites (`bm_cast_blood_magic_minor_decision`)** | Mage | `0–75` Piety + 1 Minor Lifeforce | **-1 Minor** (+ 1-yr Minor exhaustion) | `+1` `enlightenment` / `+2` `bloodline` / `+4` `ancient` |
| **Cast Major Blood Magic Rites (`bm_cast_blood_magic_major_decision`)** | Mage | `75–600` Piety + 1 Major Lifeforce | **-1 Major** (+ 3-yr Major exhaustion) | `+3` to `+5` track XP (`+10` Power XP) |
| **Cast Superior Blood Magic Rites (`bm_cast_blood_magic_superior_decision`)** | Mage | `350–1500` Piety + 1 Superior Lifeforce | **-1 Superior** (+ 3-yr Superior exhaustion) | `+5` to `+20` track XP |
| **Heal Ailments (`bm_heal_ailment`)** | Mage | `15 / 35 / 100` Piety (halved by Superior Drepsóttarstafur) | Minor: **-1 Minor**; Major: **-1 Major**; Deadly: **-1 Minor & -1 Major** | `+2` / `+4` / `+8` `benediction` |
| **Heal Old Age (`bm_heal_old_age_trait`)** | Mage | `50 / 150` Piety | Minor (-20 XP): **-1 Minor**; Major (-50 XP / Cure): **-1 Major** | `+1` / `+2` `benediction` |
| **Inscribe Rune on Other (`bm_inscribe_rune_other_interaction`)** | Mage | `0 / 200 / 400` Piety + Minor/Major/Superior Lifeforce, 5-yr CD | **-1 Minor / Major / Superior** | `+4` / `+5` / `+10` `benediction` |
| **Initiate Mage (`grant_blood_magic`)** | Mage | `100`p + Major OR `250`p + Minor Lifeforce | **-1 Major** or **-1 Minor** | `+4` (`+5` kin) or `+2` `bloodline` |
| **Ask for Blood Magic (`ask_for_blood_magic_interaction`)** | Non-Mage Actor | Actor pays `250` Piety; Teacher holds Superior Lifeforce | Teacher: **-1 Superior** | None |
| **Bless Bloodline (`bm_bless_bloodline_interaction`)** | Mage | 35 Piety + 1 Minor Lifeforce | **-1 Minor** | `+2` `bloodline` |
| **Cast Blood Curse (`bm_curse_blood_interaction`)** | Mage (>=10 Hematurgy) | 50 Piety + 1 Minor Lifeforce | **-1 Minor** (Crit success siphons **+1 Minor** back from victim) | `+2` (win) / `+4` (crit) / `+1` (fail) `hematurgy` |
| **Grant / Restore Lifeforce (`grant_lifeforce_interaction*`)** | Mage | `25–50` Piety + Minor/Major Lifeforce | Transfers stack to target or clears `lifedrained_modifier` on self or any target | `+1`/`+2` `enlightenment` or `+4` `benediction` |
| **Bleed Own Vein (`bm_bleed_own_vein_interaction`)** | Mage | Health/Stress toll, 1-yr CD | Minor: **+1 Minor** (wounded); Major: **+1 Major** (wounded_2, lifedrained_modifier, 25 stress) | Minor: `+2` `hematurgy`; Major: `+4` `hematurgy` |
| **Purge Stress Vices (`bm_purge_coping_traits_interaction`)** | Mage | 250 Piety + 1 Major Lifeforce | **-1 Major** | `+4` `enlightenment` (self) or `+4` `benediction` (other) |

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
- **No Multi-Stack Triggers:** CK3 script triggers (`has_character_modifier`) can ONLY check whether a modifier exists (`>= 1` stack). There is NO native engine trigger to check for `>= 2` stacks of a stacking modifier. Never attempt or suggest triggers checking for multiple stacks of the same modifier (e.g. Lifeforce). Lifeforce transmutation loops are balanced via piety costs and timed cooldown flags (`days = 180`).
