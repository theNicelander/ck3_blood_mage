# Blood Mage Story (`bm_blood_mage_story`)

## Executive Summary

Character-bound story cycle powering the "Blood Magic" Situation panel (`window_situation_list.gui`) for Blood Mage and Blood Knight rulers. Provides dedicated management interface for living dynasty blood mages, blood golems, and dynasty + court blood knights, alongside blood magic decisions shared with the realm Decisions tab.

## Story Architecture & Rosters

| Component | Scope / Target | Content / Members | Update Trigger |
| --- | --- | --- | --- |
| **Living Dynasty Roster** | Story variable list | All living dynasty members with `lifestyle_blood_mage` | `bm_refresh_blood_magic_rosters_effect` |
| **Blood Knight Roster** | Story variable list (`bm_blood_retinue`) | Courtiers and living dynasty members possessing `lifestyle_blood_knight` trait (de-duplicated) | Roster refresh effect (`bm_refresh_blood_magic_rosters_effect`) |
| **Blood Golem Roster** | Story variable list | Courtiers possessing `lifestyle_blood_mage` trait belonging to the Golem house (`bm_house_golem`) | Creation, shaping, death, or roster refresh effect |
| **Lifeforce Counters** | Story variables | Cached counts of Minor, Major, and Superior Lifeforce modifiers (`bm_lifeforce_minor_stacks`, `bm_lifeforce_major_stacks`, `bm_lifeforce_superior_stacks`) | Roster refresh (strips and recount stacks) |
| **Custom Status Display** | Customizable localization | Real-time readout of disciplines (mage or knight disciplines), Lifeforce stacks, active Attunement, and inscribed Blood Rune | `BM_BLOOD_MAGE_INFORMATION_STRING` evaluated on view |
| **Situation Decisions** | Shared decisions (visible in Situation and Decisions tab) | All Blood Mage and Blood Knight rituals, manifestations, harvesting, seeking power, and elevation actions | Story cycle decision list (`bm_cast_blood_magic_minor_decision`, `bm_cast_blood_magic_major_decision`, `bm_cast_blood_magic_superior_decision`, `bm_manifest_lifeforce_decision`, `bm_manifest_superior_lifeforce_decision`, `mass_lifedrain_prisoners_decision`, `blood_golem_creation_decision`, `seek_power_decision`, `seek_power_decision_wanderer`, `seek_power_decision_blood_knight`, `bm_elevate_to_blood_mage_decision`) |

## Lifecycle & Synchronization

- **Creation:** Initiated once per character via `bm_ensure_blood_mage_story_effect` upon acquiring `lifestyle_blood_mage` or `lifestyle_blood_knight`.
- **Hooks:** Hooked on game start (`bm_blood_mage_story_on_actions.txt`), birth on-actions (`bm_blood_mage_prevalence_on_actions.txt`), and yearly pulse (`bm_yearly_pulse.txt`).
- **Destruction:** Ends on character death; reinitialized on successor if they are a blood mage or blood knight.
- **Roster Snapshot Rule:** Golem and knight lists are static snapshots. Must invoke `bm_refresh_blood_magic_rosters_effect` whenever golems/knights are created, recruited, or killed.
- **Lifeforce Recount Rule:** Because CK3 script cannot query dynamic modifier stack counts, the refresh effect temporarily removes and re-adds Lifeforce modifiers to recount exact totals. Refresh effects must have zero side effects triggered by modifier changes.
- **Icon Branching Rule:** Story cycle `icon.trigger` blocks evaluate in the `story` scope; any character trait checks (`has_trait`) must explicitly scope into `story_owner = { ... }`.

## File Map

| Piece | File |
| --- | --- |
| Story definition | `common/story_cycles/bm_blood_mage_story.txt` |
| Story initialization (`bm_ensure_blood_mage_story_effect`) | `common/scripted_effects/bm_blood_mage_lifecycle_effects.txt` |
| Roster & Lifeforce refresh (`bm_refresh_blood_magic_rosters_effect`) | `common/scripted_effects/bm_blood_mage_story_list_effects.txt` |
| Story script values | `common/script_values/bm_blood_mage_story_values.txt` |
| Story creation on-actions | `common/on_action/bm_blood_mage_story_on_actions.txt` |
| Prevalence story hooks | `common/on_action/bm_blood_mage_prevalence_on_actions.txt` |
| Custom localization | `common/customizable_localization/bm_blood_mage_story_custom_loc.txt` |
| GUI Panel definition | `gui/window_situation_list.gui` |
| Localization | `localization/english/bm_blood_mage_story_l_english.yml` |
