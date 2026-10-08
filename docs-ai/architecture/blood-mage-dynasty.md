# Blood Mage Dynasty

> Living document. Follow `AGENTS.md` in this folder: concepts only, no numbers. Update it when a house, dynasty or bloodline modifier is added, removed or changes meaning.

## Executive Summary

- **How to get it:** Blood mages take the `channel_lifeforce_bloodline` decision, triggering event `bm_channel_lifeforce_bloodline.001` to select a permanent house modifier.
- **What it does:** Applies powerful supernatural house modifiers that permanently benefit all living and future members of the ruler's noble house.
- **How it levels up the mage:** The decision grants **1 `bloodline` XP** directly. In addition, each crimson modifier on the house increases the yearly chance for blood mages in that house to gain bonus `bloodline` XP via `blood_mage_yearly_events.002`.

### Simplified House Modifiers Table

Each modifier can be chosen once per house, except `Legacy`, which stacks infinitely:

| Modifier | Theme | House Member Benefits |
| --- | --- | --- |
| `dynasty_crimson_charisma_modifier` | Diplomacy & Majesty | `+2` Diplomacy, `+5` General Opinion, `+0.1` Monthly Prestige |
| `dynasty_crimson_fury_modifier` | Martial & Lethality | `+2` Martial, `+3` Prowess, `+15%` Knight Effectiveness, `+1` Knight Limit |
| `dynasty_crimson_prosperity_modifier` | Stewardship & Realm Wealth | `+2` Stewardship, `+0.1` County Control Growth, `+5%` Domain Tax, `+5%` Development Growth |
| `dynasty_crimson_shadows_modifier` | Intrigue & Schemes | `+2` Intrigue, `+5%` Hostile Scheme Success, faster friendly schemes, disrupted enemy schemes |
| `dynasty_crimson_insight_modifier` | Learning & Devotion | `+2` Learning, `+0.15` Monthly Piety, `+0.05` Capital Development Growth, `+2` Epidemic Resistance |
| `dynasty_crimson_legacy_modifier` *(stacks)* | Eugenics & Longevity | `+0.3` Health, `+10%` Fertility, `+10%` Positive Genetic Chance/Strengthen, `-10%` Negative/Inbreeding Chance |
| `dynasty_crimson_expertise_modifier` | Mastery & Mental Fortitude | `+5%` Lifestyle XP Mult, `+5%` Learning Lifestyle XP, `+5%` Stress Loss, `-5%` Stress Gain |
| *Fallback (`temporary_buff_bloodline`)* | All Modifiers Taken | House buff giving `+1` all skills, `+2` Prowess |

## Purpose

The mod uses dynasties and houses in two separate ways:

1. **Bloodline.** A blood mage can channel Lifeforce into their own house, giving the whole house a lasting enhancement. This is the fantasy behind the `bloodline` track of `lifestyle_blood_mage`: the mage's power is passed to their lineage.
2. **The Golem house.** Blood golems are created characters that all belong to one dedicated house (`bm_house_golem`), allowing the mod to recognise and roster them.
3. **Dynasty Mages Roster.** The Blood Magic panel tracks all living members of the mage's dynasty who possess the blood mage trait.

## Concepts

### Bloodline Enhancement
- Channeled via `channel_lifeforce_bloodline`, opening `bm_channel_lifeforce_bloodline.001` where the mage selects an enhancement.
- Each modifier permanently applies to the caster's noble house.
- All non-legacy modifiers are unique per house; `Legacy` can be chosen repeatedly to stack congenital trait chances.
- Feeding back into progression: each modifier on the house accelerates the yearly chance of receiving passive `bloodline` XP.
- Levels in the Blood Mage trait itself also grant monthly dynasty prestige to support dynastic renown.

### The Golem house

- `bm_house_golem` is a house in the dynasty `dynn_bm_golem`. It has its own name, motto, prefix and coat of arms.
- The blood golem character template places new golems in this house.
- The Blood Magic panel recognises golems by house membership when it rebuilds the list of the mage's owned golems from their courtiers. Moving a golem out of the house removes it from the roster.

## Where the details live

| Concept | File |
| --- | --- |
| Golem house | `common/dynasty_houses/bm_dynasty_houses.txt` |
| Golem dynasty | `common/dynasties/bm_dynasties.txt` |
| Golem house coat of arms | `common/coat_of_arms/coat_of_arms/bm_coat_of_arms.txt` |
| Bloodline house modifiers | `common/modifiers/bm_channel_dynasty_modifiers.txt` |
| Fallback buff | `temporary_buff_bloodline` in `common/modifiers/bm_modifiers.txt` |
| Channel decision | `channel_lifeforce_bloodline` in `common/decisions/bm_channel_lifeforce.txt` |
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
