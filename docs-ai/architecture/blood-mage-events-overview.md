# Blood Mage Events Overview

> Living document. Follow `AGENTS.md` in this folder: concepts only, no numbers. Update it when event files, namespaces or triggers change.

## Purpose

This document maps all event files in the `events/` directory to their corresponding subsystems, explaining which decisions, interactions, or on-actions trigger them and how they connect to sibling architecture docs.

## Concepts

- **Interactive Spellcasting.** Rather than instantly resolving complex actions in decisions or interactions, heavy or multi-stage spells hand off execution to dedicated event files.
- **Duel Resolution.** Several event files resolve contested attribute challenges (such as duels for education, golem creation, or trait theft).
- **Yearly Maintenance.** Background narrative events and progression checks are dispatched via pulse events.

## Where the details live

| Event File | Namespace | Triggered By | Subsystem & Sibling Doc |
| --- | --- | --- | --- |
| `events/bm_attune_lifeforce_events.txt` | `bm_attune_lifeforce` | Interaction: `bm_cast_blood_magic_self_attune_lifeforce` | Lifeforce attunement (`blood-mage-lifeforce.md`) |
| `events/bm_blood_golem_events.txt` | `blood_golem` | Decision: `blood_golem_creation_decision` | Golem crafting & shaping (`blood-mage-golems.md`) |
| `events/bm_blood_rune_events.txt` | `bm_crimson_rune` | Interaction: `bm_cast_blood_magic_self_major_blood_rune` | Rune inscription (`blood-mage-blood-runes.md`) |
| `events/bm_channel_lifeforce_bloodline_events.txt` | `bm_channel_lifeforce_bloodline` | Decision: `channel_lifeforce_bloodline_decision` | Dynastic house boons (`blood-mage-dynasty.md`) |
| `events/bm_channel_lifeforce_enlightenment_minor_events.txt` | `bm_channel_lifeforce_enlightenment_minor` | Interaction: `bm_cast_blood_magic_self_channel_minor_lifeforce` | Attribute channeling (`blood-mage-lifeforce.md`) |
| `events/bm_crimson_empowerment_event.txt` | `bm_crimson_empowerment_event` | Interaction: `bm_cast_blood_magic_self_major_crimson_empowerment` | Secondary trait advancement (`blood-mage-crimson-empowerment.md`) |
| `events/bm_education_enhance.txt` | `bm_education_enhance` | Interaction: `bm_cast_blood_magic_self_major_improve_education` | Education tier upgrade (`blood-mage-duels-and-education.md`) |
| `events/bm_education_new.txt` | `bm_education_new` | Interaction: `bm_cast_blood_magic_self_major_new_education` | Secondary education (`blood-mage-duels-and-education.md`) |
| `events/bm_mass_lifedrain.txt` | `bm_mass_lifedrain` | Decision: `mass_lifedrain_prisoners_decision` | Prisoner harvesting (`blood-mage-duels-and-education.md`) |
| `events/bm_seek_power_events.txt` | `bm_seek_power` | Decision: `bm_seek_power_decision` | Occult power seeking (`blood-mage-decisions.md`) |
| `events/bm_trait_drain_events.txt` | `bm_trait_drain` | Interaction: `trait_drain_prisoner_event_interaction` | Congenital trait theft (`blood-mage-duels-and-education.md`) |
| `events/bm_yearly_events.txt` | `bm_yearly_events` | On-action: `yearly_blood_mage_pulse` | Yearly narrative pulses (`blood-mage-prevalence-and-lifecycle.md`) |

## How the parts connect

- Decisions and interactions initiate events via `trigger_event = { id = <event_id> }`.
- Scripted effects in `common/scripted_effects/` supply the outcome payloads (XP, Lifeforce modifiers, deaths, or trait grants).
- Duels embedded within options follow the mechanics documented in `events/_duels.md`.

## Gotchas

- CK3 event namespaces must be declared at the top of each file with `namespace = <name>`.
- Always verify that event options clean up temporary scopes and modifiers if a duel or ritual fails.

## Not verified

Event portrait positioning and emotional animations during high-drama ritual failures on non-standard character models.
