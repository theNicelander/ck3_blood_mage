# Blood Runes and Blood Architecture

> Living document. Follow `AGENTS.md` in this folder: concepts only, no numbers. Update it when runes, rune events, modifiers or blood buildings change.

## Purpose

Blood runes and blood architecture represent the physical anchoring of blood magic into the mage's flesh and domain. Blood runes allow a mage to permanently inscribe eldritch markings upon their own body to magnify their supernatural capacity, while blood universities allow a blood mage ruler to turn their realm capital into a center of forbidden research.

## Concepts

- **Rune Tiers.** Crimson Runes are inscribed sequentially onto the caster's body through the self-cast major interaction:
  - *Minor Crimson Rune:* The foundational inscription, granting modest mystical enhancements.
  - *Major Crimson Rune:* Upgrades the minor rune, significantly deepening the caster's magical resonance.
  - *Superior Crimson Rune:* The pinnacle of personal bodily warding and power enhancement.
- **Rune Escalation.** Inscribing a higher-tier rune requires having the lower tier already inscribed and costs an escalating amount of piety and experience.
- **Blood Universities.** A series of duchy capital buildings (`bm_university_0` through `bm_university_3`) constructible only by blood mage rulers. They trade income and piety for cultural fascination, development growth, and occult research capabilities.

## Where the details live

| Piece | File |
| --- | --- |
| Inscription decision | `common/decisions/bm_inscribe_blood_runes_decision.txt` (`bm_inscribe_blood_runes_decision`) |
| Rune inscription events | `events/bm_blood_rune_events.txt` (`bm_crimson_rune.001`) |
| Rune modifiers | `common/modifiers/bm_blood_runes_modifiers.txt` |
| Rune piety cost values | `common/script_values/bm_blood_rune_cost.txt` |
| Rune XP requirement values | `common/script_values/bm_xp_requirement_values.txt` (`bm_blood_rune_minimum_xp`) |
| Duchy capital buildings | `common/buildings/bm_dutchy_buildings.txt` |

## How the parts connect

- A blood mage initiates the rune inscription ritual through `bm_inscribe_blood_runes_decision`.
- The decision verifies that the character meets the XP requirement in `bm_blood_rune_minimum_xp` and can afford `bm_blood_rune_piety_cost`.
- Event `bm_crimson_rune.001` fires, presenting the valid upgrade tier based on existing rune modifiers, and replaces the old rune modifier with the new one.
- Blood universities require the holding holder to possess `lifestyle_blood_mage` to be constructed or upgraded.

## Gotchas

- Rune modifiers do not stack with themselves; each higher tier explicitly removes the preceding tier modifier upon application.
- If a blood mage loses their duchy capital or is succeeded by an uninitiated heir, the blood university buildings remain present but may become inactive or inaccessible depending on standard CK3 building holder triggers.

## Not verified

Visual 3D model modifications on characters or province map models when constructing blood universities.
