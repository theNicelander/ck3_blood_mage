# Blood Mage Prevalence and Lifecycle

## Executive Summary

- **What:** Lifecycle, birth inheritance, world-wide population scaling, and yearly cleanup audits.
- **Mandatory Entry Effect:** `bm_become_blood_mage_effect`. Adds `lifestyle_blood_mage`, initializes story cycle `bm_blood_mage_story`, sets flag `bm_blood_mage_prevalence_reviewed`.
- **Prevalence Audits:** Evaluated at birth (`on_birth_child`) and yearly pulse (`yearly_blood_mage_pulse`). Strips trait from AI characters if rules restrict prevalence (`player_only`, `one_in_10000`, `one_in_1000`).

### Prevalence Behavior Matrix

| Rule Setting | Birth Manifestation | AI Retention | AI Decision Weight |
| --- | --- | --- | --- |
| `bm_prevalence_player_only` | Player children only | 0% for AI (instantly stripped) | 0 (AI disabled) |
| `bm_prevalence_one_in_10000` | Heavily suppressed | 0.01% retention | Heavily reduced |
| `bm_prevalence_one_in_1000` | Suppressed | 0.1% retention | Reduced |
| `bm_prevalence_default` | 25% single parent, 100% both; 0.2% birth | Standard retention | 1.0 (Standard) |
| `bm_prevalence_one_in_100` | Elevated | 100% retention + extra spontaneous | Boosted |
| `bm_prevalence_one_in_10` | Highly elevated | 100% retention + frequent spontaneous | High |
| `bm_prevalence_everyone` | 100% all newborns globally | 100% retention | Maximum |

## Lifecycle Pipeline

```
Acquisition (Decision / Event / Birth / Elevation)
  │
  ├─► Standard Entry: bm_become_blood_mage_effect
  │     ├─► add_trait = lifestyle_blood_mage
  │     ├─► bm_ensure_blood_mage_story_effect (creates situation story panel)
  │     ├─► add_character_flag = bm_blood_mage_prevalence_reviewed
  │     └─► bm_apply_blood_mage_prevalence_retention_effect (strips if AI under restricted rules)
  │
  └─► Elevation Entry: bm_elevate_blood_knight_to_blood_mage_effect
        ├─► Removes lifestyle_blood_knight, adds lifestyle_blood_mage
        ├─► Converts 50% martial XP (slaughter->hematurgy, vanguard->bloodline)
        ├─► Carries over ancient, benediction, and enlightenment XP 1:1
        └─► Ensures story panel and prevalence review flag
```

- **Childbirth Milestone:** When a child is born (`on_birth_child` -> `bm_on_birth_bloodline_xp`), any blood mage parent receives +2 `bloodline` XP (+4 `bloodline` XP if the newborn inherits the trait).

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

- **Never use bare `add_trait`:** Bypasses story cycle creation, leaving the character without the Blood Magic panel. Always call `bm_become_blood_mage_effect`.
- **Player Only:** Under `bm_prevalence_player_only`, any AI acquiring the trait has it immediately stripped by `bm_apply_blood_mage_prevalence_retention_effect`.
