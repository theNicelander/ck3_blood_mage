# Bloodlust Track (`lifestyle_blood_mage`)

Technical specification for the `bloodlust` lifestyle track on `lifestyle_blood_mage`.

## Overview & Philosophy

The `bloodlust` track is the martial, prowess, and battlefield mastery track of `lifestyle_blood_mage`.

Every Blood Mage also natively gains the **Worthy Commander** perk (`ignores_gender_army_rules = yes`), allowing all blood mages to lead armies regardless of realm gender laws.

---

## Track Progression & Stat Scaling

The `bloodlust` track uses the standard 10-tier progression (10 to 100 XP in increments of 10):

| Tier (XP) | Modifiers Added at Tier | Cumulative Total Highlights |
| :--- | :--- | :--- |
| **10 XP** | Vitality Step, `prowess = 1.5` | +0.1 Health, +2.5 Life Exp, +1.5 Prowess |
| **20 XP** | Vitality Step, `prowess = 1.5`, `martial = 1`, `knight_limit = 1` | +0.2 Health, +5 Life Exp, +3 Prowess, +1 Martial, +1 Knight Limit |
| **30 XP** | Vitality Step, `prowess = 1.5`, `advantage = 1` | +0.3 Health, +7.5 Life Exp, +4.5 Prowess, +1 Martial, +1 Advantage, +1 Knight Limit |
| **40 XP** | Vitality Step, `prowess = 1.5`, `martial = 1`, `knight_limit = 1` | +0.4 Health, +10 Life Exp, +6 Prowess, +2 Martial, +1 Advantage, +2 Knight Limit |
| **50 XP (Milestone)** | 4× Vitality Step, `prowess = 7`, `advantage = 1`, `dread_baseline_add = 5`, `martial_per_piety_level = 1`, `prowess_per_piety_level = 1` | 4× Vitality, +13 Prowess, +2 Martial, +2 Advantage, +2 Knight Limit, +5 Dread Baseline, +1 Martial & Prowess per Piety Level |
| **60 XP** | Vitality Step, `prowess = 1.5`, `martial = 1`, `knight_limit = 1` | Cumulative standard progression |
| **70 XP** | Vitality Step, `prowess = 1.5`, `advantage = 1` | Cumulative standard progression |
| **80 XP** | Vitality Step, `prowess = 1.5`, `martial = 1`, `knight_limit = 1` | Cumulative standard progression |
| **90 XP** | Vitality Step, `prowess = 1.5`, `advantage = 1` | Cumulative standard progression |
| **100 XP (Capstone)** | 8× Vitality Step, `prowess = 14`, `advantage = 1`, `knight_limit = 1`, `dread_baseline_add = 10`, `martial_per_piety_level = 1.5`, `prowess_per_piety_level = 2`, `no_prowess_loss_from_age = yes` | 8× Vitality, +30 Prowess, +4 Martial, +5 Advantage, +5 Knight Limit, +15 Dread Baseline, +1.5 Martial / +2 Prowess per Piety Level, Prowess Age-Lock |

---

## XP Gain Sources

Martial XP gains are consolidated into single, balanced increments:

1. **Battlefield Victories (`common/on_action/bm_combat_on_actions.txt`, `common/scripted_effects/bm_combat_effects.txt`):**
   - Army Commander victory: +1 to +3 Bloodlust XP (scaled by battle size: +1 for small, +2 for medium, +3 for decisive).
   - Sworn knight participation in victory: +1 to +2 Bloodlust XP.
   - Battle Defeat: +1 Bloodlust XP (survival against adversity).
2. **Duels & Single Combat (`common/on_action/bm_duel_on_actions.txt`, `events/bm_geyser_duel_events.txt`, `events/bm_seek_power_events.txt`):**
   - Fatal Single Combat kill: +3 Bloodlust XP (via `bm_combat_on_character_death_effect` / `bm_on_character_death_duel`).
   - Siphoning Duel victory: +2 Bloodlust XP.
   - Ritual Sparring victory: +2 Bloodlust XP (loss: +1 XP).
3. **Tournaments (`common/on_action/bm_duel_on_actions.txt`):**
   - Completing tournament contest: +2 Bloodlust XP.
4. **Targeted Blessings (`common/character_interactions/bm_blood_blessing.txt`):**
   - `blessing_empower` awards +5 Bloodlust XP to recipient blood mages alongside enlightenment and bloodline.
