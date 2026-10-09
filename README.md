# Blood Mages

## Local fork

This repository is an independent CK3 1.19 compatibility fork of [Blood Mages by Nicelander](https://steamcommunity.com/sharedfiles/filedetails/?id=3470491478). Relative to the original mod, it rebases religion, duel, decision-AI, trait, and character-template definitions for CK3 1.19; scopes duplicate localization keys; and adds portrait effects that evolve with Blood Mage mastery. The detailed gameplay history and local compatibility summary are in `CHANGELOG.md`.

This mod is for you if:

- You love playing a single character
- You want a way for your character to live forever, without being completely immortal
- You want your character to gain and level up positive physical traits (intelligent, beautiful, etc) in a way that feels part of the game

**Compatibility**: Uses namespaced content and does not overlay vanilla religion definitions. The
optional **Blood Mages - Vanilla Religions** submod provides native parent-religion integration for
players who prefer it and can accept religion-mod conflicts. Other mods can mark a faith as a Blood
Magic cult with the hidden `blood_magic_cult_faith` doctrine parameter; the provider remains
optional because Blood Mages does not reference its database identifiers.
The **Blood Mage Initiation Faith** game rule chooses whether the cultist initiation ritual requires
this dedicated marker or also permits characters whose faith accepts witchcraft.

The **Blood Mage Prevalence** game rule controls how readily Blood Magic spreads beyond player
characters:

| Setting | AI acquisition weight | Naturally generated/inherited AI traits retained |
| --- | --- | --- |
| Player Only | 0× | 0% |
| Extremely Rare | 0.01× Default | 10% |
| Rare | 0.10× Default | 40% |
| Uncommon | 0.50× Default | 70% |
| Default | 1.00× | 100% |
| More Frequent | 2.00× Default | 100%, plus increased newborn prevalence |

The acquisition multiplier scales each AI decision or interaction's existing weight; it is not an
absolute chance that every AI character becomes a Blood Mage. For example, the two annually checked
initiation decisions have a 10% Default AI chance when eligible, so Rare changes each to 1% and
Extremely Rare changes each to 0.1%. Character interactions also depend on valid targets, check
cadence, relationships, and their own willingness modifiers, so they do not have one universal
absolute probability.

The retention percentage is a separate one-time roll for AI traits assigned through natural
generation or inheritance. The rule does not reduce player access to Blood Mage decisions or
interactions. **Default**
preserves the mod's original balance, **Uncommon** provides a moderate reduction, and **Rare** and **Extremely Rare** are intended
for long campaigns where unrestricted AI propagation would otherwise saturate major dynasties.

The update is compatible with existing saves, which continue with **Default** behavior and do not
retroactively remove Blood Mages. Select a different prevalence setting when starting a new campaign.

Choose **Blood Mage Lore: Historical** for vanilla CK3. For AGOT, load the small optional
[**Blood Mages - AGOT Religions**](https://steamcommunity.com/sharedfiles/filedetails/?id=3775630683) companion after A Game of Thrones and Blood Mages, then choose
**Blood Mage Lore: A Game of Thrones**. The companion swaps out the vanilla-world cult database
for Westerosi traditions and holy sites without making AGOT a dependency of the main mod.

## Overview

Blood Mages drain **Lifeforce** from others to extend their own lifespan and cast powerful spells. This power can be used to heal, enhance abilities, absorb traits, and more, at the cost of their own health.

## Blood Mage Trait and Specialisation

The Blood Mage trait features five distinct tracks:

- **Ancient**: Survive
- **Enlightenment**: Strengthen yourself
- **Bloodline**: Strengthen your dynasty
- **Benediction**: Healing and strengthen others
- **Hematurgy**: Absorb traits and harvest lifeforce

Each track gains experience as you use related abilities, with ten progressive tiers of power. Maxing them all out might take you 100 years, costing tens of thousands of piety, and the benefits reflect that.

Blood Mages owns a Blood Magic story panel that tracks all five disciplines in
a compact two-row icon grid, the exact Major and Minor Lifeforce stack counts,
attunement, and the core
progression decisions. After those decisions it shows independently
collapsible, scrollable rosters for the Blood Golems and the Crimson
Warriors/Champions currently serving at the Blood Mage's court; an empty
roster collapses to a compact `None` row. Opening the Situations window repairs
a missing player story when necessary and refreshes the counters and rosters;
each roster has a small standard refresh button for manual updates. Lifeforce
and Attunement labels explain their resource and advancement rules on hover.

Compatibility submods can shadow the story definition at its exact virtual path
to add integration-only features without taking ownership of its lifecycle,
progression display, or roster implementation. The interactive roster control
requires a complete CK3 1.19.0.6 overlay of `gui/window_situation_list.gui`
because the vanilla story-cycle row exposes no additive widget hook. Generic
scripted-GUI contracts gate and refresh the custom renderer, allowing a later
compatibility submod to extend it without optional links in Blood Mages.

## Lifeforce System

Lifeforce is the fundamental resource for Blood Mages, that's primarily gained through draining other characters, such as prisoners or courtiers. Other ways do exist, but you'll have to discover those.

Two types exist:
- **Minor Lifeforce**: Smaller bonuses, used for less potent magic
- **Major Lifeforce**: Significant bonuses, required for powerful rituals

Both provide increased lifespan, fertility, disease resistance, health and prowess.

Using magic uses up Lifeforce, and grants a temporary negative Lifeforce modifier. This means **Blood Mages are NOT immortal** - they can still be assassinated, killed in combat or by illness if their lifeforce becomes depleted.

Managing Lifeforce requires careful balance between health and longevity versus short-term power gains.

## Blood Magic Abilities

Blood Mages can use this Lifeforce to perform various actions:

- Level up a unique Blood Empowerment trait, for permanent buffs.
- Get temporary buffs, or buff their dynasty permantly
- Improve education trait, or gain new ones
- Inscribe their body with runes that passively generate lifeforce
- Heal some wounds and illnesses of varying severity
- Make others Blood Mages or convert to the Blood Cult
- Restore those who have been drained
- Empower their knights with blood magic
- Create Blood Golems, and enhance their traits at the cost of piety
- Drain congenital traits from prisoners (beauty, intelligence, physique, giant, fecund)

## Blóðtrú

Blood Mages can follow their own unique religion, Blóðtrú:

- **Holy Sites**: Almost 50 locations across Europe
- **Special Bonuses**: Each site grants +1 to skills, to balance the number of sites
- **Blood Magic University**: Build special duchy buildings to enhance magical study

### Unified Faith with Pluralistic Integration

The religion features the unified faith `blodtru_faith`, utilizing pluralistic and adaptive doctrines alongside the hidden `bm_blodtru_identity_doctrine` to ensure high compatibility and minimal opinion penalties across diverse realms without overwriting vanilla religions.

### Optional Vanilla Religions submod

**Blood Mages - Vanilla Religions** moves native integration into a separate compatibility submod.
It adds one lore-specific Blood Mage cult to every vanilla religion, automatically converts each
character to the cult belonging to their previous religion, and combines that religion's complete
holy-site set with the Blóðtrú network.

The Cult of the Crimson Ka is its Egyptian–Kushite branch. Because CK3 requires complete religion
overlays to add faiths to existing religions, the submod is intentionally optional while this main
mod remains free of vanilla religion overrides.

## Getting Started

1. Select the Blood Mage trait at character creation
2. Alternatively:
   - Ask a Blood Mage friend/lover/soulmate to grant you the power
   - Convert from being a witch to a Blood Mage
   - Join the Cult of Blood and complete the transformation ritual



## Miscellaneous

**Development plans**: https://trello.com/b/1qS7Y4n0/ck3-blood-mage-mod

**Github repo**: https://github.com/theNicelander/ck3_blood_mage

Feel free to use all the code for your own work. If you do, then please give me a shoutout :)

## Like the mod?

Consider buying be a coffee to support my work 😀

https://www.buymeacoffee.com/TheNicelander
