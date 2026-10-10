# Blood Mage Track XP & Costs

> Living document describing current state. Follow `AGENTS.md`: high-density technical specs, zero roleplay fluff.

## Executive Summary

- **What:** Master technical catalog of XP acquisition methods, Piety costs, Lifeforce sinks/sources, cooldowns, and XP values across all 3 lifestyle traits and 13 progression tracks.
- **Traits Covered:** `lifestyle_blood_mage` (5 tracks: `ancient`, `enlightenment`, `bloodline`, `benediction`, `hematurgy`), `lifestyle_blood_empowerment` (5 tracks: `dynasty`, `mastery`, `presence`, `prosperity`, `shadows`), `lifestyle_blood_knight` (3 tracks: `vanguard`, `slaughter`, `resilience`).
- **Engine Cap:** Strictly 100 XP max per track (10 tiers at 10 XP steps). Overflow discarded.
- **Cost Types:** Piety, Lifeforce (`minor`, `major`, `superior`), Piety Levels, and cooldowns.

### Master Track Progression Overview

| XP Gain | Cost | Action / Primary Sources | Trait | Track |
| --- | --- | --- | --- | --- |
| +1 XP/yr; +1 XP (50% roll) | 0 (pulse) / 25 Piety + Minor Lifeforce (attune) | Yearly pulse; Attunement roll | `lifestyle_blood_mage` | `ancient` |
| +1 to +10 XP | 25 – 1000 Piety + Minor/Major/Superior Lifeforce | Manifestations, education, empowerment, grant | `lifestyle_blood_mage` | `enlightenment` |
| +1 to +5 XP | 0 – 500 Piety + Major/Superior Lifeforce | Empower bloodline, Golem forge, house modifiers | `lifestyle_blood_mage` | `bloodline` |
| +2 to +10 XP | 0 – 400 Piety (scaled) + Minor/Major/Superior Lifeforce | Curing illness, granting power, blood runes | `lifestyle_blood_mage` | `benediction` |
| +1 to +2 XP | 25 – 250 Piety (Grants Minor/Major, or Major sink for trait drain) | Prisoner/courtier draining, trait draining, duels | `lifestyle_blood_mage` | `hematurgy` |
| +10 XP (chosen track) | 150 Piety + Major Lifeforce | Channel Blood Empowerment decision | `lifestyle_blood_empowerment` | `dynasty`, `mastery`, `presence`, `prosperity`, `shadows` |
| +5 or +10 XP (all 3 tracks) | Minor/Major Lifeforce (caster) | Knight empowerment interaction | `lifestyle_blood_knight` | `vanguard`, `slaughter`, `resilience` |
| +1, +5, or +6 XP | None | Battle victories & surviving defeats | `lifestyle_blood_knight` | `vanguard` |
| +3 or +6 XP | None | Single combat kills; tournament completion | `lifestyle_blood_knight` | `slaughter` |
| +1 XP | None | Yearly survival pulse; defeat survival | `lifestyle_blood_knight` | `resilience` |

---

## 1. Lifestyle Blood Mage (`lifestyle_blood_mage`)

### 1.1 Ancient Track (`ancient`)

| XP Gain | Cost | Action | Type | Requirements | Cooldown |
| --- | --- | --- | --- | --- | --- |
| **+1 XP** | None | Yearly Pulse | On-action (`blood_mage_yearly_events.001`) | Has `lifestyle_blood_mage` | 1 year |
| **+1 XP** | None (50% roll) | Ancient Attunement Roll | Yearly event roll (`blood_mage_yearly_events.001`) | Has `ancient_attuned` | 1 year |
| Grants `ancient_attuned` | 25 Piety + Minor Lifeforce (`lifeforce_modifier_minor`) | Attune Lifeforce (Ancient) | Event option (`bm_cast_blood_magic_minor.001`) | Has minor lifeforce | None |

### 1.2 Enlightenment Track (`enlightenment`)

| XP Gain | Cost | Action | Type | Requirements | Cooldown |
| --- | --- | --- | --- | --- | --- |
| **+1 XP** | 75 Piety + Minor Lifeforce (`lifeforce_modifier_minor`) | Channel Minor Lifeforce | Event option (`bm_cast_blood_magic_minor.001`) | Minor lifeforce | None |
| **+1 XP** | 25 Piety + Minor Lifeforce (`lifeforce_modifier_minor`) | Grant Lifeforce (Minor) | Interaction (`grant_lifeforce_interaction`) | Minor lifeforce, courtier/prisoner | None |
| **+2 XP** | 50 Piety + Major Lifeforce (`lifeforce_modifier_major`) | Grant Lifeforce (Major) | Interaction (`grant_lifeforce_interaction`) | Major lifeforce, courtier/prisoner | None |
| **+3 XP** (+10 Empowerment XP) | 150 Piety + Major Lifeforce (`lifeforce_modifier_major`) | Channel Blood Empowerment | Event option (`bm_cast_blood_magic_major.001`) | `piety_level >= 1` | None |
| **+5 XP** | 100 Piety (Generates Minor or Major on duel) | Manifest Lifeforce | Decision (`bm_manifest_lifeforce_decision`) | `piety_level >= 2` | 1 year |
| **+5 XP** | Scaled: 75 (1->2), 125 (2->3), 200 (3->4) Piety + Major Lifeforce (`lifeforce_modifier_major`) | Improve Education (2★/3★/4★) | Event option (`bm_cast_blood_magic_major.001`) | `piety_level >= 3` | 2 years |
| **+5 XP** (on duel success) | 200 Piety + Major Lifeforce (`lifeforce_modifier_major`) | Manifest Perfection (Congenital 1-3) | Event option (`bm_cast_blood_magic_major.001`) | `piety_level >= 2` | None |
| **+10 XP** (crit), **+5 XP** (success), **+2 XP** (fail) | 250 Piety + Minor & Major Lifeforce (Generates Superior) | Manifest Superior Lifeforce | Decision (`bm_manifest_superior_lifeforce_decision`) | `piety_level >= 3`, Minor + Major | 2 years |
| **+10 XP** upfront (+10 XP on duel win) | 350 Piety + Superior Lifeforce (`lifeforce_modifier_superior`) | Master Education (5★) | Event option (`bm_cast_blood_magic_superior.001`) | `piety_level >= 3`, 4★ education | 2 years |
| **+10 XP** | 1000 Piety + Superior Lifeforce (`lifeforce_modifier_superior`) | New Education (2nd Trait) | Event option (`bm_cast_blood_magic_superior.001`) | `piety_level >= 4`, 5★ education | 2 years |
| **+1 XP** | None (50% roll) | Enlightenment Attunement Roll | Yearly event roll (`blood_mage_yearly_events.001`) | Has `enlightenment_attuned` | 1 year |

### 1.3 Bloodline Track (`bloodline`)

| XP Gain | Cost | Action | Type | Requirements | Cooldown |
| --- | --- | --- | --- | --- | --- |
| **+5 XP** | 350 Piety + Major Lifeforce (`lifeforce_modifier_major`) | Empower Bloodline | Event option (`bm_cast_blood_magic_major.001`) | `exists = house`, `piety_level >= 1` | 3 years |
| **+5 XP** | 500 Piety + Superior Lifeforce (`lifeforce_modifier_superior`) | Forge Blood Golem | Decision (`blood_golem_creation_decision`) | `piety_level >= 3`, Superior lifeforce | 3 years |
| **+1 XP** (+5% chance per active house modifier, up to 35%) | None | Yearly Dynasty Modifiers Pulse | On-action (`blood_mage_yearly_events.002`) | Has house, house modifiers | 1 year |
| **+1 XP** | None (50% roll) | Bloodline Attunement Roll | Yearly event roll (`blood_mage_yearly_events.001`) | Has `bloodline_attuned` | 1 year |

### 1.4 Benediction Track (`benediction`)

| XP Gain | Cost | Action | Type | Requirements | Cooldown |
| --- | --- | --- | --- | --- | --- |
| **+2 XP** | **15 Piety per trait cured** (`cure_illness_cost_minor`) + Minor Lifeforce (`lifeforce_modifier_minor`) | **Heal Disease: Minor** (`heal_disease_minor`) | Interaction | Self or courtier with `wounded_1`, `ill`, `lovers_pox`, `gout_ridden`, `scarred` | None |
| **+4 XP** | **35 Piety per trait cured** (`cure_illness_cost_major`) + Major Lifeforce (`lifeforce_modifier_major`) | **Heal Disease: Major** (`heal_disease_major`) | Interaction | Self or courtier with `wounded_2`, `incapable`, `pneumonic`, `early_great_pox`, `infirm`, `withering_mind`, `clouded_eyes`, `fragile_bones`, `maimed`, `consumption`, `typhus`, `measles`, `blind`, `one_eyed`, `weak`, `lunatic_1`, `possessed_1`, `dull`, `depressed_1` | None |
| **+8 XP** | **100 Piety per trait cured** (`cure_illness_cost_benediction`) + **both** Minor & Major Lifeforce | **Heal Disease: Benediction** (`heal_disease_benediction`) | Interaction | Self or courtier with `wounded_3`, `sickly`, `great_pox`, `cancer`, `bubonic_plague`, `smallpox`, `leper`, `impotent`, `dysentery`, `ergotism`, `disfigured`, `one_legged`, `faltering_heart` | None |
| **+4 XP** | 75 Piety + Major Lifeforce (`lifeforce_modifier_major`) | Grant Blood Magic | Interaction (`grant_blood_magic_interaction`) | Target without blood mage | None |
| **+4 XP** | 100 Piety + Major Lifeforce (`lifeforce_modifier_major`) | Make Blood Knight | Interaction (`make_blood_knight_interaction`) | Target without blood knight | None |
| **+4 XP** (caster) | 0 Piety + Major Lifeforce (`lifeforce_modifier_major`) | Empower Blood Knight (Major) | Interaction (`empower_blood_knight_interaction`) | Target is blood knight | None |
| **+2 XP** (caster) | 0 Piety + Minor Lifeforce (`lifeforce_modifier_minor`) | Empower Blood Knight (Minor) | Interaction (`empower_blood_knight_interaction`) | Target is blood knight | None |
| **+4 XP** | 25 Piety + Major Lifeforce (`lifeforce_modifier_major`) | Restore Lifedrained Courtier | Interaction (`grant_lifeforce_interaction_reversed`) | Target has `lifedrained_modifier` | None |
| **+5 XP** | 0 Piety + Minor & Major Lifeforce | Inscribe Minor Blood Rune | Event option (`bm_cast_blood_magic_major.001`) | `piety_level >= 2` | 5 years |
| **+5 XP** | 200 Piety + Minor & Major Lifeforce | Inscribe Major Blood Rune | Event option (`bm_cast_blood_magic_major.001`) | `piety_level >= 3`, Minor rune | 5 years |
| **+10 XP** | 400 Piety + Superior Lifeforce (`lifeforce_modifier_superior`) | Inscribe Superior Blood Rune | Event option (`bm_cast_blood_magic_superior.001`) | `piety_level >= 4`, Major rune | 5 years |
| **+1 XP** | None (50% roll) | Benediction Attunement Roll | Yearly event roll (`blood_mage_yearly_events.001`) | Has `benediction_attuned` | 1 year |

### 1.5 Hematurgy Track (`hematurgy`)

| XP Gain | Cost | Action | Type | Requirements | Cooldown |
| --- | --- | --- | --- | --- | --- |
| **+2 XP** | 50 Piety (`lifedrain_piety_cost_major`); **Grants** Major Lifeforce (Executes victim) | Lifedrain Prisoner | Interaction (`lifedrain_prisoner_event_interaction`) | Imprisoned target | None |
| **+1 XP** | 25 Piety (`lifedrain_piety_cost_minor`); **Grants** Minor Lifeforce | Lifedrain Courtier | Interaction (`lifedrain_courtier_event_interaction`) | Courtier/prisoner not recently drained | 3 months |
| **+2 XP** (on duel win) | 100 Piety (`trait_drain_base_piety_cost`) + Major Lifeforce (Executes victim) | Drain Prisoner Trait (Lvl 1 / Fecund / Giant) | Interaction + Event (`bm_trait_drain.001`) | Prisoner with trait | 60 days |
| **+2 XP** (on duel win) | 175 Piety (100 base + 75 lvl 2) + Major Lifeforce (Executes victim) | Drain Prisoner Trait (Lvl 2) | Interaction + Event (`bm_trait_drain.001`) | Prisoner with rank 2 trait | 60 days |
| **+2 XP** (on duel win) | 250 Piety (100 base + 150 lvl 3) + Major Lifeforce (Executes victim) | Drain Prisoner Trait (Lvl 3) | Interaction + Event (`bm_trait_drain.001`) | Prisoner with rank 3 trait | 60 days |
| **+2 XP** | 0 Piety; **Grants** Major Lifeforce | Single Combat Fatal Slaying | On-action (`bm_on_character_death_duel`) | Killer is blood mage in single combat duel | None |
| **+1 XP** | None (50% roll) | Hematurgy Attunement Roll | Yearly event roll (`blood_mage_yearly_events.001`) | Has `hematurgy_attuned` | 1 year |

---

## 2. Lifestyle Blood Empowerment (`lifestyle_blood_empowerment`)

Tracks: `dynasty`, `mastery`, `presence`, `prosperity`, `shadows` (5 tracks total).

| XP Gain | Cost | Action | Type | Requirements | Cooldown |
| --- | --- | --- | --- | --- | --- |
| **+10 XP** in chosen track (+3 `enlightenment` XP) | 150 Piety + Major Lifeforce (`lifeforce_modifier_major`) | Channel Blood Empowerment (`bm_cast_blood_magic_major_decision` -> `bm_blood_empowerment_event.001`) | Decision -> Event | `piety_level >= 1`, Major lifeforce held | None |
| **0 XP** (strictly manual advancement) | None | Passive Growth | None | None | None |

---

## 3. Lifestyle Blood Knight (`lifestyle_blood_knight`)

Tracks: `vanguard`, `slaughter`, `resilience` (3 tracks total).

| XP Gain | Cost | Action | Type | Requirements | Cooldown |
| --- | --- | --- | --- | --- | --- |
| **+10 XP to all 3 tracks** (`vanguard`, `slaughter`, `resilience`) | 0 Piety (knight); Caster consumes Major Lifeforce (`lifeforce_modifier_major`) | Empower Blood Knight: Major | Interaction (`empower_blood_knight_interaction`) | Blood Mage empowers knight | None |
| **+5 XP to all 3 tracks** (`vanguard`, `slaughter`, `resilience`) | 0 Piety (knight); Caster consumes Minor Lifeforce (`lifeforce_modifier_minor`) | Empower Blood Knight: Minor | Interaction (`empower_blood_knight_interaction`) | Blood Mage empowers knight | None |
| **+6 XP** (`vanguard`) | None | Battle Victory (Commander) | On-action (`bm_on_combat_end_winner`) | Army commander | Per battle |
| **+5 XP** (`vanguard`) | None | Battle Victory (Knight) | On-action (`bm_on_combat_end_winner`) | Army knight | Per battle |
| **+1 XP** (`vanguard`) + **+1 XP** (`resilience`) | None | Battle Defeat (Surviving Commander / Knight) | On-action (`bm_on_combat_end_loser`) | Surviving side commander or knight | Per battle |
| **+6 XP** (`slaughter`) | None | Single Combat Fatal Slaying | On-action (`bm_on_character_death_duel`) | Slaying opponent in single combat | None |
| **+3 XP** (`slaughter`) | None | Tournament Completion | On-action (`bm_on_travel_activity_complete_tournament`) | Completing `activity_tournament` | Per tourney |
| **+1 XP** (`resilience`) | None | Yearly Survival Pulse | On-action (`blood_mage_yearly_events.004`) | Has `lifestyle_blood_knight` | 1 year |

---

## Where the details live

| Subsystem | Key Files |
| --- | --- |
| XP Helper Macros | `common/scripted_effects/bm_trait_track_xp_gain_effects.txt` |
| Blood Magic Scripted Effects | `common/scripted_effects/bm_blood_magic_used_effects.txt` |
| Cure Illness Interactions & Costs | `common/character_interactions/bm_cure_illness_interactions.txt`<br>`common/script_values/bm_cure_illness_values.txt` |
| Drain & Grant Interactions & Costs | `common/character_interactions/bm_drain_lifeforce.txt`<br>`common/character_interactions/bm_grant_lifeforce.txt`<br>`common/script_values/bm_drain_piety_cost.txt` |
| Trait Drain Duel & Events | `common/character_interactions/bm_drain_trait.txt`<br>`events/bm_trait_drain_events.txt`<br>`common/scripted_effects/bm_drain_trait_effects.txt` |
| Education Enhancement Costs & Duels | `common/script_values/bm_education_enhancement_piety_cost.txt`<br>`common/script_values/bm_xp_requirement_values.txt`<br>`common/scripted_effects/bm_education_duel_effect.txt` |
| Blood Empowerment Events | `events/bm_blood_empowerment_event.txt` |
| Blood Knight Interactions & Hooks | `common/character_interactions/bm_blood_knight_interactions.txt`<br>`common/on_action/bm_combat_on_actions.txt`<br>`common/on_action/bm_duel_on_actions.txt` |
| Yearly Pulse & Attunements | `events/bm_yearly_events.txt`<br>`events/bm_attune_lifeforce_events.txt` |

---

## Gotchas

- **Healing Cost Stacking:** Curing multiple conditions in a single interaction charges the per-condition Piety cost additively (e.g., curing `wounded_1` + `ill` via `heal_disease_minor` charges 15 + 15 = 30 Piety, but still awards flat +2 `benediction` XP).
- **Major Healing Drain:** `heal_disease_benediction` strictly drains **both** Minor and Major Lifeforce simultaneously (`benediction_magic_cast_effect_major_minor`).
- **Attunement Exclusivity:** A character can only hold one attunement modifier at a time (`ancient_attuned`, `enlightenment_attuned`, `bloodline_attuned`, `benediction_attuned`, `hematurgy_attuned`). Selecting a new attunement wipes previous ones (`remove_all_attunement`).
- **Blood Empowerment Hard Cap:** Fully capped tracks (100 XP) are hidden from the `bm_blood_empowerment_event.001` menu. If all 5 tracks are at 100 XP, the fallback `versatility` option fires (+2 all stats 10-year buff).
- **Engine XP Ceiling:** The CK3 engine caps trait track progression at 100 XP. Any excess XP awarded beyond 100 does not roll over and is discarded.

---

## Not verified

- AI frequency and selection weights for multi-target bulk healing vs single-target triage under low piety budgets.
