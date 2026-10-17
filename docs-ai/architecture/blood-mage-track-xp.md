# Blood Mage Track XP & Costs

Living technical specification for XP acquisition, Piety costs, Lifeforce sinks/sources, and track progression.

## Executive Summary

- **What:** Master technical catalog of XP acquisition methods, Piety costs, Lifeforce sinks/sources, cooldowns, and XP values across all lifestyle traits and 12 progression tracks.
- **Traits Covered:** `lifestyle_blood_mage` (5 tracks: `ancient`, `enlightenment`, `bloodline`, `benediction`, `hematurgy`), `lifestyle_blood_empowerment` (5 tracks: `dynasty`, `mastery`, `presence`, `prosperity`, `shadows`), `lifestyle_blood_knight` (5 tracks: `vanguard`, `slaughter`, and shared `ancient`, `benediction`, `enlightenment`).
- **Engine Cap:** Strictly 100 XP max per track (10 tiers at 10 XP steps). Overflow discarded.
- **Stat Parity & Milestone Cleanliness:** Tiers 10–40 and 60–90 scale identical baseline vitality bonuses: `+0.1` Health, `+2` Life Expectancy, `+1` Year Fertility, `+1` Epidemic Resistance. Tiers 50 and 100 skip vitality baselines for distinct milestones and capstones.
- **Apex Devotion (Levels 6–8):** The 100 XP capstones of `ancient`, `enlightenment`, and `benediction` each grant `character_max_piety_level_add = 1` across both Blood Mages and Blood Knights.
- **Age Prowess Lock:** All track capstones at 100 XP grant `no_prowess_loss_from_age = yes`.
- **Cost Types:** Piety, Lifeforce (`minor`, `major`, `superior`), Piety Levels, and cooldowns.

### Master Track Progression Overview

| XP Gain | Cost | Action / Primary Sources | Trait | Track |
| --- | --- | --- | --- | --- |
| +1 to +10 XP | 0 (pulse) / 25–400 Piety + Minor/Major/Superior Lifeforce | Yearly pulse, attunement, condense lifeforce, inscribe blood runes, manifest superior lifeforce | `lifestyle_blood_mage` & `lifestyle_blood_knight` | `ancient` |
| +1 to +10 XP | 75 – 1000 Piety + Minor/Major/Superior Lifeforce | Manifest lifeforce (Learning duel), education enhancements, lifeforce channeling, empowerment | `lifestyle_blood_mage` & `lifestyle_blood_knight` | `enlightenment` |
| +2 to +6 XP | 0 – 500 Piety + Minor/Major/Superior Lifeforce | Grant blood magic, childbirth, bless kin, commune rite, congenital traits, empower bloodline, golems | `lifestyle_blood_mage` | `bloodline` |
| +2 to +8 XP | 15 – 100 Piety + Minor/Major Lifeforce | Curing illnesses (minor, major, deadly), empowering blood knights, restoring drained courtiers | `lifestyle_blood_mage` & `lifestyle_blood_knight` | `benediction` |
| +1 to +2 XP | 25 – 250 Piety (Grants Minor/Major lifeforce) | Prisoner/courtier draining, congenital trait theft, wilderness harvest | `lifestyle_blood_mage` | `hematurgy` |
| +10 XP (chosen track) | 150 Piety + Major Lifeforce | Channel Blood Empowerment decision | `lifestyle_blood_empowerment` | `dynasty`, `mastery`, `presence`, `prosperity`, `shadows` |
| +1 to +10 XP | 0 – 500 Piety + Minor/Major/Superior Lifeforce | Commander/knight battle victories, initiating knights, healing comrades, congenital traits, golem crafting | `lifestyle_blood_knight` | `vanguard` |
| +1 to +10 XP | None / 25 Piety | Single combat fatal kills (Major Lifeforce + 25% Superior chance), tournaments, minor lifedrain, trait theft | `lifestyle_blood_knight` | `slaughter` |

---

## 1. Lifestyle Blood Mage (`lifestyle_blood_mage`)

### 1.1 Ancient Track (`ancient`)

| XP Gain | Cost | Action | Type | Requirements | Cooldown |
| --- | --- | --- | --- | --- | --- |
| **+1 XP** | None | Yearly Pulse | On-action (`blood_mage_yearly_events.001` / `.004`) | Has `lifestyle_blood_mage` or `lifestyle_blood_knight` | 1 year |
| **+1 XP** (**+2 XP** with Superior **Hulinhjálmur**) | None (guaranteed) | Ancient Attunement Pulse | Yearly event (`blood_mage_yearly_events.001` / `.004`) | Has `ancient_attuned` | 1 year |
| Grants `ancient_attuned` | 25 Piety + Minor Lifeforce (`lifeforce_modifier_minor`) | Attune Lifeforce (Ancient) | Decision (`bm_attune_lifeforce_decision`) | Has minor lifeforce, piety >= 25 | None |
| **+2 XP** | 100 Piety + Minor Lifeforce (Forges Major Lifeforce) | Condense Lifeforce | Event option (`bm_cast_blood_magic_minor.001`) | Has minor lifeforce | None |
| **+8 XP** (crit), **+5 XP** (success), **+2 XP** (fail) | 250 Piety + Minor & Major Lifeforce (Generates Superior) | Manifest Superior Lifeforce | Decision (`bm_manifest_superior_lifeforce_decision`) | `piety_level >= 3`, Minor + Major | 2 years |
| **+4 XP** | 0 Piety + Minor Lifeforce (`lifeforce_modifier_minor`) | Inscribe Minor Blood Rune (Self) | Event option (`bm_cast_blood_magic_minor.001`) | `piety_level >= 2` | 5 years |
| **+5 XP** | 200 Piety + Major Lifeforce (`lifeforce_modifier_major`) | Inscribe Major Blood Rune (Self) | Event option (`bm_cast_blood_magic_major.001`) | `piety_level >= 3`, Minor rune | 5 years |
| **+10 XP** | 400 Piety + Superior Lifeforce (`lifeforce_modifier_superior`) | Inscribe Superior Blood Rune (Self) | Event option (`bm_cast_blood_magic_superior.001`) | `piety_level >= 4`, Major rune | 5 years |
| **-5 XP** | 250 Piety + Minor Lifeforce + `wounded_1` | Flay & Swap Minor Rune | Event option (`bm_blood_runes.002`) | Has active Minor rune | None |
| **-10 XP** | 500 Piety + Major Lifeforce + `wounded_1` + Major Exhaustion | Flay & Swap Major Rune | Event option (`bm_blood_runes.002`) | Has active Major rune | None |
| **-15 XP** | 1000 Piety + Superior Lifeforce + `wounded_2` + Superior Exhaustion | Flay & Swap Superior Rune | Event option (`bm_blood_runes.002`) | Has active Superior rune | None |

### 1.2 Enlightenment Track (`enlightenment`)

| XP Gain | Cost | Action | Type | Requirements | Cooldown |
| **+1 / +3 / +5 / +7 XP** | 100 / 250 / 500 / 1000 Piety (Learning duel for Minor, Major, or Superior Lifeforce) | Manifest Lifeforce | Decision (`bm_manifest_lifeforce_decision`) | `piety_level >= 2`, `piety >= 100` | 1 year |
| **+1 XP** | 75 Piety + Minor Lifeforce (`lifeforce_modifier_minor`) | Channel Minor Lifeforce | Event option (`bm_cast_blood_magic_minor.001`) | Minor lifeforce | None |
| **+1 XP** | 25 Piety + Minor Lifeforce (`lifeforce_modifier_minor`) | Grant Lifeforce (Minor) | Interaction (`grant_lifeforce_interaction`) | Minor lifeforce, courtier/prisoner | None |
| **+2 XP** | 50 Piety + Major Lifeforce (`lifeforce_modifier_major`) | Grant Lifeforce (Major) | Interaction (`grant_lifeforce_interaction`) | Major lifeforce, courtier/prisoner | None |
| **+3 XP** (+10 Empowerment XP) | 150 Piety + Major Lifeforce (`lifeforce_modifier_major`) | Channel Blood Empowerment | Event option (`bm_cast_blood_magic_major.001`) | `piety_level >= 1` | None |
| **+5 XP** | 75–200 Piety + Major Lifeforce (`lifeforce_modifier_major`) | Improve Education (2★/3★/4★) | Event option (`bm_cast_blood_magic_major.001`) | `piety_level >= 3` | 2 years |
| **+10 XP** (+10 on duel win) | 350 Piety + Superior Lifeforce (`lifeforce_modifier_superior`) | Master Education (5★) | Event option (`bm_cast_blood_magic_superior.001`) | `piety_level >= 3`, 4★ education | 2 years |
| **+10 XP** | 1000 Piety + Superior Lifeforce (`lifeforce_modifier_superior`) | New Education (2nd Trait) | Event option (`bm_cast_blood_magic_superior.001`) | `piety_level >= 4`, 5★ education | 2 years |
| **+2 XP** (on duel win) | 1000–1500 Piety + Superior Lifeforce (`lifeforce_modifier_superior`) | Manifest Apex Perfection (Congenital 3-5) | Event option (`bm_cast_blood_magic_superior.001`) | `piety_level >= 3` | 5 years |
| **+1 XP** (**+2 XP** with Superior **Hulinhjálmur**) | None (guaranteed) | Enlightenment Attunement Pulse | Yearly event (`blood_mage_yearly_events.001` / `.004`) | Has `enlightenment_attuned` | 1 year |

### 1.3 Bloodline Track (`bloodline`)

| XP Gain | Cost | Action | Type | Requirements | Cooldown |
| --- | --- | --- | --- | --- | --- |
| **+4 XP** (+5 XP if child/kin) | 100 Piety + Major Lifeforce | Grant Blood Magic (Major) | Interaction (`grant_blood_magic_interaction`) | Target non-mage, non-knight | None |
| **+2 XP** | 250 Piety + Minor Lifeforce | Grant Blood Magic (Minor) | Interaction (`grant_blood_magic_interaction`) | Target non-mage, non-knight | None |
| **+2 XP** (+4 XP if child inherits; doubled to +4/+8 by Superior Feingur) | None; **Grants** +1 Major Lifeforce | Childbirth Milestone | On-action (`on_birth_child` -> `bm_on_birth_bloodline_xp`) | Parent is blood mage | Per birth |
| **+2 XP** | 35 Piety + Minor Lifeforce (`lifeforce_modifier_minor`) | Bless Kin's Blood | Interaction (`bm_bless_bloodline_interaction`) | Target child/dynasty kin | 10 years (target buff) |
| **+2 XP** | 50 Piety + Minor Lifeforce (`lifeforce_modifier_minor`) | Bless Dynasty Bloodline (Feingur) | Interaction (`bm_feingur_bless_dynasty_interaction`) | Superior Feingur stave; child or dynasty kin | Permanent |
| **+2 XP** | 50 Piety + Minor Lifeforce (`lifeforce_modifier_minor`) | Purge Bodily Impurities (Congenital Flaw Cleansed) | Event option (`bm_cast_blood_magic_minor.001`) | Has ugly/dull/weak | None |
| **+4 XP** (on duel win) | 200–600 Piety + Major Lifeforce (`lifeforce_modifier_major`) | Manifest Perfection (Congenital 1-2) | Event option (`bm_cast_blood_magic_major.001`) | `piety_level >= 2` | 5 years |
| **+6 XP** (on duel win) | 1000–1500 Piety + Superior Lifeforce (`lifeforce_modifier_superior`) | Manifest Apex Perfection (Congenital 3-5) | Event option (`bm_cast_blood_magic_superior.001`) | `piety_level >= 3` | 5 years |
| **+5 XP** | 350 Piety + Major Lifeforce (`lifeforce_modifier_major`) | Empower Bloodline | Event option (`bm_cast_blood_magic_major.001`) | `exists = house`, `piety_level >= 1` | 3 years |
| **+5 XP** | 500 Piety + Superior Lifeforce (`lifeforce_modifier_superior`) | Forge Blood Golem | Decision (`blood_golem_creation_decision`) | `piety_level >= 3`, Superior lifeforce | 3 years |
| **+1 XP** (+10% chance per active house modifier, up to 70%) | None | Yearly Dynasty Modifiers Pulse | On-action (`blood_mage_yearly_events.002`) | Has house, house modifiers | 1 year |
| **+1 XP** (**+2 XP** with Superior **Hulinhjálmur**) | None (guaranteed) | Bloodline Attunement Pulse | Yearly event (`blood_mage_yearly_events.001`) | Has `bloodline_attuned` | 1 year |

### 1.4 Benediction Track (`benediction`)

| XP Gain | Cost | Action | Type | Requirements | Cooldown |
| --- | --- | --- | --- | --- | --- |
| **+2 XP** | 15 Piety (`cure_illness_cost_minor_neg`) + Minor Lifeforce (`lifeforce_modifier_minor`) | **Heal Affliction: Minor** (`bm_heal_ailment`) | Interaction & Event | Target with `wounded_1`, `ill`, `lovers_pox`, `gout_ridden`, `scarred` | None |
| **+4 XP** | 35 Piety (`cure_illness_cost_major_neg`) + Major Lifeforce (`lifeforce_modifier_major`) | **Heal Affliction: Major** (`bm_heal_ailment`) | Interaction & Event | Target with `wounded_2`, `incapable`, `pneumonic`, `infirm`, `maimed`, etc. | None |
| **+8 XP** | 100 Piety (`cure_illness_cost_benediction_neg`) + **both** Minor & Major Lifeforce | **Heal Affliction: Deadly** (`bm_heal_ailment`) | Interaction & Event | Target with `wounded_3`, `cancer`, `plague`, `leper`, `disfigured`, etc. | None |
| **+4 XP** (caster) | 0 Piety + Major Lifeforce (`lifeforce_modifier_major`) | Empower Blood Knight (Major) | Interaction (`empower_blood_knight_interaction`) | Blood Knight caster; Target is blood knight | None |
| **+2 XP** (caster) | 0 Piety + Minor Lifeforce (`lifeforce_modifier_minor`) | Empower Blood Knight (Minor) | Interaction (`empower_blood_knight_interaction`) | Blood Knight caster; Target is blood knight | None |
| **+4 XP** | 25 Piety + Major Lifeforce (`lifeforce_modifier_major`) | Restore Lifedrained Courtier | Interaction (`grant_lifeforce_interaction_reversed`) | Target has `lifedrained_modifier` | None |
| **+4 XP** (caster) | 0 Piety + Minor Lifeforce (`lifeforce_modifier_minor`) | Inscribe Minor Rune on Other | Interaction (`bm_inscribe_rune_other_interaction`) | `piety_level >= 2`, 25 Track XP | 5 years |
| **+5 XP** (caster) | 200 Piety + Major Lifeforce (`lifeforce_modifier_major`) | Upgrade Major Rune on Other | Interaction (`bm_inscribe_rune_other_interaction`) | `piety_level >= 3`, 50 Track XP, Minor rune | 5 years |
| **+10 XP** (caster) | 400 Piety + Superior Lifeforce (`lifeforce_modifier_superior`) | Upgrade Superior Rune on Other | Interaction (`bm_inscribe_rune_other_interaction`) | Blood Mage, `piety_level >= 4`, 100 Track XP, Major rune | 5 years |
| **+1 XP** (**+2 XP** with Superior **Hulinhjálmur**) | None (guaranteed) | Benediction Attunement Pulse | Yearly event (`blood_mage_yearly_events.001`) | Has `benediction_attuned` | 1 year |

### 1.5 Hematurgy Track (`hematurgy`)

| XP Gain | Cost | Action | Type | Requirements | Cooldown |
| --- | --- | --- | --- | --- | --- |
| **+2 XP** | 50 Piety (`lifedrain_piety_cost_major`); **Grants** Major Lifeforce (Executes victim) | Lifedrain Prisoner | Interaction (`lifedrain_prisoner_event_interaction`) | Imprisoned target | None |
| **+1 XP** | 25 Piety (`lifedrain_piety_cost_minor`); **Grants** Minor Lifeforce | Lifedrain Courtier | Interaction (`lifedrain_courtier_event_interaction`) | Courtier/prisoner not recently drained | 3 months |
| **+2 XP** (win), **+4 XP** (crit), **+1 XP** (fail) | 50 Piety + Minor Lifeforce (Crit siphons Minor Lifeforce back) | Cast Blood Curse | Interaction (`bm_curse_blood_interaction`) | >= 10 Hematurgy XP | 1 year |
| **+2 XP** (on duel win) | 100–325 Piety + Major Lifeforce (Executes victim) | Drain Prisoner Trait (Lvl 1–5) | Interaction + Event (`bm_trait_drain.001`) | Prisoner with congenital trait | 60 days |
| **+1 XP** (**+2 XP** with Superior **Hulinhjálmur**) | None (guaranteed) | Hematurgy Attunement Pulse | Yearly event (`blood_mage_yearly_events.001`) | Has `hematurgy_attuned` | 1 year |

---

## 2. Lifestyle Blood Empowerment (`lifestyle_blood_empowerment`)

Tracks: `dynasty`, `mastery`, `presence`, `prosperity`, `shadows` (5 tracks total).

| XP Gain | Cost | Action | Type | Requirements | Cooldown |
| --- | --- | --- | --- | --- | --- |
| **+10 XP** in chosen track (+3 `enlightenment` XP) | 150 Piety + Major Lifeforce (`lifeforce_modifier_major`) | Channel Blood Empowerment (`bm_cast_blood_magic_major_decision` -> `bm_blood_empowerment_event.001`) | Decision -> Event | `piety_level >= 1`, Major lifeforce held | None |
| **0 XP** (strictly manual advancement) | None | Passive Growth | None | None | None |

---

## 3. Lifestyle Blood Knight (`lifestyle_blood_knight`)

Tracks: `vanguard`, `slaughter` (and shared `ancient`, `benediction`, `enlightenment`).

| XP Gain | Cost | Action | Type | Requirements | Cooldown |
| --- | --- | --- | --- | --- | --- |
| **+10 XP to martial tracks** (`vanguard` & `slaughter`) | 0 Piety (knight); Caster consumes Major Lifeforce | Empower Blood Knight: Major | Interaction (`empower_blood_knight_interaction`) | Fellow Blood Knight empowers knight | None |
| **+5 XP to martial tracks** (`vanguard` & `slaughter`) | 0 Piety (knight); Caster consumes Minor Lifeforce | Empower Blood Knight: Minor | Interaction (`empower_blood_knight_interaction`) | Fellow Blood Knight empowers knight | None |
| **+4 XP** (caster) (`benediction`) | 0 Piety + Major Lifeforce | Empower Blood Knight: Major (Caster) | Interaction (`empower_blood_knight_interaction`) | Blood Knight empowers sworn knight | None |
| **+2 XP** (caster) (`benediction`) | 0 Piety + Minor Lifeforce | Empower Blood Knight: Minor (Caster) | Interaction (`empower_blood_knight_interaction`) | Blood Knight empowers sworn knight | None |
| **+4 XP** (`vanguard`) | 100 Piety + Major Lifeforce | Make Blood Knight (Major) | Interaction (`make_blood_knight_interaction`) | Blood Knight initiates knight | None |
| **+2 XP** (`vanguard`) | 250 Piety + Minor Lifeforce | Make Blood Knight (Minor) | Interaction (`make_blood_knight_interaction`) | Blood Knight initiates knight | None |
| **+2 XP** (`vanguard`) | 35 Piety + Minor Lifeforce | Bless Kin's Blood | Interaction (`bm_bless_bloodline_interaction`) | Target child/dynasty kin | 10 years (target buff) |
| **+2 to +5 XP** (`vanguard`) | None; Scaled Lifeforce Harvest (10%–100% Minor, 0%–100% Major) | Battle Victory (Commander) | On-action (`bm_on_combat_end_winner`) | Army commander; scales by battle size (<100 to 10k+) | Per battle |
| **+1 to +5 XP** (`vanguard`) | None; Scaled Lifeforce Harvest (10%–100% Minor, 0%–100% Major) | Battle Victory (Knight) | On-action (`bm_on_combat_end_winner`) | Army knight; scales by battle size (<100 to 10k+) | Per battle |
| **+1 XP** (`vanguard`) + **+1 XP** (`benediction`) | 15 Piety + Minor Lifeforce | Heal Minor Affliction (Comrade / Knight / Liege) | Interaction & Event (`bm_heal_ailment`) | Target ally with minor ailment | None |
| **+2 XP** (`vanguard`) + **+2 XP** (`benediction`) | 35 Piety + Major Lifeforce | Heal Major Affliction (Comrade / Knight / Liege) | Interaction & Event (`bm_heal_ailment`) | Target ally with major ailment | None |
| **+8 XP** (`benediction`) | 100 Piety + Minor & Major Lifeforce | Heal Deadly Affliction (Comrade / Knight / Liege) | Interaction & Event (`bm_heal_ailment`) | Target with deadly ailment | None |
| **+4 XP** (`vanguard`) | 200–600 Piety + Major Lifeforce | Manifest Perfection (Congenital 1-2) | Event option (`bm_cast_blood_magic_major.001`) | `piety_level >= 2` | 5 years |
| **+6 XP** (`vanguard`) + **+2 XP** (`enlightenment`) | 1000–1500 Piety + Superior Lifeforce | Manifest Apex Perfection (Congenital 3-5) | Event option (`bm_cast_blood_magic_superior.001`) | `piety_level >= 3` | 5 years |
| **+5 XP** (`vanguard`) | 350 Piety + Major Lifeforce | Empower Bloodline | Event option (`bm_cast_blood_magic_major.001`) | `exists = house`, `piety_level >= 1` | 3 years |
| **+5 XP** (`vanguard`) | 500 Piety + Superior Lifeforce | Forge Blood Golem | Decision (`blood_golem_creation_decision`) | `piety_level >= 3`, Superior lifeforce | 3 years |
| **+1 to +3 XP** (`vanguard`) + **0 to +2 XP** (`enlightenment`) | None | Battle Defeat (Surviving Commander / Knight) | On-action (`bm_on_combat_end_loser`) | Surviving side commander or knight | Per battle |
| **+2 XP** (`vanguard`) (+4 XP if child inherits; doubled to +4/+8 by Superior Feingur) | None | Childbirth Milestone | On-action (`on_birth_child` -> `bm_on_birth_bloodline_xp`) | Parent is blood knight | Per birth |
| **+5 XP** (`slaughter`) | None; **Grants** Major Lifeforce (25% chance Superior if victim prowess >= 35 or blood trait) | Single Combat Fatal Slaying | On-action (`bm_on_character_death_duel`) | Slaying opponent in single combat | None |
| **+3 XP** (`slaughter`) | None | Tournament Completion | On-action (`bm_on_travel_activity_complete_tournament`) | Completing `activity_tournament` | Per tourney |
| **+1 to +2 XP** (`slaughter` / `enlightenment`) | None | Seek Power Wilderness Harvest | Decision & Event (`seek_power.001`) | Blood knight | 1–2 years |
| **+1 / +3 / +5 / +7 XP** (`enlightenment`) | 100 / 250 / 500 / 1000 Piety; **Grants** Minor, Major, or Superior Lifeforce on Learning duel | Manifest Lifeforce | Decision (`bm_manifest_lifeforce_decision`) | `piety_level >= 2`, `piety >= 100` | 1 year |
| **+8/+5/+2 XP** (`ancient`) | 250 Piety + Minor & Major Lifeforce; **Grants** Superior Lifeforce | Manifest Superior Lifeforce | Decision (`bm_manifest_superior_lifeforce_decision`) | `piety_level >= 3`, Minor + Major | 2 years |
| **+2 XP** (`ancient`) | 100 Piety + Minor Lifeforce; **Grants** Major Lifeforce | Condense Lifeforce | Event option (`bm_cast_blood_magic_minor.001`) | Minor lifeforce held | None |
| **+3 XP** (`enlightenment`) (+10 Empowerment XP) | 150 Piety + Major Lifeforce | Channel Blood Empowerment | Decision -> Event (`bm_cast_blood_magic_major.001`) | `piety_level >= 1`, Major lifeforce held | None |
| **+2 XP** (`enlightenment`) | 15 Piety + Minor Lifeforce | Heal Minor Affliction (Self-Healing Wounds) | Interaction & Event (`bm_heal_ailment`) | Self has minor wound/illness | None |
| **+4 XP** (`enlightenment`) | 35 Piety + Major Lifeforce | Heal Major Affliction (Self-Healing Major Ailments) | Interaction & Event (`bm_heal_ailment`) | Self has major ailment | None |
| **+1 XP** (`slaughter`) | 25 Piety; **Grants** Minor Lifeforce | Minor Lifedrain (Courtier / Prisoner) | Interaction (`lifedrain_courtier_event_interaction`) | Siphoning victim via prowess | 3 months |
| **+2 XP** (`slaughter`) | 100–325 Piety + Major Lifeforce | Trait Drain (Prisoner, up to rank 5) | Interaction & Event (`trait_drain_prisoner_event_interaction`) | Draining congenital trait from prisoner | 60 days (15d w/ Superior Hulinhjálmur) |
| **+5 XP** (`enlightenment`) | 75–200 Piety + Major Lifeforce | Improve Education (Tiers 1★ to 4★) | Decision & Event (`bm_cast_blood_magic_major.001`) | Holds any education trait below rank 4 | 2 years |
| **+10 XP** (+10 on win) (`enlightenment`) | 350 Piety + Superior Lifeforce | Master Education (Tier 5★) | Decision & Event (`bm_cast_blood_magic_superior.001`) | Holds 4★ education trait | 2 years |
| **+10 XP** (`enlightenment`) | 1000 Piety + Superior Lifeforce | Embrace New Education (2nd Trait) | Decision & Event (`bm_cast_blood_magic_superior.001`) | `piety_level >= 4`, holds 5★ education | 2 years |
| **+4 XP** (`ancient`) | 0 Piety + Minor Lifeforce | Inscribe Minor Blood Rune (Self) | Event option (`bm_cast_blood_magic_minor.001`) | `piety_level >= 2` | 5 years |
| **+5 XP** (`ancient`) | 200 Piety + Major Lifeforce | Inscribe Major Blood Rune (Self) | Event option (`bm_cast_blood_magic_major.001`) | `piety_level >= 3`, Minor rune | 5 years |
| **+10 XP** (`ancient`) | 400 Piety + Superior Lifeforce | Inscribe Superior Blood Rune (Self) | Event option (`bm_cast_blood_magic_superior.001`) | `piety_level >= 4`, Major rune | 5 years |
| **+4 XP** (`benediction`) | 0 Piety + Minor Lifeforce | Inscribe Minor Rune on Other | Interaction (`bm_inscribe_rune_other_interaction`) | `piety_level >= 2`, 25 Track XP | 5 years |
| **+5 XP** (`benediction`) | 200 Piety + Major Lifeforce | Upgrade Major Rune on Other | Interaction (`bm_inscribe_rune_other_interaction`) | `piety_level >= 3`, 50 Track XP, Minor rune | 5 years |
| **-5 / -10 / -15 XP** (`ancient`) | 250 / 500 / 1000 Piety + Lifeforce + Wound | Flay & Swap Minor / Major / Superior Rune | Event option (`bm_blood_runes.002`) | Has active Minor / Major / Superior rune | None |
| **+1 XP** (`enlightenment`) + **+1 XP** (`ancient`) | None (33% ambient roll for Minor Lifeforce) | Yearly Survival Pulse | On-action (`blood_mage_yearly_events.004`) | Has `lifestyle_blood_knight` | 1 year |
| **+1 XP** (**+2 XP** with Superior **Hulinhjálmur**) (`vanguard` / `slaughter` / `ancient` / `benediction` / `enlightenment`) | None (guaranteed) | Discipline Attunement Pulse | Yearly event (`blood_mage_yearly_events.004`) | Has matching `<track>_attuned` | 1 year |

## Where the details live

| Subsystem | Key Files |
| --- | --- |
| XP Helper Macros | `common/scripted_effects/bm_trait_track_xp_gain_effects.txt` |
| Blood Magic Scripted Effects | `common/scripted_effects/bm_blood_magic_used_effects.txt` |
| Blood Runes & Galdrastafir | `common/modifiers/bm_blood_runes_modifiers.txt`<br>`common/script_values/bm_blood_rune_cost.txt`<br>`common/scripted_effects/bm_blood_runes_effects.txt`<br>`common/character_interactions/bm_inscribe_rune_other.txt`<br>`events/bm_blood_runes_events.txt` |
| Cure Illness Interactions & Costs | `common/character_interactions/bm_cure_illness_interactions.txt`<br>`common/script_values/bm_cure_illness_values.txt` |
| Drain & Grant Interactions & Costs | `common/character_interactions/bm_drain_lifeforce.txt`<br>`common/character_interactions/bm_grant_lifeforce.txt`<br>`common/character_interactions/bm_grant_blood_magic.txt`<br>`common/character_interactions/bm_bless_bloodline.txt` |
| Trait Drain Duel & Events | `common/character_interactions/bm_drain_trait.txt`<br>`events/bm_trait_drain_events.txt`<br>`common/scripted_effects/bm_drain_trait_effects.txt` |
| Education Enhancement Costs & Duels | `common/script_values/bm_education_enhancement_piety_cost.txt`<br>`common/scripted_effects/bm_education_duel_effect.txt` |
| Congenital Trait Manifestation | `common/scripted_effects/bm_manifest_traits_effects.txt`<br>`events/bm_channel_manifest_traits_events.txt` |
| Blood Empowerment Events | `events/bm_blood_empowerment_event.txt` |
| Blood Knight Interactions & Hooks | `common/character_interactions/bm_blood_knight_interactions.txt`<br>`common/on_action/bm_combat_on_actions.txt`<br>`common/on_action/bm_duel_on_actions.txt` |
| Yearly Pulse, Attunements & Birth | `events/bm_yearly_events.txt`<br>`common/decisions/cast_magic/bm_attune_lifeforce_decision.txt`<br>`common/on_action/bm_blood_mage_prevalence_on_actions.txt` |
