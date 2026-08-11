# Changelog - Highlights

## Unreleased

* Added a Blood Mage Prevalence game rule with Player Only, Extremely Rare, Rare, Uncommon, Default, and More Frequent settings. It scales AI initiation decisions and interactions, controls naturally generated and inherited Blood Mage retention, adjusts newborn prevalence, and keeps the existing behavior as the default.
* Added a Blood Mage Appearance game rule with No Alteration, Eyes Only, and Eyes and Hair settings. Eyes and Hair preserves the existing transformation as the default, and all supported languages include the new rule text.
* Updated Blood Mage healing for every CK3 1.19 age-related ailment: Heal Ailment now cures Withering Mind, Clouded Eyes, and Fragile Bones alongside Infirm, while Heal Deadly Ailment cures Faltering Heart.
* Added a game rule that makes the Blood Cultist initiation ritual require a dedicated Blood Magic cult faith or additionally allow faiths with Witchcraft Accepted, with the strict dedicated-cult mode as the default, and completed the hidden cult identity doctrine's UI metadata.
* Added a dedicated, icon-backed Blood Mages game-rule category and a Blood Mage Lore rule with Historical and A Game of Thrones settings for the optional AGOT religion companion.
* Corrected mistranslated religious terminology, dynamic substitutions, and duplicated legacy text across the supported non-English localizations.
* Renamed the religion game rule to remain accurate with optional native faith integrations, expanded the Cult of the Quintessence religion-family description, and refreshed religion localization across all supported languages.
* Added a hidden Blood Magic identity doctrine and taught cult eligibility to recognize the shared `blood_magic_cult_faith` parameter, allowing optional religion integrations without static dependencies.
* Retained all seven standalone Cult of Quintessence heritage faiths and added automatic conversion routing for Christian, Islamic, Jewish, Eastern, Sinitic, Ásatrú, and other unreformed origins, with a documented Christian Syncretism fallback.
* Moved native-religion integration, including the Cult of the Crimson Ka, into the optional Blood Mages - Vanilla Religions submod so the main mod no longer overlays vanilla religions.
* Moved the Blood Magic story panel, progression display, and lifecycle initialization into Blood Mages so compatibility submods only extend the base-owned panel.
* Added exact Major/Minor Lifeforce stack counts and independently collapsible, scrollable Blood Golem and Crimson retinue rosters after the Blood Magic decisions, with compact empty states, atomic story creation across every Blood Mage acquisition path, missing-story reconciliation when Situations opens, automatic refresh, and a compact standard refresh control on each roster.
* Added inline mechanic tooltips to the Lifeforce and Attunement status lines.
* Condensed the five discipline counters into a two-row grid with their dedicated trait-track icons.
* Fixed folded and empty character rosters retaining the expanded scroll-area height while preserving expandable content, and completed the refresh control's fade-out/fade-in cycle.

## 1.19 compatibility
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
