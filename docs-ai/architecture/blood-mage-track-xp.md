# Blood Mage Track XP & Costs

> Living document describing current state. Follow `AGENTS.md`: high-density technical specs, zero roleplay fluff.

## Executive Summary

- **What:** Master technical catalog of XP acquisition methods, Piety costs, Lifeforce sinks/sources, cooldowns, and XP values across all 3 lifestyle traits and 13 progression tracks.
- **Traits Covered:** `lifestyle_blood_mage` (5 tracks: `ancient`, `enlightenment`, `bloodline`, `benediction`, `hematurgy`), `lifestyle_blood_empowerment` (5 tracks: `dynasty`, `mastery`, `presence`, `prosperity`, `shadows`), `lifestyle_blood_knight` (3 tracks: `vanguard`, `slaughter`, `resilience`).
- **Engine Cap:** Strictly 100 XP max per track (10 tiers at 10 XP steps). Overflow discarded.
- **Cost Types:** Piety, Lifeforce (`minor`, `major`, `superior`), Piety Levels, and cooldowns.

### Master Track Progression Overview

| Trait | Track | Primary Sources | Piety Cost | Lifeforce Cost / Yield | XP Yield |
| --- | --- | --- | --- | --- | --- |
| `lifestyle_blood_mage` | `ancient` | Yearly pulse; Attunement roll | 0 (pulse) / 25 (attune) | None (pulse) / Minor sink (attune) | +1 XP/yr; +1 XP (50% roll) |
| `lifestyle_blood_mage` | `enlightenment` | Manifestations, education, empowerment, grant | 25 – 1000 Piety | Minor/Major/Superior sink | +1 to +10 XP |
| `lifestyle_blood_mage` | `bloodline` | Empower bloodline, Golem forge, house modifiers | 0 – 500 Piety | Major/Superior sink | +1 to +5 XP |
| `lifestyle_blood_mage` | `benediction` | Curing illness, granting power, blood runes | 0 – 400 Piety (scaled) | Minor/Major/Superior sink | +2 to +10 XP |
| `lifestyle_blood_mage` | `hematurgy` | Prisoner/courtier draining, trait draining, duels | 25 – 250 Piety | Minor/Major SOURCE | +1 to +2 XP |
| `lifestyle_blood_empowerment` | `dynasty`, `mastery`, `presence`, `prosperity`, `shadows` | Channel Blood Empowerment decision | 150 Piety | Consumes Major Lifeforce | +10 XP (chosen track) |
| `lifestyle_blood_knight` | `vanguard`, `slaughter`, `resilience` | Knight empowerment interaction | 0 Piety (target) | Consumes Minor/Major Lifeforce | +5 or +10 XP (all 3 tracks) |
| `lifestyle_blood_knight` | `vanguard` | Battle victories & surviving defeats | 0 Piety | None | +1, +5, or +6 XP |
| `lifestyle_blood_knight` | `slaughter` | Single combat kills; tournament completion | 0 Piety | None | +3 or +6 XP |
| `lifestyle_blood_knight` | `resilience` | Yearly survival pulse; defeat survival | 0 Piety | None | +1 XP |

---

## 1. Lifestyle Blood Mage (`lifestyle_blood_mage`)

### 1.1 Ancient Track (`ancient`)

| Action / Trigger | Type | Requirements | Piety Cost | Lifeforce | Cooldown | XP Yield |
| --- | --- | --- | --- | --- | --- | --- |
| Yearly Pulse | On-action (`blood_mage_yearly_events.001`) | Has `lifestyle_blood_mage` | 0 | None | 1 year | **+1 XP** |
| Ancient Attunement Roll | Yearly event roll (`blood_mage_yearly_events.001`) | Has `ancient_attuned` | 0 (50% roll) | None | 1 year | **+1 XP** |
| Attune Lifeforce (Ancient) | Event option (`bm_cast_blood_magic_minor.001`) | Has minor lifeforce | 25 Piety | Consumes `lifeforce_modifier_minor` | None | Grants `ancient_attuned` |

### 1.2 Enlightenment Track (`enlightenment`)

| Action / Trigger | Type | Requirements | Piety Cost | Lifeforce | Cooldown | XP Yield |
| --- | --- | --- | --- | --- | --- | --- |
| Channel Minor Lifeforce | Event option (`bm_cast_blood_magic_minor.001`) | Minor lifeforce | 75 Piety | Consumes `lifeforce_modifier_minor` | None | **+1 XP** |
| Grant Lifeforce (Minor) | Interaction (`grant_lifeforce_interaction`) | Minor lifeforce, courtier/prisoner | 25 Piety | Consumes `lifeforce_modifier_minor` | None | **+1 XP** |
| Grant Lifeforce (Major) | Interaction (`grant_lifeforce_interaction`) | Major lifeforce, courtier/prisoner | 50 Piety | Consumes `lifeforce_modifier_major` | None | **+2 XP** |
| Channel Blood Empowerment | Event option (`bm_cast_blood_magic_major.001`) | `piety_level >= 1` | 150 Piety | Consumes `lifeforce_modifier_major` | None | **+3 XP** (+10 Empowerment XP) |
| Manifest Lifeforce | Decision (`bm_manifest_lifeforce_decision`) | `piety_level >= 2` | 100 Piety | Generates Minor or Major on duel | 1 year | **+5 XP** |
| Improve Education (2★/3★/4★) | Event option (`bm_cast_blood_magic_major.001`) | `piety_level >= 3` | Scaled: 75 (1->2), 125 (2->3), 200 (3->4) Piety | Consumes `lifeforce_modifier_major` | 2 years | **+5 XP** |
| Manifest Perfection (Congenital 1-3) | Event option (`bm_cast_blood_magic_major.001`) | `piety_level >= 2` | 200 Piety | Consumes `lifeforce_modifier_major` | None | **+5 XP** (on duel success) |
| Manifest Superior Lifeforce | Decision (`bm_manifest_superior_lifeforce_decision`) | `piety_level >= 3`, Minor + Major | 250 Piety | Consumes Minor + Major; Generates Superior | 2 years | **+10 XP** (crit), **+5 XP** (success), **+2 XP** (fail) |
| Master Education (5★) | Event option (`bm_cast_blood_magic_superior.001`) | `piety_level >= 3`, 4★ education | 350 Piety | Consumes `lifeforce_modifier_superior` | 2 years | **+10 XP** upfront (+10 XP on duel win) |
| New Education (2nd Trait) | Event option (`bm_cast_blood_magic_superior.001`) | `piety_level >= 4`, 5★ education | 1000 Piety | Consumes `lifeforce_modifier_superior` | 2 years | **+10 XP** |
| Enlightenment Attunement Roll | Yearly event roll (`blood_mage_yearly_events.001`) | Has `enlightenment_attuned` | 0 (50% roll) | None | 1 year | **+1 XP** |

### 1.3 Bloodline Track (`bloodline`)

| Action / Trigger | Type | Requirements | Piety Cost | Lifeforce | Cooldown | XP Yield |
| --- | --- | --- | --- | --- | --- | --- |
| Empower Bloodline | Event option (`bm_cast_blood_magic_major.001`) | `exists = house`, `piety_level >= 1` | 350 Piety | Consumes `lifeforce_modifier_major` | 3 years | **+5 XP** |
| Forge Blood Golem | Decision (`blood_golem_creation_decision`) | `piety_level >= 3`, Superior lifeforce | 500 Piety | Consumes `lifeforce_modifier_superior` | 3 years | **+5 XP** |
| Yearly Dynasty Modifiers Pulse | On-action (`blood_mage_yearly_events.002`) | Has house, house modifiers | 0 | None | 1 year | **+1 XP** (+5% chance per active house modifier, up to 35%) |
| Bloodline Attunement Roll | Yearly event roll (`blood_mage_yearly_events.001`) | Has `bloodline_attuned` | 0 (50% roll) | None | 1 year | **+1 XP** |

### 1.4 Benediction Track (`benediction`)

| Action / Trigger | Type | Requirements | Piety Cost | Lifeforce | Cooldown | XP Yield |
| --- | --- | --- | --- | --- | --- | --- |
| **Heal Disease: Minor** (`heal_disease_minor`) | Interaction | Self or courtier with `wounded_1`, `ill`, `lovers_pox`, `gout_ridden`, `scarred` | **15 Piety per trait cured** (`cure_illness_cost_minor`) | Consumes `lifeforce_modifier_minor` | None | **+2 XP** |
| **Heal Disease: Major** (`heal_disease_major`) | Interaction | Self or courtier with `wounded_2`, `incapable`, `pneumonic`, `early_great_pox`, `infirm`, `withering_mind`, `clouded_eyes`, `fragile_bones`, `maimed`, `consumption`, `typhus`, `measles`, `blind`, `one_eyed`, `weak`, `lunatic_1`, `possessed_1`, `dull`, `depressed_1` | **35 Piety per trait cured** (`cure_illness_cost_major`) | Consumes `lifeforce_modifier_major` | None | **+4 XP** |
| **Heal Disease: Benediction** (`heal_disease_benediction`) | Interaction | Self or courtier with `wounded_3`, `sickly`, `great_pox`, `cancer`, `bubonic_plague`, `smallpox`, `leper`, `impotent`, `dysentery`, `ergotism`, `disfigured`, `one_legged`, `faltering_heart` | **100 Piety per trait cured** (`cure_illness_cost_benediction`) | Consumes **both** `lifeforce_modifier_minor` AND `lifeforce_modifier_major` | None | **+8 XP** |
| Grant Blood Magic | Interaction (`grant_blood_magic_interaction`) | Target without blood mage | 75 Piety | Consumes `lifeforce_modifier_major` | None | **+4 XP** |
| Make Blood Knight | Interaction (`make_blood_knight_interaction`) | Target without blood knight | 100 Piety | Consumes `lifeforce_modifier_major` | None | **+4 XP** |
| Empower Blood Knight (Major) | Interaction (`empower_blood_knight_interaction`) | Target is blood knight | 0 Piety | Consumes `lifeforce_modifier_major` | None | **+4 XP** (caster) |
| Empower Blood Knight (Minor) | Interaction (`empower_blood_knight_interaction`) | Target is blood knight | 0 Piety | Consumes `lifeforce_modifier_minor` | None | **+2 XP** (caster) |
| Restore Lifedrained Courtier | Interaction (`grant_lifeforce_interaction_reversed`) | Target has `lifedrained_modifier` | 25 Piety | Consumes `lifeforce_modifier_major` | None | **+4 XP** |
| Inscribe Minor Blood Rune | Event option (`bm_cast_blood_magic_major.001`) | `piety_level >= 2` | 0 Piety | Consumes Minor + Major | 5 years | **+5 XP** |
| Inscribe Major Blood Rune | Event option (`bm_cast_blood_magic_major.001`) | `piety_level >= 3`, Minor rune | 200 Piety | Consumes Minor + Major | 5 years | **+5 XP** |
| Inscribe Superior Blood Rune | Event option (`bm_cast_blood_magic_superior.001`) | `piety_level >= 4`, Major rune | 400 Piety | Consumes Superior | 5 years | **+10 XP** |
| Benediction Attunement Roll | Yearly event roll (`blood_mage_yearly_events.001`) | Has `benediction_attuned` | 0 (50% roll) | None | 1 year | **+1 XP** |

### 1.5 Hematurgy Track (`hematurgy`)

| Action / Trigger | Type | Requirements | Piety Cost | Lifeforce | Cooldown | XP Yield |
| --- | --- | --- | --- | --- | --- | --- |
| Lifedrain Prisoner | Interaction (`lifedrain_prisoner_event_interaction`) | Imprisoned target | 50 Piety (`lifedrain_piety_cost_major`) | **Grants** `lifeforce_modifier_major` (Executes victim) | None | **+2 XP** |
| Lifedrain Courtier | Interaction (`lifedrain_courtier_event_interaction`) | Courtier/prisoner not recently drained | 25 Piety (`lifedrain_piety_cost_minor`) | **Grants** `lifeforce_modifier_minor` | 3 months | **+1 XP** |
| Drain Prisoner Trait (Lvl 1 / Fecund / Giant) | Interaction + Event (`bm_trait_drain.001`) | Prisoner with trait | 100 Piety (`trait_drain_base_piety_cost`) | Consumes `lifeforce_modifier_major` (Executes victim) | 60 days | **+2 XP** (on duel win) |
| Drain Prisoner Trait (Lvl 2) | Interaction + Event (`bm_trait_drain.001`) | Prisoner with rank 2 trait | 175 Piety (100 base + 75 lvl 2) | Consumes `lifeforce_modifier_major` (Executes victim) | 60 days | **+2 XP** (on duel win) |
| Drain Prisoner Trait (Lvl 3) | Interaction + Event (`bm_trait_drain.001`) | Prisoner with rank 3 trait | 250 Piety (100 base + 150 lvl 3) | Consumes `lifeforce_modifier_major` (Executes victim) | 60 days | **+2 XP** (on duel win) |
| Single Combat Fatal Slaying | On-action (`bm_on_character_death_duel`) | Killer is blood mage in single combat duel | 0 Piety | **Grants** `lifeforce_modifier_major` | None | **+2 XP** |
| Hematurgy Attunement Roll | Yearly event roll (`blood_mage_yearly_events.001`) | Has `hematurgy_attuned` | 0 (50% roll) | None | 1 year | **+1 XP** |

---

## 2. Lifestyle Blood Empowerment (`lifestyle_blood_empowerment`)

Tracks: `dynasty`, `mastery`, `presence`, `prosperity`, `shadows` (5 tracks total).

| Action / Trigger | Type | Requirements | Piety Cost | Lifeforce | Cooldown | XP Yield |
| --- | --- | --- | --- | --- | --- | --- |
| Channel Blood Empowerment (`bm_cast_blood_magic_major_decision` -> `bm_blood_empowerment_event.001`) | Decision -> Event | `piety_level >= 1`, Major lifeforce held | 150 Piety | Consumes `lifeforce_modifier_major` | None | **+10 XP** in chosen track (also +3 `enlightenment` XP) |
| Passive Growth | None | None | N/A | N/A | N/A | **0 XP** (strictly manual advancement) |

---

## 3. Lifestyle Blood Knight (`lifestyle_blood_knight`)

Tracks: `vanguard`, `slaughter`, `resilience` (3 tracks total).

| Action / Trigger | Type | Requirements | Piety Cost | Lifeforce | Cooldown | XP Yield |
| --- | --- | --- | --- | --- | --- | --- |
| Empower Blood Knight: Major | Interaction (`empower_blood_knight_interaction`) | Blood Mage empowers knight | 0 Piety (knight) | Caster consumes `lifeforce_modifier_major` | None | **+10 XP to all 3 tracks** (`vanguard`, `slaughter`, `resilience`) |
| Empower Blood Knight: Minor | Interaction (`empower_blood_knight_interaction`) | Blood Mage empowers knight | 0 Piety (knight) | Caster consumes `lifeforce_modifier_minor` | None | **+5 XP to all 3 tracks** (`vanguard`, `slaughter`, `resilience`) |
| Battle Victory (Commander) | On-action (`bm_on_combat_end_winner`) | Army commander | 0 | None | Per battle | **+6 XP** (`vanguard`) |
| Battle Victory (Knight) | On-action (`bm_on_combat_end_winner`) | Army knight | 0 | None | Per battle | **+5 XP** (`vanguard`) |
| Battle Defeat (Surviving Commander / Knight) | On-action (`bm_on_combat_end_loser`) | Surviving side commander or knight | 0 | None | Per battle | **+1 XP** (`vanguard`) + **+1 XP** (`resilience`) |
| Single Combat Fatal Slaying | On-action (`bm_on_character_death_duel`) | Slaying opponent in single combat | 0 | None | None | **+6 XP** (`slaughter`) |
| Tournament Completion | On-action (`bm_on_travel_activity_complete_tournament`) | Completing `activity_tournament` | 0 | None | Per tourney | **+3 XP** (`slaughter`) |
| Yearly Survival Pulse | On-action (`blood_mage_yearly_events.004`) | Has `lifestyle_blood_knight` | 0 | None | 1 year | **+1 XP** (`resilience`) |

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
