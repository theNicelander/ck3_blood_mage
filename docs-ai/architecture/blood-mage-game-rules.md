# Blood Mage Game Rules

> Living document. Follow `AGENTS.md` in this folder: concepts only, no numbers. Update it when game rules, rule options or gated systems change.

## Purpose

Game rules allow players to configure how Blood Mages mechanics integrate into their campaign. Players can tune the overall rarity and AI presence of blood mages, enable or disable the Cult of Quintessence religion family, and choose whether physical alterations (eye and hair colors) manifest on practitioners.

## Concepts

- **Prevalence Rule (`bm_blood_mage_prevalence`).** Determines how widespread blood magic is across the world.
  - *Player Only:* Restricts blood magic solely to player-controlled characters.
  - *One in 10,000 / One in 1,000:* Heavily suppresses AI adoption and purges spontaneous or inherited AI mages.
  - *Default:* Baseline spontaneous generation and standard inheritance chances.
  - *One in 100 / One in 10:* Progressively boosts AI adoption willingness and grants additional spontaneous birth and inheritance chances.
  - *Everyone:* Automatically grants the Blood Mage trait to every newborn child.
- **Physical Alteration Rule (`bm_physical_alteration`).** Controls cosmetic physical transformations for blood mages:
  - *None:* Retains natural portrait appearance.
  - *Eyes:* Alchemically shifts eye color to supernatural crimson.
  - *Eyes & Hair:* Transforms both eye and hair colors upon embracing blood magic.
- **Quintessence Religion Rule (`quintessence_religion`).** Dictates the presence and viability of the Cult of Quintessence religion family:
  - *Enabled:* Fully active for players and AI.
  - *Player Only:* Accessible only to human players; AI rulers will not convert or found holy sites.
  - *Disabled:* Completely suppresses the religion family.

## Where the details live

| Piece | File |
| --- | --- |
| Game rule definitions | `common/game_rules/bm_game_rules.txt` |
| Game rule text icons | `gui/bm_game_rule_texticons.gui` |
| Localization | `localization/english/bm_game_rules_l_english.yml` |
| Prevalence AI modifiers | `common/scripted_modifiers/bm_blood_mage_prevalence_modifiers.txt` |
| Prevalence retention logic | `common/scripted_effects/bm_blood_mage_lifecycle_effects.txt` |
| Birth inheritance handling | `common/on_action/bm_blood_mage_prevalence_on_actions.txt` |

## How the parts connect

- Game start checks evaluate the selected rules and set up appropriate modifier multipliers.
- AI decision and interaction weights test `has_game_rule = bm_<rule>_<setting>` via `bm_blood_mage_prevalence_modifiers.txt`.
- Birth and yearly pulse on-actions query the prevalence rule to determine whether new AI mages keep or forfeit the trait.
- Portrait modifier application checks `bm_physical_alteration` settings when styling characters.

## Gotchas

- Game rule naming convention strictly follows `bm_<rule>_<setting>`. Always prefix rule checks accordingly.
- Changing game rules mid-campaign via console or save-editing may leave already-generated AI blood mages in place until the next yearly retention audit.

## Not verified

Compatibility with third-party total overhaul mods that overwrite or bypass standard `game_modes` or `on_birth_child` on-action blocks.
