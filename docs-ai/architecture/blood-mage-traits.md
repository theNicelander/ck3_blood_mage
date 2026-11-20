# Blood Mage Lifestyle Traits

Living technical specification for `lifestyle_bm_acolyte`, `lifestyle_blood_mage`, and `lifestyle_bm_archmage`.

## Archetypes & Sequential 3-Tier Hierarchy

| Lifestyle Trait | Tier | Fuel | Lifestyle Tracks (6) | Magic & Subsystem Access |
| --- | --- | --- | --- | --- |
| **Blood Acolyte** (`lifestyle_bm_acolyte`) | Tier I | Minor Lifeforce | `radiance`, `fury`, `fortune`, `cunning`, `wisdom`, `ancient` | Minor Blood Magic Grimoire; foundational Major rites (Rank 1 trait manifestation, up to 3★ education, Minor/Major Runes). Track steps grant `+2` life expectancy per milestone (`60` max). |
| **Blood Mage** (`lifestyle_blood_mage`) | Tier II | Major Lifeforce | `radiance`, `fury`, `fortune`, `cunning`, `wisdom`, `ancient` | Minor & Major Grimoire; congenital manifestation up to Rank 3, education up to 4★, prisoner trait theft, Tier II covenants, Major Blood Runes, Blood Berserkers. Base stat floor: `2.0` health, `40` life expectancy (`130` max with `+3`/milestone), `+1.00` renown, `+3.00` piety, `+1` personal tenet slot, `+1` max piety level, `+1.0%` knight effectiveness per learning, permanent age lock, `+3` to all 5 main attributes, `+1` to all 5 main attributes per piety level, `+10%` income mult, `+1` max personal & hostile schemes, `+0.05` monthly piety per knight, and `+10%` monthly lifestyle XP gain. |
| **Blood Archmage** (`lifestyle_bm_archmage`) | Tier III | Superior Lifeforce | `radiance`, `fury`, `fortune`, `cunning`, `wisdom`, `ancient` | Full Superior Grimoire; 5★ Master education, 2nd education, Rank 4–5 traits, Blood Golems, Galdrastafir, Tier III covenants, deadly ailment cure, Behemoths. Base stat floor: `5.0` health, `100` life expectancy (`220` max with `+4`/milestone), `+2.00` renown, `+6.00` piety, `+2` personal tenet slots, `+2` max piety levels, `+2.0%` knight effectiveness per learning, permanent age lock, `+6` to all 5 main attributes, `+2` to all 5 main attributes per piety level, `+20%` income mult, `+2` max personal & hostile schemes, `+0.10` monthly piety per knight, and `+20%` monthly lifestyle XP gain. |

- **Inheritance & Base:** Inheritable non-genetic (`25%` single parent, `50%` with Superior Feingur, `100%` both parents, `0.20%` birth), audited by `bm_blood_mage_prevalence` rule.
- **Track Structure:** 5 milestones (10, 30, 50, 70, 100 XP). All 5 milestones grant `+0.2` Health (`+1.0` per track) and tier-scaled Life Expectancy (`+2` Acolyte, `+3` Mage, `+4` Archmage per step). Attribute tracks grant `+0.1` Monthly Piety and `+1` attribute at every milestone (`+0.5` Piety, `+5` attribute total) and `+1` attribute per piety level at 30/70 (`+2` total), plus track-specific extras at 50/100 (`+1` scheme/tenet slot, `+10%` income mult, or `+1.0%` knight eff/learning; `ancient` grants `+0.2` Monthly Piety and `+0.01`/knight at all 5 steps).

---

## Devotion Lifestyle Tracks

Complete XP sources live in [`blood-mage-track-xp.md`](blood-mage-track-xp.md), [`blood-mage-track-xp-mage.md`](blood-mage-track-xp-mage.md), and [`blood-mage-fury.md`](blood-mage-fury.md).

| Track | 10 XP (1st Step) | 30 XP (Cumulative) | 50 XP (Cumulative) | 70 XP (Cumulative) | 100 XP (Cumulative Capstone) |
| --- | --- | --- | --- | --- | --- |
| `radiance` | Vitality + `+0.1` Piety, `+1` Diplomacy | 2× Vitality + `+0.2` Piety, `+2` Diplomacy, `+1` Diplomacy / Piety Level | 3× Vitality + `+0.3` Piety, `+3` Diplomacy, `+1` Diplomacy / Piety Level, `+1` Max Personal Schemes | 4× Vitality + `+0.4` Piety, `+4` Diplomacy, `+2` Diplomacy / Piety Level, `+1` Max Personal Schemes | 5× Vitality + `+0.5` Piety, `+5` Diplomacy, `+2` Diplomacy / Piety Level, `+2` Max Personal Schemes |
| `fury` | Vitality + `+0.1` Piety, `+1` Martial | 2× Vitality + `+0.2` Piety, `+2` Martial, `+1` Martial / Piety Level | 3× Vitality + `+0.3` Piety, `+3` Martial, `+1` Martial / Piety Level, `+1.0%` Knight Eff / Learning | 4× Vitality + `+0.4` Piety, `+4` Martial, `+2` Martial / Piety Level, `+1.0%` Knight Eff / Learning | 5× Vitality + `+0.5` Piety, `+5` Martial, `+2` Martial / Piety Level, `+2.0%` Knight Eff / Learning |
| `fortune` | Vitality + `+0.1` Piety, `+1` Stewardship | 2× Vitality + `+0.2` Piety, `+2` Stewardship, `+1` Stewardship / Piety Level | 3× Vitality + `+0.3` Piety, `+3` Stewardship, `+1` Stewardship / Piety Level, `+10%` Income Mult | 4× Vitality + `+0.4` Piety, `+4` Stewardship, `+2` Stewardship / Piety Level, `+10%` Income Mult | 5× Vitality + `+0.5` Piety, `+5` Stewardship, `+2` Stewardship / Piety Level, `+20%` Income Mult |
| `cunning` | Vitality + `+0.1` Piety, `+1` Intrigue | 2× Vitality + `+0.2` Piety, `+2` Intrigue, `+1` Intrigue / Piety Level | 3× Vitality + `+0.3` Piety, `+3` Intrigue, `+1` Intrigue / Piety Level, `+1` Max Hostile Schemes | 4× Vitality + `+0.4` Piety, `+4` Intrigue, `+2` Intrigue / Piety Level, `+1` Max Hostile Schemes | 5× Vitality + `+0.5` Piety, `+5` Intrigue, `+2` Intrigue / Piety Level, `+2` Max Hostile Schemes |
| `wisdom` | Vitality + `+0.1` Piety, `+1` Learning | 2× Vitality + `+0.2` Piety, `+2` Learning, `+1` Learning / Piety Level | 3× Vitality + `+0.3` Piety, `+3` Learning, `+1` Learning / Piety Level, `+1` Personal Tenet Slot | 4× Vitality + `+0.4` Piety, `+4` Learning, `+2` Learning / Piety Level, `+1` Personal Tenet Slot | 5× Vitality + `+0.5` Piety, `+5` Learning, `+2` Learning / Piety Level, `+2` Personal Tenet Slots |
| `ancient` | Vitality + `+0.20` Piety, `+0.20` Renown, `+0.01` Piety / Knight, `+2%` Lifestyle XP | 2× Vitality + `+0.40` Piety, `+0.40` Renown, `+0.02` Piety / Knight, `+4%` Lifestyle XP | 3× Vitality + `+0.60` Piety, `+0.60` Renown, `+0.03` Piety / Knight, `+6%` Lifestyle XP | 4× Vitality + `+0.80` Piety, `+0.80` Renown, `+0.04` Piety / Knight, `+8%` Lifestyle XP | 5× Vitality + `+1.00` Piety, `+1.00` Renown, `+0.05` Piety / Knight, `+10%` Lifestyle XP, `+1` Max Piety Level |

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
| Trait definitions | `common/traits/bm_blood_mage_trait.txt` |
| XP helpers (`add_xp_bm_dynamic`, `add_shared_bm_bk_xp`) | `common/scripted_effects/bm_trait_track_xp_gain_effects.txt` |
| Lifecycle & acquisition effects | `common/scripted_effects/bm_blood_mage_lifecycle_effects.txt` |
| Portrait progression values | `common/script_values/bm_blood_mage_portrait_values.txt` |
| Geyser initiation duels | `events/bm_geyser_duel_events.txt` |
