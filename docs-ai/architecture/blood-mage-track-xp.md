# Blood Mage Track XP & Costs (Hub)

XP sources, Piety costs, Lifeforce sinks/sources, cooldowns for all lifestyle track progression. Per-trait detail: [mage](blood-mage-track-xp-mage.md) (`bloodline`, `hematurgy`, `bloodlust`), [power](blood-mage-track-xp-power.md) (`lifestyle_blood_power`). This file: shared rules and the devotion tracks on Blood Mage (`ancient`, `enlightenment`, `benediction`).

## Shared Rules

- **Engine cap**: 100 XP max per track (10 tiers at 10 XP steps). Overflow discarded.
- **Traits/tracks**: `lifestyle_blood_mage` (`ancient`, `enlightenment`, `bloodline`, `benediction`, `hematurgy`, `bloodlust`); `lifestyle_blood_power` (`dynasty`, `warband`, `mastery`, `presence`, `prosperity`, `shadows`).
- **Vitality baseline**: Tiers 10–40 and 60–90 on `lifestyle_blood_mage` give `+0.1` Health, `+2.5` Life Expectancy, `+1.25` Year Fertility, `+1` Epidemic Resistance. Tiers 50 and 100 award 4× and 8× vitality milestones. `lifestyle_blood_power` has no vitality baseline.
- **Apex Devotion (Levels 6–8)**: 100 XP capstones of `ancient`, `enlightenment`, `benediction` each grant `character_max_piety_level_add = 1`.
- **Age lock**: every track capstone at 100 XP grants `no_prowess_loss_from_age = yes`.
- **Cost types**: Piety, Lifeforce (`lifeforce_modifier_minor` / `lifeforce_modifier_major` / `lifeforce_modifier_superior`), Piety Levels (`piety_level`), cooldowns. "Grants" = action yields Lifeforce.

## Track Overview

| Trait | Track | XP per action | Cost range |
| --- | --- | --- | --- |
| Mage | `ancient` | +1 to +10 | 0 (pulse) / 25–400 Piety + Minor/Major/Superior |
| Mage | `enlightenment` | +1 to +5 | 75 – 1000 Piety + Minor/Major/Superior |
| Mage | `benediction` | +1 to +4 | 15 – 100 Piety + Minor/Major |
| Mage | `bloodline` | +1 to +3 | 0 – 500 Piety + Minor/Major/Superior |
| Mage | `hematurgy` | +1 | 25 – 250 Piety (grants Minor/Major) |
| Mage | `bloodlust` | +1 to +5 | 0 Piety (battle / single combat / duels) |
| Power | chosen track | +10 | 150 Piety + Major |

## Attunement Pulses (all tracks)

Guaranteed, no cost, 1 year cooldown: **+1 XP** (**+2 XP** with Superior **Hulinhjálmur**) when holder has `<track>_attuned` (e.g. `ancient_attuned`, `enlightenment_attuned`, `benediction_attuned`, `bloodline_attuned`, `hematurgy_attuned`, `bloodlust_attuned`).

| Track | Event |
| --- | --- |
| `ancient`, `enlightenment`, `benediction`, `bloodline`, `hematurgy`, `bloodlust` | `blood_mage_yearly_events.001` |

## `ancient`

| XP | Cost | Action | Source | Req | CD |
| --- | --- | --- | --- | --- | --- |
| +1 | None | Yearly Pulse | on-action `blood_mage_yearly_events.001` | `lifestyle_blood_mage` | 1 year |
| grants `ancient_attuned` | Initial free; change: 100 Piety + Minor (`lifeforce_modifier_minor`) | Attune Lifeforce | decision `bm_attune_lifeforce_decision` | Change: Minor lifeforce, piety >= 100 | 3 years |
| +4 | 0 Piety + Minor | Inscribe Minor Blood Rune (Self) | event option `bm_cast_blood_magic_minor.001` | `piety_level >= 2` | 5 years |
| +5 | 200 Piety + Major (`lifeforce_modifier_major`) | Inscribe Major Blood Rune (Self) | `bm_cast_blood_magic_major.001` | `piety_level >= 3`, Minor rune | 5 years |
| +10 | 400 Piety + Superior (`lifeforce_modifier_superior`) | Inscribe Superior Blood Rune (Self) | `bm_cast_blood_magic_superior.001` | `piety_level >= 4`, Major rune | 5 years |
| +2 (+5 if firstborn) | None | Childbirth Milestone | on-action `on_birth_child` -> `bm_on_birth_bloodline_xp` | Parent is blood mage | Per birth |

## `enlightenment`

| XP | Cost | Action | Source | Req | CD |
| --- | --- | --- | --- | --- | --- |
| +2 | 100 Piety + Minor; Grants Major | Purify Lifeforce (Minor to Major) | decision `bm_purify_lifeforce_decision` | Minor lifeforce, `piety_level >= 1` | 3 years |
| +3 | 250 Piety + Major; Grants Superior | Distill Lifeforce (Major to Superior) | decision `bm_distill_lifeforce_decision` | Major lifeforce, `piety_level >= 2` | 5 years |
| +2 | 100–300 Piety | Enhance Ward/Child Education (Lvl 1–5) | interaction `bm_enhance_education_interaction` | Ward/child age 6–15 | 3 years |
| +1 | 200 Piety | Study Arcane Secrets | decision | Learning lifestyle | 3 years |
| +1 | 75 Piety | Siphon Stored Lifeforce | interaction `bm_siphon_lifeforce_reserves_interaction` | Target has stored Lifeforce | 1 year |
| +5 (crit), +3 (win) | 150 Piety + Minor | Contest of the Red Art | interaction `bm_occult_mage_duel_interaction` | Target Blood Mage | 3 years |

## `benediction`

| XP | Cost | Action | Source | Req | CD |
| --- | --- | --- | --- | --- | --- |
| +1 | 15 Piety + Minor | Heal Affliction: Minor | interaction & event | Target with minor ailment | None |
| +2 | 35 Piety + Major | Heal Affliction: Major | interaction & event | Target with severe ailment | None |
| +3 | 60 Piety + Minor & Major | Heal Affliction: Deadly | interaction & event | Target with deadly disease | None |
| +1 | 50 Piety + Minor | Heal Old Age: Minor | interaction & event (`bm_heal_old_age.0001`) | Target with old age trait | None |
| +2 | 150 Piety + Major | Heal Old Age: Major | `bm_heal_old_age.0001` | Target with old age trait | None |
| +2 (Major) / +1 (Minor) | 0 Piety + Major/Minor | Empower Blood Mage (Caster) | `empower_blood_mage_interaction` | Target Blood Mage | None |
| +1 / +2 / +3 | 150 / 350 / 750 Piety + Minor/Major/Superior | Empower Bloodline (Covenants) | decision `bm_empower_bloodline_decision` | House head, Devotion 1/2/3 | 1 year |
| +4 (caster) | 0 Piety + Minor | Inscribe Minor Rune on Other | interaction `bm_inscribe_rune_other_interaction` | `piety_level >= 2` | 5 years |
| +5 (caster) | 200 Piety + Major | Upgrade Major Rune on Other | `bm_inscribe_rune_other_interaction` | `piety_level >= 3` | 5 years |
| +10 (caster) | 400 Piety + Superior | Upgrade Superior Rune on Other | `bm_inscribe_rune_other_interaction` | `piety_level >= 4` | 5 years |

## Blood Hunt (all tracks)

**+1 to +5 XP** (`bloodlust` / `enlightenment` / `hematurgy` / `benediction`). Decision & event (`seek_power_decision`, `seek_power.002`–`.011`). Grants Minor, Major, or 25% Superior Lifeforce (single combat duel vs escort knight / 20+ prowess traveler, apex beasts, or cairn). CD 1–3 years (1 year landed, 3 years wanderer).

## Implementation Files

| Subsystem | Files |
| --- | --- |
| XP helper macros | `common/scripted_effects/bm_trait_track_xp_gain_effects.txt` |
| Blood magic effects | `common/scripted_effects/bm_blood_magic_used_effects.txt` |
| Blood runes & Galdrastafir | `common/modifiers/bm_blood_runes_modifiers.txt`, `common/script_values/bm_blood_rune_cost.txt`, `common/scripted_effects/bm_blood_runes_effects.txt`, `common/character_interactions/bm_inscribe_rune_other.txt`, `common/decisions/cast_magic/bm_carve_galdrastafir_decision.txt` |
| Cure illness | `common/character_interactions/bm_cure_illness_interactions.txt`, `common/script_values/bm_cure_illness_values.txt` |
| Drain & grant | `common/character_interactions/bm_blood_drain.txt`, `common/character_interactions/bm_grant_blood_magic.txt` |
| Trait drain | `common/character_interactions/bm_drain_trait.txt`, `events/bm_trait_drain_events.txt`, `common/scripted_effects/bm_drain_trait_effects.txt` |
| Education | `common/script_values/bm_education_enhancement_piety_cost.txt` |
| Congenital manifestation | `common/scripted_effects/bm_manifest_traits_effects.txt` |
| Blood Power events | `events/bm_blood_power_event.txt` |
| Combat & duel hooks | `common/on_action/bm_combat_on_actions.txt`, `common/on_action/bm_duel_on_actions.txt` |
| Yearly pulse, attunement, birth | `events/bm_yearly_events.txt`, `common/decisions/cast_magic/bm_attune_lifeforce_decision.txt`, `common/on_action/bm_blood_mage_prevalence_on_actions.txt` |
