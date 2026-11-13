# Bloodlust Track (`lifestyle_blood_mage`)

Technical specification for the `bloodlust` lifestyle track on `lifestyle_blood_mage`.

## Overview & Philosophy

The `bloodlust` track is the martial, prowess, and battlefield mastery track of `lifestyle_blood_mage`.

Every Blood Mage also natively gains the **Worthy Commander** perk (`ignores_gender_army_rules = yes`), allowing all blood mages to lead armies regardless of realm gender laws.

---

## Track Progression & Stat Scaling

The `bloodlust` track uses a 5-milestone progression (10, 30, 50, 70, 100 XP), providing combat command advantages and empowering sworn knights without flat attribute bloat:

| Tier (XP) | Modifiers Added at Tier (Tier II Blood Mage) | Cumulative Total Highlights |
| :--- | :--- | :--- |
| **10 XP** | Vitality Step (`+0.2` Health, `+4` Life Exp), `martial = 1` | +0.2 Health, +4 Life Exp, +1 Martial |
| **30 XP** | Vitality Step (`+0.2` Health, `+4` Life Exp), `martial = 1`, `martial_per_piety_level = 1` | +0.4 Health, +8 Life Exp, +2 Martial, +1 Martial per Piety Level |
| **50 XP (Milestone)** | `martial = 1`, `monthly_piety_gain_per_knight_add = 0.02` | +0.4 Health, +8 Life Exp, +3 Martial, +1 Martial per Piety Level, +0.02 Monthly Piety per Knight |
| **70 XP** | Vitality Step (`+0.2` Health, `+4` Life Exp), `martial = 1`, `martial_per_piety_level = 1` | +0.6 Health, +12 Life Exp, +4 Martial, +2 Martial per Piety Level, +0.02 Monthly Piety per Knight |
| **100 XP (Capstone)** | Vitality Step (`+0.2` Health, `+4` Life Exp), `martial = 1`, `monthly_piety_gain_per_knight_add = 0.02` | 4× Vitality (+0.8 Health, +16 Life Exp), +5 Martial, +2 Martial per Piety Level, +0.04 Monthly Piety per Knight |

*Note: Scaling across tiers:*
- All three ranks (`lifestyle_bm_acolyte`, `lifestyle_blood_mage`, `lifestyle_bm_archmage`) share identical Bloodlust track milestones (`+5` Martial, `+2` Martial per Piety Level, `+0.04` Monthly Piety per Knight, `+0.8` Health, `+16` Life Expectancy at 100 XP).
- **Tier II (`lifestyle_blood_mage`)** base floor adds `+3` Martial, `+1` Martial per Piety Level, and `+0.02` Monthly Piety per Knight; **Tier III (`lifestyle_bm_archmage`)** base floor adds `+6` Martial, `+2` Martial per Piety Level, and `+0.04` Monthly Piety per Knight.

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
