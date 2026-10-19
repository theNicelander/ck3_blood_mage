---
name: add-decision-option-widget
description: >-
  Add decision with inline multi-choice option-list widget in CK3 1.20.
---

# Add decision option-list widget

Context: [ck3-decisions](../../rules/ck3-decisions.md), [ck3-scripting](../../rules/ck3-scripting.md), [add-blood-magic-decision](../add-blood-magic-decision/SKILL.md).

Reference implementations:
- Mod: `common/decisions/cast_magic/bm_attune_lifeforce_decision.txt`
- Vanilla: `common/decisions/10_religious_decisions.txt` (`invite_religious_exiles_decision`), `common/decisions/06_ce1_decisions.txt` (`clear_ground_legendary_building_decision`), `common/decisions/90_minor_decisions.txt` (`hire_physician_decision`).

## Pattern

Use `decision_option_list_controller` with `decision_view_widget_option_list_generic` and `show_from_start = yes` to embed an interactive scrollable list of selectable options with icons, failure tooltips, and a confirm button directly inside the Decision Detail panel.

### Why `decision_view_widget_option_list_generic` with `show_from_start = yes`?

In CK3's `window_decisions_detail.gui`:
- If `show_from_start = no`, the decision opens showing the default description/effects view (`IsDefaultWidgetShown = true`), and hides the custom option list behind a 2-step button (`ToggleCustomWidgetState`) labeled "Select Action".
- If `show_from_start = yes`, `IsDefaultWidgetShown` starts as `false`. The decision view immediately renders:
  1. The top picture illustration.
  2. The decision description (`[DecisionDetailView.GetDescription]`).
  3. The centered section label `"Select a valid option"` (`SELECT_VALID_OPTION`).
  4. The scrollbox containing `450x60` `DecisionOptionItem` buttons with `45x45` DDS icons, option names, and hover tooltips.
  5. The cost label (e.g. `Cost: [Piety] 25`), the single confirm button, and the decision notification toggle at the bottom.

## Syntax

```pdx
<decision_name> = {
	picture = { reference = "gfx/interface/illustrations/decisions/<pic>.dds" }
	decision_group_type = <group>

	desc = <decision_desc_loc_key>
	selection_tooltip = <decision_tooltip_loc_key>

	is_shown = { ... }

	# Show failures cleanly if requirements are not met
	is_valid_showing_failures_only = {
		custom_tooltip = {
			text = <failure_tt_key>
			<condition>
		}
	}

	cost = {
		piety = 25 # or gold, prestige, etc.
	}

	widget = {
		gui = "decision_view_widget_option_list_generic"
		controller = decision_option_list_controller
		decision_to_second_step_button = "<DECISION_NEXT_STEP_BUTTON_LOC_KEY>"
		show_from_start = yes

		item = {
			value = <option_scope_name>
			localization = <option_scope_name>
			current_description = <option_scope_name>
			icon = "gfx/interface/icons/<path_to_icon>.dds"

			is_shown = {
				# Filter which options are visible
			}

			is_valid = {
				# Wrap failure reason so disabled options show a clean red requirement
				custom_tooltip = {
					text = <option_unavailable_req_tt>
					<validity_trigger>
				}
			}

			# CRITICAL: ai_chance here is a script value, NOT an event weight block!
			ai_chance = {
				value = 50
				if = {
					limit = { <condition> }
					multiply = 0
				}
			}
		}
	}

	effect = {
		# Dispatches based on the selected option scope
		if = {
			limit = { scope:<option_scope_name> = yes }
			<effect_for_option>
		}
		else_if = {
			limit = { scope:<other_option_scope_name> = yes }
			<other_effect>
		}
		else = {
			# Fallback preview tooltip shown before any option is clicked
			custom_tooltip = <decision_effect_preview_tt>
		}

		close_view = {
			view = decisions
			player = root
		}
	}

	ai_check_interval = 12
	ai_will_do = { ... }
}
```

## Key Rules

1. **Selection Scope**: Selecting an item sets `scope:<value> = yes` in the decision effect execution scope. Use descriptive identifier names matching the target behavior (e.g. `bm_attune_ancient`).
2. **Item Localization Conventions**:
   - For `value = <option_key>`:
     - `localization = <option_key>`: The button title text.
     - `current_description = <option_key>`: Used by `[Entry.GetTooltip]`.
     - In localization `.yml`, provide both `<option_key>` (name) and `<option_key>_tooltip` (full hover tooltip description), matching vanilla's `invite_all_exiles` / `invite_all_exiles_tooltip`.
     - Keep option text and tooltips concise and direct: specify concrete mechanics ("Lifeforce") rather than fluffy flavour ("vitality").
3. **Item Failure Tooltips (`custom_tooltip`)**:
   - Always wrap `is_valid` conditions in `item` with `custom_tooltip = { text = <req_key> ... }`.
   - Disabled options will display this failure message in red, identical to vanilla's `"! There are no exiles of this type within range that you can invite"`.
   - Remember to provide both `<req_key>` and `NOT_<req_key>` in localization to prevent missing tooltip bugs.
4. **Button Label**:
   - Define `<DECISION_NEXT_STEP_BUTTON_LOC_KEY>` (e.g. `BM_ATTUNE_LIFEFORCE_DECISION_NEXT_STEP_BUTTON`) and alias `<decision_name>_confirm: "$<DECISION_NEXT_STEP_BUTTON_LOC_KEY>$"`.
5. **AI Chance Script Trap**:
   - `ai_chance` inside `decision_option_list_controller` `item` is a **script value block** (`value = N`, `if = { limit = { ... } add = M }`, `multiply = X`, `min = 0`). Never use event weight syntax (`base = N`, `modifier = { ... }`), which silently fails to evaluate.
6. **Icons**:
   - Use 45×45 DDS icons (e.g. trait tracks in `gfx/interface/icons/trait_level_tracks/` or court positions in `gfx/interface/icons/court_position_types/`).
7. **Close View**:
   - Add `close_view = { view = decisions player = root }` inside `effect` so the panel closes cleanly upon confirmation.
