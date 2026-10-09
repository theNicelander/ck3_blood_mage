# Blood Mages

## Local fork

This repository is a CK3 1.20 fork of [Blood Mages by Nicelander](https://steamcommunity.com/sharedfiles/filedetails/?id=3470491478), maintained at [im-mortal/ck3_blood_mage](https://github.com/im-mortal/ck3_blood_mage). It includes the current upstream gameplay and a complete Russian localization. `descriptor.mod` declares CK3 `1.20.*` support; in-game compatibility and translated UI layout still require testing.

## Русская локализация

Все тексты мода переведены на русский: свойства, решения, взаимодействия, события, панель магии крови, модификаторы, здания, конфессии, священные места и отладочные действия. Перевод выбирается автоматически при русском языке игры; отдельный русификатор не нужен. Личные ритуалы доступны через щелчок правой кнопкой по своему персонажу.

Для ручной установки поместите файлы мода в папку `Documents/Paradox Interactive/Crusader Kings III/mod/ck3_blood_mage`. Создайте рядом файл `ck3_blood_mage.mod`, скопировав в него содержимое `descriptor.mod` и добавив строку `path="mod/ck3_blood_mage"`. Включите локальную копию в наборе модов лаунчера. Одновременно должна быть активна только одна копия Blood Mages.

После первого запуска проверьте русские подсказки и `Documents/Paradox Interactive/Crusader Kings III/logs/error.log`. Полнота перевода проверяется командой `python3 scripts/bm_validate_localization.py`.


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
| One in 10,000 | 0.05× Default | 5% |
| One in 1,000 | 0.50× Default | 50% |
| Default (One in 500) | 1.00× | 100% |
| One in 100 | 2.00× Default | 100%, plus increased newborn acquisition |
| One in 10 | 5.00× Default | 100%, plus increased newborn acquisition |
| Everyone | 10.00× Default | 100%, and all AI newborns receive the trait |

These names describe approximate spontaneous prevalence, not the chance of every AI
interaction succeeding. Acquisition weights scale each action's existing AI weight;
targets, relationships, eligibility and check cadence still matter. Retention is a
separate review of naturally generated or inherited AI traits. Increased-prevalence
settings add birth rolls for AI children who have not already received the trait.
The default keeps standard inheritance and spontaneous appearance. The rule does
not reduce player access to Blood Mage decisions or interactions.

Select the prevalence rule when creating a campaign. Existing saves keep their stored
game rules; this localization update does not remove traits or change gameplay balance.

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
attunement, and the available story decisions. Personal rituals are self-interactions accessible by
right-clicking your character. After those decisions it shows independently
collapsible, scrollable rosters for the Blood Golems and the Crimson
Warriors/Champions currently serving at the Blood Mage's court; an empty
roster collapses to a compact `None` row. Opening the Situations window repairs
a missing player story when necessary and refreshes the counters and rosters;
each roster has a small standard refresh button for manual updates. Lifeforce
and Attunement labels explain their resource and advancement rules on hover.

Compatibility submods can shadow the story definition at its exact virtual path
to add integration-only features without taking ownership of its lifecycle,
progression display, or roster implementation. The interactive roster control
uses a complete overlay of `gui/window_situation_list.gui`
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

- Level up a unique Crimson Empowerment trait, for permanent buffs.
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
