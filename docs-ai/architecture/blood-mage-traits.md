# Blood Mage Traits

> Living document. Follow `AGENTS.md` in this folder: concepts only, no numbers. Update it when a trait or track is added, removed or changes meaning.

## Purpose

Two lifestyle traits carry the mod's progression. `lifestyle_blood_mage` marks a character as a blood mage and deepens through use. `lifestyle_crimson_empowerment` is a separate trait that grows from empowerment gained through blood magic. Both are lifestyle traits with XP tracks, so the character's mastery is visible and earned over time.

The idea: a blood mage is not a class chosen at a menu, it is a path. Blood magic is learned, taken or inherited, and then the character grows by spending lifeforce in a way that fits a theme (themselves, their family, others, victims, time). Using the magic is what advances it.

## Concepts

### Blood Mage (`lifestyle_blood_mage`)

- It is the identity trait. Acquisition always goes through the shared `bm_become_blood_mage_effect`, which adds the trait, makes sure the character has the Blood Magic story (see `blood-mage-story.md`) and marks the character as reviewed for the prevalence rule.
- It is hereditary and counts as a good trait. The game rules can limit AI characters from having it (the prevalence rule).
- It has five tracks. Each is a **school of mastery** with its own theme and its own way of gaining XP:

| Track | Theme | Grown by |
| --- | --- | --- |
| `ancient` | Defying time and piety | Passing time (yearly pulse, and the Ancient attunement) |
| `enlightenment` | Mastery of the self | Casting blood magic on yourself, and channelling lifeforce |
| `bloodline` | The dynasty | Enhancing your lineage, and house crimson modifiers each year |
| `benediction` | Giving life to others | Healing and empowering others |
| `hematurgy` | Taking from others | Draining lifeforce and harvesting traits |

- Every level gives a steady bonus that fits the school. Every track also adds a little vitality.
- **Milestones** reward the mage at the halfway point and at full mastery. Each is tied to the school's skill, and full mastery stops age from eroding prowess.

### Crimson Empowerment (`lifestyle_crimson_empowerment`)

- It is not inherited and hidden from the ruler designer. It represents power the mage has built up, and some self-cast blood magic requires experience in it.
- It is added by `bm_crimson_empowerment_event.001`, which is fired by the major self-cast blood magic. The player picks which track to advance. Tracks that are already full are not offered.
- It has seven tracks, each a theme of empowerment:

| Track | Theme |
| --- | --- |
| `charisma` | Presence and opinion |
| `fury` | Martial strength and control |
| `prosperity` | Wealth and development |
| `shadows` | Dread and secrecy |
| `insight` | Learning and development |
| `legacy` | Passing on strong traits |
| `expertise` | Faster growth in lifestyles |

## How one becomes a blood mage

All routes call `bm_become_blood_mage_effect`. They differ in fantasy:

- **Self-initiation.** Decisions for a character who follows the Quintessence faith, or who survives the internal ritual (a Learning duel that can scar the character).
- **Taught by a mage.** A blood mage grants blood magic to someone, who gains opinion of them. Non-mages can also ask a mage who is their friend, lover or soulmate.
- **Taken from a prisoner.** A non-mage can try to take blood magic from an imprisoned mage, at a terrible cost to the prisoner.
- **Conversion.** A witch can trade witchcraft for blood magic.
- **Birth and inheritance.** The trait is hereditary (see `blood-mage-trait-inheritance.md`). The prevalence game rules decide how often AI children get it, and whether AI characters keep it.
- **Scripted starts.** Character templates can give the trait.
- **AI.** The AI uses the ask and grant interactions. Their willingness is scaled by the prevalence rule.

## How the trait grows

Growth is **use-driven**, with a slow passive background:

1. **Passive (yearly).** A yearly pulse gives every blood mage a little XP in `ancient`. The Ancient attunement can add more, and house crimson modifiers can add `bloodline` XP. Crimson runes can also grant lifeforce each year.
2. **Active (spending lifeforce).** Casting blood magic needs Lifeforce (see `blood-mage-decisions.md`). Each cast removes the lifeforce modifier and adds XP to the track that matches the spell's school. Bigger casts give more XP. `add_xp_bm_dynamic` and the small `add_xp_*` helpers are the shared way to do this.
3. **Levels and milestones.** Track XP crosses level thresholds, which apply bonuses. Milestones add bonuses at the halfway point and full mastery.
4. **Gates.** Some actions read XP back, so deeper mastery unlocks stronger actions. That closes the loop between using magic and getting better at it.

Crimson Empowerment grows only through the major self-cast event: every cast lets the mage pick one empowerment track to advance.

## Where the details live

| Piece | File |
| --- | --- |
| Blood Mage trait | `common/traits/bm_blood_mage_trait.txt` |
| Crimson Empowerment trait | `common/traits/bm_crimson_empowerment_trait.txt` |
| XP helpers (`add_xp_bm_dynamic`, `add_crimson_empowerment_xp`) | `common/scripted_effects/bm_trait_track_xp_gain_effects.txt` |
| Acquisition effect | `common/scripted_effects/bm_blood_mage_lifecycle_effects.txt` |
| Per-school cast effects (XP per spell) | `common/scripted_effects/bm_blood_magic_used_effects.txt`, `bm_drain_trait_effects.txt` |
| Yearly passive XP and rune lifeforce | `events/bm_yearly_events.txt`, `common/on_action/bm_yearly_pulse.txt` |
| Crimson Empowerment choice event | `events/bm_crimson_empowerment_event.txt` |
| Birth and prevalence on-actions | `common/on_action/bm_blood_mage_prevalence_on_actions.txt` |
| Acquisition interactions and decisions | `common/character_interactions/bm_become_a_blood_mage.txt`, `bm_grant_blood_magic.txt`, `common/decisions/bm_become_blood_mage_decision.txt`, `bm_convert_from_witch.txt` |
| Names and track descriptions | `localization/english/bm_traits_l_english.yml` |

Per-level values, milestones, inheritance chances and XP thresholds are in those files.

## How the parts connect

- Decisions, interactions and yearly pulses add track XP, and XP-gated actions read it back (see `blood-mage-decisions.md`). That loop is the progression.
- Prevalence game rules and the acquisition effect control who can become a blood mage.
- Dynasty bloodline modifiers feed `bloodline` XP (see `blood-mage-dynasty.md`).
- The trait's presence drives the Blood Magic story, buildings, character templates and the Quintessence religion's virtues.

## Gotchas

- Each track needs localization for its name and description.
- Per-level bonuses are written out by hand per level, so changing a bonus means editing every level.
- Never add `lifestyle_blood_mage` with a bare `add_trait`. Use `bm_become_blood_mage_effect` so the story and prevalence flag are set.
- Several XP-gated actions check all five blood mage tracks. A new track must be added to those checks.

## Not verified

I read the trait definitions, the acquisition effect and the main XP sources in script. I did not read every level bonus or every XP-gated trigger. In-game behaviour (progression pace, event flow, AI uptake) is unconfirmed.
