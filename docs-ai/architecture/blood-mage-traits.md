# Blood Mage Lifestyle Traits

Living technical specification for `lifestyle_blood_mage` and secondary `lifestyle_blood_power`.

## Archetypes & Sequential 3-Tier Hierarchy

| Lifestyle Trait | Tier | Fuel | Lifestyle Tracks (6) | Magic & Subsystem Access |
| --- | --- | --- | --- | --- |
| **Blood Acolyte** (`lifestyle_bm_acolyte`) | Tier I | Minor Lifeforce | `bloodline`, `hematurgy`, `benediction`, `enlightenment`, `bloodlust`, `ancient` | Minor Blood Magic Grimoire; foundational Major rites (Rank 1 trait manifestation, up to 3★ education, Minor/Major Runes, Blood Power channeling). Standard 0.5x track scaling; age lock at 100 XP on Ancient. |
| **Blood Mage** (`lifestyle_blood_mage`) | Tier II | Major Lifeforce | `bloodline`, `hematurgy`, `benediction`, `enlightenment`, `bloodlust`, `ancient` | Minor & Major Grimoire; congenital manifestation up to Rank 3, education up to 4★, prisoner trait theft, Tier II covenants, Major Blood Runes, Blood Berserkers. Base stat floor absorbs Tier I vitals (2.0 health, 30 life, +1 domain limit, +1 personal tenet slot) + 50 XP milestones (+1 stats and prowess per piety level) + permanent age lock. |
| **Blood Archmage** (`lifestyle_bm_archmage`) | Tier III | Superior Lifeforce | `bloodline`, `hematurgy`, `benediction`, `enlightenment`, `bloodlust`, `ancient` | Full Superior Grimoire; 5★ Master education, 2nd education, Rank 4–5 traits, Blood Golems, Galdrastafir, Tier III covenants, deadly ailment cure, Behemoths. Base stat floor absorbs Tier II vitals (5.0 health, 100 life, +2 domain limit, +2 personal tenet slots) + 50 XP milestones (+2 stats and prowess per piety level) + permanent age lock. 1.5x–2.0x apex scaling. |
| **Blood Power** (`lifestyle_blood_power`) | Secondary | — | 6 tracks: `dynasty`, `warband`, `mastery`, `presence`, `prosperity`, `shadows` | Retained alongside primary tier trait; never reset on tier elevation. +0.1 monthly Piety and +5 monthly Lifestyle XP per 10 XP step, 50 XP milestones, 100 XP capstones including `no_prowess_loss_from_age = yes`. |

- **Inheritance & Base:** Inheritable non-genetic (`25%` single parent, `50%` with Superior Feingur, `100%` both parents, `0.20%` birth), audited by `bm_blood_mage_prevalence` rule. Base: `same_opinion = 10`, `ignores_gender_army_rules = yes`.
- **Track Structure:** 10 tiers (10–100 XP). Tiers 10–40 and 60–90 grant standard Vitality step (`+0.1` Health, `+2` Life Exp; 0.5x Acolyte, 1.5x Archmage; epidemic resistance reserved for Lifeforce). Tier 50 = Devotion-scaling milestones (`<stat>_per_piety_level = 1`); Tier 100 = Devotion Apex (and age lock for Acolyte / Blood Power; Mage and Archmage hold permanent age lock on their base trait).

---

## Devotion Lifestyle Tracks

Complete XP sources live in [`blood-mage-track-xp.md`](blood-mage-track-xp.md), [`blood-mage-track-xp-mage.md`](blood-mage-track-xp-mage.md), and [`blood-mage-bloodlust.md`](blood-mage-bloodlust.md).

| Track | 10 XP (1st Step) | 50 XP (Cumulative Milestone) | 100 XP (Cumulative Capstone) |
| --- | --- | --- | --- |
| `ancient` | Vitality + `+5%` Monthly Renown Mult (`+0.1` Monthly Legitimacy Add at 20, 40, 60, 80) | 4× Vitality + `+20%` Monthly Renown Mult, `+0.2` Monthly Legitimacy, `+20%` Devotion Impact, `+1` Tenet Slot | 8× Vitality + `+40%` Monthly Renown Mult, `+0.4` Monthly Legitimacy, `+60%` Devotion Impact, `+2` Tenet Slots, `no_prowess_loss_from_age = yes` (Acolyte) |
| `enlightenment` | Vitality + `+5%` Monthly Piety Mult | 4× Vitality + `+20%` Monthly Piety Mult, `+1` Learning per Piety level, `+8%` Lifestyle XP | 8× Vitality + `+40%` Monthly Piety Mult, `+2` Learning per Piety level, `+23%` Lifestyle XP |
| `benediction` | Vitality + `+2` General Opinion (`+5%` Monthly Prestige Mult at 20, 40, 60, 80) | 4× Vitality + `+8` General Opinion, `+10%` Monthly Prestige Mult, `+1` Diplomacy per Piety level | 8× Vitality + `+16` General Opinion, `+20%` Monthly Prestige Mult, `+2` Diplomacy per Piety level |
| `bloodline` | Vitality + `+3%` Monthly Income Mult | 4× Vitality + `+12%` Monthly Income Mult, `+1` Stewardship per Piety level, `+1` Domain Limit | 8× Vitality + `+24%` Monthly Income Mult, `+2` Stewardship per Piety level, `+2` Domain Limit |
| `hematurgy` | Vitality + `+4` Hostile Scheme Success (`-8` Enemy Hostile Scheme Success at 20, 40, 60, 80) | 4× Vitality + `+16` Hostile Scheme Success, `-16` Enemy Hostile Scheme Success, `+1` Intrigue per Piety level | 8× Vitality + `+32` Hostile Scheme Success, `-32` Enemy Hostile Scheme Success, `+1` Max Hostile Schemes, `+2` Intrigue per Piety level |
| `bloodlust` | Vitality + `+10%` Knight Effectiveness (`+1` Knight Limit at 20, 40, 60, 80) | 4× Vitality + `+40%` Knight Effectiveness, `+2` Knight Limit, `+1` Martial & Prowess per Piety level | 8× Vitality + `+80%` Knight Effectiveness, `+4` Knight Limit, `+2` Martial & Prowess per Piety level |

---

## Secondary Blood Power Tracks (`lifestyle_blood_power`)

Base: none. Granted automatically with Mage at base 0 XP. Consolidated into 5 distinct milestones at 10, 30, 50, 70, and 100 XP. In CK3 engine mechanics, trait track thresholds stack additively (all reached tiers add together); each script block defines the incremental delta granted at that milestone. Every 10 XP grants **+5 flat monthly Lifestyle XP** (+15 quarterly) via `quarterly_playable_pulse`. Shared 50 and 100 milestones award `+10%` Monthly Piety Mult, `+5` Life Expectancy, `+0.25` Health, and `+0.02` Monthly Piety per sworn knight (`+20%`, `+10`, `+0.50`, `+0.04` total per track). Full breakdown in [`blood-mage-blood-power.md`](blood-mage-blood-power.md).

| Track | 10 XP (Starter) | 30 XP (Medium) | 50 XP (Milestone) | 70 XP (Major) | 100 XP (Capstone) | Flat Lifestyle XP |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `presence` | `+0.1` Piety, `+5` Opinion, `+0.2` Prestige, `+5%` Legitimacy, `+8` Scheme | `+0.3` Piety, `+10` Opinion, `+0.4` Prestige, `+10%` Legitimacy, `+16` Scheme | `+0.5` Piety, `+15` Opinion, `+0.7` Prestige, `+16%` Legitimacy, `+24` Scheme, `+1` Max Schemes | `+0.7` Piety, `+20` Opinion, `+1.0` Prestige, `+23%` Legitimacy, `+32` Scheme, `+1` Max Schemes | **`+1.0` Piety**, **`+25` Opinion**, **`+1.5` Prestige**, **`+30%` Legitimacy**, **`+40` Scheme**, **`+2` Max Schemes**, Age Lock | `+5` to `+50`/mo Diplomacy |
| `warband` | `+0.1` Piety, `+1` Knight, `+15%` Knight Eff, `+2` Adv, `+5%` Speed | `+0.3` Piety, `+2` Knight, `+30%` Knight Eff, `+4` Adv, `+10%` Speed | `+0.5` Piety, `+4` Knight, `+45%` Knight Eff, `+6` Adv, `+15%` Speed | `+0.7` Piety, `+6` Knight, `+60%` Knight Eff, `+8` Adv, `+20%` Speed | **`+1.0` Piety**, **`+8` Knight**, **`+75%` Knight Eff**, **`+10` Adv**, **`+25%` Speed**, Age Lock | `+5` to `+50`/mo Martial |
| `prosperity` | `+0.1` Piety, `+0.3` Gold, `+6%` Income Mult, `-6%` MaA Maint | `+0.3` Piety, `+0.6` Gold, `+12%` Income Mult, `-12%` MaA Maint | `+0.5` Piety, `+1.0` Gold, `+18%` Income Mult, `-18%` MaA Maint | `+0.7` Piety, `+1.4` Gold, `+24%` Income Mult, `-24%` MaA Maint | **`+1.0` Piety**, **`+2.0` Gold**, **`+30%` Income Mult**, **`-30%` MaA Maint**, Age Lock | `+5` to `+50`/mo Stewardship |
| `shadows` | `+0.1` Piety, `+8` Hostile, `-10` Enemy, `+6` Dread | `+0.3` Piety, `+16` Hostile, `-20` Enemy, `+12` Dread | `+0.5` Piety, `+24` Hostile, `-30` Enemy, `+18` Dread, `+1` Max Schemes | `+0.7` Piety, `+32` Hostile, `-40` Enemy, `+24` Dread, `+1` Max Schemes | **`+1.0` Piety**, **`+40` Hostile**, **`-50` Enemy**, **`+30` Dread**, **`+2` Max Schemes**, Age Lock | `+5` to `+50`/mo Intrigue |
| `mastery` | `+0.1` Piety, `+10%` XP, `-10%` Stress Gain, `+10%` Stress Loss | `+0.3` Piety, `+20%` XP, `-20%` Stress Gain, `+20%` Stress Loss | `+0.5` Piety, `+30%` XP, `-30%` Stress Gain, `+30%` Stress Loss | `+0.7` Piety, `+40%` XP, `-40%` Stress Gain, `+40%` Stress Loss | **`+1.0` Piety**, **`+50%` XP**, **`-50%` Stress Gain**, **`+50%` Stress Loss**, Age Lock | `+5` to `+50`/mo Learning |
| `dynasty` | `+0.1` Piety, `+10%` Strengthen | `+0.3` Piety, `+20%` Strengthen | `+0.5` Piety, `+30%` Strengthen, `-50%` Inbreed | `+0.7` Piety, `+40%` Strengthen, `-50%` Inbreed | **`+1.0` Piety**, **`+50%` Strengthen**, **Immunity (`-100%`)**, Age Lock | `+5` to `+50`/mo Active Focus |

---

## Acquisition Triggers

All routes invoke `bm_become_blood_mage_effect`:
- `bm_blood_cultist_become_blood_mage_decision`: Blóðtrú faithful initiation duel vs Egill Skallagrímsson (`bm_geyser_duel.0001`) in Reykjavik or Tsushima (`piety_level >= 2`, costs 1 Devotion level).
- `bm_enhance_blood_ritual_decision`: Non-faithful with occult traits/stats; identical Geyser duel (`piety_level >= 2`, costs 1 Devotion level).
- `grant_blood_magic_interaction`: Blood Mage initiates courtier/kin (`100` Piety + Major LF or `250` Piety + Minor LF).
- `ask_for_blood_magic_interaction`: Non-mage asks friend/lover/soulmate/liege Mage to teach them (`250` Piety; teacher consumes 1 Superior LF).
- `bm_get_blood_magic_from_prisoner_interaction`: Non-mage steals `lifestyle_blood_mage` from imprisoned Mage (`100` Piety, skill duel).
- `convert_to_blood_magic_from_witch`: Witch player swaps witch trait for `lifestyle_blood_mage`.
- **Birth:** Rolled via `on_birth_child` (`bm_blood_mage_prevalence_on_actions.txt`).

---

## Where the details live

| Component | File |
| --- | --- |
| Trait definitions | `common/traits/bm_blood_mage_trait.txt`, `bm_blood_power_trait.txt` |
| XP helpers (`add_xp_bm_dynamic`, `add_shared_bm_bk_xp`, `add_blood_power_xp`) | `common/scripted_effects/bm_trait_track_xp_gain_effects.txt` |
| Lifecycle & acquisition effects | `common/scripted_effects/bm_blood_mage_lifecycle_effects.txt` |
| Portrait progression values | `common/script_values/bm_blood_mage_portrait_values.txt` |
| Geyser initiation duels | `events/bm_geyser_duel_events.txt` |
| Blood Power event | `events/bm_blood_power_event.txt` |
