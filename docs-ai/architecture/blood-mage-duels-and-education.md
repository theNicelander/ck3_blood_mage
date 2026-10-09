# Blood Duels and Education Enhancement

## Executive Summary

- **What:** Contested skill duels for initiation, trait theft from prisoners, education upgrades, and mass dungeon execution.
- **Duel Formula:** Uses CK3 skill duel system. Caster attribute compared against defender attribute. Delta scales victory weight.

### Duels & Education Master Table

| Ritual / Action | Type | Trigger / File | Cost & Req | Opponent / Skill | Outcome |
| --- | --- | --- | --- | --- | --- |
| **Geyser Initiation** | Decision | `bm_become_blood_mage_ritual_decision` -> `bm_geyser_duel.0001` | 250 piety. In Reykjavik or Tsushima. CD: 5 yrs. | 111-yr hermit (Learning) | Win: `lifestyle_blood_mage`. Lose: wound, stress, or scarred. |
| **Trait Theft** | Interaction | `trait_drain_prisoner_event_interaction` -> `bm_trait_drain.001` | Piety. Prisoner has positive congenital trait caster lacks. | Prisoner (Prowess/Learning) | Win: Steals trait from captive. Captive drained. Lose: Backlash modifier. |
| **Upgrade Education** | Decision | `bm_improve_education_decision` -> `bm_education_enhance.txt` | Scaled piety + Major Lifeforce. Req: CE XP (10-50). CD: 2 yrs. | Mental duel (Learning) | Win: Upgrades education star tier (up to tier 5). Lose: Stress / failure. |
| **New Education** | Decision | `bm_new_education_decision` -> `bm_education_new.txt` | 1000 piety + Major Lifeforce. Req: 75 CE XP. CD: 2 yrs. | Self-ritual (Learning) | Grants an additional, secondary education trait at tier 1. |

| **Mass Lifedrain** | Decision | `bm_mass_lifedrain_prisoners` -> `bm_mass_lifedrain.txt` | Piety per prisoner. Dungeon has prisoners. | Uncontested execution | Kills prisoners (`death_lifedrain_reason`). Awards Lifeforce + hematurgy XP. Standard tyranny/kinslaying rules apply. |

## Key Mechanics

- **Trait Theft Scaling:** Easier as caster gains total blood mage XP (`trait_drain_easier_with_xp`). Harder against higher-tier traits (`trait_drain_harder_per_trait_modifier`).
- **Education Gating:**
  - Upgrade 2->3: Req 10 CE XP (`education_level_2_cost_xp`).
  - Upgrade 3->4: Req 30 CE XP (`education_level_3_cost_xp`).
  - Upgrade 4->5: Req 50 CE XP (`education_level_4_cost_xp`).
  - Second Education: Req 75 CE XP (`required_xp_new_education`).
- **Mass Execution:** Options to drain all prisoners or preserve prisoners with positive congenital traits.

## Where the details live

| Piece | File |
| --- | --- |
| Duel mechanics guide | `events/_duels.md` |
| Geyser duel events | `events/bm_geyser_duel_events.txt` (`bm_geyser_duel.0001`) |
| Initiation decisions | `common/decisions/bm_become_blood_mage_decision.txt` |
| Trait drain interaction | `common/character_interactions/bm_drain_trait.txt` |
| Trait drain events | `events/bm_trait_drain_events.txt` (`bm_trait_drain.001`) |
| Trait drain duel values | `common/script_values/bm_drain_duel_values.txt` |
| Education events | `events/bm_education_enhance.txt`, `bm_education_new.txt` |
| Education duel effect | `common/scripted_effects/bm_education_duel_effect.txt` |
| Education costs & XP | `common/script_values/bm_education_enhancement_piety_cost.txt`, `bm_xp_requirement_values.txt` |
| Mass lifedrain decision | `common/decisions/bm_mass_lifedrain_prisoners.txt` |
| Mass lifedrain event | `events/bm_mass_lifedrain.txt` |
| Execution effects | `common/scripted_effects/bm_drain_all_prisoners_effects.txt` |

## Gotchas

- Trait drain requires prisoner to hold congenital traits the caster does NOT already possess.
- Mass lifedrain triggers vanilla tyranny and kinslayer flags if prisoners lack rightful execution reasons.
