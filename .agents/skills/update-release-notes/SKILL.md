---
name: update-release-notes
description: >-
  Keep RELEASE_NOTES.md (public Steam notes + version history) updated with net player changes.
---

# Update release notes

`RELEASE_NOTES.md`: player-facing net features/bugfixes since v1.15 + `## Version history`.

- Player-facing only (gameplay impact, no script internals). Verify claims against `common/` + `localization/english/`.
- Net state only: fold/delete bullets for replaced or removed mechanics.
- 1 sentence/bullet under existing feature headings (new system = new section before Bugfixes; fixes in Bugfixes).
- Version history: prepend `* <branch>: <short imperative outcome>` (≤120 chars).
- Headline numbers only when player needs them; keep ~13 KB.
