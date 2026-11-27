---
name: add-decision-option-widget
description: >-
  Add decision with inline multi-choice option-list widget in CK3 1.21.
---

# Add decision option-list widget

Canonical mod ref: `common/decisions/cast_magic/bm_attune_lifeforce_decision.txt` (vanilla: `invite_religious_exiles_decision`, `hire_physician_decision`).

`show_from_start = yes` renders scrollable `DecisionOptionItem` list (45×45 icons) immediately in Decision Detail; `no` hides behind "Select Action".

```ck3
widget = {
	gui = "decision_view_widget_option_list_generic"
	controller = decision_option_list_controller
	decision_to_second_step_button = "<NEXT_STEP_LOC_KEY>"
	show_from_start = yes
	item = {
		value = <opt_scope>  localization = <opt_scope>  current_description = <opt_scope>
		icon = "gfx/interface/icons/<path>.dds"  # 45x45 DDS
		is_shown = { ... }  is_valid = { ... }
		ai_chance = { value = 50 if = { limit = { ... } multiply = 0 } }  # SCRIPT VALUE syntax!
	}
}
```

## Rules

- Selecting item sets `scope:<value> = yes` in `effect`; add `else = { custom_tooltip = <preview_tt> }` for pre-click preview.
- End `effect` with `close_view = { view = decisions player = root }`.
- Loc: `<opt_key>`, `<opt_key>_tooltip` (concise 1-liner; see `localization/AGENTS.md`), `<NEXT_STEP_LOC_KEY>`, `<decision>_confirm: "$<NEXT_STEP_LOC_KEY>$"`.
- **`ai_chance` trap**: in `item`, `ai_chance` is a **script value** (`value`, `if/add`, `multiply`, `min`). Event `base`/`modifier` syntax silently fails.
