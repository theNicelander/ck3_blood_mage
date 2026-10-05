# Blóðtrú and Blood Faiths

> Living document. Follow `AGENTS.md` in this folder: concepts only, no numbers. Update it when religions, faiths, rites, holy sites, doctrines, or conversion effects change.

## Purpose

The Blóðtrú religion family provides an in-game spiritual and theological foundation for blood magic. It anchors practitioners with a unified blood faith, a mainline rite establishing stable ritual traditions, an extensive holy site network across Europe centered around the volcanic cradle of Iceland, broad coexistence mechanics that prevent universal hostility from neighboring realms, and compatibility hooks that allow foreign faiths and companion mods to participate in cult mechanics.

## Concepts

- **Blóðtrú (`blodtru_religion`).** The primary religion in the `rf_blodtru` religious family. It venerates the vital current and sacred flow of life, treating blood magic and mysticism as divine virtues. It utilizes pluralistic doctrines to avoid extreme hostility with surrounding global faiths.
- **Faith Structure.** The religion encompasses three core cultural branches:
  - `blodtru_faith`: Blóðtrú. Centered in Europe and Iceland, equipped with adaptive tolerance, ancestor worship, and ritual celebration tenets.
  - `ketsudo_faith`: Ketsudō. The Japanese and Korean branch anchored in sacred volcanic peaks, Shinto/Buddhist shrines, and regional seats.
  - `xuedao_faith`: Xuédào. The Chinese branch centered on the Central Plains, venerating ancestral dynastic currents, sacred mountain peaks, imperial capitals, and maritime hubs.
- **Mainline Rite.** Each faith links 1:1 to a scripted mainline rite (`blodtru_faith`, `ketsudo_faith`, `xuedao_faith`). These rites anchor each faith's ritual traditions, colors, and doctrines, preventing the engine from generating untracked dynamic rites.
- **Holy Site Network.** A two-tier holy site network spanning Europe, the Atlantic isles, Japan, Korea, and China:
  - Eminent Holy Sites: Primary spiritual centers and power capitals granting global faith-wide modifiers (Iceland centers `talknafjordur` and `reykjavik`, European capitals, Far East duel sanctuary `tsushima`, Japanese peaks and seats `kyoto`, `edo`, `mount_fuji`, `kaesong`, and Chinese sacred peaks and ancient imperial capitals `taishan`, `huashan`, `songshan`, `mount_wutai`, `huangshan`, `changan`, `luoyang`).
  - Regular Holy Sites: Regional sanctuaries across Europe, Atlantic isles, Japan peaks and cities, Korea peaks and cities, Chinese sacred peaks (`hengshan_north`, `hengshan_south`, `mount_emei`, `mount_jiuhua`, `putuoshan`), economic capitals and ports (`kaifeng`, `beijing`, `nanjing`, `hangzhou`, `chengdu`, `guangzhou`, `quanzhou`, `fuzhou`, `kunming`), and frontiers (`dunhuang`, `taipei`, `hanoi`, `karakorum`) granting local health, vitality, or defensive modifiers to county holders.
- **Cult Conversion Decision.** Taking the decision to embrace the faith requires high devotion and major lifeforce, routing characters to `xuedao_faith` if their culture holds Chinese-sphere heritage pillars (Chinese, Qiangic, Tai, Viet, Tibetan), `ketsudo_faith` for Japonic, Korean, Mongolic, or Tungusic heritages, or `blodtru_faith` otherwise.
- **Hidden Identity Doctrine (`bm_blodtru_identity_doctrine`).** A non-visible doctrine that exposes the `blood_magic_cult_faith` parameter and applies global different-faith opinion buffering. Triggers check this parameter (`bm_is_blood_cult_faith_trigger`), allowing external faiths and companion mods to access blood cult mechanics without hardcoded dependencies.
- **Initiation Duel Hub.** Rulers of both `ketsudo_faith` and `xuedao_faith` share `tsushima` as an Eminent holy site and initiation sanctuary, serving as the Eastern counterpart to Reykjavik.
- **Faith-Gated Blood Initiation.** Initiation into blood magic through the cult decision is governed by campaign game rules (`bm_initiation_faith_requirement`). Depending on the rule, initiation may require following a recognized cult faith or accept faiths where witchcraft is tolerated or celebrated.
- **Reformation Repair.** Unreformed Blóðtrú faiths are designed without a temporal head of faith. To prevent game engine edge cases or legacy headship states from blocking faith reformation, human rulers can use a repair decision to safely clear temporal titles and reset headship to no head (`bm_repair_blodtru_reformation_decision`).

## Mod conventions

- **Tripartite cultural branches.** Faith features are organized under `blodtru_faith` (Western/Atlantic), `ketsudo_faith` (Japanese/Korean), and `xuedao_faith` (Chinese/Central Plains), preserving a unified religious family without fragmenting into dozens of micro-sects.
- **The hidden identity doctrine needs UI metadata.** It carries `icon`, a name key and `visible = no`, and links to its group through `doctrine_group_type`.

## Where the details live

| Concept | File |
| --- | --- |
| Religion Family | `common/religion/religion_family_types/bm_religion_family.txt` |
| Religion Definition | `common/religion/religion_types/bm_religion.txt` |
| Faith Definitions | `common/religion/faith_types/bm_faith_types.txt`, `common/religion/faith_types/bm_xuedao_faith.txt` |
| Mainline Rites | `common/religion/rite_types/bm_rite_types.txt`, `common/religion/rite_types/bm_xuedao_rite.txt` |
| Holy Sites | `common/religion/holy_site_types/bm_holy_sites.txt`, `common/religion/holy_site_types/bm_china_holy_sites.txt` |
| Identity Doctrine Group | `common/religion/doctrine_group_types/bm_doctrine_group_types.txt` |
| Identity Doctrine Type | `common/religion/doctrine_types/bm_doctrine_types.txt` |
| Conversion Scripted Effect | `common/scripted_effects/bm_religion_conversion_effects.txt` |
| Religion Compatibility Triggers | `common/scripted_triggers/bm_religion_compatibility_triggers.txt` |
| Reformation Repair Decision | `common/decisions/bm_reformation_repair_decision.txt` |
| Reformation Repair Effects & Triggers | `common/scripted_effects/bm_reformation_repair_effects.txt`, `common/scripted_triggers/bm_reformation_repair_triggers.txt` |
| Reformation Repair Events | `events/bm_reformation_repair_events.txt` |
| Cult Decision | `common/decisions/bm_become_blood_cultist_decision.txt` |
| Cult Initiation Decision | `common/decisions/bm_become_blood_mage_decision.txt` |
| Religion & Initiation Game Rules | `common/game_rules/bm_game_rules.txt` (`blodtru_religion`, `bm_initiation_faith_requirement`) |
| Localization | `localization/english/bm_religion_l_english.yml`, `localization/english/bm_ketsudo_l_english.yml`, `localization/english/bm_xuedao_l_english.yml` |

## How the parts connect

- When a blood mage decides to convert via `become_blood_cultist_decision`, the decision consumes one major lifeforce and routes conversion via `bm_convert_to_blood_cult_by_heritage_effect`.
- Non-mages seeking blood magic via `bm_blood_cultist_become_blood_mage_decision` check `bm_meets_blood_mage_initiation_faith_requirement_trigger`, which evaluates the character's faith against the active initiation rule.
- Both decisions rely on `bm_is_blood_cult_faith_trigger`, which returns true if the character's faith belongs to `rf_blodtru` or possesses the `blood_magic_cult_faith` doctrine parameter.
- Faiths define their core tenets and link to their corresponding mainline rite via `main_rite`.
- Characters reforming an unreformed Blóðtrú faith can invoke `bm_repair_blodtru_reformation_decision` if headship titles block normal progression, resetting headship via `bm_repair_blodtru_reformation_effect`.
- Campaign game rules dictate whether AI rulers adopt the religion (`blodtru_religion`) and whether initiation requires pure cult adherence or accepts witchcraft traditions (`bm_initiation_faith_requirement`).

## Gotchas

- Faiths must be defined as root objects in `faith_types/`; placing `faiths = { ... }` blocks inside `religion_types/` is invalid in 1.20.
- Every faith must have an explicit 1:1 mainline rite in `rite_types/` linked via `main_rite = <key>`; omitting this causes the engine to generate unlocalized dynamic rites.
- Holy sites must use `county_holder_character_modifier` for county holders and `faith_character_modifier` for Eminent sites; generic `character_modifier` is invalid.
- The `blood_magic_cult_faith` parameter must be declared as a bare symbol in `parameters = { ... }` within `bm_doctrine_types.txt`, checked via `has_doctrine_parameter`.
- Never reference external mod faiths or titles directly; use `blood_magic_cult_faith` or route conversions through extensible scripted effects.

## Not verified

- AI reformation pacing and holy site selection for custom reformed Blóðtrú branches.
- UI scaling and list scrolling for holy sites when dynamic rites generate additional holy sites.
