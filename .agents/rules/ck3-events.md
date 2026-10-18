---
trigger: model_decision
description: Events and on_actions (namespaces, triggers, scopes, options).
---

# Events and on_actions

- One namespace per file (`namespace = bm_<feature>`).
- Every event requires a trigger source: `trigger_event`, `on_action`, decision, or interaction. Uncalled events fail silently; audit with `grep`.
- Silent state changes: wrap in `hidden_effect`. Scope persistence: use `save_scope_as`.
- Event options require loc ([ck3-localization.md](ck3-localization.md)) and tooltips for mechanical outcomes.
- Interface toasts (`send_interface_toast`): outcome effects (XP, lifeforce modifiers, stat gains, `hidden_effect = { bm_recount_lifeforce_stacks_effect = yes }`) must be placed directly inside `send_interface_toast = { ... }` so they render in the toast popup. Omit `custom_tooltip` so the engine formats effect lines natively.
- On-actions: hook into vanilla via `on_actions = { bm_<on_action> }`. Never duplicate vanilla on-action definitions.
- Event map: see `docs-ai/architecture/blood-mage-events-overview.md`.
