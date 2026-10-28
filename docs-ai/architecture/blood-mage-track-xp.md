# Blood Mage Track XP & Costs (Hub)

XP sources, Piety costs, Lifeforce sinks/sources, cooldowns for all lifestyle track progression. Per-trait detail: [mage](blood-mage-track-xp-mage.md) (`bloodline`, `hematurgy`), [knight](blood-mage-track-xp-knight.md) (`vanguard`, `slaughter`), [power](blood-mage-track-xp-power.md) (`lifestyle_blood_power`). This file: shared rules and the tracks shared by Mage and Knight (`ancient`, `enlightenment`, `benediction`).

## Shared Rules

- **Engine cap**: 100 XP max per track (10 tiers at 10 XP steps). Overflow discarded.
- **Traits/tracks**: `lifestyle_blood_mage` (`ancient`, `enlightenment`, `bloodline`, `benediction`, `hematurgy`); `lifestyle_blood_knight` (`vanguard`, `slaughter` + shared `ancient`, `benediction`, `enlightenment`); `lifestyle_blood_power` (`dynasty`, `fury`, `mastery`, `presence`, `prosperity`, `shadows`).
- **Vitality baseline**: Tiers 10–40 and 60–90 on `lifestyle_blood_mage` and `lifestyle_blood_knight` give `+0.1` Health, `+2.5` Life Expectancy, `+1.25` Year Fertility, `+1` Epidemic Resistance. Tiers 50 and 100 skip it (milestone/capstone). `lifestyle_blood_power` has no vitality baseline.
- **Apex Devotion (Levels 6–8)**: 100 XP capstones of `ancient`, `enlightenment`, `benediction` each grant `character_max_piety_level_add = 1` (Mage and Knight).
- **Age lock**: every track capstone at 100 XP grants `no_prowess_loss_from_age = yes`.
- **Cost types**: Piety, Lifeforce (`lifeforce_modifier_minor` / `lifeforce_modifier_major` / `lifeforce_modifier_superior`), Piety Levels (`piety_level`), cooldowns. "Grants" = action yields Lifeforce.
- Knight reuses Mage costs unless its file says otherwise. Tables below: Who = M (Mage), K (Knight), MK (both).

## Track Overview

| Trait | Track | XP per action | Cost range |
| --- | --- | --- | --- |
| Mage, Knight | `ancient` | +1 to +10 | 0 (pulse) / 25–400 Piety + Minor/Major/Superior |
| Mage, Knight | `enlightenment` | +1 to +5 | 75 – 1000 Piety + Minor/Major/Superior |
| Mage | `bloodline` | +1 to +3 | 0 – 500 Piety + Minor/Major/Superior |
| Mage, Knight | `benediction` | +1 to +4 | 15 – 100 Piety + Minor/Major |
| Mage | `hematurgy` | +1 | 25 – 250 Piety (grants Minor/Major) |
| Power | chosen track | +10 | 150 Piety + Major |
| Knight | `vanguard` | +1 to +5 | 0 – 500 Piety + Minor/Major/Superior |
| Knight | `slaughter` | +1 to +5 | None / 25 Piety |

## Attunement Pulses (all tracks)

Guaranteed, no cost, 1 year cooldown: **+1 XP** (**+2 XP** with Superior **Hulinhjálmur**) when holder has `<track>_attuned` (e.g. `ancient_attuned`, `enlightenment_attuned`, `benediction_attuned`, `bloodline_attuned`, `hematurgy_attuned`).

| Track | Event |
| --- | --- |
| `ancient`, `enlightenment` | `blood_mage_yearly_events.001` / `.004` |
| `benediction`, `bloodline`, `hematurgy` | `blood_mage_yearly_events.001` |
| Knight discipline: `vanguard` / `slaughter` / `ancient` / `benediction` / `enlightenment` (needs matching `<track>_attuned`) | `blood_mage_yearly_events.004` |

## `ancient`

| Who | XP | Cost | Action | Source | Req | CD |
| --- | --- | --- | --- | --- | --- | --- |
| MK | +1 | None | Yearly Pulse | on-action `blood_mage_yearly_events.001` / `.004` | `lifestyle_blood_mage` or `lifestyle_blood_knight` | 1 year |
| K | +1 | None (33% ambient roll Minor Lifeforce) | Yearly Survival Pulse | `blood_mage_yearly_events.004` | `lifestyle_blood_knight` | 1 year |
| MK | grants `ancient_attuned` | Initial free; change: 100 Piety + Minor (`lifeforce_modifier_minor`) | Attune Lifeforce | decision `bm_attune_lifeforce_decision` | Change: Minor lifeforce, piety >= 100 | 3 years |
| MK | +4 | 0 Piety + Minor | Inscribe Minor Blood Rune (Self) | M: event option `bm_cast_blood_magic_minor.001`; K: decision widget `bm_cast_blood_magic_minor_decision` | `piety_level >= 2` | 5 years |
| MK | +5 | 200 Piety + Major (`lifeforce_modifier_major`) | Inscribe Major Blood Rune (Self) | M: `bm_cast_blood_magic_major.001`; K: `bm_cast_blood_magic_major_decision` | `piety_level >= 3`, Minor rune | 5 years |
| MK | +10 | 400 Piety + Superior (`lifeforce_modifier_superior`) | Inscribe Superior Blood Rune (Self) | M: `bm_cast_blood_magic_superior.001`; K: `bm_cast_blood_magic_superior_decision` | `piety_level >= 4`, Major rune | 5 years |
| MK | +2 (+5 if firstborn) | None | Childbirth Milestone | on-action `on_birth_child` -> `bm_on_birth_bloodline_xp` | Parent is blood mage or blood knight | Per birth |

## `enlightenment`

| Who | XP | Cost | Action | Source | Req | CD |
| --- | --- | --- | --- | --- | --- | --- |
| MK | +2 | 100 Piety + Minor; Grants Major | Condense Lifeforce | event option `bm_cast_blood_magic_minor.001` / decision `bm_cast_blood_magic_minor_decision` | Minor lifeforce | None |
| MK | +3 (crit/success), +1 (fail) | 250 Piety + Minor & Major; Grants Superior | Condense Superior Lifeforce | event option `bm_cast_blood_magic_major.001` / decision `bm_cast_blood_magic_major_decision` | `piety_level >= 3`, Minor + Major | 2 years |
| MK | +1 / +1 / +2 / +2 | 100 / 250 / 500 / 1000 Piety (Learning duel for Minor, Major, Superior Lifeforce) | Manifest Lifeforce | decision `bm_manifest_lifeforce_decision` | `piety_level >= 2`, `piety >= 100` | 1 year |
| M | +1 | 75 Piety + Minor | Channel Minor Lifeforce | `bm_cast_blood_magic_minor.001` | Minor lifeforce | None |
| M | +1 | 25 Piety + Minor | Grant Lifeforce (Minor) | interaction `grant_lifeforce_interaction` | Minor lifeforce, courtier/prisoner | None |
| M | +2 | 50 Piety + Major | Grant Lifeforce (Major) | `grant_lifeforce_interaction` | Major lifeforce, courtier/prisoner | None |
| MK | +1 (+10 Power XP) | 150 Piety + Major | Channel Blood Power | M: `bm_cast_blood_magic_major.001`; K: decision -> event `bm_cast_blood_magic_major.001` | `piety_level >= 1`, Major lifeforce held | None |
| MK | +2 | 75–200 Piety + Major | Improve Education (2★/3★/4★; K: tiers 1★ to 4★) | M: `bm_cast_blood_magic_major.001`; K: `bm_cast_blood_magic_major_decision` | M: `piety_level >= 3`; K: holds education trait below rank 4 | 2 years |
| MK | +3 (+2 on duel win) | 350 Piety + Superior | Master Education (5★) | M: `bm_cast_blood_magic_superior.001`; K: `bm_cast_blood_magic_superior_decision` | `piety_level >= 3`, 4★ education | 2 years |
| MK | +3 | 1000 Piety + Superior | New Education (2nd Trait) | M: `bm_cast_blood_magic_superior.001`; K: `bm_cast_blood_magic_superior_decision` | `piety_level >= 4`, 5★ education | 2 years |
| MK | +4 (success) / +1 (failure) | 250 Piety + Major | Influence Personality | interaction `bm_reshape_personality_interaction` | `piety_level >= 3`, relationship target | 5 years (success) / 1 year (failure) |
| K | +3 to +8 | 250–1500 Piety + Major/Superior | Manifest Intellect / Manifest Trait (Congenital 1-5; targeted XP; scaled 3/4/5/6/7/8 based on trait rank) | event option `bm_cast_blood_magic_major/superior.001`; decision `bm_cast_blood_magic_major/superior_decision` | `piety_level >= 2` | 5 years |
| M | +3 (Major) / +1 (Minor) | 0 Piety (recipient); caster consumes Lifeforce | Empower Blood Mage (Recipient; also `bloodline`) | interaction `empower_blood_mage_interaction` | Fellow Blood Mage empowers target | None |
| MK | +1 | 150 Piety + Minor | Contest of the Red Art (Defeat) | interaction `bm_occult_mage_duel_interaction` | Blood Mage or Blood Knight | 3 years |
| K | +1 to +3 `vanguard` + 0 to +2 `enlightenment` | None | Battle Defeat | see knight doc | | |

## `benediction`

Heal Old Age rows: reduce old-age trait XP, or remove it if at or below threshold (Knight: "cure").

| Who | XP | Cost | Action | Source | Req | CD |
| --- | --- | --- | --- | --- | --- | --- |
| MK | +1 | 15 Piety (`cure_illness_cost_minor_neg`) + Minor | Heal Affliction: Minor (`bm_heal_ailment`) | interaction & event | Target with `wounded_1`, `ill`, `lovers_pox`, `gout_ridden`, `scarred` | None |
| MK | +2 | 35 Piety (`cure_illness_cost_major_neg`) + Major | Heal Affliction: Major (`bm_heal_ailment`) | interaction & event | Target with `wounded_2`, `incapable`, `pneumonic`, `maimed`, etc. | None |
| MK | +2 | 100 Piety (`cure_illness_cost_benediction_neg`) + both Minor & Major | Heal Affliction: Deadly (`bm_heal_ailment`) | interaction & event | Target with `wounded_3`, `cancer`, `plague`, `leper`, `disfigured`, etc. | None |
| MK | +1 | 50 Piety (`heal_old_age_cost_minor_neg`) + Minor | Heal Old Age: Minor (`bm_heal_old_age_trait`) | interaction & event (`bm_heal_old_age.0001`) | Old age trait, -20 XP or remove if <= 20 XP | None |
| MK | +2 | 150 Piety (`heal_old_age_cost_major_neg`) + Major | Heal Old Age: Major (`bm_heal_old_age_trait`) | `bm_heal_old_age.0001` | Old age trait, -50 XP or remove if <= 50 XP | None |
| M | +2 (caster) | 0 Piety + Major | Empower Blood Knight (Major) | interaction `empower_blood_knight_interaction` | Blood Knight caster; target is blood knight | None |
| M | +1 (caster) | 0 Piety + Minor | Empower Blood Knight (Minor) | `empower_blood_knight_interaction` | same | None |
| K | +2 / +1 (caster) | 0 Piety + Major / Minor | Empower Blood Knight (Caster) | `empower_blood_knight_interaction` | Blood Knight empowers sworn knight | None |
| M | +2 (Major) / +1 (Minor) (caster) | 0 Piety + Major/Minor | Empower Blood Mage (Caster) | `empower_blood_mage_interaction` | Blood Mage empowers fellow Blood Mage | None |
| M | +2 | 25 Piety + Major | Restore Lifedrained Courtier | interaction `grant_lifeforce_interaction_reversed` | Target has `lifedrained_modifier` | None |
| MK | +1 | 150 Piety + Major | Empower Dynasty | event option `bm_blood_power_event.001` | Cast Major Blood Magic Grimoire | None |
| K | +1 | 35 Piety + Minor | Bless Kin's Blood | interaction `bm_bless_bloodline_interaction` | Target child/dynasty kin | 10 years (target buff) |
| MK | +1 / +2 / +3 | 150 / 350 / 750 Piety + Minor/Major/Superior | Empower Bloodline (Tier I/II/III Covenant) | decision `bm_empower_bloodline_decision` | M: Blood Knight; `exists = house`; Devotion Rank 1/2/3 | 1 year |
| K | +1 | None (+3% / +6% / +10% chance per Tier I/II/III Covenant, up to 70%) | Yearly Dynasty Modifiers Pulse | on-action `blood_mage_yearly_events.002` | Blood Knight, has house covenants | 1 year |
| MK | +4 (caster) | 0 Piety + Minor | Inscribe Minor Rune on Other | interaction `bm_inscribe_rune_other_interaction` | `piety_level >= 2`, 25 Track XP | 5 years |
| MK | +5 (caster) | 200 Piety + Major | Upgrade Major Rune on Other | `bm_inscribe_rune_other_interaction` | `piety_level >= 3`, 50 Track XP, Minor rune | 5 years |
| M | +10 (caster) | 400 Piety + Superior | Upgrade Superior Rune on Other | `bm_inscribe_rune_other_interaction` | Blood Mage, `piety_level >= 4`, 100 Track XP, Major rune | 5 years |

## Blood Hunt (all tracks)

**+1 to +5 XP** (`slaughter` / `vanguard` / `enlightenment` / `hematurgy` / `benediction`). Decision & event (`seek_power_decision`, `seek_power.002`–`.011`). Grants Minor, Major, or 25% Superior Lifeforce (single combat duel vs escort knight / 20+ prowess traveler, apex beasts, or cairn). Mage or Knight. CD 1–3 years (1 year landed, 3 years wanderer).

## Implementation Files

| Subsystem | Files |
| --- | --- |
| XP helper macros | `common/scripted_effects/bm_trait_track_xp_gain_effects.txt` |
| Blood magic effects | `common/scripted_effects/bm_blood_magic_used_effects.txt` |
| Blood runes & Galdrastafir | `common/modifiers/bm_blood_runes_modifiers.txt`, `common/script_values/bm_blood_rune_cost.txt`, `common/scripted_effects/bm_blood_runes_effects.txt`, `common/character_interactions/bm_inscribe_rune_other.txt`, `common/decisions/cast_magic/bm_carve_galdrastafir_decision.txt` |
| Cure illness | `common/character_interactions/bm_cure_illness_interactions.txt`, `common/script_values/bm_cure_illness_values.txt` |
| Drain & grant | `common/character_interactions/bm_drain_lifeforce.txt`, `common/character_interactions/bm_grant_lifeforce.txt`, `common/character_interactions/bm_grant_blood_magic.txt`, `common/character_interactions/bm_bless_bloodline.txt` |
| Trait drain | `common/character_interactions/bm_drain_trait.txt`, `events/bm_trait_drain_events.txt`, `common/scripted_effects/bm_drain_trait_effects.txt` |
| Education | `common/script_values/bm_education_enhancement_piety_cost.txt`, `common/scripted_effects/bm_education_duel_effect.txt` |
| Congenital manifestation | `common/scripted_effects/bm_manifest_traits_effects.txt`, `events/bm_channel_manifest_traits_events.txt` |
| Blood Power events | `events/bm_blood_power_event.txt` |
| Knight hooks | `common/character_interactions/bm_blood_knight_interactions.txt`, `common/on_action/bm_combat_on_actions.txt`, `common/on_action/bm_duel_on_actions.txt` |
| Yearly pulse, attunement, birth | `events/bm_yearly_events.txt`, `common/decisions/cast_magic/bm_attune_lifeforce_decision.txt`, `common/on_action/bm_blood_mage_prevalence_on_actions.txt` |
