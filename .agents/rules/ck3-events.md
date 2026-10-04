---
trigger: model_decision
description: Writing CK3 events and on_actions (namespaces, sources, options, scopes). Read before touching events/ or common/on_action/.
---

# Events and on_actions

- One namespace per file. Match neighbouring files.
- Every event needs a source (`trigger_event`, an `on_action`, a decision, an interaction). Dead events are not errors, so check by grep.
- Use `hidden_effect` for silent state changes. Save scopes you need later (`save_scope_as`).
- Event options need localization (`ck3-localization.md`), and options that matter need tooltips.
- On-actions: add to the named vanilla on-action via `on_actions = { <your_on_action> }` and don't copy vanilla bodies.
- Mod-specific events are mapped in `docs-ai/architecture/`. Start at its `README.md`.
