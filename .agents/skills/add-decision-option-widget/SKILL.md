---
name: add-decision-option-widget
description: >-
  Add decision with inline multi-choice option-list widget in CK3 1.20.
---

# Add decision option-list widget

Context: rules `ck3-decisions`, `ck3-scripting`; skill `add-blood-magic-decision`.
References: mod `common/decisions/cast_magic/bm_attune_lifeforce_decision.txt`; vanilla `10_religious_decisions.txt` (`invite_religious_exiles_decision`), `90_minor_decisions.txt` (`hire_physician_decision`).

`show_from_start = yes` renders the option list immediately in the Decision Detail panel (picture, description, scrollable `DecisionOptionItem` list with 45×45 icons, cost, confirm). `no` hides it behind a "Select Action" step.

## Syntax

```pdx
<decision_name> = {
	picture = { reference = "gfx/interface/illustrations/decisions/<pic>.dds" }
	decision_group_type = <group>
	desc = <desc_key>
	selection_tooltip = <tooltip_key>
	is_shown = { ... }
	is_valid_showing_failures_only = { custom_tooltip = { text = <failure_tt> <condition> } }
	cost = { piety = 25 }

	widget = {
		gui = "decision_view_widget_option_list_generic"
		controller = decision_option_list_controller
		decision_to_second_step_button = "<NEXT_STEP_BUTTON_LOC_KEY>"
		show_from_start = yes

		item = {
			value = <option_scope_name>
			localization = <option_scope_name>
			current_description = <option_scope_name>
			icon = "gfx/interface/icons/<path>.dds"
			is_shown = { ... }
			is_valid = { custom_tooltip = { text = <req_tt> <validity_trigger> } }
			ai_chance = { value = 50 if = { limit = { <condition> } multiply = 0 } }
		}
	}

	effect = {
		if = { limit = { scope:<option_a> = yes } <effect_a> }
		else_if = { limit = { scope:<option_b> = yes } <effect_b> }
		else = { custom_tooltip = <preview_tt> }   # preview before a click
		close_view = { view = decisions player = root }
	}

	ai_check_interval = 12
	ai_will_do = { ... }
}
```

## Rules

1. Selecting an item sets `scope:<value> = yes` in `effect`; name options by behaviour (`bm_attune_ancient`).
2. Loc per item: `<option_key>` (button title) and `<option_key>_tooltip` (hover). Concise; "Lifeforce", not "vitality".
3. Wrap item `is_valid` in `custom_tooltip`; define both `<req_tt>` and `NOT_<req_tt>` loc.
4. Define `<NEXT_STEP_BUTTON_LOC_KEY>` (e.g. `BM_ATTUNE_LIFEFORCE_DECISION_NEXT_STEP_BUTTON`) and `<decision_name>_confirm: "$<KEY>$"`.
5. `ai_chance` in an `item` is a **script value** (`value`, `if/add`, `multiply`, `min`). Event syntax (`base`, `modifier`) silently fails.
6. Icons: 45×45 DDS (`gfx/interface/icons/trait_level_tracks/`, `court_position_types/`).
7. Always `close_view` at the end of `effect`.
