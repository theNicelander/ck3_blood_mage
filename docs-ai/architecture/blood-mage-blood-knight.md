# Blood Mage: Blood Knight

Living technical specification for the Blood Knight subsystem.

## Executive Summary

- **What:** Permanent, Devotion-anchored martial endgame peer (`lifestyle_blood_knight`) to `lifestyle_blood_mage`, modeled after CK3 1.20's Proclaim the Living Word split (*Fire and Sword* vs *Shepherd of the Faithful*). Features 5 tracks: 2 martial tracks specific to Blood Knight (`vanguard`, `slaughter`) and 3 shared tracks (`ancient`, `benediction`, `enlightenment`), max 100 XP each.
- **Icon:** `bm_blood_knight.dds` (`gfx/interface/icons/traits/bm_blood_knight.dds`).
- **Base stats:** `same_opinion = 10`. Ruler designer cost: 50. Inheritable (25% single parent, 100% both; 0.20% birth) scaled by campaign game rule `bm_blood_knight_prevalence`. Mutually exclusive with `lifestyle_blood_mage` (scripted dual-wielding preserved for legendary figures like Egill).
- **How to acquire:**
  - `make_blood_knight_interaction`: Initiated by a fellow Blood Knight (Major Lifeforce + 100 Piety OR Minor Lifeforce + 250 Piety) on a sworn knight/courtier.
  - **Geyser Duel Initiation (`bm_geyser_duel.0001`):** Travel to Reykjavik or Tsushima via `bm_blood_cultist_become_blood_mage_decision` or `bm_enhance_blood_ritual_decision` (requires `piety_level >= 2`). Choosing the Prowess duel requires `piety_level >= 2`, costs 1 Devotion level (`add_piety_level = -1`), and bestows `lifestyle_blood_knight` upon victory.
- **Mutual Exclusivity:** Choice between Blood Mage and Blood Knight is permanent. Elevation decisions (`bm_elevate_to_blood_mage_decision`) are deprecated.
- **Apex Devotion (Levels 6–8):** The 100 XP capstones of all 3 shared tracks (`ancient`, `enlightenment`, `benediction`) each grant `character_max_piety_level_add = 1` for both Blood Knights and Blood Mages, enabling ascension to Level 8 Devotion (Godlike).
- **Track Milestones & Cleanliness:** Vitality baselines (`health`, `life_expectancy`, `years_of_fertility`, `epidemic_resistance`) are applied at standard levels (10-40, 60-90) and skipped at 50 XP and 100 XP milestones. Every track capstone at 100 XP grants `no_prowess_loss_from_age = yes`.
- **How to level & sustain lifeforce:**
  - **Empower Blood Knight Interaction (`empower_blood_knight_interaction`):** Direct interaction popup from a fellow Blood Knight to a sworn knight comrade (Major Lifeforce: +10 XP to `vanguard` and `slaughter`, +4 Benediction XP to caster; Minor: +5 martial XP, +2 Benediction XP to caster).
  - **Battle Victory / Defeat:** Gains `vanguard` (+4 commander / +3 knight; 33% chance Minor Lifeforce) and defeat survival (+1 `vanguard`, +1 `enlightenment`).
  - **Fatal Duels:** Slaying a foe in single combat grants +5 `slaughter` XP and 1 Major Lifeforce. Slaying a foe with `prowess >= 35` or holding `lifestyle_blood_mage`/`lifestyle_blood_knight` has a 25% chance to yield Superior Lifeforce directly.
  - **Tournament Participation/Victory:** Completing a tournament awards +3 XP (`slaughter`).
  - **Seek Power in Nature's Domain (`seek_power_decision`):** Wilderness expedition harvesting Lifeforce and martial XP (2-year cooldown landed, 1-year unlanded/wanderer).
  - **Manifest Lifeforce (`bm_manifest_lifeforce_decision`):** Undergo Learning duel to stoke blood, granting +3 `enlightenment` XP and Major or Minor Lifeforce.
  - **Manifest Superior Lifeforce (`bm_manifest_superior_lifeforce_decision`):** Distill 1 Minor + 1 Major Lifeforce + 250 Piety in a Learning duel yielding Superior Lifeforce and +2 to +8 `ancient` XP.
  - **Ambient Lifeforce Roll (`blood_mage_yearly_events.004`):** Passive ~33% chance per year to condense Minor Lifeforce ambiently in addition to passive +1 XP in `enlightenment` and `ancient`. Strictly exclusive to Blood Knights (`lifestyle_blood_knight`).
  - **Lifeforce Condensation:** Spend 1 Minor Lifeforce + 100 Piety via `bm_cast_blood_magic_minor` to forge 1 Major Lifeforce (+2 `ancient` XP).
  - **Minor Lifedrain on Courtiers and Prisoners (`lifedrain_courtier_event_interaction`):** Siphon free courtiers or prisoners using a Prowess duel (costs 25 Piety), granting Minor Lifeforce and +1 `slaughter` XP.
  - **Trait Drain on Prisoners (`trait_drain_prisoner_event_interaction`):** Holding Major Lifeforce can steal congenital traits from prisoners up to rank 5 (`genius`, `herculean`, `beautiful`, plus `fecund`/`giant`/`pure_blooded`), granting +2 `slaughter` XP.
  - **Bless Bloodline (`bm_bless_bloodline_interaction`):** Bless kin's blood (costs 35 Piety + Minor Lifeforce), granting +2 `vanguard` XP to caster.
  - **Become Blood Cultist (`become_blood_cultist_decision`):** Convert realm faith to Blóðtrú, Ketsudō, or Xuédào (costs 250 Piety + Major Lifeforce; 10-year cooldown).
  - **Full Superior Magic Access (`bm_cast_blood_magic_superior_decision`):**
    - Inscribe Superior Blood Rune (+10 `ancient` XP, +30% `piety_level_impact_mult`).
    - Master Education to 5★ (+10 `enlightenment` XP).
    - Forge Blood Golem (+5 `vanguard` XP).
    - Manifest Apex Congenital Perfection (Ranks 3-5; +6 `vanguard`, +2 `enlightenment` XP).
  - **Full Healing Access (`bm_heal_ailment`):** Heal minor, major, and deadly ailments (cancer, leprosy, bubonic plague, wounded_3, etc.) on self and others.

### Tracks Master Table

Each track has 10 tiers (10, 20, 30, ..., 100 XP).
- **`vanguard`**: Army command, strategic speed, and Devotion scaling:
  - Tiers 10-40, 60-90: Vitality baseline (+0.1 Health, +2 Life Exp, +1 Fertility, +1 Epidemic Res), +1 Advantage, +2% Army Speed, +3% Pursuit, +1 Knight Limit.
  - 50 XP: +2 Martial, +1 Martial per Piety Level, +2 Knight Limit, +5 Advantage.
  - 100 XP: +5 Martial, +2 Martial per Piety Level, +4 Knight Limit, `no_prowess_loss_from_age = yes`.
- **`slaughter`**: Combat lethality, knight effectiveness, and Devotion scaling:
  - Tiers 10-40, 60-90: Vitality baseline, +2 Prowess, +10% Knight Effectiveness, +5% Dread Gain, +1 Knight Limit.
  - 50 XP: +10 Prowess, +1 Prowess per Piety Level, +50% Knight Effectiveness, +10 Natural Dread.
  - 100 XP: +20 Prowess, +2 Prowess per Piety Level, +100% Knight Effectiveness, `no_prowess_loss_from_age = yes`.
- **`enlightenment`**: Shared: Piety, learning, and self-mastery:
  - Tiers 10-40, 60-90: Vitality baseline, +0.2 Monthly Piety, +5% Piety Gain.
  - 50 XP: +2 Learning, +1 Learning per Piety Level, +0.2 Monthly Piety, +5% Piety Gain.
  - 100 XP: +5 Learning, +2 Learning per Piety Level, `character_max_piety_level_add = 1`, `no_prowess_loss_from_age = yes`.
- **`ancient`**: Shared: Dynasty prestige, lifestyle XP, longevity, and age resilience:
  - Tiers 10-40, 60-90: Vitality baseline, +0.1 Monthly Dynasty Prestige, +5% Lifestyle XP.
  - 50 XP: +0.25 Negate Health Penalty, +0.1 Monthly Dynasty Prestige, +5% Lifestyle XP.
  - 100 XP: +0.5 Negate Health Penalty, `character_max_piety_level_add = 1`, `no_prowess_loss_from_age = yes`.
- **`benediction`**: Shared: Healing, opinion, and diplomatic Devotion:
  - Tiers 10-40, 60-90: Vitality baseline, +5 Same Faith Opinion, +5 Vassal Opinion.
  - 50 XP: +2 Diplomacy, +1 Diplomacy per Piety Level, +10 Same Faith Opinion, +10 Vassal Opinion.
  - 100 XP: +5 Diplomacy, +2 Diplomacy per Piety Level, `character_max_piety_level_add = 1`, `no_prowess_loss_from_age = yes`.

## Where the details live

| Concept | File |
| --- | --- |
| Trait definition & tracks | `common/traits/bm_blood_knight_trait.txt` |
| Lifecycle & prevalence effects | `common/scripted_effects/bm_blood_mage_lifecycle_effects.txt` |
| Prevalence game rule | `common/game_rules/bm_game_rules.txt` (`bm_blood_knight_prevalence`) |
| Bestow & empower interactions | `common/character_interactions/bm_blood_knight_interactions.txt` |
| Healing & ailment removal | `common/character_interactions/bm_cure_illness_interactions.txt` |
| Superior magic decision & events | `common/decisions/cast_magic/bm_cast_blood_magic_superior.txt`<br>`events/bm_cast_blood_magic_superior_events.txt` |
| Duel fatality & Superior harvest | `common/on_action/bm_duel_on_actions.txt` |
| Yearly pulse | `events/bm_yearly_events.txt` |
