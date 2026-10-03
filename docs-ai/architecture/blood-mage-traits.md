# Blood Mage Traits

> Living document. Follow `AGENTS.md` in this folder: concepts only, no numbers. Update it when a trait or track is added, removed or changes meaning.

## Purpose

Two lifestyle traits carry the mod's progression. `lifestyle_blood_mage` marks a character as a blood mage and deepens through use. `lifestyle_crimson_empowerment` is a separate trait that grows from empowerment gained through blood magic. Both are lifestyle traits with XP tracks, so the character's mastery is visible and earned over time.

## Concepts

### Blood Mage (`lifestyle_blood_mage`)

- It is the identity trait. Acquisition always goes through the shared `bm_become_blood_mage_effect`.
- It is hereditary and counts as a good trait. The game rules can limit AI characters from having it (the prevalence rule).
- It has five tracks. Each is a **school of mastery** with its own theme and its own way of gaining XP:

| Track | Theme | Grown by |
| --- | --- | --- |
| `ancient` | Defying time and piety | Passing time |
| `enlightenment` | Mastery of the self | Casting blood magic on yourself |
| `bloodline` | The dynasty | Enhancing your lineage |
| `benediction` | Giving life to others | Healing and empowering others |
| `hematurgy` | Taking from others | Draining lifeforce and harvesting traits |

- Every level gives a steady bonus that fits the school. Every track also adds a little vitality.
- **Milestones** reward the mage at the halfway point and at full mastery. Each is tied to the school's skill, and full mastery stops age from eroding prowess.

### Crimson Empowerment (`lifestyle_crimson_empowerment`)

- It is not inherited and hidden from the ruler designer. It represents power the mage has built up, and some self-cast blood magic requires experience in it.
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

## Where the details live

| Piece | File |
| --- | --- |
| Blood Mage trait | `common/traits/bm_blood_mage_trait.txt` |
| Crimson Empowerment trait | `common/traits/bm_crimson_empowerment_trait.txt` |
| XP helper (`add_xp_bm_dynamic`) | `common/scripted_effects/bm_trait_track_xp_gain_effects.txt` |
| Names and track descriptions | `localization/english/bm_traits_l_english.yml` |

Per-level values, milestones, inheritance chances and XP thresholds are in those files.

## How the parts connect

- Decisions, interactions and yearly pulses add track XP, and XP-gated actions read it back (see `blood-mage-decisions.md`). That loop is the progression.
- Prevalence game rules and the acquisition effect control who can become a blood mage.

## Gotchas

- Each track needs localization for its name and description.
- Per-level bonuses are written out by hand per level, so changing a bonus means editing every level.
- Several XP-gated actions check all five blood mage tracks. A new track must be added to those checks.

## Not verified

I read the trait definitions and the English loc. I didn't trace every XP source in script. The "grown by" column is from the track descriptions.
