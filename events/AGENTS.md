# Events & On-Actions (`events/`)

Map: `docs-ai/architecture/blood-mage-events-overview.md`.

- One `namespace = bm_<feature>` per file.
- Every event needs a trigger source (`trigger_event`, `on_action`, decision, interaction); uncalled events fail silently — grep to verify.
- Silent state changes → `hidden_effect`. Scope persistence → `save_scope_as`.
- `show_as_unavailable` is a **sibling** of `trigger` directly in `option` (never nested inside `trigger`).
- Event options use `ai_chance = { base = N modifier = { ... } }` (relative weights).
- On-actions: hook vanilla via `on_actions = { bm_<on_action> }`; never duplicate vanilla on-action blocks.
