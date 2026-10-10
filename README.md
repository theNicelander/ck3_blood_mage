# Blood Mages [Nicelander]

Low-fantasy blood magic for Crusader Kings III (1.20.*).

Drain **Lifeforce** to extend lifespan, fuel rituals, steal congenital traits, forge loyal golems, and empower sworn blood knights.

Modular architecture. **Zero vanilla file overwrites**. Mid-save compatible. Full compatibility with total overhauls: *A Game of Thrones (AGOT)*, *Realms in Exile (LotR)*, *Elder Kings 2 (EK2)*, and *Princes of Darkness (PoD)*.

---

## Highlights

- **Long Life, Not True Immortality**: Live centuries, but stay mortal. Wounds, disease, murder, and exhaustion still kill.
- **Earned Genetic Power**: Acquire or upgrade Genius, Beautiful, and Herculean through Lifeforce, rituals, and sacrifice.
- **Deep Progression**: 3 lifestyle traits across 13 mastery tracks (10–100 XP).
- **AI Parity**: AI uses all mechanics, balanced by game rules.
- **Zero Vanilla Overwrites**: Drops cleanly into any load order.

---

## The Lifeforce Resource

Stored as character modifiers across three tiers:
- **Minor Lifeforce**: Minor heals, attribute channeling, knight empowerment.
- **Major Lifeforce**: Major rituals, education rank 1–4, bloodline empowerment, trait manifestation.
- **Superior Lifeforce**: Distilled essence for 5-star education, superior body runes, and blood golems.

### Sources
- **Prisoner & Courtier Drain**: Siphon captives or courtiers individually.
- **Mass Lifedrain**: Drain entire dungeons in one action.
- **Combat & Single Combat**: Harvest essence from battlefield victories and fatal duels.
- **Spiritual Manifestation**: Meditate via Learning duels to manifest or distill tiers.
- **Seek Power**: Venture into the wilderness (landed or landless adventurer) for beasts and fonts.
- **Inscribed Body Runes**: Passive annual Lifeforce roll from flesh runes.

### Mortality & Magic Toll
**Blood Mages are not immortal.** Spells cost Lifeforce and cause temporary exhaustion backlash. Empty reserves drop health, leaving mages vulnerable to illness, schemes, and battlefield death.

---

## Three Lifestyle Traits & 13 Mastery Tracks

Tracks scale from 10 to 100 XP with milestones at level 50 and 100.

### 1. Blood Mage (`lifestyle_blood_mage`)
Base trait. Grants `+2` Learning per Piety level and unlocks the Blood Magic Situation panel.
- **Ancient**: Piety gain and old-age Prowess retention.
- **Enlightenment**: Lifestyle XP gain, Martial, Prowess.
- **Bloodline**: Monthly dynasty prestige, Stewardship, house blood modifiers.
- **Benediction**: Diplomacy, prestige, general and vassal opinion.
- **Hematurgy**: Intrigue, hostile scheme resistance, trait theft proficiency.

### 2. Blood Empowerment (`lifestyle_blood_empowerment`)
Unlocked via Major Blood Magic. Every track level grants `+0.1` Health, `+2` Life Expectancy, `+1` Year Fertility, and `+1` Epidemic Resistance:
- **Dynasty**: Congenital trait inheritance chance and fertility.
- **Mastery**: Lifestyle XP multiplier, language scheme speed and capacity.
- **Presence**: Stress loss multiplier, opinion, sway schemes.
- **Prosperity**: Domain tax, construction discounts, Men-at-Arms maintenance.
- **Shadows**: Scheme secrecy, hostile scheme resistance, enemy plot disruption.

### 3. Blood Knight (`lifestyle_blood_knight`)
Martial identity for champions and commanders. Leveled via battles, duels, tournaments, and minor magic. Can cast minor magic, seek power, and heal minor ailments without full Blood Mage initiation.
- **Vanguard**: Advantage, Martial, knight effectiveness.
- **Slaughter**: Prowess, dread gain, duel lethality.
- **Resilience**: Health recovery, wound healing, fertility, epidemic resistance.

---

## Spells & Ritual Hubs

### Minor Blood Magic
- **Channel Lifeforce**: 5-year buff to any primary attribute or Prowess.
- **Attunement**: Specialize aura for annual bonuses (Ancient, Vanguard, Slaughter, Resilience).
- **Minor Restoration**: Cure wounds, scars, gout, and early illnesses on self or courtiers.

### Major Blood Magic
- **Blood Empowerment**: Progress the 5 empowerment tracks.
- **Enhance Education (1★ → 4★)**: Upgrade education rank via mental trials.
- **Inscribe Minor/Major Runes**: Carve body runes for annual Lifeforce rolls.
- **Empower Bloodline**: Lasting house-wide dynasty modifiers.
- **Manifest Perfection (Ranks 1–3)**: Awaken Quick, Comely, or Hale without donors.

### Superior Blood Magic
- **Master Education (5★)**: Attain 5-star education traits.
- **Secondary Education**: Acquire a complete second education trait.
- **Inscribe Superior Rune**: Top-tier body rune for annual Lifeforce rolls.
- **Manifest Transcendent Perfection (Ranks 4–5)**: Awaken Genius, Beautiful, or Herculean.
- **Forge Blood Golem**: Construct loyal golem champions.

### Trait Harvesting & Cleansing
- **Harvest Congenital Traits**: Steal Genius, Beautiful, Herculean, Giant, and Fecund from prisoners.
- **Purge Genetic Flaws**: Cleanse Dull, Ugly, and Delicate by draining afflicted captives.

---

## Blood Golems & Retinue

- **Blood Golems**: Constructs forged from Superior Lifeforce and piety (`bm_house_golem`). Completely loyal, sterile, no title inheritance.
- **Shaping Duels**: Spar with golems to grant Berserker, Blademaster, Athletic, and education traits.
- **Blood Knight Retinue**: Swear courtiers or knights into the order as elite commanders.

---

## Shrines & Universities

- **Domicile Blood Shrines (Tiers I–V)**: Built in Adventurer Camps (`camp`) and Noble Estates (`estate`). Grants piety, health, lifespan, genetic inheritance bonuses, and courtier protection aura (`bm_blood_shrine_aura`).
- **Blood Universities (Tiers 0–3)**: Built in Duchy Capitals. Accelerates development and cultural fascination.

---

## Blóðtrú Religion Family (`rf_blodtru`)

Three regional faiths:
- **Blóðtrú (`blodtru_faith`)**: Europe/Atlantic focus. Centers on Iceland (Reykjavik, Tálknafjörður) and European power centers.
- **Ketsudō (`ketsudo_faith`)**: East Asia focus for Japonic, Korean, and Mongolic cultures (Mount Fuji, Yamashiro, Gyeongju).
- **Xuédào (`xuedao_faith`)**: China/Himalayas focus for Chinese, Qiangic, and Tibetan cultures (Chang'an, Luoyang, Taishan).

### Religion Mechanics
- **50 Holy Sites**: Across Europe and Asia, with holder-specific buffs to prevent stat bloat.
- **Identity Doctrine (`bm_blodtru_identity_doctrine`)**: Built-in syncretism, high foreign tolerance, and opinion buffers. Peaceful coexistence without altering vanilla faiths.

---

## Situation Panel

Dedicated in-game UI hub:
- Real-time tracker for disciplines, attunement, and body runes.
- Stack counters for Minor, Major, and Superior Lifeforce.
- Collapsible rosters: Dynasty Blood Mages, active Golems, sworn Blood Retinue.
- Direct buttons for mass drain and situation decisions.

---

## Campaign Game Rules

| Game Rule | Settings | Default | Description |
| --- | --- | --- | --- |
| **Blood Mage Prevalence** | Player Only, 1 in 10,000, 1 in 1,000, Default, 1 in 100, 1 in 10, Everyone | Default | Controls AI adoption rates, birth inheritance, and yearly retention audits. |
| **Physical Appearance** | None, Blood-Red Eyes, Eyes & White Hair | Eyes & White Hair | Evolving visual portrait effects as blood magic mastery increases. |
| **Blóðtrú Religion** | Fully Enabled, Player Only, Completely Disabled | Fully Enabled | Controls whether AI characters can adopt Blóðtrú faiths. |
| **Initiation Faith Requirement** | Dedicated Cult Only, Cult or Witchcraft Accepted, Unrestricted | Dedicated Cult | Requirements for the blood cultist conversion decision. |
| **Blood Mage Lore** | Historical Campaign, A Game of Thrones | Historical | Selects historical world setup or AGOT integration flavor. |

---

## Getting Started

Become a Blood Mage or Blood Knight:
1. **Ruler Designer**: Pick either trait directly.
2. **Egill Duel**: Travel to Reykjavik or Tsushima. Fight Egill Skallagrímsson in a Learning duel (Blood Mage, costs Devotion) or Prowess duel (Blood Knight, costs Fame).
3. **Blood Cultist Decision**: Adopt a Blóðtrú faith and take the transformation rite.
4. **Learn from Another**: Request initiation from a Blood Mage friend, lover, or soulmate.
5. **Convert Witchcraft**: Abandon coven to convert witchcraft into blood magic.
6. **Siphon Prisoner**: Drain an imprisoned Blood Mage to take their power.
7. **Hereditary Birth**: Inherited by blood mage offspring based on game rule frequency.

---

## Companion Submods

- **[Blood Mages — Vanilla Religions](https://steamcommunity.com/sharedfiles/filedetails/?id=3774392244)**: Native blood cults for all 49 vanilla faiths, blending parent holy sites with Blóðtrú.
- **[Blood Mages — AGOT Religions](https://steamcommunity.com/sharedfiles/filedetails/?id=3775630683)**: Blood cults for Westerosi faiths (Seven, Old Gods, Drowned God, R'hllor, Mother Rhoyne, Valyrian).
- **[Dracul — Vampires & Blood Mages](https://steamcommunity.com/sharedfiles/filedetails/?id=3765753769)**: Interactions, mutual feeding, and vampire blood knight recruitment.

---

## Links

- **Steam Workshop**: [Blood Mages](https://steamcommunity.com/sharedfiles/filedetails/?id=3470491478)
- **GitHub**: [theNicelander/ck3_blood_mage](https://github.com/theNicelander/ck3_blood_mage)
- **Roadmap**: [Trello Board](https://trello.com/b/1qS7Y4n0/ck3-blood-mage-mod)
- **Support**: [Buy Me a Coffee](https://www.buymeacoffee.com/TheNicelander)
- **Author**: Nicelander ([TheNicelander](https://github.com/theNicelander))
