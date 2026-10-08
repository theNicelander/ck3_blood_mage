# Blood Mage Story (`bm_blood_mage_story`)

## Executive Summary

Character-bound story cycle powering the "Blood Magic" Situation panel (`window_situation_list.gui`). Provides dedicated management interface for living dynasty blood mages, blood golems, and crimson retinue warriors, alongside situation-exclusive decisions.

## Story Architecture & Rosters

| Component | Scope / Target | Content / Members | Update Trigger |
| --- | --- | --- | --- |
| **Living Dynasty Roster** | Story variable list | All living dynasty members with `lifestyle_blood_mage` | `bm_refresh_blood_magic_rosters_effect` |
| **Blood Golem Roster** | Story variable list | Courtiers possessing `lifestyle_blood_mage` trait belonging to the Golem house (`house_blood_golem`) | Creation, shaping, death, or roster refresh effect |
| **Crimson Retinue Roster** | Story variable list | Courtiers granted Crimson Warrior (`bm_crimson_warrior`) or Champion (`bm_crimson_champion`) modifiers | Empowerment interactions or roster refresh effect |
| **Lifeforce Counters** | Story variables | Cached counts of Minor, Medium, and Major Lifeforce modifiers | Roster refresh (strips and recount stacks) |
| **Situation Decisions** | Hidden decisions (`is_invisible = yes`) | Compact blood magic actions accessible only inside panel | Story cycle decision list |

## Lifecycle & Synchronization

- **Creation:** Initiated once per character via `bm_ensure_blood_mage_story_effect` upon acquiring `lifestyle_blood_mage`.
- **Hooks:** Hooked on game start (`bm_blood_mage_story_on_actions.txt`), birth on-actions (`bm_blood_mage_prevalence_on_actions.txt`), and yearly pulse (`bm_yearly_pulse.txt`).
- **Destruction:** Ends on character death; reinitialized on successor if they are a blood mage.
- **Roster Snapshot Rule:** Golem and retinue lists are static snapshots. Must invoke `bm_refresh_blood_magic_rosters_effect` whenever golems/retinue are created, recruited, or killed.
- **Lifeforce Recount Rule:** Because CK3 script cannot query dynamic modifier stack counts, the refresh effect temporarily removes and re-adds Lifeforce modifiers to recount exact totals. Refresh effects must have zero side effects triggered by modifier changes.

## File Map

| Piece | File |
| --- | --- |
| Story definition | `common/story_cycles/bm_blood_mage_story.txt` |
| Story initialization (`bm_ensure_blood_mage_story_effect`) | `common/scripted_effects/bm_blood_mage_lifecycle_effects.txt` |
| Roster & Lifeforce refresh (`bm_refresh_blood_magic_rosters_effect`) | `common/scripted_effects/bm_blood_mage_story_list_effects.txt` |
| Story script values | `common/script_values/bm_blood_mage_story_values.txt` |
| Story creation on-actions | `common/on_action/bm_blood_mage_story_on_actions.txt` |
| Prevalence story hooks | `common/on_action/bm_blood_mage_prevalence_on_actions.txt` |
| GUI Panel definition | `gui/window_situation_list.gui` |
| Localization | `localization/english/bm_blood_mage_story_l_english.yml` |
