# Architecture docs index

Rules (`.agents/rules/`) say how to write CK3 script in general. These docs say how this mod implements things. Read the doc matching the code you are changing, and update it in the same change (see `AGENTS.md` in this folder).

## Path to doc

| Path | Doc |
| --- | --- |
| `common/story_cycles/bm_blood_mage_story.txt`, `bm_blood_mage_story_list_effects.txt`, `bm_blood_mage_story_values.txt` | `blood-mage-story.md` |
| `common/decisions/bm_*` | `blood-mage-decisions.md` |
| `common/character_interactions/bm_*` | `blood-mage-interactions.md` |
| `common/traits/bm_*_trait.txt` | `blood-mage-traits.md`, `blood-mage-crimson-empowerment.md`, `blood-mage-trait-inheritance.md` |
| `common/scripted_effects/bm_trait_track_xp_gain_effects.txt`, `common/script_values/bm_xp_requirement_values.txt`, `common/scripted_modifiers/bm_ai_value_modifiers.txt`, `bm_cost_modifiers.txt` | `blood-mage-progression.md` |
| `common/on_action/bm_blood_mage_prevalence_on_actions.txt`, `bm_yearly_pulse.txt`, `common/scripted_effects/bm_blood_mage_lifecycle_effects.txt` | `blood-mage-prevalence-and-lifecycle.md`, `blood-mage-trait-inheritance.md` |
| `common/game_rules/bm_game_rules.txt` | `blood-mage-game-rules.md` |
| `common/modifiers/bm_lifeforce.txt`, `bm_blood_magic_*_effects.txt` | `blood-mage-lifeforce.md` |
| `common/buildings/bm_dutchy_buildings.txt`, `common/modifiers/bm_blood_runes_modifiers.txt` | `blood-mage-blood-runes.md` |
| `bm_golem_duel_effect.txt`, `bm_create_blood_golem.txt`, `events/bm_blood_golem_events.txt` | `blood-mage-golems.md` |
| `common/dynasty_houses/`, `common/dynasties/`, `bm_channel_dynasty_modifiers.txt` | `blood-mage-dynasty.md` |
| `bm_drain_trait_effects.txt`, `bm_education_duel_effect.txt`, `common/script_values/bm_drain_duel_values.txt` | `blood-mage-duels-and-education.md` |
| `events/bm_*` | `blood-mage-events-overview.md` |
| `common/religion/**`, `bm_religion_conversion_effects.txt`, `bm_reformation_repair_*` | `blood-mage-religions.md` |
| `common/scripted_triggers/bm_triggers.txt`, `common/opinion_modifiers/`, `common/nicknames/`, `common/deathreasons/`, `gui/*texticons*` | `blood-mage-shared-scripting.md` |

## Docs

| Doc | One line |
| --- | --- |
| `blood-mage-story.md` | The Blood Magic panel (story cycle) and its rosters |
| `blood-mage-decisions.md` | Actions a blood mage can take and the routes into blood magic |
| `blood-mage-interactions.md` | Draining, granting, curing and self-casting interactions |
| `blood-mage-traits.md` | The lifestyle traits and their progression tracks |
| `blood-mage-trait-inheritance.md` | How the trait propagates by inheritance and birth |
| `blood-mage-crimson-empowerment.md` | Crimson Empowerment trait and warrior retinue |
| `blood-mage-progression.md` | XP gains, requirement gates, cost scaling, AI weighting |
| `blood-mage-prevalence-and-lifecycle.md` | Trait acquisition, retention and yearly pulse |
| `blood-mage-game-rules.md` | Campaign game rules |
| `blood-mage-lifeforce.md` | The Lifeforce resource |
| `blood-mage-blood-runes.md` | Crimson Runes and university buildings |
| `blood-mage-golems.md` | Blood golem lifecycle |
| `blood-mage-dynasty.md` | Bloodline house modifiers and the Golem house |
| `blood-mage-duels-and-education.md` | Duels, trait draining, education, mass lifedrain |
| `blood-mage-events-overview.md` | Event files mapped to their triggers |
| `blood-mage-religions.md` | Blóðtrú, faiths, rites, holy sites |
| `blood-mage-shared-scripting.md` | Shared triggers, opinions, nicknames, icons, compat |
