# Blood Mages — Major Update Release Notes (v1.20)

Comprehensive release notes detailing all net additions, overhauls, and gameplay features introduced since the 2025 baseline release (v1.15).

---

## ⚔️ The Twin Devotion Paths: Blood Mage & Blood Knight

- **Twin Endgame Lifestyle Classes**: Blood magic is now split into two permanent, mutually exclusive lifestyle archetypes, each with distinct playstyles and 5 progression tracks (2 unique specialization tracks and 3 shared Devotion tracks):
  - **Blood Mage** (_Shepherd of the Faithful_): The occult scholar and dynasty architect. Focuses on realm stability, domain development, dread manipulation, and dynasty expansion.
  - **Blood Knight** (_Fire and Sword_): A dedicated martial warlord and battlefield champion. Focuses on personal prowess, combat advantage, army movement speed, and knight empowerment.
- **Mutual Exclusivity & Awakening**: Characters choose their path upon awakening to blood magic—via hereditary bloodlines, occult mentorship, witch conversion, or by venturing north to duel the 100-year-old hermit **Egill Skallagrímsson** in Iceland or Tsushima.
- **Shared Devotion Progression (Ancient, Enlightenment, Benediction)**:
  - Both classes advance through 3 shared spiritual tracks scaling up to 100 XP.
  - **Ancient**: Stepping stones grant +1 personal tenet slot every 20 XP (+5 slots total at 100 XP), alongside monthly dynasty prestige, lifestyle XP gain, Devotion Impact, and age-lock prowess.
  - **50 XP Milestones**: Dynamic scaling bonuses based on your Level of Devotion, including bonus knights, cultural acceptance, and diplomacy.
  - **100 XP Apex Capstones**: Unlock a massive **+50% Devotion Impact** multiplier (amplifying all Level of Devotion effects across your realm), universal immunity to aging prowess loss (**Age Prowess Lock**), and +2.0 skill points per Devotion level.
- **Dedicated Blood Knight Tracks**:
  - **Vanguard**: Boosts army movement speed, combat advantage, supply duration, and direct martial prowess.
  - **Slaughter**: Drastically increases personal prowess, knight limit, knight effectiveness, and bonus prowess scaling with Devotion.
- **Dedicated Blood Mage Tracks (Restructured 10-Step Cadence)**:
  - **Bloodline**: Standardized onto a clean 10-step cadence granting up to +24% Domain Taxes (8 standard steps of +3%), +40% Inactive Trait Inheritance Chance (4 medium steps of +10%), +50% Dynasty Prestige Multiplier (+25% at 50 & 100 XP), +2 Stewardship per Piety Level (+1 at 50 & 100 XP), and Age Prowess Lock.
  - **Hematurgy**: Streamlined onto a clean 10-step cadence granting up to +32 Hostile Scheme Success (8 standard steps of +4), -32 Enemy Hostile Scheme Success (4 medium steps of -8), +2 Intrigue per Piety Level (+1 at 50 & 100 XP), +2 Max Hostile Schemes (+1 at 50 & 100 XP), and Age Prowess Lock.

- **Blood Knight Rites & Champion Sacrifices**:
  - **Bless Blood — Blood of Iron**: Consecrate sworn knights, Blood Knight courtiers, or dynasty kin with Minor Lifeforce to bestow +2 Martial, +4 Prowess, +25% Knight Effectiveness, +1.0 Health, and +0.50 Health Penalty Negation for 10 years (`bm_blessed_blood_iron_modifier`).
  - **Crimson Sparring Ring (Yearly Decision)**: Convene sworn Blood Knights into the courtyard ring once per year (1 Minor Lifeforce, 1-year cooldown). Samples up to 3 candidates proportionally weighted by prowess ($w_i = \text{prowess}_i$) and initiates interactive practice duels via the Single Combat Engine (SCE). Victor condenses **1 Major Lifeforce** (+3 Vanguard/Hematurgy XP), loser earns +1 XP, and both combatants gain **+20 Blademaster trait XP** and +15 opinion.
  - **Cull Fallen Champion**: Offer critically broken followers or formidable captured warriors (Prowess 12+ or Blood Knights) upon the sacrificial altar for 1 Major Lifeforce and Slaughter/Hematurgy XP, rolling a prowess-scaled chance (up to 50%) to condense 1 Superior Lifeforce.
  - **Family & Kin Initiation**: Blood Knights can now initiate their spouse, children (any age), close family, extended family, and dynasty kin into `lifestyle_blood_knight` via `make_blood_knight_interaction` without requiring prior appointment as a combat knight. Major initiation awards **+5 Vanguard XP** (up from +4) when initiated into the dynasty, matching Blood Mage parity. Blood Knights can also empower family members and spouses via `empower_blood_knight_interaction` even if landed or outside their court.
- **Blood Magic Men-at-Arms Regiments**:
  - **Blood Berserkers (`bm_blood_berserkers`)**: Ferocious heavy infantry shock warriors (`100` soldiers/stack, unlocked at Devotion Level 2+ for Blood Mages and Blood Knights) boasting **60 Damage**, **20 Toughness**, **20 Pursuit**, and **0.10/day Siege Progress**. Counters Pikemen (1.5×), Skirmishers (1.0×), and Archers (1.0×), excels in Taiga/Forest/Mountains (+12 Damage, +8 Pursuit) and Winter (+10 Damage, +5 Toughness), and is recruited and maintained with Piety (250 Piety buy cost; 1.50 raised / 0.50 unraised monthly Piety).
  - **Blood-Bound Behemoths (`bm_blood_behemoths`)**: Towering albino flesh-constructs (`25` soldiers/stack, `elephant_cavalry` archetype, unlocked at Devotion Level 4+ for Blood Mages and Blood Knights) with **210 Damage**, **80 Toughness**, and **0.25/day Siege Progress** (matching heavy siege engines while dominating melee). Counters Heavy Infantry (2.0×) and Pikemen (2.0×), gains +15 Toughness in Mountains, Desert Mountains, Hills, and Drylands, suffers zero winter/desert penalties, consumes **0 Adventurer Provisions**, and is recruited and maintained with Piety (400 Piety buy cost; 1.50 raised / 0.50 unraised monthly Piety).

- **Go on a Blood Hunt Overhaul & Wilderness Expansion**:
  - Re-themed into **Go on a Blood Hunt**, open to both **Blood Mages** and **Blood Knights**.
  - **Inverted Cooldowns for Landed Rulers**: Blood Hunt cooldown is now **1 year** for landed rulers (addressing landed piety/Lifeforce scarcity) and **3 years** for wandering adventurers (halved to **6 months** landed, **1.5 years** wanderer with Superior **Vegvísir**).
  - **Unified Road Encounter with Escort Knight Champion**: The road encounter dynamically scales with character Prowess (clamped between 20% and 50% chance) and now unconditionally spawns both the wandering traveler and their formidable sworn escort knight champion for both Blood Mages and Blood Knights. Both classes can challenge the champion to a **Battlefield Single Combat Duel** (`prowess >= 25`), test the traveler in a Friendly Brawl, harvest them via Lifedrain (Prowess + Learning), or recruit them to court.
  - **Prowess-Driven Dispatcher & Multi-Skill Rebalance**: Fallback wilderness encounter rolls scale purely by Prowess, and all violent encounters use thematic multi-skill combinations calibrated to a fair 20 skill benchmark (~60% total success at 20 skill, ~70% at 25, ~80% at 30, ~95% at 40+):
    - *The Beast's Lair*: Face an apex predator via Prowess + Martial (vs 20 benchmark) for Major Lifeforce on a clean kill, Minor Lifeforce with wounds on a mixed kill, 0 Lifeforce if it breaks away, or a savage mauling on critical failure (or safely harvest kills outside).
    - *Blood in the Embers*: Ambush an outlaw camp via Prowess + Martial (vs 20 benchmark) to butcher them for Major Lifeforce and 25 Gold, skirmish for Minor Lifeforce and 10 Gold with wounds, watch them scatter, or get overpowered and robbed (or extort tribute peacefully).
    - *The Edge of the Woods*: Stalk an isolated homestead via Prowess + Intrigue + Martial (vs 20 benchmark) for a silent Major Lifeforce harvest, take minor wounds fighting off defenders, face barred doors, or get cornered (or demand an orderly blood tithe).
    - *The Crimson Rite*: Raid a rival occultist via Prowess + Learning (vs 20 benchmark) for Major Lifeforce, take a dying hex with Minor Lifeforce, watch them dissolve into mist, or suffer a catastrophic occult curse (or share the chalice peacefully).
    - *The Stag's Last Stand*: Run down a royal stag for Minor Lifeforce and Slaughter (Knight) / Hematurgy (Mage) XP.
    - *Blades on the Lonely Road*: Test wanderers in a 4-tier bout for blood, engage in Single Combat, drain traits, or recruit.
    - *The Cairn of Forgotten Carnage*: Rare ancient sacrificial cairn yielding clean Major Lifeforce, Enlightenment XP, and Ancient XP without exhaustion penalties.
  - **Contextual Availability Restrictions**: 'Go on a Blood Hunt' remains visible but grayed out with clear requirement tooltips whenever a character is traveling (`is_travelling = no`), participating in another activity or planning one (`is_in_activity = no`), imprisoned (`is_imprisoned = no`), or incapable (`is_incapable = no`).
  - **Dynamic Visuals**: Replaced passive portraits with active hunting and weapon stances across all encounters.

---

## 🧬 Blood Power & Somatic Ascendancy

- **Secondary Mastery Trait**: Blood Power is granted alongside Blood Mage or Blood Knight, representing the physical and metaphysical refinement of the caster's body and mind.
- **Flat Monthly Lifestyle XP Engine**: Every 10 XP in a track yields **+5 flat monthly Lifestyle XP** (paid out silently every 3 months via the quarterly playable pulse as **+15 XP per quarter**, up to **+50/mo = +150/quarter** at 100 XP):
  - *Presence* grants flat Diplomacy Lifestyle XP.
  - *Fury* grants flat Martial Lifestyle XP.
  - *Prosperity* grants flat Stewardship Lifestyle XP.
  - *Shadows* grants flat Intrigue Lifestyle XP.
  - *Mastery* grants flat Learning Lifestyle XP.
  - *Dynasty* grants flat Lifestyle XP to your currently active lifestyle focus (or a random core lifestyle if unfocused).
- **Six Focused Specialization Tracks (10 / 20 / 50 / 100 Cadence)**:
  - **Dynasty (Sanguine Eugenics & Kinship)**: Small steps grant positive inactive congenital inheritance (+40%) and trait upgrade chances (+40%); medium stepping stones add +5 Years of Fertility (+20 years total); milestones at 50 and 100 XP grant complete inbreeding immunity (-100%) and massive dynasty renown (+25%), plus flat Active Focus Lifestyle XP (+5 to +50/mo).
  - **Fury (Warfare & Siege Command)**: Small steps grant +1 Advantage (+8 total) and -3% Army Maintenance (-24% total); medium stepping stones grant -5% Siege Phase Time (-20% total) and +1 Knight limit (+4 total); milestones at 50 and 100 XP grant +1 Martial and +1 Prowess per Devotion level (+2 each total), Age Prowess Lock, and flat Martial Lifestyle XP (+5 to +50/mo).
  - **Mastery (World-Walker & Schemes)**: Small steps accelerate lifestyle XP gain (+40%); medium stepping stones grant personal scheme success (+20) and phase acceleration (-20 days); 50 and 100 XP milestones grant +1 Learning per Devotion level (+2 total, granting +2 Language Limit natively), +2 concurrent personal schemes, immunity to negative culture opinion, and flat Learning Lifestyle XP (+5 to +50/mo).
  - **Presence (Mesmeric Majesty)**: Small steps command realm-wide loyalty (+24 general opinion) and calm stress (-40%); medium stepping stones boost Fame Impact (+20%); 50 and 100 XP milestones grant +1 Diplomacy per Devotion level (+2 total), stabilize succession with -20% short reign duration, grant +20% long reign bonus, and flat Diplomacy Lifestyle XP (+5 to +50/mo).
  - **Prosperity (Wealth & Architecture)**: Small steps multiply monthly realm income (+40%) and cut holding and domicile construction costs (-24% for both landed holdings and adventurer camps/noble estates); medium stepping stones reduce Men-at-Arms maintenance (-20%); 50 and 100 XP milestones grant +1 Stewardship per Devotion level (+2 total), +2 domain limit (+1 at 50 XP, +2 total at 100 XP), and flat Stewardship Lifestyle XP (+5 to +50/mo).
  - **Shadows (Occult Warding & Intrigue)**: Small steps increase hostile scheme success (+40) and blunt enemy plot success against you (-40); medium stepping stones suppress enemy scheme maximum success caps (-20%); 50 and 100 XP milestones grant +1 Intrigue per Devotion level (+2 total), +2 concurrent hostile scheme slots, +15% own hostile scheme maximum success cap, and flat Intrigue Lifestyle XP (+5 to +50/mo).
- **De-cluttered Interface**: Streamlined track step tooltips and removed redundant universal vitality modifiers from Blood Power (already granted by Blood Mage and Blood Knight), keeping track progression comfortably visible on screen.
- **Major Grimoire Integration**: Channeling Blood Power is housed directly within the Cast Major Blood Magic Grimoire, presenting detailed breakdowns of 10 XP steps, 20 XP stepping stones, 50 XP milestones, and 100 XP capstones with zero-cost backout navigation.

---

## 🩸 The Three-Tier Lifeforce Economy

- **Three Potencies of Lifeforce**:
  - **Minor Lifeforce**: Common vital essence harvested from prisoners or minor rituals; provides passive health and disease resistance.
  - **Major Lifeforce**: Concentrated lifeblood used for powerful body modifications and high rituals; significantly extends lifespan.
  - **Superior Lifeforce**: The apex manifestation of life essence, required for creating immortal Blood Golems and carving legendary Superior Capstone runes.
- **Interactive Manifest Lifeforce**: Cast a scaling ritual via an interactive popup with four investment tiers (from 250 to 1,500 Piety), letting you condense life essence on demand without arbitrary cooldowns.
- **Battlefield Lifeforce Harvesting**: Blood Knights leading armies now directly reap Lifeforce from victorious battles, dynamically scaling with the scale of the confrontation (Skirmish, Battle, or Epic Clash).
- **Single-Combat Harvest**: Slaying rivals or duelists in lethal single combat allows Blood Knights to harvest their victim's life essence on the spot.
- **Childbirth Blessing**: Blood Mage and Blood Knight mothers channel supernatural protection during childbirth, yielding Major Lifeforce upon safe delivery.

---

## 📜 Grimoires, Spellcasting & Decision Widgets

- **Inline Option-List Decision Widgets**: Replaced event popup Grimoires with native CK3 1.20 scrollable decision option drawers for Minor, Major, and Superior Blood Magic, keeping every spell permanently visible with 45×45 icons, direct selection, and red failure tooltips:
  - **Minor Blood Magic**: Fast utility rituals including Lifeforce Attunement, Minor Blood Runes, Vitality Cleansing, and Lifeforce Condensation.
  - **Major Blood Magic**: Powerful rituals including Channel Blood Power, Condense Lifeforce (distilling Minor and Major into Superior Lifeforce), Education Enhancement (Tiers 1★–4★), Major Blood Runes, Congenital Trait Manifestation, and House Blessings.
  - **Superior Blood Magic**: Legendary rites including Blood Golem Creation, 5★ Master Educations, Secondary Educations, and Superior Capstone Runes.
  - _Attune Lifeforce_: Select your yearly lifestyle XP bonus with synchronized January 1st progression and clear interface toasts for both base Ancient progression and attunement gains.
  - _Empower Dynasty Bloodline_: Weave 7 Three-Tier House Covenants (Majesty, Warband, Prosperity, Shadow, Insight, Legacy, Mastery) across Minor, Major, and Superior tiers with live UI level tags and distinct House Modifier icons to permanently fortify your house (1-year cooldown), granting Bloodline XP to Blood Mages and Benediction XP to Blood Knights.
- **Unified Heal Affliction & Situation Alerts (`bm_heal_ailment`)**:
  - Cure up to 32 physical, mental, and fatal ailments, purge all 11 stress coping vices (-50 Stress), or progressively treat 5 old-age degenerative traits (`infirm`, `clouded_eyes`, `fragile_bones`, `withering_mind`, `faltering_heart`) on yourself, your courtiers, family, or knights through a single unified **Heal Affliction** interaction.
  - Elderly afflictions are managed through a streamlined 2-tier rejuvenation system: **Minor Treatment** (1 Minor Lifeforce + 50 Piety) automatically purges and cures the trait if track XP <= 20 (or reduces XP by -20 otherwise); **Major Treatment** (1 Major Lifeforce + 150 Piety) automatically purges and cures the trait if track XP <= 50 (or reduces XP by -50 otherwise), with dynamic button labels and interface toasts.
  - A persistent **"You Can Heal Someone"** notification appears in the Current Situation dropdown whenever an eligible courtier or family member is afflicted.
- **Ex-Nihilo Congenital Manifestation**: Manifest or improve genetic beauty, intellect, and physique traits through ritual blood channeling, supporting progression up to Rank 5.
- **Personality Reshaping**: Purge negative or conflicting personality traits from courtiers and imprint occult virtues through ritual blood manipulation.
- **Master & Secondary Educations**: Elevate education traits to mythical 5★ rank, or study under an ancient blood mentor to acquire an entirely new secondary education trait.

---

## ᚱ Icelandic Galdrastafir Flesh-Carved Blood Runes

- **Five Historical Galdrastafir Staves**: Carve authentic Icelandic magical staves directly into your character's flesh, each granting a passive ambient Lifeforce pulse and unique thematic bonuses:
  - **Vegvísir** (_The Wayfinder_): Travel safety, movement speed, supply capacity, and battlefield retreat defense.
  - **Ægishjálmur** (_Helm of Awe_): Terror, dread, knight effectiveness, and bonus Lifeforce from battlefield kills.
  - **Feingur** (_The Fertility Stave_): Fertility, pregnancy chance, health, and dynasty-wide blessing rites.
  - **Nábrókarstafur** (_Necropants / Wealth Stave_): Direct domain tax bonuses, building gold cost reductions, and monthly gold income.
  - **Hulinhjálmur** (_Helm of Disguise_): Hostile scheme success, scheme secrecy, and personal plot defense.
- **Superior Stave Capstones & Standalone Decision**: Reach Superior rune depth to unlock the standalone **Carve Galdrastafir Stave** decision (`bm_carve_galdrastafir_decision`), an inline option-list drawer displaying all 5 staves with dedicated icons and graying out your active stave, unlocking game-changing capstone powers (such as guaranteed double attunement XP, +20 gold per travel landmark POI, or terrifying battlefield debuffs).
- **Rune Inscription on Followers**: Inscribe blood runes onto your sworn knights, champions, and family members to bolster their combat prowess and loyalty.
- **Custom DDS Icons**: Every Galdrastafir stave features authentic, hand-crafted 120×120 visual iconography across modifiers, decisions, and menus.
- **Seven-Tier Blood Temples (`bm_blood_temple_01..07`)**: Construct and upgrade a 7-tier regular **Blood Temple** building line (**Blood Altar** $\rightarrow$ **Blood Shrine** $\rightarrow$ **Blood Monument** $\rightarrow$ **Blood Temple** $\rightarrow$ **Great Blood Temple** $\rightarrow$ **Blood Pantheon** $\rightarrow$ **Blood Acropolis**) in any holding type (castles, cities, temples, and tribal settlements) as a Blood Mage, Blood Knight, or Blóðtrú follower. Gated progressively by Level of Devotion (`piety_level`) with zero gold or piety upkeep, each step awards **+0.2 Health** and **+2 Life Expectancy** (up to +1.4 Health and +14 Life Expectancy at Tier VII), scaling monthly Piety (+0.5 to +4.0 and +5% to +40% mult), Dynasty Prestige (+0.1 to +1.0), county Development Growth (+0.1 to +0.8 flat and +5% to +40% factor), and monthly County Control Growth (+0.1 to +0.8), culminating in Tier V–VII lineage genetics (+5% to +15%), Prowess (+2), Fort Level (+2), and Defender Advantage (+5) capstones.

---

## 🗿 Immortal Blood Golems & Dynasty Legacy

- **Immortal Golem Champions**: Forge terrifying, albino, hairless flesh-constructs using Superior Lifeforce and high-stakes shaping duels.
- **Cadet Branch Integration (`bm_house_golem`)**: Golems are formally integrated into your dynasty as loyal immortal defenders under their own dedicated cadet branch.
- **Seven Supernatural House Modifiers**: Channel major blood rituals to permanently bless your dynasty's bloodline, unlocking stacking realm-wide bonuses to fertility, health, prowess, and domain administration.
- **4-Way Blood Blessings (`bm_bless_bloodline_interaction`)**: Bless children, dynasty kin, and sworn knights with specialized enhancements tailored to their role (automatically hiding once active): **Blood of the Sovereign** (+2 Dip/Stew, +10 Vassal Opinion, -25% Short Reign, +1.0 Health), **Blood of Iron** (+2 Martial, +4 Prowess, +25% Knight Effectiveness, +1.0 Health, +0.50 Health Penalty Negation), **Sanguine Crucible** (+25% Fertility, +25% Positive Congenital Chance, -25% Stress Gain, +1.0 Health) for 10 years, or **Feingur's Eternal Blessing** (permanent +25% Fertility, +20% Positive Genetic Chance, +0.50 Health, +5 Life Expectancy when holding Superior **Feingur**).
- **Anoint Heir in Blood & Succession Legacy Transfer (`bm_anoint_heir_interaction`)**: Consecrate a chosen successor with Major Lifeforce for permanent stat, opinion, and short-reign bonuses (hiding once anointed). Upon the ruler's death, the anointed heir awakens the predecessor's blood class trait, inherits 1 stack of each held Lifeforce tier, and absorbs 25% of all active trait track XP across all tracks.
- **House Head Blood Tithe (`bm_demand_blood_tithe_interaction`)**: House Heads can levy lifeforce from adult kin, yielding Major Lifeforce (from fellow practitioners) or Minor Lifeforce (from mundane relatives).
- **Situation Roster Tracking**: Keep track of all active blood golems and sworn mages across your realm directly within the Blood Magic Situation panel.


---

## ⛩️ Blóðtrú Religion Family & Sacred Sites

- **Three Specialized Regional Faiths**:
  - **Blóðtrú** (Norse & Germanic): The core occult faith emphasizing human sacrifice, ancestor communion, and blood initiation.
  - **Ketsudō** (Japanese & Shinto-Syncretic): Eastern warrior-mystic tradition centered on honor, discipline, and ritual dueling.
  - **Xuédào** (Chinese & Sinitic): Daoist-inspired internal alchemy focusing on vital energy cultivation and immortality.
- **Ancestor Worship Tenet**: Commemorate departed dynastic forebears to earn piety, renown, and spiritual defense.
- **Eminent Holy Sites**: Standardized holy sites across Iceland, Scandinavia, Ireland, Central Europe, China, and Japan, offering unique realm-wide spiritual bonuses (including Tsushima as the Eastern initiation eminent holy site for Ketsudō).
- **Challenge the Hermit of Reykjavík & Tsushima**: Landed rulers and wanderers can travel to remote geothermal springs to challenge the legendary 100-year-old warrior-mage **Egill Skallagrímsson** in a lethal duel to unlock blood magic secrets.
- **Reformation Repair System**: A built-in decision to cleanly resolve holy site and reformation locks when creating customized occult faiths.

---

## 🏕️ Domiciles & Realm Holdings

- **Five-Tier Blood Shrine**:
  - Landless adventurers (camps) and noble families (estates) can construct and upgrade a dedicated 5-tier Blood Shrine building line.
  - Scales piety generation (+0.5 per tier, up to +2.5 monthly piety at Tier V), health, lifespan, and genetic inheritance chances, while projecting a camp-wide occult aura at half potency (+0.25 piety, +0.1 health, +1 lifespan, +2.5% genetics per tier) to all followers and courtiers.
- **Seven-Tier Duchy Blood Temples**: Expand county development, control, piety generation, and personal longevity with 7 tiers of Blood Temple Duchy Capital buildings (Altar, Shrine, Monument, Temple, Great Temple, Pantheon, Acropolis) constructible in any duchy capital (including tribal holdings, with tribal rulers progressing up to Tier IV and feudalized realms reaching Tier VII). Always visible in the duchy building slot with grayed-out requirement preview.

---

## 🖥️ "Blood Magic" Situation Panel & User Interface

- **Centralized Situation Hub**: Access the mod's core systems from a dedicated "Blood Magic" Situation panel:
  - Monitor your current discipline, track XP progression, active Lifeforce potencies, and carved Galdrastafir stave.
  - Real-time live character rosters tracking **Dynasty Blood Mages**, **Sworn Blood Knights**, and **Blood Golems**.
  - Direct one-click access to Grimoires, Attunement, and Carving decisions.
- **Dedicated "Blood Magic" Context Menu Section**: All mod character interactions (healing, Lifeforce harvesting, trait theft, blood knight creation, curses, runes, self-exsanguination, vice purging, consecrated unions, peer empowerment, and personality influence) now appear neatly grouped under a dedicated **Blood Magic** header section with a crimson accent bar in the right-click character menu, removing clutter from vanilla Personal and Hostile tabs.
- **Bleed the Own Vein Interaction**: Self-interaction on a 1-year cooldown allowing Blood Mages and Blood Knights to condense Minor or Major Lifeforce directly from their own veins at the cost of wounds, stress, and drained vitality.
- **Purge Stress Vices Interaction**: Burn away all 11 negative stress coping traits (Drunkard, Hashishiyah, Rakish, Reclusive, Irritable, Flagellant, Profligate, Improvident, Contrite, Comfort Eater, Inappetetic) from yourself or a close relation/ally using 250 Piety and 1 Major Lifeforce, reducing Stress by -50.
- **Bidirectional Blood Knight Mentorship & Lifeforce Sharing**: Non-magical characters can now ask Blood Knights for blood magic or extract it from imprisoned Blood Knights to awaken directly as a Blood Knight. Blood Knights can also grant or restore Lifeforce stacks to allies and prisoners.
- **Stealth Siphon Stave Concealment**: Superior **Hulinhjálmur** now flawlessly conceals the caster from opinion discovery penalties when failing courtier siphons or blood curses.
- **Consecrate Union Interaction**: Consecrate the bond between yourself and your spouse, consort, or lover. Channeling Minor (3 years) or Major (10 years) Lifeforce applies the Consecrated Union modifier (+50% Fertility, +10 Years Fertility Window, +30% Positive Congenital Chance, +30% Congenital Trait Reinforce Chance) while awarding Bloodline or Benediction XP.
- **Empower Blood Mage**: Symmetrical peer empowerment interaction allowing Blood Mages to channel Minor or Major Lifeforce into court mages, apprentices, family, and spouses, advancing their Enlightenment and Bloodline tracks while awarding Benediction experience to the caster.
- **Siphon Stored Lifeforce**: Contested extraction rite allowing Blood Mages (Learning/Intrigue) and Blood Knights (Prowess) to rip away held Lifeforce reserves (Minor, Major, Superior) from other characters, with guaranteed automatic success when draining imprisoned captives.
- **Contest of the Red Art**: High-stakes occult duel between Blood Mages and Blood Knights testing combined Learning and Prowess, rewarding critical victors with Major Lifeforce while cursing their defeated rivals.
- **Interface Toast Wrappers**: Initiations and empowerments now wrap outcomes directly in native interface toasts with automatic Lifeforce stack recounting.
- **Influence Personality Interaction**: Commune with a relationship target's mind to dissolve an unwanted personality trait and imprint one of your own, or rewrite their cultural heritage to embrace your own culture, via a Learning contest (50% base, scaling to 95% at +20 Learning difference; 5-year cooldown on success, 1-year cooldown on failure, no Cast Major Blood Magic debuff).
- **Distinctive Visual Assets**: Custom 120×120 DDS icons across traits, level tracks, character interactions, staves, and religious faiths.
- **Situation Alerts**: Prominent warnings in CK3's Current Situation dropdown notify you whenever a kinsperson or courtier needs healing.

---

## 👁️ Supernatural Visuals & Campaign Game Rules

- **Supernatural Portrait Evolution**:
  - **Glowing Eyes**: Progresses dynamically from subtle red to supernatural crimson, pale arcane, and pure white eyes at maximum mastery.
  - **Supernatural White Hair Evolution**: Blood Mages and Blood Knights gradually bleach from subtle silver to pure white hair alongside crimson and white eyes.
- **Unified Appearance Game Rule**: Configure physical transformations at game start:
  - _Off_: Retain normal human appearance.
  - _Gradual_: Eyes and hair transform dynamically as lifestyle track XP is earned.
  - _On (Default)_: Immediately display full supernatural eyes and hair upon awakening to blood magic.
- **Comprehensive Campaign Game Rules**:
  - _Blood Mage Prevalence_ (Player Only to Frequent AI spawn).
  - _Blood Knight Prevalence_ (Player Only to Frequent).
  - _Blóðtrú Religion Availability_ (Player Only, Unreformed Only, or World Distribution).
  - _Historical Starting Counties_ (Toggle historical occult centers in Iceland and Tsushima).
  - _Initiation Faith Requirements_ (Strict blood cult requirement vs. Witchcraft tolerance).
  - _Lore Integration_ (Vanilla historical vs. AGOT overhaul lore compatibility).
- **Strict Zero-Vanilla Overwrite Architecture**: 100% modular scripting (`bm_` prefix on all files) ensures complete plug-and-play compatibility with total conversion overhauls (AGOT, Elder Kings, Realms in Exile, More Bookmarks+).

---

## 🩸 Interactive Narrative & Interpersonal Events

- **Dynamic Interpersonal Pulse**: Narrative events fire through an annual pulse for player Blood Mages and Blood Knights (governed by a 3-year cooldown):
  - **A Drop on the Lips (Lovers, Soulmates & Spouses)**: Share a drop of Minor Lifeforce to bless your partner's health and fertility for 10 years and relieve mutual stress; willingly drink from their offered vein to harvest Minor or Major Lifeforce; or initiate an unawakened partner into the Crimson Mysteries using Major Lifeforce to awaken them as a Blood Mage or Blood Knight and forge an eternal Soulmate bond.
  - **The Fever of Awakening (Children & Wards Age 6–15)**: Detect the dangerous occult churning of blood in young scions. Guide their pulse with Minor Lifeforce to permanently boost Learning, Martial, and Prowess; spend Major Lifeforce to force their awakening early with bonus Ancient XP; or soothe their fever with pious prayer.
  - **The Red Banquet After Battle (Sworn Knights)**: Following combat victories with knights on the field (15% chance), partake in the gory aftermath together to restore Minor Lifeforce and forge lasting camaraderie; claim the entire battlefield harvest as an undisputed Warlord for Major Lifeforce and Slaughter XP; or consecrate the fallen earth for massive Piety and Enlightenment XP.
  - **Echoes in the Clay (Blood Golems)**: Commune with your court's Blood Golem as ambient magic settles into its frame. Bind it as an immortal shield to grant your primary heir or spouse the Golem's Aegis (+4 Prowess, +0.25 Health, -20% Enemy Hostile Scheme Success for 10 years); awaken its ancient martial memory to grant Blademaster or +4 Prowess; or siphon excess ichor from its core for Major Lifeforce.
  - **The Whispering Sanctum (Snooping Courtiers)**: Catch an uninitiated courtier intruding upon your private sanctum rites. Subdue and drain them in the dark via an Intrigue/Prowess duel for Minor Lifeforce, Dread, and Hematurgy/Slaughter XP; bribe their eternal silence with a drop of Minor Lifeforce to gain a permanent Strong Loyalty Hook and +40 Opinion; or disperse the ritual mist to regain composure.

---

## 🛠️ Bugfixes & Engine Modernization

- **Lifedrained Self-Restoration & Universal Reversal**: Fixed an issue where characters who used Bleed Own Veins (Major) were permanently afflicted by `lifedrained_modifier` with no self-cast interaction or decision to cleanse it. Updated `grant_lifeforce_interaction` so blood mages and blood knights can target themselves whenever afflicted with `lifedrained_modifier`, opening directly into the Reverse Lifedrain rite (consuming 1 Major Lifeforce and 25 Piety, cleansing the drain, bestowing 1 Minor Lifeforce rebate, and awarding +4 Benediction XP). Additionally broadened targeting so any character suffering Lifedrained can be targeted for cleansing regardless of family/court relations, and configured the interaction to display grayed out with a clear requirement tooltip whenever lacking Major Lifeforce.

- **AI Lifedrain Court Protections & Modifier Ordering Fix**: Fixed Clausewitz AI modifier evaluation ordering and inverted title-tier calculations in `ai_willingness_to_lifedrain` that previously caused additive scores to override `factor = 0` vetoes. AI blood mages and knights are now strictly forbidden from lifedraining spouses, children, close family, knights, councillors, employed court positions (physicians, bodyguards, seneschals, caravan masters), and Blood Golems under any circumstances. Human players retain complete roleplay agency.
- **Engine Trait Flags & Debug Log Cleanup**: Removed `good = yes` and `random_creation = 0.20` declarations from non-genetic lifestyle traits (`lifestyle_blood_mage` and `lifestyle_blood_knight`), resolving four engine startup errors in `error.log`. Streamlined internal execution logging to eliminate loc data-system parsing errors during tooltip evaluations in mass execution events.
- **Trait Track XP Rebalance & Vanguard Depuration**: Rebalanced XP progression for Blood Knights and Blood Mages so that track gains remain low, earned, and paced across a character's lifetime:
  - Purged non-combat family rites (consecrate union, anoint heir, blood tithe) and childbirth from advancing the martial `vanguard` track, rerouting family rites to `benediction` (+1 to +2 XP) and childbirth milestones to `ancient` (+1 to +2 XP).
  - Consolidated all healing magic (self-healing and healing others) to grant strictly `benediction` XP (+1 for minor ailments, +2 for major/deadly), fixing erroneous `enlightenment` and `vanguard` gains.
  - Targeted congenital trait manifestation XP by attribute: Physique grants `vanguard` (+1 standard, +2 superior), Intellect grants `enlightenment` (+1 standard, +2 superior), and Beauty grants `ancient` (+1 standard, +2 superior), while removing excessive superior Enlightenment bonuses.
  - Flattened `Manifest Lifeforce` decision XP to a disciplined +1/+1/+2/+2 `enlightenment` progression, fixed double-counting on minor channeling, scaled down Master Education XP (+3 to +5) and Second Trait (+3), and toned down interpersonal yearly event option rewards to +1 XP.
- **Interaction Data-Binding & Scoping Fix**: Bound recipient scopes (`subject = scope:recipient`) in `Consecrate Union` and `Siphon Stored Lifeforce` failure conditions, resolving `Failed to find type 'recipient'` data-binding errors in interaction tooltips.
- **Blood Golem Trait Option Visibility**: Corrected event option syntax in golem shaping rites (`blood_golem.002`) by placing `show_as_unavailable` at the option level rather than inside trigger blocks, resolving `Unknown trigger: show_as_unavailable` errors.
- **Null-Safe Heir Comparison**: Replaced direct primary heir comparison with native `is_primary_heir_of` in other-rune inscription interactions, preventing crashes on unlanded or heirless characters.
- **Localization Polish**: Added missing toast localization for Minor Purge Impurities (`bm_purge_impurities_toast`), purged duplicate Manifest Traits keys, removed dangling references to deprecated `resilience_attuned`, and updated interpersonal event themes to native engine standards.

- **Decision Event Dialog Fix**: Resolved an issue where multiple UTF-8 BOM headers at file start caused the game engine to drop event namespaces, preventing dialogs from opening when clicking "Seek Power" and "Cast Major Blood Magic -> Channel Blood Power".
- **Interaction Registration**: Corrected encoding on character interactions ensuring "Inscribe Blood Rune" registers cleanly in character menus.
- **Localization Syntax**: Fixed a formatting typo in modifier descriptions that caused localization parser errors.
- **Current Situation Healing Alerts**: Fixed a display issue where "(NUM)" appeared literally in the grouped healing alert header, and streamlined descriptions to concisely instruct spending Lifeforce.
- **Empower Dynasty Bloodline Tooltip**: Removed obsolete legacy un-suffixed modifier removal effects that caused Tier I covenant previews to falsely claim the house would lose an old modifier.
- **Covenant Button Syntax Fix**: Corrected unescaped square brackets in dynamic covenant button labels that triggered the engine's data-binding parser and displayed `ERROR:[Minor]` or `ERROR:[Major]` in the Empower Dynasty Bloodline decision widget.
- **Empower Dynasty Benediction XP**: Updated the Blood Power "Empower Dynasty" ritual option to grant +3 Benediction XP instead of Enlightenment XP, and harmonized Blood Knight house covenant gains to award Benediction XP.
- **Tiered Education Devotion Requirements & Superior Piety Level Costs**: Overhauled education advancement rites (`bm_major_improve_education` / `bm_education_enhancement.001` and `bm_superior_master_education` / `bm_education_master.001`) so Devotion Level requirements scale with trait rank while devotion level loss is strictly reserved for Superior magic:
  - **1★ -> 2★**: Requires Devotion Level 1+ (Dutiful). No Devotion Level cost.
  - **2★ -> 3★**: Requires Devotion Level 2+ (Faithful). No Devotion Level cost.
  - **3★ -> 4★**: Requires Devotion Level 3+ (Servant of God). No Devotion Level cost.
  - **4★ -> 5★ (Mastery)**: Requires Devotion Level 4+ (Holy Person). Advancing costs 1 Devotion Level on success or critical failure (Superior magic).
  - **Embrace New Education**: Requires Devotion Level 4+ (Holy Person) and 1000 Piety + Superior Lifeforce without deducting a Devotion Level.
  - Possessed disciplines that lack the required Devotion Level are displayed grayed out with the exact unmet requirement, while unowned education disciplines remain hidden to prevent event window clipping.
- **Blóðtrú Faith Virtues**: Added `lifestyle_blood_knight` as an explicit virtue alongside `lifestyle_blood_mage`.
- **Repository Integrity**: Updated repo validation tools with strict multi-BOM and embedded BOM detection to prevent file encoding regressions.
