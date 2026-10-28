# Blood Duels, Trait Acquisition, and Education Enhancement

Living technical specification for contested skill duels, initiation trials, ex-nihilo congenital trait manifestation, prisoner trait theft, education mastery, and mass dungeon execution.

## Overview

Contested skill duel subsystems governing how characters awaken to blood magic, manifest or steal congenital traits (up to Rank 5), ascend education traits (1★ to 5★ + secondary education), and harvest Lifeforce. Accessible to both **Blood Mages** and **Blood Knights**.

### Duels & Self-Advancement Master Table
| Ritual / Action | Interface / File | Cost & Cooldown | Requirements | Duel Skill & DC | Win Outcome | Failure Outcome |
| --- | --- | --- | --- | --- | --- | --- |
| **Geyser Initiation Duel** | `bm_blood_cultist_become_blood_mage_decision` / `bm_enhance_blood_ritual_decision` -> `bm_geyser_duel.0001` | **1 Devotion Level** (`add_piety_level = -1`) paid on duel choice. Free back-out; no CD. | Non-mage, non-knight, `piety_level >= 2`, located in Reykjavik (`b_reykjavik`) or Tsushima (`c_tsushima`). | vs. **Egill Skallagrímsson** (Learning 20 for Blood Mage; Prowess 30 for Blood Knight). | Bestows `lifestyle_blood_mage` (Learning) or `lifestyle_blood_knight` (Prowess). | Injury (strictly capped at `wounded_2`), stress, or trauma. Can retry without paying level again or back out. |
| **Manifest Trait (Ranks 1–3)** | Major Grimoire (`bm_cast_blood_magic_major.001` -> `bm_channel_manifest_traits.001`) | `250/500/750` Piety + Major Lifeforce. CD: 5 yrs (`bm_manifest_traits_cooldown`). | `piety_level >= 2/3/4` for Ranks 1/2/3, target branch below Rank 3. | Learning duel (`value = 15`) + Learning traits + XP bonus. | Steps target congenital branch (`intellect`, `physique`, `beauty`) up by 1 tier (cleanses bad or adds Rank 1–3). Advancing to Rank 3 deducts 1 Devotion Level (`add_piety_level = -1`). `+3` to `+6` `bloodline` (Mage) / `enlightenment` or `vanguard` (Knight) XP based on trait rank (Cleanse/Neutral: `+3`, Rank 1: `+4`, Rank 2: `+5`, Rank 3: `+6`). | Standard fail: refunds Minor Lifeforce. Crit fail: Minor exhaustion debuff + wound increase + 50 Stress. |
| **Manifest Apex Perfection (Ranks 4–5)** | Superior Grimoire (`bm_cast_blood_magic_superior.001` -> `bm_channel_manifest_traits.002`) | `1000/1500` Piety + Superior Lifeforce. CD: 5 yrs (`bm_manifest_traits_cooldown`). | `piety_level >= 5`, holds Rank 3–4 in target branch. | Learning duel (`value = 25`) + Learning traits + XP bonus. | Steps congenital branch up to Rank 4 or 5 (overhaul compat). Deducts 1 Devotion Level (`add_piety_level = -1`). `+7` to `+8` `bloodline` (Mage) / `enlightenment` or `vanguard` (Knight) XP based on trait rank (Rank 4: `+7`, Rank 5: `+8`). | Standard fail: refunds Major Lifeforce. Crit fail: Major exhaustion debuff + wound increase + 50 Stress. |
| **Prisoner Trait Theft (Ranks 1–5)** | Interaction `trait_drain_prisoner_event_interaction` -> `bm_trait_drain.001` | `100–325` Piety + Major Lifeforce. CD: 60d (15d with Superior Hulinhjálmur). | Prisoner has congenital trait caster lacks (`intellect`/`physique`/`beauty` 1–5, `fecund`, `giant`, `pure_blooded`). | Learning duel vs. Prisoner, scaled by trait rank penalty & total XP. | Steals congenital trait; executes prisoner (`death_lifedrain_reason`). `+2` `hematurgy` (Mage) / `+2` `slaughter` (Knight) XP. | Target survives with `trait_drain_attempted`; caster suffers Major exhaustion backlash. |
| **Improve Education (1★ -> 4★)** | Major Grimoire (`bm_cast_blood_magic_major.001` -> `bm_education_enhancement.001`) | `75–200` Piety + Major Lifeforce. CD: 2 yrs (`bm_improve_education_cooldown`). | Holds any 1★–3★ education trait. Devotion rank scaled: 1★ requires Devotion 1+, 2★ requires Devotion 2+, 3★ requires Devotion 3+. | Mental Learning duel (`bm_education_duel_effect`). | Upgrades selected education by `+1★` (up to 4★). `+5` `enlightenment` XP. No Devotion Level loss. | 3-yr Major exhaustion backlash (`+5` `enlightenment` XP still awarded on attempt). |
| **Master Education (4★ -> 5★)** | Superior Grimoire (`bm_cast_blood_magic_superior.001` -> `bm_education_master.001`) | `350` Piety + Superior Lifeforce + 1 Devotion Level. CD: 2 yrs (`bm_improve_education_cooldown`). | `piety_level >= 4`, holds a 4★ education trait. | Mental duel in matching discipline skill. | Upgrades 4★ education to legendary 5★ tier. Deducts 1 Devotion Level. `+20` total `enlightenment` XP (`+10` cast + `+10` win). | 3-yr Superior exhaustion backlash (`+10` `enlightenment` XP on attempt; crit fail loses 1 Devotion Level). |
| **Embrace New Education (2nd Trait)** | Superior Grimoire (`bm_cast_blood_magic_superior.001` -> `bm_education_new.001`) | `1000` Piety + Superior Lifeforce. CD: 2 yrs (`bm_new_education_cooldown`). | `piety_level >= 4`, holds a 5★ education and no 1★–4★ secondary education. | Uncontested self-ritual. | Grants a secondary 1★ education trait in a chosen discipline (can then be leveled to 5★). `+10` `enlightenment` XP. | None (uncontested). |
| **Single Combat Fatality** | On-action `bm_on_character_death_duel` | Passive combat hook. | Killer has `lifestyle_blood_knight`. | Vanilla Single Combat Engine (SCE) lethal kill. | `+5` `slaughter` XP (Knight) + **1 Major Lifeforce**. **25% chance of 1 Superior Lifeforce** if victim had `prowess >= 35` or blood mage/knight trait. | — |
| **Mass Lifedrain Prisoners** | Decision `mass_lifedrain_prisoners_decision` -> `bm_mass_lifedrain.001` | Piety per prisoner. No CD. | Has dungeon prisoners. | Uncontested batch execution. | Executes all prisoners (or spares those with good congenital traits), harvesting Lifeforce & `hematurgy` XP (+25g/victim with Superior Nábrókarstafur). | Applies standard vanilla tyranny & kinslaying penalties if prisoners lack execution reasons. |

---

## Detailed Subsystem Mechanics

### 1. Geyser Initiation Duel vs. Egill Skallagrímsson (`bm_geyser_duel.0001`)
- **Opponent Profile:** Historical/occult master Egill Skallagrímsson (100 years old, holds both `lifestyle_blood_mage` and `lifestyle_blood_knight`, 50 XP across all tracks, Learning 20, Martial 18, Prowess 30).
- **Win Probability Brackets:**
  - **Learning Duel (Blood Mage, Target 20):** Learning 10 -> 25% win; Learning 20 -> 50% win; Learning 30 -> 75% win; Learning 40+ -> 90% cap.
  - **Prowess Duel (Blood Knight, Target 30):** Prowess 15 -> 25% win; Prowess 30 -> 50% win; Prowess 45 -> 75% win; Prowess 60+ -> 90% cap.
- **Safety Cap:** Injuries on defeat are strictly capped at `wounded_2` (never inflicts `wounded_3` or `maimed`).

### 2. Ex-Nihilo Congenital Trait Manifestation (`bm_manifest_traits_values.txt`)
Allows characters to cleanse congenital flaws and ascend `intellect`, `physique`, and `beauty` lines without relying on prisoner RNG:

| Current Trait State | Target Step | Grimoire Tier | Piety Cost | Lifeforce Cost | XP Gained | Duel Base Success / Fail / Crit Fail Weights |
| --- | --- | --- | --- | --- | --- | --- |
| `*_bad_3` -> `*_bad_2` | Cleanse Bad 3 | Major | `250` Piety | 1 Major | `+3` XP | Success `10 + 2×(Learning - 15)` + bonuses; Fail `50` (refunds Minor); Crit Fail `10` (+Minor debuff) |
| `*_bad_2` -> `*_bad_1` | Cleanse Bad 2 | Major | `250` Piety | 1 Major | `+3` XP | Same as above |
| `*_bad_1` -> None | Cleanse Bad 1 | Major | `250` Piety | 1 Major | `+3` XP | Same as above |
| None -> `*_good_1` | Rank 1 (Quick / Hale / Comely) | Major | `250` Piety | 1 Major | `+4` XP | Same as above (`+10` tier bonus) |
| `*_good_1` -> `*_good_2` | Rank 2 (Intelligent / Robust / Handsome) | Major | `500` Piety | 1 Major | `+5` XP | Same as above (`+60` failure weight) |
| `*_good_2` -> `*_good_3` | Rank 3 (Genius / Herculean / Beautiful) | Major | `750` Piety | 1 Major | `+6` XP | Same as above (`+110` failure weight; success loses 1 Devotion Level) |
| `*_good_3` -> Rank 4 | Rank 4 (Overhaul 5-tier compat) | Superior | `1000` Piety | 1 Superior | `+7` XP | DC 25 (`value = 25`), Fail `50 + 150` (refunds Major); Crit Fail `15` (+Major debuff; success loses 1 Devotion Level) |
| Rank 4 -> Rank 5 | Rank 5 (Overhaul 5-tier compat) | Superior | `1500` Piety | 1 Superior | `+8` XP | DC 25 (`value = 25`), Fail `50 + 200` (refunds Major); Crit Fail `15` (+Major debuff; success loses 1 Devotion Level) |

- **Duel Modifiers:**
  - **Learning Traits Bonus (`bm_manifest_traits_learning_traits_bonus`):** `+5` to `+25` from Learning education (`1★` to `5★`), `+15` Scholar, `+10` Theologian, `+10` Mystic.
  - **Track XP Bonus (`bm_manifest_traits_xp_bonus`):** Scales with caster's total Blood Mage / Blood Knight XP.
  - **Existing Congenital Traits Penalty (`bm_manifest_traits_existing_traits_penalty`):** Increases failure and critical failure weights for each positive congenital tier already held across all branches, preventing effortless omnipotent stacking.

### 3. Prisoner Trait Theft Duel Math (`bm_drain_duel_values.txt`)
- **Net Caster Modifier (`trait_drain_modifier`):**
  $$\text{Modifier} = \text{Total Blood Mage/Knight XP} - \text{Prisoner Trait Penalty}$$
- **Prisoner Trait Penalty (`trait_drain_harder_per_trait_modifier`):**
  - Rank 1 (`intellect_good_1`, `physique_good_1`, `beauty_good_1`, `fecund`, `giant`, `pure_blooded`): `-30` per trait.
  - Rank 2 (`intellect_good_2`, `physique_good_2`, `beauty_good_2`): `-60` per trait.
  - Ranks 3–5 (`intellect_good_3..5`, `physique_good_3..5`, `beauty_good_3..5`): `-100` per trait.

### 4. Education Enhancement & Mastery Costs (`bm_education_enhancement_piety_cost.txt`)
- **Formula (`scaled_education_enhancement_cost`):** Base `50` Piety + sum of surcharges across all education traits currently held by the character:
  - Holds 1★ trait: `+25` Piety (`75` Piety total for single education).
  - Holds 2★ trait: `+75` Piety (`125` Piety total for single education).
  - Holds 3★ trait: `+150` Piety (`200` Piety total for single education).
  - Holds 4★ trait (Mastery 4★ -> 5★): `+300` Piety (`350` Piety total for single education).
  - Holds existing 5★ trait (when leveling a 2nd education): `+500` Piety surcharge per 5★ trait held.
- **Zero-Cost Backout:** Piety, Lifeforce, and the 2-year cooldown flag (`bm_improve_education_cooldown` / `bm_new_education_cooldown`) are only deducted when selecting a specific discipline option, allowing players to return to the Major/Superior Grimoire freely.
- **Cooldown Tooltip Localization:** The 2-year cooldown flag (`bm_improve_education_cooldown`) is localized with player-facing sibling keys and wrapped in `custom_description` (`bm_improve_education_cooldown_tt`) in both Major and Superior Grimoires to cleanly display remaining cooldown requirements when options are shown as unavailable.
- **Option Visibility Exception:** In education enhancement (`bm_education_enhancement.001`) and mastery (`bm_education_master.001`), `show_as_unavailable` is scoped to disciplines the character currently possesses (`has_trait = education_<trait>`). Disciplines the character does not possess remain hidden, preventing inappropriate grayed-out disciplines and avoiding CK3 character event window option slot cutoff (maximum 4 options before clipping). When a possessed discipline lacks sufficient Devotion Level (1★: Devotion 1+, 2★: Devotion 2+, 3★: Devotion 3+, 4★: Devotion 4+), it displays grayed out with the unmet devotion requirement.

## Where the details live

| Piece | File |
| --- | --- |
| Geyser initiation decisions & events | `common/decisions/become_mage/bm_become_blood_mage_decision.txt`, `events/bm_geyser_duel_events.txt` |
| Ex-nihilo trait manifestation events, effects & values | `events/bm_channel_manifest_traits_events.txt`, `common/scripted_effects/bm_manifest_traits_effects.txt`, `common/script_values/bm_manifest_traits_values.txt` |
| Prisoner trait theft interaction, events & values | `common/character_interactions/bm_drain_trait.txt`, `events/bm_trait_drain_events.txt`, `common/scripted_effects/bm_drain_trait_effects.txt`, `common/script_values/bm_drain_duel_values.txt` |
| Education enhancement, mastery & 2nd education | `events/bm_education_enhance.txt`, `events/bm_education_master_events.txt`, `events/bm_education_new.txt`, `common/scripted_effects/bm_education_duel_effect.txt`, `common/script_values/bm_education_enhancement_piety_cost.txt` |
| Single combat fatality Lifeforce harvest | `common/on_action/bm_duel_on_actions.txt` |
| Mass lifedrain decision, event & effects | `common/decisions/bm_mass_lifedrain_prisoners.txt`, `events/bm_mass_lifedrain.txt`, `common/scripted_effects/bm_drain_all_prisoners_effects.txt` |
