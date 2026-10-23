# Blood Mage Prevalence and Lifecycle

## Executive Summary

- **What:** Lifecycle, birth inheritance, world-wide population scaling, and yearly cleanup audits for Blood Mages and Blood Knights.
- **Mandatory Entry Effects:**
  - Blood Mage: `bm_become_blood_mage_effect`. Adds `lifestyle_blood_mage` and base `lifestyle_blood_power`, initializes story cycle `bm_blood_mage_story`, sets flag `bm_blood_mage_prevalence_reviewed`.
  - Blood Knight: `bm_become_blood_knight_effect`. Adds `lifestyle_blood_knight` and base `lifestyle_blood_power`, initializes story cycle `bm_blood_mage_story`, sets flag `bm_blood_knight_prevalence_reviewed`.
- **Prevalence Audits:** Evaluated at birth (`on_birth_child`), game start (`on_game_start_after_lobby`), and yearly pulse (`random_yearly_everyone_pulse`). Strips traits from AI characters if rules restrict prevalence (`player_only`, `one_in_10000`, `one_in_1000`).

### Prevalence Behavior Matrix

| Rule Setting (Mage / Knight) | Birth Manifestation | AI Retention | AI Decision Weight |
| --- | --- | --- | --- |
| `player_only` | Player children only | 0% for AI (instantly stripped) | 0 (AI disabled) |
| `one_in_10000` | Heavily suppressed | 0.01% retention | Heavily reduced |
| `one_in_1000` | Suppressed | 0.1% retention | Reduced |
| `default` | 25% single parent, 100% both; 0.2% birth | Standard retention | 1.0 (Standard) |
| `one_in_100` | Elevated | 100% retention + extra spontaneous | Boosted |
| `one_in_10` | Highly elevated | 100% retention + frequent spontaneous | High |
| `everyone` | 100% all newborns globally | 100% retention | Maximum |

### Trait Inheritance Rules

| Trait | Hereditary Type | Single Parent Chance | Both Parents Chance | Baseline Birth Roll | Notes |
| --- | --- | --- | --- | --- | --- |
| `lifestyle_blood_mage` | Scripted Birth On-Action (`on_birth_child`, non-genetic) | Scaled by game rule (35%–60%) | 100% | Scaled by game rule (1%–10%) | Evaluated on birth by prevalence engine & game rules. |
| `lifestyle_blood_knight` | Scripted Birth On-Action (`on_birth_child`, non-genetic) | Scaled by game rule (35%–60%) | 100% | Scaled by game rule (1%–10%) | Evaluated on birth by prevalence engine & game rules. |
| `lifestyle_blood_power` | Non-Hereditary (`inheritable = no`, `genetic = no`) | 0% | 0% | 0% | Personal occult mastery. Granted automatically at 0 XP alongside Mage/Knight traits. |

- **Lineage Enhancement & Trait Theft:** Blood Power `dynasty` track and house modifier `dynasty_blood_legacy_modifier` boost positive congenital transmission. Trait drain interaction (`trait_drain_prisoner_event_interaction`) siphons congenital traits into personal lineage without natural mating.


## Lifecycle Pipeline

```
Acquisition (Decision / Event / Birth)
  │
  ├─► Standard Blood Mage Entry: bm_become_blood_mage_effect
  │     ├─► add_trait = lifestyle_blood_mage (blocked if already blood knight)
  │     ├─► add_trait = lifestyle_blood_power (base 0 XP for adjacent UI grouping)
  │     ├─► bm_ensure_blood_mage_story_effect (creates situation story panel)
  │     ├─► add_character_flag = bm_blood_mage_prevalence_reviewed
  │     └─► bm_apply_blood_mage_prevalence_retention_effect (strips mage + power if AI under restricted rules)
  │
  └─► Standard Blood Knight Entry: bm_become_blood_knight_effect
        ├─► add_trait = lifestyle_blood_knight (blocked if already blood mage)
        ├─► add_trait = lifestyle_blood_power (base 0 XP for adjacent UI grouping)
        ├─► bm_ensure_blood_mage_story_effect (creates situation story panel)
        ├─► add_character_flag = bm_blood_knight_prevalence_reviewed
        └─► bm_apply_blood_knight_prevalence_retention_effect (strips knight + power if AI under restricted rules)
```

- **Childbirth Milestone:** When a child is born (`on_birth_child` -> `bm_on_birth_bloodline_xp`), any blood mage parent receives **+1 Major Lifeforce** (`lifeforce_modifier_major`) and +2 `bloodline` XP (+4 `bloodline` XP if the newborn inherits the trait; doubled by Superior Feingur). Blood knight parents receive martial `vanguard` XP without Lifeforce gain.

## Where the details live

| Piece | File |
| --- | --- |
| Lifecycle scripted effects | `common/scripted_effects/bm_blood_mage_lifecycle_effects.txt` |
| Birth prevalence on-actions | `common/on_action/bm_blood_mage_prevalence_on_actions.txt` |
| Yearly pulse on-actions | `common/on_action/bm_yearly_pulse.txt` |
| Prevalence AI modifiers | `common/scripted_modifiers/bm_blood_mage_prevalence_modifiers.txt` |
| Yearly events | `events/bm_yearly_events.txt` |
| Character templates | `common/scripted_character_templates/bm_character_templates.txt` |
| Prevalence game rule | `common/game_rules/bm_game_rules.txt` (`bm_blood_mage_prevalence`) |

## Gotchas

- **Non-Genetic Rule:** Never set `genetic = yes` on `lifestyle_blood_mage`. Genetic traits route into CK3's recessive/tier system, breaking deterministic 25%/100% inheritance.
- **Never use bare `add_trait`:** Bypasses story cycle creation, leaving the character without the Blood Magic panel. Always call `bm_become_blood_mage_effect`.
- **Player Only:** Under `bm_prevalence_player_only`, any AI acquiring the trait has it immediately stripped by `bm_apply_blood_mage_prevalence_retention_effect`.
