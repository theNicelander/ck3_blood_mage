# Architecture Docs Index

Rules (`.agents/rules/`) say how to write CK3 script in general. These docs say how this mod implements things. Read the doc matching the code you are changing, and update it in the same change (see `AGENTS.md` in this folder). All architecture docs follow high-density caveman style: executive summaries, master tables, costs, requirements, XP gains, benefits; zero roleplay fluff.

## Path to Doc

Player-facing text has an English source and a complete Russian translation in matching
`localization/english/` and `localization/russian/` files. The
`scripts/bm_validate_localization.py` checker enforces matching keys, CK3 format, protected
tokens, local aliases, and explicit `bm_` UI references. GitHub Actions runs it together
with the repository format checker. Shared terminology: Lifeforce = Жизненная сила;
Crimson Empowerment = Багровое усиление; Hematurgy = Гематургия.

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

## Docs Reference

| Doc | Coverage |
| --- | --- |
| `blood-mage-traits.md` | Core `lifestyle_blood_mage` trait, 5 schools master table, milestones, acquisition triggers |
| `blood-mage-crimson-empowerment.md` | `lifestyle_crimson_empowerment` trait, 7 tracks master table, costs, spell unlocks, retinue |
| `blood-mage-dynasty.md` | 7 house modifiers, costs, cooldowns, yearly XP loop, Golem cadet house |
| `blood-mage-blood-runes.md` | Blood Runes tiers 1-3, costs, requirements, passive rolls, Blood Universities 0-3 |
| `blood-mage-decisions.md` | Master decisions table: panels, costs, cooldowns, requirements, XP gains, effects |
| `blood-mage-duels-and-education.md` | Duels, trait drain, education upgrades/re-spec, mass lifedrain, exact XP gates |
| `blood-mage-events-overview.md` | Complete event namespace, trigger, and outcome matrix across all event files |
| `blood-mage-game-rules.md` | Master game rules table: all 5 campaign rules, settings, and behavioral impacts |
| `blood-mage-golems.md` | Golem lifecycle matrix: creation costs, stat template, shaping duels, roster management |
| `blood-mage-interactions.md` | Master character interactions table: target filters, costs, cooldowns, XP gains, effects |
| `blood-mage-lifeforce.md` | Lifeforce modifiers table: Minor/Medium/Major bonuses, sources and sinks matrix |
| `blood-mage-prevalence-and-lifecycle.md` | Prevalence game rules matrix, birth pipeline diagram, lifecycle scripted effects |
| `blood-mage-progression.md` | XP sources by track, AI evaluation formulas, ritual XP gates |
| `blood-mage-religions.md` | Blóðtrú religious family, 3 faiths, rites, holy site hierarchy, identity doctrine, cult decisions |
| `blood-mage-shared-scripting.md` | Shared triggers, opinion modifiers, death reasons, text icons, overhaul compat guards |
| `blood-mage-story.md` | `bm_blood_mage_story` cycle, Situation panel, rosters (dynasty mages, golems, retinue) |
| `blood-mage-trait-inheritance.md` | Direct inheritance odds (25%/100%), birth prevalence pipeline, non-genetic rules |
