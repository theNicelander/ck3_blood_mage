# Cult of Quintessence and Blood Faiths

> Living document. Follow `AGENTS.md` in this folder: concepts only, no numbers. Update it when religions, faiths, rites, holy sites, doctrines, or conversion effects change.

## Purpose

The Cult of Quintessence religion family provides an in-game spiritual and theological foundation for blood magic. It anchors practitioners with dedicated syncretic faiths that bridge blood magic with global traditions, mainline rites that establish stable ritual traditions, custom holy sites across Europe centered around the volcanic cradle of Iceland, and compatibility hooks that allow foreign faiths and companion mods to participate in cult mechanics.

## Concepts

- **Cult of Quintessence (`quintessence_religion`).** The primary religion in the `rf_quintessence` religious family. It venerates the vital current and quintessence of life, treating blood magic and mysticism as divine virtues.
- **Syncretic Blood Faiths.** Seven distinct faiths representing theological adaptations across cultural spheres:
  - `quintessence_faith`: Christian syncretic branch.
  - `quintessence_faith_islamic`: Islamic syncretic branch.
  - `quintessence_faith_jewish`: Jewish syncretic branch.
  - `quintessence_faith_eastern`: Dharmic and Eastern syncretic branch.
  - `quintessence_faith_sinitic`: Taoist and Confucian syncretic branch.
  - `quintessence_faith_asatru`: Norse and Ásatrú branch focused on human sacrifice and martial devotion.
  - `quintessence_faith_unreformed`: Syncretic branch for traditionalist and unreformed pagan heritages.
- **Mainline Rites.** Each faith links 1:1 to a scripted mainline rite in `common/religion/rite_types/`. These rites anchor the faith's ritual traditions, colors, and doctrines, preventing the engine from generating untracked dynamic rites.
- **Holy Site Network.** A two-tier holy site network across Europe and Iceland:
  - Eminent Holy Sites: Primary spiritual centers and power capitals granting global faith-wide stat/piety modifiers (Iceland centers `talknafjordur` and `reykjavik`, major stat capitals `london`, `madrid`, `oslo`, `paris`, `berlin`, and prominent historical/religious centers including `rome`, `constantinople`, `jerusalem`, `mecca`).
  - Regular Holy Sites: European regional sanctuaries granting local health, life expectancy, or epidemic resistance modifiers to county holders.
- **Conversion by Heritage.** Taking the decision to join the cult does not require manual selection from a menu. The scripted conversion effect inspects the convert's previous faith and doctrines, automatically routing them to the matching Quintessence syncretism branch, with Christian syncretism serving as the universal fallback.
- **Hidden Identity Doctrine (`bm_quintessence_identity_doctrine`).** A non-visible doctrine that exposes the `blood_magic_cult_faith` parameter. Triggers check this parameter (`bm_is_blood_cult_faith_trigger`), allowing external faiths and companion mods to access blood cult mechanics without hardcoded dependencies.
- **Faith-Gated Blood Initiation.** Initiation into blood magic through the cult decision is governed by campaign game rules (`bm_initiation_faith_requirement`). Depending on the rule, initiation may require following a recognized cult faith or accept faiths where witchcraft is tolerated or celebrated.
- **Reformation Repair.** Unreformed Quintessence faiths are designed without a temporal head of faith. To prevent game engine edge cases or legacy headship states from blocking faith reformation, human rulers can use a repair decision to safely clear temporal titles and reset headship to no head.

## Mod conventions

- **Heritage conversion is the extension point.** Conversion routing lives in one scripted effect so companion mods can override it. Optional native-faith integration lives outside this repo.
- **The hidden identity doctrine needs UI metadata.** It carries `icon`, a name key and `visible = no`, and links to its group through `doctrine_group_type`.

## Where the details live

| Concept | File |
| --- | --- |
| Religion Family | `common/religion/religion_family_types/bm_religion_family.txt` |
| Religion Definition | `common/religion/religion_types/bm_religion.txt` |
| Faith Definitions | `common/religion/faith_types/bm_faith_types.txt` |
| Mainline Rites | `common/religion/rite_types/bm_rite_types.txt` |
| Holy Sites | `common/religion/holy_site_types/bm_holy_sites.txt` |
| Identity Doctrine Group | `common/religion/doctrine_group_types/bm_doctrine_group_types.txt` |
| Identity Doctrine Type | `common/religion/doctrine_types/bm_doctrine_types.txt` |
| Heritage Conversion Effect | `common/scripted_effects/bm_religion_conversion_effects.txt` |
| Religion Compatibility Triggers | `common/scripted_triggers/bm_religion_compatibility_triggers.txt` |
| Reformation Repair Decision | `common/decisions/bm_reformation_repair_decision.txt` |
| Reformation Repair Effects & Triggers | `common/scripted_effects/bm_reformation_repair_effects.txt`, `common/scripted_triggers/bm_reformation_repair_triggers.txt` |
| Reformation Repair Events | `events/bm_reformation_repair_events.txt` |
| Cult Decision | `common/decisions/bm_become_blood_cultist_decision.txt` |
| Cult Initiation Decision | `common/decisions/bm_become_blood_mage_decision.txt` |
| Religion & Initiation Game Rules | `common/game_rules/bm_game_rules.txt` (`quintessence_religion`, `bm_initiation_faith_requirement`) |

## How the parts connect

- When a blood mage decides to convert via `become_blood_cultist_decision`, the effect calls `bm_convert_to_blood_cult_by_heritage_effect`, routing them to the appropriate faith based on their prior faith's doctrines.
- Non-mages seeking blood magic via `bm_blood_cultist_become_blood_mage_decision` check `bm_meets_blood_mage_initiation_faith_requirement_trigger`, which evaluates the character's faith against the active initiation rule.
- Both decisions rely on `bm_is_blood_cult_faith_trigger`, which returns true if the character's faith belongs to `rf_quintessence` or possesses the `blood_magic_cult_faith` doctrine parameter.
- Faiths define their core tenets and link to their corresponding mainline rite via `main_rite`.
- Characters reforming an unreformed Quintessence faith can invoke `bm_repair_quintessence_reformation_decision` if headship titles block normal progression, resetting headship via `bm_repair_quintessence_reformation_effect`.
- Campaign game rules dictate whether AI rulers adopt the religion (`quintessence_religion`) and whether initiation requires pure cult adherence or accepts witchcraft traditions (`bm_initiation_faith_requirement`).

## Gotchas

- Faiths must be defined as root objects in `faith_types/`; placing `faiths = { ... }` blocks inside `religion_types/` is invalid in 1.20.
- Every faith must have an explicit 1:1 mainline rite in `bm_rite_types.txt` linked via `main_rite = <key>`; omitting this causes the engine to generate unlocalized dynamic rites.
- Holy sites must use `county_holder_character_modifier` for county holders and `faith_character_modifier` for Eminent sites; generic `character_modifier` is invalid.
- The `blood_magic_cult_faith` parameter must be declared as a bare symbol in `parameters = { ... }` within `bm_doctrine_types.txt`, checked via `has_doctrine_parameter`.
- Never reference external mod faiths or titles directly; use `blood_magic_cult_faith` or route conversions through extensible scripted effects.

## Not verified

- AI reformation pacing and holy site selection for custom reformed Quintessence branches.
- UI scaling and list scrolling for holy sites when dynamic rites generate additional holy sites.
