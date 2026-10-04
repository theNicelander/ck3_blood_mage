# Blood Mage Decisions

> Living document. Follow `AGENTS.md` in this folder: concepts only, no numbers. Update it when a decision is added, removed or changes meaning.

## Purpose

Decisions are the player-facing actions of a blood mage, plus the routes into blood magic. Most are grouped together under the mod's own decision group. Heavier actions hand off to an event or a character interaction for the real consequences.

## Concepts

### Becoming a blood mage

There are several ways in, and all end in the shared `bm_become_blood_mage_effect`.

- **Enhance Blood Ritual** is the risky route for an outsider who is capable and desperate enough. It is a struggle against the raw power of blood. Success makes them a blood mage and failure leaves lasting mental, physical or injury scars.
- **Challenge the Blood Mage of Reykjavik** is an initiation duel located at the holy site in Reykjavik. An outsider challenges a hermit blood mage in an arcane contest of Learning backed by Prowess, awakening blood magic on victory or suffering severe backlash on defeat.
- **Blood Cultist to Blood Mage** is the route for followers of the Quintessence faith. It is a deliberate, low-risk initiation.
- **Convert from Witch** is a conversion that swaps witchcraft for blood magic. It is player-only.

### Using blood magic

These appear in the Blood Magic panel (see `blood-mage-story.md`).

- **Seek Power** is an event chain in the wilderness. The mage hunts beasts, meets a lost traveller or finds something stranger, and can gain extra Lifeforce. Landless adventurers get their own variant of the same decision, because they have fewer prisoners and so need a different source.
- **Manifest Lifeforce** converts spiritual power directly into Lifeforce. The outcome is a gamble on Learning, from a major gain through to a backfire.
- **Channel Lifeforce into the Bloodline** is a ritual that extends blood magic across the whole dynasty. It feeds the Bloodline track.
- **Blood Golem Creation** is a major ritual that builds a golem servant. It leads to the blood golem events, where the golem can be enhanced.
- **Mass Lifedrain of Prisoners** harvests Lifeforce from the dungeon. The mage chooses between draining everyone and sparing those with valuable traits.

### Faith

- **Become Blood Cultist** moves a blood mage into the Cult of Quintessence. It respects the game rules for religion and is hidden for overhaul mods.

### Debug

Debug decisions exist to add or remove Lifeforce and XP while testing. They aren't gameplay.

## Where the details live

| Concept | File in `common/decisions/` |
| --- | --- |
| Enhance Blood Ritual, Blood Cultist to Blood Mage | `bm_become_blood_mage_decision.txt` |
| Challenge the Blood Mage of Reykjavik | `bm_reykjavik_blood_mage_duel_decision.txt` |
| Convert from Witch | `bm_convert_from_witch.txt` |
| Seek Power (normal and wanderer) | `bm_seek_power_decision.txt` |
| Manifest Lifeforce | `bm_manifest_lifeforce.txt` |
| Channel Lifeforce into the Bloodline | `bm_channel_lifeforce.txt` |
| Blood Golem Creation | `bm_create_blood_golem.txt` |
| Mass Lifedrain of Prisoners | `bm_mass_lifedrain_prisoners.txt` |
| Become Blood Cultist | `bm_become_blood_cultist_decision.txt` |
| Debug | `bm_debug_decisions.txt` |

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
