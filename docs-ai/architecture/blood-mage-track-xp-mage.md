# Blood Mage Track XP: Mage (`lifestyle_blood_mage`)

Mage tracks `fortune`, `cunning`, and `fury`. Shared tracks (`ancient`, `wisdom`, `radiance`), attunement pulses, rules: [hub](blood-mage-track-xp.md).

## `fortune`

| XP | Cost | Action | Source | Req | CD |
| --- | --- | --- | --- | --- | --- |
| +2 / +4 / +6 | 50 / 150 / 250 Piety + Minor/Major/Superior | Cast Blood Blessing (Fortune) | interaction `bm_cast_blood_blessing_interaction` | Devotion 1/3/5 | 1 year (target) |
| +4 | 50 Piety + Ancient LF | Grant Ancient Blood | interaction `bm_cast_blood_blessing_interaction` | Target non-self | None |
| +3 | 50 Piety; Grants Minor/Major | Demand Blood Tithe | interaction `bm_blood_drain_interaction` (`drain_tithe`) | Adult house kin | 2 years |
| +4 | 250 Piety + Major | Bestow Blood Traits | interaction `bm_bestow_traits_interaction` | Dynasty/spouse | 3 years |
| +4 | 250 Piety + Major | Adopt into Dynasty | interaction `bm_adopt_lowborn_interaction` | Lowborn courtier | 1 year |
| +3 / +4 (+4 if child/kin) | 100 Piety + Major | Grant Blood Magic (Major) | interaction `grant_blood_magic_interaction` | Target non-mage | None |
| +2 | 250 Piety + Minor | Grant Blood Magic (Minor) | `grant_blood_magic_interaction` | Target non-mage | None |
| +2 (+4 if child inherits; doubled to +4/+8 by Superior Feingur) | None; Grants +1 Major | Childbirth Milestone | on-action `on_birth_child` -> `bm_on_birth_fortune_xp` | Parent is blood mage | Per birth |
| +2 | 50 Piety + Minor | Purge Bodily Impurities (Congenital Flaw Cleansed) | event option `bm_cast_blood_magic_minor.001` | Has ugly/dull/weak | None |
| +3 to +8 (scaled 3/4/5/6/7/8 based on trait rank) | 250–1500 Piety + Major/Superior | Manifest Trait (Congenital 1-5) | event option `bm_cast_blood_magic_major/superior.001` | `piety_level >= 2` | 2 years |
| +3 / +5 / +8 | 150 / 350 / 750 Piety + Minor/Major/Superior (`lifeforce_modifier_superior`) | Empower Bloodline (Tier I/II/III Covenant) | decision `bm_empower_bloodline_decision` | `exists = house`, `piety_level >= 1` / `>= 2` / `>= 3` | 1 year |
| +8 | 500 Piety + Superior | Forge Blood Golem | event option `bm_cast_blood_magic_superior.001` | `piety_level >= 3`, Superior lifeforce | 3 years |
| +3 (Major) / +2 (Minor) | 0 Piety (recipient); caster consumes Lifeforce | Empower Blood Mage (Recipient) | interaction `bm_cast_blood_blessing_interaction` | Fellow Blood Mage empowers target | None |
| +1 (25% / 50% / 100% chance for Tier I/II/III Covenant of Fortune) | None | Yearly Covenant Pulse | on-action `blood_mage_yearly_events.002` | Has house, house covenant | 1 year |
| +1 (+2 with Superior Hulinhjálmur) | None (guaranteed) | Bloodline Attunement Pulse | `blood_mage_yearly_events.001` | Has `fortune_attuned` | 1 year |

## `cunning`

| XP | Cost | Action | Source | Req | CD |
| --- | --- | --- | --- | --- | --- |
| +2 / +4 / +6 | 50 / 150 / 250 Piety + Minor/Major/Superior | Cast Blood Blessing (Cunning) | interaction `bm_cast_blood_blessing_interaction` | Devotion 1/3/5 | 1 year (target) |
| +3 | 50 Piety; Grants Major (executes victim) | Major Life Drain | interaction `bm_blood_drain_interaction` (`drain_major`) | Imprisoned target | None |
| +1 | 20 Piety; Grants Minor | Minor Life Drain | interaction `bm_blood_drain_interaction` (`drain_minor`) | Target not recently drained | 3 months |
| +2 | 100 Piety; Grants Minor | Minor Life Drain (Empowered) | interaction `bm_blood_drain_interaction` (`drain_minor_empowered`) | Non-prisoner target | 3 months |
| +3 | 75 Piety | Siphon Stored Lifeforce | interaction `bm_blood_drain_interaction` (`drain_stored`) | Target possesses stored Lifeforce | 1 year |
| +4 (crit), +2 (win), +1 (fail) | 50 Piety + Minor (crit siphons Minor back) | Cast Blood Curse | interaction `bm_blood_drain_interaction` (`drain_curse`) | >= 10 Cunning XP | 1 year |
| +3 (leveled), +5 (rare) | 100–325 Piety + Major (executes victim) | Drain Positive Traits | interaction `bm_blood_drain_interaction` (`drain_trait`) + `bm_trait_drain.001` | Prisoner with congenital trait | 60 days |
| +1 (25% / 50% / 100% chance for Tier I/II/III Covenant of Cunning) | None | Yearly Covenant Pulse | on-action `blood_mage_yearly_events.002` | Has house, house covenant | 1 year |
| +1 (+2 with Superior Hulinhjálmur) | None (guaranteed) | Cunning Attunement Pulse | `blood_mage_yearly_events.001` | Has `cunning_attuned` | 1 year |

## `fury`

| XP | Cost | Action | Source | Req | CD |
| --- | --- | --- | --- | --- | --- |
| +2 / +4 / +6 | 50 / 150 / 250 Piety + Minor/Major/Superior | Cast Blood Blessing (Fury) | interaction `bm_cast_blood_blessing_interaction` | Devotion 1/3/5 | 1 year (target) |
| +4 (win) / +1 (loss) | 50 Piety; Win: Superior (`Prowess%`) or Major; Loss: Minor + wound + 20 Stress + escape | Blood Pit Duel | interaction `bm_blood_drain_interaction` (`drain_blood_duel`) + `bm_prisoner_blood_duel.0001` | 20+ prowess prisoner | None |
| +3 (crit), +2 (win) | 150 Piety + Minor | Contest of the Red Art | interaction `bm_occult_mage_duel_interaction` | Target Blood Mage | 3 years |
| +2 (Minor) / +4 (Major) | Health / Stress toll; Grants Minor/Major | Bleed Own Vein | interaction `bm_bleed_own_vein_interaction` | Self | 1 year |
| +2 to +4 | None | Battlefield Victory (Commander/Knight) | on-action `bm_combat_on_actions.txt` / `bm_combat_effects.txt` | Won battle | Per battle |
| +1 to +2 | None | Battlefield Defeat | on-action `bm_combat_on_actions.txt` / `bm_combat_effects.txt` | Survived lost battle | Per battle |
| +3 | None | Single Combat Fatality (Duel Kill) | on-action `bm_duel_on_actions.txt` / `bm_combat_on_character_death_effect` | Slew opponent in single combat | Per fatal duel |
| +2 | None | Tournament Completion | on-action `bm_duel_on_actions.txt` | Completed contest | Per contest |
| +2 (win) / +1 (loss) | None | Ritual Sparring | decision & event `bm_ritual_spar_decision.txt` | Sworn knight opponent | 1 year |
| +3 (Major) / +2 (Minor) | 0 Piety (recipient); caster consumes Lifeforce | Empower Blood Mage (Recipient) | interaction `bm_cast_blood_blessing_interaction` | Fellow Blood Mage empowers target | None |
| +1 (25% / 50% / 100% chance for Tier I/II/III Covenant of Fury) | None | Yearly Covenant Pulse | on-action `blood_mage_yearly_events.002` | Has house, house covenant | 1 year |
| +1 (+2 with Superior Hulinhjálmur) | None (guaranteed) | Fury Attunement Pulse | `blood_mage_yearly_events.001` | Has `fury_attuned` | 1 year |
