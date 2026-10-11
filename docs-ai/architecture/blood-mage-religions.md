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
| `become_blood_cultist_decision` | Decisions | 250 Piety | 10 years | Blood Mage, Devotion >= 2, Major Lifeforce | None | Fires `bm_faith_conversion.0001`: converts character to cultural faith (`xuedao_faith`, `ketsudo_faith`, or `blodtru_faith`), consumes 1 Major Lifeforce. |
| `bm_repair_blodtru_reformation_decision` | Decisions | None | None | Blóðtrú faith, unformed/bugged temporal head title | None | Executes `bm_repair_blodtru_reformation_effect`: clears temporal head title, resets headship to no head. |
| `bm_blood_cultist_become_blood_mage_decision` | Decisions | Free (1 Devotion level for Learning, 1 Fame level for Prowess) | None | Non-mage, adult, meets faith initiation rule, located in Reykjavik or Tsushima | None | Fires `bm_geyser_duel.0001` against Egill Skallagrímsson to win `lifestyle_blood_mage` (Learning) or `lifestyle_blood_knight` (Prowess). |

## Initiation Duel Hub (Tsushima)

- Eastern counterpart to Reykjavik for blood magic awakening.
- Rulers travel to Tsushima (`c_tsushima`) to challenge hermit blood master Egill in Learning & Prowess contest to unlock blood magic without conversion.

## Game Rules

- `blodtru_religion`: Controls campaign availability of Blóðtrú religion family:
  - `blodtru_religion_enabled`: Fully active.
  - `blodtru_religion_player_only`: Available to player only; AI conversion blocked.
  - `blodtru_religion_disabled`: Entire religion family disabled.
- `bm_initiation_faith_requirement`: Determines faith gates for `bm_blood_cultist_become_blood_mage_decision`:
  - `bm_initiation_dedicated_cult`: Must follow a blood cult faith (`bm_is_blood_cult_faith_trigger`).
  - `bm_initiation_cult_or_witchcraft_accepted`: Accepts cult faiths or faiths where witchcraft is accepted/virtuous.

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
| Reformation Repair | `common/decisions/religion/bm_reformation_repair_decision.txt`, `common/scripted_effects/bm_reformation_repair_effects.txt` |
| Cult Decisions | `common/decisions/religion/bm_become_blood_cultist_decision.txt`, `common/decisions/become_mage/bm_become_blood_mage_decision.txt` |
