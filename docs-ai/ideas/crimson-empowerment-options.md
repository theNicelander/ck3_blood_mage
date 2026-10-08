# Ideas: Crimson Empowerment Overhaul & Adventurer Support

Living brainstorm / proposal document for redesigning and strengthening the `lifestyle_crimson_empowerment` trait, especially addressing landless adventurer utility and low return on investment.

---

## 1. Current State & Pain Points

- **High Cost vs. Low Reward**: Consumes 150 Piety + a **Major Lifeforce** per rank (10 XP). The rewards (`+0.05` control, `+0.05` development, `+2.5%` domain tax per rank) feel marginal compared to other blood magic rituals.
- **Strictly Landed Bias**:
  - `fury`: County control growth does nothing for landless characters or commanders on the road.
  - `prosperity`: Capital county development and domain tax are completely wasted on unlanded adventurers / wandering mercenaries.
  - `insight`: County development growth only affects landed holdings.
  - `expertise`: Cultural fascination mult is 100% useless unless you are the Cultural Head.
- **Missing Travel/Adventurer Integration**: Since vanilla 1.20 and Roads to Power introduced landless play, camp logistics, and travel hazards, the empowerment trait does not leverage these systems.

---

## 2. 5 Options Per Track (Concise Overview)

All candidate modifiers use verified vanilla 1.20 script keys. Values are listed **per rank** (10 ranks / up to 100 XP per track).

| Track | Option 1 | Option 2 | Option 3 | Option 4 | Option 5 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`charisma`** *(Diplomacy)* | `adventurer_contract_reward_mult = 0.05`<br>*(+5% Contract Rewards)* | `sway_scheme_power_mult = 0.05`<br>*(+5% Sway Scheme Power)* | `courtier_and_guest_opinion = 3`<br>*(+3 Follower / Guest Opinion)* | `diplomatic_range_mult = 0.05`<br>*(+5% Interaction Range)* | `mercenary_hire_cost_mult = -0.03`<br>*(-3% Mercenary Recruitment Cost)* |
| **`fury`** *(Martial)* | `character_travel_speed = 2`<br>*(+2 Flat Travel Speed)* | `prowess = 1`<br>*(+1 Prowess every 2 ranks)* | `advantage = 1`<br>*(+1 Commander Advantage)* | `knight_limit = 1`<br>*(+1 Knight cap at ranks 3, 6, 9)* | `maa_damage_mult = 0.03`<br>*(+3% Men-at-Arms Damage)* |
| **`prosperity`** *(Stewardship)* | `provisions_gain_mult = 0.05`<br>*(+5% Provisions Gained)* | `provisions_capacity_add = 30`<br>*(+30 Max Provisions)* | `men_at_arms_maintenance = -0.03`<br>*(-3% MaA / Retinue Cost)* | `provisions_loss_mult = -0.03`<br>*(-3% Provision Consumption)* | `domicile_building_cost_mult = -0.03`<br>*(-3% Camp / Estate Cost)* |
| **`shadows`** *(Intrigue)* | `character_travel_safety = 2`<br>*(+2 Travel Safety)* | `hostile_scheme_resistance_add = 3`<br>*(+3 Scheme Resistance)* | `hostile_scheme_phase_duration_mult = -0.03`<br>*(-3% Scheme Speed / Delay)* | `stress_gain_mult = -0.03`<br>*(-3% Stress Gain)* | `character_travel_speed_mult = 0.03`<br>*(+3% Travel Speed)* |
| **`insight`** *(Learning)* | `character_travel_safety = 2`<br>*(+2 Travel Safety)* | `stress_loss_mult = 0.05`<br>*(+5% Stress Relief)* | `health = 0.08`<br>*(+0.08 Health, +0.8 at cap)* | `learn_language_scheme_power_mult = 0.10`<br>*(+10% Language Scheme Power)* | `personal_scheme_power_mult = 0.05`<br>*(+5% Personal Scheme Power)* |
| **`legacy`** *(Bloodline)* | `fertility = 0.03`<br>*(+3% Fertility)* | `dynasty_opinion = 3`<br>*(+3 Dynasty / Kin Opinion)* | `monthly_dynasty_prestige_mult = 0.03`<br>*(+3% Dynasty Renown Mult)* | `child_education_aptitude = 2`<br>*(+2 Ward / Child Education)* | `natural_prowess = 1`<br>*(+1 Base Prowess for bloodline)* |
| **`expertise`** *(Versatility)* | `character_travel_speed_mult = 0.04`<br>*(+4% Travel Speed Mult)* | `monthly_lifestyle_xp_gain_mult = 0.03`<br>*(Boost to +5.5% Total Lifestyle XP)* | `different_culture_opinion = 2`<br>*(+2 Foreign Culture Opinion)* | `all_skills = 0.5`<br>*(+1 All Stats every 2 ranks)* | `character_travel_safety = 1.5`<br>*(+1.5 Travel Safety)* |

---

## 3. High-Level Architectural Paths

### Path 1: Dual-Benefit Integration (Keep 7 Tracks)
- Retain the existing 7 tracks (`charisma`, `fury`, `prosperity`, `shadows`, `insight`, `legacy`, `expertise`).
- Add one universal or adventurer modifier to each track alongside the existing landed modifiers.
- **Pros**: Zero UI changes to events/decisions; zero script trigger reworks; works immediately for landed and unlanded alike.
- **Cons**: Still retains some dead stats for adventurers viewing the tooltip.

### Path 2: Replace Dead Landed Modifiers Outright (Keep 7 Tracks)
- Strip out `character_capital_county_monthly_development_growth_add`, `monthly_county_control_growth_add`, and `cultural_head_fascination_mult`.
- Replace them with body/caravan mechanics:
  - `fury`: Knight effectiveness + Travel/Army Speed or Direct Prowess.
  - `prosperity`: Domain tax + Provisions efficiency / MaA maintenance reduction.
  - `expertise`: Lifestyle XP mult + Travel speed / Language learning.
- **Pros**: Every single modifier on the trait benefits any character archetype.

### Path 3: Add Dedicated New Tracks (Expand to 8 or 9 Tracks)
Instead of forcing travel/survival stats into the standard 5 attribute tracks, introduce dedicated new tracks:

1. **New Track: `wayfarer` (The Roaming Blood)**:
   - Dedicated wanderer/adventurer track.
   - Modifiers: `character_travel_speed_mult = 0.04`, `character_travel_safety = 2.5`, `provisions_capacity_add = 40`, `movement_speed = 0.02`.
2. **New Track: `transmutation` (Somatic / Bodily Fortification)**:
   - Dedicated physical body refinement.
   - Modifiers: `prowess = 1`, `health = 0.1`, `stress_loss_mult = 0.05`, `fertility = 0.02`.
3. **New Track: `dominion` (The Overlord / Landed Track)**:
   - Move all development, county control, and domain tax here so only landed rulers choose it.

- **Pros**: Maximum roleplay flavor; clear player choices.
- **Cons**: Requires adding new options to `bm_crimson_empowerment_event.001`, updating trait loc, and adjusting decision total XP thresholds (`bm_enhance_education_decision`, `bm_blood_rune_minimum_xp`) which sum total trait XP.

---

## 4. Universal Baseline Buff Suggestions

Currently, every rank of every track gives:
- `+1 Life Expectancy`
- `+0.1 Monthly Piety`

To make the early ranks feel punchier, consider adding one of the following to the **universal baseline** per tier:
- `character_travel_safety = 0.5` (Empowered blood resists disease, exhaustion, and accidents on the road).
- `prowess = 0.5` (+5 Prowess per completed track).
