# Ideas: Crimson Warrior Evolving Trait (Combat & Duel Progression)

Proposal to replace the static character modifiers `lifeforce_modifier_crimson_warrior` and `lifeforce_modifier_crimson_champion` with an evolving lifestyle trait with tracks: **`lifestyle_crimson_warrior`**.

Infused retainers, knights, commanders, and blood mages gain XP dynamically by fighting in **army battles** and surviving **single combat duels**.

---

## 1. Core Mechanics & Concept

- **Identity**: `lifestyle_crimson_warrior`
- **Acquisition**:
  - Granted to knights/courtiers via character interactions:
    - `grant_crimson_warrior_interaction` (consumes Minor Lifeforce, grants base trait at 0 XP).
    - `grant_crimson_champion_interaction` (consumes Major Lifeforce, grants base trait + 30 XP in chosen track, or unlocks higher track cap).
  - Can also be self-granted by a blood mage who fights on the front lines.
- **Physical Toll (Baseline Penalty)**:
  - Base trait retains the somatic strain of blood magic: `-0.2` Health, `-2` Life Expectancy.
  - As the warrior levels up through combat, their tracks can overcome this decay or turn it into overwhelming lethality.

---

## 2. Progression & XP Triggers (Battles & Duels)

XP is awarded automatically through vanilla CK3 hooks without manual player micro:

### A. Army Combat Hooks (`common/on_action/combat_on_actions.txt`)
- **Battle Victory (`on_combat_end_winner`)**:
  - All knights (`every_side_knight`) with `lifestyle_crimson_warrior`: **+5 XP** in their active/highest track.
  - Side commander (`every_side_commander`) with the trait: **+6 XP**.
- **Battle Defeat (`on_combat_end_loser`)**:
  - Surviving knights/commanders with the trait: **+2 XP** (trial by blood and survival).

### B. Single Combat & Duel Hooks (`single_combat_events.txt` / SCE)
- **Duel Victory (`single_combat.0041`)**:
  - Victor with `lifestyle_crimson_warrior`: **+8 XP** (or **+12 XP** if lethal execution).
- **Duel Loss / Survival (`single_combat.0031`)**:
  - Loser surviving non-fatal combat: **+3 XP**.
- **Tournament Contests (Hastiludes / Melee)**:
  - Participating in martial tournament contests awards minor XP (+3 XP per contest won).

---

## 3. Proposed Tracks (4 Tracks, 5 Benefit Ideas per Track)

Each track has 5 or 10 tiers (max 100 XP). Benefits shown are **per rank**:

| Track | Focus | Option 1 | Option 2 | Option 3 | Option 4 | Option 5 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **`slaughter`** | **Single Combat & Prowess** | `prowess = 1.5`<br>*(+1.5 Prowess per rank)* | `wound_recovery_mult = 0.05`<br>*(+5% Wound Healing Speed)* | `prowess_per_prestige_level = 0.2`<br>*(Fame converts to Prowess)* | `advantage = 1`<br>*(+1 Duel / Single Combat Advantage)* | `disease_resistance = 0.08`<br>*(Resists infected battle wounds)* |
| **`vanguard`** | **Army Knight & Unit Leadership** | `knight_effectiveness_mult = 0.08`<br>*(+8% Knight Effectiveness)* | `enemy_fatal_casualties_mult = 0.05`<br>*(+5% Fatalities Inflicted)* | `maa_pursuit_mult = 0.06`<br>*(+6% Pursuit Casualties)* | `commander_military_attrition_mult = -0.05`<br>*(-5% Supply Attrition)* | `character_travel_speed = 2`<br>*(+2 Travel Speed as Bodyguard)* |
| **`blood_frenzy`** | **Dread & Psychological Terror** | `dread_baseline_add = 4`<br>*(+4 Dread Baseline)* | `enemy_hostile_scheme_success_chance_add = -4`<br>*(-4% Enemy Assassin Success)* | `stress_gain_mult = -0.05`<br>*(-5% Stress in Warfare)* | `maa_damage_mult = 0.03`<br>*(+3% Commanded Unit Damage)* | `general_opinion = -1`<br>`same_opinion = 8`<br>*(Feared by mortals, adored by cult)* |
| **`resilience`** | **Overcoming Biological Decay** | `health = 0.08`<br>*(Counteracts health malus)* | `life_expectancy = 1`<br>*(Reclaims lost lifespan)* | `character_travel_safety = 3`<br>*(+3 Travel Safety for party)* | `fertility = 0.02`<br>*(+2% Fertility)* | `stress_loss_mult = 0.06`<br>*(+6% Stress Recovery)* |

---

## 4. Integration with Mod Systems

1. **Roster Tracking**:
   - The Blood Magic Story Panel (`bm_story_cycles.txt` / `bm_refresh_blood_magic_rosters_effect`) lists Crimson Warriors in the retinue roster.
   - It can display their track level (e.g., *"Sir Guy — Rank 4 Slaughter, Rank 2 Vanguard"*).
2. **Landless Adventurer Synergy**:
   - Landless blood mage mercenary captains can infuse their followers into an elite band of evolving super-soldiers that grow stronger with every mercenary contract battle.
3. **Player Progression**:
   - If the player is a martial/warrior blood mage, they can also gain the trait and progress it alongside their normal blood magic tracks.
