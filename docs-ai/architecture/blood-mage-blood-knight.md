# Blood Mage: Blood Knight

Living technical specification for the Blood Knight subsystem.

## Executive Summary

- **What:** Evolving martial combat lifestyle trait `lifestyle_blood_knight` functioning as a stepping stone toward Blood Mage. Features 5 tracks: 3 martial tracks (`vanguard`, `slaughter`, `resilience`) and 2 tracks shared with Blood Mage (`ancient`, `benediction`), max 100 XP each.
- **Base stats:** `health = -1`, `life_expectancy = -5`, `prowess = -5`. Ruler designer cost: 50. Non-inheritable (`genetic = no`). Mutually exclusive with `lifestyle_blood_mage` (`opposites = { lifestyle_blood_mage }`).
- **How to acquire:**
  - `make_blood_knight_interaction`: Cast by a Blood Mage on a sworn knight/courtier (cannot target self; a Blood Mage cannot become a Blood Knight). Cost: `blood_knight_creation_piety_cost` (100 Piety) + `lifeforce_modifier_major`.
  - **Geyser Duel Initiation (`bm_geyser_duel.0001`):** Travel to Reykjavik or Tsushima and confront Egill Skallagrímsson via `bm_blood_cultist_become_blood_mage_decision` or `bm_enhance_blood_ritual_decision` (requires Piety or Prestige level >= 2 to open decision). Choosing the Prowess duel requires Prestige level >= 2, costs 1 Fame level (`add_prestige_level = -1`), requires not being a Blood Mage, and bestows `lifestyle_blood_knight` upon victory.
- **Elevation to Blood Mage:**
  - Blood Knights can take the decision `bm_elevate_to_blood_mage_decision` to attempt a ritual elevation into a full Blood Mage. During the trial, the character undergoes a Learning or Prowess test. Upon success, `lifestyle_blood_knight` is removed, `lifestyle_blood_mage` is gained, all accumulated `ancient` and `benediction` track XP carries over loss-free (1:1), and 50% of martial XP converts thematically (`slaughter` -> `hematurgy`, `vanguard` -> `bloodline`, `resilience` -> `enlightenment`).
- **Universal rank progression:** Every trait rank across all tracks awards exact stat parity with Blood Mage: `health = 0.1`, `life_expectancy = 2`, `years_of_fertility = 1`, and `epidemic_resistance = 1`, alongside `monthly_prestige = 0.1` and track-specific martial modifiers.
- **How to level & sustain lifeforce:**
  - **Empower Blood Knight Interaction (`empower_blood_knight_interaction`):** Direct interaction popup from a Blood Mage (Major Lifeforce: +10 XP to martial tracks; Minor: +5 XP).
  - **Battle Victory / Defeat:** Gains `vanguard` (+5 commander / +4 knight; 33% chance Minor Lifeforce) and `resilience` (+2 on surviving defeat).
  - **Duel Victory:** Victor gains +5 XP (`slaughter`) and awards 1 Minor Lifeforce (strictly exclusive to Blood Knights).
  - **Tournament Participation/Victory:** Completing a tournament awards +3 XP (`slaughter`).
  - **Manifest Lifeforce (`bm_manifest_lifeforce_decision`):** Blood Knights undergo a Prowess duel to stoke their blood, granting +3 XP (`resilience`) and either Major Lifeforce (critical success) or Minor Lifeforce (success).
  - **Ambient Lifeforce Roll (`blood_mage_yearly_events.004`):** Passive ~33% chance per year to condense Minor Lifeforce ambiently in addition to passive +1 XP in `resilience` and `ancient`.
  - **Lifeforce Condensation:** Spend 1 Minor Lifeforce + 100 Piety via `bm_cast_blood_magic_minor` to forge 1 Major Lifeforce (+2 Resilience XP).
  - **Minor Restorative Magic (`bm_heal_ailment`):** Healing self grants +2 XP (`resilience`); healing comrades, fellow knights, or liege grants +1 XP (`vanguard`) and +1 XP (`benediction`).
  - **Minor Blood Magic Channeling (`bm_cast_blood_magic_minor_decision`):** Blood Knights can channel minor lifeforce or purge bodily frailty (+2 `resilience` XP).

### Tracks Master Table

Each track has 10 tiers (10, 20, 30, ..., 100 XP).
- **`vanguard`**: Army command and operational mobility (+1 Advantage/tier, +1 Martial at even tiers, +2% Movement Speed/tier, +3% Pursuit/tier, +1 Martial/prestige tier at 50 & 100 XP).
- **`slaughter`**: Single combat and champion devastation (+2 Prowess/tier, +10% Knight Effectiveness/tier, +5% Dread Gain/tier, +1 Prowess/prestige tier at 50 & 100 XP).
- **`resilience`**: Somatic fortification and trauma resistance (+0.05 Health/tier, +3% Stress Loss/tier, +1 Epidemic Resistance/tier, +0.25/+0.5 Negate Health Penalty at 50/100 XP, age prowess lock at 100 XP).
- **`ancient`**: Shared with Blood Mage: Piety and age resilience.
- **`benediction`**: Shared with Blood Mage: Healing, opinion, and prestige.

## Key Mechanics

- **Mutual Exclusivity & Hierarchy:**
  - `lifestyle_blood_mage` and `lifestyle_blood_knight` are mutually exclusive opposites.
  - Blood Mages can grant Blood Knight to others, but cannot become Blood Knights themselves.
  - Blood Knights can elevate themselves to Blood Mage via `bm_elevate_to_blood_mage_decision`.
- **Major Blood Magic & Secondary Empowerment:**
  - Blood Knights have full access to Major Blood Magic (`bm_cast_blood_magic_major_decision`) and the secondary trait `lifestyle_blood_empowerment` upon possessing Major Lifeforce. Superior Blood Magic remains strictly exclusive to Blood Mages.
- **Minor Blood Magic & Healing:**
  - `bm_heal_ailment`: Can target self, courtiers, liege, close family, spouse, and knights. Blood Knights can selectively mend minor wounds/illnesses (`wounded_1`, `ill`, `lovers_pox`, `gout_ridden`, `scarred`).
  - `bm_cast_blood_magic_minor_decision`: Allows self-channeling, self-purging of negative traits, and condensing Minor Lifeforce into Major Lifeforce.

## Where the details live

| Concept | File |
| --- | --- |
| Trait definition & tracks | `common/traits/bm_blood_knight_trait.txt` |
| Elevation decision | `common/decisions/become_mage/bm_elevate_blood_knight_decision.txt` |
| Elevation event & trial | `events/bm_blood_knight_elevation_events.txt` |
| Trait XP transfer macro | `common/scripted_effects/bm_blood_mage_lifecycle_effects.txt` |
| Bestow & empower interactions | `common/character_interactions/bm_blood_knight_interactions.txt` |
| Minor healing & trait removal | `common/character_interactions/bm_cure_illness_interactions.txt` |
| Minor blood magic decision & self-purge | `common/decisions/cast_magic/bm_cast_blood_magic_minor.txt`<br>`events/bm_cast_blood_magic_minor_events.txt` |
| Yearly pulse | `events/bm_yearly_events.txt` |
