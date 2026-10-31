# Blood Mage Lifestyle Traits

Living technical specification for `lifestyle_blood_mage`, `lifestyle_blood_knight`, and secondary `lifestyle_blood_power`.

## Archetypes & Class Comparison

| Lifestyle Trait | Archetype | Exclusive Tracks (2) | Shared Devotion Tracks (3) | Magic & Subsystem Access |
| --- | --- | --- | --- | --- |
| **Blood Mage** (`lifestyle_blood_mage`) | *Shepherd of the Faithful* — Occult scholar, dynasty architect, scheme master | `bloodline`, `hematurgy` | `ancient`, `enlightenment`, `benediction` | Minor, Major, Superior Blood Magic; builds Duchy Blood Temples (`bm_duchy_buildings.txt`); inscribes Superior Blood Runes on others. |
| **Blood Knight** (`lifestyle_blood_knight`) | *Fire and Sword* — Martial warlord, battlefield harvester, champion | `vanguard`, `slaughter` | `ancient`, `enlightenment`, `benediction` | Minor, Major, Superior Blood Magic; harvests Lifeforce from battles, single combat, yearly pulse; recruits Blood Berserkers & Behemoths; empowers sworn knights. |
| **Blood Power** (`lifestyle_blood_power`) | *Secondary Personal Mastery* — Granted alongside Mage or Knight (base 0 XP) | 6 tracks: `dynasty`, `warband`, `mastery`, `presence`, `prosperity`, `shadows` | — | Advanced via Major Magic (`bm_cast_blood_magic_major.001.power`). +0.1 monthly Piety and +5 monthly Lifestyle XP per 10 XP step, 50 XP milestones, 100 XP capstones including `no_prowess_loss_from_age = yes`. |

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

Base: none. Granted automatically with Mage or Knight at base 0 XP. Consolidated into 5 distinct milestones at 10, 30, 50, 70, and 100 XP. In CK3 engine mechanics, trait track thresholds stack additively (all reached tiers add together); each script block defines the incremental delta granted at that milestone. Every 10 XP grants **+5 flat monthly Lifestyle XP** (+15 quarterly) via `quarterly_playable_pulse`. Full breakdown in [`blood-mage-blood-power.md`](blood-mage-blood-power.md).

| Track | 10 XP (Starter) | 30 XP (Medium) | 50 XP (Milestone) | 70 XP (Major) | 100 XP (Capstone) | Flat Lifestyle XP |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `presence` | `+0.1` Piety, `+5` Success, `-5d` Phase | `+0.3` Piety, `+10` Success, `-10d` Phase | `+0.5` Piety, `+15` Success, `-15d` Phase, `+15%` Renown | `+0.7` Piety, `+20` Success, `-20d` Phase, `+15%` Renown | **`+1.0` Piety**, **`+25` Success**, **`-25d` Phase**, **`+35%` Renown**, **`+1` Max Schemes**, Age Lock | `+5` to `+50`/mo Diplomacy |
| `warband` | `+0.1` Piety, `+15%` Knight Eff, `+1` Knight Limit | `+0.3` Piety, `+30%` Knight Eff, `+2` Knight Limit | `+0.5` Piety, `+45%` Knight Eff, `+2` Knight Limit, `+2` Adv | `+0.7` Piety, `+60%` Knight Eff, `+3` Knight Limit, `+2` Adv | **`+1.0` Piety**, **`+75%` Knight Eff**, **`+4` Knight Limit**, **`+5` Adv**, Age Lock | `+5` to `+50`/mo Martial |
| `prosperity` | `+0.1` Piety, `+15%` Income, `-5%` MaA Maint | `+0.3` Piety, `+30%` Income, `-10%` MaA Maint | `+0.5` Piety, `+45%` Income, `-15%` MaA Maint, `+0.5` Gold | `+0.7` Piety, `+60%` Income, `-20%` MaA Maint, `+0.5` Gold | **`+1.0` Piety**, **`+75%` Income**, **`-25%` MaA Maint**, **`+1.5` Gold**, Age Lock | `+5` to `+50`/mo Stewardship |
| `shadows` | `+0.1` Piety, `+8` Hostile, `+5` Dread | `+0.3` Piety, `+16` Hostile, `+10` Dread | `+0.5` Piety, `+24` Hostile, `+15` Dread, `+1` Max Schemes | `+0.7` Piety, `+32` Hostile, `+20` Dread, `+1` Max Schemes | **`+1.0` Piety**, **`+40` Hostile**, **`+25` Dread**, **`+2` Max Schemes**, **`+15` Own Cap**, Age Lock | `+5` to `+50`/mo Intrigue |
| `mastery` | `+0.1` Piety, `+8%` XP, `-8%` Stress | `+0.3` Piety, `+16%` XP, `-16%` Stress | `+0.5` Piety, `+24%` XP, `-24%` Stress, `+0.25` Health | `+0.7` Piety, `+32%` XP, `-32%` Stress, `+0.25` Health | **`+1.0` Piety**, **`+40%` XP**, **`-40%` Stress**, **`+0.50` Health**, **`+20%` Piety Mult**, Age Lock | `+5` to `+50`/mo Learning |
| `dynasty` | `+0.1` Piety, `+15%` Strengthen, `+4` Fertile | `+0.3` Piety, `+30%` Strengthen, `+8` Fertile | `+0.5` Piety, `+45%` Strengthen, `+12` Fertile, `-50%` Inbreed | `+0.7` Piety, `+60%` Strengthen, `+16` Fertile, `-50%` Inbreed | **`+1.0` Piety**, **`+75%` Strengthen**, **`+20` Fertile**, **Immunity (`-100%`)**, Age Lock | `+5` to `+50`/mo Active Focus |

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
