# Icelandic Culture Subsystem

## Executive Summary

- **What:** Playable `bm_icelandic` culture under `heritage_north_germanic` featuring equal gender martial rights, 5 traditions, an Icelandic saga name list with epenthetic `-ur` patronymics, and Day 1 conversion of Iceland.
- **Acquisition / Selection:** Selectable in Ruler Designer; initialized on all counties and courts in `d_iceland` on game start via campaign game rule.

### Culture Specification

| Attribute | Value | Details |
| --- | --- | --- |
| **Identifier** | `bm_icelandic` | Parent: `norse`; Era created: `867.1.1` |
| **Color** | `{ 210 150 255 }` | Matches Norwegian pastel palette |
| **Ethos** | `ethos_communal` | Emphasizes community solidarity and cultural acceptance |
| **Heritage** | `heritage_north_germanic` | Enables North Germanic innovations and hybridizations |
| **Language** | `language_norse` | Shares language with Norse and Norwegian |
| **Martial Custom** | `martial_custom_equal` | Both men and women serve as knights and commanders |
| **Traditions** | 5 total | Alþingi Commonwealth, Verbúðir, Beacon of Learning (fallback Philosopher Culture), Coastal Warriors (fallback Hird), Northern Stories (fallback Runestones) |
| **Name List** | `bm_name_list_icelandic` | Saga names, epenthetic `-ur` endings, `-sson` / `-sdottir` patronymics |
| **Innovations** | Baseline North Germanic | Defined for `867.1.1`, `950.1.1`, and `1066.1.1` |

## Key Mechanics

### 1. Cultural Traditions

| Tradition ID | Name | DLC Required | Fallback |
| --- | --- | --- | --- |
| `bm_tradition_althingi` | Alþingi Commonwealth | None | None |
| `bm_tradition_verbudir` | Verbúðir | None | None |
| `tradition_fp3_beacon_of_learning` | Beacon of Learning | `legacy_of_persia` | `tradition_philosopher_culture` |
| `tradition_fp1_coastal_warriors` | Coastal Warriors | `the_northern_lords` | `tradition_hird` |
| `tradition_fp1_northern_stories` | Northern Stories | `the_northern_lords` | `tradition_runestones` |

#### Alþingi Commonwealth (`bm_tradition_althingi`)
- **Succession & Assembly:** Unlocks Scandinavian Elective (`scandinavian_elective_enabled = yes`). Preserves mutual exclusivity with `tradition_things`.
- **Trial by Combat (Hólmganga):** Unlocks Hólmganga duel interaction via native `has_access_to_trials_by_combat = yes` and `trial_by_combat_enabled = yes`.
- **Ruler & Capital Modifiers (`character_modifier`):** `character_capital_county_monthly_development_growth_add = 0.10`, `cultural_head_fascination_mult = 0.25`.
- **County Development & Control (`county_modifier`):** `development_growth = 0.05` (+0.05/mo flat development growth), `development_growth_factor = 0.25` (+25% development growth factor), and `monthly_county_control_growth_add = 0.10` (+0.10/mo county control growth).

#### Verbúðir (`bm_tradition_verbudir`)
- **Tribal Maritime Powerhouse:** Replaces `tradition_maritime_mercantilism`. Fully pickable and functional for Tribal cultures from 867 (`trade_ports_enabled_for_tribals = yes`, `next_level_trade_ports = yes`). Mutually exclusive with `tradition_maritime_mercantilism` and `tradition_fishermen`.
- **Tradeport Harbor Bonuses:** Hooks cleanly into Tradeport tiers 1–8:
  - Stationed Men-at-Arms bonus via `trade_ports_stationed_maa_bonus = yes`.
  - Monthly County Control Growth (+0.10 to +0.25) via native `trade_ports_give_control_growth = yes`.
  - Levies (+4% to +16%) via native `trade_ports_give_levies = yes`.
  - Cultural Fascination (+2% progress per level) via `trade_ports_give_fascination = yes`.
  - Coastal Holdings tax bonus across castles, cities, and temples via `maritime_mercantilism_coastal_holdings = yes`.
  - River sailing capability via `can_travel_along_rivers = yes`.
- **Character Travel Modifiers (`character_modifier`):** `embarkation_cost_mult = -0.75` (-75% embarkation cost), `sea_travel_danger = medium_sea_danger_reduction`, and `coastal_sea_travel_danger = medium_sea_danger_reduction`.
- **County Economy & Military (`county_modifier`):** `monthly_county_control_growth_add = 0.05` (+0.05/mo control growth), `tax_mult = 0.20` (+20% taxes), `levy_size = 0.20` (+20% levies), and `supply_limit_mult = 0.25` (+25% supply limit).

### 2. Name List & Patronymics (`bm_name_list_icelandic`)

- **Patronymics:** `always_use_patronym = yes`, `dynnpat_suf_male = "dynnpat_suf_sson"` (`-sson`), `patronym_suffix_female = "bm_dynnpat_suf_sdottir"` (`-sdóttir`), prefix `"dynnp_af"`.
- **Name Naming Convention:** Uses engine-safe ASCII keys in script (`PE_tur`, `IngO_lfur`, `KonrA_D_`, `GuD_finnur`, `LA_ra`, `SigrU_n`) paired with explicit localized strings (**Pétur**, **Ingólfur**, **Konráð**, **Guðfinnur**, **Lára**, **Sigrún**).
- **Curated Roster (124 Male, 73 Female):** Contains strictly curated saga, mythological, historical, and literary names. All unrequested baseline Old Norse names are purged.
- **Epenthetic `-ur`:** Applied systematically across nominative masculine and feminine names (*Gunnhildur, Einar, Grímur, Þorbrandur, Ingólfur, Sigurður, Haraldur, Guðmundur, Eiríkur, Hallur, Haukur, Leifur, Kveldúlfur, Skallagrímur, Álfrhildur, Hólmfríður*).
- **Dynasties (31 total):**
  - *Sturlungaöld (Age of the Sturlungs) Chieftains:* Sturlungar, Haukdælir, Oddaverjar, Ásbirningar, Svínfellingar, Vatnsfirðingar.
  - *Heroic / Legendary:* Völsungar, Loðbrók, Járnsíða, Beinlausi, Hárfagri, Bebbanburg, Ragnarsynir, Langsverð.
  - *Tolkien-Inspired Icelandic Houses:* Eikinskjaldi, Hringberi, Stígandi, Stríðsmaður, Róhansmenn.
  - *Saga Houses:* Hlíðarendi, Ormstunga, Eyfells, Kormákur, Eldjárn, Blöndal, Nordal, Haarde, Gnarr, Goði, Gautur.

### 3. Campaign Game Rule & Day 1 Setup

- **Game Rule:** `bm_icelandic_culture` (`bm_game_rules.txt`).
  - `bm_icelandic_culture_enabled` (Default): Converts `d_iceland` counties and courts.
  - `bm_icelandic_culture_disabled`: Preserves vanilla historical Norse/Norwegian setup; culture remains in Ruler Designer.
- **On-Action Hook:** `on_game_start` -> `bm_setup_icelandic_culture_on_start` (`bm_icelandic_culture.txt`).
- **Conversion Scope:** Iterates `title:d_iceland.every_de_jure_county`, converting county culture, county holder, courtier/guest pool, unlanded family, and every barony holder.

## Where the details live

| Concept | File Path |
| --- | --- |
| Culture definition & pillars | `common/culture/cultures/bm_icelandic.txt` |
| Culture traditions | `common/culture/traditions/bm_culture_traditions.txt` |
| Name list & patronymics | `common/culture/name_lists/bm_name_list_icelandic.txt` |
| Innovations history | `history/cultures/bm_icelandic.txt` |
| Game start conversion on-action | `common/on_action/bm_icelandic_culture.txt` |
| Game rule declaration | `common/game_rules/bm_game_rules.txt` |
| Game rule localization | `localization/english/bm_game_rules_l_english.yml` |
| Culture & name localization | `localization/english/culture/bm_icelandic_l_english.yml` |
| Traditions localization | `localization/english/culture/bm_culture_traditions_l_english.yml` |

## Gotchas

- **Vanilla history preservation:** Never overwrite `history/provinces/k_norway.txt` or `history/characters/norse.txt`; the modular `on_game_start` on-action cleanly overwrites county/character culture dynamically without file conflicts.
- **Engine name token collisions:** When adding modern/saga names with special characters (accented vowels, thorn, eth), script tokens must use Paradox ASCII substitutions (`A_`, `E_`, `I_`, `O_`, `U_`, `T_`, `D_`) with corresponding sibling keys in `bm_icelandic_l_english.yml` to prevent parsing breaks.

## Not verified

- AI divergence/hybridization weights if an AI ruler holds `d_iceland` with `bm_icelandic_culture_disabled`.
