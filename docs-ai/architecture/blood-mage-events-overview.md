# Blood Mage Events Overview

## Executive Summary

- **What:** Event routing layer. Dispatches complex decision outcomes, skill duels, and yearly background pulses.
- **Rule:** One namespace per event file.

### Event Files Matrix

| Event File | Namespace | Triggered By | Subsystem & Function |
| --- | --- | --- | --- |
| `events/bm_attune_lifeforce_events.txt` | `bm_attune_lifeforce` | Decision `bm_attune_lifeforce_decision` | Selects 1 of 5 school attunements (+50% yearly XP roll). |
| `events/bm_blood_golem_events.txt` | `blood_golem` | Decision `bm_create_blood_golem` | Golem crafting outcome, stat shaping duels. |
| `events/bm_blood_rune_events.txt` | `bm_crimson_rune` | Decision `bm_inscribe_blood_runes_decision` | Inscription of minor, major, or superior body runes. |
| `events/bm_channel_lifeforce_bloodline_events.txt` | `bm_channel_lifeforce_bloodline` | Decision `channel_lifeforce_bloodline` | Bestows permanent house modifiers. |
| `events/bm_channel_lifeforce_enlightenment_minor_events.txt` | `bm_channel_lifeforce_enlightenment_minor` | Decision `bm_channel_minor_lifeforce_decision` | Converts minor lifeforce into temporary attribute boost. |
| `events/bm_crimson_empowerment_event.txt` | `bm_crimson_empowerment_event` | Decision `bm_crimson_empowerment_decision` | Advances chosen CE track (+10 XP) or fallback Versatility. |
| `events/bm_education_enhance.txt` | `bm_education_enhance` | Decision `bm_improve_education_decision` | Learning duel to advance education star level (up to 5-star). |
| `events/bm_education_new.txt` | `bm_education_new` | Decision `bm_new_education_decision` | Grants an additional secondary education trait. |

| `events/bm_mass_lifedrain.txt` | `bm_mass_lifedrain` | Decision `bm_mass_lifedrain_prisoners` | Mass execution of dungeon prisoners for Lifeforce. |
| `events/bm_seek_power_events.txt` | `bm_seek_power` | Decision `bm_seek_power_decision` | Wilderness exploration event chain (beasts, encounters, lifeforce). |
| `events/bm_trait_drain_events.txt` | `bm_trait_drain` | Interaction `trait_drain_prisoner_event_interaction` | Siphons positive congenital traits from prisoners via duel. |
| `events/bm_yearly_events.txt` | `blood_mage_yearly_events` | Yearly pulse on-action | .001: +1 ancient & attunement rolls. .002: bloodline dynasty rolls. .003: rune lifeforce rolls. |

## Key Mechanics

- **Decisions -> Events:** Decisions validate costs/prerequisites, then trigger the matching event (`trigger_event = { id = <event_id> }`).
- **Duel Resolution:** Duels embedded in event options use comparative skill values documented in `events/_duels.md`.
- **Payloads:** Event options call shared effects in `common/scripted_effects/` to grant XP, apply modifiers, or execute prisoners.
