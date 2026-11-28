# Blood Golems

Living technical specification for the Blood Golem construct subsystem.

## Executive Summary

- **What:** Artificial construct champions forged from Superior Lifeforce (`blood_golem_template`). Serve as hyper-loyal knights and bodyguards in a dedicated non-inheriting house (`bm_house_golem`).
- **How to create:** Superior Grimoire option (`bm_cast_blood_magic_superior.001`) accessed via `bm_cast_blood_magic_superior_decision`.
  - **Requirements:** `lifestyle_blood_mage`, Devotion Rank 3 (`piety_level >= 3`), `lifeforce_modifier_superior`.
  - **Cost & Cooldown:** 500 Piety + 1 Superior Lifeforce (inflicts 3-year Superior exhaustion). Cooldown: 3 years (`bm_blood_golem_cooldown`).
  - **XP Gain:** `+5` `fortune` XP.
- **How to shape:** Event `blood_golem.002` loops repeatedly after creation (`blood_golem.001`), letting the creator spend Piety in contested Learning duels (`golem_duel_effect` / `golem_duel_effect_level`) to mold combat and physical traits onto the golem until the creator chooses to complete the ritual.

### Golem Lifecycle & Base Template (`blood_golem_template`)

| Attribute / Property | Specification |
| --- | --- |
| **House & Dynasty** | House `bm_house_golem` in Dynasty `dynn_bm_golem` (used by Story Panel to track owned golems) |
| **Age & Gender** | Male, spawned at age 18–30 in creator's capital (`culture = root.culture`, `faith = root.faith`) |
| **Base Skills** | **15 Prowess**, 1 Diplomacy, 1 Martial, 1 Stewardship, 1 Intrigue, 1 Learning |
| **Innate Personality** | `content`, `brave`, `trusting`, `loyal` (+100 loyalty/opinion synergy, never schemes against creator) |
| **Innate Physical / Status** | `education_martial_1`, `bm_blood_golem` (blocks marriage, children, and inheritance via `can_not_marry`, `can_have_children = no`, `inheritance_blocker = all`, `claim_inheritance_blocker = all`; base `+2` Prowess, `-100%` Stress Gain, `+15` Dread, `-10` General Opinion, `-15` Attraction Opinion, `+20` Same Opinion, `no_prowess_loss_from_age = yes`, `+15` Epidemic Res; starts at `100` XP, decays `-2` XP/yr via `bm_blood_golem_yearly_decay`, 10 steps at every 10 XP granting `+10` Life Exp, `+1` Prowess, `+0.2` Health each; refuelable via Cast Blood Blessing Grant Lifeforce `+20/+50/+100` XP and `bm_interpersonal_events.0009` `+25/+15` XP) |
| **Portrait Model** | `bm_blood_golem_physique` & `bm_blood_golem_appearance` in `gfx/portraits/trait_portrait_modifiers/bm_trait_modifiers.txt` (giant stature, pale scaly skin, vivid blood-red eyes, completely bald/hairless/beardless; gated by `NOT = { has_game_rule = bm_physical_alteration_off }`, independent of XP) |
| **Rune Synergy** | Eligible target for `bm_inscribe_rune_other_interaction` (e.g. carving **Ægishjálmur** onto a golem) |

### Golem Shaping Options & Dynamic Piety Cost (`blood_golem.002`)

Every shaping attempt in `blood_golem.002` charges a dynamic Piety cost (`golem_piety_cost_scaled_by_traits` in `common/script_values/bm_golem_piety_values.txt`) equal to a **25 Piety base cost** plus a cumulative surcharge for every shaped trait the golem already possesses:

| Shaping Option | Trait Key(s) Added | Max Rank | Duel Macro | Surcharge Added to Future Shaping Attempts |
| --- | --- | --- | --- | --- |
| **Athletic** | `athletic` | 1 | `golem_duel_effect` | `+10` Piety (`level_1_cost`) |
| **Hunter** | `lifestyle_hunter` | 1 | `golem_duel_effect` | `+10` Piety (`level_1_cost`) |
| **Blademaster** | `lifestyle_blademaster` | 1 | `golem_duel_effect` | `+20` Piety (`level_2_cost`) |
| **Viking / Raider** | `viking` | 1 | `golem_duel_effect` | `+20` Piety (`level_2_cost`) |
| **Berserker** | `berserker` | 1 | `golem_duel_effect` | `+30` Piety (`level_3_cost`) |
| **Physique (Hale -> Herculean)** | `physique_good_1..3` | 3 | `golem_duel_effect_level` | Rank 1: `+10`p; Rank 2: `+20`p; Rank 3: `+50`p (`level_4_cost`) |
| **Prowess Education (1★ -> 4★)** | `education_martial_prowess_1..4` | 4 | `golem_duel_effect_level` | Ranks 1–2: `+10`p each; Rank 3: `+20`p; Rank 4: `+30`p |

### Shaping Duel Resolution & Backlash (`bm_golem_duel_effect.txt`)

- **Single-Tier Traits (`golem_duel_effect`):** Learning duel (`value = 0`).
  - **Success** (base 100, `+5` per Learning above 0): Adds `$TRAIT$` to golem.
  - **Failure** (base 100): Pays double Piety cost (`golem_piety_cost_scaled_by_traits`) and rolls trait-count health backlash (`scale_cost_by_number_of_traits_golem_has`, risking wounds or `death_blood_golem_failed` if the golem already holds many traits).
  - **Critical Failure** (base 100, `-2` per Learning): Pays extra Piety, applies 1-year `lifeforce_modifier_negative_minor`, `+10` Stress, and health backlash.
- **Leveled Traits (`golem_duel_effect_level`):** Learning duel (`value = 0`).
  - **Success** (base 40, `+3` per Learning): Adds rank 1 or increments rank by `+1`.
  - **Failure** (base 60): Applies 1-year `lifeforce_modifier_negative_minor`, `+10` Stress, and trait-count health backlash.

## Where the details live

| Piece | File |
| --- | --- |
| Superior Grimoire option | `events/bm_cast_blood_magic_superior_events.txt` (`bm_cast_blood_magic_superior.001`) |
| Creation & shaping events | `events/bm_blood_golem_events.txt` (`blood_golem.001`, `blood_golem.002`) |
| Shaping duel & backlash effects | `common/scripted_effects/bm_golem_duel_effect.txt` (`golem_duel_effect`, `golem_duel_effect_level`) |
| Dynamic Piety cost script values | `common/script_values/bm_golem_piety_values.txt` (`golem_piety_cost_scaled_by_traits`) |
| Golem character template | `common/scripted_character_templates/bm_character_templates.txt` (`blood_golem_template`) |
| Golem house & dynasty | `common/dynasty_houses/bm_dynasty_houses.txt` (`bm_house_golem`), `common/dynasties/bm_dynasties.txt` (`dynn_bm_golem`) |
| Story panel roster integration | `common/scripted_effects/bm_blood_mage_story_list_effects.txt` (`bm_refresh_blood_magic_rosters_effect`) |

## Gotchas & Not Verified

- **Unified Identification (`bm_is_blood_golem_trigger`):** Rosters, interpersonal events, AI hostile-magic vetoes, and rune targeting check `bm_is_blood_golem_trigger` (`has_trait = bm_blood_golem` or `house ?= house:bm_house_golem` fallback for older saves).
- **Sterility & Succession:** Handled directly by `bm_blood_golem` (`can_not_marry`, `can_have_children = no`, `inheritance_blocker = all`, `claim_inheritance_blocker = all`), replacing legacy `beardless_eunuch`, `giant`, and `albino` template traits.
- **Not Verified:** AI willingness to chain multiple shaping rounds in `blood_golem.002` at low health thresholds.
