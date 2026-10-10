# Blood Mage Lifeforce

## Executive Summary

- **What:** Core spellcasting resource. Stored as physical character modifiers (`lifeforce_modifier_minor`, `lifeforce_modifier_major`, `lifeforce_modifier_superior`).
- **Sources:** Harvesting prisoners/courtiers, slaying duel opponents, or spiritual self-manifestation (including distillation of superior lifeforce from minor and major reserves).
- **Sinks:** Spent to power decisions, interactions, golem forging, bloodline enhancements, and retinue. Casting applies temporary negative exhaustion backlash.

### Lifeforce Modifiers Table

| Modifier | Type | Stacking | Duration | Mechanical Effects |
| --- | --- | --- | --- | --- |
| `lifeforce_modifier_minor` | Positive | Yes | Permanent until spent | `+0.1` Health, `+1` Life Exp, `+1` Fertility Yr, `+1` Epidemic Res, `+0.1` Negate Health Penalty |
| `lifeforce_modifier_major` | Positive | Yes | Permanent until spent | `+0.3` Health, `+3` Life Exp, `+3` Fertility Yrs, `+3` Epidemic Res, `+0.3` Negate Health Penalty |
| `lifeforce_modifier_superior` | Positive | Yes | Permanent until spent | `+0.6` Health, `+6` Life Exp, `+6` Fertility Yrs, `+6` Epidemic Res, `+0.6` Negate Health Penalty, `+3` Prowess |
| `lifeforce_modifier_negative_minor` | Backlash | Yes | Temporary (expires) | `-0.1` Health, `-1` Life Exp, `-1` Fertility Yr, `-1` Epidemic Res, `-0.1` Negate Health Penalty, `-1` Prowess |
| `lifeforce_modifier_negative_major` | Backlash | Yes | Temporary (expires) | `-0.3` Health, `-3` Life Exp, `-3` Fertility Yrs, `-3` Epidemic Res, `-0.3` Negate Health Penalty, `-2` Prowess |
| `lifeforce_modifier_negative_superior` | Backlash | Yes | Temporary (expires) | `-0.6` Health, `-6` Life Exp, `-6` Fertility Yrs, `-6` Epidemic Res, `-0.6` Negate Health Penalty, `-4` Prowess |
| `lifedrained_modifier` | Victim Toll | Yes | Permanent | `-0.5` Health, `-10` Life Exp, `-5` Fertility Yrs, `-5` Epidemic Res, `-0.5` Negate Health Penalty, `-5` Prowess |
| `recently_lifedrained_modifier` | Victim CD | No | Temporary | Cooldown debuff preventing immediate re-harvesting of same courtier |

## Sources & Sinks Matrix

| Action | Cost / Requirements | Lifeforce Delta | XP Gain |
| --- | --- | --- | --- |
| `lifedrain_prisoner_interaction` | Piety. Dungeon prisoner. | Grants `lifeforce_modifier_minor` | +1 hematurgy |
| `lifedrain_courtier_event_interaction` | Piety. Unlanded courtier. | Grants `lifeforce_modifier_minor` | +1 hematurgy |
| Lethal duel kill (combat on-action) | Win lethal single combat duel (`bm_on_character_death_duel`). | Grants `lifeforce_modifier_minor` (strictly exclusive to Blood Knight) | +5 slaughter (Knight) |
| Battle victory (combat on-action) | Win army battle as knight/commander. | 33% chance grants `lifeforce_modifier_minor` (Blood Knight) | +5-6 vanguard (Knight) |
| `bm_manifest_lifeforce_decision` | 100 piety. Learning check (Mage) or Prowess duel (Knight). | Grants Minor or Major Lifeforce | +3 ancient (Mage) / +3 resilience (Knight) |
| Condense Lifeforce (minor ritual) | 100 piety + Minor Lifeforce. | Consumes Minor Lifeforce, grants Major Lifeforce | +2 ancient (Mage) / +2 resilience (Knight) |
| `seek_power` (decision) | Free. CD: 1-2 yrs. | Grants Minor Lifeforce (beast/source/knight contest) or Major (Mage ancient/harvest) | +1-2 school (Mage) / +1-2 slaughter/vanguard/resilience (Knight) |
| `bm_manifest_superior_lifeforce_decision` | 250 piety + Minor + Major Lifeforce. Learning check. | Consumes Minor + Major upfront. Crit success: Superior. Success: Superior + 1 yr Major exhaustion. Fail: 3 yr Major exhaustion + refund Major. Crit fail: 3 yr Major + 1 yr Minor exhaustion. | +2 to +8 ancient |
| `blood_golem_creation_decision` (decision) | 500 piety + Superior Lifeforce. | Consumes `lifeforce_modifier_superior` | +5 bloodline |
| `bm_cast_blood_magic_minor_decision` | 25-100 piety + Minor Lifeforce. | Consumes `lifeforce_modifier_minor` | +1 enlightenment / +2 bloodline / +2 resilience |
| `bm_cast_blood_magic_major_decision` (Empowerment/Bloodline/Education/Runes/Traits) | 150-350 piety + Major Lifeforce. | Consumes `lifeforce_modifier_major` (plus minor for runes) | +3-5 track XP |
| `bm_cast_blood_magic_superior_decision` (Mastery/New Edu/Superior Rune/Ascended Traits/Golem) | 200-1000 piety + Superior Lifeforce. | Consumes `lifeforce_modifier_superior` | +5-10 track XP |
| `bm_heal_ailment` | 15 / 35 / 100 piety + Lifeforce. | Minor: consumes Minor; Major: consumes Major; Deadly: consumes Minor & Major | Minor: +2 benediction (Mage) / +2 resilience (Knight self) / +1 vanguard & +1 benediction (Knight ally); Major: +4 benediction; Deadly: +8 benediction |
| `make_blood_knight_interaction` | 100 piety + Major Lifeforce. | Consumes `lifeforce_modifier_major` | +4 benediction |
| `empower_blood_knight_interaction` (Minor option) | Minor Lifeforce. | Consumes `lifeforce_modifier_minor` | +2 benediction |
| `empower_blood_knight_interaction` (Major option) | Major Lifeforce. | Consumes `lifeforce_modifier_major` | +4 benediction |
| `bm_bless_bloodline_interaction` | 35 piety + Minor Lifeforce. | Consumes `lifeforce_modifier_minor` | +2 bloodline |
| `grant_lifeforce_interaction` | 25p (Minor) or 50p (Major) + Lifeforce. | Consumes actor's Lifeforce, grants to target | +1 / +2 enlightenment |
| `grant_lifeforce_interaction_reversed` | 25 piety + Major Lifeforce. | Consumes `lifeforce_modifier_major`, grants target minor | +4 benediction |

## Where the details live

| Piece | File |
| --- | --- |
| Lifeforce modifiers | `common/modifiers/bm_lifeforce.txt` |
| Temporary backlash effects | `common/scripted_effects/bm_blood_magic_temporary_effects.txt` |
| Cast consumption effects | `common/scripted_effects/bm_blood_magic_used_effects.txt` |
| Harvesting interactions | `common/character_interactions/bm_drain_lifeforce.txt` |
| Duel fatality harvesting | `common/on_action/bm_duel_on_actions.txt` |
| Manifestation decisions | `common/decisions/get_lifeforce/bm_manifest_lifeforce.txt`, `bm_manifest_superior_lifeforce.txt` |
| Mass harvesting decision | `common/decisions/bm_mass_lifedrain_prisoners.txt` |
| Story panel stack tally | `common/scripted_effects/bm_blood_mage_story_list_effects.txt` |

## Gotchas

- Positive stacks never expire on their own; only removed by script consumption effects.
- Scripted cast consumption in `bm_blood_magic_used_effects.txt` removes the positive modifier and applies the corresponding temporary negative exhaustion modifier.
