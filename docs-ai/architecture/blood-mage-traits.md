# Blood Mage Lifestyle Traits

Living technical specification for `lifestyle_blood_mage`, `lifestyle_blood_knight`, and secondary `lifestyle_blood_power`.

## Archetypes & Class Comparison

| Lifestyle Trait | Archetype | Exclusive Tracks (2) | Shared Devotion Tracks (3) | Magic & Subsystem Access |
| --- | --- | --- | --- | --- |
| **Blood Mage** (`lifestyle_blood_mage`) | *Shepherd of the Faithful* — Occult scholar, dynasty architect, scheme master | `bloodline`, `hematurgy` | `ancient`, `enlightenment`, `benediction` | Minor, Major, Superior Blood Magic; builds Duchy Blood Temples (`bm_duchy_buildings.txt`); inscribes Superior Blood Runes on others. |
| **Blood Knight** (`lifestyle_blood_knight`) | *Fire and Sword* — Martial warlord, battlefield harvester, champion | `vanguard`, `slaughter` | `ancient`, `enlightenment`, `benediction` | Minor, Major, Superior Blood Magic; harvests Lifeforce from battles, single combat, yearly pulse; recruits Blood Berserkers & Behemoths; empowers sworn knights. |
| **Blood Power** (`lifestyle_blood_power`) | *Secondary Personal Mastery* — Granted alongside Mage or Knight (base 0 XP) | 6 tracks: `dynasty`, `fury`, `mastery`, `presence`, `prosperity`, `shadows` | — | Advanced via Major Magic (`bm_cast_blood_magic_major.001.power`). +5 monthly Lifestyle XP per 10 XP step, 50 XP milestones, 100 XP capstones including `no_prowess_loss_from_age = yes`. |

- **Inheritance & Base:** Inheritable non-genetic (`25%` single parent, `50%` with Superior Feingur, `100%` both parents, `0.20%` birth), audited by `bm_blood_mage_prevalence` / `bm_blood_knight_prevalence` rules. Base: `same_opinion = 10`. Dual-wielding blocked (only Egill Skallagrímsson holds both).
- **Track Structure:** 10 tiers (10–100 XP). Tiers 10–40 and 60–90 grant standard Vitality step (`+0.1` Health, `+2.5` Life Exp, `+1.25` Fertility Yr, `+1` Epidemic Res; 4× at 50 XP, 8× at 100 XP). Tier 50 = Devotion-scaling milestones (`<stat>_per_piety_level = 1`); Tier 100 = Devotion Apex (`+50%` Devotion Impact on `ancient`, `+2` stat on `enlightenment`/`benediction`) and universal age lock (`no_prowess_loss_from_age = yes`).

---

## Devotion Lifestyle Tracks

Complete XP sources live in [`blood-mage-track-xp.md`](blood-mage-track-xp.md), [`blood-mage-track-xp-mage.md`](blood-mage-track-xp-mage.md), and [`blood-mage-track-xp-knight.md`](blood-mage-track-xp-knight.md).

| Track | Class | 10 XP (1st Step) | 50 XP (Cumulative Milestone) | 100 XP (Cumulative Capstone) |
| --- | --- | --- | --- | --- |
| `ancient` | Shared | Vitality + `+0.10` Monthly Dynasty Prestige, `+4%` Lifestyle XP Mult (+1 Tenet Slot at 20, 40, 60, 80, 100) | 4× Vitality + `+0.4` Dynasty Prestige, `+16%` Lifestyle XP, `+17.5%` Devotion Impact, `+2` Tenet Slots | 8× Vitality + `+0.8` Dynasty Prestige, `+32%` Lifestyle XP, `+17.5%` Devotion Impact, `character_max_piety_level_add = 1`, `no_prowess_loss_from_age = yes`, `+5` Tenet Slots |
| `enlightenment` | Shared | Vitality + `+0.175` Monthly Piety, `+4%` Monthly Piety Mult | 4× Vitality + `+0.7` Monthly Piety, `+16%` Piety Mult, `+1` Learning per Piety level | 8× Vitality + `+1.4` Monthly Piety, `+32%` Piety Mult, `+1.5` Learning per Piety level, `character_max_piety_level_add = 1`, `no_prowess_loss_from_age = yes` |
| `benediction` | Shared | Vitality + `+1.5` General Opinion, `+1` Vassal Opinion, `+0.175` Monthly Prestige, `+4%` Prestige Mult | 4× Vitality + `+6` General Opinion, `+4` Vassal Opinion, `+0.7` Monthly Prestige, `+16%` Prestige Mult, `+1` Diplomacy per Piety level | 8× Vitality + `+12` General Opinion, `+8` Vassal Opinion, `+1.4` Monthly Prestige, `+32%` Prestige Mult, `+1.5` Diplomacy per Piety level, `character_max_piety_level_add = 1`, `no_prowess_loss_from_age = yes` |
| `bloodline` | Mage | Vitality + `+3%` Domain Tax | 4× Vitality + `+12%` Domain Tax, `+20%` Inactive Inheritance (20, 40), `+1` Stewardship per Piety level, `+25%` Dynasty Prestige Mult | 8× Vitality + `+24%` Domain Tax, `+40%` Inactive Inheritance (20, 40, 60, 80), `+2` Stewardship per Piety level, `+50%` Dynasty Prestige Mult, `no_prowess_loss_from_age = yes` |
| `hematurgy` | Mage | Vitality + `+4` Hostile Scheme Success | 4× Vitality + `+16` Hostile Scheme Success, `-16` Enemy Hostile Success, `-10%` Dread Decay, `+1` Intrigue per Piety level | 8× Vitality + `+32` Hostile Scheme Success, `-32` Enemy Hostile Success, `-20%` Dread Decay, `+2` Intrigue per Piety level, `no_prowess_loss_from_age = yes` |
| `vanguard` | Knight | Vitality + `+1.75%` Army Speed (+1 Martial and +1 Advantage at 20, 40, 60, 80; +1 Adv at 30, 70, 90) | 4× Vitality + `+3` Advantage, `+7%` Army Speed, `+2` Martial, `+1` Martial per Piety Level, `+1` Prowess per Piety Level | 8× Vitality + `+7` Advantage, `+14%` Army Speed, `+4` Martial, `+1.5` Martial per Piety Level, `+1` Prowess per Piety Level, `no_prowess_loss_from_age = yes` |
| `slaughter` | Knight | Vitality + `+1.5` Prowess, `+8.75%` Knight Effectiveness (+1 Knight Limit at 20–40, 60–90) | 4× Vitality + `+7` Prowess, `+3` Knight Limit, `+35%` Knight Effectiveness, `+1` Prowess per Piety Level | 8× Vitality + `+14` Prowess, `+7` Knight Limit, `+70%` Knight Effectiveness, `+2` Prowess per Piety Level, `no_prowess_loss_from_age = yes` |

---

## Secondary Blood Power Tracks (`lifestyle_blood_power`)

Base: none. Granted automatically with Mage or Knight at base 0 XP. Every 10 XP grants **+5 flat monthly Lifestyle XP** (+15 quarterly).

| Track | 10 XP (1st Step) | 50 XP (Cumulative Milestone) | 100 XP (Cumulative Capstone) | Flat Lifestyle XP |
| --- | --- | --- | --- | --- |
| `dynasty` | `+5%` Pos. Inactive Inheritance, `+5%` Trait Strengthen | `+20%` Inactive Inheritance, `+20%` Trait Strengthen, `+10` Yrs Fertility, **`-50%` Inbreeding Chance**, **`+10%` Renown** | **`+40%` Inactive Inheritance**, **`+40%` Trait Strengthen**, **`+20` Yrs Fertility**, **`-100%` Inbreeding Chance (Immunity)**, **`+25%` Renown**, `no_prowess_loss_from_age = yes` | `+5` to `+50`/mo Active Focus |
| `fury` | `+1` Advantage, `-3%` Army Maintenance | `+4` Advantage, `-12%` Army Maint, `-10%` Siege Phase Time, `+2` Knights, **`+1` Martial/Prowess per Devotion** | **`+8` Advantage**, **`-24%` Army Maint**, **`-20%` Siege Phase Time**, **`+4` Knights**, **`+2` Martial/Prowess per Devotion**, `no_prowess_loss_from_age = yes` | `+5` to `+50`/mo Martial |
| `mastery` | `+5%` Lifestyle XP Mult | `+20%` Lifestyle XP Mult, `+10` Scheme Success, `-10`d Scheme Phase, **`+1` Learning per Devotion**, **`+1` Max Personal Schemes** | **`+40%` Lifestyle XP Mult**, **`+20` Scheme Success**, **`-20`d Scheme Phase**, **`+2` Learning per Devotion**, **`+2` Max Personal Schemes**, **Ignore Culture Penalties**, `no_prowess_loss_from_age = yes` | `+5` to `+50`/mo Learning |
| `presence` | `+3` General Opinion, `-5%` Stress Gain | `+12` General Opinion, `-20%` Stress Gain, `+10%` Fame Impact, **`+1` Diplomacy per Devotion**, **`-10%` Short Reign**, **`+10%` Long Reign** | **`+24` General Opinion**, **`-40%` Stress Gain**, **`+20%` Fame Impact**, **`+2` Diplomacy per Devotion**, **`-20%` Short Reign**, **`+20%` Long Reign**, `no_prowess_loss_from_age = yes` | `+5` to `+50`/mo Diplomacy |
| `prosperity` | `+5%` Income, `-3%` Build Cost | `+20%` Income, `-12%` Build Cost, `-10%` MaA Maint, **`+1` Stewardship per Devotion**, **`+1` Domain Limit** | **`+40%` Income**, **`-24%` Holding & Domicile Build Cost**, **`-20%` MaA Maint**, **`+2` Stewardship per Devotion**, **`+2` Domain Limit**, `no_prowess_loss_from_age = yes` | `+5` to `+50`/mo Stewardship |
| `shadows` | `+5` Scheme Success, `-5` Enemy Scheme Success | `+20` Scheme Success, `-20` Enemy Scheme Success, `-10%` Enemy Max Cap, **`+1` Intrigue per Devotion**, **`+1` Max Hostile Schemes** | **`+40` Scheme Success**, **`-40` Enemy Scheme Success**, **`-20%` Enemy Max Cap**, **`+15%` Own Max Cap**, **`+2` Intrigue per Devotion**, **`+2` Max Hostile Schemes**, `no_prowess_loss_from_age = yes` | `+5` to `+50`/mo Intrigue |

---

## Acquisition Triggers

All routes invoke `bm_become_blood_mage_effect` or `bm_become_blood_knight_effect`:
- `bm_blood_cultist_become_blood_mage_decision`: Blóðtrú faithful initiation duel vs Egill Skallagrímsson (`bm_geyser_duel.0001`) in Reykjavik or Tsushima (`piety_level >= 2`, costs 1 Devotion level).
- `bm_enhance_blood_ritual_decision`: Non-faithful with occult traits/stats; identical Geyser duel (`piety_level >= 2`, costs 1 Devotion level).
- `grant_blood_magic_interaction`: Blood Mage initiates courtier/kin (`100` Piety + Major LF or `250` Piety + Minor LF).
- `make_blood_knight_interaction`: Blood Knight initiates kin/spouse/knight/courtier (`100` Piety + Major LF or `250` Piety + Minor LF).
- `ask_for_blood_magic_interaction`: Non-mage asks friend/lover/soulmate/liege Mage to teach them (`250` Piety; teacher consumes 1 Superior LF).
- `bm_get_blood_magic_from_prisoner_interaction`: Non-mage steals `lifestyle_blood_mage` from imprisoned Mage (`100` Piety, skill duel).
- `convert_to_blood_magic_from_witch`: Witch player swaps witch trait for `lifestyle_blood_mage`.
- **Birth:** Rolled via `on_birth_child` (`bm_blood_mage_prevalence_on_actions.txt`).

---

## Where the details live

| Component | File |
| --- | --- |
| Trait definitions | `common/traits/bm_blood_mage_trait.txt`, `bm_blood_knight_trait.txt`, `bm_blood_power_trait.txt` |
| XP helpers (`add_xp_bm_dynamic`, `add_shared_bm_bk_xp`, `add_blood_knight_xp`, `add_blood_power_xp`) | `common/scripted_effects/bm_trait_track_xp_gain_effects.txt` |
| Lifecycle & acquisition effects | `common/scripted_effects/bm_blood_mage_lifecycle_effects.txt` |
| Portrait progression values | `common/script_values/bm_blood_mage_portrait_values.txt` |
| Geyser initiation duels | `events/bm_geyser_duel_events.txt` |
| Blood Power event | `events/bm_blood_power_event.txt` |
