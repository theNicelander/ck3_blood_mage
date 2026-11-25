# Blood Mage Events Overview

## Executive Summary

- **What:** Event routing layer. Dispatches complex decision outcomes, skill duels, and yearly background pulses.
- **Rule:** One namespace per event file.

### Event Files Matrix

| Event File | Namespace | Triggered By | Subsystem & Function |
| --- | --- | --- | --- |
| `events/bm_ascension_duel_events.txt` | `bm_ascension_duel` | Decision `bm_elevate_blood_mage_tier_decision` | Non-lethal Blood Mirror duel against self-reflection to ascend Blood Mage tier. |
| `events/bm_bestow_traits_events.txt` | `bm_bestow_traits` | Interaction `bm_bestow_traits_interaction` | Bestows congenital/physical traits to spouse or dynasty kin. |
| `events/bm_blood_conclave_events.txt` | `bm_blood_conclave` | Decision `bm_blood_conclave_decision` | Convene a Blood Conclave event (`.0001`) resolving shared study, Lifeforce pooling, or communion with 15% disruption duel. |
| `events/bm_blood_golem_events.txt` | `blood_golem` | Decision option `bm_superior_create_blood_golem` (`bm_cast_blood_magic_superior_decision`) | Golem crafting outcome (`.001`) and repeatable trait-shaping Learning duels (`.002`). |
| `events/bm_buy_captives_events.txt` | `bm_buy_captives` | Decision `bm_buy_captives_decision` | Captive broker purchase and haggle events (`.0001`–`.0003`). |
| `events/bm_channel_manifest_traits_events.txt` | `bm_channel_manifest_traits` | Decision options `bm_major_manifest_traits` / `bm_superior_manifest_traits` (`bm_cast_blood_magic.txt`) | Learning self-duel to manifest/upgrade congenital traits (Ranks 1–3 in `.001` vs. Apex Ranks 4–5 in `.002`). |
| `events/bm_education_enhance.txt` | `bm_education_enhancement` | Decision option `bm_major_improve_education` (`bm_cast_blood_magic.txt`) | Learning duel to advance education star level (up to 4-star). |
| `events/bm_education_master_events.txt` | `bm_education_master` | Decision option `bm_superior_master_education` (`bm_cast_blood_magic.txt`) | Discipline duel to advance 4-star education to legendary 5-star mastery. |
| `events/bm_education_new.txt` | `bm_education_new` | Decision option `bm_superior_new_education` (`bm_cast_blood_magic.txt`) | Grants an additional secondary education trait. |
| `events/bm_faith_conversion_events.txt` | `bm_faith_conversion` | Decision `become_blood_cultist_decision` | Faith conversion grimoire (.0001) converting character and realm to cultural Blóðtrú faith. |
| `events/bm_geyser_duel_events.txt` | `bm_geyser_duel` | Decision `bm_blood_cultist_become_blood_mage_decision` or `bm_enhance_blood_ritual_decision` | Initiation duel (.0001) against Egill Skallagrímsson in Reykjavik or Tsushima. |
| `events/bm_heal_ailment_events.txt` | `bm_heal_ailment` | Interaction `bm_heal_ailment` | Individual ailment curing grimoire (.0001) with options across 40 afflictions. |
| `events/bm_heal_old_age_events.txt` | `bm_heal_old_age` | Interaction `bm_heal_ailment` (when target only has old-age traits) | Rejuvenation event (.0001) for 5 degenerative traits (`infirm`, `clouded_eyes`, `fragile_bones`, `withering_mind`, `faltering_heart`). |
| `events/bm_mass_lifedrain.txt` | `bm_mass_lifedrain` | Decision `mass_lifedrain_prisoners_decision` | Mass execution of dungeon prisoners (all or expendable filter) or non-lethal Minor siphon (`.001`). |
| `events/bm_memory_drain_events.txt` | `bm_memory_drain` | Interaction `bm_blood_drain_interaction` (`drain_memory`) | Extracts lifestyle/commander/fame traits from prisoners. |
| `events/bm_prisoner_blood_duel_events.txt` | `bm_prisoner_blood_duel` | Interaction `bm_blood_drain_interaction` (`drain_blood_duel`) | Blood Pit Single Combat resolution event. |
| `events/bm_reformation_repair_events.txt` | `bm_reformation_repair` | Decision `bm_repair_blodtru_reformation_decision` | Clears bugged/corrupted temporal head title. |
| `events/bm_reshape_personality_events.txt` | `bm_reshape_personality` | Interaction `bm_reshape_personality_interaction` | Learning duel to copy personality trait or culture. |
| `events/bm_ritual_spar_events.txt` | `bm_ritual_spar_events` | Decision `bm_ritual_spar_decision` | Blood Sparring Ring partner selection and SCE bout outcome. |
| `events/bm_seek_power_events.txt` | `seek_power` | Decision `seek_power_decision` | Blood Hunt event chain (`.001` dispatcher, martial encounters `.002`–`.011`, non-martial encounters `.012` Sunken Blood Shrine, `.013` Plague-Touched Hermit, `.014` Rival Coven's Cache, Single Combat output `.006`, invalidation `.007`). |
| `events/bm_trait_drain_events.txt` | `bm_trait_drain` | Interaction `bm_blood_drain_interaction` (`drain_traits`) | Siphons positive congenital traits from prisoners via duel. |
| `events/bm_yearly_events.txt` | `blood_mage_yearly_events` | Yearly pulse on-action | .001: +1 ancient & guaranteed attunement XP (+2 with Superior **Hulinhjálmur**). .002: bloodline dynasty rolls. .003: rune lifeforce rolls. |
| `events/bm_interpersonal_events.txt` | `bm_interpersonal_events` | Yearly interpersonal pulse & battle victory on-action | 10 narrative & earned-risk events (`.0001` lover/spouse, `.0002` child/ward fever, `.0003` post-battle Red Banquet, `.0004` golem aegis/honing/siphoning, `.0005` snooping courtier, `.0006` Red Thirst overdrain/exhaustion, `.0007` Weight of Centuries 85+, `.0008` Challenger in Crimson, `.0009` Fractured Clay golem maintenance, `.0010` Eager Acolyte mentorship). |

## Key Mechanics

- **Decisions -> Events:** Decisions validate costs/prerequisites, then trigger the matching event (`trigger_event = { id = <event_id> }`).
- **Duel Resolution:** Duels embedded in event options use comparative skill values documented in `events/_duels.md`.
- **Payloads:** Event options call shared effects in `common/scripted_effects/` to grant XP, apply modifiers, or execute prisoners.
