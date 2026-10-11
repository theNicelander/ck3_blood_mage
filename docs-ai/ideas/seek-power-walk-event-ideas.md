# Ideas: Expanding "Take a Walk" & "Seek Power" Events

Living proposal for expanding, restructuring, and adding narrative depth to the **Seek Power / Take a Walk** blood mage decision chain.

Originally starting as "Take a Stroll / Walk Through Town" (`bm_stroll_through_town`) before being repurposed into "Seek Power in Nature's Domain" (`bm_seek_power_decision.txt` / `bm_seek_power_events.txt`), the current mechanic is a 2-year cooldown decision with a single prowess roll that splits into 3 outcomes:
1. `seek_power.002`: Slaying a wild stag for minor lifeforce.
2. `seek_power.003`: Meeting a lost traveler (drain, trait drain, recruit, or ignore).
3. `seek_power.004`: Finding the ancient Bleeding Tree for major lifeforce.

This document collects expansion paths and event ideas inspired by vanilla CK3 event mechanics (hunt activities, travel danger, stress coping, lifestyle events, and witchcraft/mysticism).

---

## 1. Engine & Implementation Foundations

### Current vs. Proposed Architecture
- **Current Flow**:
  Decision -> `seek_power.001` (prowess duel) -> Single immediate resolution (`.002`, `.003`, or `.004`).
- **Proposed Flow Options**:
  - **Option A: Dual Environment Decision**: Keep the quick entry point, but let the player choose *where* to wander:
    - *The Shadowed Settlement* (Urban / Castle Town stroll: alleyways, crypts, markets).
    - *The Untamed Wilds* (Wilderness / Forest expedition: beasts, tainted groves, hermits).
  - **Option B: Multi-Stage Scouting Chain**: The first event presents sensory cues (scent of blood, sound of steel, mystical hum), and the player's choice directs the resulting encounter and skill checks.
  - **Option C: Expanded Event Pool**: Keep the wilderness framework, but expand the outcome pool from 3 to 8+ diverse encounters weighted by location, terrain, character traits, and blood mage track levels.

---

## 2. Direction 1: The Midnight Prowl (Urban / Castle Town Strolls)

*Inspired by vanilla stress relief walks, murder schemes, and intrigue/city travel events.*

For landless adventurers in settlements or feudal rulers dwelling in castles, the city streets at night offer very different opportunities than the deep woods.

### Event Idea 1.1: The Alchemist's Back-Alley Lab
- **Premise**: Drawn down a foul-smelling alleyway by the scent of brimstone and copper, the mage finds an apothecary or rogue alchemist working late on forbidden distillations.
- **Skill Checks / Tracks**: Learning (`enlightenment`) or Intrigue (`ancient`).
- **Options**:
  - *Seize their research and apparatus*: Gain `enlightenment` or `ancient` track XP, gain gold or alchemical artifact, but anger the local merchants/guilds.
  - *Harvest the practitioner*: Drain the alchemist for lifeforce; their concoctions grant a temporary stat buff or disease resistance.
  - *Sponsor their workshop*: Spend gold to gain a county modifier boosting development/physician opinion, or recruit them as a court physician/mystic.

### Event Idea 1.2: The Drunken Watchman / Carousing Noble
- **Premise**: An isolated noble carouser or town guardsman is stumbling through the dark streets alone after curfew.
- **Skill Checks / Tracks**: Intrigue vs. target's Prowess/Perception.
- **Options**:
  - *A clean, fatal harvest*: Drain them completely. Gain major lifeforce, but risk raising county suspicion/unrest if rolled poorly.
  - *Surgical phlebotomy (Subtle feeding)*: Take only a measure of blood while clouding their mind (`hematurgy`). Gain minor lifeforce with zero chance of exposure; leave the victim believing they simply drank too much.
  - *Frame a rival*: Drain the victim and plant evidence implicating a rival courtier or faction member.

### Event Idea 1.3: The Catacombs of Saint Sanguis
- **Premise**: Sneaking into the local churchyard or crypts beneath the city walls.
- **Skill Checks / Tracks**: Learning / Intrigue.
- **Options**:
  - *Disturb the fresh barrows*: Harvest lingering lifeforce from recently deceased bodies (no murder needed, but high stress for zealous/compassionate characters, risk of discovery by clergy).
  - *Desecrate a holy relic*: Drain sanctified relic blood preserved in a shrine; high piety penalty or heresy secret, but massive `ancient` XP or major lifeforce.
  - *Commune with ancient bones*: Meditate in the crypts to calm the mind (significant stress reduction).

---

## 3. Direction 2: Expanding the Wilderness Encounters

*Inspired by vanilla hunt events, travel danger, and wild fauna interactions.*

Expands the current wilderness pool beyond just the Stag, Traveler, and Bleeding Tree.

### Event Idea 2.1: The Alpha Predator's Kill
- **Premise**: You come across an apex predator (a great wolf, bear, or big cat) feeding on fresh game in a clearing.
- **Skill Checks / Tracks**: Prowess / Hematurgy.
- **Options**:
  - *Boil the beast's blood*: Use raw hemomancy to strike down both predator and prey simultaneously. Duel check rewarding major lifeforce and `hematurgy` XP.
  - *Subjugate and bind*: Infuse the predator with a droplet of your own empowered lifeforce to tame it. Spend minor lifeforce to gain a hunting pet / court hound modifier or combat prowess modifier.
  - *Yield the kill and observe*: Study the predator's natural vitality from afar (Stress reduction, minor Learning XP).

### Event Idea 2.2: The Isolated Hermit of the Outskirts
- **Premise**: Deep in the forest, you stumble across a remote hut inhabited by an old hermit—either a hedge witch, a retired soldier, or an exiled mystic.
- **Skill Checks / Tracks**: Diplomacy / Learning.
- **Options**:
  - *Trade secrets and lore*: Exchange occult knowledge. Gain `enlightenment` track XP and friendly opinion.
  - *Consume their gathered wisdom*: Harvest the hermit entirely. Gain lifeforce and track XP, but receive Dread and potential Stress.
  - *Offer them sanctuary*: Invite the hermit to court as an arcane scholar or herbalist.

### Event Idea 2.3: The Blood-Tainted Spring
- **Premise**: In a secluded cavern or misty glen, water bubbles up thick and dark crimson from mineral veins or forgotten battlefields.
- **Skill Checks / Tracks**: Learning / Health check.
- **Options**:
  - *Drink deeply of the spring*: Risky gambit—chance of temporary illness vs. granting high lifeforce or the `ancient_attuned` modifier.
  - *Bottle the tainted waters*: Collect vials for future rituals (gain a minor trinket artifact or consumable character modifier).
  - *Cleanse / Consecrate the ground*: Cast a ritual to channel the earth's energy into your demesne (increases county control or popular opinion).

### Event Idea 2.4: The Bandit Ambush Turned Prey
- **Premise**: A group of desperate outlaws ambushes you, unaware of what you truly are.
- **Skill Checks / Tracks**: Prowess / Dread check.
- **Options**:
  - *Unleash crimson horror*: Slit your palm and slaughter them with blood spikes. Major Dread gain, `crimson_warrior` or `prowess` XP, harvest multiple minor lifeforce modifiers.
  - *Break their minds and recruit*: Terrify the survivors into serving you as criminal levies or retinue recruits.
  - *Merciful escape*: Use mist/shadow blood trickery to vanish, leaving them baffled.

---

## 4. Direction 3: Multi-Stage Choice Chain (The Scent of Life)

Instead of jumping straight from decision to a random event, turn the stroll into an atmospheric 2-stage scouting trek:

### Stage 1: Reading the Leylines (`seek_power.010`)
*Description*: You close your eyes, extend your senses into the surrounding lands, and taste the currents of life pulsing through the air. Three distinct resonances call out to you.
- **Option A (The Scent of Iron & Conflict)**: "I sense steel, sweat, and racing pulses."
  - Leads to encounters with patrols, wounded knights, bandit camps, or dueling beasts. Tests **Prowess** and **Intrigue**.
- **Option B (The Hum of Sanctity & Lore)**: "I feel an unnatural convergence of spirit and prayer."
  - Leads to shrines, relics, hermits, pilgrim caravans, or hidden cult gatherings. Tests **Learning** and **Diplomacy**.
- **Option C (The Cold Stillness of the Ancient)**: "I feel the quiet chill of ancient blood and decay."
  - Leads to ruins, bleeding trees, crypts, barrows, and prehistoric altars. Tests **Learning** and **Ancient** track level.

### Stage 2: Climax & Resolution
Each path branches into 2-3 specific narrative resolutions with distinct trade-offs between Lifeforce, Stress, Trait XP, and County Modifiers.

---

## 5. Direction 4: Companion & Blood Golem Field Tests

If the character has specific conditions active:

### 5.1 With a Blood Golem (`has_character_modifier = bm_blood_golem_*`)
- **Field Trial**: Taking your blood golem out on the prowl to test its obedience and lethal potential.
- **Encounters**:
  - *The Golem Rampage*: The construct catches the scent of blood from a nearby cottage or herd and strains against your mental command (Learning/Prowess contest to master it or let it feed).
  - *Excavation*: The golem tears through bedrock or tangled roots, unearthing an ancient blood rune or buried reliquary.

### 5.2 With Crimson Retinue / Disciples
- Taking an apprentice or Crimson Warrior squire on the hunt to teach them how to feed or how to siphon essence without losing their mind to the blood-thirst.
- Gives XP to both master and student.

---

## 6. Summary Comparison Matrix

| Idea Concept | Primary Skills | Key Rewards | Risk / Downsides |
| :--- | :--- | :--- | :--- |
| **Urban Midnight Prowl** | Intrigue, Learning | Alchemical gold, secret hooks, subtle lifeforce | Crime exposure, clergy wrath, local unrest |
| **Wilderness Expansion** | Prowess, Learning | Major lifeforce, beast familiars, rare traits | Physical injury, disease, lost travel safety |
| **The Scent of Life (2-Stage)** | Player Choice | Tailored rewards according to chosen focus | Longer chain, higher variance |
| **Golem Field Trial** | Learning, Prowess | Golem combat buffs, unearthed runes | Construct disobedience, terrorizing locals |
