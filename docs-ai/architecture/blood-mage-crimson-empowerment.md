# Crimson Empowerment

> Living document. Follow `AGENTS.md` in this folder: concepts only, no numbers. Update it when the trait, tracks, empowerment events or retinue modifiers change.

## Executive Summary

- **How to get it:** Unlocked via the `bm_crimson_empowerment_decision` decision in the Situation panel, triggering `bm_crimson_empowerment_event.001` (adds `lifestyle_crimson_empowerment` on first use).
- **What it does:** Advanced lifestyle trait granting passive ruler and realm boosts across 7 specialization tracks. Acts as the prerequisite gate for high-tier self-cast blood magic (upgrading education, acquiring a second education trait, and inscribing blood runes).
- **How to level it up:** Active channeling only. Each channel decision costs major Lifeforce and grants **10 XP** in the selected track (via `add_crimson_empowerment_xp`).

### Simplified Track Benefits Table

Each track spans 10 levels (10 to 100 XP, 10 XP per channel). All 10 levels in each track share the same active modifiers, including a **Universal Baseline** (`+1` Life Expectancy, `+0.1` Monthly Piety) per active tier:

| Track | Specialization Theme | Benefits per Level (All Levels 10–100) |
| --- | --- | --- |
| `charisma` | Diplomatic Majesty | Baseline + `+2.5` General Opinion, `+5%` Monthly Prestige Gain Mult |
| `fury` | Battlefield Slaughter | Baseline + `+5%` Knight Effectiveness, `+0.05` Monthly County Control Growth |
| `prosperity` | Domain Wealth | Baseline + `+2.5%` Domain Tax, `+0.05` Capital County Monthly Development Growth |
| `shadows` | Dread & Espionage | Baseline + `+3` Dread Baseline, `-0.01` Monthly Tyranny (decay), `+5` Scheme Secrecy |
| `insight` | Esoteric Lore | Baseline + `+5%` Development Growth (all holdings), `+5%` Monthly Piety Gain Mult |
| `legacy` | Bloodline Eugenics | Baseline + `+5%` Positive Congenital Chance, `+5%` Inactive Positive Inheritance |
| `expertise` | Self-Mastery | Baseline + `+2.5%` Lifestyle XP Gain Mult, `+5%` Cultural Fascination Mult |
| *Versatility* | Capped Track Fallback | 10-year buff `temporary_buff_self` (`+2` all stats, `+4` Prowess) & rolls for permanent stat points (`+1` skill, `+2` Prowess) |

## Purpose

Crimson Empowerment is an advanced, secondary supernatural discipline available to seasoned blood mages. Where basic blood magic manipulates life fluid and vitality, Crimson Empowerment refines that raw power inward to transform the mage's aura, presence, and battlefield fury, or outward to elevate elite mortal followers into superhuman retainers.

## Concepts

- **The Trait.** `lifestyle_crimson_empowerment` is a distinct lifestyle trait separate from `lifestyle_blood_mage`. It features dedicated tracks that enhance ruler attributes, realm governance, personal lethality, and bloodline potency.
- **Awakening and Growth.** The trait is awakened and advanced through `bm_crimson_empowerment_decision`. This triggers `bm_crimson_empowerment_event.001`, where the mage selects which aspect to advance. Capped tracks (100 XP) are excluded from selection.
- **High-Tier Magic Gates.** Total accumulated experience in `lifestyle_crimson_empowerment` gates advanced self-enhancement rituals: upgrading education traits, acquiring a secondary education trait, and inscribing blood runes.
- **Empowered Retinue.** Blood mages can project empowerment outward onto courtiers:
  - *Crimson Warriors:* Infuses a courtier with enhanced combat abilities at slight physical strain (`lifeforce_modifier_crimson_warrior`).
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
| Versatility modifier | `common/modifiers/bm_modifiers.txt` (`temporary_buff_self`) |
| XP scripted effects | `common/scripted_effects/bm_trait_track_xp_gain_effects.txt` (`add_crimson_empowerment_xp`) |
| High-tier spell gates | `common/character_interactions/bm_cast_blood_magic_self_major.txt`, `common/decisions/bm_enhance_education_decision.txt` |
| Story panel retinue roster | `common/scripted_effects/bm_blood_mage_story_list_effects.txt` |

## How the parts connect

- When a blood mage reaches high proficiency, they spend Lifeforce via `bm_crimson_empowerment_decision`.
- The decision fires `bm_crimson_empowerment_event.001`, which adds the trait if not present and awards track XP via `add_crimson_empowerment_xp`.
- Advancing Crimson Empowerment unlocks high-tier rituals (education enhancement and blood runes) once overall empowerment experience meets the requisite gates.
- The interactions `grant_crimson_warrior_interaction` and `grant_crimson_champion_interaction` consume the caster's Lifeforce to apply modifiers to selected courtiers.
- The story cycle refreshes the retinue roster whenever courtiers are granted or stripped of empowerment.

## Gotchas

- `lifestyle_crimson_empowerment` does not grant passive XP over time; it only advances when the player or AI explicitly invests major Lifeforce into the empowerment decision.
- Crimson Champions suffer significant health and life expectancy penalties; they are terrifying combatants but have shorter lifespans.
- All seven empowerment tracks share baseline increases to life expectancy and monthly piety, so advancing multiple tracks compounds longevity and spiritual power.

## Not verified

AI rulers balancing the heavy physical drain of sustaining multiple Crimson Champions against the military advantage provided in ongoing wars.
