# feat(religion): Migrate to CK3 1.19 religion layout and add initiation faith requirement rule

## Summary of Changes

This PR extracts the religion folder structure migration and related religion mechanics from PR #94 onto the current branch without pulling in unrelated portrait transformations, prevalence rules, or trait inheritance changes.

### 1. CK3 1.19 Religion Folder Layout Migration
* Reorganized `common/religion/` into the official Crusader Kings III 1.19 schema:
  * `common/religion/religions/` → `common/religion/religion_types/`
  * `common/religion/holy_sites/` → `common/religion/holy_site_types/`
  * `common/religion/religion_families/` → `common/religion/religion_family_types/`
  * Added new `common/religion/doctrine_types/bm_doctrine_types.txt`
  * Added new `common/religion/doctrine_group_types/bm_doctrine_group_types.txt`
  * Removed deprecated pre-1.19 folders (`religions/`, `holy_sites/`, `religion_families/`).
* Added hidden `bm_quintessence_identity_doctrine` carrying the parameter `blood_magic_cult_faith = yes` to allow optional submods and external mods to opt in without hard dependencies.
* Added doctrine group icon `gfx/interface/icons/faith_doctrine_groups/bm_quintessence_identity_group.dds`.
* Added 7 standalone Cult of Quintessence heritage variants in `common/religion/religion_types/bm_religion.txt` (Christian, Islamic, Jewish, Eastern, Sinitic, Ásatrú, and Unreformed syncretism).

### 2. Blood Mage Initiation Faith Requirement Rule
* **Game Rule (`common/game_rules/bm_game_rules.txt`)**:
  * Added `bm_initiation_faith_requirement`:
    * `bm_initiation_dedicated_cult` (*Default*): Only characters following the Cult of the Quintessence or a faith explicitly marked with `blood_magic_cult_faith` may perform the initiation ritual.
    * `bm_initiation_cult_or_witchcraft_accepted`: Characters may perform the initiation ritual if following a dedicated blood cult or any faith with the `witchcraft_accepted` doctrine.
* **Compatibility Triggers (`common/scripted_triggers/bm_religion_compatibility_triggers.txt`)**:
  * `bm_is_blood_cult_faith_trigger`: Checks if faith is in `rf_quintessence` or has doctrine parameter `blood_magic_cult_faith`.
  * `bm_meets_blood_mage_initiation_faith_requirement_trigger`: Evaluates player/character eligibility based on the active `bm_initiation_faith_requirement` rule.
* **Decisions**:
  * `bm_blood_cultist_become_blood_mage_decision`: Gated by `bm_meets_blood_mage_initiation_faith_requirement_trigger = yes`.
  * `become_blood_cultist_decision`: Gated by `NOR = { bm_is_blood_cult_faith_trigger = yes }` and executes `bm_convert_to_blood_cult_by_heritage_effect = yes`.

### 3. Conversion Routing & Reformation Repair
* **Heritage Conversion Routing (`common/scripted_effects/bm_religion_conversion_effects.txt`)**:
  * `bm_convert_to_blood_cult_by_heritage_effect` dynamically directs converting characters to the matching Quintessence syncretism faith based on their originating religion family (with Christian syncretism as default fallback).
* **Reformation Repair System**:
  * `common/decisions/bm_reformation_repair_decision.txt`: Allows detaching a premature temporal Head of Faith so players can reform an unreformed cult faith without destroying titles or disrupting the realm.
  * Supported by `bm_can_repair_quintessence_reformation_trigger`, `bm_repair_quintessence_reformation_effect`, and fallback event `bm_reformation_repair.0001` in `events/bm_reformation_repair_events.txt`.

### 4. Localization & Documentation
* Updated `localization/english/bm_religion_l_english.yml`, `bm_game_rules_l_english.yml`, and `bm_decisions_l_english.yml` with names and descriptions for all new faiths, doctrines, rules, and decisions.
* Updated `CHANGELOG.md` with an `## Unreleased` section summarizing the changes.

## Verification
* All script and localization files checked for balanced braces and valid Paradox syntax.
* Verified UTF-8 with BOM on all modified game files.
* Passed `git diff --check` with 0 whitespace errors.
