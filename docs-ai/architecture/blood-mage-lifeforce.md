# Blood Mage Lifeforce

## Executive Summary

- **What:** Core spellcasting resource. Stored as physical character modifiers (`lifeforce_modifier_minor`, `lifeforce_modifier_major`).
- **Sources:** Harvesting prisoners/courtiers, slaying duel opponents, or spiritual self-manifestation.
- **Sinks:** Spent to power decisions, interactions, golem forging, bloodline enhancements, and retinue. Casting applies temporary negative exhaustion backlash.

### Lifeforce Modifiers Table

| Modifier | Type | Stacking | Duration | Mechanical Effects |
| --- | --- | --- | --- | --- |
| `lifeforce_modifier_minor` | Positive | Yes | Permanent until spent | `+0.1` Health, `+1` Life Exp, `+1` Fertility Yr, `+1` Epidemic Res, `+1` Prowess |
| `lifeforce_modifier_major` | Positive | Yes | Permanent until spent | `+0.5` Health, `+10` Life Exp, `+5` Fertility Yrs, `+5` Epidemic Res, `+5` Prowess |
| `lifeforce_modifier_negative_minor` | Backlash | Yes | Temporary (expires) | `-0.1` Health, `-1` Life Exp, `-1` Fertility Yr, `-1` Epidemic Res, `-1` Prowess |
| `lifeforce_modifier_negative_major` | Backlash | Yes | Temporary (expires) | `-0.5` Health, `-5` Life Exp, `-5` Fertility Yrs, `-5` Epidemic Res, `-5` Prowess |
| `lifedrained_modifier` | Victim Toll | Yes | Permanent | `-0.5` Health, `-10` Life Exp, `-5` Fertility Yrs, `-5` Epidemic Res, `-5` Prowess |
| `recently_lifedrained_modifier` | Victim CD | No | Temporary | Cooldown debuff preventing immediate re-harvesting of same courtier |

## Sources & Sinks Matrix

| Action | Cost / Requirements | Lifeforce Delta | XP Gain |
| --- | --- | --- | --- |
| `lifedrain_prisoner_interaction` | Piety. Dungeon prisoner. | Grants `lifeforce_modifier_minor` | +1 hematurgy |
| `lifedrain_courtier_event_interaction` | Piety. Unlanded courtier. | Grants `lifeforce_modifier_minor` | +1 hematurgy |
| Lethal duel kill (combat on-action) | Win lethal single combat duel. | Grants `lifeforce_modifier_major` | +2 hematurgy |
| `bm_manifest_lifeforce` (decision) | 250 piety. Learning check. | Grants minor or major Lifeforce | +1 enlightenment |
| `bm_crimson_empowerment_decision` | 150 piety + Major Lifeforce. | Consumes `lifeforce_modifier_major` | +3 enlg, +10 CE |
| `channel_lifeforce_bloodline` | 350 piety + Major Lifeforce. | Consumes `lifeforce_modifier_major` | +5 bloodline |
| `bm_create_blood_golem` | 350 piety + Major Lifeforce. | Consumes `lifeforce_modifier_major` | +3 enlightenment |
| `grant_crimson_warrior_interaction` | Piety + Minor Lifeforce. | Consumes `lifeforce_modifier_minor` | +1 benediction |
| `grant_crimson_champion_interaction` | Piety + Major Lifeforce. | Consumes `lifeforce_modifier_major` | +2 benediction |

## Where the details live

| Piece | File |
| --- | --- |
| Lifeforce modifiers | `common/modifiers/bm_lifeforce.txt` |
| Temporary backlash effects | `common/scripted_effects/bm_blood_magic_temporary_effects.txt` |
| Cast consumption effects | `common/scripted_effects/bm_blood_magic_used_effects.txt` |
| Harvesting interactions | `common/character_interactions/bm_drain_lifeforce.txt` |
| Duel fatality harvesting | `common/on_action/bm_duel_on_actions.txt` |
| Manifestation decision | `common/decisions/bm_manifest_lifeforce.txt` |
| Mass harvesting decision | `common/decisions/bm_mass_lifedrain_prisoners.txt` |
| Story panel stack tally | `common/scripted_effects/bm_blood_mage_story_list_effects.txt` |

## Gotchas

- Positive stacks never expire on their own; only removed by script consumption effects.
- Scripted cast consumption in `bm_blood_magic_used_effects.txt` removes the positive modifier and applies the corresponding temporary negative exhaustion modifier.
