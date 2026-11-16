# Blood Mage Dynasty

Living technical specification for supernatural house modifiers, covenants, heir succession legacy, and Blood Golem dynasty mechanics.

## Overview

House Covenant system accessed via `bm_empower_bloodline_decision` ("Empower Dynasty Bloodline").
- **6 House Covenants (3 Tiers Each):** Tier I (150 Piety + Minor LF, Devotion 1+, `+3` XP), Tier II (350 Piety + Major LF, Devotion 2+, `+5` XP), Tier III (750 Piety + Superior LF, Devotion 3+, `+8` XP). Awards `fortune` XP. 1-year decision cooldown.
- **1 One-Off Covenant (`Covenant of Initiation`, `dynasty_blood_acolyte_modifier`):** 350 Piety + Major LF, Devotion 5+, Blood Mage or Archmage (`+5` `fortune` XP). Grants `+1` Monthly Piety across the house and unlocks `bm_covenant_acolyte_decision` for adult uninitiated house members (`piety_level >= 3`, `250` Piety) to become Blood Mage Acolytes.
- **AI Adoption:** `bm_empower_bloodline_interaction` (`ai_frequency = 6`, `ai_targets = { ai_recipients = self }`) handles AI covenant upgrades; `bm_covenant_acolyte_decision` uses `ai_check_interval = 6`, `ai_will_do = { base = 100 }`.
- **Universal Piety & Lifespan Baseline:** Every tiered Covenant grants **+0.1 / +0.3 / +0.5 Monthly Piety** across Tiers 1 / 2 / 3 (up to **+3.0 Monthly Piety** when all 6 Covenants are at Tier 3) and **+2 / +4 / +6 Life Expectancy** (`+2 / +4 / +8` for Ancient).
- **Monthly Lifestyle XP:** Each tiered Covenant grants `+2 / +4 / +6` monthly lifestyle XP in its matching vanilla lifestyle (`+1 / +2 / +4` all-lifestyle XP for Ancient).
- **1:1 Devotion Scaling:** Every Covenant grants **+1 [Stat] per Devotion Level** at Tier 3 (Superior).
- **Feedback Loop:** Yearly pulse `blood_mage_yearly_events.002` grants yearly XP in the matching `lifestyle_blood_mage` track for each active covenant (Tier I: 50% `+1` [0.5/yr], Tier II: 100% `+1` [1/yr], Tier III: 100% `+1` + 50% `+1` [1.5/yr]), capped at 100 XP.

## 6 Three-Tier House Covenants Table

Modifiers apply to all living and future members of the caster's house (landless adventurers, estate administrators, courtiers, knights, and landed rulers alike):

| Track | Minor (Tier I) | Major (Tier II) | Superior (Tier III) |
| :--- | :--- | :--- | :--- |
| **Radiance** | `+0.1` Piety/mo, `+0.1` Prestige/mo, `+1` Diplomacy, `+5` Gen Opinion, `+5` Personal Scheme Success, `+5%` Legitimacy Mult | `+0.3` Piety/mo, `+0.3` Prestige/mo, `+2` Diplomacy, `+10` Gen Opinion, `+10` Personal Scheme Success, `+10%` Legitimacy Mult, `-10%` Short Reign, `+10%` Long Reign, **`+1` Diplomacy per Devotion** | `+0.5` Piety/mo, `+0.5` Prestige/mo, `+4` Diplomacy, `+15` Gen Opinion, `+20` Personal Scheme Success, `+15%` Legitimacy Mult, `-20%` Short Reign, `+20%` Long Reign, **`+1` Personal Tenet Slot**, **`+1` Diplomacy per Devotion** |
| **Fury** | `+0.1` Piety/mo, `+1` Martial, `+1` Prowess, `+1` Knight, `+5%` Army Damage, `+0.02` Piety/Knight, `+0.2%` Knight Eff per Prowess | `+0.3` Piety/mo, `+2` Martial, `+2` Prowess, `+2` Knights, `+10%` Army Damage, `+1` MaA Regiments & Size, `+0.04` Piety/Knight, `+0.5%` Knight Eff per Prowess, **`+1` Martial per Devotion** | `+0.5` Piety/mo, `+4` Martial, `+4` Prowess, `+3` Knights, `+15%` Army Damage, `+1` MaA Regiments & Size, `+0.06` Piety/Knight, `+1.0%` Knight Eff per Prowess, **`+1` Martial per Devotion** |
| **Bloodline** | `+0.1` Piety/mo, `+0.1` Gold/mo, `+1` Stewardship, `+5%` Income Mult, `-5%` Domicile & Holding Build Cost, `-5%` MaA Upkeep, `+5%` Dev Growth | `+0.3` Piety/mo, `+0.3` Gold/mo, `+2` Stewardship, `+10%` Income Mult, `-10%` Domicile & Holding Build Cost, `-10%` MaA Upkeep, `+10%` Dev Growth, **`+1` Stewardship per Devotion** | `+0.5` Piety/mo, `+0.5` Gold/mo, `+4` Stewardship, `+15%` Income Mult, `-15%` Domicile & Holding Build Cost, `-15%` MaA Upkeep, `+15%` Dev Growth, **`+1` Domain Limit**, **`+1` Stewardship per Devotion** |
| **Cunning** | `+0.1` Piety/mo, `+1` Intrigue, `+3` Hostile Scheme Success, `-5` Enemy Hostile Success | `+0.3` Piety/mo, `+2` Intrigue, `+6` Hostile Scheme Success, `-10` Enemy Hostile Scheme Success, `+5` Scheme Secrecy, `-5` Enemy Max Success Cap, **`+1` Intrigue per Devotion** | `+0.5` Piety/mo, `+4` Intrigue, `+12` Hostile Scheme Success, `-20` Enemy Hostile Success, `+10` Scheme Secrecy, `-10` Enemy Max Success Cap, **`+1` Intrigue per Devotion** |
| **Wisdom** | `+0.1` Piety/mo, `+1` Learning, `+5%` Lifestyle XP, `-5%` Stress Gain, `+1%` Piety/Knight Mult, `+0.2%` Knight Eff per Learning | `+0.3` Piety/mo, `+2` Learning, `+10%` Lifestyle XP, `-10%` Stress Gain, `+10%` Stress Loss, `+5%` Piety Mult, `+0.15` Health, `+2%` Piety/Knight Mult, `+0.5%` Knight Eff per Learning, **`+1` Learning per Devotion** | `+0.5` Piety/mo, `+4` Learning, `+20%` Lifestyle XP, `-20%` Stress Gain, `+20%` Stress Loss, `+10%` Piety Mult, `+0.3` Health, `+3%` Piety/Knight Mult, `+1.0%` Knight Eff per Learning, **`+1` Personal Tenet Slot**, **`+1` Learning per Devotion**, **Ignore Negative Culture Opinion** |
| **Ancient** | `+0.1` Piety/mo, `+0.15` Health, `+2` Life Exp, `+2` Fertile Yrs, `+5%` Fertility, `+5%` Pos Congenital & Strengthen | `+0.3` Piety/mo, `+0.3` Health, `+4` Life Exp, `+4` Fertile Yrs, `+15%` Fertility, `+15%` Pos Congenital & Strengthen, `-15%` Inbreeding Chance, **`+1` Prowess per Devotion** | `+0.5` Piety/mo, `+0.5` Health, `+8` Life Exp, `+8` Fertile Yrs, `+25%` Fertility, `+25%` Pos Congenital & Strengthen, **`-30%` Inbreeding Chance**, **`+1` Prowess per Devotion** |

---

## Heir Anointment & Succession Legacy

- **Anoint Heir (`bm_anoint_heir_interaction`):**
  - **Prerequisites:** Actor has `lifestyle_blood_mage`. Target is living `primary_heir` or `child` and does not already have `bm_anointed_heir_modifier` (hidden once anointed).
  - **Cost:** 250 Piety + 1 Major Lifeforce (`blood_magic_used_major`).
  - **Effect:** Strips `bm_anointed_heir_modifier` from any other child or previous heir. Applies permanent `bm_anointed_heir_modifier` (`+1.0` Health, `+15` Dynasty Opinion, `+25%` Monthly Lifestyle XP, `-35%` Short Reign Duration) to recipient, `+30` Opinion, and `+2` `fortune` XP.
- **Permanent Tiered Blood Blessings (`bm_cast_blood_blessing_interaction` & `bm_cast_blood_magic_minor_decision`):**
  - **Prerequisites:** Actor has `lifestyle_blood_mage` (any tier). Target is self, `child`, `dynasty` member, `spouse`/`consort`, sworn `knight`, `councillor`, or `liege`, and does not have the 1-year `bm_blessing_cooldown` flag.
  - **Tiers & Costs:**
    - **Minor:** `50` Piety + Devotion 1 + `1` Minor Lifeforce (`blood_magic_used_minor`), `+2` `wisdom` (self) / `radiance` (others) XP.
    - **Major:** Requires Minor blessing of that line, `150` Piety + Devotion 3 + `1` Major Lifeforce (`blood_magic_used_major`), `+4` XP. Replaces Minor.
    - **Superior:** Requires Major blessing of that line, `250` Piety + Devotion 5 + `1` Superior Lifeforce (`blood_magic_used_superior`), `+6` XP. Replaces Major.
  - **6 Lines (all stackable; max 1 tier per line, permanent, +25 Opinion on others):**
    1. **Blessing of Radiance (`bm_blessing_radiance_<tier>_modifier`):** `+1/+3/+5` Diplomacy, `+5/+10/+15` monthly Diplomacy Lifestyle XP, `+5%/+10%/+20%` monthly Lifestyle XP.
    2. **Blessing of Fortune (`bm_blessing_fortune_<tier>_modifier`):** `+1/+3/+5` Stewardship, `+5/+10/+15` monthly Stewardship Lifestyle XP, `+5%/+10%/+20%` monthly Lifestyle XP.
    3. **Blessing of Fury (`bm_blessing_fury_<tier>_modifier`):** `+1/+3/+5` Martial, `+5/+10/+15` monthly Martial Lifestyle XP, `+5%/+10%/+20%` monthly Lifestyle XP.
    4. **Blessing of Cunning (`bm_blessing_cunning_<tier>_modifier`):** `+1/+3/+5` Intrigue, `+5/+10/+15` monthly Intrigue Lifestyle XP, `+5%/+10%/+20%` monthly Lifestyle XP.
    5. **Blessing of Wisdom (`bm_blessing_wisdom_<tier>_modifier`):** `+1/+3/+5` Learning, `+5/+10/+15` monthly Learning Lifestyle XP, `+5%/+10%/+20%` monthly Lifestyle XP.
    6. **Blessing of Ancient (`bm_blessing_ancient_<tier>_modifier`):** `+5/+10/+15` all-lifestyle monthly XP, `+5%/+10%/+20%` monthly Lifestyle XP, `+5%/+15%/+25%` Fertility, `+2/+4/+8` Years of Fertility.
- **Succession Legacy Awakening (`bm_transfer_anointed_heir_legacy_effect`):**
  - Triggered via `on_death` / `on_character_death` when a Blood Mage ruler dies with an anointed heir:
    1. **Awakening:** If the heir lacks `lifestyle_blood_mage`, awakens it via `bm_become_blood_mage_effect`.
    2. **Lifeforce Inheritance:** Inherits 1 stack of each Lifeforce tier held by the dying ruler at death (Minor $\rightarrow$ Minor, Major $\rightarrow$ Major, Superior $\rightarrow$ Superior), followed by recalculation.
    3. **25% Track XP Transfer:** Heir inherits 25% of the dying ruler's XP across all active tracks: `ancient`, `wisdom`, `radiance`, `fortune`, `cunning`, `fury`.

---

## House Head Blood Tithe

- **Interaction (`bm_demand_blood_tithe_interaction`):**
  - **Prerequisites:** Actor is House Head with `lifestyle_blood_mage`. Target is an adult living house member (`house ?= scope:actor.house`, not actor, without `recently_lifedrained_modifier`).
  - **Cost & Cooldown:** 50 Piety, 2-year interaction cooldown.
  - **Effect:**
    - Caster gains **1 Major Lifeforce** (if target is a Blood Mage) or **1 Minor Lifeforce** (if target is mundane kin), along with `+2` `fortune` XP.
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
| Blood Blessing & heir modifiers | `common/modifiers/bm_blood_blessing_modifiers.txt` |
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
