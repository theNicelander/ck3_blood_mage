# Shared Scripting and System Utilities

> Living document. Follow `AGENTS.md` in this folder: concepts only, no numbers. Update it when triggers, opinion modifiers, nicknames, text icons or compat layers change.

## Purpose

This document covers cross-cutting system assets and conventions that underpin all Blood Mages features. It serves as the reference for shared scripted triggers, custom opinion modifiers, nicknames, death reasons, UI text icons, third-party mod compatibility guards, and syntax validation standards.

## Concepts

- **Scripted Triggers.** `common/scripted_triggers/bm_triggers.txt` holds reusable condition blocks. Notably, `is_playing_overhaul_mod` detects major overhaul total conversions (such as AGOT, Elder Kings, Lord of the Rings) to adjust gameplay rules and avoid conflicts.
- **Opinion Modifiers.** `common/opinion_modifiers/bm_opinions.txt` defines social reactions to blood magic. These include decaying positive opinions from beneficiaries (`magic_opinion_positive`), gratitude for receiving blood magic (`made_me_a_blood_mage`), horror from being drained (`lifedrained_me`), and negative reactions to forbidden sorcery.
- **Nicknames & Death Reasons.** `common/nicknames/bm_nicknames.txt` holds thematic titles (`nick_the_wanderer`). `common/deathreasons/bm_event_deaths.txt` defines unique mortality causes like `death_lifedrain_reason` and `death_blood_golem_failed`, ensuring character death logs properly reflect occult demise.
- **UI Assets & Text Icons.** `gui/bm_blood_magic_texticons.gui` and `gui/bm_game_rule_texticons.gui` register inline font icons (e.g. `@bm_game_rule_icon!`) used in decision headers, game rules, and event descriptions.
- **Third-Party Compatibility.** External overhaul mod traits, faiths, or mechanics must never be referenced directly. Mod compatibility is achieved by querying global flags (e.g. `has_global_variable = AGOT_is_loaded`) as detailed in `.agents/rules/ck3-religions.md`.
- **Validation Standards.** Script files must be UTF-8 with BOM, use trailing newlines, and maintain balanced braces.

## Mod conventions

- **Optional-mod compatibility.** Guard with `has_global_variable = AGOT_is_loaded` or doctrine parameters. Never reference another mod's traits, faiths or titles directly.

## Where the details live

| Piece | File |
| --- | --- |
| Shared scripted triggers | `common/scripted_triggers/bm_triggers.txt` |
| Custom trigger localization | `common/trigger_localization/bm_trigger_localization.txt` |
| Opinion modifiers | `common/opinion_modifiers/bm_opinions.txt` |
| Nicknames | `common/nicknames/bm_nicknames.txt` |
| Custom death reasons | `common/deathreasons/bm_event_deaths.txt` |
| Decision group definitions | `common/decision_group_types/bm_decision_group_types.txt` |
| Font text icons | `gui/bm_blood_magic_texticons.gui`, `gui/bm_game_rule_texticons.gui` |
| Faith & religion text icons | `gui/shared/bm_texticons_religion.gui` |

## How the parts connect

- Decisions and interactions include `bm_decision_group_types.txt` to organize player decisions under the dedicated blood magic banner.
- Custom deaths assign `death_reason = death_lifedrain_reason` to provide evocative tooltips in family trees and memorial screens.
- Inline text icons are embedded in localization strings across `localization/english/` to visually indicate blood magic actions and resources.

## Gotchas

- Unprefixed files or identifiers that shadow vanilla assets will silently override vanilla behaviour. Always adhere to the `bm_` prefix convention.
- Modifiers applied without valid duration parameters or decaying settings may accumulate indefinitely or persist after death.

## Not verified

Compatibility flags with future or unreleased updates to third-party total overhaul mods.
