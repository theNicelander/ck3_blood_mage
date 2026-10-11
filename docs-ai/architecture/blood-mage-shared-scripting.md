# Shared Scripting and System Utilities

## Executive Summary

Cross-cutting infrastructure supporting Blood Mages. Houses shared scripted triggers, opinion reactions, death reasons, decision groups, UI text icons, and third-party total conversion mod isolation guards.

## Shared System Components

| Category | Component / Asset | File | Description |
| --- | --- | --- | --- |
| **Overhaul Guard** | `is_playing_overhaul_mod` | `common/scripted_triggers/bm_triggers.txt` | Detects total conversions (AGOT, Elder Kings, LOTR) via global variables (e.g. `AGOT_is_loaded`). Protects vanilla references. |
| **Blood Cult Trigger** | `bm_is_blood_cult_faith_trigger` | `common/scripted_triggers/bm_religion_compatibility_triggers.txt` | Evaluates if faith belongs to `rf_blodtru` or possesses `blood_magic_cult_faith` parameter. |
| **Opinion: Beneficiary** | `magic_opinion_positive` | `common/opinion_modifiers/bm_opinions.txt` | Decaying positive opinion bonus toward spellcaster. |
| **Opinion: Initiator** | `made_me_a_blood_mage` | `common/opinion_modifiers/bm_opinions.txt` | High gratitude opinion bonus for bestowing the Blood Mage trait. |
| **Opinion: Victim** | `lifedrained_me` | `common/opinion_modifiers/bm_opinions.txt` | Hostile opinion malus from characters who survived lifedrain. |
| **Death Reason** | `death_lifedrain_reason` | `common/deathreasons/bm_event_deaths.txt` | Assigned when character dies from lifedrain or fatal siphoning duels. |
| **Death Reason** | `death_blood_golem_failed` | `common/deathreasons/bm_event_deaths.txt` | Assigned when golem creation collapses lethally. |
| **Nicknames** | `nick_the_wanderer`, etc. | `common/nicknames/bm_nicknames.txt` | Occult titles granted via milestones and duels. |
| **Decision Group** | `bm_decision_group` | `common/decision_group_types/bm_decision_group_types.txt` | Groups blood magic decisions into unified decision UI tab. |
| **Text Icons** | `@bm_game_rule_icon!`, `@bm_blood_drop!` | `gui/bm_blood_magic_texticons.gui`, `gui/bm_game_rule_texticons.gui` | Registered inline font icons for decisions, game rules, and tooltips. |
| **Religion Icons** | `@bm_blodtru_icon!`, `@bm_ketsudo_icon!` | `gui/shared/bm_texticons_religion.gui` | Inline icons for Blóðtrú family faiths. |

## Mod Conventions & Compatibility Rules

- **Strict Prefixing:** Every custom trigger, modifier, and asset must use `bm_` prefix. Unprefixed names that shadow vanilla are forbidden unless deliberately overriding vanilla core mechanics.
- **Third-Party Isolation:** Never reference third-party traits, faiths, or title tags directly in mod files. Guard conditionally using flags:
  ```pdx
  has_global_variable = AGOT_is_loaded
  ```
- **Modifier Cleanup:** Custom character modifiers must have explicit durations or decaying parameters to prevent infinite stacking upon death or succession.
- **File Integrity:** UTF-8 with BOM (`utf-8-sig`), balanced braces, and trailing newlines enforced across all script files.

## File Map

| Piece | File |
| --- | --- |
| Shared scripted triggers | `common/scripted_triggers/bm_triggers.txt` |
| Religion triggers | `common/scripted_triggers/bm_religion_compatibility_triggers.txt` |
| Custom trigger localization | `common/trigger_localization/bm_trigger_localization.txt` |
| Opinion modifiers | `common/opinion_modifiers/bm_opinions.txt` |
| Nicknames | `common/nicknames/bm_nicknames.txt` |
| Custom death reasons | `common/deathreasons/bm_event_deaths.txt` |
| Decision group definitions | `common/decision_group_types/bm_decision_group_types.txt` |
| Blood magic font icons | `gui/bm_blood_magic_texticons.gui` |
| Game rule font icons | `gui/bm_game_rule_texticons.gui` |
| Religion font icons | `gui/shared/bm_texticons_religion.gui` |
