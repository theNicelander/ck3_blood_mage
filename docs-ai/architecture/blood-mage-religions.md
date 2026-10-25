# Blóðtrú and Blood Faiths

Living technical specification for `rf_blodtru` religion family, cultural blood faiths, holy sites, and conversion mechanics.

## Overview

Spiritual framework in `common/religion/`. Religious family `rf_blodtru` and religion `blodtru_religion` with 3 regional faiths (`blodtru_faith`, `ketsudo_faith`, `xuedao_faith`), bound 1:1 to mainline rites (`bm_rite_types.txt`).
- **Identity Doctrine:** Hidden doctrine `bm_blodtru_identity_doctrine` sets parameter `blood_magic_cult_faith = yes`, checked by `bm_is_blood_cult_faith_trigger`. Allows third-party / reformed faiths to integrate with blood magic mechanics.
- **Core Tenets:** `tenet_ancestor_worship` (family opinion, prestige on birth/marriage), `tenet_mendicant_preachers` (travel speed, conversion), `tenet_literalism` (learning skill, scholarship).

## Faith Structure, Mainline Rites & Holy Sites

| Faith Key | Rite Key | Cultural Sphere (`bm_faith_conversion.0001`) | Eminent Holy Sites (`eminent_holy_sites`) | Regular Holy Sites (`holy_sites`) |
| --- | --- | --- | --- | --- |
| **Blóðtrú** (`blodtru_faith`) | `blodtru_faith` | Default / European / Atlantic / Global fallback | **58 Sites:** All European capitals and landmarks (`talknafjordur`, `reykjavik`, `london`, `madrid`, `oslo`, `paris`, `berlin`, `rome`, `constantinople`, `olympus`, `kiev`, `athens`, `tenerife`, `amsterdam`, `vienna`, `stonehenge`, `isle_of_man`, etc.) | None (all holy sites are eminent) |
| **Ketsudō** (`ketsudo_faith`) | `ketsudo_faith` | Japonic, Korean, Mongolic, Tungusic | **27 Sites:** `tsushima`, `yamashiro`, `kamakura`, `mount_fuji`, `mount_aso`, `mount_osore`, `gyeongju`, `edo`, `hakodate`, `mount_baekdu`, `gaegyeong`, `hanyang`, etc. | None (all holy sites are eminent) |
| **Xuédào** (`xuedao_faith`) | `xuedao_faith` | Chinese, Qiangic, Tai, Viet, Tibetan | **32 Sites:** `changan`, `luoyang`, `beijing`, `hangzhou`, `chengdu`, `guangzhou`, `taishan`, `gyeongju`, `dunhuang`, Sacred Five Mountains, Four Buddhist/Daoist Peaks, `nanjing`, `lhasa`, etc. | None (all holy sites are eminent) |

### Holy Site Modifier Architecture (CK3 1.20)
- **All Sites Eminent (`eminent_holy_sites_max = 80`):** Every holy site in Blóðtrú faiths is defined under `eminent_holy_sites`. Each site grants **both** a `faith_character_modifier` (applies to all followers of the faith when controlled) **and** a `county_holder_character_modifier` (applies directly to the county holder, stacking with the faith-wide bonus). Benefits are calibrated as smaller incremental bonuses (`+0.25` Health, `+1` Life Expectancy, `+1` Epidemic Resistance, or `+1 [Skill/Prowess] per Piety Level`) designed to reward wide geographic control and spread across multiple holy sites.
- **Zero Vanilla Holy Site Overwrites:** Vanilla holy site keys (`luoyang`, `dunhuang`, `tenerife`, `rome`, `constantinople`, `kiev`, `athens`, `madrid`, `paris`) are referenced directly in the faith definitions without re-declaring their keys in `common/religion/holy_site_types/`. Custom regional holy sites lacking vanilla definitions (such as `hangzhou` and `quanzhou`) are declared directly in `common/religion/holy_site_types/bm_china_holy_sites.txt`.

## Identity Doctrine (`bm_blodtru_identity_doctrine`)

- **Group:** `bm_blodtru_identity_group` (`visible = no`, icon `core_tenet_sacred_shadows`).
- **Passive Faith Modifiers:**
  - `different_faith_opinion = 15`
  - `different_faith_liege_opinion = 10`
  - `different_faith_county_opinion_mult = -0.25`
- **Doctrine Parameter:** `blood_magic_cult_faith = yes`. Checked by `bm_is_blood_cult_faith_trigger` (`has_doctrine_parameter = blood_magic_cult_faith` OR `religion = { is_in_family = rf_blodtru }`).

## Religious & Initiation Decisions

| Decision | Panel | Cost & Cooldown | Requirements | Effect |
| --- | --- | --- | --- | --- |
| `become_blood_cultist_decision` | Religious & Situation | 250 Piety + 1 Major Lifeforce. CD: 10 yrs. | `lifestyle_blood_mage` or `lifestyle_blood_knight`, `piety_level >= 3`, Major Lifeforce, not already in `rf_blodtru`. | Fires `bm_faith_conversion.0001`: consumes Major Lifeforce and converts character (and consenting courtiers/vassals) to `xuedao_faith`, `ketsudo_faith`, or `blodtru_faith` based on cultural heritage. |
| `bm_blood_cultist_become_blood_mage_decision` | Decisions | **1 Devotion Level** (`add_piety_level = -1`) paid on duel choice. No CD. | Adult lacking Blood Mage & Blood Knight, `piety_level >= 2`, meets `bm_initiation_faith_requirement` rule, located in Reykjavik (`b_reykjavik`) or Tsushima (`c_tsushima`). | Fires `bm_geyser_duel.0001` against Egill Skallagrímsson: Learning duel bestows `lifestyle_blood_mage`; Prowess duel bestows `lifestyle_blood_knight`. |
| `bm_repair_blodtru_reformation_decision` | Religious | Free. No CD. | Follows `rf_blodtru` faith with broken/unformed temporal head of faith title after vanilla pagan reformation. | Executes `bm_repair_blodtru_reformation_effect`: clears corrupted temporal head title and restores clean headship state. |

## Religion Game Rules (`common/game_rules/bm_game_rules.txt`)

| Rule ID | Settings | Default | Effect |
| --- | --- | --- | --- |
| `blodtru_religion` | `enabled` / `player_only` / `disabled` | `enabled` | Controls whether AI can convert to Blóðtrú faiths or disables the religion family entirely. |
| `bm_starting_counties_faith` | `vanilla` / `iceland` / `tsushima` / `both` | `vanilla` | Converts Iceland (`d_iceland` -> `blodtru_faith`) and/or Tsushima (`c_tsushima` -> `ketsudo_faith`) and their landed holders at campaign start (`bm_starting_counties_effects.txt`). |
| `bm_starting_holders_blood_mage` | `vanilla` / `iceland` / `tsushima` / `both` | `vanilla` | Bestows `lifestyle_blood_mage` onto landed county holders in Iceland and/or Tsushima at campaign start. |
| `bm_initiation_faith_requirement` | `dedicated_cult` / `cult_or_witchcraft_accepted` | `dedicated_cult` | Controls whether `bm_blood_cultist_become_blood_mage_decision` requires a `rf_blodtru` cult faith or allows any faith with accepted/virtuous witchcraft. |

## Where the details live

| Piece | File |
| --- | --- |
| Religion Family | `common/religion/religion_family_types/bm_religion_family.txt` |
| Religion Definition | `common/religion/religion_types/bm_religion.txt` |
| Faith Definitions | `common/religion/faith_types/bm_blodtru.txt`, `common/religion/faith_types/bm_ketsudo.txt`, `common/religion/faith_types/bm_xuedao_faith.txt` |
| Mainline Rites | `common/religion/rite_types/bm_rite_types.txt` |
| Holy Sites | `common/religion/holy_site_types/bm_europe_holy_sites.txt`, `bm_china_holy_sites.txt`, `bm_japan_holy_sites.txt`, `bm_korea_holy_sites.txt` |
| Identity Doctrine | `common/religion/doctrine_group_types/bm_doctrine_group_types.txt`, `common/religion/doctrine_types/bm_doctrine_types.txt` |
| Cultural Conversion Event & Effects | `events/bm_faith_conversion_events.txt`, `common/scripted_effects/bm_religion_conversion_effects.txt` |
| Starting Counties & Holders Effects | `common/scripted_effects/bm_starting_counties_effects.txt` |
| Compatibility Triggers | `common/scripted_triggers/bm_religion_compatibility_triggers.txt` |
| Reformation Repair | `common/decisions/religion/bm_reformation_repair_decision.txt`, `common/scripted_effects/bm_reformation_repair_effects.txt` |
| Cult & Initiation Decisions | `common/decisions/religion/bm_become_blood_cultist_decision.txt`, `common/decisions/become_mage/bm_become_blood_mage_decision.txt` |
