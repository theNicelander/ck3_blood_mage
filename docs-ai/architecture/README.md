# Mod architecture & subsystem index

Architecture specs for the **Blood Mages** mod (CK3 1.20.*). Living specs of current state only; see `AGENTS.md` in this directory for authoring rules.

## Subsystem directory

| Document | Topic | Key Files |
| --- | --- | --- |
| [`blood-mage-magic-tiers.md`](blood-mage-magic-tiers.md) | Minor, Major, Superior Blood Magic tiers | `common/decisions/cast_magic/` |
| [`blood-mage-traits.md`](blood-mage-traits.md) | Lifestyle traits: Mage, Knight, Power | `common/traits/bm_*_trait.txt` |
| [`blood-mage-blood-knight.md`](blood-mage-blood-knight.md) | Blood Knight mechanics, combat hooks, MaA | `common/men_at_arms_types/` |
| [`blood-mage-blood-power.md`](blood-mage-blood-power.md) | Secondary Power trait, 6 progression tracks | `common/traits/bm_power_trait.txt` |
| [`blood-mage-track-xp.md`](blood-mage-track-xp.md) | XP master hub & shared tracks (`ancient`, `enlightenment`, `benediction`) | `common/scripted_effects/bm_trait_track_xp_gain_effects.txt` |
| [`blood-mage-track-xp-mage.md`](blood-mage-track-xp-mage.md) | Blood Mage XP tracks (`bloodline`, `hematurgy`) | `common/scripted_effects/bm_trait_track_xp_gain_effects.txt` |
| [`blood-mage-track-xp-knight.md`](blood-mage-track-xp-knight.md) | Blood Knight XP tracks (`vanguard`, `slaughter`) | `common/scripted_effects/bm_trait_track_xp_gain_effects.txt` |
| [`blood-mage-track-xp-power.md`](blood-mage-track-xp-power.md) | Blood Power XP tracks (6 secondary tracks) | `common/scripted_effects/bm_trait_track_xp_gain_effects.txt` |
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
| [`blood-mage-game-rules.md`](blood-mage-game-rules.md) | Campaign game rules & settings | `common/game_rules/` |
| [`blood-mage-events-overview.md`](blood-mage-events-overview.md) | Event mapping across all namespaces | `events/` |
| [`blood-mage-shared-scripting.md`](blood-mage-shared-scripting.md) | Shared triggers, opinion modifiers, nicknames | `common/scripted_triggers/` |
