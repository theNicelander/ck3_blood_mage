# Blood Mage Track XP: Knight (`lifestyle_blood_knight`)

Knight-only tracks `vanguard` and `slaughter`, plus Knight-specific rows. Shared tracks `ancient`, `enlightenment`, `benediction` (rune, condense, education, Manifest Lifeforce/Intellect/Trait, Influence Personality, Contest Defeat, Channel Blood Power, heals, Bless Kin's Blood, Empower Bloodline/Dynasty, Dynasty Modifiers Pulse, Blood Hunt, Survival Pulse, Childbirth) and attunement pulses: [hub](blood-mage-track-xp.md). Knight heals (Self / Comrade / Knight) use the same costs as Mage.

## Empower & Initiate

| XP | Cost | Action | Source | Req | CD |
| --- | --- | --- | --- | --- | --- |
| +3 to `vanguard` & `slaughter` | 0 Piety (knight); caster consumes Major | Empower Blood Knight: Major | interaction `empower_blood_knight_interaction` | Fellow Blood Knight empowers knight | None |
| +1 to `vanguard` & `slaughter` | 0 Piety (knight); caster consumes Minor | Empower Blood Knight: Minor | `empower_blood_knight_interaction` | same | None |
| +2 / +1 `benediction` (caster) | 0 Piety + Major / Minor | Empower Blood Knight (Caster) | `empower_blood_knight_interaction` | Blood Knight empowers sworn knight | None |
| `vanguard` +1 / +2 (+2 if child/kin) | 100 Piety + Major | Make Blood Knight (Major) | interaction `make_blood_knight_interaction` | Blood Knight initiates kin, spouse, courtier, or knight | None |
| `vanguard` +1 | 250 Piety + Minor | Make Blood Knight (Minor) | `make_blood_knight_interaction` | same | None |
| `vanguard` +5 | 500 Piety + Superior | Forge Blood Golem | event option `bm_cast_blood_magic_superior.001` | `piety_level >= 3`, Superior lifeforce | 3 years |
| +3 to +8 `vanguard` / `enlightenment` (targeted: Vanguard for Physique, Enlightenment for Intellect/Beauty; scaled 3/4/5/6/7/8 based on trait rank) | 250–1500 Piety + Major/Superior | Manifest Trait (Congenital 1-5) | event option `bm_cast_blood_magic_major/superior.001` | `piety_level >= 2` | 5 years |

## Battle

| XP | Cost | Action | Source | Req | CD |
| --- | --- | --- | --- | --- | --- |
| `vanguard` +2 to +5 | None; scaled Lifeforce harvest (10%–100% Minor, 0%–100% Major) | Battle Victory (Commander) | on-action `bm_on_combat_end_winner` | Army commander; scales by battle size (<100 to 10k+) | Per battle |
| `vanguard` +1 to +5 | same | Battle Victory (Knight) | `bm_on_combat_end_winner` | Army knight; same scaling | Per battle |
| `vanguard` +1 to +3 and `enlightenment` +0 to +2 | None | Battle Defeat (Surviving Commander / Knight) | on-action `bm_on_combat_end_loser` | Surviving side commander or knight | Per battle |

## `slaughter`

| XP | Cost | Action | Source | Req | CD |
| --- | --- | --- | --- | --- | --- |
| +5 | None; Grants Major (25% chance Superior if victim prowess >= 20 or blood trait) | Single Combat Fatal Slaying | on-action `bm_on_character_death_duel` | Slaying opponent in single combat | None |
| +3 | None | Tournament Completion | on-action `bm_on_travel_activity_complete_tournament` | Completing `activity_tournament` | Per tourney |
| +3 | 75 Piety | Siphon Stored Lifeforce | interaction `bm_siphon_lifeforce_reserves_interaction` | Target possesses stored Lifeforce | 1 year |
| +5 (crit) / +3 (win) | 150 Piety + Minor | Contest of the Red Art | interaction `bm_occult_mage_duel_interaction` | Target is Blood Mage or Blood Knight | 3 years |
| +1 | 25 Piety; Grants Minor | Minor Lifedrain (Courtier / Prisoner) | interaction `lifedrain_courtier_event_interaction` | Siphoning victim via prowess | 3 months |
| +1 | 50 Piety; Grants Major | Major Lifedrain (Prisoner Execution) | interaction `lifedrain_prisoner_event_interaction` | Executing prisoner via blood drain | None |
| +2 | 100–325 Piety + Major | Trait Drain (Prisoner, up to rank 5) | interaction & event `trait_drain_prisoner_event_interaction` | Draining congenital trait from prisoner | 60 days |
