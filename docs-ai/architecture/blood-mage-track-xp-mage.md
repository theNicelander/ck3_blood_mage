# Blood Mage Track XP: Mage (`lifestyle_blood_mage`)

Mage tracks `bloodline`, `hematurgy`, and `bloodlust`. Shared tracks (`ancient`, `enlightenment`, `benediction`), attunement pulses, rules: [hub](blood-mage-track-xp.md).

## `bloodline`

| XP | Cost | Action | Source | Req | CD |
| --- | --- | --- | --- | --- | --- |
| +3 / +4 (+4 if child/kin) | 100 Piety + Major | Grant Blood Magic (Major) | interaction `grant_blood_magic_interaction` | Target non-mage | None |
| +2 | 250 Piety + Minor | Grant Blood Magic (Minor) | `grant_blood_magic_interaction` | Target non-mage | None |
| +2 (+4 if child inherits; doubled to +4/+8 by Superior Feingur) | None; Grants +1 Major | Childbirth Milestone | on-action `on_birth_child` -> `bm_on_birth_bloodline_xp` | Parent is blood mage | Per birth |
| +2 | 35 Piety + Minor (`lifeforce_modifier_minor`) | Bless Kin's Blood | interaction `bm_bless_bloodline_interaction` | Target child/dynasty kin | 10 years (target buff) |
| +2 | 50 Piety + Minor | Bless Dynasty Bloodline (Feingur) | interaction `bm_feingur_bless_dynasty_interaction` | Superior Feingur stave; child or dynasty kin | Permanent |
| +2 | 50 Piety + Minor | Purge Bodily Impurities (Congenital Flaw Cleansed) | event option `bm_cast_blood_magic_minor.001` | Has ugly/dull/weak | None |
| +3 to +8 (scaled 3/4/5/6/7/8 based on trait rank) | 250–1500 Piety + Major/Superior | Manifest Trait (Congenital 1-5) | event option `bm_cast_blood_magic_major/superior.001` | `piety_level >= 2` | 2 years |
| +3 / +5 / +8 | 150 / 350 / 750 Piety + Minor/Major/Superior (`lifeforce_modifier_superior`) | Empower Bloodline (Tier I/II/III Covenant) | decision `bm_empower_bloodline_decision` | `exists = house`, `piety_level >= 1` / `>= 2` / `>= 3` | 1 year |
| +8 | 500 Piety + Superior | Forge Blood Golem | event option `bm_cast_blood_magic_superior.001` | `piety_level >= 3`, Superior lifeforce | 3 years |
| +3 (Major) / +2 (Minor) | 0 Piety (recipient); caster consumes Lifeforce | Empower Blood Mage (Recipient) | interaction `empower_blood_mage_interaction` | Fellow Blood Mage empowers target | None |
| +1 (25% / 50% / 100% chance for Tier I/II/III Covenant of Bloodline) | None | Yearly Covenant Pulse | on-action `blood_mage_yearly_events.002` | Has house, house covenant | 1 year |
| +1 (+2 with Superior Hulinhjálmur) | None (guaranteed) | Bloodline Attunement Pulse | `blood_mage_yearly_events.001` | Has `bloodline_attuned` | 1 year |

## `hematurgy`

| XP | Cost | Action | Source | Req | CD |
| --- | --- | --- | --- | --- | --- |
| +3 | 50 Piety (`lifedrain_piety_cost_major`); Grants Major (executes victim) | Lifedrain Prisoner | interaction `lifedrain_prisoner_event_interaction` | Imprisoned target | None |
| +2 | 25 Piety (`lifedrain_piety_cost_minor`); Grants Minor | Lifedrain Courtier | interaction `lifedrain_courtier_event_interaction` | Courtier/prisoner not recently drained | 3 months |
| +3 | 75 Piety | Siphon Stored Lifeforce | interaction `bm_siphon_lifeforce_reserves_interaction` | Target possesses stored Lifeforce | 1 year |
| +5 (crit), +3 (win) | 150 Piety + Minor | Contest of the Red Art | interaction `bm_occult_mage_duel_interaction` | Target is Blood Mage | 3 years |
| +2 (win), +4 (crit), +1 (fail) | 50 Piety + Minor (crit siphons Minor back) | Cast Blood Curse | interaction `bm_curse_blood_interaction` | >= 10 Hematurgy XP | 1 year |
| +3 (on duel win, +5 for rare) | 100–325 Piety + Major (executes victim) | Drain Prisoner Trait (Lvl 1–5 / Rare) | interaction + event `bm_trait_drain.001` | Prisoner with congenital trait | 60 days |
| +1 (25% / 50% / 100% chance for Tier I/II/III Covenant of Hematurgy) | None | Yearly Covenant Pulse | on-action `blood_mage_yearly_events.002` | Has house, house covenant | 1 year |
| +1 (+2 with Superior Hulinhjálmur) | None (guaranteed) | Hematurgy Attunement Pulse | `blood_mage_yearly_events.001` | Has `hematurgy_attuned` | 1 year |

## `bloodlust`

| XP | Cost | Action | Source | Req | CD |
| --- | --- | --- | --- | --- | --- |
| +2 to +4 | None | Battlefield Victory (Commander) | on-action `bm_combat_on_actions.txt` / `bm_combat_effects.txt` | Won battle as commander | Per battle |
| +2 to +4 | None | Battlefield Victory | on-action `bm_combat_on_actions.txt` / `bm_combat_effects.txt` | Won battle as commander or knight | Per battle |
| +1 | None | Battlefield Defeat | on-action `bm_combat_on_actions.txt` / `bm_combat_effects.txt` | Survived lost battle | Per battle |
| +3 | None | Single Combat Fatality (Duel Kill) | on-action `bm_duel_on_actions.txt` / `bm_combat_on_character_death_effect` | Slew opponent in single combat | Per fatal duel |
| +2 | None | Tournament Completion | on-action `bm_duel_on_actions.txt` | Completed contest | Per contest |
| +2 (win) / +1 (loss) | None | Ritual Sparring | decision & event `bm_ritual_spar_decision.txt` | Sworn knight opponent | 1 year |
| +2 (win) | None | Siphoning Duel | interaction `bm_siphoning_duel_interaction` | Target Blood Mage | 1 year |
| +5 | 0 Piety (recipient); caster consumes Lifeforce | Empower Blood Mage (Recipient) | interaction `empower_blood_mage_interaction` | Fellow Blood Mage empowers target | None |
| +1 (25% / 50% / 100% chance for Tier I/II/III Covenant of Bloodlust) | None | Yearly Covenant Pulse | on-action `blood_mage_yearly_events.002` | Has house, house covenant | 1 year |
| +1 (+2 with Superior Hulinhjálmur) | None (guaranteed) | Bloodlust Attunement Pulse | `blood_mage_yearly_events.001` | Has `bloodlust_attuned` | 1 year |
