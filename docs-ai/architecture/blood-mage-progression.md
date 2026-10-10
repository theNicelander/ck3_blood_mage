# Blood Mage Progression

## Executive Summary

- **What:** Dynamic XP acquisition across 5 Blood Mage schools, 5 Blood Empowerment specializations, and 3 Blood Knight martial tracks (plus shared ancient/benediction).
- **Rule:** Max 100 XP per track. XP added via `add_xp_bm_dynamic`, `add_blood_empowerment_xp`, or `add_blood_knight_xp`.

### XP Sources by School & Track

| School / Track | Primary XP Sources | Amount | Notes |
| --- | --- | --- | --- |
| `ancient` | Yearly pulse, attunement, manifest lifeforce, inscribe blood runes, condense lifeforce | +1 to +10 XP | Pulse (+1), Attuned (+1 roll), Manifest (+3), Superior Manifest (+2 to +8), Runes (+4/+5/+10), Condense (+2). Shared with Blood Knight. |
| `enlightenment` | Education rituals, channeling lifeforce, blood empowerment | +1 to +8 XP | Channel minor (+1), Grant lifeforce (+1/+2), Empowerment (+3), Edu 2-4 (+4), Master Edu (+8), New Edu (+8), Congenital 4-5 (+2). |
| `bloodline` | Childbirth, grant trait, kin blessing, commune, congenital traits, house pulse, golems | +1 to +6 XP | Grant trait (+4/+5), Childbirth (+2/+4), Bless kin (+2), Commune (+2), Purge impurities (+2), Congenital 1-3 (+4), Congenital 4-5 (+6), Empower bloodline (+5), Golems (+5), +10% yearly per house modifier. |
| `benediction` | Cure ailment, make/empower blood knights, restore drained victims | +2 to +8 XP | Heal ailment (+2 minor / +4 major / +8 deadly), Make Blood Knight (+4), Empower Blood Knight (+2/+4), Restore drained (+4). Shared with Blood Knight. |
| `hematurgy` | Prisoner/courtier draining, trait theft, seek power | +1 to +2 XP | Prisoner drain (+1/+2), Courtier drain (+1), Trait theft (+2), Seek power (+1-2). Lethal combat duel kills reserved for Blood Knights. |
| `vanguard` | Battle victories, battle defeat, healing allies | +1 to +5 XP | Commander win (+5), Knight win (+4), Defeat survival (+1), Heal ally (+1), Empowered by Mage (+5/+10). |
| `slaughter` | Single combat fatal kills, tournaments, empowerment | +3 to +10 XP | Single combat fatal kill (+5, yields Minor Lifeforce), Tournament (+3), Empowered by Mage (+5/+10). |
| `resilience` | Manifest lifeforce, defeat survival, self-healing, condense lifeforce, yearly pulse | +1 to +3 XP | Manifest lifeforce (+3), Condense lifeforce (+2), Self-heal (+2), Purge frailty (+2), Defeat survival (+2), Pulse (+1), Empowerment (+3). |
| **All CE Tracks** | Channel Blood Empowerment decision | +10 XP / channel | Dedicated track selected in event `bm_blood_empowerment_event.001` (`dynasty`, `mastery`, `presence`, `prosperity`, `shadows`). |

### Ritual XP Gates Table

Defined in `common/script_values/bm_xp_requirement_values.txt`:

| Ritual / Action | Gated By | Required XP Value | Target Effect |
| --- | --- | --- | --- |
| `bm_create_blood_golem` | Learning XP | 50 XP (`required_xp_blood_golem`) | Crafting blood golem construct |
| `bm_improve_education_decision` (Lvl 2->3) | CE Track XP | 10 XP (`education_level_2_cost_xp`) | Upgrades education to 3-star |
| `bm_improve_education_decision` (Lvl 3->4) | CE Track XP | 30 XP (`education_level_3_cost_xp`) | Upgrades education to 4-star |
| `bm_improve_education_decision` (Lvl 4->5) | CE Track XP | 50 XP (`education_level_4_cost_xp`) | Upgrades education to 5-star |
| `bm_new_education_decision` | CE Track XP | 75 XP (`required_xp_new_education`) | Adds secondary education trait |

| Inscribe Minor Blood Rune | CE Track XP | 25 XP (`bm_blood_rune_minimum_xp`) | Inscribes `minor_blood_rune_modifier` |
| Inscribe Major Blood Rune | CE Track XP | 50 XP (`bm_blood_rune_minimum_xp`) | Upgrades to `major_blood_rune_modifier` |
| Inscribe Superior Blood Rune | CE Track XP | 100 XP (`bm_blood_rune_minimum_xp`) | Upgrades to `superior_blood_rune_modifier` |
| `bm_heal_ailment` (Deadly) | Benediction Tier | Minor + Major Lifeforce, 100 Piety | Cures deadly and permanent ailments (blind, cancer, plague, infirm, etc.) |

## Where the details live

| Piece | File |
| --- | --- |
| Dynamic XP effects | `common/scripted_effects/bm_trait_track_xp_gain_effects.txt` |
| XP requirement script values | `common/script_values/bm_xp_requirement_values.txt` |
| Piety costs | `common/script_values/bm_drain_piety_cost.txt`, `bm_blood_rune_cost.txt`, `bm_golem_piety_values.txt` |
| Cost scaling modifiers | `common/scripted_modifiers/bm_cost_modifiers.txt` |
| AI value modifiers | `common/scripted_modifiers/bm_ai_value_modifiers.txt` |
| Blood Mage trait tracks | `common/traits/bm_blood_mage_trait.txt` |
| Blood Empowerment tracks | `common/traits/bm_blood_empowerment_trait.txt` |

## Key Mechanics & Gotchas

- **Hard Cap:** Tracks cap strictly at 100 XP. Any XP earned beyond 100 is discarded by the engine.
- **Shared Helpers:** Always grant XP via `add_xp_bm_dynamic` or `add_blood_empowerment_xp`. Never use raw `add_trait_xp` inline in decisions.
