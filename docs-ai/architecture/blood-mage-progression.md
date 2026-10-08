# Blood Mage Progression

## Executive Summary

- **What:** Dynamic XP acquisition across 5 Blood Mage tracks and 7 Crimson Empowerment tracks.
- **Rule:** Max 100 XP per track. XP added via `add_xp_bm_dynamic` or `add_crimson_empowerment_xp`.

### XP Sources by School

| School Track | Primary XP Source | Amount | Notes |
| --- | --- | --- | --- |
| `ancient` | Yearly pulse on-action | +1 XP / yr | +1 bonus roll if `ancient_attuned` (50% chance). |
| `enlightenment` | Self-cast spells (`bm_cast_blood_magic_self_*`) | +1 to +3 XP | Manifest Lifeforce (+1), Golem (+3), CE channel (+3). |
| `bloodline` | Channel Bloodline decision | +5 XP / cast | +5% yearly chance per house crimson modifier. |
| `benediction` | Cure disease & grant power to others | +1 to +3 XP | Minor cure/warrior (+1), major cure/champion (+2), benediction cure (+3). |
| `hematurgy` | Lifedrain interactions & lethal duel kills | +1 to +2 XP | Prisoner/courtier drain (+1), trait drain (+2), lethal combat kill (+2). |
| **All CE Tracks** | Channel Crimson Empowerment decision | +10 XP / channel | Dedicated track selected in event `bm_crimson_empowerment_event.001`. |

### Ritual XP Gates Table

Defined in `common/script_values/bm_xp_requirement_values.txt`:

| Ritual / Action | Gated By | Required XP Value | Target Effect |
| --- | --- | --- | --- |
| `bm_create_blood_golem` | Learning XP | 50 XP (`required_xp_blood_golem`) | Crafting blood golem construct |
| `bm_enhance_education_decision` (Lvl 2->3) | CE Track XP | 10 XP (`education_level_2_cost_xp`) | Upgrades education to 3-star |
| `bm_enhance_education_decision` (Lvl 3->4) | CE Track XP | 30 XP (`education_level_3_cost_xp`) | Upgrades education to 4-star |
| `bm_enhance_education_decision` (Lvl 4->5) | CE Track XP | 50 XP (`education_level_4_cost_xp`) | Upgrades education to 5-star |
| `bm_cast_blood_magic_self_major` (New Ed) | CE Track XP | 75 XP (`required_xp_new_education`) | Adds secondary education trait |
| Inscribe Minor Blood Rune | CE Track XP | 25 XP (`bm_blood_rune_minimum_xp`) | Inscribes `minor_crimson_rune_modifier` |
| Inscribe Major Blood Rune | CE Track XP | 50 XP (`bm_blood_rune_minimum_xp`) | Upgrades to `major_crimson_rune_modifier` |
| Inscribe Superior Blood Rune | CE Track XP | 100 XP (`bm_blood_rune_minimum_xp`) | Upgrades to `superior_crimson_rune_modifier` |
| `heal_disease_benediction` | Benediction XP | 50 XP | Cures permanent ailments (blind, infirm, etc.) |

## Where the details live

| Piece | File |
| --- | --- |
| Dynamic XP effects | `common/scripted_effects/bm_trait_track_xp_gain_effects.txt` |
| XP requirement script values | `common/script_values/bm_xp_requirement_values.txt` |
| Piety costs | `common/script_values/bm_drain_piety_cost.txt`, `bm_blood_rune_cost.txt`, `bm_golem_piety_values.txt` |
| Cost scaling modifiers | `common/scripted_modifiers/bm_cost_modifiers.txt` |
| AI value modifiers | `common/scripted_modifiers/bm_ai_value_modifiers.txt` |
| Blood Mage trait tracks | `common/traits/bm_blood_mage_trait.txt` |
| Crimson Empowerment tracks | `common/traits/bm_crimson_empowerment_trait.txt` |

## Key Mechanics & Gotchas

- **Hard Cap:** Tracks cap strictly at 100 XP. Any XP earned beyond 100 is discarded by the engine.
- **Shared Helpers:** Always grant XP via `add_xp_bm_dynamic` or `add_crimson_empowerment_xp`. Never use raw `add_trait_xp` inline in decisions.
