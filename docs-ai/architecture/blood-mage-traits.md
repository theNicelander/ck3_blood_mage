# Blood Mage Traits

Living technical specification for the Blood Mage lifestyle traits subsystem.

## Executive Summary

- **How to get it:** Acquired through `bm_become_blood_mage_effect` via self-initiation (faith decision or Learning ritual duel in Reykjavik/Tsushima), teaching from a friend/lover/liege (`ask_for_blood_magic_interaction`), initiation by an existing Blood Mage (`grant_blood_magic_interaction`), siphoning an imprisoned mage, witch conversion, or hereditary birth.
- **What it does:** Marks the character as a blood mage (`lifestyle_blood_mage`), granting base benefits (`+2` Learning per Piety level, `+10` Same Trait Opinion), unlocking the Blood Magic story cycle, enabling Lifeforce spellcasting, and progressing across 5 school tracks.
- **How to level it up:** Spending Lifeforce on blood magic grants XP in the spell's corresponding school (using `add_xp_bm_dynamic`). Slow passive growth comes from the yearly pulse (`ancient`), active house blood modifiers (`bloodline`), and yearly attunements.

### Master Cumulative Track Benefits (10 XP / 50 XP / 100 XP)

Each track has 10 progression levels (10 to 100 XP). In CK3, each tier unlocked applies additively.
*Note: In `lifestyle_blood_mage`, `lifestyle_blood_knight`, and shared tracks, tiers 10–40 and 60–90 grant the standard Vitality Baseline (`+0.1` Health, `+2` Life Expectancy, `+1` Year Fertility, `+1` Epidemic Resistance). Tiers 50 and 100 skip the vitality step in favor of distinct milestones and capstones (4 vitality steps at 50 XP, 8 at 100 XP).*

#### 1. Blood Mage (`lifestyle_blood_mage`)
Base: `+2` Learning per Piety level, `+10` Same Trait Opinion.

| Track | 10 XP | 50 XP | 100 XP |
| --- | --- | --- | --- |
| `ancient` | Vitality + `+0.1` Monthly Dynasty Prestige, `+5%` Lifestyle XP Gain Mult | 4× Vitality + `+0.5` Monthly Dynasty Prestige, `+25%` Lifestyle XP Gain Mult, `+0.25` Negate Health Penalty, `+1` Prowess per Piety level | 8× Vitality + `+1.0` Monthly Dynasty Prestige, `+50%` Lifestyle XP Gain Mult, `+0.5` Negate Health Penalty, `+1` Prowess per Piety level, `character_max_piety_level_add = 1`, `no_prowess_loss_from_age = yes` |
| `enlightenment` | Vitality + `+0.2` Monthly Piety, `+5%` Monthly Piety Gain Mult | 4× Vitality + `+1.0` Monthly Piety, `+25%` Monthly Piety Gain Mult, `+1` Learning per Piety level, `+1` Prowess per Piety level | 8× Vitality + `+2.0` Monthly Piety, `+50%` Monthly Piety Gain Mult, `+2` Learning per Piety level, `+1` Prowess per Piety level, `character_max_piety_level_add = 1`, `no_prowess_loss_from_age = yes` |
| `bloodline` | Vitality + `+0.2` Monthly Dynasty Prestige, `-2%` Build Gold Cost, `+2%` Domain Tax | 4× Vitality + `+1.0` Monthly Dynasty Prestige, `+1` Domain Limit, `+10%` Gold Gain Mult, `+1` Stewardship per Piety level, `+1` Prowess per Piety level, `+5` Vassal Limit, `-8%` Build Gold Cost, `+8%` Domain Tax, `+10%` Development Growth Factor, `-5%` Holding Build Speed | 8× Vitality + `+2.0` Monthly Dynasty Prestige, `+3` Domain Limit, `+30%` Gold Gain Mult, `+2` Stewardship per Piety level, `+1` Prowess per Piety level, `+15` Vassal Limit, `-20%` Build Gold Cost, `+20%` Domain Tax, `+25%` Development Growth Factor, `-15%` Holding Build Speed, `no_prowess_loss_from_age = yes` |
| `benediction` | Vitality + `+5` Same Faith Opinion, `+5` Vassal Opinion | 4× Vitality + `+2` Diplomacy, `+1` Diplomacy per Piety level, `+10` Same Faith Opinion, `+10` Vassal Opinion, `+1` Prowess per Piety level | 8× Vitality + `+5` Diplomacy, `+2` Diplomacy per Piety level, `+20` Same Faith Opinion, `+20` Vassal Opinion, `+1` Prowess per Piety level, `character_max_piety_level_add = 1`, `no_prowess_loss_from_age = yes` |
| `hematurgy` | Vitality + `+3` Hostile Scheme Success, `+3` Scheme Secrecy, `+2` Dread Baseline, `-2%` Tyranny Gain Mult | 4× Vitality + `+15` Hostile Scheme Success, `+15` Scheme Secrecy, `+1` Max Hostile Schemes, `-10` Days Scheme Phase, `+10` Dread Baseline, `+15%` Dread Gain Mult, `-10%` Tyranny Gain Mult, `+1` Intrigue per Piety level, `+1` Prowess per Piety level | 8× Vitality + `+30` Hostile Scheme Success, `+30` Scheme Secrecy, `+2` Max Hostile Schemes, `-20` Days Scheme Phase, `+20` Dread Baseline, `+25%` Dread Gain Mult, `-20%` Tyranny Gain Mult, `+2` Intrigue per Piety level, `+1` Prowess per Piety level, `no_prowess_loss_from_age = yes` |

#### 2. Blood Knight (`lifestyle_blood_knight`)
Base: `same_opinion = 10`. Vitality baseline applied at tiers 10–40, 60–90; skipped at 50 & 100 XP milestones.

| Track | 10 XP | 50 XP | 100 XP |
| --- | --- | --- | --- |
| `vanguard` | Vitality + `+1` Advantage, `+2%` Army Speed, `+3%` Pursuit Mult, `+1` Knight Limit | 4× Vitality + `+2` Martial, `+1` Martial per Piety Level, `+2` Knight Limit, `+5` Advantage, `+10%` Army Speed, `+15%` Pursuit Mult | 8× Vitality + `+5` Martial, `+2` Martial per Piety Level, `+4` Knight Limit, `+10` Advantage, `+20%` Army Speed, `+30%` Pursuit Mult, `no_prowess_loss_from_age = yes` |
| `slaughter` | Vitality + `+2` Prowess, `+10%` Knight Effectiveness, `+5%` Dread Gain Mult, `+1` Knight Limit | 4× Vitality + `+10` Prowess, `+1` Prowess per Piety Level, `+50%` Knight Effectiveness, `+10` Natural Dread, `+25%` Dread Gain Mult | 8× Vitality + `+20` Prowess, `+2` Prowess per Piety Level, `+100%` Knight Effectiveness, `+20` Natural Dread, `+50%` Dread Gain Mult, `no_prowess_loss_from_age = yes` |
| `ancient` | Identical to Mage track | Identical to Mage track | Identical to Mage track (`character_max_piety_level_add = 1`, `no_prowess_loss_from_age = yes`) |
| `enlightenment` | Identical to Mage track | Identical to Mage track | Identical to Mage track (`character_max_piety_level_add = 1`, `no_prowess_loss_from_age = yes`) |
| `benediction` | Identical to Mage track | Identical to Mage track | Identical to Mage track (`character_max_piety_level_add = 1`, `no_prowess_loss_from_age = yes`) |

#### 3. Blood Empowerment (`lifestyle_blood_empowerment`)
Base: None. Vitality baseline applied at tiers 10–90; skipped at 100 XP in favor of Devotion impact multiplier.

| Track | 10 XP | 50 XP | 100 XP |
| --- | --- | --- | --- |
| `dynasty` | Vitality + `+4%` Fertility, `+2.5%` Congenital Chance, `+2.5%` Inactive Inheritance | 5× Vitality + `+20%` Fertility, `+12.5%` Congenital Chance, `+12.5%` Inactive Inheritance | 9× Vitality + `+40%` Fertility, `+25%` Congenital Chance, `+25%` Inactive Inheritance, `+5%` Devotion Impact (`piety_level_impact_mult = 0.05`), `no_prowess_loss_from_age = yes` |
| `mastery` | Vitality + `+4%` Lifestyle XP Mult, `-10`d Language Phase, `+3%` Personal Scheme Success | 5× Vitality + `+20%` Lifestyle XP Mult, `-50`d Language Phase, `+15%` Personal Scheme Success, `+1` Language Slot | 9× Vitality + `+40%` Lifestyle XP Mult, `-100`d Language Phase, `+30%` Personal Scheme Success, `+4` Language Slots, `+5%` Devotion Impact (`piety_level_impact_mult = 0.05`), `no_prowess_loss_from_age = yes` |
| `presence` | Vitality + `+1.5` General Opinion, `+1.0` Vassal Opinion, `+5%` Stress Loss Mult | 5× Vitality + `+7.5` General Opinion, `+5.0` Vassal Opinion, `+25%` Stress Loss Mult | 9× Vitality + `+15.0` General Opinion, `+10.0` Vassal Opinion, `+50%` Stress Loss Mult, `+5%` Devotion Impact (`piety_level_impact_mult = 0.05`), `no_prowess_loss_from_age = yes` |
| `prosperity` | Vitality + `+0.1` Income, `+2.5%` Income Mult | 5× Vitality + `+0.5` Income, `+12.5%` Income Mult | 9× Vitality + `+1.0` Income, `+25%` Income Mult, `+5%` Devotion Impact (`piety_level_impact_mult = 0.05`), `no_prowess_loss_from_age = yes` |
| `shadows` | Vitality + `+5` Scheme Secrecy, `-3%` Enemy Scheme Success Chance | 5× Vitality + `+25` Scheme Secrecy, `-15%` Enemy Scheme Success Chance | 9× Vitality + `+50` Scheme Secrecy, `-30%` Enemy Scheme Success Chance, `+5%` Devotion Impact (`piety_level_impact_mult = 0.05`), `no_prowess_loss_from_age = yes` |

## Concepts

### Blood Mage (`lifestyle_blood_mage`)
- **Type:** Lifestyle trait. Mutually exclusive permanent choice with `lifestyle_blood_knight`. Inheritable (25% single parent, 100% both parents; 0.2% birth / random creation).
- **Base Stats:** `+2` Learning per Piety level, `+10` Same Trait Opinion.
- **Entry Effect:** Added via `bm_become_blood_mage_effect`.
- **Tracks:** 5 schools (`ancient`, `enlightenment`, `bloodline`, `benediction`, `hematurgy`). Max 100 XP each. `ancient`, `benediction`, and `enlightenment` are shared identically with `lifestyle_blood_knight`.
- **Devotion Apex:** Capstones at 100 XP in `ancient`, `enlightenment`, and `benediction` each grant `character_max_piety_level_add = 1` (enabling Levels 6–8 Devotion: Divine, Demigod, Godlike).
- **Prowess Age Lock:** Every track capstone at 100 XP grants `no_prowess_loss_from_age = yes`.

### Acquisition Triggers
All routes call `bm_become_blood_mage_effect`:
- `bm_blood_cultist_become_blood_mage_decision`: Decision for Blóðtrú faithful; initiation duel against Egill Skallagrímsson (`bm_geyser_duel.0001`) in Reykjavik or Tsushima (`piety_level >= 2`, costs 1 Devotion level).
- `bm_enhance_blood_ritual_decision`: Decision for non-faithful; initiation duel against Egill Skallagrímsson (`bm_geyser_duel.0001`) in Reykjavik or Tsushima (`piety_level >= 2`, costs 1 Devotion level).
- `grant_blood_magic_interaction`: Mage initiates apprentice/courtier (Major Lifeforce + 100 Piety OR Minor Lifeforce + 250 Piety; awards Bloodline XP).
- `ask_for_blood_magic_interaction`: Non-mage asks friend/lover/soulmate mage to teach them (spends 250 Piety + recipient Superior Lifeforce).
- `bm_get_blood_magic_from_prisoner_interaction`: Character harvests trait from imprisoned blood mage.
- `convert_to_blood_magic_from_witch`: Witch swaps witch trait/secret for blood magic.
- Birth inheritance: Rolled on newborn children of blood mages via `on_birth_child`.

## Where the details live

| Piece | File |
| --- | --- |
| Blood Mage trait | `common/traits/bm_blood_mage_trait.txt` |
| Blood Knight trait | `common/traits/bm_blood_knight_trait.txt` |
| Blood Empowerment trait | `common/traits/bm_blood_empowerment_trait.txt` |
| XP helpers (`add_xp_bm_dynamic`, `add_shared_bm_bk_xp`, `add_blood_knight_xp`, `add_blood_empowerment_xp`) | `common/scripted_effects/bm_trait_track_xp_gain_effects.txt` |
| Acquisition effect | `common/scripted_effects/bm_blood_mage_lifecycle_effects.txt` |
| Total trait progression value | `common/script_values/bm_blood_mage_portrait_values.txt` |
| Geyser duels | `events/bm_geyser_duel_events.txt` |
| Blood Empowerment event | `events/bm_blood_empowerment_event.txt` |
