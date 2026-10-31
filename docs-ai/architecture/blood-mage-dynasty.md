# Blood Mage Dynasty

Living technical specification for supernatural house modifiers, covenants, heir succession legacy, and Blood Golem dynasty mechanics.

## Overview

House Covenant system accessed via `bm_empower_bloodline_decision` ("Empower Dynasty Bloodline").
- **6 House Covenants (3 Tiers Each):** Tier I (150 Piety + Minor LF, Devotion 1+, `+1` XP), Tier II (350 Piety + Major LF, Devotion 2+, `+2` XP), Tier III (750 Piety + Superior LF, Devotion 3+, `+3` XP). Awards `bloodline` (Mages) or `benediction` (Knights) XP. 1-year decision cooldown.
- **Universal Piety Baseline:** Every Covenant grants **+0.1 / +0.3 / +0.5 Monthly Piety** across Tiers 1 / 2 / 3 (up to **+3.0 Monthly Piety** when all 6 Covenants are at Tier 3).
- **1:1 Devotion Scaling:** Every Covenant grants **+1 [Stat] per Devotion Level** at Tier 3 (Superior).
- **Feedback Loop:** Yearly pulse `blood_mage_yearly_events.002` rolls independently for each active covenant per living Blood Mage / Knight in the House to grant `+1` XP in the matching `lifestyle_blood_power` track (Tier I: 50%, Tier II: 67%, Tier III: 100%), capped at 100 XP.

## 6 Three-Tier House Covenants Table

Modifers apply to all living and future members of the caster's house (landless adventurers, estate administrators, courtiers, knights, and landed rulers alike):

| Covenant | Key (`_1` / `_2` / `_3`) | Modifier Icon (`modifiers/`) | Tier I (Minor) | Tier II (Major) | Tier III (Superior) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Majesty** | `dynasty_blood_majesty_modifier_*` | `bm_covenant_majesty.dds` | `+0.1` Piety/mo, `+1` Diplomacy, `+2` Gen/Dyn Opinion, `+5` Personal Scheme Success | `+0.3` Piety/mo, `+2` Diplomacy, `+5` Gen/Dyn Opinion, `+10` Personal Scheme Success, `-10%` Short Reign, `+10%` Long Reign | `+0.5` Piety/mo, `+4` Diplomacy, `+10` Gen/Dyn Opinion, `+20` Personal Scheme Success, `-20%` Short Reign, `+20%` Long Reign, **`+1` Diplomacy per Devotion**, **`+1` Max Personal Schemes** |
| **Warband** | `dynasty_blood_warband_modifier_*` | `bm_covenant_warband.dds` | `+0.1` Piety/mo, `+1` Martial, `+1` Prowess, `+5%` Knight Eff, `+5` Dread Baseline | `+0.3` Piety/mo, `+2` Martial, `+2` Prowess, `+2` Knight Limit, `+10%` Knight Eff, `+2` Advantage, `+10` Dread Baseline | `+0.5` Piety/mo, `+4` Martial, `+4` Prowess, `+3` Knight Limit, `+20%` Knight Eff, `+4` Advantage, `+15` Dread Baseline, **`+1` Martial per Devotion**, **`+1` MaA Regiment Size** |
| **Prosperity** | `dynasty_blood_prosperity_modifier_*` | `bm_covenant_prosperity.dds` | `+0.1` Piety/mo, `+0.1` Gold/mo, `+1` Stewardship, `+3%` Income Mult, `-3%` Domicile & Holding Build Cost | `+0.3` Piety/mo, `+0.3` Gold/mo, `+2` Stewardship, `+6%` Income Mult, `-6%` Domicile & Holding Build Cost, `-6%` MaA Upkeep, `+5%` Dev Growth | `+0.5` Piety/mo, `+0.5` Gold/mo, `+4` Stewardship, `+12%` Income Mult, `-12%` Domicile & Holding Build Cost, `-12%` MaA Upkeep, `+10%` Dev Growth, **`+1` Stewardship per Devotion**, **`+1` Domain Limit** |
| **Shadow** | `dynasty_blood_shadows_modifier_*` | `bm_covenant_shadow.dds` | `+0.1` Piety/mo, `+1` Intrigue, `+3` Hostile Scheme Success, `-3` Enemy Hostile Success | `+0.3` Piety/mo, `+2` Intrigue, `+6` Hostile Scheme Success, `-6` Enemy Hostile Success, `+6` Scheme Secrecy, `+5` Dread Baseline, `-5` Enemy Max Success Cap | `+0.5` Piety/mo, `+4` Intrigue, `+12` Hostile Scheme Success, `-12` Enemy Hostile Success, `+12` Scheme Secrecy, `+10` Dread Baseline, `-10` Enemy Max Success Cap, **`+1` Intrigue per Devotion**, **`+1` Max Hostile Schemes** |
| **Mastery** | `dynasty_blood_mastery_modifier_*` | `bm_covenant_mastery.dds` | `+0.1` Piety/mo, `+1` Learning, `+5%` Lifestyle XP, `-5%` Stress Gain | `+0.3` Piety/mo, `+2` Learning, `+10%` Lifestyle XP, `-10%` Stress Gain, `+10%` Piety Mult, `+2` Language Slots | `+0.5` Piety/mo, `+4` Learning, `+20%` Lifestyle XP, `-20%` Stress Gain, `+20%` Piety Mult, `+3` Language Slots, **`+1` Learning per Devotion**, **Ignore Negative Culture Opinion** |
| **Legacy** | `dynasty_blood_legacy_modifier_*` | `bm_covenant_legacy.dds` | `+0.1` Piety/mo, `+0.2` Health, `+2` Life Exp, `+2` Fertile Yrs, `+5%` Fertility | `+0.3` Piety/mo, `+0.4` Health, `+5` Life Exp, `+5` Fertile Yrs, `+10%` Fertility, `+10%` Pos Congenital & Strengthen, `-20%` Inbreeding Chance | `+0.5` Piety/mo, `+0.8` Health, `+10` Life Exp, `+10` Fertile Yrs, `+20%` Fertility, `+20%` Pos Congenital & Strengthen, **`-40%` Inbreeding Chance**, **`+1` Prowess per Devotion** |

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
    3. **25% Track XP Transfer:** Heir inherits 25% of the dying ruler's XP across all active tracks: `ancient`, `enlightenment`, `benediction`, `bloodline` / `vanguard`, `hematurgy` / `slaughter`, and all six `lifestyle_blood_power` tracks (`dynasty`, `warband`, `mastery`, `presence`, `prosperity`, `shadows`).

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
