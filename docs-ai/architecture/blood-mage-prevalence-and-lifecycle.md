# Blood Mage Prevalence and Lifecycle

> Living document. Follow `AGENTS.md` in this folder: concepts only, no numbers. Update it when spawn rates, birth inheritance, yearly pulses, or lifecycle effects change.

## Purpose

Prevalence and lifecycle logic controls how blood mages appear, spread, age, and perish across the medieval world. It ensures that the frequency of blood mages conforms to player-configured game rules, prevents uncontrolled runaway proliferation among AI rulers, and reliably initializes necessary story cycles upon trait acquisition.

## Concepts

- **Lifecycle Entrypoint.** Every route that awards `lifestyle_blood_mage` is routed through the central scripted effect `bm_become_blood_mage_effect`. This guarantees that the Blood Magic story cycle is immediately created (`bm_ensure_blood_mage_story_effect`) and prevalence review flags are applied.
- **Birth Inheritance.** On-action `on_birth_child` triggers `bm_apply_blood_mage_prevalence_at_birth`. Depending on game rule settings, children born to blood mage parents may inherit the trait, and rare spontaneous manifestations can occur (see `blood-mage-trait-inheritance.md`).
- **Retention Filtering.** When game rules restrict prevalence (e.g. Rare, Extremely Rare, or Player Only), `bm_apply_blood_mage_prevalence_retention_effect` rolls against retention chances. AI characters who fail retention have the trait stripped immediately upon generation.
- **Yearly Review Pulse.** `yearly_blood_mage_pulse` in `common/on_action/bm_yearly_pulse.txt` periodically audits characters across the realm, firing yearly progression events (`events/bm_yearly_events.txt`) and enforcing prevalence caps on unreviewed AI mages.
- **Character Templates.** Preset templates in `bm_character_templates.txt` provide baseline parameters for spawning new blood mages, wandering practitioners, and artificial constructs.

## Mod conventions

- **Single entry point.** The trait is granted only through `bm_become_blood_mage_effect`, which also creates the story. Never use a bare `add_trait = lifestyle_blood_mage` elsewhere.
- **AI acquisition and retention follow the prevalence rule.** They go through the prevalence effects and scripted modifiers, not hard-coded chances.

## Where the details live

| Piece | File |
| --- | --- |
| Lifecycle scripted effects | `common/scripted_effects/bm_blood_mage_lifecycle_effects.txt` |
| Birth prevalence on-actions | `common/on_action/bm_blood_mage_prevalence_on_actions.txt` |
| Yearly pulse on-actions | `common/on_action/bm_yearly_pulse.txt` |
| Prevalence AI modifiers | `common/scripted_modifiers/bm_blood_mage_prevalence_modifiers.txt` |
| Yearly blood mage events | `events/bm_yearly_events.txt` |
| Character templates | `common/scripted_character_templates/bm_character_templates.txt` |
| Prevalence game rules | `common/game_rules/bm_game_rules.txt` (`bm_blood_mage_prevalence`) |

## How the parts connect

- When any decision, interaction, or event bestows blood magic, calling `bm_become_blood_mage_effect` adds `lifestyle_blood_mage`, creates `bm_blood_mage_story`, and marks `bm_blood_mage_prevalence_reviewed`.
- `bm_blood_mage_prevalence_modifiers.txt` scales AI willingness to take blood magic decisions according to the active game rule setting.
- The yearly pulse reviews any blood mages who escaped birth/creation checks and applies retention checks if required.
- Natural death, lifedrain execution, or golem collapse cleans up stories and rosters automatically.

## Gotchas

- Never apply `add_trait = lifestyle_blood_mage` directly without calling `bm_become_blood_mage_effect`; doing so bypasses story cycle initialization and leaves the character without the Blood Magic panel.
- Under `bm_prevalence_player_only`, any AI character attempting to acquire the trait will immediately have it stripped by the retention effect.

## Not verified

Global AI character performance impact during late-game yearly pulses on heavily populated world maps with `bm_prevalence_more_frequent`.
