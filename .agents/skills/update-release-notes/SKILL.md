---
name: update-release-notes
description: >-
  Keep the public-facing live release notes document (RELEASE_NOTES.md) updated with net player changes.
---

# Update Release Notes

`RELEASE_NOTES.md` is a living, public-facing summary of all net features and bugfixes since the last major release, formatted for players and Steam Workshop release notes.

## Principles

1. **Player-Facing Only**: No internal script syntax, variable scopes, or implementation trivia. Focus on gameplay impact, player abilities, bonuses, and immersive mechanics.
2. **Net Diff Only**: If a feature was added, modified, refactored, and adjusted, record only the final net state (e.g. *"Implemented standalone Blood Knight lifestyle class with 5 tracks"*).
3. **Sections + Bullets**: Group changes into thematic feature sections with clear bullet points.
4. **Bugfixes at the End**: Place engine fixes, rendering corrections, and script error resolutions in the final `Bugfixes & Technical Improvements` section.

## Steps

1. Read `RELEASE_NOTES.md` at repo root.
2. Identify the matching feature section:
   - *The Twin Devotion Paths: Blood Mage & Blood Knight*
   - *Blood Empowerment & Somatic Ascendancy*
   - *The Three-Tier Lifeforce Economy*
   - *Grimoires, Spellcasting & Decision Widgets*
   - *Icelandic Galdrastafir Flesh-Carved Blood Runes*
   - *Immortal Blood Golems & Dynasty Legacy*
   - *Blóðtrú Religion Family & Sacred Sites*
   - *Domiciles & Realm Holdings*
   - *Blood Magic Situation Panel & User Interface*
   - *Supernatural Visuals & Campaign Game Rules*
   - *Bugfixes & Technical Improvements*
3. If introducing an entirely new system, add a new section before Bugfixes.
4. Update or append bullet points describing the net gameplay feature or fix.
5. If a prior mechanic was replaced or removed, fold or delete its bullet point so the document reflects the current playable state.

## Verify

- Feature descriptions match current script values in `common/` and localizations in `localization/english/`.
- Trailing newlines, clean Markdown formatting, and balanced sections.
