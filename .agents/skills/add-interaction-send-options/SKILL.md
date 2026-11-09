---
name: add-interaction-send-options
description: >-
  Add or refactor a character interaction with exclusive modal options in CK3 1.20.
---

# Add interaction send options

Context: rules `ck3-decisions`, `ck3-scripting`; skill `add-blood-magic-decision`.
References: mod `common/character_interactions/bm_blood_blessing.txt`; vanilla `00_diarch_interactions.txt`.

`send_options_exclusive = yes` opens a modal choice window before sending the interaction, letting the actor pick one of several mutually exclusive radio options (`send_option`).

## Syntax

```pdx
<interaction_name> = {
	category = interaction_category_bm_blood_magic
	common_interaction = yes
	auto_accept = yes
	desc = <interaction_name>_desc

	cost = {
		piety = {
			if = {
				limit = { scope:<option_a> = yes }
				value = <cost_a>
			}
			else_if = {
				limit = { scope:<option_b> = yes }
				value = <cost_b>
			}
		}
	}

	is_shown = {
		scope:actor = { ... }
		scope:recipient = { ... }
	}

	is_valid_showing_failures_only = {
		custom_description = {
			text = <failure_tt>
			scope:actor = { ... }
		}
	}

	send_options_exclusive = yes

	send_option = {
		flag = <option_a>
		localization = <loc_key_a>
		current_description = <desc_key_a>
		is_shown = { always = yes }
		is_valid = {
			scope:actor = { ... }
			scope:recipient = { ... }
		}
		starts_enabled = {
			# Evaluated to select default radio button on window open
			scope:actor = { ... }
		}
	}

	send_option = {
		flag = <option_b>
		localization = <loc_key_b>
		current_description = <desc_key_b>
		is_shown = { always = yes }
		is_valid = {
			scope:actor = { ... }
		}
		starts_enabled = {
			NOT = { scope:actor = { ... } }
		}
	}

	on_accept = {
		debug_log = "Interaction: <name> | Actor: [actor.GetShortUINameNoTooltip] -> Recipient: [recipient.GetShortUINameNoTooltip]"
		if = {
			limit = { scope:<option_a> = yes }
			scope:actor = {
				send_interface_toast = {
					type = event_toast_effect_good
					title = <toast_key_a>
					left_icon = scope:actor
					right_icon = scope:recipient
					<effect_a>
					hidden_effect = {
						bm_recount_lifeforce_stacks_effect = yes
					}
				}
			}
		}
		else_if = {
			limit = { scope:<option_b> = yes }
			scope:actor = {
				send_interface_toast = {
					type = event_toast_effect_good
					title = <toast_key_b>
					left_icon = scope:actor
					right_icon = scope:recipient
					<effect_b>
					hidden_effect = {
						bm_recount_lifeforce_stacks_effect = yes
					}
				}
			}
		}
	}

	ai_potential = { always = yes }
	ai_frequency = 12
	ai_targets = {
		ai_recipients = ...
	}
	ai_will_do = {
		base = 20
		...
	}
}
```

## Rules

1. Each `send_option` must define `flag = <unique_flag>`. In `cost`, `on_accept`, and `on_send`, this flag is checked as `scope:<flag> = yes`.
2. Loc per option: `localization = <key>` (option label in radio list) and `current_description = <key_desc>` (body/hover summary in the modal).
3. Keep options visible and greyed out (`show_as_unavailable` / `is_valid`) per mod principle. Only hide via `is_shown` when completely inapplicable.
4. Set `starts_enabled` on the options so the most relevant/unlocked option is pre-selected when the window opens.
5. In `cost`, guard variable costs with `if = { limit = { scope:<flag> = yes } value = ... }`.
6. Enclose stat/modifier/Lifeforce gains in `send_interface_toast` with `hidden_effect = { bm_recount_lifeforce_stacks_effect = yes }`.
7. **Always set `can_invalidate_interaction = yes`** on each `send_option`.
8. **AI must score modal options**: In `ai_will_do`, explicitly add weights for each option: `modifier = { scope:<flag> = yes add = N }`.
9. **Absolute empty-set veto**: CK3 AI evaluates combinations of flags including empty `{}`. You MUST end `ai_will_do` with `factor = 0` when no modal option is selected (`modifier = { NOR = { scope:<opt_a> = yes scope:<opt_b> = yes } factor = 0 }`), otherwise the AI fires the interaction with no options selected (zero cost, zero effect).
10. **Structured debug logging**: Output structured `debug_log` inside each `if / else_if` in `on_accept`, and add an `else` branch logging `(NO OPTION)` fallback. Include Actor, Recipient, Option, Relationship, Tag (`bm_debug_relation_tags`), and Opinion.
