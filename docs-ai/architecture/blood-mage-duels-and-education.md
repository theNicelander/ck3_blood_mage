# Blood Duels and Education Enhancement

> Living document. Follow `AGENTS.md` in this folder: concepts only, no numbers. Update it when duel formulas, trait-draining, education improvement or mass execution mechanics change.

## Purpose

Blood magic can be used to violently extract knowledge, congenital traits, and vitality from prisoners, or channel immense power inward to rewrite the caster's intellect and education. These high-stakes interactions rely on CK3's duel mechanics, pitting the caster's supernatural force against the target's mental and physical resistance.

## Concepts

- **Duel Mechanics.** As outlined in `events/_duels.md`, blood magic duels calculate victory odds by comparing the caster's relevant attribute against the opponent's attribute. A `compare_modifier` multiplies this stat delta and adds it to the outcome weights, producing probabilistic success or failure.
- **Reykjavik Initiation Duel.** Through `bm_reykjavik_blood_mage_duel_decision`, an aspiring outsider challenges a temporary hermit blood mage NPC at the holy site of Reykjavik (`c_vestisland`). The challenge is resolved through a Learning duel with a Prowess bonus, cleanly removing the opponent afterwards and awarding blood magic on victory.
- **Trait Theft (Genetic Drain).** Through `trait_drain_prisoner_event_interaction`, a blood mage challenges a captive to forcibly siphon their positive congenital traits (e.g. intellect, beauty, physique).
  - The duel is made easier as the caster accumulates XP across all blood mage tracks (`trait_drain_easier_with_xp`).
  - High-tier genetic traits provide greater resistance against extraction (`trait_drain_harder_per_trait_modifier`).
  - Failure applies temporary negative modifiers or physical backlash.
- **Education Enhancement.** A blood mage can use major self-cast interactions to either upgrade their existing education trait tier (`bm_cast_blood_magic_self_major_improve_education` / `bm_education_enhance.txt`) or acquire an entirely new secondary education branch (`bm_cast_blood_magic_self_major_new_education` / `bm_education_new.txt`).
- **Mass Lifedrain Executions.** The decision `mass_lifedrain_prisoners_decision` and event `bm_mass_lifedrain.txt` allow a ruler to execute multiple prisoners simultaneously. The scripted effect `lifedrain_execution_effect` manages the executions, applies proper tyranny/kinslaying rules, and converts the victims into Lifeforce.

## Where the details live

| Piece | File |
| --- | --- |
| Duel mechanics guide | `events/_duels.md` |
| Reykjavik initiation duel decision | `common/decisions/bm_reykjavik_blood_mage_duel_decision.txt` |
| Reykjavik duel script values | `common/script_values/bm_reykjavik_duel_values.txt` |
| Trait drain interaction | `common/character_interactions/bm_drain_trait.txt` |
| Trait drain events | `events/bm_trait_drain_events.txt` (`bm_trait_drain.001`) |
| Trait drain script values & modifiers | `common/script_values/bm_drain_duel_values.txt` |
| Trait drain scripted effects | `common/scripted_effects/bm_drain_trait_effects.txt` |
| Education improvement events | `events/bm_education_enhance.txt` |
| New education events | `events/bm_education_new.txt` |
| Education duel effect | `common/scripted_effects/bm_education_duel_effect.txt` |
| Education piety & XP costs | `common/script_values/bm_education_enhancement_piety_cost.txt`, `common/script_values/bm_xp_requirement_values.txt` |
| Mass lifedrain decision | `common/decisions/bm_mass_lifedrain_prisoners.txt` |
| Mass lifedrain event | `events/bm_mass_lifedrain.txt` |
| Execution scripted effects | `common/scripted_effects/bm_drain_all_prisoners_effects.txt` |

## How the parts connect

- Taking `trait_drain_prisoner_event_interaction` initiates a contested duel using values in `bm_drain_duel_values.txt`. Winning strips the trait from the prisoner and awards it to the caster via `bm_drain_trait_effects.txt`.
- Education rituals check learning skills and total blood mage XP. Successful education duels advance education tiers up to tier 5 or grant multi-disciplinary knowledge.
- Mass lifedrain loops through imprisoned characters, applying `death_lifedrain_reason` and granting major Lifeforce stacks to the executioner.

## Gotchas

- Trait draining requires the prisoner to actually possess transferable traits that the caster does not already have.
- Executing prisoners via mass lifedrain still triggers vanilla tyranny and kinslayer flags unless the executioner possesses rightful imprisonment reasons or exempting cultural doctrines.
- Education enhancement costs scale based on the target level being pursued.

## Not verified

AI rulers using mass lifedrain to instantly clear sprawling dungeon populations during sudden realm succession crises.
