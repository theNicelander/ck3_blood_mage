# Blood Mages — Release Notes (v1.20)

Net player-facing changes since v1.15 (2025 baseline), grouped by feature area. Version history is at the bottom.

---

## Blood Mage & Bloodlust

- Unified single lifestyle path: **Blood Mage** featuring six distinct progression tracks: Ancient, Enlightenment, Benediction, Bloodline, Hematurgy, and the new **Bloodlust** track (combat advantage, knight effectiveness, sworn knight limit, and duel harvesting).
- Awaken via bloodline, occult mentorship, witch conversion, fellow Blood Mage mentorship, or by duelling the hermit **Egill Skallagrímsson** in Iceland or Tsushima.
- All Blood Mages are recognized as **Worthy Commanders** (`ignores_gender_army_rules = yes`), allowing them to lead armies into battle regardless of faith or cultural gender rules.
- Devotion tracks (Ancient, Enlightenment, Benediction) scale to 100 XP: Ancient adds +0.1 monthly legitimacy per 10 XP (+1.0/mo = +12/yr at 100 XP) alongside +1 personal tenet slot per 20 XP.
- 50 XP milestones scale with Devotion Level; 100 XP capstones give +50% Devotion Impact and +2.0 skill per Devotion level (and age lock for Acolyte and Blood Power tracks).
- Bloodline and Hematurgy: 10-step cadence (universal monthly income mult, trait inheritance, dynasty prestige, hostile scheme power and defence, natural dread baseline).
- **Bloodlust**: 10-step cadence granting scaling Commander Advantage (+8 to +16 total), Knight Effectiveness (+40% to +120% total), Knight Limit (+4 to +8 total), and scaling Martial & Prowess per Piety Level (+1 to +2 per level at 50/100 XP milestones), culminating in an Age Prowess Lock for Acolytes.
- Tier II (Mage) and Tier III (Archmage) base stats permanently absorb all cumulative track milestone benefits up to 50 XP (and 100 XP for Ancient) alongside innate age prowess locks, preserving all scheme slots, success chances, opinion, army damage, income multipliers, and spiritual tenets upon tier elevation.
- **Blood Mirror Ascension Duel**: In the tier elevation ritual, face an exact mirror reflection of your mortal vessel—sharing your given name, dynasty "Blood Ghost", mirrored personality, education, physical and combat traits, 20 across mental/governing attributes, and prowess matching your own. Lifeforce is no longer required or consumed to attempt tier ascension, and unspent discipline experience is extracted into Lifeforce at 1 stack per 20 XP upon victory.
- XP sources unified: battlefield victories (+1 to +3), combat survival (+1), lethal single combat (+3), and tournaments (+2) feed Bloodlust directly.
- **Blood Power** secondary trait with six mirrored tracks (Dynasty, Warband, Mastery, Presence, Prosperity, Shadows) structured into five milestone tiers (10, 30, 50, 70, 100 XP) with scaling monthly Piety (+0.1 to +1.0), flat monthly lifestyle XP (+5 to +50/mo), shared 50 & 100 XP milestone bonuses (+10% monthly Piety mult, +5 life expectancy, +0.25 health, +0.02 monthly Piety per knight), and a tight suite of 3–4 high-impact personal modifiers delivering 2x–3x the power of House Covenants (including scaling legitimacy mult, stress composure, universal income mult, and inbreeding immunity), culminating in an Age Prowess Lock.
- Track XP sources rebalanced: healing grants Benediction, family rites and childbirth grant Ancient/Benediction, congenital manifestation grants XP by attribute.
- Regiments: **Blood Berserkers** (heavy shock infantry, Devotion 2+) and **Blood-Bound Behemoths** (siege-capable monsters, Devotion 4+), Piety-maintained.
- Crimson Sworn-Guard court position and Crimson Warrior champions.
- **Track Tooltip Trim & 5-Milestone Consolidation**: Consolidated all six lifestyle tracks across Acolyte, Mage, and Archmage into 5 clean milestones (10, 30, 50, 70, 100 XP) matching Blood Power, removing tooltip bloat and eliminating overlap with specialized reservoirs. Ancient grants flat dynasty renown, legitimacy, devotion impact, personal tenet slots (+1 at 50/100), and max piety level (+1 at 100 XP, absorbed as +1 on Mage and +2 on Archmage base traits). Enlightenment provides flat and percentage monthly piety plus knight effectiveness per Learning (+0.5% to +1.0% per milestone, plus +0.5% / +1.0% base floors). Benediction adds general opinion, personal scheme max success chance, and +1 concurrent personal schemes at 50 XP. Bloodline boosts monthly income, cuts army maintenance costs, fosters capital county development growth, grants flat monthly income, and expands direct domain limit (+1 to +4 holdings). Hematurgy raises hostile scheme max success, reduces enemy max success, and unlocks +1 concurrent hostile schemes at 50 XP. Bloodlust increases sworn knight limit (+1 at every milestone 10/30/50/70/100; +3 base on Mage, +6 base on Archmage), army damage percentage, and knight effectiveness per Prowess (+0.5% to +1.0% per milestone, plus +0.5% / +1.0% base floors). Warband focuses on Men-at-Arms counter efficiency (+10% to +50%), regiment size (+1 to +4), and max regiments (+1 to +2). Removed fertility years and plague resistance from generic track steps into dedicated Mojo Lifeforce and doubled Lifeforce disease resistance (+2 / +6 / +12).

## Lifeforce

- Three tiers: **Minor** (health, disease resistance), **Major** (lifespan, body rituals), **Superior** (Blood Golems, capstone runes).
- **Bidirectional Condensation & Splitting**: Transmute between Lifeforce tiers in Cast Blood Magic decisions: condense Minor to Major (150 Piety, 6-mo cooldown), condense Major to Superior (350 Piety, 6-mo cooldown), split Superior into 2 Major (350 Piety, 6-mo cooldown), or split Major into 2 Minor (150 Piety, 6-mo cooldown).
- **Specialized Lifeforce Reservoirs (Mojo, Fury, Focus)**: Dedicated permanent, stackable Lifeforce reservoirs transmutable from Minor/Major reserves. Blood Mojo governs fertility and congenital inheritance (+10% fertility, +5 years, +5% inheritance/strengthen chance); Blood Fury fuels martial lethality and swift deployment (+2 prowess, +10% knight effectiveness, +2% army movement speed, +2 travel safety); Blood Focus sharpens study and composure (+1 learning, -10% stress gain, +5% monthly lifestyle XP). Removed prowess from Superior Lifeforce, focusing core reserves strictly on Immortality and Vitality. Convert Minor (50 Piety) or Major (100 Piety -> 3 stacks) to specialized reservoirs, reclaim to Minor (75 Piety), bestow Mojo upon spouses and kin, or burn Mojo during childbirth to quicken newborn awakening.
- **Manifest Lifeforce**: four Piety tiers (250–1,500), no cooldown.
- Blood Mages harvest Lifeforce from battles and lethal single combat duels.
- Blood Mage mothers yield Major Lifeforce on safe childbirth.
- **Bleed Own Veins**: self-interaction (1-year cooldown) for Minor or Major Lifeforce at the cost of wounds, stress and drain.
- **Siphon Stored Lifeforce** takes Minor/Major/Superior reserves from other characters via a contest.
- **Contest of the Red Art**: Learning + Prowess duel between fellow Blood Mages.
- **House Head Blood Tithe** levies Lifeforce from adult kin.

## Spellcasting & Decisions

- Cast Blood Magic (Minor, Major, Superior) are inline option-list decisions; every spell stays visible, grayed out when unavailable.
- **Transmute Lifeforce**: Dedicated inline option-list decision consolidating all 13 Lifeforce-to-Lifeforce conversions (Minor/Major to Mojo/Fury/Focus, reservoir reclaiming, tier condensation, and tier splitting) into one place, accessible from both the Decisions view and the Blood Mage Situation tab, decluttering the Minor, Major, and Superior spellcasting grimoires.
- **Minor**: Minor Blood Runes, Cleansing Impurities, Channel Minor Lifeforce (+10 monthly Lifestyle XP in chosen attribute; +5 monthly to active focus for Experience Gain).
- **Major**: Channel Blood Power, Education Enhancement, Major Runes, Congenital Manifestation, House Blessing.
- **Superior**: Blood Golem creation, 5★ Master Educations, Secondary Educations, Capstone Runes.
- **Attune Lifeforce**: choose your yearly lifestyle XP bonus (applied January 1st).
- **Empower Dynasty Bloodline**: six three-tier House Covenants (Presence, Warband, Prosperity, Shadow, Mastery, Legacy) granting monthly Piety (+0.1/+0.3/+0.5), skill, and +1 attribute per Devotion at Tier 2 and Tier 3 alongside balanced house-wide bonuses (Men-at-Arms, army damage, speed, domain limit, opinion, legitimacy mult, monthly Piety per knight, and knight effectiveness per Prowess/Learning on Warband and Mastery); active covenants roll annually to award +1 XP in the matching Blood Power track for living kin.
- Education advancement needs Devotion Level 1+/2+/3+/4+ for 1★→2★ … 4★→5★; only Superior magic (5★, Embrace New Education) costs Devotion or needs 1000 Piety plus Superior Lifeforce.
- **Heal Ailment**: cures up to 32 ailments, purges all 11 stress vices (−50 Stress), and treats old-age traits (Minor: 1 Minor Lifeforce + 50 Piety; Major tier for deeper rejuvenation).
- **Influence Personality**: Learning contest to swap a trait or culture (5-year cooldown on success, 1 year on failure).
- **Congenital Manifestation**: Transmute Intellect, Physique, and Beauty up to Rank 3 in Major Blood Magic (250/500/750 Piety, Piety Levels 2/3/4; Rank 3 costs 1 Devotion Level) and up to Ranks 4–5 in Superior Blood Magic (1000/1500 Piety, Piety Level 5; costs 1 Devotion Level); 2-year cooldown. Standard failure refunds lower-tier Lifeforce; critical failure inflicts additional exhaustion.
- **Bestow Blood Traits**: Spend 250 Piety and 1 Major Lifeforce to pass positive congenital (Intellect, Physique, Beauty) or physical traits (Fecund, Pure-Blooded, Giant, Strong, Shrewd) to your spouse or dynasty kin. Elevates target one tier per ritual; guaranteed if transferring a rank lower than your own, or resolved via a Learning duel with yourself (50% at 20 Learning, 90% cap at 50 Learning) if transferring a matching rank.
- Personality Reshaping (Learning contest to swap traits).

## Blood Hunt

- *Seek Power* became **Go on a Blood Hunt**, open to Blood Mages; grayed out while travelling, in an activity, imprisoned or incapable.
- Cooldown: 1 year (halved to 6 months with Superior Vegvísir).
- Encounters scale with Prowess: Beast's Lair, Blood in the Embers, Edge of the Woods, Blood Rite, Stag's Last Stand, Blades on the Lonely Road, Cairn of Forgotten Carnage.
- Roughly 60% success at skill 20, 70% at 25, 80% at 30, 95% at 40+; peaceful options exist for most encounters.
- Road encounter can include a sworn escort champion to duel (Prowess 25+).

## Blood Rites

- **Bless Blood**: consecrate knights and kin (+2 Martial, +4 Prowess, +25% Knight Effectiveness for 10 years).
- **Blood Sparring Ring** (yearly, 1 Minor Lifeforce): practice duels; winner gains 1 Major Lifeforce, both gain Blademaster XP.
- **Cull Fallen Champion**: sacrifice broken or captured warriors for Major Lifeforce, with a chance of Superior.
- **Anoint Champion / Anoint Heir**: permanent bonuses; anointed heirs awaken with a Lifeforce transfer on succession.
- Overlapping blessing interactions merged into one 4-option Bless Blood; options hide once active.

## Galdrastafir & Blood Runes

- Five Icelandic staves carved into the flesh, each with an ambient Lifeforce pulse: **Vegvísir** (travel), **Ægishjálmur** (terror, knights), **Feingur** (fertility), **Nábrókarstafur** (gold), **Hulinhjálmur** (schemes, concealment).
- Superior rune depth unlocks the standalone **Carve Galdrastafir Stave** decision.
- Inscribe blood runes on sworn knights, champions and family; 3-year cooldown on rune inscriptions and upgrades.
- Custom icons for all staves, traits, tracks, interactions and faiths.

## Blood Golems & Dynasty

- Forge immortal albino golems with Superior Lifeforce and a shaping duel; they join the dynasty as cadet house `bm_house_golem`.
- Seven house modifiers stack realm-wide bonuses to fertility, health, prowess and administration.
- **Bless Bloodline** (children, kin, knights) with role-specific blessings.
- **Anoint Heir in Blood**: permanent stats, opinion and short-reign bonuses.
- **Consecrate Union**: spouse/lover/consort gain +50% fertility and better genetic inheritance (Minor 3 years, Major 10 years).
- **Empower Blood Mage**: peer interaction advancing Enlightenment and Bloodline tracks.

## Blóðtrú Religion

- Three reformed mainline faiths: **Blóðtrú** (European), **Ketsudō** (Japanese), and **Xuédào** (Chinese), organized by default to remove Feudal/Clan vassal penalties and enable Holy Wars. Three unreformed ancestral counterparts (**Old Blóðtrú**, **Old Ketsudō**, **Old Xuédào**) available at character creation or via conversion decision for tribal raiders and manual reformation roleplay.
- Ancestor Worship tenet earns piety, renown and defence; Mendicant Preaching replaces Ritual Celebrations.
- All 58 Blóðtrú, 27 Ketsudō and 32 Xuédào holy sites are now Eminent Holy Sites (up to 80 active), granting smaller stacked global faith bonuses alongside local county holder modifiers.
- Reformation repair decision resolves holy-site locks when creating custom faiths.
- Blood Mage is no longer a religion virtue.
- **Level of Devotion Cap**: Default Piety Level cap raised to 8 globally (`DEFAULT_PIETY_LEVEL_CAP = 8`), unlocking Level 6 (Divine), Level 7 (Demigod), and Level 8 (Godlike) for all rulers and governments.

## Buildings

- **Blood Temples**: seven-tier duchy-capital buildings (Altar → … → Acropolis), available in all duchy capitals including tribal; tiers I–IV open to more holders, granting scaling monthly Piety, Piety per sworn knight (+0.02 to +0.20 and +1% to +5% per knight), dynasty renown, health, lifespan, and genetics.
- **Blood Shrine**: five-tier line for camps and estates (up to +2.5 monthly piety, +0.10 and +5% monthly piety per knight at Tier V, plus health, lifespan and inheritance).

## Interface & Interactions

- **Blood Magic Situation panel**: discipline, track XP, Lifeforce, stave, and rosters of dynasty Blood Mages and Golems.
- All mod interactions grouped in a "Blood Magic" context-menu section; outcomes shown in interface toasts.
- Consolidated positive character interactions into unified modal window **Blood Blessing** (Empower Blood Mage, Grant Lifeforce, Bless Blood, Annoint Heir, Consecrate Union, Inscribe Blood Rune).
- Consolidated hostile lifeforce extraction into unified modal window **Blood Drain** (Major Life drain, Minor Life drain, Drain Stored Lifeforce, Demand Blood Tithe).
- **Blood Healing**: interaction is always clickable when an affliction is present to inspect requirements directly in the event; Deadly afflictions (leprosy, cancer, plague) now require Superior Lifeforce and 100 Piety (+3 Benediction XP).
- Current Situation healing alert (`bm_action_can_heal`) monitors councillors, immediate and close family, court positions, and companions; styled green (`Can Heal`) when the corresponding Lifeforce is held, and gray (`Needs Lifeforce`) under unimportant actions when Lifeforce is lacking. Alerts also notify when prisoners can be lifedrained or 20+ Prowess champions culled.
- Cull Fallen Champion requires 20+ Prowess across all targets (captives and fallen followers).
- **Purge Stress Vices** burns away all 11 coping traits.
- Hulinhjálmur conceals the caster from discovery penalties on failed siphons and curses.

## Narrative Events

Annual pulse (3-year cooldown) for player Blood Mages:
- **A Drop on the Lips**: bless a lover or spouse, or awaken them.
- **The Fever of Awakening**: guide or hasten a child's (6–15) awakening.
- **The Red Banquet After Battle**: feast, claim the harvest, or consecrate the field.
- **Echoes in the Clay**: shield an heir, grant Blademaster, or siphon the golem.
- **The Whispering Sanctum**: drain, bribe or disperse an intruding courtier.

## Icelandic Culture & Traditions

- Playable **Icelandic** culture (`bm_icelandic`) featuring equal martial custom, North Germanic heritage, communal ethos, and 5 starting traditions.
- Custom tradition **Alþingi Commonwealth** (`bm_tradition_althingi`) replaces Ting-Meet:
  - Unlocks Scandinavian Elective and Hólmganga (Trial by Combat).
  - Grants +0.10 monthly development growth to the capital, +25% cultural head fascination, +0.05 county development growth, +25% county development growth factor, and +0.10 monthly county control growth.
- Custom tradition **Verbúðir** (`bm_tradition_verbudir`) replaces Maritime Mercantilism:
  - Accessible to Tribal and Feudal cultures from 867; allows Tradeport construction 1 era earlier and enables Tradeports in Tribal holdings.
  - Integrates with Tradeport harbor tiers 1–8: grants stationed Men-at-Arms toughness, scaling County Control Growth, Levies, and +2% Cultural Fascination Progress per tier alongside Avaricious bonuses.
  - Grants -75% embarkation gold cost, reduced sea and coastal danger, +20% county taxes, +20% levies, +25% supply limit, and +0.05 monthly control growth.
- Curated Icelandic saga name list with epenthetic `-ur` patronymics and 31 historical Sturlungaöld, heroic, and Tolkien-adapted houses.
- Modular game-start conversion of `d_iceland` gated by the `bm_icelandic_culture` game rule.

## Visuals & Game Rules

- Eyes progress from red to crimson, pale and white; hair bleaches to white.
- Rules: Appearance (Off / Gradual / On), Blood Mage Prevalence, Blóðtrú Availability, Historical Starting Counties, Initiation Faith Requirements, Lore Integration (vanilla vs AGOT).
- Fully modular (`bm_` prefix), no vanilla overwrites; compatible with total conversions.

## Bugfixes

- Fixed supernatural appearance game rule (white hair and white eyes) not applying to Blood Acolytes or Blood Archmages.
- Ascension duel defeat effects (exhaustion, wounds, XP penalty) display natively in toast notification.
- Reverse Lifedrain: self-targeting works for characters drained by Bleed Own Veins.
- Fixed decision dialogs not opening and "Inscribe Blood Rune" missing from menus (duplicate BOM).
- Fixed raw "(NUM)" in healing alerts and `ERROR:[Minor]` in covenant buttons.
- Fixed tooltip scoping errors in Consecrate Union and Siphon Stored Lifeforce.
- Fixed golem rite option visibility and heirless-character crashes in rune interactions.
- Empower Dynasty tooltip no longer claims a house loses an old modifier.
- Added missing toast and loc keys; removed dangling modifier references.
- Resolved startup trait errors in ascension duel mirroring, restored Blood Crucible blessing to Blood Blessing interaction, and fixed decision debug logging.

---

## Version history

- v1.20.80: Mainline blood faiths (Blóðtrú, Ketsudō, Xuédào) organized/reformed by default; introduce explicit unreformed variants (Old Blóðtrú, Old Ketsudō, Old Xuédào) with 1:1 mainline rites and conversion decision sub-options; dedicated Transmute Lifeforce decision consolidating all 13 Lifeforce-to-Lifeforce conversions into a single option-list widget, decluttering Minor, Major, and Superior spellcasting grimoires.
- v1.20.79: Comprehensive Blood Mage lifestyle trait rebalance across all 3 tiers (Acolyte, Mage, Archmage) to standardized targets at 100 XP: Army Damage (15/30/50%), Army Maintenance (-15/-30/-50%), General Opinion (+10/+20/+30), Capital Development Growth (+0.25/+0.50/+1.00), Devotion Impact (+25/+50/+100%), Flat Piety (+2/+5/+10/mo), Piety % (+30/+60/+100%), Dynasty Renown (+1/+2/+3/mo), Life Expectancy (+50/+100/+200 years), Hostile/Personal Scheme Potential (15/30/50%), and removed Knight Effectiveness per Learning; apply supernatural hair and eye appearance game rules across all tiers.
- v1.20.78: Fix error.log script issues: repair ascension duel mirror traits, restore Blood Crucible modifier to Blood Blessing, and fix decision debug logging.
- v1.20.77: Add knight effectiveness per Prowess/Learning and monthly Piety per knight across Bloodlust & Enlightenment tracks, Warband & Mastery house covenants, Duchy Blood Temples, and Domicile Blood Shrines.
- v1.20.76: Replace non-functional monthly income per devotion level on Blood Mage bloodline track and base traits with flat monthly income (+0.5 to +4.5/mo) and direct domain limit expansion (+1 to +4 holdings); restore full cumulative track milestone benefits up to 50 XP (and 100 XP for Ancient) into base traits of Blood Mage and Blood Archmage to eliminate power loss on tier elevation.
- v1.20.74: Complete Specialized Lifeforce Reservoirs triad with Blood Fury (+2 prowess, +10% knight effectiveness, +2% army movement speed, +2 travel safety) and Blood Focus (+1 learning, -10% stress gain, +5% monthly lifestyle XP gain); add Minor/Major transmutation and reclaim decision loops; decouple prowess from Superior Lifeforce so core reserves strictly govern immortality and vitality; update story panel counters; remove Lifeforce requirements and consumption from Ascend Blood Magic Tier decision; de-duplicate Bloodlust (+1 Knight Limit at 10/30/50/70/100, +3 base on Mage, +6 base on Archmage) and Warband (+10% to +50% Men-at-Arms counter efficiency, +1 to +4 regiment size, +1 to +2 regiments).
- v1.20.73: Bidirectional Lifeforce Transmutation: condense Minor into Major and Major into Superior; split Superior into Major and Major into Minor.
- v1.20.72: Trim Blood Mage trait track tooltips to 2–3 unique benefits; introduce stackable Mojo Lifeforce subsystem for active fertility and congenital inheritance; convert Minor/Major to Mojo and grant to kin or consume at childbirth; centralize Plague Resistance on Lifeforce reserves (+2 / +6 / +12); grant Domain Limit to Bloodline and Personal Tenet Slots to Ancient.
- v1.20.71: Mirror player stats and traits in ascension duel; native toast polish; universal track XP progression.
- v1.20.70: Rebalance Bloodlust track (replace flat Martial/Prowess with Advantage, Knight Effectiveness, and Knight Limit); move Dread Baseline to Hematurgy track; add devotion prowess to Mage (+1) and Archmage (+2) base stats; remove redundant age lock from higher tier tracks; allow Blood Acolytes and Archmages to take up the Blóðtrú faith.
- v1.20.69: Sequential 3-Tier Hierarchy: Blood Acolyte (Tier I), Blood Mage (Tier II), Blood Archmage (Tier III) with standardized 6-track progression; blank-slate elevation with overflow Lifeforce extraction; anti-nerf base stat floors; Sanguine Distillation rite; Crimson Mirror non-lethal battlefield ascension duel vs self-clone.
- v1.20.68: Consolidate Blood Knight into Blood Mage trait as the new 6th track 'Bloodlust' (prowess, martial, advantage, knight limit, and dread baseline); grant all Blood Mages Worthy Commander army gender exemption; unify battlefield and single combat XP gain; clean up UI and retire separate Blood Knight trait; old saves are not supported (breaking change)
- v1.20.66: Blood Mages can initiate Blood Knights alongside Knights; add human-only Superior Magic class transmutation in Cast Superior Blood Magic (preserving Ancient, Enlightenment, and Benediction track XP); fix AI modal interaction execution and add comprehensive debug logging across all decisions and interactions
- v1.20.65: Add custom Alþingi Commonwealth and Verbúðir traditions to Icelandic culture; standardize Icelandic names and ethos; exempt Blood Knights from gender warfare restrictions to serve as knights and commanders
- v1.20.64: Add playable Icelandic culture with equal martial custom, saga name lists, and modular game start setup gated by campaign game rule (on by default)
- v1.20.63: Align House Covenants (7 to 6) and Blood Power (6 tracks); universal monthly Piety and 1:1 Devotion attribute scaling; yearly covenant pulse feeds matching Blood Power tracks
- v1.20.62: Standardize event exits to "Back"; reduce manifest/rune/hunt cooldowns; lower Blood Berserker provision cost
- v1.20.61: Restructure Manifest Congenital Traits (Ranks 1–3 in Major, Ranks 4–5 in Superior with 3/4/5/6/7/8 XP scaled by trait rank); unify positive interactions into Blood Blessing and hostile harvesting into Blood Drain; rename Heal Affliction to Heal Healing
- v1.20.60: Rebalance Ancient and Enlightenment XP; Condense Lifeforce grants Enlightenment XP; AI always selects initial Lifeforce attunement; alerts for prisoner lifedrain and culling champions; require 20+ Prowess for Cull Champion
- v1.20.59: Blood Temples become duchy-capital buildings in all duchies
- v1.20.58: Add Blood Berserkers and Blood-Bound Behemoths regiments
- v1.20.57: Merge blessing interactions into one Bless Blood; declutter menus
- v1.20.56: Blood Hunt cooldown inverted: 1 year landed, 3 wandering
- v1.20.55: Old-age traits get progressive rejuvenation interaction
- v1.20.54: Rebalance track XP sources for Blood Knights and Mages
- v1.20.53: Cast Blood Magic becomes inline option-list widgets
- v1.20.52: Remove passive yearly Enlightenment XP on Blood Knights
- v1.20.51: Blood Knights initiate kin; Blood Hunt gets tiered encounters
- v1.20.50: Add Consecrate Union, Empower Blood Mage, Siphon, Red Art duel, Sworn-Guard, events
- v1.20.49: Seek Power becomes Go on a Blood Hunt for both paths
- v1.20.48: Blood Power tracks move to 10/20/50/100 XP cadence
- v1.20.47: Blood Empowerment renamed Blood Power
- v1.20.46: Rune inscription options show only at correct tier
- v1.20.45: Blood Power tracks and milestones overhauled
- v1.20.44: Custom icons for all five Galdrastafir staves
- v1.20.43: Staves moved to standalone Carve Galdrastafir decision
- v1.20.42: Attune widget, rebalanced Manifest and Condense duels
- v1.20.41: Manifest Lifeforce Piety popup; childbirth Major Lifeforce
- v1.20.40: Add Blood Runes and five Galdrastafir staves
- v1.20.39: Blood Knight becomes full peer lifestyle to Blood Mage
- v1.20.38: Healing alerts in Current Situation
- v1.20.37: Situation decisions mirrored in Decisions tab
- v1.20.36: Blood Knight icon, domicile buildings, duel Lifeforce rewards
- v1.20.35: Simplify magic tiers; scale battle XP and Lifeforce
- v1.20.34: Blood Knight situation tab, prevalence rules, error fixes
- v1.20.75: Raise default Level of Devotion cap to 8 (Divine, Demigod, Godlike accessible globally)
- v1.20.74: Specialized Lifeforce Reservoirs (Blood Fury & Focus), 5-milestone core trait consolidation, and tier ascension Lifeforce requirement removal
- v1.20.73: Bidirectional Lifeforce transmutation (condense Minor/Major, split Superior/Major with 6-month cooldowns)
- v1.20.63: Align and streamline House Covenants and Blood Power across six mirrored tracks; cap Blood Power at 4 core personal modifiers per track, moving devotion and prestige scaling, domain limit, opinion, and Men-at-Arms bonuses into House Covenants
- v1.20.32: Overhaul Bloodline and Hematurgy tracks
- v1.20.31: Standalone Blood Knight trait with unified healing events
- v1.20.30: Add Egill Skallagrímsson bookmark character
- v1.20.29: Blood Knights cast minor magic and seek power
- v1.20.28: Add Superior rites and Egill duel integration
- v1.20.27: Rebalance Blood Mage tracks; cap opinion bonuses
- v1.20.26: Rebalance Blood Empowerment tracks
- v1.20.25: Major ritual manifests congenital traits
- v1.20.24: Add Superior Lifeforce; required for Blood Golems
- v1.20.23: Merge cast decisions into Minor and Major grimoires
- v1.20.22: Rename Crimson and Sanguine entities to Blood
- v1.20.21: Illness, lifedrain and duchy building fixes
- v1.20.20: Self-cast magic returns to Decisions tab
- v1.20.19: Refine Blood Knight popup interaction
- v1.20.18: Add Blood Shrine building chain
- v1.20.17: Add blood magic debug logging
- v1.20.16: Add standalone Crimson Warrior trait
- v1.20.15: Add agent token-cost check and style rules
- v1.20.14: Harvest Lifeforce from single combat
- v1.20.13: Minor lifedrain repeatable; manifest Lifeforce unrestricted
- v1.20.12: Standardize holy site modifiers; add debug interactions
- v1.20.11: Split East Asian faith into Xuédào and Ketsudō
- v1.20.10: Rename religion family and core faith to Blóðtrú
- v1.20.9: Consolidate Blóðtrú with Ancestor Worship tenet
- v1.20.7: Add Reykjavik duel decision against the hermit
- v1.20.6: Streamline docs and agent rules
- v1.20.5: Add repo format checks; fix religion script
- v1.20.4: Fix trait syntax; update descriptor
- v1.20.3: Reorganize decision and agent rules
- v1.20.2: English-only localization source
- v1.20.1: CK3 1.20 compatibility and layout modernization
- Pre-1.20: Migrate to CK3 1.19 layout; interactions replace decisions for targeted magic (15.37)
- 15.25: Cultist conversion, Ancient track, crimson warriors, more toasts
- 15.20: Track-based traits; major/minor Lifeforce; Channel Lifeforce decision
- 15.15: Unreformed religion, more holy sites, white eyes for Blood Mages
