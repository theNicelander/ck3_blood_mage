---
trigger: model_decision
description: Events and on_actions (namespaces, triggers, scopes, options).
---

# Events and on_actions

- One namespace per file (`namespace = bm_<feature>`).
- Every event requires a trigger source: `trigger_event`, `on_action`, decision, or interaction. Uncalled events fail silently; audit with `grep`.
- Silent state changes: wrap in `hidden_effect`. Scope persistence: use `save_scope_as`.
- Event options require loc ([ck3-localization.md](ck3-localization.md)) and tooltips for mechanical outcomes.
- Event option visibility (`show_as_unavailable`): Keep options visible and grayed out (`show_as_unavailable = { ... }`) whenever possible so players can inspect available rites and their requirements. Only hide an option when its prerequisite stage is unreached or when it is permanently completed/superseded.
- Interface toasts (`send_interface_toast`): anything that grants modifiers (character, county, lifeforce stacks), traits (lifestyle, education, congenital, personality), XP, or stats in event options or roll branches (duels, `random_list`) MUST be enclosed inside `send_interface_toast = { ... }`. Effects outside the toast block are invisible in the popup banner. Omit `custom_tooltip` inside toasts when native effects are present so the engine formats effect lines natively.
- On-actions: hook into vanilla via `on_actions = { bm_<on_action> }`. Never duplicate vanilla on-action definitions.
- Event map: see `docs-ai/architecture/blood-mage-events-overview.md`.
