# Blood Mage Track XP: Mage (`lifestyle_blood_mage`)

Mage-only tracks `bloodline` and `hematurgy`. Shared tracks (`ancient`, `enlightenment`, `benediction`), attunement pulses, rules: [hub](blood-mage-track-xp.md).

## `bloodline`

| XP | Cost | Action | Source | Req | CD |
| --- | --- | --- | --- | --- | --- |
| +1 / +2 (+2 if child/kin) | 100 Piety + Major | Grant Blood Magic (Major) | interaction `grant_blood_magic_interaction` | Target non-mage, non-knight | None |
| +1 | 250 Piety + Minor | Grant Blood Magic (Minor) | `grant_blood_magic_interaction` | Target non-mage, non-knight | None |
| +2 (+4 if child inherits; doubled to +4/+8 by Superior Feingur) | None; Grants +1 Major | Childbirth Milestone | on-action `on_birth_child` -> `bm_on_birth_bloodline_xp` | Parent is blood mage | Per birth |
| +1 | 35 Piety + Minor (`lifeforce_modifier_minor`) | Bless Kin's Blood | interaction `bm_bless_bloodline_interaction` | Target child/dynasty kin | 10 years (target buff) |
| +1 | 50 Piety + Minor | Bless Dynasty Bloodline (Feingur) | interaction `bm_feingur_bless_dynasty_interaction` | Superior Feingur stave; child or dynasty kin | Permanent |
| +1 | 50 Piety + Minor | Purge Bodily Impurities (Congenital Flaw Cleansed) | event option `bm_cast_blood_magic_minor.001` | Has ugly/dull/weak | None |
| +1 / +2 (on duel win) | 200–600 Piety + Major (`lifeforce_modifier_major`) | Manifest Trait (Congenital 1-5) | event option `bm_cast_blood_magic_major/superior.001` | `piety_level >= 2` | 5 years |
| +1 / +2 / +3 | 150 / 350 / 750 Piety + Minor/Major/Superior (`lifeforce_modifier_superior`) | Empower Bloodline (Tier I/II/III Covenant) | decision `bm_empower_bloodline_decision` | `exists = house`, `piety_level >= 1` / `>= 2` / `>= 3` | 1 year |
| +5 | 500 Piety + Superior | Forge Blood Golem | event option `bm_cast_blood_magic_superior.001` | `piety_level >= 3`, Superior lifeforce | 3 years |
| +3 (Major) / +1 (Minor) | 0 Piety (recipient); caster consumes Lifeforce | Empower Blood Mage (Recipient) | interaction `empower_blood_mage_interaction` | Fellow Blood Mage empowers target | None |
| +1 (+3% / +6% / +10% chance per Tier I/II/III Covenant, up to 70%) | None | Yearly Dynasty Modifiers Pulse | on-action `blood_mage_yearly_events.002` | Has house, house covenants | 1 year |
| +1 (+2 with Superior Hulinhjálmur) | None (guaranteed) | Bloodline Attunement Pulse | `blood_mage_yearly_events.001` | Has `bloodline_attuned` | 1 year |

## `hematurgy`

| XP | Cost | Action | Source | Req | CD |
| --- | --- | --- | --- | --- | --- |
| +2 | 50 Piety (`lifedrain_piety_cost_major`); Grants Major (executes victim) | Lifedrain Prisoner | interaction `lifedrain_prisoner_event_interaction` | Imprisoned target | None |
| +1 | 25 Piety (`lifedrain_piety_cost_minor`); Grants Minor | Lifedrain Courtier | interaction `lifedrain_courtier_event_interaction` | Courtier/prisoner not recently drained | 3 months |
| +3 | 75 Piety | Siphon Stored Lifeforce | interaction `bm_siphon_lifeforce_reserves_interaction` | Target possesses stored Lifeforce | 1 year |
| +5 (crit), +3 (win) | 150 Piety + Minor | Contest of the Red Art | interaction `bm_occult_mage_duel_interaction` | Target is Blood Mage or Blood Knight | 3 years |
| +2 (win), +4 (crit), +1 (fail) | 50 Piety + Minor (crit siphons Minor back) | Cast Blood Curse | interaction `bm_curse_blood_interaction` | >= 10 Hematurgy XP | 1 year |
| +2 (on duel win) | 100–325 Piety + Major (executes victim) | Drain Prisoner Trait (Lvl 1–5) | interaction + event `bm_trait_drain.001` | Prisoner with congenital trait | 60 days |
| +1 (+2 with Superior Hulinhjálmur) | None (guaranteed) | Hematurgy Attunement Pulse | `blood_mage_yearly_events.001` | Has `hematurgy_attuned` | 1 year |
