# Architecture docs & subsystem index

Architecture specs for the **Blood Mages** mod (CK3 1.20.*). Living specs of current state only. Generic CK3 guidance lives in `.agents/rules/`, not here.

## Subsystem directory

| Document | Topic | Key Files |
| --- | --- | --- |
| [`blood-mage-magic-tiers.md`](blood-mage-magic-tiers.md) | Minor, Major, Superior Blood Magic tiers | `common/decisions/cast_magic/` |
| [`blood-mage-traits.md`](blood-mage-traits.md) | Lifestyle traits: Acolyte, Mage, Archmage | `common/traits/bm_blood_mage_trait.txt` |
| [`blood-mage-bloodlust.md`](blood-mage-bloodlust.md) | Bloodlust track mechanics, martial & duels | `common/traits/bm_blood_mage_trait.txt` |
| [`blood-mage-track-xp.md`](blood-mage-track-xp.md) | XP master hub & shared tracks (`ancient`, `enlightenment`, `benediction`) | `common/scripted_effects/bm_trait_track_xp_gain_effects.txt` |
| [`blood-mage-track-xp-mage.md`](blood-mage-track-xp-mage.md) | Blood Mage XP tracks (`bloodline`, `hematurgy`, `bloodlust`) | `common/scripted_effects/bm_trait_track_xp_gain_effects.txt` |
| [`blood-mage-lifeforce.md`](blood-mage-lifeforce.md) | Lifeforce resource, modifiers, sinks & sources | `common/modifiers/bm_lifeforce.txt` |
| [`blood-mage-blood-runes.md`](blood-mage-blood-runes.md) | 5 Galdrastafir staves, capstones, Duchy Temples | `common/modifiers/bm_blood_runes_modifiers.txt`, `common/buildings/` |
| [`blood-mage-decisions.md`](blood-mage-decisions.md) | Decisions catalog, costs, requirements | `common/decisions/` |
| [`blood-mage-interactions.md`](blood-mage-interactions.md) | Character interactions, healing, trait theft | `common/character_interactions/` |
| [`blood-mage-duels-and-education.md`](blood-mage-duels-and-education.md) | Initiation duels, congenital traits, education | `events/bm_duel_events.txt` |
| [`blood-mage-golems.md`](blood-mage-golems.md) | Blood Golems lifecycle, creation, house roster | `events/bm_blood_golem_events.txt` |
| [`blood-mage-dynasty.md`](blood-mage-dynasty.md) | Dynasty house modifiers, bloodline mechanics | `common/dynasties/`, `common/dynasty_houses/` |
| [`blood-mage-domicile-buildings.md`](blood-mage-domicile-buildings.md) | 5-tier Blood Shrine line (camp & estate) | `common/domiciles/buildings/` |
| [`blood-mage-religions.md`](blood-mage-religions.md) | Blóðtrú religion family, rites, holy sites | `common/religion/` |
| [`blood-mage-story.md`](blood-mage-story.md) | Blood Magic Situation panel & story cycles | `common/story_cycles/` |
| [`blood-mage-prevalence-and-lifecycle.md`](blood-mage-prevalence-and-lifecycle.md) | Trait distribution, inheritance, pulses | `common/on_action/` |
| [`blood-mage-culture.md`](blood-mage-culture.md) | Icelandic culture, traditions, saga names & Day 1 setup | `common/culture/`, `history/cultures/` |
| [`blood-mage-game-rules.md`](blood-mage-game-rules.md) | Campaign game rules & settings | `common/game_rules/` |
| [`blood-mage-events-overview.md`](blood-mage-events-overview.md) | Event mapping across all namespaces | `events/` |
| [`blood-mage-shared-scripting.md`](blood-mage-shared-scripting.md) | Shared triggers, opinion modifiers, nicknames | `common/scripted_triggers/` |
| [`blood-mage-character-modifiers.md`](blood-mage-character-modifiers.md) | Character modifiers, dynamic scaling & scope rules | `common/modifier_definition_formats/` |

## Writing rules

- **Current state only.** No history, changelog, "previously"/"now". Rewrite text so it is true today. History belongs in the PR/branch doc.
- **Specs, not prose.** Compact tables of identifiers, `Cost`, `Cooldown`, `Req`, `XP`, `Benefit`. No roleplay or adjectives. Complete mechanical numbers stay (costs, brackets, XP, cooldowns, duel math).
- **Collapse repeats.** Multi-tier tracks: state the repeating step once, list milestones (10/50/100 XP), not identical rows.
- **Link, don't duplicate.** Point to the owning doc or `.agents/rules/`.
- Identifiers exactly as in script; grep to confirm they exist. Backticks for files and identifiers. English only; plain markdown (no BOM).

## Doc structure

1. **Summary**: 1–3 lines on what it is and how it ties to Lifeforce, Devotion, tracks, bloodlust track.
2. **Spec**: tables and short bullets.
3. **Where**: concept → file paths.
4. **Gotchas / not verified**: only when real.

## Maintenance

- Read the matching doc before changing a subsystem; update it in the same change when a concept is added, removed or rewired (not for pure tuning of unlisted values).
- New subsystem = new `blood-mage-<subsystem>.md` plus an index row in the directory table above.
