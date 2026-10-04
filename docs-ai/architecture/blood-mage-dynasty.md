# Blood Mage Dynasty

> Living document. Follow `AGENTS.md` in this folder: concepts only, no numbers. Update it when a house, dynasty or bloodline modifier is added, removed or changes meaning.

## Purpose

The mod uses dynasties and houses in two separate ways:

1. **Bloodline.** A blood mage can channel Lifeforce into their own house, giving the whole house a lasting enhancement. This is the fantasy behind the `bloodline` track of `lifestyle_blood_mage`: the mage's power is passed to their lineage.
2. **The Golem house.** Blood golems are created characters that all belong to one dedicated house, so the mod can recognise them.
3. **Dynasty Mages Roster.** The Blood Magic panel tracks all living members of the mage's dynasty who possess the blood mage trait.

The features do not depend on each other. They share only the dynasty and house scopes.

## Concepts

### Bloodline enhancement

- Channel Lifeforce into your bloodline is a decision for blood mages. It opens an event where the player picks which enhancement the house receives.
- Each enhancement is a **house modifier** with a theme. Their names follow `dynasty_crimson_<theme>_modifier`:

| Modifier | Theme |
| --- | --- |
| `dynasty_crimson_charisma_modifier` | Diplomacy, opinion, prestige |
| `dynasty_crimson_fury_modifier` | Martial strength, prowess, knights |
| `dynasty_crimson_prosperity_modifier` | Stewardship, control, taxes, development |
| `dynasty_crimson_shadows_modifier` | Intrigue, stronger own schemes, weaker enemy schemes |
| `dynasty_crimson_insight_modifier` | Learning, piety, development, epidemic resistance |
| `dynasty_crimson_legacy_modifier` | Health, fertility and better inheritance of traits |
| `dynasty_crimson_expertise_modifier` | Faster lifestyle XP and less stress |

- Each modifier can only be taken once per house, except Legacy, which stacks. A house that already has every other modifier falls back to a temporary house-wide buff and a chance of permanent skill gains for the caster (`temporary_buff_bloodline`).
- The AI chooses between the available options with equal preference.
- The house modifiers also **feed back** into the mage. A yearly hidden event gives the `bloodline` track XP, with a better chance for each bloodline modifier the house holds. The more the house has been enhanced, the faster the mage's bloodline mastery grows.
- Levels in the blood mage trait also grant monthly dynasty prestige. See [blood-mage-traits.md](blood-mage-traits.md).

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
