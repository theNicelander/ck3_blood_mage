# Archive: Blood Knight (`lifestyle_blood_knight`) — Deprecated in v1.20.68

> [!NOTE] Historical Archive
> This document preserves the architectural specification of the `lifestyle_blood_knight` trait, its tracks (`vanguard`, `slaughter`), and related systems as they existed prior to consolidation in release **v1.20.68**. In v1.20.68, all Blood Knight mechanics and XP sources were unified into the single `lifestyle_blood_mage` trait under the new **Bloodlust** (`bloodlust`) track, preparing the path for a linear Acolyte -> Mage -> Archmage tier system.

---

## Historical Overview (Pre-v1.20.68)

Permanent, Devotion-anchored martial endgame peer (`lifestyle_blood_knight`) to `lifestyle_blood_mage` (*Fire and Sword* vs *Shepherd of the Faithful*).
- **Traits & Base:** `gfx/interface/icons/traits/bm_blood_knight.dds`. Base: `same_opinion = 10`, `ruler_designer_cost = 50`. Inheritable (`25%` single parent, `100%` both, `0.20%` spontaneous birth), scaled by `bm_blood_knight_prevalence` rule. Mutually exclusive with `lifestyle_blood_mage` (dual-wielding reserved for Egill Skallagrímsson).
  - **Knight & Commander Exemption:** Blood Knights automatically received the vanilla character modifier `ignores_gender_army_rules` ("Worthy Commander"), enabling them to serve as both knights and army commanders across all cultures and faiths regardless of gender restrictions. (In v1.20.68+, this exemption was granted to all Blood Mages).
- **Acquisition (Historical):**
  - `make_blood_knight_interaction`: Initiated by a Blood Knight or Blood Mage on spouse, child, kin, knight, or courtier.
  - **Superior Magic Transmutation (`bm_cast_blood_magic_superior_decision`):** Human player option to transmute between Blood Mage and Blood Knight for 1 Superior Lifeforce.
  - **Geyser Duel Initiation (`bm_geyser_duel.0001`):** Travel to Reykjavik or Tsushima, duel Egill in prowess.
- **Apex Devotion & Milestones:** Shared 100 XP capstones (`ancient`, `enlightenment`, `benediction`) grant Devotion scaling. Standard Vitality steps applied across all tracks.

---

## Historical Harvesting & Advancement

- **Battlefield Victory (`bm_on_combat_end_winner`):** As commander or knight: `+1` to `+5` `vanguard` XP; rolls troop-scaled Lifeforce (`10%–100%` Minor, `0%–100%` Major across `<100` to `10,000+` troops).
- **Battlefield Defeat (`bm_on_combat_end_loser`):** As commander or knight: `+1` to `+3` `vanguard` XP, `0` to `+2` `enlightenment` XP.
- **Fatal Single Combat (`bm_on_character_death_duel`):** Slaying a foe granted `+5` `slaughter` XP and 1 Major Lifeforce. If foe had `prowess >= 20` or held Mage/Knight trait: 25% chance of 1 Superior Lifeforce.
- **Tournament Completion (`bm_on_travel_activity_complete_tournament`):** `+3` `slaughter` XP.
- **Yearly Ambient Pulse (`blood_mage_yearly_events.004`):** Passive ~33% chance/year for 1 Minor Lifeforce + `+1` `ancient` XP. Exclusive to Blood Knights.

---

## Historical Exclusive Tracks

| Track | Focus | Step Bonus (Tiers 10–40, 60–90) | 50 XP Milestone | 100 XP Capstone |
| --- | --- | --- | --- | --- |
| **`vanguard`** | Army Command & Speed | `+1` Advantage (tiers 20–40, 60–90), `+1.75%` Army Speed (`+1` Martial at 20, 40, 60, 80) | 4× Vitality + `+3` Advantage, `+7%` Army Speed, `+2` Martial, `+1` Martial per Piety Level | 8× Vitality + `+7` Advantage, `+14%` Army Speed, `+4` Martial, `+1.5` Martial per Piety Level, `no_prowess_loss_from_age = yes` |
| **`slaughter`** | Lethality & Knights | `+1.5` or `+2` Prowess, `+1` Knight Limit (tiers 20–40, 60–90), `+8.75%` Knight Effectiveness | 4× Vitality + `+7` Prowess, `+3` Knight Limit, `+35%` Knight Effectiveness, `+1` Prowess per Piety Level | 8× Vitality + `+14` Prowess, `+7` Knight Limit, `+70%` Knight Effectiveness, `+2` Prowess per Piety Level, `no_prowess_loss_from_age = yes` |

---

## Consolidation Mapping in v1.20.68

| Pre-v1.20.68 System | Status in v1.20.68+ |
| --- | --- |
| `lifestyle_blood_knight` trait | **Deleted**. All characters use `lifestyle_blood_mage`. |
| `vanguard` track | Consolidated into `bloodlust` track on `lifestyle_blood_mage`. |
| `slaughter` track | Consolidated into `bloodlust` track on `lifestyle_blood_mage`. |
| Battlefield victory XP | Awards `+1` to `+3` `bloodlust` XP (halved to eliminate rapid progression bloat). |
| Battlefield defeat XP | Awards `+1` `bloodlust` XP. |
| Single combat lethal kill | Awards `+3` `bloodlust` XP + 1 Major Lifeforce. |
| Tournament completion | Awards `+2` `bloodlust` XP. |
| `make_blood_knight_interaction` | **Deleted**. Initiation unified under `bm_grant_blood_magic` and faith rites. |
| Transmutation between Mage and Knight | **Deleted**. Unneeded due to unified track layout. |
| `bm_blood_knight_prevalence` rule | **Deleted**. Prevalences unified under `bm_prevalence`. |
| Worthy Commander trait flag | Granted to all Blood Mages upon trait gain. |
