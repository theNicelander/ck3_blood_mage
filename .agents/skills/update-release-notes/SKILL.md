---
name: update-release-notes
description: >-
  Keep RELEASE_NOTES.md (public Steam notes + version history) updated with net player changes.
---

# Update release notes

`RELEASE_NOTES.md`: player-facing net features/bugfixes since v1.15, plus a `## Version history` list.

## Rules

- Player-facing only: gameplay impact, no script syntax or internals.
- Net state only: fold or delete bullets for replaced or removed mechanics.
- One sentence per bullet, grouped under the existing feature headings; new system = new section before Bugfixes. Fixes go in the final Bugfixes section.
- Version history: prepend one line `* <branch>: <short imperative outcome>` (≤120 chars) matching the branch name.
- Headline numbers only where a player needs them; keep the file compact (~13 KB).
- Check claims against `common/` and `localization/english/`.
