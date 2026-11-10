# Bloodlust Track (`lifestyle_blood_mage`)

Technical specification for the `bloodlust` lifestyle track on `lifestyle_blood_mage`.

## Overview & Philosophy

The `bloodlust` track is the martial, prowess, and battlefield mastery track of `lifestyle_blood_mage`.

Every Blood Mage also natively gains the **Worthy Commander** perk (`ignores_gender_army_rules = yes`), allowing all blood mages to lead armies regardless of realm gender laws.

---

## Track Progression & Stat Scaling

The `bloodlust` track uses the standard 10-tier progression (10 to 100 XP in increments of 10), providing combat command advantages and empowering sworn knights without flat attribute bloat:

| Tier (XP) | Modifiers Added at Tier (Tier II Blood Mage) | Cumulative Total Highlights |
| :--- | :--- | :--- |
| **10 XP** | Vitality Step, `advantage = 1.5`, `knight_effectiveness_mult = 0.10` | +0.1 Health, +2.5 Life Exp, +1.5 Advantage, +10% Knight Eff |
| **20 XP** | Vitality Step, `advantage = 1.5`, `knight_effectiveness_mult = 0.10`, `knight_limit = 1` | +0.2 Health, +5 Life Exp, +3 Advantage, +20% Knight Eff, +1 Knight Limit |
| **30 XP** | Vitality Step, `advantage = 1.5`, `knight_effectiveness_mult = 0.10` | +0.3 Health, +7.5 Life Exp, +4.5 Advantage, +30% Knight Eff, +1 Knight Limit |
| **40 XP** | Vitality Step, `advantage = 1.5`, `knight_effectiveness_mult = 0.10`, `knight_limit = 1` | +0.4 Health, +10 Life Exp, +6 Advantage, +40% Knight Eff, +2 Knight Limit |
| **50 XP (Milestone)** | `martial_per_piety_level = 1`, `prowess_per_piety_level = 1` | 4× Vitality, +6 Advantage, +40% Knight Eff, +2 Knight Limit, +1 Martial & Prowess per Piety Level |
| **60 XP** | Vitality Step, `advantage = 1.5`, `knight_effectiveness_mult = 0.10`, `knight_limit = 1` | +0.5 Health, +12.5 Life Exp, +7.5 Advantage, +50% Knight Eff, +3 Knight Limit |
| **70 XP** | Vitality Step, `advantage = 1.5`, `knight_effectiveness_mult = 0.10` | +0.6 Health, +15 Life Exp, +9 Advantage, +60% Knight Eff, +3 Knight Limit |
| **80 XP** | Vitality Step, `advantage = 1.5`, `knight_effectiveness_mult = 0.10`, `knight_limit = 1` | +0.7 Health, +17.5 Life Exp, +10.5 Advantage, +70% Knight Eff, +4 Knight Limit |
| **90 XP** | Vitality Step, `advantage = 1.5`, `knight_effectiveness_mult = 0.10` | +0.8 Health, +20 Life Exp, +12 Advantage, +80% Knight Eff, +4 Knight Limit |
| **100 XP (Capstone)** | `martial_per_piety_level = 1`, `prowess_per_piety_level = 1` | 8× Vitality, +12 Advantage, +80% Knight Eff, +4 Knight Limit, +2 Martial & Prowess per Piety Level |

*Note: Scaling across tiers:*
- **Tier I: Blood Acolyte (`lifestyle_bm_acolyte`)**: +1 Advantage & +5% Knight Effectiveness per step (+8 Adv, +40% Knight Eff total), +1 Knight Limit on even steps (+4 Knights), +1 Martial & Prowess per Piety Level at 50 XP and 100 XP (+2 each total), Age Prowess Lock at 100 XP.
- **Tier II: Blood Mage (`lifestyle_blood_mage`)**: +1.5 Advantage & +10% Knight Effectiveness per step (+12 Adv, +80% Knight Eff total), +1 Knight Limit on even steps (+4 Knights), +1 Martial & Prowess per Piety Level at 50 XP and 100 XP (+2 each total, plus innate +1 base trait floor).
- **Tier III: Blood Archmage (`lifestyle_bm_archmage`)**: +2 Advantage & +15% Knight Effectiveness per step (+16 Adv, +120% Knight Eff total), +2 Knight Limit on even steps (+8 Knights), +2 Martial & Prowess per Piety Level at 50 XP and 100 XP (+4 each total, plus innate +2 base trait floor).

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
