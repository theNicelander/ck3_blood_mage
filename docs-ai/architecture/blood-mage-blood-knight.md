# Blood Mage: Blood Knight

Living technical specification for the Blood Knight subsystem.

## Executive Summary

- **What:** Evolving martial combat lifestyle trait `lifestyle_blood_knight` functioning as a stepping stone toward Blood Mage. Features 5 tracks: 2 martial/prowess tracks specific to Blood Knight (`vanguard`, `slaughter`) and 3 tracks shared with Blood Mage (`ancient`, `benediction`, `enlightenment`), max 100 XP each.
- **Icon:** `bm_blood_knight.dds` (`gfx/interface/icons/traits/bm_blood_knight.dds`).
- **Base stats:** `prowess = 5`. Ruler designer cost: 50. Inheritable (25% single parent, 100% both; 0.20% birth) scaled by campaign game rule `bm_blood_knight_prevalence`. Mutually exclusive with `lifestyle_blood_mage` via entry effect, birth priority, and decision/interaction gates (permitting scripted dual-wielding on legendary figures like Egill).
- **How to acquire:**
  - `make_blood_knight_interaction`: Cast by a Blood Mage (100 Piety + Major Lifeforce) or fellow Blood Knight (200 Prestige + Minor Lifeforce, OR 0 Prestige + Major Lifeforce) on a sworn knight/courtier (cannot target self; a Blood Mage cannot become a Blood Knight).
  - **Geyser Duel Initiation (`bm_geyser_duel.0001`):** Travel to Reykjavik or Tsushima and confront Egill Skallagrímsson via `bm_blood_cultist_become_blood_mage_decision` or `bm_enhance_blood_ritual_decision` (requires Piety or Prestige level >= 2 to open decision; unavailable to existing Blood Mages and Blood Knights). Choosing the Prowess duel requires Prestige level >= 2, costs 1 Fame level (`add_prestige_level = -1`), and bestows `lifestyle_blood_knight` upon victory.
- **Elevation to Blood Mage:**
  - Blood Knights can take the decision `bm_elevate_to_blood_mage_decision` (requires Piety level >= 3, Learning > 30, Minor or Major Lifeforce held, costs 500 Piety) to attempt a ritual elevation into a full Blood Mage. During the trial, the character undergoes a Learning or Prowess test. Upon success, `lifestyle_blood_knight` is removed, `lifestyle_blood_mage` is gained, all accumulated `ancient`, `benediction`, and `enlightenment` track XP carries over loss-free (1:1), and 50% of knight-exclusive XP converts thematically (`vanguard` -> `bloodline`, `slaughter` -> `hematurgy`).
- **Universal rank progression:** Every trait rank across all tracks awards exact stat parity with Blood Mage: `health = 0.1`, `life_expectancy = 2`, `years_of_fertility = 1`, and `epidemic_resistance = 1`, alongside `monthly_prestige = 0.1` and track-specific martial modifiers.
- **How to level & sustain lifeforce:**
  - **Empower Blood Knight Interaction (`empower_blood_knight_interaction`):** Direct interaction popup from a fellow Blood Knight to a sworn knight comrade (Major Lifeforce: +10 XP to `vanguard` and `slaughter`, +4 Benediction XP to caster; Minor: +5 martial XP, +2 Benediction XP to caster).
  - **Battle Victory / Defeat:** Gains `vanguard` (+4 commander / +3 knight; 33% chance Minor Lifeforce) and defeat survival (+1 `vanguard`, +1 `enlightenment`).
  - **Duel Victory:** Victor gains +5 XP (`slaughter`) and awards 1 Minor Lifeforce (strictly exclusive to Blood Knights).
  - **Tournament Participation/Victory:** Completing a tournament awards +3 XP (`slaughter`).
  - **Seek Power in Nature's Domain (`seek_power_decision`):** Unified wilderness expedition harvesting Lifeforce and martial XP (2-year cooldown landed, 1-year unlanded/wanderer).
  - **Manifest Lifeforce (`bm_manifest_lifeforce_decision`):** Blood Knights undergo a Learning duel to stoke their blood, granting +3 XP (`enlightenment`) and either Major Lifeforce (critical success) or Minor Lifeforce (success).
  - **Ambient Lifeforce Roll (`blood_mage_yearly_events.004`):** Passive ~33% chance per year to condense Minor Lifeforce ambiently in addition to passive +1 XP in `enlightenment` and `ancient`. Strictly exclusive to Blood Knights (`lifestyle_blood_knight`); Blood Mages do not receive ambient Lifeforce.
  - **Lifeforce Condensation:** Spend 1 Minor Lifeforce + 100 Piety via `bm_cast_blood_magic_minor` to forge 1 Major Lifeforce (+2 `ancient` XP).
  - **Minor Lifedrain on Courtiers and Prisoners (`lifedrain_courtier_event_interaction`):** Blood Knights can siphon free courtiers or prisoners using a Prowess duel (costs 25 Piety), granting Minor Lifeforce and +1 `slaughter` XP.
  - **Trait Drain on Prisoners (`trait_drain_prisoner_event_interaction`):** Blood Knights holding Major Lifeforce can steal congenital traits from prisoners up to rank 5 (`genius`, `herculean`, `beautiful`, plus `fecund`/`giant`/`pure_blooded`), granting +2 `slaughter` XP.
  - **Bless Bloodline (`bm_bless_bloodline_interaction`):** Blood Knights can bless their kin's blood (costs 35 Piety + Minor Lifeforce), granting +2 `vanguard` XP to the caster.
  - **Become Blood Cultist (`become_blood_cultist_decision`):** Blood Knights can convert realm faith to Blóðtrú, Ketsudō, or Xuédào (costs 250 Piety + Major Lifeforce; 10-year cooldown).
  - **Education Elevation (`bm_cast_blood_magic_major_decision`):** Blood Knights can elevate any education trait they hold up to rank 4 via Major Blood Magic (costs Major Lifeforce + Piety), granting +5 `enlightenment` XP (level 5 remains exclusive to Blood Mages via Superior Magic).
  - **Restorative Magic (`bm_heal_ailment`):** Blood Knights can heal minor and major ailments on self and others using Minor or Major Lifeforce (healing allies awards +1 Vanguard & +1 Benediction XP for minor, +2 Vanguard & +2 Benediction XP for major; self-healing awards +2 or +4 Enlightenment XP; deadly ailments remain exclusive to Blood Mages via Superior Magic).
  - **Minor Blood Magic Channeling (`bm_cast_blood_magic_minor_decision`):** Blood Knights can channel minor lifeforce or purge bodily frailty (+1/+2 `enlightenment` XP).

### Tracks Master Table

Each track has 10 tiers (10, 20, 30, ..., 100 XP).
- **`vanguard`**: Army command and operational mobility (+1 Advantage/tier, +1 Martial at even tiers, +2% Movement Speed/tier, +3% Pursuit/tier, +1 Knight Limit/tier, +1 Martial/prestige tier at 50 & 100 XP).
- **`slaughter`**: Single combat and champion devastation (+2 Prowess/tier, +10% Knight Effectiveness/tier, +5% Dread Gain/tier, +1 Prowess/prestige tier at 50 & 100 XP).
- **`enlightenment`**: Shared with Blood Mage: Piety, learning, and self-mastery (+0.2 Monthly Piety/tier, +5% Piety Gain/tier, +1 Learning per Piety level at 50 & 100 XP, age prowess lock at 100 XP).
- **`ancient`**: Shared with Blood Mage: Dynasty prestige, lifestyle XP, longevity, and age resilience (+0.1 Monthly Dynasty Prestige/tier, +5% Lifestyle XP/tier, +0.25/+0.5 Negate Health Penalty at 50/100 XP, age prowess lock at 100 XP).
- **`benediction`**: Shared with Blood Mage: Healing, opinion, and prestige.

## Key Mechanics

- **Mutual Exclusivity & Hierarchy:**
  - `lifestyle_blood_mage` and `lifestyle_blood_knight` are mutually exclusive opposites.
  - Blood Mages can grant Blood Knight to others, but cannot become Blood Knights themselves.
  - Blood Knights can elevate themselves to Blood Mage via `bm_elevate_to_blood_mage_decision`.
- **Major Blood Magic & Secondary Empowerment:**
  - Blood Knights have full access to Major Blood Magic (`bm_cast_blood_magic_major_decision`) and the secondary trait `lifestyle_blood_empowerment` upon possessing Major Lifeforce. Superior Blood Magic remains strictly exclusive to Blood Mages.
- **Restorative Blood Magic & Healing:**
  - `bm_heal_ailment`: Can target self, courtiers, liege, close family, spouse, and knights. Blood Knights can use Minor Lifeforce to heal minor ailments, and Major Lifeforce to heal major ailments on both self and others (e.g. `weak`, `wounded_2`, `incapable`, `infirm`, `blind`, etc.; deadly ailments remain Blood Mage only). Awards +2 `enlightenment` XP (minor self-healing), +4 `enlightenment` XP (major self-healing), +1 `vanguard` and +1 `benediction` XP (minor ally healing), or +2 `vanguard` and +2 `benediction` XP (major ally healing).
  - `bm_cast_blood_magic_minor_decision`: Allows self-channeling, self-purging of negative traits, and condensing Minor Lifeforce into Major Lifeforce.
- **Situation Panel Access:**
  - Blood Knight rulers have access to the Blood Magic Situation panel (`bm_blood_mage_story`), displaying their knight disciplines (`vanguard`, `slaughter`, `ancient`, `benediction`, `enlightenment`), Lifeforce reserves, active attunement, and the unified Blood Knights (Dynasty & Court) roster.

## Where the details live

| Concept | File |
| --- | --- |
| Trait definition & tracks | `common/traits/bm_blood_knight_trait.txt` |
| Lifecycle & prevalence effects | `common/scripted_effects/bm_blood_mage_lifecycle_effects.txt` |
| Prevalence game rule | `common/game_rules/bm_game_rules.txt` (`bm_blood_knight_prevalence`) |
| Elevation decision | `common/decisions/become_mage/bm_elevate_blood_knight_decision.txt` |
| Elevation event & trial | `events/bm_blood_knight_elevation_events.txt` |
| Trait XP transfer macro | `common/scripted_effects/bm_blood_mage_lifecycle_effects.txt` |
| Bestow & empower interactions | `common/character_interactions/bm_blood_knight_interactions.txt` |
| Minor healing & trait removal | `common/character_interactions/bm_cure_illness_interactions.txt` |
| Minor blood magic decision & self-purge | `common/decisions/cast_magic/bm_cast_blood_magic_minor.txt`<br>`events/bm_cast_blood_magic_minor_events.txt` |
| Yearly pulse | `events/bm_yearly_events.txt` |
