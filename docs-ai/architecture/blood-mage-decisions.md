# Blood Mage Decisions

## Executive Summary

- **What:** Player-facing actions for blood mages. Grouped under `bm_decision_group`.
- **Types:**
  - **Standard Decisions:** Visible in main realm decisions list.
  - **Situation Actions:** `is_invisible = yes`. Visible exclusively in the Blood Magic story panel (`bm_blood_mage_story`).

### Decisions Master Table

| Decision ID | Panel Type | Cost & Cooldown | Requirements | XP Gain | Primary Effect |
| --- | --- | --- | --- | --- | --- |
| `bm_blood_cultist_become_blood_mage_decision` | Standard | 100 piety. No cooldown. | Follows Blóðtrú faith. | None | Grants `lifestyle_blood_mage` via `bm_become_blood_mage_effect`. |
| `bm_enhance_blood_ritual_decision` | Standard | 250 piety. CD: 5 yrs. | Non-Blóðtrú. Location: Reykjavik or Tsushima. | None | Learning duel. Success: blood mage. Failure: wounds/stress/scarring. |
| `convert_to_blood_magic_from_witch` | Standard | Free. No cooldown. | Player only. Has witch trait. | None | Removes witch trait, grants blood mage. |
| `seek_power_decision` | Standard | Free. CD: 2 yrs. | Feudal/landed blood mage. | +1-2 school | Wilderness hunt event chain (`seek_power.001`). Harvests lifeforce. |
| `seek_power_decision_wanderer` | Standard | Free. CD: 1 yr. | Landless adventurer blood mage. | +1-2 school | Landless wilderness event chain. |
| `blood_golem_creation_decision` | Standard | 500p + Superior Lifeforce. CD: 3 yrs. | High learning/track XP. | +5 bloodline | Spawns courtier in `bm_house_golem`, triggers shaping duel (`blood_golem.001`). |
| `mass_lifedrain_prisoners_decision` | Situation | None. No CD. | Dungeon prisoners available. | +hematurgy | Mass harvests lifeforce from dungeon prisoners (`bm_mass_lifedrain.001`). |
| `become_blood_cultist_decision` | Religious | None. Rank 3 Devotion + 1 Major Lifeforce. | Blood mage. | None | Converts character and realm to Blóðtrú faith. |
| `bm_manifest_lifeforce_decision` | Standard | 100 piety. CD: 1 yr. | Piety rank >= 2. | +5 enlightenment | Learning duel to generate Lifeforce. |
| `bm_manifest_superior_lifeforce_decision` | Standard | 250 piety + Minor + Major Lifeforce. CD: 2 yrs. | Piety rank >= 2. | +2-10 enlightenment | Learning duel to distill Minor and Major into Superior Lifeforce. |
| `bm_cast_blood_magic_minor_decision` | Standard | Decision free; rites cost 25-75p + Minor Lifeforce. | Has minor lifeforce. | Dependent on rite (+1 enlightenment on channel) | Opens minor ritual selection (`bm_cast_blood_magic_minor.001`): Channel Minor Lifeforce, Attune Lifeforce. |
| `bm_cast_blood_magic_major_decision` | Standard | Decision free; rites cost 150-350p + Major Lifeforce. Per-rite CD flags (2-5 yrs). | Has major lifeforce, rank >= 1 Devotion. | +3 to +5 track XP per rite | Opens major ritual selection (`bm_cast_blood_magic_major.001`): Blood Empowerment, Enhance Education (tiers 1-4), Inscribe Minor/Major Blood Rune, Empower Bloodline, Manifest Perfection (ranks 1-3). |
| `bm_cast_blood_magic_superior_decision` | Standard | Decision free; rites cost 200-1000p + Superior Lifeforce. Per-rite CD flags (2-5 yrs). | Has superior lifeforce, rank >= 2 Devotion. | +5 to +10 track XP per rite | Opens superior ritual selection (`bm_cast_blood_magic_superior.001`): Master Education (5★), Embrace New Education, Inscribe Superior Blood Rune, Manifest Transcendent Perfection (ranks 4-5), Forge Blood Golem. |

## Where the details live

| Concept | File in `common/decisions/` |
| --- | --- |
| Ritual of Blood, Blood Cultist to Blood Mage | `bm_become_blood_mage_decision.txt` |
| Convert from Witch | `bm_convert_from_witch.txt` |
| Seek Power (landed & adventurer) | `bm_seek_power_decision.txt` |
| Manifest Lifeforce | `get_lifeforce/bm_manifest_lifeforce.txt` |
| Manifest Superior Lifeforce | `get_lifeforce/bm_manifest_superior_lifeforce.txt` |
| Major Rituals (Empowerment, Education 1-4, Runes 1-2, Bloodline, Manifest 1-3) | `cast_magic/bm_cast_blood_magic_major.txt` |
| Superior Rituals (Master Education 5★, New Education, Superior Rune, Transcendent Perfection 4-5, Blood Golem) | `cast_magic/bm_cast_blood_magic_superior.txt` |
| Minor Rituals (Channel Minor, Attunement) | `cast_magic/bm_cast_blood_magic_minor.txt` |
| Blood Golem Creation (Standalone) | `cast_magic/bm_create_blood_golem.txt` |
| Mass Lifedrain of Prisoners | `bm_mass_lifedrain_prisoners.txt` |
| Become Blood Cultist (Religious) | `bm_become_blood_cultist_decision.txt` |
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
