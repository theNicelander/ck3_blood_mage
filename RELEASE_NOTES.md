# Blood Mages — Release Notes (v1.20)

Net player-facing changes since v1.15 (2025 baseline), grouped by feature area. Version history is at the bottom.

---

## Blood Mage & Blood Knight

- Two permanent, mutually exclusive lifestyle paths chosen on awakening: **Blood Mage** (realm, dynasty, dread, domain) and **Blood Knight** (prowess, combat advantage, knights, army speed).
- Awaken via bloodline, occult mentorship, witch conversion, Blood Knight mentorship (also from imprisoned Blood Knights), or by duelling the hermit **Egill Skallagrímsson** in Iceland or Tsushima.
- Shared Devotion tracks (Ancient, Enlightenment, Benediction) scale to 100 XP: Ancient adds +1 personal tenet slot per 20 XP.
- 50 XP milestones scale with Devotion Level; 100 XP capstones give +50% Devotion Impact, Age Prowess Lock and +2.0 skill per Devotion level.
- Blood Mage tracks Bloodline and Hematurgy: 10-step cadence (taxes, trait inheritance, dynasty prestige, hostile scheme power and defence).
- Blood Knight tracks Vanguard (army speed, advantage, supply, prowess) and Slaughter (prowess, knight limit and effectiveness).
- Blood Knights can initiate spouse, children and kin (+5 Vanguard XP for dynasty), and empower family even if landed or outside their court.
- **Blood Power** secondary trait with six tracks (Dynasty, Fury, Mastery, Presence, Prosperity, Shadows) on a 10/20/50/100 XP cadence; every 10 XP adds flat monthly lifestyle XP in the matching skill.
- Track XP sources rebalanced: healing grants Benediction, family rites and childbirth grant Ancient/Benediction, congenital manifestation grants XP by attribute.
- Regiments: **Blood Berserkers** (heavy shock infantry, Devotion 2+) and **Blood-Bound Behemoths** (siege-capable monsters, Devotion 4+), Piety-maintained.
- Crimson Sworn-Guard court position and Crimson Warrior champions.

## Lifeforce

- Three tiers: **Minor** (health, disease resistance), **Major** (lifespan, body rituals), **Superior** (Blood Golems, capstone runes).
- **Manifest Lifeforce**: four Piety tiers (250–1,500), no cooldown.
- Blood Knights harvest Lifeforce from battles (by battle size) and lethal single combat.
- Blood Mage and Blood Knight mothers yield Major Lifeforce on safe childbirth.
- **Bleed Own Veins**: self-interaction (1-year cooldown) for Minor or Major Lifeforce at the cost of wounds, stress and drain.
- **Siphon Stored Lifeforce** takes Minor/Major/Superior reserves from other characters via a contest.
- **Contest of the Red Art**: Learning + Prowess duel between Blood Mages and Blood Knights.
- **House Head Blood Tithe** levies Lifeforce from adult kin.

## Spellcasting & Decisions

- Cast Blood Magic (Minor, Major, Superior) are inline option-list decisions; every spell stays visible, grayed out when unavailable.
- **Minor**: Attunement, Minor Blood Runes, Cleansing, Condensation.
- **Major**: Channel Blood Power, Condense into Superior Lifeforce, Education Enhancement, Major Runes, Congenital Manifestation, House Blessing.
- **Superior**: Blood Golem creation, 5★ Master Educations, Secondary Educations, Capstone Runes.
- **Attune Lifeforce**: choose your yearly lifestyle XP bonus (applied January 1st).
- **Empower Dynasty Bloodline**: seven three-tier House Covenants (Majesty, Warband, Prosperity, Shadow, Insight, Legacy, Mastery).
- Education advancement needs Devotion Level 1+/2+/3+/4+ for 1★→2★ … 4★→5★; only Superior magic (5★, Embrace New Education) costs Devotion or needs 1000 Piety plus Superior Lifeforce.
- **Heal Ailment**: cures up to 32 ailments, purges all 11 stress vices (−50 Stress), and treats old-age traits (Minor: 1 Minor Lifeforce + 50 Piety; Major tier for deeper rejuvenation).
- **Influence Personality**: Learning contest to swap a trait or culture (5-year cooldown on success, 1 year on failure).
- Personality Reshaping and Congenital Manifestation (up to rank 5).

## Blood Hunt

- *Seek Power* became **Go on a Blood Hunt**, open to Blood Mages and Blood Knights; grayed out while travelling, in an activity, imprisoned or incapable.
- Cooldown: 1 year landed, 3 years wandering (halved with Superior Vegvísir).
- Encounters scale with Prowess: Beast's Lair, Blood in the Embers, Edge of the Woods, Crimson Rite, Stag's Last Stand, Blades on the Lonely Road, Cairn of Forgotten Carnage.
- Roughly 60% success at skill 20, 70% at 25, 80% at 30, 95% at 40+; peaceful options exist for most encounters.
- Road encounter can include a sworn escort champion to duel (Prowess 25+).

## Blood Knight Rites

- **Bless Blood**: consecrate knights and kin (+2 Martial, +4 Prowess, +25% Knight Effectiveness for 10 years).
- **Crimson Sparring Ring** (yearly, 1 Minor Lifeforce): practice duels; winner gains 1 Major Lifeforce, both gain Blademaster XP.
- **Cull Fallen Champion**: sacrifice broken or captured warriors for Major Lifeforce, with a chance of Superior.
- **Anoint Champion / Anoint Heir**: permanent bonuses; anointed heirs awaken with a Lifeforce transfer on succession.
- Overlapping blessing interactions merged into one 4-option Bless Blood; options hide once active.

## Galdrastafir & Blood Runes

- Five Icelandic staves carved into the flesh, each with an ambient Lifeforce pulse: **Vegvísir** (travel), **Ægishjálmur** (terror, knights), **Feingur** (fertility), **Nábrókarstafur** (gold), **Hulinhjálmur** (schemes, concealment).
- Superior rune depth unlocks the standalone **Carve Galdrastafir Stave** decision.
- Inscribe blood runes on sworn knights, champions and family.
- Custom icons for all staves, traits, tracks, interactions and faiths.

## Blood Golems & Dynasty

- Forge immortal albino golems with Superior Lifeforce and a shaping duel; they join the dynasty as cadet house `bm_house_golem`.
- Seven house modifiers stack realm-wide bonuses to fertility, health, prowess and administration.
- **Bless Bloodline** (children, kin, knights) with role-specific blessings.
- **Anoint Heir in Blood**: permanent stats, opinion and short-reign bonuses.
- **Consecrate Union**: spouse/lover/consort gain +50% fertility and better genetic inheritance (Minor 3 years, Major 10 years).
- **Empower Blood Mage**: peer interaction advancing Enlightenment and Bloodline tracks.

## Blóðtrú Religion

- Three faiths: **Blóðtrú** (Norse/Germanic), **Ketsudō** (Japanese), **Xuédào** (Chinese).
- Ancestor Worship tenet earns piety, renown and defence; Mendicant Preaching replaces Ritual Celebrations.
- All 58 Blóðtrú, 27 Ketsudō and 32 Xuédào holy sites are now Eminent Holy Sites (up to 80 active), granting smaller stacked global faith bonuses alongside local county holder modifiers.
- Reformation repair decision resolves holy-site locks when creating custom faiths.
- Blood Mage and Blood Knight are no longer religion virtues.

## Buildings

- **Blood Temples**: seven-tier duchy-capital buildings (Altar → … → Acropolis), available in all duchy capitals including tribal; tiers I–IV open to more holders.
- **Blood Shrine**: five-tier line for camps and estates (up to +2.5 monthly piety at Tier V, plus health, lifespan and inheritance).

## Interface & Interactions

- **Blood Magic Situation panel**: discipline, track XP, Lifeforce, stave, and rosters of dynasty Blood Mages, Blood Knights and Golems.
- All mod interactions grouped in a "Blood Magic" context-menu section; outcomes shown in interface toasts.
- Current Situation alert when a kinsperson or courtier can be healed.
- **Purge Stress Vices** burns away all 11 coping traits.
- Hulinhjálmur conceals the caster from discovery penalties on failed siphons and curses.

## Narrative Events

Annual pulse (3-year cooldown) for player Blood Mages and Blood Knights:
- **A Drop on the Lips**: bless a lover or spouse, or awaken them.
- **The Fever of Awakening**: guide or hasten a child's (6–15) awakening.
- **The Red Banquet After Battle**: feast, claim the harvest, or consecrate the field.
- **Echoes in the Clay**: shield an heir, grant Blademaster, or siphon the golem.
- **The Whispering Sanctum**: drain, bribe or disperse an intruding courtier.

## Visuals & Game Rules

- Eyes progress from red to crimson, pale and white; hair bleaches to white.
- Rules: Appearance (Off / Gradual / On), Blood Mage and Blood Knight Prevalence, Blóðtrú Availability, Historical Starting Counties, Initiation Faith Requirements, Lore Integration (vanilla vs AGOT).
- Fully modular (`bm_` prefix), no vanilla overwrites; compatible with total conversions.

## Bugfixes

- Reverse Lifedrain: self-targeting works for characters drained by Bleed Own Veins.
- Fixed decision dialogs not opening and "Inscribe Blood Rune" missing from menus (duplicate BOM).
- Fixed raw "(NUM)" in healing alerts and `ERROR:[Minor]` in covenant buttons.
- Fixed tooltip scoping errors in Consecrate Union and Siphon Stored Lifeforce.
- Fixed golem rite option visibility and heirless-character crashes in rune interactions.
- Empower Dynasty tooltip no longer claims a house loses an old modifier.
- Removed passive yearly Enlightenment XP on Blood Knights.
- Added missing toast and loc keys; removed dangling modifier references.

---

## Version history

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
