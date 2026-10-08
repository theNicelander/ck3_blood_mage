# Ideas: High-Level Thematic Features & Expansion Roadmap

Living brainstorm document outlining 10 deep, emergent, and high-flavor feature concepts for the Blood Mages mod, leveraging CK3 1.20 systems (activities, legends, travel, court positions, schemes, relics, epidemics, and adventurer camps).

---

## 1. Grand Activity: The Sanguine Conclave (The Blood Moot)

- **System Hook**: Custom Activity (`common/activities/`).
- **Concept**: A gathering of blood mages, tributary vassals, apprentices, and occult philosophers hosted in a grand castle or hidden grove.
- **Phases**:
  1. *The Grand Gathering*: Welcoming occultists, exchanging forbidden grimoires, boosting `enlightenment` and `benediction` XP.
  2. *The Communal Siphon*: Ceremonial pooling of lifeforce from condemned war captives, replenishing the host's and guests' lifeforce stores.
  3. *The Crucible of Champions*: Fatal or non-fatal single-combat duels between Crimson Warriors and apprentices for enchanted blood artifacts.
- **Risk / Reward**: Immense prestige, piety, and XP, but if discovered by orthodox faiths, can spark a Holy Inquest, Papal Excommunication, or peasant panic.

---

## 2. Dynastic Memory & Ancestral Reincarnation

- **System Hook**: Dynastic Story Cycle / Death Event Hook (`events/`, `common/on_action/character_on_actions.txt`).
- **Concept**: Ancient blood mages imprint their consciousness into the bloodline before physical death.
- **Mechanics**:
  - Aging patriarchs/matriarchs (age 60+ or terminally ill) cast a major ritual binding their soul to a chosen young scion or newborn.
  - Upon succession, the heir triggers awakening childhood narrative events:
    - Inheriting a portion of the ancestor's lifestyle perk XP, skill points, or blood magic tracks.
    - Special dialogue options reacting to old enemies and court politics (*"I remember your grandfather's treachery..."*).
- **Impact**: Alleviates succession anxiety and creates powerful emergent generational storytelling.

---

## 3. Occult Court Position: The Royal Hemomancer / Court Leech

- **System Hook**: Court Positions & Camp Officers (`common/court_positions/types/`).
- **Concept**: An appointed position for an unlanded blood mage serving a landed lord or mercenary camp captain.
- **Aptitude & Scaling**: Scales with `lifestyle_blood_mage` rank, Learning, and Prowess.
- **Tasks & Passive Benefits**:
  - *Sanguine Chirurgery*: Boosts realm courtier health, stanches battle wounds, treats plagues.
  - *Automated Siphon*: Slowly converts low-tier dungeon prisoners into Lifeforce modifiers without manual player micro.
  - *Ward Defense*: Acts as a magical bodyguard against hostile murder and abduction schemes.
  - *Occult Malice*: Can be directed to target rivals with chronic fatigue or reduced fertility.

---

## 4. Interactive Legends: The Crimson Myth & Sanguine Saints

- **System Hook**: Legends of the Dead DLC engine (`common/legends/`).
- **Concept**: Propagating tales of supernatural immortality, holy bloodlines, or dark benevolence across the map.
- **Seed Types**:
  - *The Undying Sovereign (Heroic)*: Proclaims the ruler has transcended mortal decay through divine vitae. Gives massive vassal acceptance, dread, and long-reign bonuses.
  - *The Red Redeemer (Holy - Blóðtrú)*: Legitimizes blood rituals as sacred sacraments rather than witchcraft, making neighboring faiths treat Blóðtrú as Righteous or Astray instead of Evil.
- **Rewards**: Regional buildings (*Shrines of the Bleeding Heart*), unique dynastic modifiers, and special titular kingdom titles.

---

## 5. Hostile & Personal Scheme: Sanguine Thrall

- **System Hook**: CK3 Scheme Engine (`common/schemes/`).
- **Concept**: A dark occult scheme that binds an unsuspecting foreign ruler, powerful vassal, or key councilor into supernatural subjugation.
- **Requirements**: Requires a blood sample from the target (procured via an agent bribe, poisoned wine, or battlefield duel wound).
- **Outcome**: The target gains the `trait_blood_thrall`:
  - Banned from joining factions against the caster.
  - Automatically accepts invites to join hostile schemes targeting their liege.
  - Can be blackmailed or compelled into ceding claims, gold, or arranging dynastic marriages.

---

## 6. Relic Forging: Crystalline Vitae & Soul-Bound Blades

- **System Hook**: Artifacts & Inspirations (`common/artifacts/`).
- **Concept**: Transforming the concentrated essence of executed kings, legendary knights, or master mages into physical relics.
- **Artifact Types**:
  - *The Bleeding Blade (Weapon)*: Prowess and advantage dynamically increase the more enemy combatants it slays in battle.
  - *Phial of the Primordial King (Pedestal)*: A glowing ruby phial that radiates control, popular opinion, and health to the court.
  - *Crucible Relics*: Can be consumed in emergency rituals as an instant substitute for Major Lifeforce.

---

## 7. Landless Adventurer Path: The Wandering Coven

- **System Hook**: Adventurer Contracts & Camp Purposes (`common/domiciles/`, `common/landless/contracts/`).
- **Concept**: A specialized camp purpose for landless blood mages traveling across the known world.
- **Occult Contracts**:
  - *Purge the Red Death*: Towns pay exorbitant gold for the coven to halt an ongoing plague.
  - *Curse the Usurper*: Disgruntled pretenders hire you to covertly assassinate or enfeeble an enemy duke.
  - *Beast of the Blood*: Townships hire your Crimson Warriors to slay terrifying rogue monsters or rogue mages.
- **Dynamic Persecution**: High magic usage increases local suspicion; when suspicion maxes out, an armed mob or holy order attacks the camp unless you pack up and relocate.

---

## 8. Feudal & Clan Vassal Contract: The Blood Tithe

- **System Hook**: Vassal Contract Obligations (`common/vassal_contracts/`).
- **Concept**: A customized contract clause between a Blood Mage liege and their vassals.
- **The Tradeoff**:
  - *Vassal Obligation*: Lower gold and levy duties, but the vassal regularly surrenders prisoners and recruits to the liege's court for lifeforce harvest and Crimson Warrior transformation.
  - *Liege Obligation*: The liege guarantees occult protection, granting the vassal holding epidemic resistance and dispatching Blood Golems to protect their castles during civil wars.

---

## 9. Epidemic Manipulation: Red Plagues & Hemomantic Cleansing

- **System Hook**: Epidemic & Disease System (`common/epidemics/`).
- **Concept**: Direct interaction with map plagues rather than passive suffering.
- **Abilities**:
  - *Harvest the Sick*: During severe plagues in your capital county, initiate massive harvesting rituals that yield abundant Lifeforce from dying masses.
  - *Sanguine Quarantine*: Spend lifeforce to create a magical ward around your capital county, granting +50% infection resistance.
  - *The Crimson Blight*: A covert offensive ritual that unleashes an unnatural, rapidly spreading plague inside a rival capital.

---

## 10. Mid/Late-Game Crisis: Awakening of the First Progenitor

- **System Hook**: Dynamic Narrative Mini-Crisis / Historical Incursions (`events/`, `common/story_cycles/`).
- **Concept**: An ancient, immortal progenitor of blood magic stirs beneath an ancient tomb after enough blood magic has been cast across Europe.
- **Crisis Mechanics**:
  - An ancient ruler awakens with forgotten tier-5 blood spells, an army of giant Blood Golems, and fanatical Blóðtrú zealots.
  - Spreads rapidly across a specific region, demanding all mortal rulers submit.
- **Player Divergence**:
  - *Serve the Master*: Bend the knee to become the Progenitor's Grand Marshal, conquering realms under an occult empire.
  - *Slay the God*: Lead a grand alliance of mortal kings and rebel blood mages to defeat the Progenitor, slay them in single combat, and harvest their Primordial Heart.
