# Blood Mage Decisions

Living technical specification for decisions in the Blood Mage mod.

## Executive Summary

- **What:** Player-facing actions for blood mages and blood knights. Grouped under `bm_decision_group`.
- **Visibility:** Visible in both the realm decisions list under `bm_decision_group` ("Blood Mage Decisions") and in the Blood Magic story panel (`bm_blood_mage_story`) in the Situation window.

### Decisions Master Table

| Decision ID | Panel Type | Cost & Cooldown | Requirements | XP Gain | Primary Effect |
| --- | --- | --- | --- | --- | --- |
| `bm_blood_cultist_become_blood_mage_decision` | Decisions | Decision free (both duel options cost 1 Devotion level). No cooldown. | Follows Blóðtrú faith, missing Blood Mage and Blood Knight, `piety_level >= 2`. Location: Reykjavik or Tsushima. | None | Initiates `bm_geyser_duel.0001` against Egill (Learning for `lifestyle_blood_mage`, Prowess for `lifestyle_blood_knight`). |
| `bm_enhance_blood_ritual_decision` | Decisions (Major) | Decision free (both duel options cost 1 Devotion level). No cooldown. | Non-Blóðtrú, missing Blood Mage and Blood Knight, `piety_level >= 2`, qualifying stats/traits. Location: Reykjavik or Tsushima. | None | Initiates `bm_geyser_duel.0001` against Egill (Learning for `lifestyle_blood_mage`, Prowess for `lifestyle_blood_knight`). |
| `convert_to_blood_magic_from_witch` | Decisions | Free. No cooldown. | Player only. Has witch trait. Missing Blood Mage and Blood Knight. | None | Removes witch trait, grants blood mage. |
| `seek_power_decision` | Decisions & Situation | Free. CD: `bm_seek_power_cooldown_days` (730d landed, 365d unlanded/adventurer; halved to 365d/180d with Superior **Vegvísir**). | `lifestyle_blood_knight` (Mages excluded). | +1–2 `slaughter`/`vanguard`/`enlightenment` (Knight) | Wilderness hunt event chain (`seek_power.001`). Exclusive to Blood Knights. Harvests Minor or Major Lifeforce and martial XP. |
| `blood_golem_creation_decision` | Decisions & Situation | 500p + Superior Lifeforce. CD: 3 yrs. | Blood Mage or Blood Knight, Devotion >= 3, Superior Lifeforce. | +5 `bloodline` (Mage) / +5 `vanguard` (Knight) | Spawns courtier in `bm_house_golem`, triggers shaping duel (`blood_golem.001` -> `.002`). |
| `mass_lifedrain_prisoners_decision` | Decisions & Situation | Piety per prisoner. No CD. | Dungeon prisoners available. | +`hematurgy` | Mass harvests Lifeforce from dungeon prisoners (`bm_mass_lifedrain.001`; +25g/victim with Superior **Nábrókarstafur**). |
| `become_blood_cultist_decision` | Religious & Situation | 250p + 1 Major Lifeforce. CD: 10 yrs. | Blood Mage or Blood Knight, Devotion >= 3, Major Lifeforce. | None | Fires `bm_faith_conversion.0001` to convert character and realm to cultural Blóðtrú faith (`blodtru_faith`, `ketsudo_faith`, or `xuedao_faith`). |
| `bm_manifest_lifeforce_decision` | Decisions & Situation | Free upfront (options cost 100/250/500/1000p). CD: 1 yr. | Blood Mage or Blood Knight, piety >= 100, piety rank >= 2. | +3 to +12 `enlightenment` | Opens interaction modal popup (`bm_manifest_lifeforce_interaction`) with 4 offering tiers (100p: 50% fail -> 4% floor; 250p: 25% fail -> 3% floor; 500p: guaranteed Minor, 1x/2x Major/Minor options; 1000p: guaranteed Minor & 1 Major, 1x/2x Major/Superior options). |
| `bm_manifest_superior_lifeforce_decision` | Decisions & Situation | 250 piety + Minor + Major Lifeforce. CD: 2 yrs. | Blood Mage or Blood Knight, piety rank >= 3. | +2 to +8 `ancient` | Learning duel to condense Minor and Major into Superior Lifeforce (50% fail at L0 -> 30% at L20 -> 4% floor at L50+). |
| `bm_cast_blood_magic_minor_decision` | Decisions & Situation | Decision free; rites cost 0–100p + Minor Lifeforce. Per-rite CD flags. | Blood Mage or Blood Knight with Minor Lifeforce. | Dependent on rite (+1–2 `enlightenment`, +2 `bloodline`/`benediction` for purge, +2 `ancient` for condense, +4 `ancient` for minor rune) | Opens minor ritual selection (`bm_cast_blood_magic_minor.001`): Channel Minor Lifeforce, Condense Lifeforce (forge Major), Purge Impurities, Inscribe Minor Blood Rune (+4 `ancient`), Flay Minor Rune (`bm_blood_runes.002`). |
| `bm_attune_lifeforce_decision` | Decisions & Situation | 25p + Minor Lifeforce. No CD. | Blood Mage or Blood Knight with Minor Lifeforce, piety >= 25. | None (passive +1/yr XP) | Interactive multi-choice widget (`decision_view_widget_option_list_generic` with `show_from_start = yes`). Attunes character to 1 of 5 class tracks, guaranteeing +1 XP/yr (+2 with Superior **Hulinhjálmur**) and passive blessings. |
| `bm_cast_blood_magic_major_decision` | Decisions & Situation | Decision free; rites cost 75–600p + Major Lifeforce. Per-rite CD flags (2–5 yrs). | Blood Mage or Blood Knight with Major Lifeforce, rank >= 1 Devotion. | +3 to +5 track XP per rite | Opens major ritual selection (`bm_cast_blood_magic_major.001`): Blood Empowerment (+10 Empowerment XP), Enhance Education (tiers 1–4), Inscribe Major Blood Rune (+5 `ancient`), Flay Major Rune (`bm_blood_runes.002`), Empower Bloodline (+5 `bloodline`/`vanguard`), Manifest Perfection Ranks 1–2 (+4 `bloodline`/`vanguard`). |
| `bm_cast_blood_magic_superior_decision` | Decisions & Situation | Decision free; rites cost 350–1500p + Superior Lifeforce. Per-rite CD flags (2–5 yrs). | Blood Mage or Blood Knight with Superior Lifeforce, rank >= 2 Devotion. | +5 to +20 track XP per rite | Opens superior ritual selection (`bm_cast_blood_magic_superior.001`): Master Education (5★), Embrace New Education (2nd trait), Inscribe Superior Blood Rune (+10 `ancient`), Flay Superior Rune (`bm_blood_runes.002`), Manifest Apex Perfection Ranks 3–5 (+6 `bloodline`/`vanguard`, +2 `enlightenment`), Forge Blood Golem (+5 `bloodline`/`vanguard`). |

## Where the details live

| Concept | File in `common/decisions/` |
| --- | --- |
| Ritual of Blood, Blood Cultist to Blood Mage | `become_mage/bm_become_blood_mage_decision.txt` |
| Convert from Witch | `become_mage/bm_convert_from_witch.txt` |
| Seek Power (landed, adventurer, blood knight) | `get_lifeforce/bm_seek_power_decision.txt` |
| Manifest Lifeforce | `get_lifeforce/bm_manifest_lifeforce.txt` |
| Manifest Superior Lifeforce | `get_lifeforce/bm_manifest_superior_lifeforce.txt` |
| Major Rituals (Empowerment, Education 1-4, Major Rune, Bloodline, Manifest 1-2) | `cast_magic/bm_cast_blood_magic_major.txt` |
| Superior Rituals (Master Education 5★, New Education, Superior Rune, Transcendent Perfection 3-5, Blood Golem) | `cast_magic/bm_cast_blood_magic_superior.txt` |
| Minor Rituals (Channel Minor, Condense, Purge, Minor Rune) | `cast_magic/bm_cast_blood_magic_minor.txt` |
| Lifeforce Attunement (Option-list Widget) | `cast_magic/bm_attune_lifeforce_decision.txt` |
| Blood Golem Creation (Standalone) | `cast_magic/bm_create_blood_golem.txt` |
| Mass Lifedrain of Prisoners | `bm_mass_lifedrain_prisoners.txt` |
| Become Blood Cultist (Religious) | `religion/bm_become_blood_cultist_decision.txt` |
| Reformation Repair (Religious) | `religion/bm_reformation_repair_decision.txt` |
| Debug decisions | `bm_debug_decisions.txt` |
