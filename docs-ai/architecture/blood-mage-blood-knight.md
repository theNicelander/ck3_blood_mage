# Blood Mage: Blood Knight

Living technical specification for the Blood Knight subsystem (`lifestyle_blood_knight`).

## Executive Summary

- **What:** Permanent, Devotion-anchored martial endgame peer (`lifestyle_blood_knight`) to `lifestyle_blood_mage`, modeled after CK3 1.20's *Proclaim the Living Word* split (*Fire and Sword* vs. *Shepherd of the Faithful*). Features 5 tracks: 2 exclusive martial tracks (`vanguard`, `slaughter`) and 3 shared Devotion tracks (`ancient`, `benediction`, `enlightenment`), max 100 XP each.
- **Icon & Base Stats:** `bm_blood_knight.dds` (`gfx/interface/icons/traits/bm_blood_knight.dds`). Base: `same_opinion = 10`, `ruler_designer_cost = 50`. Inheritable (`25%` single parent, `100%` both; `0.20%` birth) scaled by campaign game rule `bm_blood_knight_prevalence`. Mutually exclusive with `lifestyle_blood_mage` (dual-wielding preserved only for historical Egill Skallagrímsson).
- **How to acquire:**
  - `make_blood_knight_interaction`: Initiated by a fellow Blood Knight (`100` Piety + Major Lifeforce OR `250` Piety + Minor Lifeforce) on a spouse, child, family member, sworn knight, or courtier. Awards `+4` Vanguard XP (`+5` if child or dynasty kin).
  - **Geyser Duel Initiation (`bm_geyser_duel.0001`):** Travel to Reykjavik or Tsushima via `bm_blood_cultist_become_blood_mage_decision` or `bm_enhance_blood_ritual_decision` (requires `piety_level >= 2`). Choosing the Prowess duel costs **1 Devotion level** (`add_piety_level = -1`) and bestows `lifestyle_blood_knight` upon victory.
- **Apex Devotion Capstones:** The 100 XP capstones of all 3 shared tracks (`ancient`, `enlightenment`, `benediction`) grant massive Devotion-scaling powers (`+50%` Devotion Impact on `ancient`, `+2` Learning per Devotion level on `enlightenment`, and `+2` Diplomacy per Devotion level on `benediction`).
- **Track Milestones & Cleanliness:** Vitality baselines (`+0.1` Health, `+2.5` Life Expectancy, `+1.25` Year Fertility, `+1` Epidemic Resistance) apply at standard tiers (10–40, 60–90) and are skipped at 50 XP and 100 XP milestones. Every track capstone at 100 XP grants `no_prowess_loss_from_age = yes`.

### How Blood Knights Harvest Lifeforce & Advance Tracks
- **Battlefield Victory (`bm_on_combat_end_winner`):** Surviving a battle as commander or knight awards `+1` to `+5` `vanguard` XP and rolls troop-scaled Lifeforce (`10%–100%` Minor Lifeforce and `0%–100%` Major Lifeforce across `<100` to `10,000+` troop brackets).
- **Battlefield Defeat Survival (`bm_on_combat_end_loser`):** Surviving a defeat as commander or knight awards `+1` to `+3` `vanguard` XP and `0` to `+2` `enlightenment` XP.
- **Fatal Single Combat Duels (`bm_on_character_death_duel`):** Slaying a foe in single combat grants `+5` `slaughter` XP and **1 Major Lifeforce**. Slaying a foe with `prowess >= 20` or holding `lifestyle_blood_mage`/`lifestyle_blood_knight` has a **25% chance to yield 1 Superior Lifeforce** directly.
- **Tournament Completion (`bm_on_travel_activity_complete_tournament`):** Completing a tournament (`activity_tournament`) awards `+3` `slaughter` XP.
- **Ambient Yearly Pulse (`blood_mage_yearly_events.004`):** Passive **~33% chance per year** to condense 1 Minor Lifeforce ambiently, alongside passive `+1` `ancient` XP (plus attunement rolls). Strictly exclusive to `lifestyle_blood_knight`.
- **Empower Blood Knight (`empower_blood_knight_interaction`):** Fellow Blood Knight empowers a Blood Knight spouse, child, family member, sworn knight, or courtier:
  - Major Lifeforce: `+10` XP to both `vanguard` and `slaughter` on target; `+4` `benediction` XP to caster.
  - Minor Lifeforce: `+5` XP to both `vanguard` and `slaughter` on target; `+2` `benediction` XP to caster.
- **Go on a Blood Hunt (`seek_power_decision`):** Martial and occult wilderness expedition harvesting Lifeforce, martial, and discipline XP (`365`d cooldown landed, `1095`d unlanded/wanderer; halved by Superior **Vegvísir**). Available to both Blood Knights and Blood Mages who are not travelling, not participating in another activity, not imprisoned, and not incapable. Features a 20%–50% prowess-scaled chance (`bm_seek_power_traveler_chance_value`, equal to Prowess score clamped to min 20% max 50%) for the traveler encounter (`.003`), falling back to a 6-way pure Prowess encounter duel:
  - **The Stag's Last Stand (`seek_power.002`):** Run down and slaughter a royal stag for **1 Minor Lifeforce** + `+1` `slaughter` XP (Knight) / `+1` `hematurgy` XP (Mage).
  - **The Beast's Lair (`seek_power.008`):** Slay a monstrous apex predator in its den via Prowess+Martial duel vs `20` benchmark (~60% total success at 20 skill, ~70% at 25, ~80% at 30):
    - *Success:* **1 Major Lifeforce**, `+25` Prestige, `+2` `slaughter`/`hematurgy` XP.
    - *Mixed:* **1 Minor Lifeforce**, Wounded (`increase_wounds_no_death_effect`), `+10` Stress, `+1` `vanguard`/`ancient` XP.
    - *Fail:* Beast breaks away, `0` Lifeforce, `+5` Stress.
    - *Critical Fail:* Savagely mauled, Wounded, `0` Lifeforce, `+20` Stress, `-25` Prestige.
    - *Option B:* Safe carcass harvest for **1 Minor Lifeforce** + `+1` `ancient` XP.
  - **The Edge of the Woods (`seek_power.009`):** Stalk an isolated homestead via Prowess+Intrigue+Martial duel vs `20` benchmark:
    - *Success:* **1 Major Lifeforce**, `+2` `slaughter`/`hematurgy` XP.
    - *Mixed:* **1 Minor Lifeforce**, Wounded, `+10` Stress, `+5` Dread, `+1` `slaughter`/`hematurgy` XP.
    - *Fail:* Barred doors, `0` Lifeforce, `+5` Stress.
    - *Critical Fail:* Cornered by defenders, Wounded, `0` Lifeforce, `+20` Stress, `-15` Prestige.
    - *Option B:* Orderly blood tithe for **1 Minor Lifeforce** + `+1` `benediction` XP.
  - **Blades on the Lonely Road (`seek_power.003`):** Spawns a wandering warrior (`traveller_character_template`, Learning `10–18`, Prowess `8–18`, Martial `8–16`) accompanied by a sworn escort knight (`bm_escort_knight_character_template`, prowess `10–15`) for **both Blood Mages and Blood Knights**. Both spawn with player culture and county/player faith.
    - *Bout for Blood (`seek_power.003.knight`):* Prowess skill duel against the traveler: Crit Win awards **1 Major Lifeforce** + `+3` `slaughter`/`hematurgy` XP; Win awards **1 Minor Lifeforce** + `+2` `slaughter`/`hematurgy` XP; Spar awards `+1` `vanguard`/`hematurgy` XP; Escape awards `0` Lifeforce.
    - *Lifedrain (`seek_power.003.a`):* Prowess+Learning duel vs `20` benchmark against the traveler: Silent harvest drains lifeblood and awards **1 Major Lifeforce** + `+3` `slaughter`/`hematurgy` XP.
    - *Battlefield Single Combat Duel (`seek_power.003.battlefield_duel` -> `seek_power.006`):* Open to both classes (`prowess >= 25`, Single Combat Engine, `FATALITY = possible`, `LOCALE = battlefield`). Victory allows harvesting **1 Major Lifeforce**, `+5` `slaughter`/`hematurgy` XP, and a **25% chance of 1 Superior Lifeforce**—or sparing and attempting to recruit the warrior via a Prowess duel (Win: recruit courtier, `+2` `vanguard`/`ancient` XP, **1 Minor Lifeforce**; Fail: warrior refuses fealty and departs with no rewards).
    - *Recruitment:* Persuade traveler via Learning duel (`+1` `enlightenment` XP) or recruit escort knight via Prowess duel (`+2` `vanguard`/`ancient` XP).
  - **Blood in the Embers (`seek_power.010`):** Ambush an outlaw camp via Prowess+Martial duel vs `20` benchmark:
    - *Success:* **1 Major Lifeforce**, `+25` Gold, `+2` `slaughter`/`hematurgy` XP.
    - *Mixed:* **1 Minor Lifeforce**, Wounded, `+10` Gold, `+10` Stress, `+1` `vanguard`/`hematurgy` XP.
    - *Fail:* Brigands scatter, `0` Lifeforce, `0` Gold, `+5` Stress.
    - *Critical Fail:* Overpowered and robbed, Wounded, `0` Lifeforce, `-25` Gold, `+20` Stress, `-25` Prestige.
    - *Option B:* Extort tribute for **1 Minor Lifeforce**, `+15` Gold, `+5` Dread, `+1` `vanguard`/`bloodline` XP.
  - **The Crimson Rite (`seek_power.011`):** Usurp a rival occultist's ritual via Prowess+Learning duel vs `20` benchmark:
    - *Success:* **1 Major Lifeforce**, `+2` `slaughter`/`hematurgy` XP.
    - *Mixed:* **1 Minor Lifeforce**, Wounded, `+15` Stress, `+1` `vanguard`/`hematurgy` XP.
    - *Fail:* Occultist escapes, `0` Lifeforce, `+5` Stress.
    - *Critical Fail:* Catastrophic hex, Wounded, `0` Lifeforce, `-50` Piety, `+20` Stress.
    - *Option B:* Share the chalice for **1 Minor Lifeforce**, `+50` Piety, `+2` `enlightenment` XP.
  - **The Cairn of Forgotten Carnage (`seek_power.004`):** Ancient sacrificial cairn yielding **1 Major Lifeforce** + `+2` `enlightenment` XP + `+1` `ancient` XP cleanly for both classes.
- **Manifest & Condense Lifeforce:**
  - `bm_manifest_lifeforce_decision`: `100` Piety Learning duel -> `+3` `enlightenment` XP and Minor/Major Lifeforce.
  - Condense Lifeforce (`bm_cast_blood_magic_minor.001`): `100` Piety + 1 Minor Lifeforce -> 1 Major Lifeforce (`+2` `ancient` XP).
  - Condense Superior Lifeforce (`bm_cast_blood_magic_major.001`): `250` Piety + 1 Minor + 1 Major Lifeforce (`piety_level >= 3`) -> 1 Superior Lifeforce (`+1` to `+3` `ancient` XP).
- **Hostile & Support Interactions:**
  - `lifedrain_courtier_event_interaction`: Prowess duel siphon (`25` Piety, 3-mo CD) -> 1 Minor Lifeforce + `+1` `slaughter` XP.
  - `trait_drain_prisoner_event_interaction`: Steal congenital traits up to Rank 5 from prisoners (`100–325` Piety + Major Lifeforce) -> `+2` `slaughter` XP.
  - `bm_bless_bloodline_interaction`: Bless child, dynasty kin, sworn knight, or Blood Knight courtier (`35` Piety + Minor Lifeforce, 10-yr buff; `50` Piety for permanent Feingur blessing) -> `+1` `benediction` XP. The **Blood of Iron** option (`bm_blessed_blood_iron_modifier`: `+2` Martial, `+4` Prowess, `+25%` Knight Effectiveness, `+1.0` Health, `+0.50` Negate Health Penalty for 10 yrs) serves as the unified champion blessing for sworn knights and Blood Knight courtiers.
  - `bm_ritual_spar_decision`: Annual courtyard ritual spar against sworn Blood Knights (1 Minor Lifeforce, 1-yr CD). Samples up to 3 candidates proportionally weighted by prowess ($w_i = \text{prowess}_i$) and initiates an interactive Single Combat Engine (SCE) practice duel (non-lethal). Victor claims **1 Major Lifeforce** + `+3` Vanguard/Hematurgy XP; Loser earns `+1` Vanguard/Enlightenment XP; Both gain `+20` Blademaster trait XP and `+15` opinion.
  - `bm_cull_champion_interaction`: Blood sacrifice of prowess >= 12 prisoner / Blood Knight prisoner or critically broken follower (`50` Piety; hidden on close family/spouses unless rival) -> Executes target (`death_lifedrain_reason`), yields **1 Major Lifeforce**, `+3` `slaughter` (Knight) / `+3` `hematurgy` (Mage) XP, and rolls `1 × prowess` chance (capped at 50%) for **1 Superior Lifeforce**.
  - `bm_inscribe_rune_other_interaction`: Carve Minor (`+4` `benediction` XP) or Major (`+5` `benediction` XP) Galdrastafir runes onto courtiers, kin, knights, or golems.
  - `bm_heal_ailment`: Unified healing access across Minor, Major, and Deadly ailments (`32` conditions), progressive old-age trait rejuvenation (`5` traits), and stress coping vice purging (`11` traits) on self and comrades.
- **Full Minor, Major & Superior Grimoire Access:**
  - Self-inscribe Minor (`+4` `ancient`), Major (`+5` `ancient`), and Superior (`+10` `ancient`) Galdrastafir Blood Runes.
  - Unlock and level all 5 `lifestyle_blood_power` tracks (`+3` `enlightenment` + `+10` Power XP).
  - Upgrade Education (1★–4★, `+5` `enlightenment`), Master Education to 5★ (`+20` `enlightenment`), and Embrace 2nd Education (`+10` `enlightenment`).
  - Manifest Congenital Perfection Ranks 1–2 (`+4` `vanguard`) and Apex Ranks 3–5 (`+6` `vanguard`, `+2` `enlightenment`).
  - Empower Dynasty Bloodline (`+3`/`+5`/`+10` `benediction` XP) and Forge Blood Golem (`+5` `vanguard` XP).
  - Convert realm faith via `become_blood_cultist_decision` (`250` Piety + Major Lifeforce).

---

## Blood Magic Men-at-Arms Regiments (`common/men_at_arms_types/bm_men_at_arms_types.txt`)

Both **Blood Mages** (`lifestyle_blood_mage`) and **Blood Knights** (`lifestyle_blood_knight`) can recruit two dedicated Piety-maintained Men-at-Arms regiments. Both regiments remain visible (`should_show_when_unavailable`) to any Blood Mage or Blood Knight before reaching the required Devotion level, have no per-ruler regiment cap (`max_regiments` uncapped), and cannot appear in generic mercenary/hired troops (`allowed_in_hired_troops = no`).

| Regiment | Key & Archetype | Stack | Stats (Dmg / Tough / Pur / Scr / Siege) | Counters | Terrain & Winter Modifiers | Costs & Requirements |
| --- | --- | --- | --- | --- | --- | --- |
| **Blood Berserkers** | `bm_blood_berserkers`<br>`heavy_infantry`<br>Icon: `varangian_veterans` | `100` | `68` / `20` / `35` / `0` / `0.10` | • Pikemen (`1.5`)<br>• Skirmishers (`1.0`)<br>• Archers (`1.0`) | • **Taiga / Forest / Mountains:** `+12` Dmg, `+8` Pur<br>• **Mild & Harsh Winter:** `+10` Dmg, `+5` Tough<br>• **Desert / Floodplains:** `-8` Dmg, `-4` Tough | • **Unlock:** Blood Mage or Blood Knight + **Devotion 2+** (`piety_level >= 2`)<br>• **Buy:** `150` Piety<br>• **Maint:** `1.35` / `0.40` Piety/mo (Raised / Unraised)<br>• **Provisions:** `7` (`@provisions_cost_infantry_moderate`) |
| **Blood-Bound Behemoths** | `bm_blood_behemoths`<br>`elephant_cavalry`<br>Icon: `war_elephants` | `25`<br>*(Hired: 10)* | `210` / `80` / `0` / `0` / `0.25` | • Heavy Infantry (`2.0`)<br>• Pikemen (`2.0`) | • **Mountains / Desert Mountains / Hills / Drylands:** `+15` Tough<br>• **Winter / Desert:** No combat penalty (`0` drain)<br>• **Wetlands:** `-30` Dmg, `-15` Tough | • **Unlock:** Blood Mage or Blood Knight + **Devotion 4+** (`piety_level >= 4`)<br>• **Buy:** `400` Piety<br>• **Maint:** `1.50` / `0.50` Piety/mo (Raised / Unraised)<br>• **Provisions:** `0` |

---

## Tracks Master Table (Cumulative Totals)

Each track has 10 tiers (`10, 20, ..., 100` XP). Vitality step = `+0.1` Health, `+2.5` Life Expectancy, `+1.25` Year Fertility, `+1` Epidemic Resistance (applied at tiers 10–40 and 60–90; **4× Vitality** at 50 XP, **8× Vitality** at 100 XP).

| Track | Focus | Step Bonus (Per Tier) | 50 XP Cumulative Total | 100 XP Cumulative Total |
| --- | --- | --- | --- | --- |
| **`vanguard`** | Army Command & Speed | `+1` Advantage (tiers 20–40, 60–90), `+1.75%` Army Speed (`+1` Martial at tiers 20, 40, 60, 80) | 4× Vitality + `+3` Advantage, `+7%` Army Speed, `+2` Martial, `+1` Martial per Piety Level | 8× Vitality + `+7` Advantage, `+14%` Army Speed, `+4` Martial, `+1.5` Martial per Piety Level, `no_prowess_loss_from_age = yes` |
| **`slaughter`** | Combat Lethality & Knights | `+1.5` or `+2` Prowess, `+1` Knight Limit (tiers 20–40, 60–90), `+8.75%` Knight Effectiveness | 4× Vitality + `+7` Prowess, `+3` Knight Limit, `+35%` Knight Effectiveness, `+1` Prowess per Piety Level | 8× Vitality + `+14` Prowess, `+7` Knight Limit, `+70%` Knight Effectiveness, `+2` Prowess per Piety Level, `no_prowess_loss_from_age = yes` |
| **`ancient`** *(shared)* | Longevity & Lifestyle XP | `+0.1` Monthly Dynasty Prestige, `+4%` Lifestyle XP Mult | 4× Vitality + `+0.4` Dynasty Prestige, `+16%` Lifestyle XP, `+0.25` Negate Health Penalty, `+1` Prowess per Piety Level, `+17.5%` Devotion Impact | 8× Vitality + `+0.8` Dynasty Prestige, `+32%` Lifestyle XP, `+0.75` Negate Health Penalty, `+1` Prowess per Piety Level, `+50%` Devotion Impact, `no_prowess_loss_from_age = yes` |
| **`enlightenment`** *(shared)* | Piety & Scholarship | `+0.175` Monthly Piety, `+4%` Monthly Piety Mult | 4× Vitality + `+0.7` Monthly Piety, `+16%` Piety Mult, `+1` Learning per Piety Level | 8× Vitality + `+1.4` Monthly Piety, `+32%` Piety Mult, `+2` Learning per Piety Level, `no_prowess_loss_from_age = yes` |
| **`benediction`** *(shared)* | Opinion & Prestige | `+1.5` General Opinion, `+1` Vassal Opinion, `+0.175` Monthly Prestige, `+4%` Prestige Mult | 4× Vitality + `+6` General Opinion, `+4` Vassal Opinion, `+0.7` Monthly Prestige, `+16%` Prestige Mult, `+1` Diplomacy per Piety Level | 8× Vitality + `+12` General Opinion, `+8` Vassal Opinion, `+1.4` Monthly Prestige, `+32%` Prestige Mult, `+2` Diplomacy per Piety Level, `no_prowess_loss_from_age = yes` |

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
| Battlefield victory/defeat & tournament hooks | `common/on_action/bm_combat_on_actions.txt`, `common/scripted_effects/bm_combat_effects.txt` |
| Duel fatality & Superior harvest | `common/on_action/bm_duel_on_actions.txt` |
| Yearly pulse | `events/bm_yearly_events.txt` (`blood_mage_yearly_events.004`) |
| Blood Magic Men-at-Arms | `common/men_at_arms_types/bm_men_at_arms_types.txt`, `localization/english/bm_men_at_arms_l_english.yml` |
