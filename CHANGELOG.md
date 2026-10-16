# Changelog

## Game version 1.20

- v1.20.41: Manifest Lifeforce scaling piety popup, childbirth Major Lifeforce for Blood Mages, and restrict seek power to Blood Knights.
- v1.20.40: Blood Runes & Galdrastafir with 5 staves, sequential progression, superior capstones, and retinue inscription.
- v1.20.39: Blood Knight refactor into a viable lifestyle peer to Blood Mage with parallel Devotion.
- v1.20.38: Current Situation healing alerts, faith decision integration, and Blood Knight elevation polish.
- v1.20.37: Replicate Situation decisions in Decisions tab, AI targeting polish, and Blood Rune toasts.
- v1.20.36: Blood Knight trait icon, domicile buildings, major blood runes, and duel lifeforce rewards.
- v1.20.35: Magic tier simplification and battle XP and lifeforce scaling.
- v1.20.34: Blood Knight situation tab, prevalence game rules, and runtime error fixes.
- v1.20.32: Overhaul Bloodline and Hematurgy tracks, and consolidate debug character interactions.
- v1.20.31: Standalone Blood Knight lifestyle trait with elevation bridge and unified healing events.
- v1.20.30: Historical Egill Skallagrímsson character bookmark and geyser initiation rebalance.
- v1.20.29: Blood Knights cast minor blood magic and seek power.
- v1.20.28: Superior blood magic rites, Egill duel integration, and runtime fixes.
- v1.20.27: Rebalance blood mage tracks, cap opinion bonuses, and normalize economic scaling.
- v1.20.26: Rebalance blood empowerment tracks and standardize trait baselines.
- v1.20.25: Major channel ritual to manifest congenital traits.
- v1.20.24: Add Superior Lifeforce tier; require for Blood Golem creation.
- v1.20.23: Consolidate cast magic decisions into Minor and Major grimoire events.
- v1.20.22: Rename Crimson and Sanguine entities to Blood across mod.
- v1.20.21: DRY triggers, illness and lifedrain bugfixes, and duchy building fix.
- v1.20.20: Return self-cast blood magic to decisions tab and reorganize.
- v1.20.19: Blood Knight popup interaction refinement.
- v1.20.18: Blood Shrine building chain for holdings and domiciles.
- v1.20.17: Debug logging for blood magic operations.
- v1.20.16: Standalone Crimson Warrior trait.
- v1.20.15: Agent token cost pre-commit check and caveman style rules.
- v1.20.14: Lifeforce harvest from single combat duels.
- v1.20.13: Repeatable minor lifedrain and unrestricted manifest lifeforce.
- v1.20.12: Standardize holy site modifiers and add debug interactions.
- v1.20.11: Split East Asian branch into Xuédào (Chinese) and Ketsudō (Japanese) faiths.
- v1.20.10: Rename religion family and core faith to Blóðtrú.
- v1.20.9: Consolidate Blóðtrú faith with Ancestor Worship tenet.
- v1.20.7: Reykjavik duel decision to challenge occult hermit.
- v1.20.6: Streamline documentation and agent rules.
- v1.20.5: Pre-commit repository format checks and religion script fixes.
- v1.20.4: Trait definition syntax fixes and descriptor update.
- v1.20.3: Reorganize decision and AI agent rules.
- v1.20.2: English-only localization source and drop non-English stubs for auto-generation.
- v1.20.1: CK3 1.20 baseline compatibility, layout modernization, and AI agent rules.

## Historical (pre-1.20)

- Migrated religion definitions to the CK3 1.19 folder structure.
- Updated duel, decision AI, trait, and character-template definitions for the 1.19 parser.
- Replaced duplicate and inline localization keys with mod-scoped localization.

## 15.37

- Changed decisions targetting player, into character interactions instead: Blood Rune / Education / Crimson Empowerment / Attune Lifeforce / Channel lifeforce
- Lots of testing, to make sure AI uses the interactions, some they weren't doing before
- Convert from witch to blood mage, no longer used by AI, to allow for witches and compatibility with Witchcraft mod
- Lowered chance of AI taking up blood cultist faith to 5% yearly, felt it was happening too frequently
- Minor lifedrain now has a 6 month cooldown for balance/AI reasons
- Mass lifedrain (that AI sometimes uses) skips dynasty members by default, to avoid them getting kinslayer trait
- Attunement grants small bonuses, around 2x what 10xp in the track would give
- Lowered cost of blood runes to 0/200/400 instead of 100/500/1000
- Blood golem slightly less OP, with 5 in all stats and 15 in prowess
- New thumbnail

## 15.36

- Can become blood mage, if you have a prisoner that's a blood mage, by consuming their flesh.
- Can heal weak and one legged as well
- AI Prioritise self, for casting positive magic
- Golems are beardless albinos

## 15.35

- Can convert friend/soulmate/consort/family to cult
- Various decisions have XP requirements now: Enhance and new Education / manifest lifeforce / create blood golem / blood rune
- Removed channel major, and replaced with new Trait: Crimson Empowerment
  - Cast Lifeforce, to gain 10xp in one of 7 tracks, each 10xp gives a differnt bonus
  - Tracks are based around diplomacy/martial/stewardship/intrigue/learning/genetics/lifestyle xp gain
- Blood cost (piety / xp level) scales with which rune you have
- Levelling up education, cost and xp scales with eduation level

## 15.34

- Converting others to blood mages, now can be done with a hook
- Tweaked piety level requirements for all decisions
  - blood runes: lvl 2
  - channel: lvl 1
  - education: lvl 2 to improve, lvl 3 for new one
  - manifesting: lvl 2
- Piety level only reduced for runes and chance to happen with education
- Piety now generally more expensive
- Enhance lifeforce removed (not fun)

- Can now get new education trait, if we have level 5
- Golem attributes cost scaling amounts of piety, no longer grant bloodline XP for each attribute added, and cannot continue without piety
- Lots of AI balances, so AI considers relationship with target and it's own health before doing actions

## 15.33

- Character interactions dont trigger events, if there's only one outcome (blood cult + drain lifeforce), instead show up in the character interaction
- Creating golem traits cost piety each time
- New decision: Manifest lifeforce, at great cost of piety
- Balance dynasty/major modifiers, generally stronger
- Balance blood mage trait, generally stronger
- Golems belong to same dynasty/house

## 15.32

- New decisions: Enhance lifeforce, to convert minor to major (later removed)
- New Blood Mage icons for modifiers (white)
- Can level up education with decision, at high cost of piety
- Can create blood golem, high prowess courtiers, at high cost to piety

## 15.30

- Healing pox more costly (piety + major & minor lifeforce)
- Channelling decisions, show potential modifiers before casting decision
- New decision: blood runes for chance to get yearly lifeforce (minor or major, depends on rune level)
- Wandering characters, can seek power every 1 year, instead of 2 to balance (easier to get lifeforce for landed)
- Bloodline xp yearly, scales with number of dynasty modifiers

## 15.29

- Balance blood mage trait, all tracks negate prowess loss at 100xp
- Balance dynasty/major modifiers, more x_per_piety_level now
- AI chooses attunement, based on XP levels
- Seek power wanderer, can have traits, some drainable. Can also join the player's court
- Major channelling can only be done if piety level is positive
- Drain trait harder, the more traits you have + 6 month cooldown
- LLM context updated: more modifiers

# 15.25

- Cultists can become blood mages, with decision and wise versa
- Trait, modifier and holy site balancing
- Attune lifeforce, chance to get extra XP per year
- New ANCIENT track in trat, 1xp per year, for rewarding long living characters
- Channel minor lifeforce, for temporary bonuses
- More interface toasts, to get feedback on what happened
- Can only convert courtiers/prisoners to cult
- Create crimson warriors/champions, granting knights extra prowess

# 15.20

- Update trait to new format, with tracks
- Seek power event/decision, rather than stroll through town (better theme with wandering)
- Split lifeforce into major/minor. Minor draining doesn't kill
- Granting lifeforce, reverts minor lifedraining
- Update icon graphics
- Add LLM RAG documents for context
- Create channel (major) lifeforce decision, strong permanent buffs for self or dynasty
- Create .pre-commit-config.yaml

# 15.15

- Religion unreformed, and syncs with christians (less hate)
- Add more holy Sites, and each grant +1 skill
- Mass drain needs prisoners
- Can spend minor lifeforce to convert to cult
- Blood mages can convert to cult
- Blood mages have white eyes
- Decisions show up in own group (#30)
