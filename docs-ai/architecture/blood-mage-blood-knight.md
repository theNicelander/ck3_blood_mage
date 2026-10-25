# Blood Mage: Blood Knight

Living technical specification for the Blood Knight subsystem (`lifestyle_blood_knight`).

## Overview

Permanent, Devotion-anchored martial endgame peer (`lifestyle_blood_knight`) to `lifestyle_blood_mage` (*Fire and Sword* vs *Shepherd of the Faithful*).
- **Traits & Base:** `gfx/interface/icons/traits/bm_blood_knight.dds`. Base: `same_opinion = 10`, `ruler_designer_cost = 50`. Inheritable (`25%` single parent, `100%` both, `0.20%` spontaneous birth), scaled by `bm_blood_knight_prevalence` rule. Mutually exclusive with `lifestyle_blood_mage` (dual-wielding reserved for Egill Skallagrímsson).
- **Acquisition:**
  - `make_blood_knight_interaction`: Initiated by a fellow Blood Knight (`100` Piety + Major Lifeforce or `250` Piety + Minor Lifeforce) on spouse, child, kin, knight, or courtier. Awards `+4` Vanguard XP (`+5` for child or dynasty kin).
  - **Geyser Duel Initiation (`bm_geyser_duel.0001`):** Travel to Reykjavik or Tsushima via `bm_blood_cultist_become_blood_mage_decision` or `bm_enhance_blood_ritual_decision` (`piety_level >= 2`). Prowess duel costs 1 Devotion level (`add_piety_level = -1`) and grants `lifestyle_blood_knight` on win.
- **Apex Devotion & Milestones:** Shared 100 XP capstones (`ancient`, `enlightenment`, `benediction`) grant Devotion scaling (`+50%` Devotion Impact, `+2` Learning/Diplomacy per Devotion level). All 5 tracks grant `no_prowess_loss_from_age = yes` at 100 XP. Standard Vitality steps (`+0.1` Health, `+2.5` Life Exp, `+1.25` Fertility Yr, `+1` Epidemic Res) apply at tiers 10–40 and 60–90 (4× at 50 XP, 8× at 100 XP).

---

## Harvesting & Advancement

- **Battlefield Victory (`bm_on_combat_end_winner`):** As commander or knight: `+1` to `+5` `vanguard` XP; rolls troop-scaled Lifeforce (`10%–100%` Minor, `0%–100%` Major across `<100` to `10,000+` troops).
- **Battlefield Defeat (`bm_on_combat_end_loser`):** As commander or knight: `+1` to `+3` `vanguard` XP, `0` to `+2` `enlightenment` XP.
- **Fatal Single Combat (`bm_on_character_death_duel`):** Slaying a foe grants `+5` `slaughter` XP and 1 Major Lifeforce. If foe has `prowess >= 20` or holds Mage/Knight trait: 25% chance of 1 Superior Lifeforce.
- **Tournament Completion (`bm_on_travel_activity_complete_tournament`):** `+3` `slaughter` XP.
- **Yearly Ambient Pulse (`blood_mage_yearly_events.004`):** Passive ~33% chance/year for 1 Minor Lifeforce + `+1` `ancient` XP. Exclusive to Blood Knights.
- **Empower Blood Knight (`empower_blood_knight_interaction`):** Cast on spouse, child, kin, knight, courtier:
  - Major LF: `+10` `vanguard` and `slaughter` XP to target; `+4` `benediction` to caster.
  - Minor LF: `+5` `vanguard` and `slaughter` XP to target; `+2` `benediction` to caster.
- **Court & Dungeon Interactions:**
  - `lifedrain_courtier_event_interaction`: Prowess duel siphon (`25` Piety, 3-mo CD) -> 1 Minor Lifeforce + `+1` `slaughter` XP.
  - `trait_drain_prisoner_event_interaction`: Steal congenital traits up to Rank 5 (`100–325` Piety + Major Lifeforce) -> `+2` `slaughter` XP.
  - `bm_bless_bloodline_interaction`: Bless child, kin, knight, courtier (`35` Piety + Minor LF for 10-yr buff; `50` Piety for permanent Feingur) -> `+1` `benediction` XP. **Blood of Iron** (`bm_blessed_blood_iron_modifier`: `+2` Martial, `+4` Prowess, `+25%` Knight Effectiveness, `+1.0` Health, `+0.50` Negate Health Penalty for 10 yrs) serves as the unified champion blessing.
  - `bm_ritual_spar_decision`: Annual courtyard practice duel (SCE, non-lethal, 1 Minor LF, 1-yr CD). Samples up to 3 candidates weighted by prowess ($w_i = 	ext{prowess}_i$). Victor: 1 Major LF + `+3` Vanguard/Hematurgy XP; Loser: `+1` Vanguard/Enlightenment XP; Both: `+20` Blademaster XP, `+15` opinion.
  - `bm_cull_champion_interaction`: Blood sacrifice of prowess >= 12 prisoner / Blood Knight prisoner or broken follower (`50` Piety) -> Executes target (`death_lifedrain_reason`), yields 1 Major LF, `+3` `slaughter` (Knight) / `+3` `hematurgy` (Mage) XP, and rolls `1 × prowess` chance (max 50%) for 1 Superior Lifeforce.
  - `bm_inscribe_rune_other_interaction`: Carve Minor (`+4` `benediction` XP) or Major (`+5` `benediction` XP) runes onto courtiers, kin, knights, or golems.
  - `bm_heal_ailment`: Heals 32 conditions, 5 old-age traits, and 11 coping vices.
- **Grimoires & Spells:** Full access to Minor (`bm_cast_blood_magic_minor`), Major (`bm_cast_blood_magic_major`), and Superior (`bm_cast_blood_magic_superior`) Blood Magic, including Education (1★–5★), Congenital manifestation (Ranks 1–5), Blood Golems, and Runes. See [`blood-mage-magic-tiers.md`](blood-mage-magic-tiers.md).

### Blood Hunt Encounters (`seek_power_decision`)

Cooldown: 1 yr landed, 3 yrs wanderer (halved by Superior **Vegvísir**). Available to Knights and Mages (not traveling, not in activity, not imprisoned, not incapable). 20%–50% prowess-scaled chance (`bm_seek_power_traveler_chance_value`) for Lonely Road (`.003`), falling back to a 6-way encounter roll:

| Encounter | Duel / Check | Outcomes & Rewards |
| --- | --- | --- |
| Royal Stag (`seek_power.002`) | Auto | **1 Minor Lifeforce**, `+1` `slaughter` (Knight) / `+1` `hematurgy` (Mage) XP. |
| Beast's Lair (`seek_power.008`) | Prowess+Martial vs 20 | **Success:** 1 Major LF, `+25` Prestige, `+2` `slaughter`/`hematurgy` XP.<br>**Mixed:** 1 Minor LF, Wounded, `+10` Stress, `+1` `vanguard`/`ancient` XP.<br>**Fail / Crit Fail:** `0` LF, `+5` to `+20` Stress, Wounded.<br>**Option B:** Safe harvest -> 1 Minor LF, `+1` `ancient` XP. |
| Edge of Woods (`seek_power.009`) | Prowess+Intrigue+Martial vs 20 | **Success:** 1 Major LF, `+2` `slaughter`/`hematurgy` XP.<br>**Mixed:** 1 Minor LF, Wounded, `+10` Stress, `+5` Dread, `+1` `slaughter`/`hematurgy` XP.<br>**Fail / Crit Fail:** `0` LF, `+5` to `+20` Stress, Wounded, `-15` Prestige.<br>**Option B:** Blood tithe -> 1 Minor LF, `+1` `benediction` XP. |
| Lonely Road (`seek_power.003`) | Spawns `traveller_character_template` (Prowess 8–18) + `bm_escort_knight_character_template` (Prowess 10–15) | **Bout (`.003.knight`):** Crit Win -> 1 Major LF, `+3` XP; Win -> 1 Minor LF, `+2` XP; Spar -> `+1` `vanguard`/`hematurgy` XP.<br>**Lifedrain (`.003.a`):** Prowess+Learning vs 20 -> 1 Major LF, `+3` XP.<br>**SCE Duel (`.006`):** `prowess >= 25`, fatal SCE -> 1 Major LF, `+5` XP, 25% chance of 1 Superior LF (or spare/recruit).<br>**Recruit:** Persuade traveler (`+1` `enlightenment` XP) or recruit escort (`+2` `vanguard`/`ancient` XP). |
| Outlaw Camp (`seek_power.010`) | Prowess+Martial vs 20 | **Success:** 1 Major LF, `+25` Gold, `+2` `slaughter`/`hematurgy` XP.<br>**Mixed:** 1 Minor LF, Wounded, `+10` Gold, `+10` Stress, `+1` `vanguard`/`hematurgy` XP.<br>**Fail / Crit Fail:** `0` LF, `-25` Gold, `+5` to `+20` Stress.<br>**Option B:** Tribute -> 1 Minor LF, `+15` Gold, `+5` Dread, `+1` `vanguard`/`bloodline` XP. |
| Crimson Rite (`seek_power.011`) | Prowess+Learning vs 20 | **Success:** 1 Major LF, `+2` `slaughter`/`hematurgy` XP.<br>**Mixed:** 1 Minor LF, Wounded, `+15` Stress, `+1` `vanguard`/`hematurgy` XP.<br>**Fail / Crit Fail:** `0` LF, `-50` Piety, `+5` to `+20` Stress.<br>**Option B:** Chalice -> 1 Minor LF, `+50` Piety, `+2` `enlightenment` XP. |
| Sacrificial Cairn (`seek_power.004`) | Auto | **1 Major Lifeforce**, `+2` `enlightenment` XP, `+1` `ancient` XP. |

---

## Blood Magic Men-at-Arms Regiments (`common/men_at_arms_types/bm_men_at_arms_types.txt`)

Recruited by Blood Mages and Blood Knights. Visible when unavailable (`should_show_when_unavailable`), uncapped `max_regiments`, excluded from mercenaries (`allowed_in_hired_troops = no`).

| Regiment | Key & Archetype | Stack | Stats (Dmg / Tough / Pur / Scr / Siege) | Counters | Terrain & Winter Modifiers | Costs & Requirements |
| --- | --- | --- | --- | --- | --- | --- |
| **Blood Berserkers** | `bm_blood_berserkers`<br>`heavy_infantry`<br>Icon: `varangian_veterans` | `100` | `60` / `20` / `20` / `0` / `0.10` | • Pikemen (`1.5`)<br>• Skirmishers (`1.0`)<br>• Archers (`1.0`) | • **Taiga / Forest / Mountains:** `+12` Dmg, `+8` Pur<br>• **Mild & Harsh Winter:** `+10` Dmg, `+5` Tough<br>• **Desert / Floodplains:** `-8` Dmg, `-4` Tough | • **Unlock:** Devotion 2+ (`piety_level >= 2`)<br>• **Buy:** `250` Piety<br>• **Maint:** `1.50` / `0.50` Piety/mo (Raised / Unraised)<br>• **Provisions:** `7` (`@provisions_cost_infantry_moderate`) |
| **Blood-Bound Behemoths** | `bm_blood_behemoths`<br>`elephant_cavalry`<br>Icon: `war_elephants` | `25`<br>*(Hired: 10)* | `210` / `80` / `0` / `0` / `0.25` | • Heavy Infantry (`2.0`)<br>• Pikemen (`2.0`) | • **Mountains / Desert Mountains / Hills / Drylands:** `+15` Tough<br>• **Winter / Desert:** No combat penalty (`0` drain)<br>• **Wetlands:** `-30` Dmg, `-15` Tough | • **Unlock:** Devotion 4+ (`piety_level >= 4`)<br>• **Buy:** `400` Piety<br>• **Maint:** `1.50` / `0.50` Piety/mo (Raised / Unraised)<br>• **Provisions:** `0` |

---

## Exclusive Tracks

Complete track catalog and shared tracks live in [`blood-mage-track-xp-knight.md`](blood-mage-track-xp-knight.md) and [`blood-mage-track-xp.md`](blood-mage-track-xp.md).

| Track | Focus | Step Bonus (Tiers 10–40, 60–90) | 50 XP Milestone | 100 XP Capstone |
| --- | --- | --- | --- | --- |
| **`vanguard`** | Army Command & Speed | `+1` Advantage (tiers 20–40, 60–90), `+1.75%` Army Speed (`+1` Martial at 20, 40, 60, 80) | 4× Vitality + `+3` Advantage, `+7%` Army Speed, `+2` Martial, `+1` Martial per Piety Level | 8× Vitality + `+7` Advantage, `+14%` Army Speed, `+4` Martial, `+1.5` Martial per Piety Level, `no_prowess_loss_from_age = yes` |
| **`slaughter`** | Lethality & Knights | `+1.5` or `+2` Prowess, `+1` Knight Limit (tiers 20–40, 60–90), `+8.75%` Knight Effectiveness | 4× Vitality + `+7` Prowess, `+3` Knight Limit, `+35%` Knight Effectiveness, `+1` Prowess per Piety Level | 8× Vitality + `+14` Prowess, `+7` Knight Limit, `+70%` Knight Effectiveness, `+2` Prowess per Piety Level, `no_prowess_loss_from_age = yes` |

---

## Where the details live

| Concept | File |
| --- | --- |
| Trait definition & tracks | `common/traits/bm_blood_knight_trait.txt` |
| Lifecycle & prevalence effects | `common/scripted_effects/bm_blood_mage_lifecycle_effects.txt` |
| Prevalence game rule | `common/game_rules/bm_game_rules.txt` (`bm_blood_knight_prevalence`) |
| Make & empower interactions | `common/character_interactions/bm_blood_knight_interactions.txt` |
| Knight rites & sparring | `common/character_interactions/bm_knight_rites.txt` |
| Healing & ailment removal | `common/character_interactions/bm_cure_illness_interactions.txt`, `events/bm_heal_ailment_events.txt` |
| Superior magic decision & events | `common/decisions/cast_magic/bm_cast_blood_magic_superior.txt`, `events/bm_cast_blood_magic_superior_events.txt` |
| Combat on-actions & effects | `common/on_action/bm_combat_on_actions.txt`, `common/scripted_effects/bm_combat_effects.txt` |
| Duel fatality & Superior harvest | `common/on_action/bm_duel_on_actions.txt` |
| Yearly pulse | `events/bm_yearly_events.txt` (`blood_mage_yearly_events.004`) |
| Blood Magic Men-at-Arms | `common/men_at_arms_types/bm_men_at_arms_types.txt`, `localization/english/bm_men_at_arms_l_english.yml` |
