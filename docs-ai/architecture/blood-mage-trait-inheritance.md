# Blood Mage Trait Inheritance

> Living document. Follow `AGENTS.md` in this folder: concepts only, no numbers. Update it when trait inheritance rules, birth on-actions, or lineage modifiers change.

## Purpose

Trait inheritance in the Blood Mages mod determines how supernatural bloodlines pass power down through generations. Rather than using CK3's vanilla tiered or recessive genetic system, the mod uses explicit direct inheritance chances paired with birth prevalence auditing to govern who inherits blood magic, how game rules control AI proliferation, and how mages can supernaturally alter the inheritance of their lineage.

## Concepts

- **Direct Hereditary Lifestyle Trait.** `lifestyle_blood_mage` is hereditary, but it is not a recessive genetic trait. It relies on explicit engine inheritance chances. A child of one blood mage parent can inherit the trait, while a child of two blood mage parents is guaranteed to inherit it.
- **Spontaneous Manifestation at Birth.** Children born to non-mage parents can occasionally awaken blood magic spontaneously at birth or during character generation.
- **Birth Prevalence Auditing.** Whenever an AI newborn inherits or manifests blood magic, birth on-actions audit the child against active prevalence game rules. AI children who fail retention checks have the trait removed immediately, and under Player Only mode, all AI inheritance is strictly blocked.
- **Non-Hereditary Personal Mastery.** `lifestyle_crimson_empowerment` is strictly non-hereditary. It represents individual power accrued through active casting rituals and cannot be passed to descendants.
- **Lineage Trait Enhancement.** Blood mages can enhance the inheritance of other congenital traits across their family. Advancing the Legacy track of Crimson Empowerment and enacting Crimson Legacy house modifiers increases the odds of descendants inheriting positive inactive traits while suppressing negative traits.
- **Trait Theft Bypass.** Rather than relying on generational inheritance, blood mages can bypass reproduction entirely by siphoning congenital traits directly from captive subjects via duels.

## Where the details live

| Piece | File |
| --- | --- |
| Blood Mage trait definition & inheritance chances | `common/traits/bm_blood_mage_trait.txt` |
| Crimson Empowerment definition (non-hereditary) | `common/traits/bm_crimson_empowerment_trait.txt` |
| Birth prevalence on-actions | `common/on_action/bm_blood_mage_prevalence_on_actions.txt` |
| Prevalence retention scripted effects | `common/scripted_effects/bm_blood_mage_lifecycle_effects.txt` |
| Crimson Empowerment legacy track modifiers | `common/traits/bm_crimson_empowerment_trait.txt` |
| Crimson Legacy house modifier | `common/modifiers/bm_channel_dynasty_modifiers.txt` |
| Trait drain interaction & duel effects | `common/character_interactions/bm_drain_trait.txt`, `common/scripted_effects/bm_drain_trait_effects.txt` |
| Prevalence game rules | `common/game_rules/bm_game_rules.txt` (`bm_blood_mage_prevalence`) |

## How the parts connect

- When a child is born, the base engine rolls inheritance chances from parents who have `lifestyle_blood_mage`.
- The `on_birth_child` on-action triggers `bm_apply_blood_mage_prevalence_at_birth`.
- AI children born with the trait are audited by `bm_apply_blood_mage_prevalence_retention_effect`:
  - If the active game rule permits retention, the child retains the trait, sets the reviewed flag, and initializes their story cycle via `bm_ensure_blood_mage_story_effect`.
  - If retention fails (or Player Only mode is active), the trait is immediately stripped.
- Under high-frequency game rules, AI children who did not inherit naturally receive a secondary roll to awaken blood magic if either parent is a practitioner.
- Blood mages channeling house legacy or progressing in the Legacy empowerment track bestow modifiers that raise the transmission rate of positive inactive traits to their descendants.

## Gotchas

- The Blood Mage trait does not use `genetic = yes`; making it genetic would route it through CK3's recessive trait mechanics instead of the mod's explicit inheritance logic.
- AI children who inherit the trait naturally must still be processed by the prevalence retention effect; otherwise, unreviewed AI blood mages proliferate beyond configured game rules and lack the Blood Magic story panel.
- Crimson Empowerment is personal and never inherited; any power passed to heirs must be achieved through dynasty modifiers or by training them after birth.

## Not verified

Generational trait retention across multi-century AI dynasties with mixed human and golem lineages.
