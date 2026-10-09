---
trigger: model_decision
description: Events and on_actions (namespaces, triggers, scopes, options).
---

# Events and on_actions

- One namespace per file (`namespace = bm_<feature>`).
- Every event requires a trigger source: `trigger_event`, `on_action`, decision, or interaction. Uncalled events fail silently; audit with `grep`.
- Silent state changes: wrap in `hidden_effect`. Scope persistence: use `save_scope_as`.
- Event options require loc ([ck3-localization.md](ck3-localization.md)) and tooltips for mechanical outcomes.
- On-actions: hook into vanilla via `on_actions = { bm_<on_action> }`. Never duplicate vanilla on-action definitions.
- Event map: see `docs-ai/architecture/blood-mage-events-overview.md`.
