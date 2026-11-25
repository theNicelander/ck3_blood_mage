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
| `lifeforce_modifier_radiant` | Diplomacy / Radiance Reservoir | Yes | Permanent until spent | `-5%` Short Reign, `+5%` Long Reign, `+5%` Legitimacy Gain, `+5%` Monthly Prestige Mult, `+5%` Fame Impact, `-5d` Personal Scheme Phase, `+3%` Personal Scheme Success, `+3%` Max Personal Scheme Cap, `+3` Vassal Opinion, `+3` Monthly Diplomacy Lifestyle XP |
| `lifeforce_modifier_furious` | Martial / Fury Reservoir | Yes | Permanent until spent | `+1` Prowess, `+5%` Army Movement Speed, `+5%` Raid Speed, `+5%` Army Damage, `-5%` Siege Phase Time, `+0.1%` Knight Eff per Prowess, `+0.01` Piety/Knight, `+5%` Counter Efficiency, `+3` Monthly Martial Lifestyle XP |
| `lifeforce_modifier_fortunate` | Stewardship / Fortune Reservoir | Yes | Permanent until spent | `+2%` Domain Tax Mult, `-3%` Building/District Gold Cost, `-3%` Building/District Time, `+3%` Prosperity Growth, `-3%` MaA Maintenance, `+3` Monthly Stewardship Lifestyle XP |
| `lifeforce_modifier_cunning` | Intrigue / Cunning Reservoir | Yes | Permanent until spent | `-3%` Max Enemy Hostile Scheme Cap, `-5d` Hostile Scheme Phase, `+3%` Scheme Secrecy, `+3%` Hostile Scheme Success, `+3%` Max Hostile Scheme Cap, `+5%` Scheme Discovery Chance, `+3` Dread Baseline, `+3` Monthly Intrigue Lifestyle XP |
| `lifeforce_modifier_wise` | Learning / Wisdom Reservoir | Yes | Permanent until spent | `+5%` Monthly Piety Mult, `+5%` Devotion Impact, `+3%` Monthly Lifestyle XP Mult, `-5%` Stress Gain, `+5%` Stress Loss, `+0.1%` Knight Eff per Learning, `-5d` Learn Language Phase, `+3` Monthly Learning Lifestyle XP |
| `lifeforce_modifier_ancient` | Lineage / Ancient Reservoir | Yes | Permanent until spent | `+5%` Fertility, `+5` Fertility Yrs, `+5%` Inactive Inheritance Chance, `+5%` Genetic Trait Chance, `+5%` Strengthen Blood Chance, `+5%` Monthly Renown Mult, `+3` Dynasty Opinion, `-5%` Inbreeding Chance, `+3` Attraction Opinion, `+3` Monthly Active Lifestyle XP |
| `lifeforce_modifier_negative_minor` | Minor Exhaustion | Yes | **1 Year** (`365` days) | `-0.1` Health, `-1` Life Exp, `-2` Epidemic Res, `-0.1` Negate Health Penalty, `-1` Prowess |
| `lifeforce_modifier_negative_major` | Major Exhaustion | Yes | **3 Years** (`1095` days; `365`d on Flay/Distill) | `-0.3` Health, `-3` Life Exp, `-6` Epidemic Res, `-0.3` Negate Health Penalty, `-2` Prowess |
| `lifeforce_modifier_negative_superior` | Superior Exhaustion | Yes | **3 Years** (`1095` days; `5` yrs on Flay) | `-0.6` Health, `-6` Life Exp, `-12` Epidemic Res, `-0.6` Negate Health Penalty, `-4` Prowess |
| `bm_overdrained_modifier` | Emergency Drain Strain | Yes | **2 Years** (`years = 2`) | `-0.3` Health, `-1.0` Monthly Piety, `-5%` Monthly Piety |
| `lifedrained_modifier` | Victim Siphon Toll | Yes | Permanent (until restored) | `-0.5` Health, `-10` Life Exp, `-5` Epidemic Res, `-0.5` Negate Health Penalty, `-5` Prowess |
| `recently_lifedrained_modifier` | Victim Cooldown | No | **1 Year** (`years = 1`) | Blocks repeat `drain_tithe` (Demand Blood Tithe) on the same victim (`drain_minor` uses 3-month `bm_minor_lifedrain_cooldown` on victim + escalating wounds) |

---

## Battlefield Lifeforce & XP Scaling (`common/scripted_effects/bm_combat_effects.txt`)

Triggered on `on_combat_end_winner` (`bm_on_combat_end_winner`) for surviving side commanders and knights who have `lifestyle_blood_mage`:

| Battle Size (`num_total_troops` OR `num_enemies_killed`) | Minor Lifeforce Chance | Major Lifeforce Chance | Commander `fury` XP | Knight `fury` XP |
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

*Note: Surviving a battle defeat (`bm_on_combat_end_loser`) grants `+1` to `+3` `fury` XP and `0` to `+2` `wisdom` XP based on battle size, with no Lifeforce harvest.*

---

## Master Lifeforce Sources & Sinks Matrix

| Action / Hook | Class Access | Cost / Requirements | Lifeforce Delta | Track XP Gain |
| --- | --- | --- | --- | --- |
| **Execute Prisoner (`bm_blood_drain_interaction`: Major / Major Overdrained)** | Mage | 50 Piety (`lifedrain_piety_cost_major`) OR 0 Piety (`drain_major_overdrained`: 2-yr stackable `bm_overdrained_modifier`, `+20` Stress, `wounded_1` if uninjured), un-drained prisoner | **+1 Major** (executes victim) | `+3` `cunning` |
| **Blood Pit Duel (`bm_blood_drain_interaction`: Blood Pit Duel)** | Mage | 50 Piety, `20+` Prowess prisoner, both `can_start_single_combat_trigger` | Win: **+1 Major** + **`Prowess%` chance +1 Superior** (`bm_duel_victory_lifeforce_effect`); Loss: **+1 Minor** (caster wounded, `+20` Stress, prisoner escapes) | Win: `+4` `fury`; Loss: `+1` `fury` |
| **Mass Lifedrain (`mass_lifedrain_prisoners_decision`)** | Mage | Piety per prisoner, dungeon prisoners | **+Minor / +Major** per prisoner executed | Scaled `cunning` |
| **Siphon Target (`bm_blood_drain_interaction`: Minor / Empowered Minor)** | Mage | `20` Piety (Minor) or `100` Piety (Empowered Minor, non-prisoner only), 3-mo victim CD | **+1 Minor** (prisoners auto-succeed; non-prisoners contest Intrigue + Learning duel, `50%` / `80%` base at 0 diff, `~90%` at `+30`, `-20` weight outside court; fail: 3-mo CD, `-25` opinion, `+20` Stress) | `+1` `cunning` |
| **Single Combat Lethal Kill (`bm_on_character_death_duel`)** | Mage | Slay opponent in single combat | **+1 Major** + **`Prowess%` chance +1 Superior** (`bm_duel_victory_lifeforce_effect`) | `+5` `fury` |
| **Battlefield Victory (`bm_on_combat_end_winner`)** | Mage | Win battle as commander or knight | **10%–100% Minor** & **0%–100% Major** (scales by troop bracket) | `+1` to `+5` `fury` |
| **Murder Scheme Execution (`bm_on_murder_success_hulinhjalmur`)** | Superior Hulinhjálmur | Execute successful Murder scheme | **+1 Major** | None |
| **Manifest Lifeforce (`bm_manifest_lifeforce_decision`)** | Mage | 100–1000 Piety, `piety_level >= 2`, 1-yr CD | Interaction modal popup (`bm_manifest_lifeforce_interaction`): 100p (+2 XP, nothing guaranteed, 50% fail -> 4% floor, Minor/Major success), 250p (+3 XP, guaranteed Minor upfront, 25% fail -> 3% floor, 1x/2x Major success), 500p (+5 XP, guaranteed Major upfront, 1x/2x Major or Minor, zero fail), 1000p (+7 XP, guaranteed Minor & 1 Major upfront, 1x/2x Major or Superior, zero fail) | `+2` / `+3` / `+5` / `+7` `wisdom` |
| **Condense Minor Lifeforce (`bm_minor_condense`)** | Mage (`bm_cast_blood_magic_minor_decision`) | 100 Piety + 1 Minor Lifeforce, 6-mo CD | **-1 Minor -> +1 Major** (no exhaustion debuff) | `+2` `ancient` |
| **Condense Major Lifeforce (`bm_major_condense`)** | Mage (`bm_cast_blood_magic_major_decision`) | 250 Piety + 1 Major Lifeforce, `piety_level >= 2`, 6-mo CD | **-1 Major -> +1 Superior** (no exhaustion debuff) | `+3` `ancient` |
| **Split Superior Lifeforce (`bm_superior_split`)** | Mage (`bm_cast_blood_magic_superior_decision`) | 350 Piety + 1 Superior Lifeforce, `piety_level >= 2`, 6-mo CD | **-1 Superior -> +2 Major** (no exhaustion debuff) | `+3` `ancient` |
| **Split Major Lifeforce (`bm_major_split`)** | Mage (`bm_cast_blood_magic_major_decision`) | 50 Piety + 1 Major Lifeforce, 6-mo CD | **-1 Major -> +2 Minor** (no exhaustion debuff) | `+2` `ancient` |
| **Burn Lifeforce (`bm_minor/major/superior_burn_lifeforce`)** | Mage (`bm_cast_blood_magic_*_decision`) | 1 Minor / Major / Superior Lifeforce, 180d per-tier CD | **-1 Minor / Major / Superior -> +50 / +150 / +300 Piety** (+ standard tier exhaustion) | None |
| **Childbirth Milestone (`bm_on_birth_fortune_xp`)** | Mage only | Child born to blood mage parent | **+1 Major** per child born; burns 1 Mojo per parent | `+2` (`+4` inheriting; doubled by Superior Feingur) `fortune`; `+3` per Mojo burned |
| **Transmute Major -> Reservoir (`bm_transmute_lifeforce.0002`)** | Mage (`bm_transmute_lifeforce_decision`) | 50 Piety + 1 Major Lifeforce | **-1 Major -> +1 Reservoir** (`radiant`, `furious`, `fortunate`, `cunning`, `wise`, `ancient`) | `+1` `ancient` (Ancient Blood) / `+2` matching track (others) |
| **Reclaim Major from Reservoir (`bm_transmute_lifeforce.0004`)** | Mage (`bm_transmute_lifeforce_decision`) | 50 Piety + 1 Reservoir stack | **-1 Reservoir -> +1 Major** (`radiant`, `furious`, `fortunate`, `cunning`, `wise`, `ancient`) | None |
| **Go on a Blood Hunt (`seek_power_decision`)** | Mage | Free, 1-yr CD (halved to 6 months by Superior Vegvísir) | **+1 Minor**, **+1 Major**, or **+1 Major + `Prowess%` +1 Superior** (`bm_duel_victory_lifeforce_effect` on Single Combat battlefield duel) | `+1` to `+5` `fury` / `+1` to `+5` `cunning` / `+1` `fortune` / `+2` `ancient` / `+1`–`+2` `wisdom` / `+1` `radiance` |
| **Cast Minor Blood Magic Rites (`bm_cast_blood_magic_minor_decision`)** | Mage | `0–75` Piety + 1 Minor Lifeforce | **-1 Minor** (+ 1-yr Minor exhaustion) | `+1` `wisdom` / `+2` `fortune` / `+4` `ancient` |
| **Cast Major Blood Magic Rites (`bm_cast_blood_magic_major_decision`)** | Mage | `75–600` Piety + 1 Major Lifeforce | **-1 Major** (+ 3-yr Major exhaustion) | `+3` to `+5` track XP |
| **Cast Superior Blood Magic Rites (`bm_cast_blood_magic_superior_decision`)** | Mage | `350–1500` Piety + 1 Superior Lifeforce | **-1 Superior** (+ 3-yr Superior exhaustion) | `+5` to `+20` track XP |
| **Heal Ailments (`bm_heal_ailment`)** | Mage | `15 / 35 / 100` Piety (halved by Superior Drepsóttarstafur) | Minor: **-1 Minor**; Major: **-1 Major**; Deadly: **-1 Minor & -1 Major** | `+2` / `+4` / `+8` `radiance` |
| **Heal Old Age (`bm_heal_old_age_trait`)** | Mage | `50 / 150` Piety | Minor (-20 XP): **-1 Minor**; Major (-50 XP / Cure): **-1 Major** | `+1` / `+2` `radiance` |
| **Inscribe Rune on Other (`bm_inscribe_rune_other_interaction`)** | Mage | `0 / 200 / 400` Piety + Minor/Major/Superior Lifeforce, 5-yr CD | **-1 Minor / Major / Superior** | `+4` / `+5` / `+10` `radiance` |
| **Initiate Mage (`grant_blood_magic`)** | Mage | `100`p + Major OR `250`p + Minor Lifeforce | **-1 Major** or **-1 Minor** | `+4` (`+5` kin) or `+2` `fortune` |
| **Ask for Blood Magic (`ask_for_blood_magic_interaction`)** | Non-Mage Actor | Actor pays `250` Piety; Teacher holds Superior Lifeforce | Teacher: **-1 Superior** | None |
| **Bless Bloodline (`bm_bless_bloodline_interaction`)** | Mage | 35 Piety + 1 Minor Lifeforce | **-1 Minor** | `+2` `fortune` |
| **Cast Blood Curse (`bm_curse_blood_interaction`)** | Mage (>=10 Cunning) | 50 Piety + 1 Minor Lifeforce | **-1 Minor** (Crit success siphons **+1 Minor** back from victim) | `+2` (win) / `+4` (crit) / `+1` (fail) `cunning` |
| **Grant / Restore Lifeforce (`grant_lifeforce_interaction*`)** | Mage | `25–50` Piety + Minor/Major Lifeforce | Transfers stack to target or clears `lifedrained_modifier` on self or any target | `+1`/`+2` `wisdom` or `+4` `radiance` |
| **Bleed Own Vein (`bm_bleed_own_vein_interaction`)** | Mage | Health/Stress toll, 1-yr CD | Minor: **+1 Minor** (+1 wound tier); Major: **+1 Major** (+2 wound tiers, 25 stress; blocked at `wounded_2`/`3`) | Minor: `+2` `cunning`; Major: `+4` `cunning` |
| **Seek Captive Brokers (`bm_buy_captives_decision`)** | Mage | Gold (`30 + 5*Prowess + 50` if `20+` Prowess + stacking per-trait surcharges: `+50/+100/+150` tiered genetic, `+75` `fecund`/`giant`/`pure_blooded`, `+150` Blood Mage, `+25` per drainable commander/lifestyle/fame trait), 1-yr CD (90-day walk-away CD) | Spawns `1–3` random captives (`bm_buy_captives.0001`/`.0002`/`.0003`, Stewardship-scaled: `60/20/20%` at `10`, `20/60/20%` at `20`, `0/50/50%` at `30`, `0/0/100%` at `50`); per-candidate pay full price or Stewardship haggle gamble (`70%` / `125%` / refused) | `+2` `fortune` per captive |
| **Purge Stress Vices (`bm_purge_coping_traits_interaction`)** | Mage | 250 Piety + 1 Major Lifeforce | **-1 Major** | `+4` `wisdom` (self) or `+4` `radiance` (other) |

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
| Transmute Lifeforce decision | `common/decisions/cast_magic/bm_transmute_lifeforce_decision.txt` |
| Mass dungeon harvesting decision | `common/decisions/bm_mass_lifedrain_prisoners.txt` |
| Story panel Lifeforce stack recount | `common/scripted_effects/bm_blood_mage_story_list_effects.txt` (`bm_recount_lifeforce_stacks_effect`) |

## Gotchas

- **Permanent Positive Stacks:** Positive Lifeforce modifiers never expire on their own; they are only removed when consumed by `blood_magic_used_minor/major/superior` or `bm_recount_lifeforce_stacks_effect`.
- **Recounting Stacks:** Because CK3 script cannot directly query dynamic modifier stack counts, `bm_recount_lifeforce_stacks_effect` strips and re-adds positive Lifeforce modifiers in a `while` loop to update the Story Panel variables (`bm_lifeforce_minor/major/superior_stacks`, plus `presence/fury/prosperity/shadows/focus/mojo`). It is called on-demand by `bm_refresh_blood_magic_rosters_effect` when opening or refreshing the Story Panel, so individual Lifeforce add/remove sites do not need to call it.
- **No Multi-Stack Triggers:** CK3 script triggers (`has_character_modifier`) can ONLY check whether a modifier exists (`>= 1` stack). There is NO native engine trigger to check for `>= 2` stacks of a stacking modifier. Never attempt or suggest triggers checking for multiple stacks of the same modifier (e.g. Lifeforce). Lifeforce transmutation loops are balanced via piety costs and timed cooldown flags (`days = 180`).
