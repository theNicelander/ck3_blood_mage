# Religions, Faiths and Rites

Describes the religion subsystem of the Blood Mages mod in its current state.

## 1. Purpose

The Cult of Quintessence religion provides an in-game religious foundation for blood magic. It offers a dedicated religious family, distinct syncretic faiths that bridge blood magic with existing global faiths, scripted mainline rites to provide stable ritual traditions, and custom holy sites centered around the volcanic cradle of Iceland.

## 2. Concepts

- **Cult of Quintessence (`quintessence_religion`)**: The overarching religion belonging to the `rf_quintessence` religious family. It venerates the vital current and quintessence of life, featuring Blood Mage and Mystic virtues, holy orders, and tailored theological terminology.
- **Syncretic Blood Faiths**: Seven distinct faiths representing different theological adaptations:
  - `quintessence_faith`: Christian syncretic branch.
  - `quintessence_faith_islamic`: Islamic syncretic branch.
  - `quintessence_faith_jewish`: Jewish syncretic branch.
  - `quintessence_faith_eastern`: Dharmic/Eastern syncretic branch.
  - `quintessence_faith_sinitic`: Taoist/Confucian/Sinitic syncretic branch.
  - `quintessence_faith_asatru`: Norse/Ásatrú branch focused on human sacrifice and warmongering.
  - `quintessence_faith_unreformed`: Syncretic pagan traditionalist branch.
- **Mainline Rites**: Each faith has a 1:1 scripted mainline rite in `common/religion/rite_types/`. These rites carry the core ritual identity, matching tenets, and doctrines of each faith to avoid arbitrary engine-generated dynamic rites.
- **Eminent & Regular Holy Sites**: Holy sites in `common/religion/holy_site_types/` give bonuses to county holders (`county_holder_character_modifier`) and global bonuses to all adherents when designated as an Eminent Holy Site (`faith_character_modifier`). Iceland's `talknafjordur` and `reykjavik` serve as the universal eminent cradle.
- **Hidden Identity Doctrine (`bm_quintessence_identity_doctrine`)**: A non-visible doctrine providing the `blood_magic_cult_faith` parameter, allowing companion submods or foreign faiths to opt into blood magic cult mechanics without static code coupling.

## 3. Where the details live

| Concept | File |
| --- | --- |
| Religion Family | `common/religion/religion_family_types/bm_religion_family.txt` |
| Religion Definition | `common/religion/religion_types/bm_religion.txt` |
| Faith Definitions | `common/religion/faith_types/bm_faith_types.txt` |
| Mainline Rites | `common/religion/rite_types/bm_rite_types.txt` |
| Holy Site Types | `common/religion/holy_site_types/bm_holy_sites.txt` |
| Identity Doctrine Group | `common/religion/doctrine_group_types/bm_doctrine_group_types.txt` |
| Identity Doctrine Type | `common/religion/doctrine_types/bm_doctrine_types.txt` |
| Conversion Routing | `common/scripted_effects/bm_religion_conversion_effects.txt` |
| Reformation Triggers | `common/scripted_triggers/bm_reformation_repair_triggers.txt` |
| Game Rule Availability | `common/game_rules/bm_game_rules.txt` |

## 4. How the parts connect

- When a character initiates into blood magic or seeks the blood cult via decision (`bm_become_blood_cultist_decision.txt`), conversion is routed through `bm_convert_to_blood_cult_by_heritage_effect` in `bm_religion_conversion_effects.txt`.
- That effect examines the character's prior faith doctrines and syncretism, directing them to the culturally and theologically matching Quintessence variant.
- The faith references its mainline rite via `main_rite = <key>`, locking its ritual identity, and specifies its Eminent and Regular holy sites.
- The religion carries `bm_quintessence_identity_doctrine`, which exposes `blood_magic_cult_faith` to triggers like `bm_is_blood_magic_cult_faith_trigger`.

## 5. Gotchas

- **Do Not Nest Faiths**: In CK3 1.20, `faiths = { ... }` inside `religion_types` is unsupported. Faiths must reside in `faith_types/`.
- **Always Maintain 1:1 Rites**: When adding a new faith, always define its matching mainline rite in `bm_rite_types.txt` and set `main_rite` in `bm_faith_types.txt`.
- **Holy Site Modifier Types**: Do not use generic `character_modifier` in holy site types; use `county_holder_character_modifier` for county holders and `faith_character_modifier` for eminent bonuses.
- **Doctrine Parameters**: Parameters in `doctrine_types` must be bare identifiers in the `parameters = { ... }` list, never key-value assignments.

## 6. Not verified

- In-game Holy Sites UI layout and scrolling with custom dynamic holy sites.
- AI holy site pilgrimage weighting under high-danger travel routes.
