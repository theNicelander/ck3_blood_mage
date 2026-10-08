# Blood Mage Decisions

## Executive Summary

- **What:** Player-facing actions for blood mages. Grouped under `bm_decision_group`.
- **Types:**
  - **Standard Decisions:** Visible in main realm decisions list.
  - **Situation Actions:** `is_invisible = yes`. Visible exclusively in the Blood Magic story panel (`bm_blood_mage_story`).

### Decisions Master Table

| Decision ID | Panel Type | Cost & Cooldown | Requirements | XP Gain | Primary Effect |
| --- | --- | --- | --- | --- | --- |
| `bm_become_blood_mage_decision` | Standard | 100 piety. No cooldown. | Follows Blóðtrú faith. | None | Grants `lifestyle_blood_mage` via `bm_become_blood_mage_effect`. |
| `bm_become_blood_mage_ritual_decision` | Standard | 250 piety. CD: 5 yrs. | Non-Blóðtrú. Location: Reykjavik or Tsushima. | None | Learning duel. Success: blood mage. Failure: wounds/stress/scarring. |
| `bm_convert_from_witch_decision` | Standard | 100 piety. No cooldown. | Player only. Has witch trait or secret. | None | Removes witch trait/secret, grants blood mage. |
| `bm_seek_power_decision` | Standard | 50g, 100p. CD: 5 yrs. | Feudal/landed blood mage. | +1-2 school | Wilderness hunt event chain (`bm_seek_power.0001`). Harvests lifeforce. |
| `bm_seek_power_wanderer_decision` | Standard | 25g, 50p. CD: 3 yrs. | Landless adventurer blood mage. | +1-2 school | Landless wilderness event chain. |
| `channel_lifeforce_bloodline` | Standard | 350p + Major Lifeforce. CD: 3 yrs. | Has noble house. | +5 bloodline | Event `bm_channel_lifeforce_bloodline.001`. Adds permanent house modifier. |
| `bm_create_blood_golem` | Standard | 350p + Major Lifeforce. CD: 5 yrs. | 50 Learning XP. | +3 enlightenment | Spawns courtier in `bm_house_golem`, triggers shaping duel. |
| `bm_enhance_education_decision` | Standard | 500p + Major Lifeforce. CD: 5 yrs. | Req CE XP (10-50). | +3 enlightenment | Upgrades education tier (up to 5-star) via Learning duel. |
| `bm_inscribe_blood_runes_decision` | Situation | Major Lifeforce + 0-400p. No CD. | Req CE XP (25-100). | +3 enlightenment | Inscribes or upgrades body runes (`minor` -> `major` -> `superior`). |
| `bm_manifest_lifeforce` | Situation | 250 piety. CD: none. | Blood mage. | +1 enlightenment | Learning duel. Success: gains Lifeforce. Fail: injury / death risk. |
| `bm_mass_lifedrain_prisoners` | Situation | Piety per prisoner. No CD. | Dungeon prisoners available. | +hematurgy | Mass harvests lifeforce from dungeon prisoners. |
| `bm_attune_lifeforce_decision` | Situation | Free. No CD. | Blood mage. | None | Selects 1 of 5 attunements (+50% yearly chance of +1 school XP). |
| `bm_channel_minor_lifeforce_decision` | Situation | Minor Lifeforce. No CD. | Has `lifeforce_modifier_minor`. | +1 enlightenment | Converts minor lifeforce into temporary stat boost. |
| `bm_crimson_empowerment_decision` | Situation | 150p + Major Lifeforce. No CD. | `piety_level >= 1`. | +3 enlg, +10 CE | Event `bm_crimson_empowerment_event.001`. +10 XP in chosen CE track. |
| `bm_become_blood_cultist_decision` | Standard | 500 piety. Major decision. | Blood mage. | None | Converts character and realm to Blóðtrú faith. |

## Where the details live

| Concept | File in `common/decisions/` |
| --- | --- |
| Ritual of Blood, Blood Cultist to Blood Mage | `bm_become_blood_mage_decision.txt` |
| Convert from Witch | `bm_convert_from_witch.txt` |
| Seek Power (landed & adventurer) | `bm_seek_power_decision.txt` |
| Manifest Lifeforce | `bm_manifest_lifeforce.txt` |
| Channel Lifeforce into Bloodline | `bm_channel_lifeforce.txt` |
| Blood Golem Creation | `bm_create_blood_golem.txt` |
| Mass Lifedrain of Prisoners | `bm_mass_lifedrain_prisoners.txt` |
| Lifeforce Attunement | `bm_attune_lifeforce_decision.txt` |
| Channel Minor Lifeforce | `bm_channel_minor_lifeforce_decision.txt` |
| Channel Crimson Empowerment | `bm_crimson_empowerment_decision.txt` |
| Enhance Education | `bm_enhance_education_decision.txt` |
| Inscribe Blood Runes | `bm_inscribe_blood_runes_decision.txt` |
| Become Blood Cultist (Major) | `bm_become_blood_cultist_decision.txt` |
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
