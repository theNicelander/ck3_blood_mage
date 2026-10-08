# Blóðtrú and Blood Faiths

## Executive Summary

Spiritual framework for blood magic. Religious family `rf_blodtru` with religion `blodtru_religion`. 3 cultural faiths (`blodtru_faith`, `ketsudo_faith`, `xuedao_faith`), each bound 1:1 to scripted mainline rites. Uses hidden identity doctrine (`bm_blodtru_identity_doctrine`) exposing `blood_magic_cult_faith` parameter for soft compatibility without hard dependencies.

## Faith Structure & Mainline Rites

| Faith | Rite Key | Cultural Sphere | Eminent Holy Sites | Primary Modifier Focus |
| --- | --- | --- | --- | --- |
| `blodtru_faith` | `blodtru_faith` | European / Atlantic | Iceland (`talknafjordur`, `reykjavik`), European capitals | Learning / Prowess per piety level |
| `ketsudo_faith` | `ketsudo_faith` | Japonic, Korean, Mongolic, Tungusic | Japan & Korea (`yamashiro`, `kamakura`, `mount_fuji`, `mount_aso`, `mount_osore`, `gyeongju`) | Prowess / Dread / Health per piety level |
| `xuedao_faith` | `xuedao_faith` | Chinese, Qiangic, Tai, Viet, Tibetan | Central Plains & Sacred Peaks (`changan`, `luoyang`, `beijing`, `hangzhou`, `chengdu`, `guangzhou`, `taishan`, `gyeongju`) | Stewardship / Learning / Health per piety level |

- **Holy Site Hierarchy:**
  - **Eminent Sites:** Defined in `eminent_holy_sites = { ... }`. Grant realm/faith-wide `faith_character_modifier` scaled per piety level plus `county_holder_character_modifier`.
  - **Regular Sites:** Defined in `holy_sites = { ... }`. Grant local `county_holder_character_modifier` (health, life expectancy, epidemic resistance) to county owner.

## Identity Doctrine

- **Type:** `bm_blodtru_identity_doctrine` (Group: `bm_blodtru_identity_group`).
- **Visibility:** Hidden (`visible = no`, uses icon `core_tenet_sacred_shadows`).
- **Modifiers:**
  - `different_faith_opinion = 15`
  - `different_faith_liege_opinion = 10`
  - `different_faith_county_opinion_mult = -0.25`
- **Parameter:** Exposes `blood_magic_cult_faith`. Evaluated globally via `bm_is_blood_cult_faith_trigger` (`has_doctrine_parameter = blood_magic_cult_faith` or religion family `rf_blodtru`). Allows third-party mods to adopt cult mechanics without hardcoded dependencies.

## Decisions

| Decision | Panel | Cost | Cooldown | Requirements | XP Gain | Effect |
| --- | --- | --- | --- | --- | --- | --- |
| `bm_become_blood_cultist_decision` | Decisions | 250 Piety | 10 years | Blood Mage, Devotion >= 2, Major Lifeforce | None | Fires `bm_faith_conversion.0001`: converts character to cultural faith (`xuedao_faith`, `ketsudo_faith`, or `blodtru_faith`), consumes 1 Major Lifeforce. |
| `bm_repair_blodtru_reformation_decision` | Decisions | None | None | Blóðtrú faith, unformed/bugged temporal head title | None | Executes `bm_repair_blodtru_reformation_effect`: clears temporal head title, resets headship to no head. |
| `bm_blood_cultist_become_blood_mage_decision` | Decisions | 500 Piety | None | Non-mage, adult, meets faith initiation rule | +10 ancient | Awards `lifestyle_blood_mage` trait via cult rite. |

## Initiation Duel Hub (Tsushima)

- Eastern counterpart to Reykjavik for blood magic awakening.
- Rulers travel to Tsushima (`c_tsushima`) to challenge hermit blood master in Learning & Prowess contest to unlock blood magic without conversion.

## Game Rules

- `blodtru_religion`: Controls AI conversion/spawning of Blóðtrú religion (`vanilla_start`, `historical_flavor`, `cult_spread`).
- `bm_initiation_faith_requirement`: Determines faith gates for `bm_blood_cultist_become_blood_mage_decision`:
  - `cult_only`: Must follow a blood cult faith (`bm_is_blood_cult_faith_trigger`).
  - `witchcraft_accepted`: Accepts cult faiths or faiths where witchcraft is accepted/virtuous.
  - `unrestricted`: Any faith permitted.

## File Map

| Piece | File |
| --- | --- |
| Religion Family | `common/religion/religion_family_types/bm_religion_family.txt` |
| Religion Definition | `common/religion/religion_types/bm_religion.txt` |
| Faith Definitions | `common/religion/faith_types/bm_blodtru.txt`, `common/religion/faith_types/bm_ketsudo.txt`, `common/religion/faith_types/bm_xuedao_faith.txt` |
| Mainline Rites | `common/religion/rite_types/bm_rite_types.txt`, `common/religion/rite_types/bm_xuedao_rite.txt` |
| Holy Sites | `common/religion/holy_site_types/bm_europe_holy_sites.txt`, `common/religion/holy_site_types/bm_china_holy_sites.txt`, `common/religion/holy_site_types/bm_japan_holy_sites.txt`, `common/religion/holy_site_types/bm_korea_holy_sites.txt` |
| Identity Doctrine | `common/religion/doctrine_group_types/bm_doctrine_group_types.txt`, `common/religion/doctrine_types/bm_doctrine_types.txt` |
| Conversion Event | `events/bm_faith_conversion_events.txt` |
| Compatibility Triggers | `common/scripted_triggers/bm_religion_compatibility_triggers.txt` |
| Reformation Repair | `common/decisions/bm_reformation_repair_decision.txt`, `common/scripted_effects/bm_reformation_repair_effects.txt` |
| Cult Decisions | `common/decisions/bm_become_blood_cultist_decision.txt`, `common/decisions/bm_become_blood_mage_decision.txt` |
