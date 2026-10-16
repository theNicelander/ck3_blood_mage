---
name: add-decision-option-widget
description: >-
  Add decision with inline multi-choice option-list widget in CK3 1.20.
---

# Add decision option-list widget

Context: [ck3-decisions](../../rules/ck3-decisions.md), [ck3-scripting](../../rules/ck3-scripting.md), [add-blood-magic-decision](../add-blood-magic-decision/SKILL.md).

Reference implementations: `common/decisions/cast_magic/bm_attune_lifeforce_decision.txt`, vanilla `common/decisions/dlc_decisions/ep_3/06_ep3_admin_decisions.txt` (`convert_to_administrative_decision`), `dlc_decisions/tgp/tgp_dynastic_cycle_decisions.txt`.

## Pattern

Use `decision_option_list_controller` with `decision_view_widget_generic_multichoice_with_effects` to embed an interactive scrollable list of selectable options with icons and live effect previews directly into the Decision Detail panel.

Preferred over `decision_view_widget_option_list_generic` because `decision_view_widget_generic_multichoice_with_effects` renders the decision `effect` preview box above an expanding scrollbox of `450x60` icon-and-label buttons instead of hiding effects.

## Syntax

```pdx
<decision_name> = {
	picture = { reference = "gfx/interface/illustrations/decisions/<pic>.dds" }
	decision_group_type = <group>

	is_shown = { ... }
	is_valid = { ... }
	cost = { ... }

	widget = {
		gui = "decision_view_widget_generic_multichoice_with_effects"
		controller = decision_option_list_controller
		decision_to_second_step_button = "SELECT_ACTION"
		show_from_start = no

		item = {
			value = <option_scope_name>
			is_shown = { ... }
			is_valid = { ... }
			localization = <option_name_loc_key>
			current_description = <option_desc_tooltip_loc_key>
			icon = "gfx/interface/icons/<category>/<icon>.dds"

			# CRITICAL: ai_chance here is a script value, NOT an event weight block!
			ai_chance = {
				value = 50
				if = {
					limit = { ... }
					add = -20
				}
				min = 0
			}
		}
	}

	effect = {
		# Dispatches based on selected option
		if = {
			limit = { scope:<option_scope_name> = yes }
			<effect_for_option>
		}
		else_if = {
			limit = { scope:<other_option_scope_name> = yes }
			<other_effect>
		}
	}

	ai_check_interval = 12
	ai_will_do = { ... }
}
```

## Key Rules

1. **Selection Scope**: Selecting an item sets `scope:<value> = yes` in the decision effect execution scope. Use descriptive identifier names matching the target behavior (e.g. `bm_attune_ancient`).
2. **Dynamic Preview**: The Decision Detail panel re-evaluates `effect = { ... }` dynamically when the player clicks an option. Branching with `if = { limit = { scope:<value> = yes } ... }` provides live effect tooltips per option before confirming.
3. **AI Chance Script Trap**: `ai_chance` inside `decision_option_list_controller` `item` is a **script value block** (`value = N`, `if = { limit = { ... } add = M }`, `multiply = X`, `min = 0`). Never use event weight syntax (`base = N`, `modifier = { ... }`), which silently fails to evaluate.
4. **Icons**: Use 45×45 DDS icons (e.g. trait tracks in `gfx/interface/icons/trait_level_tracks/` or governments in `gfx/interface/icons/government_types/`).
5. **Localization**:
   - `localization`: string key for button label.
   - `current_description`: string key for button hover tooltip.
