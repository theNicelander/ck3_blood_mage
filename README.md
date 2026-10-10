# Blood Mages [Nicelander]

> Low-fantasy blood magic integrated seamlessly into Crusader Kings III (1.20.*).

Blood Mages drain **Lifeforce** from others to extend their lifespan, fuel supernatural rituals, absorb congenital traits, shape artificial constructs, and empower sworn knights into lethal combatants.

The mod is built with a strictly modular architecture: **zero vanilla file overwrites**, full save-game compatibility, and seamless interoperability with total overhauls such as *A Game of Thrones (AGOT)*, *Realms in Exile (LotR)*, *Elder Kings 2 (EK2)*, and *Princes of Darkness (PoD)*.

---

## This Mod Is For You If:

- You love playing a **single, long-lived character** without being completely immortal.
- You want to acquire and enhance **positive physical and mental traits** (Genius, Beautiful, Herculean) through earned gameplay, rituals, and sacrifice.
- You enjoy **deep progression**: 3 distinct lifestyle traits across 13 specialized mastery tracks.
- You want **AI characters** to have access to the same mechanics and decisions as players, balanced via comprehensive campaign game rules.
- You want **maximum mod compatibility** with zero core game file conflicts.

---

## The Lifeforce Resource

Lifeforce is the lifeblood of blood magic. It is stored as physical character modifiers and exists in three progressive tiers:

- **Minor Lifeforce**: Used for minor restorative magic, attribute channeling, and knight empowerments.
- **Major Lifeforce**: Fuel for major rituals, education enhancements, bloodline empowerment, and trait manifestation.
- **Superior Lifeforce**: Distilled, high-potency essence required for legendary rites, 5-star education mastery, superior body runes, and blood golem forging.

### Sources of Lifeforce
- **Harvesting Captives & Courtiers**: Violently siphon prisoners in your dungeons or willing/unwilling courtiers.
- **Mass Prisoner Lifedrain**: Drain multiple dungeon captives at once through a dedicated management action.
- **Combat & Fatal Duels**: Slay rivals in lethal single combat or harvest essence from victorious battlefield clashes.
- **Spiritual Manifestation**: Meditate through Learning duels to manifest Minor, Major, or distill Superior Lifeforce from your existing reserves.
- **Wilderness Encounters**: Venture forth via *Seek Power* (landed rulers and landless adventurers) to hunt beasts and tap ancient fonts.
- **Inscribed Body Runes**: Passively regenerate Lifeforce each year through magical runes carved into your flesh.

### Magic Toll & Mortality
**Blood Mages are NOT immortal.** Casting spells drains Lifeforce reserves and inflicts temporary exhaustion backlash. If your Lifeforce runs out or you overexert yourself, your health deteriorates, leaving you vulnerable to disease, assassination, or fatal wounds in battle.

---

## Three Lifestyle Traits & 13 Mastery Tracks

Progression is divided across three dedicated lifestyle traits featuring 13 progressive tracks (each scaling from 10 to 100 XP, with milestones at level 50 and 100):

### 1. Blood Mage (`lifestyle_blood_mage`)
The foundational identity for all blood mages. Grants `+2` Learning per Piety level and unlocks the Blood Magic Situation panel.
- **Ancient**: Passive survival over centuries. Yields monthly piety, piety multipliers, and locks Prowess against deterioration from old age.
- **Enlightenment**: Self-mastery through channeling spells. Boosts lifestyle experience gain, Martial, and Prowess.
- **Bloodline**: Dynastic preservation. Enhances monthly dynasty prestige, Stewardship, and house blood modifiers.
- **Benediction**: Healing and bestowing power upon others. Boosts general opinion, vassal opinion, Diplomacy, and prestige.
- **Hematurgy**: Siphoning lifeforce and harvesting traits. Grants hostile scheme resistance, Intrigue, and trait-theft proficiency.

### 2. Blood Empowerment (`lifestyle_blood_empowerment`)
Secondary advancement trait unlocked through Major Blood Magic. Every level across all tracks includes universal vitality bonuses (`+0.1` Health, `+2` Life Expectancy, `+1` Year Fertility, `+1` Epidemic Resistance):
- **Dynasty**: Positive congenital trait inheritance chance, inactive trait inheritance, and fertility.
- **Mastery**: Lifestyle experience gain multiplier, language scheme speed, and additional concurrent language schemes.
- **Presence**: Stress loss multiplier, vassal and general opinion, and sway scheme effectiveness.
- **Prosperity**: Monthly domain income, holding construction costs, camp/domicile build discounts, and Men-at-Arms maintenance reductions.
- **Shadows**: Hostile scheme resistance, owned scheme secrecy, and reducing enemy plot success chances.

### 3. Blood Knight (`lifestyle_blood_knight`)
A martial combat lifestyle trait for empowered champions, commanders, and knights. Leveled through battlefield victories, single combat duels, tournaments, and minor magic:
- **Vanguard**: Army command advantage, martial stats, and knight effectiveness.
- **Slaughter**: Combat prowess, dread gain, and dueling lethality.
- **Resilience**: Natural health recovery, wound healing, fertility, and epidemic resistance.
- *Blood Knights can wield Minor Blood Magic, seek power in the wilderness, and heal minor ailments without needing full Blood Mage initiation.*

---

## Spellcraft & Ritual Hubs

Rituals and decisions are organized into clean ritual hubs:

### Minor Blood Magic
- **Channel Minor Lifeforce**: Grant 5-year attribute enhancements to Martial, Prowess, Stewardship, Diplomacy, Intrigue, or Learning.
- **Lifeforce Attunement**: Specialize your aura for passive yearly bonuses (Ancient, Vanguard, Slaughter, Resilience).
- **Minor Restorative Magic**: Cure minor wounds, scars, gout, and early illnesses on yourself or courtiers.

### Major Blood Magic
- **Blood Empowerment**: Channel Major Lifeforce to progress along the 5 empowerment tracks.
- **Enhance Education (1★ → 4★)**: Undertake mental trials to elevate education traits up to rank 4.
- **Inscribe Minor & Major Blood Runes**: Carve mystical runes onto your body for passive yearly Lifeforce rolls.
- **Empower Bloodline**: Bestow lasting house-wide bloodline modifiers to strengthen your dynasty.
- **Manifest Perfection (Ranks 1–3)**: Spiritually awaken positive congenital traits (Quick, Comely, Hale) without needing donor prisoners.

### Superior Blood Magic
- **Master Education (5★)**: Push mental discipline to its absolute pinnacle, achieving legendary 5-star education traits.
- **Embrace Secondary Education**: Gain a complete second education trait to become a true polymath.
- **Inscribe Superior Blood Rune**: Carve the highest tier body rune for substantial passive Lifeforce generation.
- **Manifest Transcendent Perfection (Ranks 4–5)**: Awaken the ultimate genetic gifts (Genius, Beautiful, Herculean).
- **Forge Blood Golem**: Construct immortal artificial construct champions.

### Trait Harvesting & Reversal
- **Drain Congenital Traits**: Steal positive congenital traits (Genius, Beautiful, Herculean, Giant, Fecund) from captive prisoners.
- **Purge Genetic Flaws**: Cleanse your own negative congenital traits (Dull, Ugly, Delicate) by draining afflicted captives.

---

## Blood Golems & Retinue

- **Blood Golems**: Artificial constructs forged from Superior Lifeforce and piety. Bound to your court in the unique construct house `bm_house_golem`. They are completely loyal, sterile, and barred from title inheritance.
- **Shaping Duels**: Undertake ritual shaping duels to mold your golems, granting them martial traits such as Berserker, Blademaster, Athletic, and specialized education.
- **Blood Knights Retinue**: Swear courtiers or knights into the Blood Knight order to serve as deadly commanders and champions on the battlefield.

---

## Domicile Shrines & Blood Universities

- **Domicile Blood Shrines (Tiers I–V)**: Construct 5-tier Blood Shrines in Adventurer Camps (`camp`) and Noble Estates (`estate`). Shrines provide scaling piety, health, lifespan, and positive genetic inheritance chances to the ruler, while radiating a protective aura (`bm_blood_shrine_aura`) to all courtiers and camp followers.
- **Blood Universities (Tiers 0–3)**: Construct specialized magical universities in Duchy Capital holdings, driving cultural fascination and county development.

---

## Blóðtrú Religion Family & Faiths

Blood Mages can embrace their own dedicated religious family, **Blóðtrú** (`rf_blodtru`), featuring three cultural faiths:
- **Blóðtrú Faith (`blodtru_faith`)**: European and Atlantic focus, centered on Iceland (Reykjavik, Tálknafjörður) and major European power centers.
- **Ketsudō Faith (`ketsudo_faith`)**: East Asian focus for Japonic, Korean, and Mongolic cultures (Mount Fuji, Yamashiro, Gyeongju).
- **Xuédào Faith (`xuedao_faith`)**: Central Plains and Himalayan focus for Chinese, Qiangic, and Tibetan cultures (Chang'an, Luoyang, Taishan).

### Features
- **Nearly 50 Holy Sites**: Spanning Europe and Asia, balanced with individual county holder bonuses to prevent overwhelming stat inflation.
- **Identity Doctrine**: Features the hidden `bm_blodtru_identity_doctrine` with pluralistic integration, high foreign tolerance, and opinion buffering, allowing peaceful coexistence with outside faiths without overwriting vanilla religions.

---

## Blood Magic Situation Panel

The custom **Blood Magic Situation Panel** provides a unified in-game management interface:
- Live tracking of all 5 core disciplines, current attunement, and inscribed runes.
- Exact counts of Minor, Major, and Superior Lifeforce modifier stacks.
- Interactive, collapsible rosters displaying your living **Dynasty Blood Mages**, active **Blood Golems**, and sworn **Blood Retinue**.
- Quick access to situation decisions and mass management actions.

---

## Campaign Game Rules

Fully customize your campaign through dedicated game rules:

| Game Rule | Settings | Default | Description |
| --- | --- | --- | --- |
| **Blood Mage Prevalence** | Player Only, 1 in 10,000, 1 in 1,000, Default, 1 in 100, 1 in 10, Everyone | Default | Controls AI adoption rates, birth inheritance, and yearly retention audits. |
| **Physical Appearance** | None, Blood-Red Eyes, Eyes & White Hair | Eyes & White Hair | Evolving visual portrait effects as blood magic mastery increases. |
| **Blóðtrú Religion** | Fully Enabled, Player Only, Completely Disabled | Fully Enabled | Controls whether AI characters can adopt Blóðtrú faiths. |
| **Initiation Faith Requirement** | Dedicated Cult Only, Cult or Witchcraft Accepted, Unrestricted | Dedicated Cult | Requirements for the blood cultist conversion decision. |
| **Blood Mage Lore** | Historical Campaign, A Game of Thrones | Historical | Selects historical world setup or AGOT integration flavor. |

---

## Getting Started

You can become a Blood Mage through multiple paths:
1. **Character Creator**: Select the Blood Mage trait directly in the Ruler Designer.
2. **Ritual Initiation**: Travel to Reykjavik or Tsushima to undertake the ancient geyser duel against the legendary Egill Skallagrímsson.
3. **Blood Cultist Decision**: Adopt a Blóðtrú faith and perform the transformation rite.
4. **Learn from Another**: Ask a friend, lover, or soulmate who is a Blood Mage to grant you the power.
5. **Witch Conversion**: Renounce your witch coven and convert your witchcraft into blood magic.
6. **Siphon a Prisoner**: Drain the essence of an imprisoned Blood Mage to take their power for yourself.
7. **Hereditary Birth**: Children of blood mages have a chance to inherit the trait naturally.

---

## Optional Companion Submods

- **[Blood Mages — Vanilla Religions](https://steamcommunity.com/sharedfiles/filedetails/?id=3774392244)**: Adds native blood cults to all 49 vanilla religions (including the Cult of the Crimson Ka), blending parent religion holy sites with the Blóðtrú network.
- **[Blood Mages — AGOT Religions](https://steamcommunity.com/sharedfiles/filedetails/?id=3775630683)**: Adapts the cult database for Westerosi faiths (Faith of the Seven, Old Gods, Drowned God, R'hllor, Mother Rhoyne, Valyrian).
- **[Dracul — Vampires & Blood Mages](https://steamcommunity.com/sharedfiles/filedetails/?id=3765753769)**: Crossover mod allowing vampires and blood mages to interact, prey on each other, and recruit vampire blood knights.

---

## Credits & Links

- **Creator & Lead Developer**: Nicelander ([TheNicelander](https://github.com/theNicelander))
- **Steam Workshop**: [Blood Mages on Steam Workshop](https://steamcommunity.com/sharedfiles/filedetails/?id=3470491478)
- **GitHub Repository**: [theNicelander/ck3_blood_mage](https://github.com/theNicelander/ck3_blood_mage)
- **Development Roadmap & Trello**: [Blood Mages Trello Board](https://trello.com/b/1qS7Y4n0/ck3-blood-mage-mod)
- **Support the Mod**: [Buy Me a Coffee](https://www.buymeacoffee.com/TheNicelander)
