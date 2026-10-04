# Blood Mage Character Interactions

> Living document. Follow `AGENTS.md` in this folder: concepts only, no numbers. Update it when interactions are added, removed, or change targeting and effects.

## Purpose

Character interactions provide targeted, interpersonal expressions of blood magic. Through interactions, a blood mage can target prisoners, courtiers, family members, or themselves to harvest vitality, bestow blessings, bestow the Blood Mage trait, cure severe afflictions, or empower loyal champions.

## Concepts

- **Acquisition Interactions.** Uninitiated characters can petition known blood mages (`ask_for_blood_magic_interaction`) or forcibly extract secrets and power from imprisoned blood mages (`bm_get_blood_magic_from_prisoner_interaction`).
- **Vitality Harvesting.** Mages drain essence from prisoners (`lifedrain_prisoner_interaction`) to gain Lifeforce and execute them, or harvest courtiers (`lifedrain_courtier_event_interaction`) with a risk of debilitating or killing the victim.
- **Genetic & Trait Theft.** `trait_drain_prisoner_event_interaction` allows a blood mage to steal congential and physical traits from captive subjects through a psychic and physical duel.
- **Healing & Restoration.** Benediction interactions (`heal_disease_minor`, `heal_disease_major`, `heal_disease_benediction`) allow a blood mage to burn Lifeforce to purge diseases, wounds, and severe ailments from targets.
- **Empowerment of Others.** Mages can impart vitality to allies (`grant_lifeforce_interaction`) or empower martial servants into Crimson Warriors and Crimson Champions (`grant_crimson_warrior_interaction`, `grant_crimson_champion_interaction`).
- **Self-Targeted Rituals.** Grouped into major and minor interactions targeting oneself (`bm_cast_blood_magic_self_major`, `bm_cast_blood_magic_self_minor`), allowing the mage to attune vitality, channel minor boons, inscribe Crimson Runes, pursue additional educations, or awaken Crimson Empowerment.

## Where the details live

| Interaction Group | File |
| --- | --- |
| Become a Blood Mage (request or take from prisoner) | `common/character_interactions/bm_become_a_blood_mage.txt` |
| Harvest Lifeforce (prisoner execution or courtier drain) | `common/character_interactions/bm_drain_lifeforce.txt` |
| Drain Traits from Prisoners | `common/character_interactions/bm_drain_trait.txt` |
| Cure Illness (minor, major, benediction) | `common/character_interactions/bm_cure_illness_interactions.txt` |
| Grant Blood Infused Prowess (Crimson retinue) | `common/character_interactions/bm_grant_blood_infused_prowess.txt` |
| Grant Blood Magic Trait to Others | `common/character_interactions/bm_grant_blood_magic.txt` |
| Grant Lifeforce Stacks to Others | `common/character_interactions/bm_grant_lifeforce.txt` |
| Self Magic (Major: education, runes, empowerment) | `common/character_interactions/bm_cast_blood_magic_self_major.txt` |
| Self Magic (Minor: attunement, stat channeling) | `common/character_interactions/bm_cast_blood_magic_self_minor.txt` |

## How the parts connect

- Interactions trigger scripted effects in `bm_blood_magic_used_effects.txt` for Lifeforce consumption and XP award.
- Self-targeted interactions hand off to event chains (such as `bm_education_enhance.txt`, `bm_crimson_rune.001`, and `bm_crimson_empowerment_event.001`).
- Granting martial prowess applies warrior/champion modifiers and adds those courtiers to the story roster described in `blood-mage-story.md`.
- AI targeting strictly follows the patterns documented in `.agents/rules/ck3-decisions.md` and `ck3-ai.md` using `ai_targets` scopes to avoid expensive global character scans.

## Gotchas

- Self-targeted interactions require `ai_targets = { ai_recipients = self }` to allow AI mages to trigger them.
- Draining interactions consider imprisonment status, dread, and opinion penalties. Executing via lifedrain applies kinslayer penalties if the victim is family.
- AI harvesting of courtiers enforces strict `factor = 0` vetoes to prevent draining close family, children, spouses/consorts, friends/lovers, knights, councillors, and high-opinion subjects.
- Many interactions hide themselves if the actor lacks positive Lifeforce modifiers or prerequisite XP thresholds.

## Not verified

AI recipient acceptance calculations across varying cultural acceptance doctrines in third-party total conversion mods.
