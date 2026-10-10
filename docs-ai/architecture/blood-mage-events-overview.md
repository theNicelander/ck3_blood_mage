# Blood Mage Events Overview

## Executive Summary

- **What:** Event routing layer. Dispatches complex decision outcomes, skill duels, and yearly background pulses.
- **Rule:** One namespace per event file.

### Event Files Matrix

| Event File | Namespace | Triggered By | Subsystem & Function |
| --- | --- | --- | --- |
| `events/bm_cast_blood_magic_minor_events.txt` | `bm_cast_blood_magic_minor` | Decision `bm_cast_blood_magic_minor_decision` | Hub event (.001) offering Minor Lifeforce rites (Channel vs Attune). |
| `events/bm_cast_blood_magic_major_events.txt` | `bm_cast_blood_magic_major` | Decision `bm_cast_blood_magic_major_decision` | Hub event (.001) offering Major Lifeforce rites (Empowerment, Education 1-4, Minor/Major Runes, Bloodline, Congenital Traits 1-3). |
| `events/bm_cast_blood_magic_superior_events.txt` | `bm_cast_blood_magic_superior` | Decision `bm_cast_blood_magic_superior_decision` | Hub event (.001) offering Superior Lifeforce rites (Master Education 5★, New Education, Superior Rune, Transcendent Perfection 4-5, Blood Golem). |
| `events/bm_attune_lifeforce_events.txt` | `bm_attune_lifeforce` | Event `bm_cast_blood_magic_minor.001` | Selects 1 of 5 school attunements (+50% yearly XP roll). |
| `events/bm_blood_golem_events.txt` | `blood_golem` | Decision `blood_golem_creation_decision` or `bm_cast_blood_magic_superior.001` | Golem crafting outcome, stat shaping duels. |
| `events/bm_channel_lifeforce_bloodline_events.txt` | `bm_channel_lifeforce_bloodline` | Event `bm_cast_blood_magic_major.001` | Bestows permanent house modifiers. |
| `events/bm_channel_manifest_traits_events.txt` | `bm_channel_manifest_traits` | Event `bm_cast_blood_magic_major.001` (.001) / `bm_cast_blood_magic_superior.001` (.002) | Learning self-duel to manifest/upgrade congenital traits (ranks 1-3 vs transcendent ranks 4-5). |
| `events/bm_channel_lifeforce_enlightenment_minor_events.txt` | `bm_channel_lifeforce_enlightenment_minor` | Event `bm_cast_blood_magic_minor.001` | Converts minor lifeforce into temporary attribute boost. |
| `events/bm_blood_empowerment_event.txt` | `bm_blood_empowerment_event` | Event `bm_cast_blood_magic_major.001` | Advances chosen CE track (+10 XP) or fallback Versatility. |
| `events/bm_education_enhance.txt` | `bm_education_enhancement` | Event `bm_cast_blood_magic_major.001` | Learning duel to advance education star level (up to 4-star). |
| `events/bm_education_master_events.txt` | `bm_education_master` | Event `bm_cast_blood_magic_superior.001` | Discipline duel to advance 4-star education to legendary 5-star mastery. |
| `events/bm_education_new.txt` | `bm_education_new` | Event `bm_cast_blood_magic_superior.001` | Grants an additional secondary education trait. |
| `events/bm_mass_lifedrain.txt` | `bm_mass_lifedrain` | Decision `mass_lifedrain_prisoners_decision` | Mass execution of dungeon prisoners for Lifeforce. |
| `events/bm_seek_power_events.txt` | `bm_seek_power` | Decision `seek_power_decision` | Wilderness exploration event chain (beasts, encounters, lifeforce). |
| `events/bm_trait_drain_events.txt` | `bm_trait_drain` | Interaction `trait_drain_prisoner_event_interaction` | Siphons positive congenital traits from prisoners via duel. |
| `events/bm_yearly_events.txt` | `blood_mage_yearly_events` | Yearly pulse on-action | .001: +1 ancient & attunement rolls. .002: bloodline dynasty rolls. .003: rune lifeforce rolls. |

## Key Mechanics

- **Decisions -> Events:** Decisions validate costs/prerequisites, then trigger the matching event (`trigger_event = { id = <event_id> }`).
- **Duel Resolution:** Duels embedded in event options use comparative skill values documented in `events/_duels.md`.
- **Payloads:** Event options call shared effects in `common/scripted_effects/` to grant XP, apply modifiers, or execute prisoners.
