# Blood Mage Dynasty

> Living document. Follow `AGENTS.md` in this folder: concepts only, no numbers. Update it when a house, dynasty or bloodline modifier is added, removed or changes meaning.

## Executive Summary

- **What:** Permanent supernatural house modifiers applied via `bm_cast_blood_magic_major_decision` (Empower Dynasty Bloodline option).
- **Cost / Requirements:** 350 piety + consumes `lifeforce_modifier_major`. Req: `piety_level >= 1`. Cooldown: 3 years (flag `bm_channel_bloodline_cooldown`).
- **XP Gain:** Awards +5 `bloodline` XP (`add_xp_bm_dynamic`).
- **Feedback Loop:** Each active blood modifier on the house adds +10% yearly chance (up to 70% cap with all 7 modifiers) for blood mages in that house to gain +1 `bloodline` XP (`blood_mage_yearly_events.002`).

### House Modifiers Table

Modifiers apply to all living and future members of the caster's house. Non-legacy modifiers are unique per house; `Legacy` stacks infinitely:

| Modifier | Focus | House Member Benefits |
| --- | --- | --- |
| `dynasty_blood_charisma_modifier` | Diplomacy | `+2` Diplomacy, `+5` General Opinion, `+0.1` Monthly Prestige |
| `dynasty_blood_fury_modifier` | Martial | `+2` Martial, `+3` Prowess, `+15%` Knight Effectiveness, `+1` Knight Limit |
| `dynasty_blood_prosperity_modifier` | Stewardship | `+2` Stewardship, `+0.1` County Control Growth, `+5%` Domain Tax, `+5%` Development Growth |
| `dynasty_blood_shadows_modifier` | Intrigue | `+2` Intrigue, `+5%` Hostile Scheme Success, `-5` Scheme Phase Days; `-5%` Enemy Scheme Success, `+5` Enemy Scheme Phase Days |
| `dynasty_blood_insight_modifier` | Learning | `+2` Learning, `+0.15` Monthly Piety, `+0.05` Capital Dev Growth, `+2` Epidemic Resistance |
| `dynasty_blood_legacy_modifier` *(stacks)* | Bloodline | `+0.3` Health, `+10%` Fertility, `+10%` Positive Genetic Chance/Strengthen, `-10%` Inbreeding & Negative Congenital Chance |
| `dynasty_blood_expertise_modifier` | Mastery | `+5%` Lifestyle XP Mult, `+5%` Learning Lifestyle XP, `+5%` Stress Loss, `-5%` Stress Gain, `-15` Learn Language Phase Days |
| *Fallback (`temporary_buff_bloodline`)* | All Taken | `+1` all skills, `+2` Prowess |

## Key Mechanics

- **Decision Flow:** `bm_cast_blood_magic_major_decision` fires `bm_cast_blood_magic_major.001`, which routes to `bm_channel_lifeforce_bloodline.001`. Applies chosen modifier to `scope:actor.house`.
- **Golem House:** Dedicated house `bm_house_golem` in dynasty `dynn_bm_golem`. `blood_golem_template` places all golems here. Story panel roster identifies owned golems via house membership (`bm_refresh_blood_magic_rosters_effect`).
- **Dynasty Mages Roster:** Story panel tracks living blood mages in ruler's dynasty.

## Where the details live

| Concept | File |
| --- | --- |
| Golem house | `common/dynasty_houses/bm_dynasty_houses.txt` |
| Golem dynasty | `common/dynasties/bm_dynasties.txt` |
| Golem house coat of arms | `common/coat_of_arms/coat_of_arms/bm_coat_of_arms.txt` |
| Bloodline house modifiers | `common/modifiers/bm_channel_dynasty_modifiers.txt` |
| Fallback buff | `temporary_buff_bloodline` in `common/modifiers/bm_modifiers.txt` |
| Channel decision | `bm_cast_blood_magic_major_decision` in `common/decisions/cast_magic/bm_cast_blood_magic_major.txt` |
| Choice event | `bm_channel_lifeforce_bloodline.001` in `events/bm_channel_lifeforce_bloodline_events.txt` |
| Yearly bloodline XP | `blood_mage_yearly_events.002` in `events/bm_yearly_events.txt` |
| Golem template | `blood_golem_template` in `common/scripted_character_templates/bm_character_templates.txt` |
| Golem roster | `bm_refresh_blood_magic_rosters_effect` in `common/scripted_effects/bm_blood_mage_story_list_effects.txt` |
| Dynasty blood mages roster | `bm_refresh_blood_magic_rosters_effect` in `common/scripted_effects/bm_blood_mage_story_list_effects.txt` |
| Panel entry for the decision | `common/story_cycles/bm_blood_mage_story.txt` |
| Names, mottos, modifier text | `localization/english/bm_channel_lifeforce_l_english.yml`, `bm_modifiers_l_english.yml`, `bm_blood_golem_l_english.yml` |

## How the parts connect

- The decision is the entry point. It requires a blood mage with major Lifeforce, triggers the choice event and grants `bloodline` XP.
- The event applies a house modifier to the **caster's house**. Every member, present and future, benefits.
- The yearly event reads those house modifiers and returns `bloodline` XP to any blood mage in the house. Dependency runs decision, then event, then house modifier, then yearly XP.
- Golems only touch the dynasty layer through `bm_house_golem`. The story roster and the character template both rely on that identifier.

## Gotchas

- A new bloodline modifier needs four changes: the modifier, an option in the choice event, a localization entry, and a clause in the yearly XP event. Missing the last one means it is never counted towards `bloodline` XP.
- Bloodline enhancements need the caster to have a house. Characters without one cannot receive them, and the yearly XP event also skips them.
- Golem membership is how the mod identifies golems. Don't give other characters this house, and don't remove golems from it.
- The fallback option has a TODO in the event about applying the buff to every house member.

## Not verified

- How the golem house and dynasty look in the game (name, prefix, coat of arms, dynasty view).
- Whether the house modifiers show correctly in the house UI and stack as intended for Legacy.
- AI behaviour when choosing the enhancement.
