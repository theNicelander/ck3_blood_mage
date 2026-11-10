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
| **10 XP** | Vitality Step (`+0.2` Health, `+4` Life Exp), `knight_limit = 1`, `army_damage_mult = 0.05` | +0.2 Health, +4 Life Exp, +1 Knight Limit, +5% Army Damage |
| **30 XP** | Vitality Step (`+0.2` Health, `+4` Life Exp), `knight_limit = 1`, `army_damage_mult = 0.05` | +0.4 Health, +8 Life Exp, +2 Knight Limit, +10% Army Damage |
| **50 XP (Milestone)** | `knight_limit = 1`, `martial_per_piety_level = 1`, `prowess_per_piety_level = 1` | 2× Vitality, +3 Knight Limit, +10% Army Damage, +1 Martial & Prowess per Piety Level |
| **70 XP** | Vitality Step (`+0.2` Health, `+4` Life Exp), `knight_limit = 1`, `army_damage_mult = 0.05` | +0.6 Health, +12 Life Exp, +4 Knight Limit, +15% Army Damage, +1 Martial & Prowess per Piety Level |
| **100 XP (Capstone)** | Vitality Step (`+0.2` Health, `+4` Life Exp), `knight_limit = 1`, `army_damage_mult = 0.05`, `martial_per_piety_level = 1`, `prowess_per_piety_level = 1` | 4× Vitality (+0.8 Health, +16 Life Exp), +5 Knight Limit, +20% Army Damage, +2 Martial & Prowess per Piety Level |

*Note: Scaling across tiers:*
- **Tier I: Blood Acolyte (`lifestyle_bm_acolyte`)**: +1 Knight Limit at all 5 milestones (+5 Knights total), +3% Army Damage per step (+12% total), +1 Martial & Prowess per Piety Level at 50 XP and 100 XP (+2 each total), Age Prowess Lock at 100 XP.
- **Tier II: Blood Mage (`lifestyle_blood_mage`)**: Base trait includes +3 Knight Limit; +1 Knight Limit at all 5 milestones (+5 Knights, +8 combined total), +5% Army Damage per step (+20% total), +1 Martial & Prowess per Piety Level at 50 XP and 100 XP (+2 each total, plus innate +1 base trait floor).
- **Tier III: Blood Archmage (`lifestyle_bm_archmage`)**: Base trait includes +6 Knight Limit; +1 Knight Limit at all 5 milestones (+5 Knights, +11 combined total), +8% Army Damage per step (+32% total), +2 Martial & Prowess per Piety Level at 50 XP and 100 XP (+4 each total, plus innate +2 base trait floor).

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
