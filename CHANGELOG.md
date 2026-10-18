# Changelog

## Game version 1.20

- v1.20.48: Overhaul all 5 Blood Power tracks into a 10/20/50/100 XP stepping-stone cadence with Devotion-scaling skills (+1 at 50/100), personal scheme speed/success, holding & domicile build cost cuts, fertile years on 20s, and expanded domain/scheme limits; overhaul Harmonize Nature into Influence Personality with a Learning duel (50% base, capped at 95% at +20 difference), no opinion bonus, no Cast Major Blood Magic debuff, 1-year failure cooldown vs 5-year success cooldown, and fix root.Self localization bug; fix education enhancement and mastery option visibility by hiding unowned disciplines to prevent UI option cutoff.
- v1.20.47: Rename secondary lifestyle trait Blood Empowerment to Blood Power (lifestyle_blood_power), update Major Grimoire option to Channel Blood Power (bm_cast_blood_magic_major.001.power), rename trait and event files to bm_blood_power_trait.txt and bm_blood_power_event.txt, add add_blood_power_xp effect and bm_has_blood_power_xp_trigger with backward compatibility aliases, and update all localizations, debug decisions, and architecture documentation.
- v1.20.46: Fix blood rune inscription options across minor, major, and superior magic to only display when at the appropriate progression tier and hide once superseded; integrate Galdrastafir stave carving and swapping into Cast Major Blood Magic Grimoire (bm_galdrastafir.001) with free initial carve and 500p + Major Lifeforce swapping; remove obsolete standalone stave decision from Situation panel; institutionalize 'Nothing hidden, but often unavailable' (always show grayed out) philosophy across repo rules and skills; revamp all 5 Blood Empowerment trait tracks with high-impact, focused bonuses per step and powerful 50/100 XP capstones (Dynasty: +40% Inactive Inheritance & Trait Strengthening, -50%/-100% Inbreeding Immunity, +25% Renown; Mastery: +40% Lifestyle XP, +3 Language Cap, +2 Personal Schemes, Ignore Negative Culture Opinion; Presence: +24 General Opinion, -40% Stress Gain, +25% Fame Impact, -25% Short Reign, +25% Long Reign; Prosperity: +40% Income, -32% MaA Maintenance, +4 Domain Limit, +3 MaA Regiment Size; Shadows: +40 Hostile Scheme Success, -40 Enemy Hostile Scheme Success, -50% Enemy Max Scheme Cap, +15% Own Max Scheme Cap, +2 Hostile Schemes); overhaul Empower Dynasty Bloodline into standalone inline option-list widget decision (bm_empower_bloodline_decision) with 7 Three-Tier House Covenants (Awakened, Ascendant, Sovereign: Majesty, Warband, Prosperity, Shadows, Insight, Legacy, Expertise); assign distinctive trait level track DDS icons to all 21 house covenant modifiers; remove obsolete legacy un-suffixed dynasty house modifiers and fix Tier 1 covenant preview tooltip falsely displaying loss of old modifier; scale yearly house bloodline XP pulse by covenant tiers (+3%/+6%/+10%) for both Blood Mages and Blood Knights; remove legacy bloodline event from Major Grimoire; streamline Major Blood Magic Blood Empowerment option tooltip with interactive Lifeforce, Piety, and Blood Empowerment links and 50/100 XP milestone notes; gate Cast Major Blood Magic decision behind requiring at least 150 Piety (piety >= 150) without consuming it; add show_as_unavailable to all blood magic events across the mod (Grimoires, Purge Impurities, Blood Empowerment, Education enhancements, Manifest Congenital Traits, Blood Golem creation, Seek Power, Trait Drain, and Heal Ailments) so every option remains visibly grayed out with requirement tooltips instead of being hidden; unify Blood Knight hair progression with Blood Mages into progressive white hair, removing golden blonde modifiers; fix double UTF-8 BOM headers causing silent decision failures on Seek Power, Channel Blood Empowerment, and Inscribe Blood Rune; fix localization trailing quote token syntax error; fix Current Situation healing group label removing raw (NUM) token, streamline healing notification to concise Lifeforce spending text, and enforce concise and direct Lifeforce wording over fluffy flavour across rules and skills; expand check_repo.py with multi-BOM, embedded BOM, and YAML syntax validation; overhaul Seek Power 'A Lost Soul' wilderness encounter (seek_power.003) promoting Friendly Brawl to first option, restricting Battlefield Duel to player prowess >= 25, gating traveler recruitment on learning superiority and knight recruitment on prowess superiority with a prowess duel, and redesigning the traveler into a warrior-poet archetype with elevated learning (10-18) and local county faith spawning; encapsulate outcome effects (Lifeforce, XP, courtier recruitment, stress, and recounts) directly into send_interface_toast blocks across combat rewards, interactions, events, and covenants while dropping static custom_tooltips to restore native engine toast tooltips and icon rendering; codify toast encapsulation in scripting rules; organize all 17 mod gameplay character interactions into dedicated 'Blood Magic' category (interaction_category_bm_blood_magic, index 16) with crimson header accent; fix Empower Dynasty Bloodline house scoping on unlanded/lowborn characters (house ?=), replace culture-only cultural_acceptance_gain_mult with character-compatible cultural_head_acceptance_gain_mult on Arcane Insight house covenants, replace unknown is_ward_of trigger with has_relation_guardian in Harmonize Nature, fix lifeforce_major loc data system call, restore missing database holy site definitions for Hangzhou and Quanzhou in Xuédào faith, and remove duplicate Condense Lifeforce loc keys; public-facing living release notes document (RELEASE_NOTES.md), update-release-notes skill, and workflow rule integration.
- v1.20.45: Overhaul Blood Empowerment trait tracks, milestones (50/100 XP Fame scaling, inbreeding immunity, MaA caps, extra personal/hostile schemes, ignore faith/culture penalties), convert ritual into inline option-list widget decision; replace non-functional max piety cap with Devotion Impact (+50%) and +2.0 stat-per-devotion capstones on shared tracks; add radiant golden blonde hair and red eyes for Blood Knights; consolidate appearance game rule into Off, Gradual, and On (default).
- v1.20.44: Custom 120x120 DDS icons for all 5 Galdrastafir staves (Vegvisir, Aegishjalmur, Feingur, Nabrokarstafur, Hulinhjalmur) in modifiers and carve decision widget.
- v1.20.43: Decouple Rune Depth (ambient Lifeforce tick) from flat Superior Capstone Galdrastafir staves using inline widget decision (bm_carve_galdrastafir_decision); remove 15 tiered stave modifiers, flay rites, and blood runes event chain; free initial stave choice with 5-year swap for 500 piety and Major Lifeforce; Reshape Personality interaction to purge and imprint personality traits; free initial lifeforce attunement with 3-year cooldown and 100 piety change cost; fix Seek Power event portraits, 3D staging triggers, and character names; grant base Blood Empowerment alongside Blood Mage/Blood Knight for UI pairing; replace Slaughter 50 devotion knights pseudo-modifier with native martial per piety level; rebalance Blood Knight and Blood Mage tracks (~30% stat reduction at max level, +100 Life Expectancy / +50 Years of Fertility target); add missing cooldown localizations for education enhancement, golems, runes, and rites; remove standalone blood golem creation decision in favor of Cast Superior Blood Magic grimoire; fix runtime script errors across Manifest Lifeforce scopes, Inscribe Rune on Others XP triggers and golem house checks, Seek Power toast effects and add_blood_mage_xp alias, and Geyser Duel unset variable.
- v1.20.42: Attune to trait track option-list widget, Seek Power Blood Knight escort duel, piety rank 4 & cooldown loc for blood golems, rebalance Manifest and Condense Lifeforce duel curves, clean 50/100 milestones with dynamic devotion knights & devotion impact, guaranteed yearly attunement XP, and Galdrastafir UI polish.
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
