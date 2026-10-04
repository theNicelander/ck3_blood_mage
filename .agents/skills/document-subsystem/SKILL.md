---
name: document-subsystem
description: >-
  Use this skill when a new mod subsystem needs an architecture doc, or an
  existing doc must be rewritten.
---

# Document a subsystem

## Steps

1. Read [architecture AGENTS.md](../../../docs-ai/architecture/AGENTS.md).
2. Name the file `docs-ai/architecture/blood-mage-<subsystem>.md`.
3. Headings in order: Purpose, Concepts, Mod conventions (optional), Where the details live, How the parts connect, Gotchas, Not verified.
4. Concepts only: no costs, thresholds or chances.
5. Read the english loc entries for each identifier (see [localization rule](../../rules/ck3-localization.md)).
6. Register the doc in `docs-ai/architecture/AGENTS.md` and `README.md`.

## Verify

- Every identifier and path in the doc exists (`grep` / `ls`).
- The doc appears in both the AGENTS.md table and the README index.
