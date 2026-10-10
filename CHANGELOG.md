# Changelog

## Living changelog (branch net state since 1.20)

Always reflects current branch state. Simple line per PR merge. Superseded changes folded, reverts dropped. Caveman style.

- PR #95: CK3 1.20 baseline compat, layout modernization, AI agent rules.
- PR #97: English-only localization source. Drop non-English stubs for auto-generation.
- PR #98: Reorganize decision and AI agent rules.
- PR #99: Trait definition syntax fixes, descriptor update.
- PR #100: Pre-commit repository format checks, religion script fixes.
- PR #101: Streamline agent rules documentation.
- PR #102: Reykjavik duel decision to challenge occult hermit.
- PR #103: Consolidate Blóðtrú faith with Ancestor Worship tenet.
- PR #105: Rename religion family and core faith to Blóðtrú.
- PR #106: Split East Asian branch into Xuédào (Chinese) and Ketsudō (Japanese) faiths.
- PR #107: Standardize holy site modifiers. Add debug interactions.
- PR #108: Repeatable minor lifedrain. Unrestricted manifest lifeforce.
- PR #109: Lifeforce harvest from single combat duels.
- PR #110: Agent token cost pre-commit check. Add caveman skill.
- PR #113: Debug logging for blood magic operations.
- PR #114: Blood Shrine building chain for holdings and domiciles.
- PR #118: Keep self-cast blood magic in decisions tab.
- PR #119: DRY triggers, illness/drain bugfixes, fix duchy building typo.
- PR #120: Rename Crimson and Sanguine entities to Blood across mod.
- PR #121: Consolidate self-magic decisions into Minor and Major hub events.
- PR #122: Add Superior Lifeforce tier; require for Blood Golem creation.
- PR #123: Major channel ritual to manifest congenital traits.
- PR #124: Rebalance blood empowerment tracks. Standardize trait baselines.
- PR #125: Rebalance blood mage tracks, cap opinion bonuses, normalize economic scaling.
- PR #126: Superior blood magic rites, Egill duel integration, runtime error fixes.
- PR #127: Allow Blood Knights to cast minor blood magic and seek power.
- PR #128: Add historical Egill Skallagrímsson character bookmark.
- PR #129: Redesign Blood Knight as standalone lifestyle trait (Slaughter, Vanguard, Resilience) with elevation bridge; rework healing to unified event flow; redistribute track XP.
- PR #130: Restructure Blood Mage and Blood Knight trait tracks: 3 shared (Ancient, Benediction, Enlightenment), 2 Mage exclusive (Bloodline, Hematurgy), 2 Knight exclusive (Vanguard, Slaughter); align elevation conversion and XP sources.

## Historical (pre-1.20)

* Migrated religion definitions to the CK3 1.19 folder structure.
* Updated duel, decision AI, trait, and character-template definitions for the 1.19 parser.
* Replaced duplicate and inline localization keys with mod-scoped localization.

## 15.37
* Changed decisions targetting player, into character interactions instead: Blood Rune / Education / Crimson Empowerment / Attune Lifeforce / Channel lifeforce
* Lots of testing, to make sure AI uses the interactions, some they weren't doing before
* Convert from witch to blood mage, no longer used by AI, to allow for witches and compatibility with Witchcraft mod
* Lowered chance of AI taking up blood cultist faith to 5% yearly, felt it was happening too frequently
* Minor lifedrain now has a 6 month cooldown for balance/AI reasons
* Mass lifedrain (that AI sometimes uses) skips dynasty members by default, to avoid them getting kinslayer trait
* Attunement grants small bonuses, around 2x what 10xp in the track would give
* Lowered cost of blood runes to 0/200/400 instead of 100/500/1000
* Blood golem slightly less OP, with 5 in all stats and 15 in prowess
* New thumbnail

## 15.36
* Can become blood mage, if you have a prisoner that's a blood mage, by consuming their flesh.
* Can heal weak and one legged as well
* AI Prioritise self, for casting positive magic
* Golems are beardless albinos

## 15.35
* Can convert friend/soulmate/consort/family to cult
* Various decisions have XP requirements now: Enhance and new Education / manifest lifeforce / create blood golem / blood rune
* Removed channel major, and replaced with new Trait: Crimson Empowerment
    * Cast Lifeforce, to gain 10xp in one of 7 tracks, each 10xp gives a differnt bonus
    * Tracks are based around diplomacy/martial/stewardship/intrigue/learning/genetics/lifestyle xp gain
* Blood cost (piety / xp level) scales with which rune you have
* Levelling up education, cost and xp scales with eduation level

## 15.34
* Converting others to blood mages, now can be done with a hook
* Tweaked piety level requirements for all decisions
    * blood runes: lvl 2
    * channel: lvl 1
    * education: lvl 2 to improve, lvl 3 for new one
    * manifesting: lvl 2
* Piety level only reduced for runes and chance to happen with education
* Piety now generally more expensive
* Enhance lifeforce removed (not fun)

* Can now get new education trait, if we have level 5
* Golem attributes cost scaling amounts of piety, no longer grant bloodline XP for each attribute added, and cannot continue without piety
* Lots of AI balances, so AI considers relationship with target and it's own health before doing actions

## 15.33
* Character interactions dont trigger events, if there's only one outcome (blood cult + drain lifeforce), instead show up in the character interaction
* Creating golem traits cost piety each time
* New decision: Manifest lifeforce, at great cost of piety
* Balance dynasty/major modifiers, generally stronger
* Balance blood mage trait, generally stronger
* Golems belong to same dynasty/house

## 15.32
* New decisions: Enhance lifeforce, to convert minor to major (later removed)
* New Blood Mage icons for modifiers (white)
* Can level up education with decision, at high cost of piety
* Can create blood golem, high prowess courtiers, at high cost to piety

## 15.30
* Healing pox more costly (piety + major & minor lifeforce)
* Channelling decisions, show potential modifiers before casting decision
* New decision: blood runes for chance to get yearly lifeforce (minor or major, depends on rune level)
* Wandering characters, can seek power every 1 year, instead of 2 to balance (easier to get lifeforce for landed)
* Bloodline xp yearly, scales with number of dynasty modifiers

## 15.29
* Balance blood mage trait, all tracks negate prowess loss at 100xp
* Balance dynasty/major modifiers, more x_per_piety_level now
* AI chooses attunement, based on XP levels
* Seek power wanderer, can have traits, some drainable. Can also join the player's court
* Major channelling can only be done if piety level is positive
* Drain trait harder, the more traits you have + 6 month cooldown
* LLM context updated: more modifiers

# 15.25
* Cultists can become blood mages, with decision and wise versa
* Trait, modifier and holy site balancing
* Attune lifeforce, chance to get extra XP per year
* New ANCIENT track in trat, 1xp per year, for rewarding long living characters
* Channel minor lifeforce, for temporary bonuses
* More interface toasts, to get feedback on what happened
* Can only convert courtiers/prisoners to cult
* Create crimson warriors/champions, granting knights extra prowess

# 15.20
* Update trait to new format, with tracks
* Seek power event/decision, rather than stroll through town (better theme with wandering)
* Split lifeforce into major/minor. Minor draining doesn't kill
* Granting lifeforce, reverts minor lifedraining
* Update icon graphics
* Add LLM RAG documents for context
* Create channel (major) lifeforce decision, strong permanent buffs for self or dynasty
* Create .pre-commit-config.yaml

# 15.15
* Religion unreformed, and syncs with christians (less hate)
* Add more holy Sites, and each grant +1 skill
* Mass drain needs prisoners
* Can spend minor lifeforce to convert to cult
* Blood mages can convert to cult
* Blood mages have white eyes
* Decisions show up in own group (#30)
