# Blood Mage Traits

> Living document. Follow `AGENTS.md` in this folder: concepts only, no numbers. Update it when a trait or track is added, removed or changes meaning.

## Executive Summary

- **How to get it:** Acquired through `bm_become_blood_mage_effect` via self-initiation (faith decision or Learning ritual duel), teaching from a friend/lover/liege, siphoning an imprisoned mage, witch conversion, or hereditary birth.
- **What it does:** Marks the character as a blood mage. Grants base benefits (`+2` Learning per Piety level, `+10` Blood Mage opinion), unlocks the Blood Magic story panel, enables Lifeforce spellcasting, and progresses across 5 school tracks.
- **How to level it up:** Spending Lifeforce on blood magic grants XP in the spell's corresponding school (using `add_xp_bm_dynamic`). Slow passive growth comes from the yearly pulse (`ancient`), active house blood modifiers (`bloodline`), and yearly attunements.

### Simplified Track Benefits Table

Each track has 10 progression levels (10 to 100 XP). Every standard level (10–40 and 60–90) grants the same **Vitality Baseline** (`+0.1` Health, `+2` Life Expectancy, `+1` Year Fertility, `+1` Epidemic Resistance) alongside school bonuses. Milestones reward mastery at level 50 and 100:

| Track | School Theme | Standard Step Bonus (10–40, 60–90) | Level 50 Milestone | Level 100 Milestone | Grown By |
| --- | --- | --- | --- | --- | --- |
| `ancient` | Time & Piety | Vitality + `+0.2` Monthly Piety, `+5%` Piety Gain Mult | `+1` Learning & Prowess per Piety level | `+1` Learning per Piety level, Prowess age lock | Yearly pulse, Ancient attunement, Blood runes, Manifest lifeforce decisions |
| `enlightenment` | Self-Mastery | Vitality + `+5%` Lifestyle XP Gain Mult | `+1` Martial & Prowess per Piety level | `+1` Martial per Piety level, Prowess age lock | Education duels, Channeling lifeforce, Blood empowerment |
| `bloodline` | Dynastic Lineage | Vitality + `+0.1` Monthly Dynasty Prestige | `+1` Stewardship & Prowess per Piety level | `+1` Stewardship per Piety level, Prowess age lock | Granting blood magic, Childbirth, Bless kin, Commune rite, Congenital manifestation, House modifiers, Golems |
| `benediction` | Healing & Bestowal | Vitality + `+1.5` General Opinion, `+1.0` Vassal Opinion, `+0.2` Prestige, `+5%` Prestige Mult | `+1` Diplomacy & Prowess per Piety level | `+1` Diplomacy per Piety level, Prowess age lock | Curing ailments, Making & empowering blood knights, Restoring courtiers |
| `hematurgy` | Siphoning Vitality | Vitality + `-5` Enemy Hostile Scheme Success Chance | `+1` Intrigue & Prowess per Piety level | `+1` Intrigue per Piety level, Prowess age lock | Draining lifeforce from prisoners/courtiers, Congenital trait theft |

*Prowess age lock = `no_prowess_loss_from_age = yes` (full immunity to prowess deterioration from aging).*

## Purpose

Identity and progression trait `lifestyle_blood_mage`. Gates spellcasting, story panel, and 5 school tracks. Secondary trait `lifestyle_blood_empowerment` covered in [blood-mage-blood-empowerment.md](blood-mage-blood-empowerment.md).

## Concepts

### Blood Mage (`lifestyle_blood_mage`)
- **Type:** Lifestyle trait. Mutually exclusive with `lifestyle_blood_knight` (`opposites = { lifestyle_blood_knight }`). A blood mage cannot become a blood knight. Inheritable (25% single parent, 100% both parents; 0.2% birth / random creation). Subject to prevalence game rule.
- **Base Stats:** `+2` Learning per Piety level, `+10` Blood Mage opinion.
- **Entry Effect:** Added via `bm_become_blood_mage_effect` or `bm_elevate_blood_knight_to_blood_mage_effect` (which transfers all accrued `ancient` and `benediction` track XP 1:1, and converts 50% of `slaughter`, `vanguard`, and `resilience` into `hematurgy`, `bloodline`, and `enlightenment`).
- **Tracks:** 5 schools (`ancient`, `enlightenment`, `bloodline`, `benediction`, `hematurgy`). Max 100 XP each. `ancient` and `benediction` tracks are identical to the tracks on `lifestyle_blood_knight`.
- **Stat Parity:** Every 10 XP tier in any track scales identical baseline vitality stats (`+0.1` Health, `+2` Life Expectancy, `+1` Year Fertility, `+1` Epidemic Resistance).

### Acquisition Triggers
All routes call `bm_become_blood_mage_effect` or `bm_elevate_blood_knight_to_blood_mage_effect`:
- `bm_elevate_to_blood_mage_decision`: Blood Knights can take a dedicated ritual decision to elevate themselves and become a Blood Mage, carrying over their `ancient` and `benediction` track progress 1:1 and converting 50% of martial XP into Blood Mage schools.
- `bm_blood_cultist_become_blood_mage_decision`: Decision for Blóðtrú faithful; initiation duel against Egill Skallagrímsson (`bm_geyser_duel.0001`) in Reykjavik or Tsushima.
- `bm_enhance_blood_ritual_decision`: Decision for non-faithful; initiation duel against Egill Skallagrímsson (`bm_geyser_duel.0001`) in Reykjavik or Tsushima.
- `grant_blood_magic_interaction`: Mage grants trait to unlanded courtier (costs lifeforce; awards Bloodline XP).
- `ask_for_blood_magic_interaction`: Non-mage asks friend/lover/soulmate mage to teach them.
- `bm_get_blood_magic_from_prisoner_interaction`: Character harvests trait from imprisoned blood mage.
- `convert_to_blood_magic_from_witch`: Witch swaps witch trait/secret for blood magic.
- Birth inheritance: Rolled on newborn children of blood mages via `on_birth_child`.

### How Tracks Level Up
- **Active Spells & Interactions:** Consuming Lifeforce adds XP to the spell's corresponding school via `add_xp_bm_dynamic`.
- **Ancient:** Yearly pulse, Ancient attunement, Inscribing blood runes (Major/Superior), Condense lifeforce, and Manifesting Lifeforce decisions.
- **Bloodline:** Bestowing blood magic, welcoming newborn children (`bm_on_birth_bloodline_xp`), blessing kin, communing with the bloodline, manifesting congenital traits, and active house modifiers.
- **Benediction:** Curing ailments across 37 afflictions (`bm_heal_ailment`), empowering and creating blood knights, and restoring drained victims.
- **Hematurgy:** Draining prisoners and courtiers, and harvesting congenital traits. (Battlefield kills do not grant lifeforce to blood mages).
- **Enlightenment:** Educational enhancement duels, lifeforce channeling, and blood empowerment.

## Where the details live

| Piece | File |
| --- | --- |
| Blood Mage trait | `common/traits/bm_blood_mage_trait.txt` |
| Blood Empowerment trait | `common/traits/bm_blood_empowerment_trait.txt` |
| XP helpers (`add_xp_bm_dynamic`, `add_blood_empowerment_xp`) | `common/scripted_effects/bm_trait_track_xp_gain_effects.txt` |
| Acquisition effect | `common/scripted_effects/bm_blood_mage_lifecycle_effects.txt` |
| Per-school cast effects (XP per spell) | `common/scripted_effects/bm_blood_magic_used_effects.txt`, `bm_drain_trait_effects.txt` |
| Congenital trait manifestation (effects & events) | `common/scripted_effects/bm_manifest_traits_effects.txt`, `events/bm_channel_manifest_traits_events.txt` |
| Yearly passive XP and rune lifeforce | `events/bm_yearly_events.txt`, `common/on_action/bm_yearly_pulse.txt` |
| Blood Empowerment choice event | `events/bm_blood_empowerment_event.txt` |
| Birth and prevalence on-actions | `common/on_action/bm_blood_mage_prevalence_on_actions.txt` |
| Acquisition interactions and decisions | `common/character_interactions/bm_become_a_blood_mage.txt`<br>`common/character_interactions/bm_grant_blood_magic.txt`<br>`common/decisions/become_mage/bm_become_blood_mage_decision.txt`<br>`common/decisions/become_mage/bm_convert_from_witch.txt`<br>`common/decisions/become_mage/bm_elevate_blood_knight_decision.txt` |
| Names and track descriptions | `localization/english/bm_traits_l_english.yml` |

Per-level values, milestones, inheritance chances and XP thresholds are in those files.

## How the parts connect

- Decisions, interactions and yearly pulses add track XP, and XP-gated actions read it back (see `blood-mage-decisions.md`). That loop is the progression.
- Prevalence game rules and the acquisition effect control who can become a blood mage.
- Dynasty bloodline modifiers feed `bloodline` XP (see `blood-mage-dynasty.md`).
- The trait's presence drives the Blood Magic story, buildings, character templates and the Blóðtrú religion's virtues.

## Gotchas

- Each track needs localization for its name and description.
- Per-level bonuses are written out by hand per level, so changing a bonus means editing every level.
- Never add `lifestyle_blood_mage` with a bare `add_trait`. Use `bm_become_blood_mage_effect` so the story and prevalence flag are set.
- Several XP-gated actions check all five blood mage tracks. A new track must be added to those checks.

## Not verified

I read the trait definitions, the acquisition effect and the main XP sources in script. I did not read every level bonus or every XP-gated trigger. In-game behaviour (progression pace, event flow, AI uptake) is unconfirmed.
