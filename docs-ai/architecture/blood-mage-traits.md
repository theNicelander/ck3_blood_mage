# Blood Mage Traits

> Living document. Follow `AGENTS.md` in this folder: concepts only, no numbers. Update it when a trait or track is added, removed or changes meaning.

## Executive Summary

- **How to get it:** Acquired through `bm_become_blood_mage_effect` via self-initiation (faith decision or Learning ritual duel), teaching from a friend/lover/liege, siphoning an imprisoned mage, witch conversion, or hereditary birth.
- **What it does:** Marks the character as a blood mage. Grants base benefits (`+2` Learning per Piety level, `+10` Blood Mage opinion), unlocks the Blood Magic story panel, enables Lifeforce spellcasting, and progresses across 5 school tracks.
- **How to level it up:** Spending Lifeforce on blood magic grants XP in the spell's corresponding school (using `add_xp_bm_dynamic`). Slow passive growth comes from the yearly pulse (`ancient`), active house blood modifiers (`bloodline`), and yearly attunements.

### Master Cumulative Track Benefits (10 XP / 50 XP / 100 XP)

Each track has 10 progression levels (10 to 100 XP). In CK3, each tier unlocked applies additively.
*Note: In `lifestyle_blood_mage` and shared tracks, tiers 10–40 and 60–90 grant the standard Vitality Baseline (`+0.1` Health, `+2` Life Expectancy, `+1` Year Fertility, `+1` Epidemic Resistance). Tiers 50 and 100 grant capstones instead of the vitality step (4 vitality steps at 50 XP, 8 at 100 XP).*

#### 1. Blood Mage (`lifestyle_blood_mage`)
Base: `+2` Learning per Piety level, `+10` Same Trait Opinion.

| Track | 10 XP | 50 XP | 100 XP |
| --- | --- | --- | --- |
| `ancient` | • `+0.1` Health<br>• `+2` Life Expectancy<br>• `+1` Year Fertility<br>• `+1` Epidemic Resistance<br>• `+0.1` Monthly Dynasty Prestige<br>• `+5%` Lifestyle XP Gain Mult | • `+0.4` Health<br>• `+8` Life Expectancy<br>• `+4` Years Fertility<br>• `+4` Epidemic Resistance<br>• `+0.5` Monthly Dynasty Prestige<br>• `+25%` Lifestyle XP Gain Mult<br>• `+0.25` Negate Health Penalty<br>• `+1` Prowess per Piety level | • `+0.8` Health<br>• `+16` Life Expectancy<br>• `+8` Years Fertility<br>• `+8` Epidemic Resistance<br>• `+1.0` Monthly Dynasty Prestige<br>• `+50%` Lifestyle XP Gain Mult<br>• `+0.5` Negate Health Penalty<br>• `+1` Prowess per Piety level<br>• Full age prowess lock (`no_prowess_loss_from_age = yes`) |
| `enlightenment` | • `+0.1` Health<br>• `+2` Life Expectancy<br>• `+1` Year Fertility<br>• `+1` Epidemic Resistance<br>• `+0.2` Monthly Piety<br>• `+5%` Monthly Piety Gain Mult | • `+0.4` Health<br>• `+8` Life Expectancy<br>• `+4` Years Fertility<br>• `+4` Epidemic Resistance<br>• `+0.8` Monthly Piety<br>• `+20%` Monthly Piety Gain Mult<br>• `+1` Max Personal Schemes<br>• `+1` Learning per Piety level<br>• `+1` Prowess per Piety level | • `+0.8` Health<br>• `+16` Life Expectancy<br>• `+8` Years Fertility<br>• `+8` Epidemic Resistance<br>• `+1.8` Monthly Piety<br>• `+45%` Monthly Piety Gain Mult<br>• `+1` Max Personal Schemes<br>• `+2` Learning per Piety level<br>• `+1` Prowess per Piety level<br>• Full age prowess lock (`no_prowess_loss_from_age = yes`) |
| `bloodline` | • `+0.1` Health<br>• `+2` Life Expectancy<br>• `+1` Year Fertility<br>• `+1` Epidemic Resistance<br>• `+0.2` Monthly Dynasty Prestige<br>• `-2%` Build Gold Cost<br>• `+2%` Domain Tax | • `+0.4` Health<br>• `+8` Life Expectancy<br>• `+4` Years Fertility<br>• `+4` Epidemic Resistance<br>• `+1.0` Monthly Dynasty Prestige<br>• `+1` Domain Limit<br>• `+10%` Gold Gain Mult<br>• `+1` Stewardship per Piety level<br>• `+1` Prowess per Piety level<br>• `+5` Vassal Limit<br>• `-8%` Build Gold Cost<br>• `+8%` Domain Tax<br>• `+10%` Development Growth Factor<br>• `-5%` Holding Build Speed | • `+0.8` Health<br>• `+16` Life Expectancy<br>• `+8` Years Fertility<br>• `+8` Epidemic Resistance<br>• `+2.0` Monthly Dynasty Prestige<br>• `+3` Domain Limit<br>• `+30%` Gold Gain Mult<br>• `+2` Stewardship per Piety level<br>• `+1` Prowess per Piety level<br>• `+15` Vassal Limit<br>• `-20%` Build Gold Cost<br>• `+20%` Domain Tax<br>• `+25%` Development Growth Factor<br>• `-15%` Holding Build Speed<br>• Full age prowess lock (`no_prowess_loss_from_age = yes`) |
| `benediction` | • `+0.1` Health<br>• `+2` Life Expectancy<br>• `+1` Year Fertility<br>• `+1` Epidemic Resistance<br>• `+1.5` General Opinion<br>• `+1.0` Vassal Opinion<br>• `+0.2` Monthly Prestige<br>• `+5%` Monthly Prestige Gain Mult | • `+0.4` Health<br>• `+8` Life Expectancy<br>• `+4` Years Fertility<br>• `+4` Epidemic Resistance<br>• `+7.5` General Opinion<br>• `+5.0` Vassal Opinion<br>• `+1.0` Monthly Prestige<br>• `+25%` Monthly Prestige Gain Mult<br>• `+1` Diplomacy per Piety level<br>• `+1` Prowess per Piety level | • `+0.8` Health<br>• `+16` Life Expectancy<br>• `+8` Years Fertility<br>• `+8` Epidemic Resistance<br>• `+15.0` General Opinion<br>• `+10.0` Vassal Opinion<br>• `+2.0` Monthly Prestige<br>• `+50%` Monthly Prestige Gain Mult<br>• `+2` Diplomacy per Piety level<br>• `+1` Prowess per Piety level<br>• Full age prowess lock (`no_prowess_loss_from_age = yes`) |
| `hematurgy` | • `+0.1` Health<br>• `+2` Life Expectancy<br>• `+1` Year Fertility<br>• `+1` Epidemic Resistance<br>• `+3` Hostile Scheme Success<br>• `+3` Scheme Secrecy<br>• `+2` Dread Baseline (`dread_baseline_add`)<br>• `-2%` Tyranny Gain Mult | • `+0.4` Health<br>• `+8` Life Expectancy<br>• `+4` Years Fertility<br>• `+4` Epidemic Resistance<br>• `+15` Hostile Scheme Success<br>• `+15` Scheme Secrecy<br>• `+1` Max Hostile Schemes<br>• `-10` Days Scheme Phase Duration<br>• `+10` Dread Baseline (`dread_baseline_add`)<br>• `+15%` Dread Gain Mult<br>• `-10%` Tyranny Gain Mult<br>• `+1` Intrigue per Piety level<br>• `+1` Prowess per Piety level | • `+0.8` Health<br>• `+16` Life Expectancy<br>• `+8` Years Fertility<br>• `+8` Epidemic Resistance<br>• `+30` Hostile Scheme Success<br>• `+30` Scheme Secrecy<br>• `+2` Max Hostile Schemes<br>• `-20` Days Scheme Phase Duration<br>• `+20` Dread Baseline (`dread_baseline_add`)<br>• `+25%` Dread Gain Mult<br>• `-20%` Tyranny Gain Mult<br>• `+2` Intrigue per Piety level<br>• `+1` Prowess per Piety level<br>• Full age prowess lock (`no_prowess_loss_from_age = yes`) |

#### 2. Blood Knight (`lifestyle_blood_knight`)
Base: `-1.0` Health, `-5` Life Expectancy, `-5` Prowess. `vanguard` and `slaughter` gain vitality at all 10 tiers; `ancient`, `benediction`, `enlightenment` share Mage vitality profile (skip 50 & 100 for capstones).

| Track | 10 XP | 50 XP | 100 XP |
| --- | --- | --- | --- |
| `vanguard` | • `+0.1` Health, `+2` Life Exp, `+1` Fert, `+1` Epidemic<br>• `+0.1` Prestige, `+1` Advantage<br>• `+2%` Army Speed, `+3%` Pursuit Mult | • `+0.5` Health, `+10` Life Exp, `+5` Fert, `+5` Epidemic<br>• `+0.5` Prestige, `+5` Advantage, `+2` Martial<br>• `+10%` Army Speed, `+15%` Pursuit Mult<br>• `+1` Martial per Prestige level | • `+1.0` Health, `+20` Life Exp, `+10` Fert, `+10` Epidemic<br>• `+1.0` Prestige, `+10` Advantage, `+5` Martial<br>• `+20%` Army Speed, `+30%` Pursuit Mult<br>• `+2` Martial per Prestige level |
| `slaughter` | • `+0.1` Health, `+2` Life Exp, `+1` Fert, `+1` Epidemic<br>• `+0.1` Prestige, `+2` Prowess<br>• `+10%` Knight Effectiveness, `+5%` Dread Mult | • `+0.5` Health, `+10` Life Exp, `+5` Fert, `+5` Epidemic<br>• `+0.5` Prestige, `+10` Prowess<br>• `+50%` Knight Effectiveness, `+25%` Dread Mult<br>• `+1` Prowess per Prestige level | • `+1.0` Health, `+20` Life Exp, `+10` Fert, `+10` Epidemic<br>• `+1.0` Prestige, `+20` Prowess<br>• `+100%` Knight Effectiveness, `+50%` Dread Mult<br>• `+2` Prowess per Prestige level |

#### 3. Blood Empowerment (`lifestyle_blood_empowerment`)
Base: None. All 5 tracks gain full Vitality Baseline across all 10 tiers (`+0.5` at 50 XP, `+1.0` at 100 XP).

| Track | 10 XP | 50 XP | 100 XP |
| --- | --- | --- | --- |
| `dynasty` | Vitality + `+4%` Fertility, `+2.5%` Congenital/Genetic Chance, `+2.5%` Inactive Trait Inheritance | Vitality + `+20%` Fertility, `+12.5%` Congenital/Genetic Chance, `+12.5%` Inactive Trait Inheritance | Vitality + `+40%` Fertility, `+25%` Congenital/Genetic Chance, `+25%` Inactive Trait Inheritance |
| `mastery` | Vitality + `+4%` Lifestyle XP Mult, `-10`d Learn Language Phase, `+3%` Personal Scheme Success | Vitality + `+20%` Lifestyle XP Mult, `-50`d Learn Language Phase, `+15%` Personal Scheme Success, `+1` Learn Language Slot (30 XP) | Vitality + `+40%` Lifestyle XP Mult, `-100`d Learn Language Phase, `+30%` Personal Scheme Success, `+4` Learn Language Slots (30, 60, 90, 100 XP) |
| `presence` | Vitality + `+1.5` General Opinion, `+1.0` Vassal Opinion, `+5%` Stress Loss Mult | Vitality + `+7.5` General Opinion, `+5.0` Vassal Opinion, `+25%` Stress Loss Mult | Vitality + `+15.0` General Opinion, `+10.0` Vassal Opinion, `+50%` Stress Loss Mult |
| `prosperity` | Vitality + `+0.1` Income, `+2.5%` Income Mult | Vitality + `+0.5` Income, `+12.5%` Income Mult | Vitality + `+1.0` Income, `+25%` Income Mult |
| `shadows` | Vitality + `+5` Scheme Secrecy, `-3%` Enemy Hostile Scheme Success | Vitality + `+25` Scheme Secrecy, `-15%` Enemy Hostile Scheme Success | Vitality + `+50` Scheme Secrecy, `-30%` Enemy Hostile Scheme Success |

*Prowess age lock = `no_prowess_loss_from_age = yes` (full immunity to prowess deterioration from aging).*

## Purpose

Identity and progression trait `lifestyle_blood_mage`. Gates spellcasting, story panel, and 5 school tracks. Secondary trait `lifestyle_blood_empowerment` covered in [blood-mage-blood-empowerment.md](blood-mage-blood-empowerment.md).

## Concepts

### Blood Mage (`lifestyle_blood_mage`)
- **Type:** Lifestyle trait. Mutually exclusive with `lifestyle_blood_knight` via decisions and interactions (script-gated; opposites block omitted to permit dual-wielding on legendary figures like Egill). A blood mage cannot become a blood knight. Inheritable (25% single parent, 100% both parents; 0.2% birth / random creation). Subject to prevalence game rule.
- **Icon:** `bm_blood_mage.dds` (`gfx/interface/icons/traits/bm_blood_mage.dds`).
- **Base Stats:** `+2` Learning per Piety level, `+10` Blood Mage opinion.
- **Entry Effect:** Added via `bm_become_blood_mage_effect` or `bm_elevate_blood_knight_to_blood_mage_effect` (which transfers all accrued `ancient`, `benediction`, and `enlightenment` track XP 1:1, and converts 50% of `vanguard` and `slaughter` into `bloodline` and `hematurgy`).
- **Tracks:** 5 schools (`ancient`, `enlightenment`, `bloodline`, `benediction`, `hematurgy`). Max 100 XP each. `ancient`, `benediction`, and `enlightenment` tracks are shared identically with `lifestyle_blood_knight`.
- **Stat Parity:** Every 10 XP tier in any track scales identical baseline vitality stats (`+0.1` Health, `+2` Life Expectancy, `+1` Year Fertility, `+1` Epidemic Resistance).
- **Track Icons (`gfx/interface/icons/trait_level_tracks/`):**
  - `ancient.dds`: Fiery Blood Drop (shared; copied from `bm_interactions.dds`).
  - `benediction.dds`: Lifestyle Physician (caduceus healing staff; shared).
  - `enlightenment.dds`: Venerated Ancestor / Saint (shared).
  - `bloodline.dds`: Augustus (laurel-crowned dynastic triumph; Mage exclusive).
  - `hematurgy.dds`: Murderer (Mage exclusive).
  - `vanguard.dds`: Warrior of the Faith (Knight exclusive).
  - `slaughter.dds`: Raider / Reaver (blood-dripping axe; Knight exclusive).

### Acquisition Triggers
All routes call `bm_become_blood_mage_effect` or `bm_elevate_blood_knight_to_blood_mage_effect`:
- `bm_elevate_to_blood_mage_decision`: Blood Knights can take a dedicated ritual decision to elevate themselves and become a Blood Mage, carrying over their `ancient`, `benediction`, and `enlightenment` track progress 1:1 and converting 50% of martial XP (`vanguard` -> `bloodline`, `slaughter` -> `hematurgy`) into Blood Mage schools.
- `bm_blood_cultist_become_blood_mage_decision`: Decision for Blóðtrú faithful; initiation duel against Egill Skallagrímsson (`bm_geyser_duel.0001`) in Reykjavik or Tsushima.
- `bm_enhance_blood_ritual_decision`: Decision for non-faithful; initiation duel against Egill Skallagrímsson (`bm_geyser_duel.0001`) in Reykjavik or Tsushima.
- `grant_blood_magic_interaction`: Mage grants trait to unlanded courtier (costs lifeforce; awards Bloodline XP).
- `ask_for_blood_magic_interaction`: Non-mage asks friend/lover/soulmate mage to teach them.
- `bm_get_blood_magic_from_prisoner_interaction`: Character harvests trait from imprisoned blood mage.
- `convert_to_blood_magic_from_witch`: Witch swaps witch trait/secret for blood magic.
- Birth inheritance: Rolled on newborn children of blood mages via `on_birth_child`.

### How Tracks Level Up
- **Active Spells & Interactions:** Consuming Lifeforce adds XP to the spell's corresponding school via `add_xp_bm_dynamic`.
- **Ancient:** Yearly pulse, Ancient attunement, Inscribing blood runes (Major/Superior), and Condense lifeforce.
- **Bloodline:** Bestowing blood magic, welcoming newborn children (`bm_on_birth_bloodline_xp`), blessing kin, communing with the bloodline, manifesting congenital traits, and active house modifiers.
- **Benediction:** Curing ailments across 37 afflictions (`bm_heal_ailment`), empowering and creating blood knights, and restoring drained victims.
- **Hematurgy:** Draining prisoners and courtiers, casting remote blood curses (`bm_curse_blood_interaction`), and harvesting congenital traits. (Battlefield kills do not grant lifeforce to blood mages).
- **Enlightenment:** Manifesting lifeforce decisions (Learning duel), educational enhancement duels, lifeforce channeling, and blood empowerment.

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

- **Vitality Step Discrepancy:** Blood Mage and Blood Knight shared tracks (`ancient`, `benediction`, `enlightenment`) omit the vitality baseline at tiers 50 and 100 to budget for scaling capstones (`+1` stat per piety level, age prowess lock, negate health penalty). Blood Empowerment and martial BK tracks retain vitality at every tier.
- **Ancient Somatic Resilience:** `ancient` grants `negate_health_penalty = 0.25` at 50 XP and `0.5` at 100 XP, alongside prowess age lock (`no_prowess_loss_from_age = yes`) at 100 XP and `prowess_per_piety_level = 1`.
- **Mastery Scheme Slots:** `max_learn_language_schemes_add` triggers strictly at 30, 60, 90, and 100 XP (`+1` slot at 50 XP, `+4` slots at 100 XP).
- **Additive Compounding Across Traits:** Holding both `lifestyle_blood_mage` (or `lifestyle_blood_knight`) and `lifestyle_blood_empowerment` stacks all unlocked track benefits additively across both traits.
- **Each track needs localization** for its name and description.
- **Per-level bonuses are written out by hand per level**, so changing a bonus means editing every level.
- **Never add `lifestyle_blood_mage` with a bare `add_trait`.** Use `bm_become_blood_mage_effect` so the story and prevalence flag are set.
- **Several XP-gated actions check all five blood mage tracks.** A new track must be added to those checks.

## Not verified

I read the trait definitions, the acquisition effect and the main XP sources in script. I did not read every level bonus or every XP-gated trigger. In-game behaviour (progression pace, event flow, AI uptake) is unconfirmed.
