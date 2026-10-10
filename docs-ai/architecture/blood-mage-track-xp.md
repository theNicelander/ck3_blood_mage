# Blood Mage Track XP & Costs

> Living document describing current state. Follow `AGENTS.md`: high-density technical specs, zero roleplay fluff.

## Executive Summary

- **What:** Master technical catalog of XP acquisition methods, Piety costs, Lifeforce sinks/sources, cooldowns, and XP values across all lifestyle traits and 13 progression tracks.
- **Traits Covered:** `lifestyle_blood_mage` (5 tracks: `ancient`, `enlightenment`, `bloodline`, `benediction`, `hematurgy`), `lifestyle_blood_empowerment` (5 tracks: `dynasty`, `mastery`, `presence`, `prosperity`, `shadows`), `lifestyle_blood_knight` (5 tracks: `vanguard`, `slaughter`, `resilience`, and shared `ancient`, `benediction`).
- **Engine Cap:** Strictly 100 XP max per track (10 tiers at 10 XP steps). Overflow discarded.
- **Stat Parity:** Every 10 XP tier in both `lifestyle_blood_mage` and `lifestyle_blood_knight` scales the exact same baseline vitality bonuses: `+0.1` Health, `+2` Life Expectancy, `+1` Year Fertility, `+1` Epidemic Resistance.
- **Cost Types:** Piety, Lifeforce (`minor`, `major`, `superior`), Piety Levels, and cooldowns.

### Master Track Progression Overview

| XP Gain | Cost | Action / Primary Sources | Trait | Track |
| --- | --- | --- | --- | --- |
| +1 to +10 XP | 0 (pulse) / 25–400 Piety + Minor/Major/Superior Lifeforce | Yearly pulse, attunement, manifest lifeforce, inscribe blood runes | `lifestyle_blood_mage` | `ancient` |
| +1 to +8 XP | 75 – 1000 Piety + Minor/Major/Superior Lifeforce | Education enhancements, lifeforce channeling, empowerment | `lifestyle_blood_mage` | `enlightenment` |
| +2 to +6 XP | 0 – 500 Piety + Minor/Major/Superior Lifeforce | Grant blood magic, childbirth, bless kin, commune rite, congenital traits, empower bloodline, golems | `lifestyle_blood_mage` | `bloodline` |
| +1 to +6 XP | 0 – 100 Piety (scaled) + Minor/Major Lifeforce | Curing illnesses, making/empowering blood knights, restoring drained courtiers | `lifestyle_blood_mage` | `benediction` |
| +1 to +2 XP | 25 – 250 Piety (Grants Minor/Major lifeforce) | Prisoner/courtier draining, congenital trait theft, wilderness harvest | `lifestyle_blood_mage` | `hematurgy` |
| +10 XP (chosen track) | 150 Piety + Major Lifeforce | Channel Blood Empowerment decision | `lifestyle_blood_empowerment` | `dynasty`, `mastery`, `presence`, `prosperity`, `shadows` |
| +1 to +10 XP | None / Minor/Major Lifeforce (caster) | Commander/knight battle victories, healing comrades, mage empowerment | `lifestyle_blood_knight` | `vanguard` |
| +2 to +10 XP | None / Minor/Major Lifeforce (caster) | Single combat fatal kills (yields Minor Lifeforce), tournaments, mage empowerment | `lifestyle_blood_knight` | `slaughter` |
| +1 to +10 XP | 100 Piety (manifest) / None | Yearly survival pulse, defeat survival, Prowess manifest lifeforce, self-tending | `lifestyle_blood_knight` | `resilience` |

---

## 1. Lifestyle Blood Mage (`lifestyle_blood_mage`)

### 1.1 Ancient Track (`ancient`)

| XP Gain | Cost | Action | Type | Requirements | Cooldown |
| --- | --- | --- | --- | --- | --- |
| **+1 XP** | None | Yearly Pulse | On-action (`blood_mage_yearly_events.001`) | Has `lifestyle_blood_mage` | 1 year |
| **+1 XP** | None (50% roll) | Ancient Attunement Roll | Yearly event roll (`blood_mage_yearly_events.001`) | Has `ancient_attuned` | 1 year |
| Grants `ancient_attuned` | 25 Piety + Minor Lifeforce (`lifeforce_modifier_minor`) | Attune Lifeforce (Ancient) | Event option (`bm_cast_blood_magic_minor.001`) | Has minor lifeforce | None |
| **+3 XP** | 100 Piety (Generates Major/Minor on Learning duel) | Manifest Lifeforce | Decision (`bm_manifest_lifeforce_decision`) | `piety_level >= 2` | 1 year |
| **+8 XP** (crit), **+5 XP** (success), **+2 XP** (fail) | 250 Piety + Minor & Major Lifeforce (Generates Superior) | Manifest Superior Lifeforce | Decision (`bm_manifest_superior_lifeforce_decision`) | `piety_level >= 3`, Minor + Major | 2 years |
| **+4 XP** | 0 Piety + Minor & Major Lifeforce | Inscribe Minor Blood Rune | Event option (`bm_cast_blood_magic_major.001`) | `piety_level >= 2` | 5 years |
| **+5 XP** | 200 Piety + Minor & Major Lifeforce | Inscribe Major Blood Rune | Event option (`bm_cast_blood_magic_major.001`) | `piety_level >= 3`, Minor rune | 5 years |
| **+10 XP** | 400 Piety + Superior Lifeforce (`lifeforce_modifier_superior`) | Inscribe Superior Blood Rune | Event option (`bm_cast_blood_magic_superior.001`) | `piety_level >= 4`, Major rune | 5 years |

### 1.2 Enlightenment Track (`enlightenment`)

| XP Gain | Cost | Action | Type | Requirements | Cooldown |
| --- | --- | --- | --- | --- | --- |
| **+1 XP** | 75 Piety + Minor Lifeforce (`lifeforce_modifier_minor`) | Channel Minor Lifeforce | Event option (`bm_cast_blood_magic_minor.001`) | Minor lifeforce | None |
| **+1 XP** | 25 Piety + Minor Lifeforce (`lifeforce_modifier_minor`) | Grant Lifeforce (Minor) | Interaction (`grant_lifeforce_interaction`) | Minor lifeforce, courtier/prisoner | None |
| **+2 XP** | 50 Piety + Major Lifeforce (`lifeforce_modifier_major`) | Grant Lifeforce (Major) | Interaction (`grant_lifeforce_interaction`) | Major lifeforce, courtier/prisoner | None |
| **+3 XP** (+10 Empowerment XP) | 150 Piety + Major Lifeforce (`lifeforce_modifier_major`) | Channel Blood Empowerment | Event option (`bm_cast_blood_magic_major.001`) | `piety_level >= 1` | None |
| **+4 XP** | Scaled: 75 (1->2), 125 (2->3), 200 (3->4) Piety + Major Lifeforce (`lifeforce_modifier_major`) | Improve Education (2★/3★/4★) | Event option (`bm_cast_blood_magic_major.001`) | `piety_level >= 3` | 2 years |
| **+8 XP** upfront (+8 XP on duel win) | 350 Piety + Superior Lifeforce (`lifeforce_modifier_superior`) | Master Education (5★) | Event option (`bm_cast_blood_magic_superior.001`) | `piety_level >= 3`, 4★ education | 2 years |
| **+8 XP** | 1000 Piety + Superior Lifeforce (`lifeforce_modifier_superior`) | New Education (2nd Trait) | Event option (`bm_cast_blood_magic_superior.001`) | `piety_level >= 4`, 5★ education | 2 years |
| **+2 XP** | 200 Piety + Superior Lifeforce (`lifeforce_modifier_superior`) | Manifest Transcendent Perfection (Congenital 4-5) | Event option (`bm_cast_blood_magic_superior.001`) | `piety_level >= 3` | None |
| **+1 XP** | None (50% roll) | Enlightenment Attunement Roll | Yearly event roll (`blood_mage_yearly_events.001`) | Has `enlightenment_attuned` | 1 year |

### 1.3 Bloodline Track (`bloodline`)

| XP Gain | Cost | Action | Type | Requirements | Cooldown |
| --- | --- | --- | --- | --- | --- |
| **+4 XP** (+5 XP if child/kin) | 75 Piety + Major Lifeforce (`lifeforce_modifier_major`) | Grant Blood Magic | Interaction (`grant_blood_magic_interaction`) | Target non-mage | None |
| **+2 XP** (+4 XP if child inherits trait) | None | Childbirth Milestone | On-action (`on_birth_child` -> `bm_on_birth_bloodline_xp`) | Parent is blood mage | Per birth |
| **+2 XP** | 35 Piety + Minor Lifeforce (`lifeforce_modifier_minor`) | Bless Kin's Blood | Interaction (`bm_bless_bloodline_interaction`) | Target child/dynasty kin | 10 years (target buff) |
| **+2 XP** | 50 Piety + Minor Lifeforce (`lifeforce_modifier_minor`) | Commune with Bloodline | Event option (`bm_cast_blood_magic_minor.001`) | Has house | 3 years |
| **+2 XP** | 50 Piety + Minor Lifeforce (`lifeforce_modifier_minor`) | Purge Bodily Impurities (Congenital Flaw Cleansed) | Event option (`bm_cast_blood_magic_minor.001`) | Has ugly/dull/weak | None |
| **+4 XP** (on duel win) | 200 Piety + Major Lifeforce (`lifeforce_modifier_major`) | Manifest Perfection (Congenital 1-3) | Event option (`bm_cast_blood_magic_major.001`) | `piety_level >= 2` | None |
| **+6 XP** (on duel win) | 200 Piety + Superior Lifeforce (`lifeforce_modifier_superior`) | Manifest Transcendent Perfection (Congenital 4-5) | Event option (`bm_cast_blood_magic_superior.001`) | `piety_level >= 3` | None |
| **+5 XP** | 350 Piety + Major Lifeforce (`lifeforce_modifier_major`) | Empower Bloodline | Event option (`bm_cast_blood_magic_major.001`) | `exists = house`, `piety_level >= 1` | 3 years |
| **+5 XP** | 500 Piety + Superior Lifeforce (`lifeforce_modifier_superior`) | Forge Blood Golem | Decision (`blood_golem_creation_decision`) | `piety_level >= 3`, Superior lifeforce | 3 years |
| **+1 XP** (+10% chance per active house modifier, up to 70%) | None | Yearly Dynasty Modifiers Pulse | On-action (`blood_mage_yearly_events.002`) | Has house, house modifiers | 1 year |
| **+1 XP** | None (50% roll) | Bloodline Attunement Roll | Yearly event roll (`blood_mage_yearly_events.001`) | Has `bloodline_attuned` | 1 year |

### 1.4 Benediction Track (`benediction`)

| XP Gain | Cost | Action | Type | Requirements | Cooldown |
| --- | --- | --- | --- | --- | --- |
| **+2 XP** | **15 Piety per trait cured** (`cure_illness_cost_minor`) + Minor Lifeforce (`lifeforce_modifier_minor`) | **Heal Disease: Minor** (`heal_disease_minor`) | Interaction | Self or courtier with `wounded_1`, `ill`, `lovers_pox`, `gout_ridden`, `scarred` | None |
| **+4 XP** | **35 Piety per trait cured** (`cure_illness_cost_major`) + Major Lifeforce (`lifeforce_modifier_major`) | **Heal Disease: Major** (`heal_disease_major`) | Interaction | Self or courtier with `wounded_2`, `incapable`, `pneumonic`, `infirm`, `maimed`, etc. | None |
| **+6 XP** | **100 Piety per trait cured** (`cure_illness_cost_benediction`) + **both** Minor & Major Lifeforce | **Heal Disease: Benediction** (`heal_disease_benediction`) | Interaction | Self or courtier with `wounded_3`, `cancer`, `plague`, `leper`, `disfigured`, etc. | None |
| **+4 XP** | 100 Piety + Major Lifeforce (`lifeforce_modifier_major`) | Make Blood Knight | Interaction (`make_blood_knight_interaction`) | Target without blood knight | None |
| **+3 XP** (caster) | 0 Piety + Major Lifeforce (`lifeforce_modifier_major`) | Empower Blood Knight (Major) | Interaction (`empower_blood_knight_interaction`) | Target is blood knight | None |
| **+1 XP** (caster) | 0 Piety + Minor Lifeforce (`lifeforce_modifier_minor`) | Empower Blood Knight (Minor) | Interaction (`empower_blood_knight_interaction`) | Target is blood knight | None |
| **+3 XP** | 25 Piety + Major Lifeforce (`lifeforce_modifier_major`) | Restore Lifedrained Courtier | Interaction (`grant_lifeforce_interaction_reversed`) | Target has `lifedrained_modifier` | None |
| **+1 XP** | None (50% roll) | Benediction Attunement Roll | Yearly event roll (`blood_mage_yearly_events.001`) | Has `benediction_attuned` | 1 year |

### 1.5 Hematurgy Track (`hematurgy`)

| XP Gain | Cost | Action | Type | Requirements | Cooldown |
| --- | --- | --- | --- | --- | --- |
| **+2 XP** | 50 Piety (`lifedrain_piety_cost_major`); **Grants** Major Lifeforce (Executes victim) | Lifedrain Prisoner | Interaction (`lifedrain_prisoner_event_interaction`) | Imprisoned target | None |
| **+1 XP** | 25 Piety (`lifedrain_piety_cost_minor`); **Grants** Minor Lifeforce | Lifedrain Courtier | Interaction (`lifedrain_courtier_event_interaction`) | Courtier/prisoner not recently drained | 3 months |
| **+2 XP** (on duel win) | 100–250 Piety + Major Lifeforce (Executes victim) | Drain Prisoner Trait (Lvl 1–3) | Interaction + Event (`bm_trait_drain.001`) | Prisoner with congenital trait | 60 days |
| **+1 to +2 XP** | None | Seek Power Wilderness Harvest | Decision & Event (`seek_power.001`) | Blood mage | 1–2 years |
| **+1 XP** | None (50% roll) | Hematurgy Attunement Roll | Yearly event roll (`blood_mage_yearly_events.001`) | Has `hematurgy_attuned` | 1 year |

*Note: Battlefield combat kill lifeforce is strictly reserved for Blood Knights. Blood Mages harvest exclusively through sacrificial and draining rites.*

---

## 2. Lifestyle Blood Empowerment (`lifestyle_blood_empowerment`)

Tracks: `dynasty`, `mastery`, `presence`, `prosperity`, `shadows` (5 tracks total).

| XP Gain | Cost | Action | Type | Requirements | Cooldown |
| --- | --- | --- | --- | --- | --- |
| **+10 XP** in chosen track (+3 `enlightenment` XP) | 150 Piety + Major Lifeforce (`lifeforce_modifier_major`) | Channel Blood Empowerment (`bm_cast_blood_magic_major_decision` -> `bm_blood_empowerment_event.001`) | Decision -> Event | `piety_level >= 1`, Major lifeforce held | None |
| **0 XP** (strictly manual advancement) | None | Passive Growth | None | None | None |

---

## 3. Lifestyle Blood Knight (`lifestyle_blood_knight`)

Tracks: `vanguard`, `slaughter`, `resilience` (and shared `ancient`, `benediction`).

| XP Gain | Cost | Action | Type | Requirements | Cooldown |
| --- | --- | --- | --- | --- | --- |
| **+10 XP to martial tracks** | 0 Piety (knight); Caster consumes Major Lifeforce | Empower Blood Knight: Major | Interaction (`empower_blood_knight_interaction`) | Blood Mage empowers knight | None |
| **+5 XP to martial tracks** | 0 Piety (knight); Caster consumes Minor Lifeforce | Empower Blood Knight: Minor | Interaction (`empower_blood_knight_interaction`) | Blood Mage empowers knight | None |
| **+5 XP** (`vanguard`) | None (33% roll for Minor Lifeforce) | Battle Victory (Commander) | On-action (`bm_on_combat_end_winner`) | Army commander | Per battle |
| **+4 XP** (`vanguard`) | None (33% roll for Minor Lifeforce) | Battle Victory (Knight) | On-action (`bm_on_combat_end_winner`) | Army knight | Per battle |
| **+1 XP** (`vanguard`) + **+1 XP** (`benediction`) | 15 Piety + Minor Lifeforce | Heal Disease Minor (Comrade / Knight / Liege) | Interaction (`heal_disease_minor`) | Target ally with minor ailment | None |
| **+1 XP** (`vanguard`) + **+2 XP** (`resilience`) | None | Battle Defeat (Surviving Commander / Knight) | On-action (`bm_on_combat_end_loser`) | Surviving side commander or knight | Per battle |
| **+5 XP** (`slaughter`) | None; **Grants** Minor Lifeforce | Single Combat Fatal Slaying | On-action (`bm_on_character_death_duel`) | Slaying opponent in single combat | None |
| **+3 XP** (`slaughter`) | None | Tournament Completion | On-action (`bm_on_travel_activity_complete_tournament`) | Completing `activity_tournament` | Per tourney |
| **+3 XP** (`resilience`) | 100 Piety; **Grants** Minor Lifeforce on Prowess duel success | Manifest Lifeforce | Decision (`bm_manifest_lifeforce_decision`) | `piety_level >= 2` | 1 year |
| **+2 XP** (`resilience`) | 15 Piety + Minor Lifeforce | Heal Disease Minor (Self-Healing Wounds) | Interaction (`heal_disease_minor`) | Self has minor wound/illness | None |
| **+2 XP** (`resilience`) | 50 Piety + Minor Lifeforce | Purge Bodily Impurities (Self-Tending Weakness) | Event option (`bm_cast_blood_magic_minor.001`) | Self has physical frailty | None |
| **+1 XP** (`resilience`) + **+1 XP** (`ancient`) | None | Yearly Survival Pulse | On-action (`blood_mage_yearly_events.004`) | Has `lifestyle_blood_knight` | 1 year |

---

## Where the details live

| Subsystem | Key Files |
| --- | --- |
| XP Helper Macros | `common/scripted_effects/bm_trait_track_xp_gain_effects.txt` |
| Blood Magic Scripted Effects | `common/scripted_effects/bm_blood_magic_used_effects.txt` |
| Cure Illness Interactions & Costs | `common/character_interactions/bm_cure_illness_interactions.txt`<br>`common/script_values/bm_cure_illness_values.txt` |
| Drain & Grant Interactions & Costs | `common/character_interactions/bm_drain_lifeforce.txt`<br>`common/character_interactions/bm_grant_lifeforce.txt`<br>`common/character_interactions/bm_grant_blood_magic.txt`<br>`common/character_interactions/bm_bless_bloodline.txt` |
| Trait Drain Duel & Events | `common/character_interactions/bm_drain_trait.txt`<br>`events/bm_trait_drain_events.txt`<br>`common/scripted_effects/bm_drain_trait_effects.txt` |
| Education Enhancement Costs & Duels | `common/script_values/bm_education_enhancement_piety_cost.txt`<br>`common/scripted_effects/bm_education_duel_effect.txt` |
| Congenital Trait Manifestation | `common/scripted_effects/bm_manifest_traits_effects.txt`<br>`events/bm_channel_manifest_traits_events.txt` |
| Blood Empowerment Events | `events/bm_blood_empowerment_event.txt` |
| Blood Knight Interactions & Hooks | `common/character_interactions/bm_blood_knight_interactions.txt`<br>`common/on_action/bm_combat_on_actions.txt`<br>`common/on_action/bm_duel_on_actions.txt` |
| Yearly Pulse, Attunements & Birth | `events/bm_yearly_events.txt`<br>`events/bm_attune_lifeforce_events.txt`<br>`common/on_action/bm_blood_mage_prevalence_on_actions.txt` |

---

## Gotchas

- **Stat Parity Maintenance:** All tracks on both `lifestyle_blood_mage` and `lifestyle_blood_knight` must reference `@bm_common_health`, `@bm_common_life_expectancy`, `@bm_common_years_of_fertility`, and `@bm_common_epidemic_resistance` in their tier definitions.
- **Battlefield Lifeforce Exclusivity:** `on_combat_end_winner` and `bm_on_character_death_duel` strictly grant battlefield lifeforce to `lifestyle_blood_knight`. Blood Mages harvest exclusively via intentional rituals and prison/courtier interactions.
- **Bloodline Induction:** Granting Blood Magic to children or dynasty members checks `is_child_of` or `dynasty ?= scope:actor.dynasty` and awards +5 Bloodline XP instead of base +4.
