# Blood Mage Events Overview

## Executive Summary

- **What:** Event routing layer. Dispatches complex decision outcomes, skill duels, and yearly background pulses.
- **Rule:** One namespace per event file.

### Event Files Matrix

| Event File | Namespace | Triggered By | Subsystem & Function |
| --- | --- | --- | --- |
| `events/bm_cast_blood_magic_minor_events.txt` | `bm_cast_blood_magic_minor` | Decision `bm_cast_blood_magic_minor_decision` | Grimoire event (`.001`) offering Minor Lifeforce rites: Channel Minor, Condense into Major, Purge Impurities, Inscribe Minor Blood Rune, and Flay Minor Rune. |
| `events/bm_cast_blood_magic_major_events.txt` | `bm_cast_blood_magic_major` | Decision `bm_cast_blood_magic_major_decision` | Grimoire event (`.001`) offering Major Lifeforce rites: Blood Empowerment, Improve Education (1★–4★), Inscribe Major Blood Rune, Flay Major Rune, Empower Bloodline, and Manifest Perfection (Congenital Ranks 1–2). |
| `events/bm_cast_blood_magic_superior_events.txt` | `bm_cast_blood_magic_superior` | Decision `bm_cast_blood_magic_superior_decision` | Grimoire event (`.001`) offering Superior Lifeforce rites: Master Education (5★), Embrace New Education (2nd trait), Inscribe Superior Blood Rune, Flay Superior Rune, Manifest Apex Perfection (Congenital Ranks 3–5), and Forge Blood Golem. |
| `events/bm_blood_runes_events.txt` | `bm_blood_runes` | Grimoire rune options & `bm_inscribe_rune_other_interaction` | `.001`: 5-stave Icelandic Galdrastafir selector for self (`scope:rune_target = root`) or other (`scope:rune_target = recipient`). `.002`: Agony Flay & Swap rite burning `ancient` XP, Piety, and Lifeforce to replace active stave at current tier. |
| `events/bm_blood_golem_events.txt` | `blood_golem` | Event option `bm_cast_blood_magic_superior.001.create_blood_golem` | Golem crafting outcome (`.001`) and repeatable trait-shaping Learning duels (`.002`). |
| `events/bm_channel_lifeforce_bloodline_events.txt` | `bm_channel_lifeforce_bloodline` | Event `bm_cast_blood_magic_major.001` | Bestows permanent supernatural house modifiers. |
| `events/bm_channel_manifest_traits_events.txt` | `bm_channel_manifest_traits` | Event `bm_cast_blood_magic_major.001` (`.001`) / `bm_cast_blood_magic_superior.001` (`.002`) | Learning self-duel to cleanse flaws and manifest/upgrade congenital traits (Ranks 1–2 in `.001` vs. Apex Ranks 3–5 in `.002`). |
| `events/bm_channel_lifeforce_enlightenment_minor_events.txt` | `bm_channel_lifeforce_enlightenment_minor` | Event `bm_cast_blood_magic_minor.001` | Converts minor lifeforce into temporary attribute boost. |
| `events/bm_blood_empowerment_event.txt` | `bm_blood_empowerment_event` | Event `bm_cast_blood_magic_major.001` | Advances chosen CE track (+10 XP) or fallback Versatility. |
| `events/bm_education_enhance.txt` | `bm_education_enhancement` | Event `bm_cast_blood_magic_major.001` | Learning duel to advance education star level (up to 4-star). |
| `events/bm_education_master_events.txt` | `bm_education_master` | Event `bm_cast_blood_magic_superior.001` | Discipline duel to advance 4-star education to legendary 5-star mastery. |
| `events/bm_education_new.txt` | `bm_education_new` | Event `bm_cast_blood_magic_superior.001` | Grants an additional secondary education trait. |
| `events/bm_faith_conversion_events.txt` | `bm_faith_conversion` | Decision `become_blood_cultist_decision` | Faith conversion grimoire (.0001) converting character and realm to cultural Blóðtrú faith. |
| `events/bm_geyser_duel_events.txt` | `bm_geyser_duel` | Decision `bm_blood_cultist_become_blood_mage_decision` or `bm_enhance_blood_ritual_decision` | Initiation duel (.0001) against Egill Skallagrímsson in Reykjavik or Tsushima. |
| `events/bm_heal_ailment_events.txt` | `bm_heal_ailment` | Interaction `bm_heal_ailment` | Individual ailment curing grimoire (.0001) with options across 37 afflictions. |
| `events/bm_mass_lifedrain.txt` | `bm_mass_lifedrain` | Decision `mass_lifedrain_prisoners_decision` | Mass execution of dungeon prisoners for Lifeforce. |
| `events/bm_reformation_repair_events.txt` | `bm_reformation_repair` | Decision `bm_repair_blodtru_reformation_decision` | Clears bugged/corrupted temporal head title. |
| `events/bm_seek_power_events.txt` | `seek_power` | Decision `seek_power_decision` | Wilderness exploration event chain (`.001`–`.004`, Single Combat output `.006`, invalidation `.007`): beast harvest, traveler + 50% escort knight encounter (friendly brawl, battlefield Single Combat duel, Learning recruitment), and ancient bleeding tree. |
| `events/bm_trait_drain_events.txt` | `bm_trait_drain` | Interaction `trait_drain_prisoner_event_interaction` | Siphons positive congenital traits from prisoners via duel. |
| `events/bm_yearly_events.txt` | `blood_mage_yearly_events` | Yearly pulse on-action | .001: +1 ancient & guaranteed attunement XP (+2 with Superior **Hulinhjálmur**). .002: bloodline dynasty rolls. .003: rune lifeforce rolls. .004: blood knight +1 enlightenment/ancient, ambient lifeforce roll, & guaranteed attunement XP (+2 with Superior **Hulinhjálmur**). |

## Key Mechanics

- **Decisions -> Events:** Decisions validate costs/prerequisites, then trigger the matching event (`trigger_event = { id = <event_id> }`).
- **Duel Resolution:** Duels embedded in event options use comparative skill values documented in `events/_duels.md`.
- **Payloads:** Event options call shared effects in `common/scripted_effects/` to grant XP, apply modifiers, or execute prisoners.
