# Blood Mage Decisions

## Executive Summary

- **What:** Player-facing actions for blood mages. Grouped under `bm_decision_group`.
- **Types:**
  - **Standard Decisions:** Visible in main realm decisions list.
  - **Situation Actions:** `is_invisible = yes`. Visible exclusively in the Blood Magic story panel (`bm_blood_mage_story`).

### Decisions Master Table

| Decision ID | Panel Type | Cost & Cooldown | Requirements | XP Gain | Primary Effect |
| --- | --- | --- | --- | --- | --- |
| `bm_blood_cultist_become_blood_mage_decision` | Standard | Decision free (costs 1 Devotion level for Learning duel, 1 Fame level for Prowess duel). No cooldown. | Follows Blóðtrú faith, missing Blood Mage or Blood Knight, Piety or Prestige level >= 2. Location: Reykjavik or Tsushima. | None | Initiates `bm_geyser_duel.0001` against Egill (Learning for `lifestyle_blood_mage`, Prowess for `lifestyle_blood_knight`). |
| `bm_enhance_blood_ritual_decision` | Standard | Decision free (costs 1 Devotion level for Learning duel, 1 Fame level for Prowess duel). No cooldown. | Non-Blóðtrú, missing Blood Mage or Blood Knight, Piety or Prestige level >= 2, qualifying stats/traits. Location: Reykjavik or Tsushima. | None | Initiates `bm_geyser_duel.0001` against Egill (Learning for `lifestyle_blood_mage`, Prowess for `lifestyle_blood_knight`). |
| `convert_to_blood_magic_from_witch` | Standard | Free. No cooldown. | Player only. Has witch trait. | None | Removes witch trait, grants blood mage. |
| `bm_elevate_to_blood_mage_decision` | Standard | 100 Piety. CD: 2 yrs on fail (`bm_elevation_attempt_cooldown`). | Has `lifestyle_blood_knight`, Piety level >= 2, Minor or Major Lifeforce held. | Transfers ancient/benediction/enlightenment 1:1; 50% martial (vanguard->bloodline, slaughter->hematurgy) | Fires elevation trial `bm_blood_knight_elevation.0001` (Learning or Prowess test) to convert to `lifestyle_blood_mage`. |
| `seek_power_decision` | Standard | Free. CD: 2 yrs. | Feudal/landed blood mage. | +1-2 school | Wilderness hunt event chain (`seek_power.001`). Harvests lifeforce. |
| `seek_power_decision_wanderer` | Standard | Free. CD: 1 yr. | Landless adventurer blood mage. | +1-2 school | Landless wilderness event chain. |
| `seek_power_decision_blood_knight` | Standard | Free. CD: 1 yr. | Pure blood knight (`NOT = { has_trait = lifestyle_blood_mage }`). | +slaughter/vanguard/enlightenment | Wilderness hunt event chain (`seek_power.001`). Harvests lifeforce. |
| `blood_golem_creation_decision` | Standard | 500p + Superior Lifeforce. CD: 3 yrs. | High learning/track XP. | +5 bloodline | Spawns courtier in `bm_house_golem`, triggers shaping duel (`blood_golem.001`). |
| `mass_lifedrain_prisoners_decision` | Situation | None. No CD. | Dungeon prisoners available. | +hematurgy | Mass harvests lifeforce from dungeon prisoners (`bm_mass_lifedrain.001`). |
| `become_blood_cultist_decision` | Religious | 250p + 1 Major Lifeforce. CD: 10 yrs. | Blood mage, Rank 2 Devotion. | None | Fires `bm_faith_conversion.0001` to convert character and realm to cultural Blóðtrú faith. |
| `bm_repair_blodtru_reformation_decision` | Religious | None. No CD. | Blóðtrú faith, broken/unformed temporal head title. | None | Clears corrupted head of faith title and resets temporal headship. |
| `bm_manifest_lifeforce_decision` | Standard | 100 piety. CD: 1 yr. | Blood mage or Blood Knight, piety rank >= 2. | +3 enlightenment (Mage & Knight) | Learning duel to generate Lifeforce. Crit gives Major Lifeforce. |
| `bm_manifest_superior_lifeforce_decision` | Standard | 250 piety + Minor + Major Lifeforce. CD: 2 yrs. | Piety rank >= 2. | +2 to +8 ancient | Learning duel to distill Minor and Major into Superior Lifeforce. |
| `bm_cast_blood_magic_minor_decision` | Standard | Decision free; rites cost 25-100p + Minor Lifeforce. | Blood mage or Blood Knight with Minor Lifeforce. | Dependent on rite (+1-2 enlightenment, +2 bloodline for communion, +2 bloodline/ancient for purge, +2 ancient for condense) | Opens minor ritual selection (`bm_cast_blood_magic_minor.001`): Channel Minor Lifeforce, Attune Lifeforce, Condense Lifeforce (forge Major), Commune with Bloodline, Purge Impurities. |
| `bm_cast_blood_magic_major_decision` | Standard | Decision free; rites cost 150-350p + Major Lifeforce. Per-rite CD flags (2-5 yrs). | Blood mage or Blood Knight with Major Lifeforce, rank >= 1 Devotion. | +3 to +5 track XP per rite | Opens major ritual selection (`bm_cast_blood_magic_major.001`): Blood Empowerment, Enhance Education (tiers 1-4), Inscribe Minor/Major Blood Rune (+4/+5 ancient), Empower Bloodline (+5 bloodline), Manifest Perfection (+4 bloodline). |
| `bm_cast_blood_magic_superior_decision` | Standard | Decision free; rites cost 200-1000p + Superior Lifeforce. Per-rite CD flags (2-5 yrs). | Has superior lifeforce, rank >= 2 Devotion. | +5 to +10 track XP per rite | Opens superior ritual selection (`bm_cast_blood_magic_superior.001`): Master Education (5★), Embrace New Education, Inscribe Superior Blood Rune (+10 ancient), Manifest Transcendent Perfection (+6 bloodline, +2 enlightenment), Forge Blood Golem (+5 bloodline). |

## Where the details live

| Concept | File in `common/decisions/` |
| --- | --- |
| Ritual of Blood, Blood Cultist to Blood Mage | `become_mage/bm_become_blood_mage_decision.txt` |
| Convert from Witch | `become_mage/bm_convert_from_witch.txt` |
| Elevate Blood Knight to Blood Mage | `become_mage/bm_elevate_blood_knight_decision.txt` |
| Seek Power (landed, adventurer, blood knight) | `get_lifeforce/bm_seek_power_decision.txt` |
| Manifest Lifeforce | `get_lifeforce/bm_manifest_lifeforce.txt` |
| Manifest Superior Lifeforce | `get_lifeforce/bm_manifest_superior_lifeforce.txt` |
| Major Rituals (Empowerment, Education 1-4, Runes 1-2, Bloodline, Manifest 1-3) | `cast_magic/bm_cast_blood_magic_major.txt` |
| Superior Rituals (Master Education 5★, New Education, Superior Rune, Transcendent Perfection 4-5, Blood Golem) | `cast_magic/bm_cast_blood_magic_superior.txt` |
| Minor Rituals (Channel Minor, Attunement, Condense, Commune, Purge) | `cast_magic/bm_cast_blood_magic_minor.txt` |
| Blood Golem Creation (Standalone) | `cast_magic/bm_create_blood_golem.txt` |
| Mass Lifedrain of Prisoners | `bm_mass_lifedrain_prisoners.txt` |
| Become Blood Cultist (Religious) | `religion/bm_become_blood_cultist_decision.txt` |
| Reformation Repair (Religious) | `religion/bm_reformation_repair_decision.txt` |
| Debug decisions | `bm_debug_decisions.txt` |


Costs, gating, cooldowns and AI weights are in those files. Descriptions and tooltips are in `localization/english/`.

## How the parts connect

- Gating is progression-driven. Stronger actions need more standing and more experience in the blood mage tracks (see `blood-mage-traits.md`). Using blood magic in turn grants track XP.
- Decisions mostly trigger events (`seek_power.*`, `blood_golem.*`, `bm_channel_lifeforce_bloodline.*`, `bm_mass_lifedrain.*`). The decision is the entry point and the event holds the story and the outcome.
- Acquisition routes share `bm_become_blood_mage_effect`, which also creates the story cycle.
- AI uses a few shared modifiers: one for self-preservation (health) and one for acquisition through the prevalence rule. Player-only actions switch the AI off.

## Gotchas

- A new blood magic decision must be added to the story's decision list to appear in the panel.
- Costs are charged by the engine from the decision's `cost`. Don't charge them again in the effect (see `.agents/rules/ck3-decisions.md`).
- Keep acquisition routes going through the shared effect. Don't add the trait directly.

## Not verified

AI behaviour, in-game gating and the outcome of the gambles haven't been tested. This is derived from the files and English localization.
