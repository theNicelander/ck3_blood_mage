# Blood Mage: Blood Knight

Living technical specification for the Blood Knight subsystem (`lifestyle_blood_knight`).

## Executive Summary

- **What:** Permanent, Devotion-anchored martial endgame peer (`lifestyle_blood_knight`) to `lifestyle_blood_mage`, modeled after CK3 1.20's *Proclaim the Living Word* split (*Fire and Sword* vs. *Shepherd of the Faithful*). Features 5 tracks: 2 exclusive martial tracks (`vanguard`, `slaughter`) and 3 shared Devotion tracks (`ancient`, `benediction`, `enlightenment`), max 100 XP each.
- **Icon & Base Stats:** `bm_blood_knight.dds` (`gfx/interface/icons/traits/bm_blood_knight.dds`). Base: `same_opinion = 10`, `ruler_designer_cost = 50`. Inheritable (`25%` single parent, `100%` both; `0.20%` birth) scaled by campaign game rule `bm_blood_knight_prevalence`. Mutually exclusive with `lifestyle_blood_mage` (dual-wielding preserved only for historical Egill Skallagrímsson).
- **How to acquire:**
  - `make_blood_knight_interaction`: Initiated by a fellow Blood Knight (`100` Piety + Major Lifeforce OR `250` Piety + Minor Lifeforce) on a sworn knight or courtier.
  - **Geyser Duel Initiation (`bm_geyser_duel.0001`):** Travel to Reykjavik or Tsushima via `bm_blood_cultist_become_blood_mage_decision` or `bm_enhance_blood_ritual_decision` (requires `piety_level >= 2`). Choosing the Prowess duel costs **1 Devotion level** (`add_piety_level = -1`) and bestows `lifestyle_blood_knight` upon victory.
- **Apex Devotion Capstones:** The 100 XP capstones of all 3 shared tracks (`ancient`, `enlightenment`, `benediction`) grant massive Devotion-scaling powers (`+50%` Devotion Impact on `ancient`, `+2` Learning per Devotion level on `enlightenment`, and `+2` Diplomacy per Devotion level on `benediction`).
- **Track Milestones & Cleanliness:** Vitality baselines (`+0.1` Health, `+2.5` Life Expectancy, `+1.25` Year Fertility, `+1` Epidemic Resistance) apply at standard tiers (10–40, 60–90) and are skipped at 50 XP and 100 XP milestones. Every track capstone at 100 XP grants `no_prowess_loss_from_age = yes`.

### How Blood Knights Harvest Lifeforce & Advance Tracks
- **Battlefield Victory (`bm_on_combat_end_winner`):** Surviving a battle as commander or knight awards `+1` to `+5` `vanguard` XP and rolls troop-scaled Lifeforce (`10%–100%` Minor Lifeforce and `0%–100%` Major Lifeforce across `<100` to `10,000+` troop brackets).
- **Battlefield Defeat Survival (`bm_on_combat_end_loser`):** Surviving a defeat as commander or knight awards `+1` to `+3` `vanguard` XP and `0` to `+2` `enlightenment` XP.
- **Fatal Single Combat Duels (`bm_on_character_death_duel`):** Slaying a foe in single combat grants `+5` `slaughter` XP and **1 Major Lifeforce**. Slaying a foe with `prowess >= 20` or holding `lifestyle_blood_mage`/`lifestyle_blood_knight` has a **25% chance to yield 1 Superior Lifeforce** directly.
- **Tournament Completion (`bm_on_travel_activity_complete_tournament`):** Completing a tournament (`activity_tournament`) awards `+3` `slaughter` XP.
- **Ambient Yearly Pulse (`blood_mage_yearly_events.004`):** Passive **~33% chance per year** to condense 1 Minor Lifeforce ambiently, alongside passive `+1` `ancient` XP and `+1` `enlightenment` XP (plus attunement rolls). Strictly exclusive to `lifestyle_blood_knight`.
- **Empower Blood Knight (`empower_blood_knight_interaction`):** Fellow Blood Knight empowers a sworn Blood Knight comrade:
  - Major Lifeforce: `+10` XP to both `vanguard` and `slaughter` on target; `+4` `benediction` XP to caster.
  - Minor Lifeforce: `+5` XP to both `vanguard` and `slaughter` on target; `+2` `benediction` XP to caster.
- **Seek Power in Nature's Domain (`seek_power_decision`):** Wilderness expedition harvesting Lifeforce and martial/enlightenment XP (`730`d cooldown landed, `365`d unlanded/wanderer; halved by Superior **Vegvísir**). Strictly exclusive to Blood Knights:
  - **Traveler & Escort Encounter (`seek_power.003`):** Spawns a wandering warrior-poet (`traveller_character_template`, Learning `10–18`, Prowess `8–18`, Martial `8–16`, heavily weighted `lifestyle_poet`) accompanied by a sworn escort knight (`bm_escort_knight_character_template`, prowess `20–30` plus martial/blademaster/blood traits). Both characters spawn with the player's culture and the player's current location county faith (with fallback to player faith).
  - **Friendly Brawl (`seek_power.003.knight`):** First option, always available for Blood Knights. Prowess skill duel against the traveler (`17 / 33 / 33 / 17` base weights): Crit Success awards **1 Major Lifeforce** + `+3` `slaughter` XP; Success awards **1 Minor Lifeforce** + `+2` `slaughter` XP; Spar awards `+1` `vanguard` XP.
  - **Battlefield Single Combat Duel (`seek_power.003.battlefield_duel` -> `seek_power.006`):** Available when the player has `prowess >= 25` (Blood Knight), displaying grayed out via `show_as_unavailable` if prowess is below 25. Launches an interactive Single Combat Engine duel (`FATALITY = possible`, `LOCALE = battlefield`). Victory allows harvesting **1 Major Lifeforce**, `+5` `slaughter` XP, and a **25% chance of 1 Superior Lifeforce**—or sparing and recruiting the warrior (`+2` `vanguard` XP + **1 Minor Lifeforce**).
  - **Recruitment Options:**
    - *Persuade Traveler (`seek_power.003.c`):* Available if player has higher Learning than the traveler (`learning > scope:recipient.learning`), displaying grayed out if unmet with clean custom tooltip. Learning duel awards traveler as follower + `+1` `enlightenment` XP.
    - *Persuade Escort Knight (`seek_power.003.recruit_knight`):* Available if player has higher Prowess than the knight (`prowess > scope:escort_knight.prowess`), displaying grayed out if unmet with clean custom tooltip. Prowess duel awards knight as follower + `+2` `vanguard` XP.
- **Manifest & Condense Lifeforce:**
  - `bm_manifest_lifeforce_decision`: `100` Piety Learning duel -> `+3` `enlightenment` XP and Minor/Major Lifeforce.
  - Condense Lifeforce (`bm_cast_blood_magic_minor.001`): `100` Piety + 1 Minor Lifeforce -> 1 Major Lifeforce (`+2` `ancient` XP).
  - `bm_manifest_superior_lifeforce_decision`: `250` Piety + 1 Minor + 1 Major Lifeforce (`piety_level >= 3`) -> 1 Superior Lifeforce (`+2` to `+8` `ancient` XP).
- **Hostile & Support Interactions:**
  - `lifedrain_courtier_event_interaction`: Prowess duel siphon (`25` Piety, 3-mo CD) -> 1 Minor Lifeforce + `+1` `slaughter` XP.
  - `trait_drain_prisoner_event_interaction`: Steal congenital traits up to Rank 5 from prisoners (`100–325` Piety + Major Lifeforce) -> `+2` `slaughter` XP.
  - `bm_bless_bloodline_interaction`: Bless child/kin (`35` Piety + Minor Lifeforce, 10-yr buff) -> `+2` `vanguard` XP.
  - `bm_inscribe_rune_other_interaction`: Carve Minor (`+4` `benediction` XP) or Major (`+5` `benediction` XP) Galdrastafir runes onto courtiers, kin, knights, or golems.
  - `bm_heal_ailment`: Full healing access across Minor, Major, and Deadly ailments (`37` conditions) on self (`+2`/`+4` `enlightenment`, `+8` `benediction`) and comrades (`+1`/`+2` `vanguard` + `benediction`, `+8` `benediction`).
- **Full Minor, Major & Superior Grimoire Access:**
  - Self-inscribe Minor (`+4` `ancient`), Major (`+5` `ancient`), and Superior (`+10` `ancient`) Galdrastafir Blood Runes.
  - Unlock and level all 5 `lifestyle_blood_empowerment` tracks (`+3` `enlightenment` + `+10` Empowerment XP).
  - Upgrade Education (1★–4★, `+5` `enlightenment`), Master Education to 5★ (`+20` `enlightenment`), and Embrace 2nd Education (`+10` `enlightenment`).
  - Manifest Congenital Perfection Ranks 1–2 (`+4` `vanguard`) and Apex Ranks 3–5 (`+6` `vanguard`, `+2` `enlightenment`).
  - Empower Dynasty Bloodline (`+5` `vanguard` XP) and Forge Blood Golem (`+5` `vanguard` XP).
  - Convert realm faith via `become_blood_cultist_decision` (`250` Piety + Major Lifeforce).

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
| Healing & ailment removal | `common/character_interactions/bm_cure_illness_interactions.txt`, `events/bm_heal_ailment_events.txt` |
| Superior magic decision & events | `common/decisions/cast_magic/bm_cast_blood_magic_superior.txt`, `events/bm_cast_blood_magic_superior_events.txt` |
| Battlefield victory/defeat & tournament hooks | `common/on_action/bm_combat_on_actions.txt`, `common/scripted_effects/bm_combat_effects.txt` |
| Duel fatality & Superior harvest | `common/on_action/bm_duel_on_actions.txt` |
| Yearly pulse | `events/bm_yearly_events.txt` (`blood_mage_yearly_events.004`) |
