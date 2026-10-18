# Blood Mage Dynasty

Living technical specification for supernatural dynasty/house modifiers, covenants, surges, and the Blood Golem cadet house.

## Executive Summary

- **What:** Decoupled, multi-tiered House Covenant system accessed via the standalone inline widget decision `bm_empower_bloodline_decision` ("Empower Dynasty Bloodline").
- **7 House Covenants (3 Tiers Each):** Progresses across Tier I (Awakened), Tier II (Ascendant), and Tier III (Sovereign). Upgrading replaces the lower tier modifier on `house` to keep the character and house interface clean.
  - **Tier I:** 150 Piety + 1 Minor Lifeforce (`blood_magic_used_minor`), Devotion $\ge 1$. Grants `+3` `bloodline` / `vanguard` XP.
  - **Tier II:** 350 Piety + 1 Major Lifeforce (`blood_magic_used_major`), Devotion $\ge 2$. Grants `+5` `bloodline` / `vanguard` XP.
  - **Tier III:** 750 Piety + 1 Superior Lifeforce (`blood_magic_used_superior`), Devotion $\ge 3$. Grants `+10` `bloodline` / `vanguard` XP.
- **Cooldown:** No decision cooldown (gated purely by Lifeforce, Piety, and Devotion rank).
- **Feedback Loop:** Yearly pulse event `blood_mage_yearly_events.002` grants `+1` `bloodline` XP (Blood Mages) or `+1` `vanguard` XP (Blood Knights) based on active House Covenants:
  - Each Tier I Covenant adds `+3%` chance.
  - Each Tier II Covenant adds `+6%` chance.
  - Each Tier III Covenant adds `+10%` chance (up to a `70%` annual cap with all 7 Covenants perfected).

---

## 7 Three-Tier House Covenants Table

Modifiers apply to all living and future members of the caster's house (landless adventurers, estate administrators, courtiers, knights, and landed rulers alike):

| Covenant | Key (`_1` / `_2` / `_3`) | Icon | Tier I (Awakened) | Tier II (Ascendant) | Tier III (Sovereign) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Majesty** | `dynasty_blood_charisma_modifier_*` | `presence.dds` | `+1` Diplomacy, `+5` Gen/Attr/Dyn Opinion, `+0.25` Prestige/mo, `+5%` Renown, `+5` Personal Scheme Success | `+2` Diplomacy, `+10` Gen/Attr/Dyn Opinion, `+0.50` Prestige/mo, `+10%` Renown, `+10` Personal Scheme Success, `-5`d Scheme Phase | `+4` Diplomacy, `+15` Gen/Dyn Opinion, `+20` Attr Opinion, `+1.0` Prestige/mo, `+15%` Renown, `+15` Personal Scheme Success, `-10`d Scheme Phase, **`+1` Max Personal Schemes** |
| **Warband** | `dynasty_blood_fury_modifier_*` | `vanguard.dds` | `+1` Martial, `+2` Prowess, `+10%` Knight Eff, `+1` Knight Limit, `+10%` Travel Speed, `+5` Travel Safety | `+2` Martial, `+4` Prowess, `+20%` Knight Eff, `+1` Knight Limit, `+15%` Travel Speed, `+10` Travel Safety, `+5%` Army Speed, `+2` Advantage | `+4` Martial, `+6` Prowess, `+30%` Knight Eff, `+2` Knight Limit, `+20%` Travel Speed, `+15` Travel Safety, `+10%` Army Speed, `+4` Advantage, **`+1` MaA Regiment Size** |
| **Prosperity** | `dynasty_blood_prosperity_modifier_*` | `prosperity.dds` | `+1` Stewardship, `+0.3` Gold/mo, `+5%` Income Mult, `-5%` MaA Upkeep, `-5%` Domicile & Holding Build Cost | `+2` Stewardship, `+0.6` Gold/mo, `+10%` Income Mult, `-10%` MaA Upkeep, `-10%` Domicile & Holding Build Cost/Speed, `+10%` Dev Growth | `+4` Stewardship, `+1.2` Gold/mo, `+15%` Income Mult, `-15%` MaA Upkeep, `-15%` Domicile & Holding Build Cost/Speed, `+20%` Dev Growth, **`+1` Domain Limit** |
| **Shadows** | `dynasty_blood_shadows_modifier_*` | `shadows.dds` | `+1` Intrigue, `+5` Hostile Scheme Success, `-5`d Scheme Phase, `+5` Secrecy, `-5` Enemy Scheme Success, `+5`d Enemy Phase, `+5` Dread | `+2` Intrigue, `+10` Hostile Scheme Success, `-10`d Scheme Phase, `+10` Secrecy, `-10` Enemy Scheme Success, `+10`d Enemy Phase, `-10%` Enemy Max Scheme Success Cap, `+10` Dread | `+4` Intrigue, `+15` Hostile Scheme Success, `-15`d Scheme Phase, `+15` Secrecy, `-15` Enemy Scheme Success, `+15`d Enemy Phase, `-20%` Enemy Max Scheme Success Cap, `+15` Dread, **`+1` Max Hostile Schemes** |
| **Insight** | `dynasty_blood_insight_modifier_*` | `enlightenment.dds` | `+1` Learning, `+0.25` Piety/mo, `+5%` Piety Mult, `-5%` Stress Gain, `+5%` Stress Loss, `+5%` Cultural Head Acceptance | `+2` Learning, `+0.50` Piety/mo, `+10%` Piety Mult, `-10%` Stress Gain, `+10%` Stress Loss, `+10%` Cultural Head Acceptance, `+10` Devotion Impact | `+4` Learning, `+1.0` Piety/mo, `+20%` Piety Mult, `-15%` Stress Gain, `+15%` Stress Loss, `+15%` Cultural Head Acceptance, `+20%` Devotion Impact, **`+1` Learning per Devotion Level** |
| **Legacy** | `dynasty_blood_legacy_modifier_*` | `dynasty.dds` | `+0.25` Health, `+3` Life Exp, `+3` Fertile Yrs, `+10%` Fertility, `+10%` Pos Congenital, `+10%` Inactive Inh, `+10%` Strengthen Congenital, `-15%` Inbreeding & Neg Traits, `+3` Epidemic Res | `+0.50` Health, `+6` Life Exp, `+6` Fertile Yrs, `+20%` Fertility, `+20%` Pos Congenital, `+20%` Inactive Inh, `+20%` Strengthen Congenital, `-30%` Inbreeding & Neg Traits, `+6` Epidemic Res | `+1.0` Health, `+12` Life Exp, `+12` Fertile Yrs, `+30%` Fertility, `+35%` Pos Congenital, `+35%` Inactive Inh, `+35%` Strengthen Congenital, **`-50%` Inbreeding & Neg Traits**, `+10` Epidemic Res |
| **Expertise** | `dynasty_blood_expertise_modifier_*` | `mastery.dds` | `+10%` Lifestyle XP, `-10`d Learn Language Phase, `+1` Language Slot | `+20%` Lifestyle XP, `-20`d Learn Language Phase, `+2` Language Slots, `+10%` Fame Impact | `+30%` Lifestyle XP, `-30`d Learn Language Phase, `+3` Language Slots, `+20%` Fame Impact, **Ignore Negative Culture Opinion** |

---

## Where the details live

| Concept | File |
| :--- | :--- |
| Golem house | `common/dynasty_houses/bm_dynasty_houses.txt` |
| Golem dynasty | `common/dynasties/bm_dynasties.txt` |
| Golem house coat of arms | `common/coat_of_arms/coat_of_arms/bm_coat_of_arms.txt` |
| Bloodline house modifiers (Tiers 1–3) | `common/modifiers/bm_channel_dynasty_modifiers.txt` |
| Standalone widget decision | `common/decisions/cast_magic/bm_empower_bloodline_decision.txt` |
| Covenant upgrade scripted effects | `common/scripted_effects/bm_empower_bloodline_effects.txt` |
| Yearly bloodline XP event | `blood_mage_yearly_events.002` in `events/bm_yearly_events.txt` |
| Golem template | `blood_golem_template` in `common/scripted_character_templates/bm_character_templates.txt` |
| Golem & dynasty rosters | `bm_refresh_blood_magic_rosters_effect` in `common/scripted_effects/bm_blood_mage_story_list_effects.txt` |
| Panel entry for the decision | `common/story_cycles/bm_blood_mage_story.txt` |
| Names, mottos, modifier text | `localization/english/bm_channel_lifeforce_l_english.yml`, `bm_modifiers_l_english.yml`, `bm_blood_golem_l_english.yml` |
