# Fury Track (`lifestyle_blood_mage`)

Technical specification for the `fury` lifestyle track on `lifestyle_blood_mage`.

## Overview & Philosophy

The `fury` track is the martial, prowess, and battlefield mastery track of `lifestyle_blood_mage`.

Every Blood Mage also natively gains the **Worthy Commander** perk (`ignores_gender_army_rules = yes`), allowing all blood mages to lead armies regardless of realm gender laws.

---

## Track Progression & Stat Scaling

The `fury` track uses a 5-milestone progression (10, 30, 50, 70, 100 XP), providing combat command advantages and empowering sworn knights without flat attribute bloat:

| Tier (XP) | Modifiers Added at Tier (Tier II Blood Mage) | Cumulative Total Highlights |
| :--- | :--- | :--- |
| **10 XP** | Vitality Step (`+0.2` Health, `+3` Life Exp), `monthly_piety = 0.1`, `martial = 1` | +0.2 Health, +3 Life Exp, +0.1 Piety, +1 Martial |
| **30 XP** | Vitality Step (`+0.2` Health, `+3` Life Exp), `monthly_piety = 0.1`, `martial = 1`, `martial_per_piety_level = 1` | +0.4 Health, +6 Life Exp, +0.2 Piety, +2 Martial, +1 Martial per Piety Level |
| **50 XP (Milestone)** | Vitality Step (`+0.2` Health, `+3` Life Exp), `monthly_piety = 0.1`, `martial = 1`, `knight_effectiveness_per_learning = 0.01` | +0.6 Health, +9 Life Exp, +0.3 Piety, +3 Martial, +1 Martial per Piety Level, +1.0% Knight Eff / Learning |
| **70 XP** | Vitality Step (`+0.2` Health, `+3` Life Exp), `monthly_piety = 0.1`, `martial = 1`, `martial_per_piety_level = 1` | +0.8 Health, +12 Life Exp, +0.4 Piety, +4 Martial, +2 Martial per Piety Level, +1.0% Knight Eff / Learning |
| **100 XP (Capstone)** | Vitality Step (`+0.2` Health, `+3` Life Exp), `monthly_piety = 0.1`, `martial = 1`, `knight_effectiveness_per_learning = 0.01` | 5× Vitality (+1.0 Health, +15 Life Exp), +0.5 Piety, +5 Martial, +2 Martial per Piety Level, +2.0% Knight Eff / Learning |

*Note: Scaling across tiers:*
- All three ranks (`lifestyle_bm_acolyte`, `lifestyle_blood_mage`, `lifestyle_bm_archmage`) share identical Fury attribute, per-piety, piety, health, and knight-effectiveness-per-learning milestones (`+0.5` Piety, `+5` Martial, `+2` Martial per Piety Level, `+2.0%` Knight Eff per Learning, `+1.0` Health at 100 XP); Life Expectancy scales per tier (`+2` Acolyte, `+3` Mage, `+4` Archmage per step).
- **Tier II (`lifestyle_blood_mage`)** base floor adds `+3` Martial, `+1` Martial per Piety Level, and `+1.0%` Knight Eff per Learning; **Tier III (`lifestyle_bm_archmage`)** base floor adds `+6` Martial, `+2` Martial per Piety Level, and `+2.0%` Knight Eff per Learning.

---

## XP Gain Sources

Martial XP gains are consolidated into single, balanced increments:

1. **Battlefield Victories (`common/on_action/bm_combat_on_actions.txt`, `common/scripted_effects/bm_combat_effects.txt`, `common/script_values/bm_combat_values.txt`):**
   - Victory-only with a **60-day cooldown** (`bm_battle_fury_xp_cooldown`) and a **0 XP skirmish floor** (`< 500` total combatants). Battle defeats yield 0 XP.
   - Base `+1` Fury XP for participating knights, `+1` extra for commanders, and `+1` extra when total combatants exceed `10,000` (Commander: `+2` for `500-10,000`, `+3` for `> 10,000`; Knight: `+1` for `500-10,000`, `+2` for `> 10,000`).
2. **Duels & Single Combat (`common/on_action/bm_duel_on_actions.txt`, `events/bm_prisoner_blood_duel_events.txt`, `events/bm_seek_power_events.txt`, `events/bm_ritual_spar_events.txt`):**
   - Standard duels (Fatal Single Combat kill, Prisoner Blood Pit Duel, Blood Hunt single combat): `+2` Fury XP on victory, `+1` Fury XP on defeat.
   - Blood Sparring Ring (`bm_ritual_spar_events.0002`): `+1` Fury XP on victory, `0` on defeat.
3. **Tournaments (`common/on_action/bm_duel_on_actions.txt`):**
   - Completing tournament contest: +2 Fury XP.
4. **Targeted Blessings (`common/character_interactions/bm_blood_blessing.txt`):**
   - `blessing_empower` awards +5 Fury XP to recipient blood mages alongside wisdom and bloodline.
