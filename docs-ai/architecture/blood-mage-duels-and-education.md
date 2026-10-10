# Blood Duels and Education Enhancement

## Executive Summary

- **What:** Contested skill duels for initiation, trait theft from prisoners, education upgrades, and mass dungeon execution.
- **Duel Formula:** Uses CK3 skill duel system. Caster attribute compared against defender attribute. Delta scales victory weight.

### Duels & Education Master Table

| Ritual / Action | Type | Trigger / File | Cost & Req | Opponent / Skill | Outcome |
| **Geyser Initiation** | Decision | `bm_blood_cultist_become_blood_mage_decision` / `bm_enhance_blood_ritual_decision` -> `bm_geyser_duel.0001` | Piety or Prestige level >= 2. In Reykjavik or Tsushima. No cooldown; back out freely (0 cost). Both duel options always visible: Learning duel requires Piety level >= 2 and costs 1 Devotion level; Prowess duel requires Prestige level >= 2 and costs 1 Fame level. | Egill Skallagrímsson (Blood Mage & Blood Knight; Learning 20, Martial 18, Prowess 25) | Win Learning: `lifestyle_blood_mage`. Win Prowess: `lifestyle_blood_knight`. Lose: wound, stress, or mental/physical trauma. Retries on failure without paying level again, or allows backing out. |
| **Trait Theft** | Interaction | `trait_drain_prisoner_event_interaction` -> `bm_trait_drain.001` | Piety. Prisoner has positive congenital trait caster lacks. | Prisoner (Prowess/Learning) | Win: Steals trait from captive. Captive drained. Lose: Backlash modifier. |
| **Upgrade Education (1★–4★)** | Decision | `bm_cast_blood_magic_major_decision` -> `bm_education_enhance.txt` | Scaled piety + Major Lifeforce. CD: 2 yrs. | Mental duel (Learning) | Win: Upgrades education star tier up to tier 4. Lose: Backlash modifier. |
| **Master Education (5★)** | Decision | `bm_cast_blood_magic_superior_decision` -> `bm_education_master_events.txt` | Scaled piety + Superior Lifeforce. CD: 2 yrs. | Mental duel (Discipline skill) | Win: Upgrades 4-star to legendary 5-star tier. Lose: Superior backlash. |
| **New Education** | Decision | `bm_cast_blood_magic_superior_decision` -> `bm_education_new.txt` | 1000 piety + Superior Lifeforce. CD: 2 yrs. | Self-ritual | Grants an additional, secondary education trait at tier 1. |

| **Mass Lifedrain** | Decision | `bm_mass_lifedrain_prisoners` -> `bm_mass_lifedrain.txt` | Piety per prisoner. Dungeon has prisoners. | Uncontested execution | Kills prisoners (`death_lifedrain_reason`). Awards Lifeforce + hematurgy XP. Standard tyranny/kinslaying rules apply. |

## Key Mechanics

- **Trait Theft Scaling:** Easier as caster gains total blood mage XP (`trait_drain_easier_with_xp`). Harder against higher-tier traits (`trait_drain_harder_per_trait_modifier`).
- **Education Gating:**
  - Upgrade 1->2, 2->3, 3->4: Managed in Major Blood Magic (`bm_cast_blood_magic_major_decision`).
  - Upgrade 4->5 (Mastery): Gated behind Superior Blood Magic (`bm_cast_blood_magic_superior_decision`) requiring Superior Lifeforce.
  - Second Education: Requires at least one 5-star education and Superior Lifeforce.
- **Mass Execution:** Options to drain all prisoners or preserve prisoners with positive congenital traits.

## Where the details live

| Piece | File |
| --- | --- |
| Geyser duel events | `events/bm_geyser_duel_events.txt` (`bm_geyser_duel.0001`) |
| Initiation decisions | `common/decisions/become_mage/bm_become_blood_mage_decision.txt` |
| Trait drain interaction | `common/character_interactions/bm_drain_trait.txt` |
| Trait drain events | `events/bm_trait_drain_events.txt` (`bm_trait_drain.001`) |
| Trait drain duel values | `common/script_values/bm_drain_duel_values.txt` |
| Education events | `events/bm_education_enhance.txt`, `bm_education_master_events.txt`, `bm_education_new.txt` |
| Education duel effect | `common/scripted_effects/bm_education_duel_effect.txt` |
| Education costs & XP | `common/script_values/bm_education_enhancement_piety_cost.txt`, `bm_xp_requirement_values.txt` |
| Mass lifedrain decision | `common/decisions/bm_mass_lifedrain_prisoners.txt` |
| Mass lifedrain event | `events/bm_mass_lifedrain.txt` |
| Execution effects | `common/scripted_effects/bm_drain_all_prisoners_effects.txt` |

## Gotchas

- Trait drain requires prisoner to hold congenital traits the caster does NOT already possess.
- Mass lifedrain triggers vanilla tyranny and kinslayer flags if prisoners lack rightful execution reasons.
