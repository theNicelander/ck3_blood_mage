# Crimson Empowerment

> Living document. Follow `AGENTS.md` in this folder: concepts only, no numbers. Update it when the trait, tracks, empowerment events or retinue modifiers change.

## Purpose

Crimson Empowerment is an advanced, secondary supernatural discipline available to seasoned blood mages. Where basic blood magic manipulates life fluid and vitality, Crimson Empowerment refines that raw power inward to transform the mage's aura, presence, and battlefield fury, or outward to elevate elite mortal followers into superhuman retainers.

## Concepts

- **The Trait.** `lifestyle_crimson_empowerment` is a distinct lifestyle trait separate from `lifestyle_blood_mage`. It features dedicated tracks such as Charisma and Fury that bolster ruler prestige, personal presence, opinion, and combat prowess.
- **Awakening and Growth.** The trait is awakened and advanced through the decision `bm_crimson_empowerment_decision` (accessed in the Situation panel, hidden from the main decision list, without a cooldown). This triggers event `bm_crimson_empowerment_event.001`, where the mage selects which aspect of empowerment to advance.
- **Empowered Retinue.** Blood mages can also project this empowerment onto loyal courtiers through character interactions:
  - *Crimson Warriors:* Infuses a courtier with enhanced combat abilities at the expense of slight physical strain (`lifeforce_modifier_crimson_warrior`).
  - *Crimson Champions:* Elevates a warrior into a terrifying martial juggernaut with massive prowess bonuses at high physical toll (`lifeforce_modifier_crimson_champion`).
- **Story Roster.** Crimson warriors and champions are automatically identified by `bm_refresh_blood_magic_rosters_effect` and grouped into the mage's Crimson Retinue on the Blood Magic panel.

## Where the details live

| Piece | File |
| --- | --- |
| Trait definition | `common/traits/bm_crimson_empowerment_trait.txt` |
| Advancement event | `events/bm_crimson_empowerment_event.txt` (`bm_crimson_empowerment_event.001`) |
| Awakening decision | `common/decisions/bm_crimson_empowerment_decision.txt` (`bm_crimson_empowerment_decision`) |
| Bestow prowess interactions | `common/character_interactions/bm_grant_blood_infused_prowess.txt` |
| Retinue modifiers | `common/modifiers/bm_lifeforce.txt` |
| XP scripted effects | `common/scripted_effects/bm_trait_track_xp_gain_effects.txt` (`add_crimson_empowerment_xp`) |
| Story panel retinue roster | `common/scripted_effects/bm_blood_mage_story_list_effects.txt` |

## How the parts connect

- When a blood mage reaches high proficiency, they spend Lifeforce via `bm_crimson_empowerment_decision`.
- The decision fires `bm_crimson_empowerment_event.001`, which adds the trait if not present and awards track XP via `add_crimson_empowerment_xp`.
- The interactions `grant_crimson_warrior_interaction` and `grant_crimson_champion_interaction` consume the caster's Lifeforce to apply modifiers to selected courtiers.
- The story cycle refreshes the retinue roster whenever courtiers are granted or stripped of empowerment.

## Gotchas

- `lifestyle_crimson_empowerment` does not grant passive XP over time; it only advances when the player or AI explicitly invests major Lifeforce into the empowerment decision.
- Crimson Champions suffer significant health and life expectancy penalties; they are terrifying combatants but have shorter lifespans.

## Not verified

AI rulers balancing the heavy physical drain of sustaining multiple Crimson Champions against the military advantage provided in ongoing wars.
