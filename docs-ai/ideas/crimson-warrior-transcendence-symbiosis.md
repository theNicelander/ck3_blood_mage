# Architecture & Design: The Symbiotic Model (Crimson Transcendence & Crimson Warrior)

Living design document evaluating whether `lifestyle_crimson_warrior` should be merged into `lifestyle_crimson_transcendence` or maintained as a separate, interconnected trait.

---

## 1. Executive Summary & Recommendation

**Verdict**: Maintain **`lifestyle_crimson_warrior`** as its own dedicated trait, while weaving an explicit **Conduit / War-Bond track** into **`lifestyle_crimson_transcendence`**.

Merging both into a single trait creates severe CK3 engine friction, UI clutter for mortal knights, and conflicting progression loops (ritual casting vs. battlefield bloodshed). A **symbiotic architecture** cleanly distinguishes between the **Arcane Creator/Conduit** (the Mage) and the **Living Weapon/Vessel** (the Knight), while still permitting a martial Blood Mage to hold both traits simultaneously.

---

## 2. Structural Comparison: Unified Trait vs. Symbiotic Model

```
                     ┌─────────────────────────────────────────────────────────┐
                     │          BLOOD MAGE (The Conduit / Master)              │
                     │          Trait: lifestyle_crimson_transcendence         │
                     │                                                         │
                     │  Progression: Piety & Lifeforce Rituals                 │
                     │  Tracks:                                                │
                     │  - Vitality (Somatic Fortification)                     │
                     │  - Wayfarer (Travel & Survival)                         │
                     │  - Transmutation (Alchemy & Body Control)               │
                     │  - Mesmerism (Personal Schemes & Influence)             │
                     │  - Blood Resonance / Command (Symbiotic Conduit) ───────┐
                     └─────────────────────────────────────────────────────────│─┘
                                                                               │
                                                                 Bestows &     │ Telepathic /
                                                                 Stabilizes    │ Vitae Bond
                                                                               │
                                                                               ▼
                     ┌─────────────────────────────────────────────────────────┐
                     │          KNIGHT / CHAMPION (The Living Weapon)          │
                     │          Trait: lifestyle_crimson_warrior               │
                     │                                                         │
                     │  Progression: Battles, Duels, Slaying Champions         │
                     │  Tracks:                                                │
                     │  - Juggernaut (Physical Might & Wound Negation)         │
                     │  - Bloodhound (Pursuit, Scent & Camp Reconnaissance)    │
                     │  - Red Banshee (Dread, Morale Shock & Brutality)        │
                     └─────────────────────────────────────────────────────────┘
```

| Evaluation Dimension | Option A: Merged into Transcendence | Option B: Symbiotic Model (Recommended) |
| :--- | :--- | :--- |
| **Knights' Character Sheet** | **Polluted**: Mortal knights display wizardly/occult lifestyle tracks they cannot use or understand. | **Clean**: Knights display a razor-focused, badass martial combat trait with 3 martial tracks. |
| **Progression Mechanics** | **Clashing**: Blends ritual spell decision casting with battlefield combat triggers into one messy script. | **Cohesive**: Transcendence levels via Major Rituals; Crimson Warrior levels dynamically via kills, duels, and won battles. |
| **AI Performance & Footprint** | Heavy multi-track lifestyle checks evaluated across entire knight retinues. | Lightweight, combat-focused on-action triggers firing only on combat end and single-combat resolution. |
| **Warlord Mage Fantasy** | Forced to pick between being a mage or a fighter. | **Best of Both**: A front-line battle mage can hold **both** traits, evolving their body through rituals and their sword-arm through battle. |
| **Thematic Lore** | Muddled boundary between the spellcaster and the thrall. | Evocative dynamic of **The Alchemist and their Transmuted Champions**. |

---

## 3. The Symbiotic Weave: How Transcendence Empowers the Warrior

Rather than merging the traits, `lifestyle_crimson_transcendence` features a dedicated conduit track: **`blood_resonance`** (or *Sanguine Command*).

### Track: `blood_resonance` (Transcendence Mage Track)
A Mage who invests in this track directly enhances all Crimson Warriors sworn to them:

| Tier / Rank | Arcane Mechanism | Flavor & Gameplay Effect |
| :---: | :--- | :--- |
| **Rank 1–2** | *Vessel Stabilization* | Reduces the health penalty and life expectancy decay of all sworn Crimson Warriors by 50%. |
| **Rank 3–4** | *Sanguine Network* | +10% Knight Effectiveness per rank; Blood Mage gains notification when an infused knight wins a duel. |
| **Rank 5** *(Milestone)* | **The Siphon Harvest** | **Synergy Hook**: Whenever a sworn Crimson Warrior kills an enemy knight in battle or executes a duel opponent, the Blood Mage liege receives a burst of **Lifeforce** and **Piety**. |
| **Rank 7–8** | *Crimson Tether* | Sworn Crimson Warriors in the ruler's army gain +2 Commander Advantage and immunity to capture in battle. |
| **Rank 10** *(Mastery)* | **Defy the Grave** | If a sworn Crimson Champion suffers fatal battle injuries while in the same army as the Mage, an emergency event fires: the Mage can spend Lifeforce to stitch their mortal coil back together, preventing death. |

---

## 4. The Evolving Warrior Trait: `lifestyle_crimson_warrior`

### Core Characteristics
- **Audience**: Granted to knights, commanders, camp bodyguards, or self-applied by martial blood mages.
- **Progression Engine**:
  - `on_combat_end_winner`: +5 XP in active track.
  - Slaying an enemy knight in combat: +4 XP.
  - Winning a Single Combat Duel (`single_combat.0041`): +8 XP (ludicrous +12 XP if lethal execution).
  - Melee/Hastilude tournament victories: +3 XP.
- **Baseline Strain**: Starts with `-0.2 Health`, `-2 Life Expectancy`, which is mitigated by combat progression or the Mage's `blood_resonance`.

### The Three Combat Paths (3 Tracks, Max 100 XP)

```
                            [ lifestyle_crimson_warrior ]
                                         │
                 ┌───────────────────────┼───────────────────────┐
                 ▼                       ▼                       ▼
            JUGGERNAUT               BLOODHOUND              RED BANSHEE
        (Unbroken Flesh)       (The Crimson Tracker)      (Sovereign Terror)
```

#### 1. Track: `juggernaut` (The Unbroken Flesh)
- **Concept**: Bones calcify into iron, severed arteries close instantly, pain is converted into adrenaline.
- **Modifiers per Rank**:
  - `prowess = 1.5`
  - `wound_recovery_mult = 0.05`
  - `negate_health_penalty_add = 0.05`
  - `heavy_infantry_damage_mult = 0.04`
- **Milestone (Rank 5)**: *Ignore Mortal Ruin* — In single combat, cannot be instantly slain by a single critical strike; always delivers a retaliatory blow.

#### 2. Track: `bloodhound` (The Crimson Tracker)
- **Concept**: Heightened animalistic senses resonating with the scent of open wounds. Ideal for light cavalry, skirmishers, and adventurer camp scouts.
- **Modifiers per Rank**:
  - `maa_pursuit_mult = 0.08`
  - `enemy_fatal_casualties_mult = 0.04`
  - `character_travel_speed = 2`
  - `character_travel_safety = 1.5`
- **Milestone (Rank 5)**: *Scent of the Craven* — Armies commanded or joined by this warrior suffer -20% enemy retreat survival; routed enemies are systematically hunted down.

#### 3. Track: `red_banshee` (The Dread Sovereign's Enforcer)
- **Concept**: The psychological horror of facing an unholy, blood-soaked monstrosity. Levies break before the blade even makes contact.
- **Modifiers per Rank**:
  - `knight_effectiveness_mult = 0.08`
  - `dread_baseline_add = 4`
  - `advantage = 1`
  - `stress_gain_mult = -0.04`
- **Milestone (Rank 5)**: *Blood-Chilled Panic* — In battle, triggers unique combat events causing opposing peasant levies and lower-tier knights to break morale prematurely.

---

## 5. Narrative Hooks: The Hunger & The Red Thrall

To anchor the mechanics in dark medieval tragedy rather than pure fantasy power-creep:

1. **The Crimson Thirst**:
   - High-tier Crimson Warriors (Rank 6+) require regular warfare. If they go 3+ years without participating in a war, duel, or public execution, they gain the modifier **`crimson_withdrawal`** (+Stress, reduced Prowess, erratic AI behavior).
2. **Absolute Devotion / The Living Shield**:
   - Crimson Warriors develop a supernatural bond with the Mage who awakened them.
   - If their Mage liege is targeted by an assassination scheme, a high-rank Crimson Warrior has a high chance to discover the attempt and intercept the dagger/poison, sacrificing themselves for their master.
3. **Rogue Crimson Warriors**:
   - If the patron Blood Mage dies without an heir or coven, high-ranking Crimson Warriors may refuse to serve mundane lords, breaking away to form terrifying rogue sellsword bands or wilderness legends.
