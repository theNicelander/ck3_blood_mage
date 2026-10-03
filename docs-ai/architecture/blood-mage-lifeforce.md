# Blood Mage Lifeforce

> Living document. Follow `AGENTS.md` in this folder: concepts only, no numbers. Update it when Lifeforce modifiers, sources, sinks or mechanics change.

## Purpose

Lifeforce is the core supernatural resource fueling blood magic. Rather than an abstract numeric currency like gold or piety, Lifeforce in this mod is represented as physical essence carried directly on characters through stacking modifiers. It must be harvested from mortal lives, stored in the body, and burned to fuel spells, bloodline enhancements, and servants.

## Concepts

- **Positive Stacks.** Harvested vitality resides on the blood mage as positive modifiers (`lifeforce_modifier_major` and `lifeforce_modifier_minor`). They represent accumulated vitality, extending lifespan, enhancing health, and providing resistance to disease.
- **Backlash and Exhaustion.** Expending Lifeforce inflicts temporary negative modifiers (`lifeforce_modifier_negative_major`, `lifeforce_modifier_negative_minor`), leaving the mage physically depleted until their body recovers.
- **Harvesting.** Hematurgy spells draw Lifeforce out of living victims (prisoners, courtiers, or self-manifestation through dangerous spiritual conversion).
- **Victim Toll.** Victims who survive having their vitality stolen suffer debilitating modifiers (`lifedrained_modifier`), reducing health and life expectancy.
- **Sustained Imbuement.** Lifeforce can be bound into other beings to maintain them, such as Crimson Warriors and Crimson Champions, whose supernatural prowess is sustained at the cost of physical strain.
- **Story Tracking.** Because CK3 script cannot inspect modifier stack counts directly, the Blood Mage story cycle periodically tallies active stacks for UI display.

## Where the details live

| Piece | File |
| --- | --- |
| Lifeforce modifiers | `common/modifiers/bm_lifeforce.txt` |
| Temporary backlash effects | `common/scripted_effects/bm_blood_magic_temporary_effects.txt` |
| Magic cast consumption effects | `common/scripted_effects/bm_blood_magic_used_effects.txt` |
| Harvesting interactions | `common/character_interactions/bm_drain_lifeforce.txt` |
| Granting interactions | `common/character_interactions/bm_grant_lifeforce.txt` |
| Self-manifestation decision | `common/decisions/bm_manifest_lifeforce.txt` |
| Mass harvesting decision | `common/decisions/bm_mass_lifedrain_prisoners.txt` |
| Attunement events | `events/bm_attune_lifeforce_events.txt` |
| Enlightenment spending events | `events/bm_channel_lifeforce_enlightenment_minor_events.txt` |
| Story roster & stack tally | `common/scripted_effects/bm_blood_mage_story_list_effects.txt` |

## How the parts connect

- Gaining Lifeforce applies `lifeforce_modifier_major` or `lifeforce_modifier_minor` and awards Hematurgy track experience.
- Casting spells invokes consumption effects in `bm_blood_magic_used_effects.txt`, which remove positive stacks and apply temporary negative backlash.
- Decisions such as `manifest_lifeforce_decision` offer a gamble to convert piety and spiritual power into fresh Lifeforce stacks.
- `bm_refresh_blood_magic_rosters_effect` counts positive stacks to keep the Blood Magic panel in `blood-mage-story.md` accurate.

## Gotchas

- Positive Lifeforce stacks do not decay automatically by default; they remain until spent or removed by negative events.
- Negative backlash modifiers are temporary and wear off over time.
- Modifying Lifeforce via custom script should always respect the paired removal and backlash application in `bm_blood_magic_used_effects.txt` to keep track experience and story tallies consistent.

## Not verified

In-game tooltip formatting for multiple stacked instances of identical modifiers and portrait visual effects when holding maximum stacks.
