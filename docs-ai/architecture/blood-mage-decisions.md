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
| `channel_lifeforce_bloodline` | Standard | 350p + Major Lifeforce. CD: 3 yrs. | Has noble house. | +5 bloodline | Event `bm_channel_lifeforce_bloodline.001`. Adds permanent house modifier. |
| `blood_golem_creation_decision` | Standard | 750p + Major Lifeforce. CD: 3 yrs. | High learning/track XP. | +5 bloodline | Spawns courtier in `bm_house_golem`, triggers shaping duel (`blood_golem.001`). |
| `mass_lifedrain_prisoners_decision` | Situation | None. No CD. | Dungeon prisoners available. | +hematurgy | Mass harvests lifeforce from dungeon prisoners (`bm_mass_lifedrain.001`). |
| `become_blood_cultist_decision` | Major | None. Rank 3 Devotion + 1 Major Lifeforce. | Blood mage. | None | Converts character and realm to Blóðtrú faith. |

## Where the details live

| Concept | File in `common/decisions/` |
| --- | --- |
| Ritual of Blood, Blood Cultist to Blood Mage | `bm_become_blood_mage_decision.txt` |
| Convert from Witch | `bm_convert_from_witch.txt` |
| Seek Power (landed & adventurer) | `bm_seek_power_decision.txt` |
| Channel Lifeforce into Bloodline | `bm_channel_lifeforce.txt` |
| Blood Golem Creation | `bm_create_blood_golem.txt` |
| Mass Lifedrain of Prisoners | `bm_mass_lifedrain_prisoners.txt` |
| Become Blood Cultist (Major) | `bm_become_blood_cultist_decision.txt` |
| Debug decisions | `bm_debug_decisions.txt` |

*(Note: All rituals targeting the character themselves—such as Channel Minor Lifeforce, Attunement, Manifest Lifeforce, Crimson Empowerment, Enhance Education, Embrace New Education, and Blood Runes—are exclusively character interactions in `common/character_interactions/bm_cast_blood_magic_self_*.txt`.)*

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
