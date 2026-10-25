# Blood Mage Dynasty

Living technical specification for supernatural house modifiers, covenants, heir succession legacy, and Blood Golem dynasty mechanics.

## Overview

House Covenant system accessed via `bm_empower_bloodline_decision` ("Empower Dynasty Bloodline").
- **7 House Covenants (3 Tiers Each):** Tier I (150 Piety + Minor LF, Devotion 1+, `+3` XP), Tier II (350 Piety + Major LF, Devotion 2+, `+5` XP), Tier III (750 Piety + Superior LF, Devotion 3+, `+10` XP). Awards `bloodline` (Mages) or `benediction` (Knights) XP. 1-year decision cooldown.
- **Feedback Loop:** Yearly pulse `blood_mage_yearly_events.002` grants `+1` XP (`bloodline` for Mages, `benediction` for Knights) based on active covenants: Tier I adds `+3%`, Tier II adds `+6%`, Tier III adds `+10%` chance (up to 70% cap with all 7 covenants at Tier III).

## 7 Three-Tier House Covenants Table

Modifiers apply to all living and future members of the caster's house (landless adventurers, estate administrators, courtiers, knights, and landed rulers alike):

| Covenant | Key (`_1` / `_2` / `_3`) | Modifier Icon (`modifiers/`) | Tier I (Minor) | Tier II (Major) | Tier III (Superior) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Majesty** | `dynasty_blood_charisma_modifier_*` | `bm_covenant_majesty.dds` | `+1` Diplomacy, `+5` Gen/Attr/Dyn Opinion, `+0.25` Prestige/mo, `+5%` Renown, `+5` Personal Scheme Success | `+2` Diplomacy, `+10` Gen/Attr/Dyn Opinion, `+0.50` Prestige/mo, `+10%` Renown, `+10` Personal Scheme Success, `-5`d Scheme Phase | `+4` Diplomacy, `+15` Gen/Dyn Opinion, `+20` Attr Opinion, `+1.0` Prestige/mo, `+15%` Renown, `+15` Personal Scheme Success, `-10`d Scheme Phase, **`+1` Max Personal Schemes** |
| **Warband** | `dynasty_blood_fury_modifier_*` | `bm_covenant_warband.dds` | `+1` Martial, `+2` Prowess, `+10%` Knight Eff, `+1` Knight Limit, `+10%` Travel Speed, `+5` Travel Safety | `+2` Martial, `+4` Prowess, `+20%` Knight Eff, `+1` Knight Limit, `+15%` Travel Speed, `+10` Travel Safety, `+5%` Army Speed, `+2` Advantage | `+4` Martial, `+6` Prowess, `+30%` Knight Eff, `+2` Knight Limit, `+20%` Travel Speed, `+15` Travel Safety, `+10%` Army Speed, `+4` Advantage, **`+1` MaA Regiment Size** |
| **Prosperity** | `dynasty_blood_prosperity_modifier_*` | `bm_covenant_prosperity.dds` | `+1` Stewardship, `+0.3` Gold/mo, `+5%` Income Mult, `-5%` MaA Upkeep, `-5%` Domicile & Holding Build Cost | `+2` Stewardship, `+0.6` Gold/mo, `+10%` Income Mult, `-10%` MaA Upkeep, `-10%` Domicile & Holding Build Cost/Speed, `+10%` Dev Growth | `+4` Stewardship, `+1.2` Gold/mo, `+15%` Income Mult, `-15%` MaA Upkeep, `-15%` Domicile & Holding Build Cost/Speed, `+20%` Dev Growth, **`+1` Domain Limit** |
| **Shadow** | `dynasty_blood_shadows_modifier_*` | `bm_covenant_shadow.dds` | `+1` Intrigue, `+5` Hostile Scheme Success, `-5`d Scheme Phase, `+5` Secrecy, `-5` Enemy Scheme Success, `+5`d Enemy Phase, `+5` Dread | `+2` Intrigue, `+10` Hostile Scheme Success, `-10`d Scheme Phase, `+10` Secrecy, `-10` Enemy Scheme Success, `+10`d Enemy Phase, `-10%` Enemy Max Scheme Success Cap, `+10` Dread | `+4` Intrigue, `+15` Hostile Scheme Success, `-15`d Scheme Phase, `+15` Secrecy, `-15` Enemy Scheme Success, `+15`d Enemy Phase, `-20%` Enemy Max Scheme Success Cap, `+15` Dread, **`+1` Max Hostile Schemes** |
| **Insight** | `dynasty_blood_insight_modifier_*` | `bm_covenant_insight.dds` | `+1` Learning, `+0.25` Piety/mo, `+5%` Piety Mult, `-5%` Stress Gain, `+5%` Stress Loss, `+5%` Cultural Head Acceptance | `+2` Learning, `+0.50` Piety/mo, `+10%` Piety Mult, `-10%` Stress Gain, `+10%` Stress Loss, `+10%` Cultural Head Acceptance, `+10` Devotion Impact | `+4` Learning, `+1.0` Piety/mo, `+20%` Piety Mult, `-15%` Stress Gain, `+15%` Stress Loss, `+15%` Cultural Head Acceptance, `+20%` Devotion Impact, **`+1` Learning per Devotion Level** |
| **Legacy** | `dynasty_blood_legacy_modifier_*` | `bm_covenant_legacy.dds` | `+0.25` Health, `+3` Life Exp, `+3` Fertile Yrs, `+10%` Fertility, `+10%` Pos Congenital, `+10%` Inactive Inh, `+10%` Strengthen Congenital, `-15%` Inbreeding & Neg Traits, `+3` Epidemic Res | `+0.50` Health, `+6` Life Exp, `+6` Fertile Yrs, `+20%` Fertility, `+20%` Pos Congenital, `+20%` Inactive Inh, `+20%` Strengthen Congenital, `-30%` Inbreeding & Neg Traits, `+6` Epidemic Res | `+1.0` Health, `+12` Life Exp, `+12` Fertile Yrs, `+30%` Fertility, `+35%` Pos Congenital, `+35%` Inactive Inh, `+35%` Strengthen Congenital, **`-50%` Inbreeding & Neg Traits**, `+10` Epidemic Res |
| **Mastery** | `dynasty_blood_expertise_modifier_*` | `bm_covenant_mastery.dds` | `+10%` Lifestyle XP, `-10`d Learn Language Phase, `+1` Language Slot | `+20%` Lifestyle XP, `-20`d Learn Language Phase, `+2` Language Slots, `+10%` Fame Impact | `+30%` Lifestyle XP, `-30`d Learn Language Phase, `+3` Language Slots, `+20%` Fame Impact, **Ignore Negative Culture Opinion** |

---

## Heir Anointment & Succession Legacy

- **Anoint Heir (`bm_anoint_heir_interaction`):**
  - **Prerequisites:** Actor has `lifestyle_blood_mage` or `lifestyle_blood_knight`. Target is living `primary_heir` or `child` and does not already have `bm_anointed_heir_modifier` (hidden once anointed).
  - **Cost:** 250 Piety + 1 Major Lifeforce (`blood_magic_used_major`).
  - **Effect:** Strips `bm_anointed_heir_modifier` from any other child or previous heir. Applies permanent `bm_anointed_heir_modifier` (`+1.0` Health, `+15` Dynasty Opinion, `+25%` Monthly Lifestyle XP, `-35%` Short Reign Duration) to recipient, `+30` Opinion, and `+2` `bloodline` XP (Mage) / `+2` `benediction` XP (Knight).
- **Bless Blood (`bm_bless_bloodline_interaction`):**
  - **Prerequisites:** Actor has `lifestyle_blood_mage` or `lifestyle_blood_knight`. Target is a `child`, `dynasty` member, sworn `knight`, or `lifestyle_blood_knight` courtier. Hidden once target has all applicable blessings.
  - **Cost:** 35 Piety (50 Piety for Feingur) + 1 Minor Lifeforce (`bloodline_magic_cast_effect_minor`).
  - **Options (`send_options_exclusive = yes`):**
    1. **Blood of the Sovereign (`bm_blessed_blood_sovereign_modifier`):** 10 yrs, `+2` Diplomacy, `+2` Stewardship, `+10` Vassal Opinion, `-25%` Short Reign Duration, `+1.0` Health (children & dynasty).
    2. **Blood of Iron (`bm_blessed_blood_iron_modifier`):** 10 yrs, `+2` Martial, `+4` Prowess, `+25%` Knight Effectiveness, `+1.0` Health, `+0.50` Health Penalty Negation (children, dynasty, sworn knights, and Blood Knight courtiers).
    3. **Sanguine Crucible (`bm_blessed_blood_crucible_modifier`):** 10 yrs, `+25%` Fertility, `+25%` Positive Genetic Chance, `-25%` Stress Gain, `+1.0` Health (children & dynasty).
    4. **Feingur's Eternal Blessing (`bm_feingur_blessed_blood_modifier`):** Permanent `+25%` Fertility, `+20%` Positive Genetic Chance, `+0.50` Health, `+5` Life Expectancy (children & dynasty when caster has Superior **Feingur** stave).
- **Succession Legacy Awakening (`bm_transfer_anointed_heir_legacy_effect`):**
  - Triggered via `on_death` / `on_character_death` when a Blood Mage or Blood Knight ruler dies with an anointed heir:
    1. **Class Awakening:** If the heir lacks both `lifestyle_blood_mage` and `lifestyle_blood_knight`, awakens the parent's class trait via `bm_become_blood_mage_effect` or `bm_become_blood_knight_effect`.
    2. **Lifeforce Inheritance:** Inherits 1 stack of each Lifeforce tier held by the dying ruler at death (Minor $\rightarrow$ Minor, Major $\rightarrow$ Major, Superior $\rightarrow$ Superior), followed by recalculation.
    3. **25% Track XP Transfer:** Heir inherits 25% of the dying ruler's XP across all active tracks: `ancient`, `enlightenment`, `benediction`, `bloodline` / `vanguard`, `hematurgy` / `slaughter`, and all five `lifestyle_blood_power` tracks (`dynasty`, `mastery`, `presence`, `prosperity`, `shadows`).

---

## House Head Blood Tithe

- **Interaction (`bm_demand_blood_tithe_interaction`):**
  - **Prerequisites:** Actor is House Head with `lifestyle_blood_mage` or `lifestyle_blood_knight`. Target is an adult living house member (`house ?= scope:actor.house`, not actor, without `recently_lifedrained_modifier`).
  - **Cost & Cooldown:** 50 Piety, 2-year interaction cooldown.
  - **Effect:**
    - Caster gains **1 Major Lifeforce** (if target is a Blood Mage or Blood Knight) or **1 Minor Lifeforce** (if target is mundane kin), along with `+2` `bloodline` (Mage) / `+2` `vanguard` (Knight) XP.
    - Recipient receives `recently_lifedrained_modifier` and 1-year `lifeforce_modifier_negative_minor`.
    - Recipient suffers `-25` Opinion (`magic_opinion_negative`), which is waived if the recipient follows a Blood Cult faith (`bm_is_blood_cult_faith_trigger = yes`) or has the `loyal` trait.

---

## Where the details live

| Concept | File |
| :--- | :--- |
| Golem house | `common/dynasty_houses/bm_dynasty_houses.txt` |
| Golem dynasty | `common/dynasties/bm_dynasties.txt` |
| Golem house coat of arms | `common/coat_of_arms/coat_of_arms/bm_coat_of_arms.txt` |
| Bloodline house modifiers (Tiers 1–3) | `common/modifiers/bm_channel_dynasty_modifiers.txt` |
| Dynasty rites & heir modifiers | `common/modifiers/bm_dynasty_rites_modifiers.txt` |
| Standalone widget decision | `common/decisions/cast_magic/bm_empower_bloodline_decision.txt` |
| Covenant upgrade scripted effects | `common/scripted_effects/bm_empower_bloodline_effects.txt` |
| Heir succession transfer effect | `common/scripted_effects/bm_heir_succession_effects.txt` |
| Heir succession transfer values | `common/script_values/bm_heir_succession_values.txt` |
| Dynasty death on_actions | `common/on_action/bm_dynasty_on_actions.txt` |
| Dynasty interactions (Anoint Heir, Tithe) | `common/character_interactions/bm_dynasty_interactions.txt` |
| 3-Way Bless Bloodline interaction | `common/character_interactions/bm_bless_bloodline.txt` |
| Yearly bloodline XP event | `blood_mage_yearly_events.002` in `events/bm_yearly_events.txt` |
| Golem template | `blood_golem_template` in `common/scripted_character_templates/bm_character_templates.txt` |
| Golem & dynasty rosters | `bm_refresh_blood_magic_rosters_effect` in `common/scripted_effects/bm_blood_mage_story_list_effects.txt` |
| Panel entry for the decision | `common/story_cycles/bm_blood_mage_story.txt` |
| Names, mottos, modifier text | `localization/english/bm_channel_lifeforce_l_english.yml`, `bm_dynasty_rites_l_english.yml`, `bm_modifiers_l_english.yml`, `bm_blood_golem_l_english.yml` |

