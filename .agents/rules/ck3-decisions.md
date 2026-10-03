---
trigger: model_decision
description: How to write CK3 decisions and character interactions in this mod (structure, validity blocks, costs, AI, localization). Read before touching common/decisions or common/character_interactions.
---

# CK3 decisions (and character interactions)

Sources: CK3 wiki (Decisions modding), vanilla 1.19 decisions, and `common/decisions/` in this repo. Follow a nearby decision in this repo when structure is in doubt.

## Anatomy of a decision

```
bm_example_decision = {
	picture = { reference = "gfx/interface/illustrations/decisions/decision_personal_religious.dds" }
	desc = bm_example_decision_desc          # optional if the default <key>_desc key is used
	selection_tooltip = bm_example_decision_tooltip
	decision_group_type = bm_decision_group  # groups it in the decision window (see common/decision_group_types)
	sort_order = 50                          # optional ordering inside the group
	cooldown = { years = 5 }                 # optional, blocks reuse after the effect

	is_shown = { ... }                       # show/hide: cheap triggers only
	is_valid_showing_failures_only = { ... } # greyed out; only the failing lines are shown
	is_valid = { ... }                       # greyed out; all lines are listed as requirements

	cost = { piety = bm_example_piety_cost } # script value or literal; resources are checked and spent automatically
	effect = { ... }                         # runs when taken; root = deciding character

	ai_check_interval = 12                   # months; 0 disables the AI
	ai_will_do = { base = 10 }
}
```

### Block semantics

- **`is_shown`** decides if the player ever sees the decision. Failing it removes the decision from the list. It is evaluated constantly. Keep it cheap and put "who is this for" checks here (for example `has_trait`, faith, `is_adult`).
- **`is_valid`** requirements are shown as a checklist, and the decision cannot be taken until all pass. Use `is_valid_showing_failures_only` for long lists so only the unmet items are shown. You can use both.
- **`cost`**: `gold`, `prestige`, `piety`. Use script values for anything reused (`common/script_values/bm_*_piety_cost.txt`), and `minimum_cost` when the full cost is not required to take the decision. The cost is paid by the engine, **so never also deduct it in `effect`** (a double piety charge was a real bug in this mod).
- **`effect`**: runs with `root` = the character taking the decision. Put heavy or story logic in a scripted effect (`bm_*_effect`) or an event the decision triggers. Everything listed is shown in the tooltip unless wrapped in `hidden_effect`.
- **Tooltips**: if an effect or requirement is not self-explanatory, add `custom_tooltip = { text = key }`. Add the `key` to **all** languages.
- **Cooldowns**: prefer `cooldown = { ... }` over hand-rolled flags unless the effect needs per-target state.
- `widget`, `confirm_click_sound`, `is_invisible`, and `should_create_alert` exist too. Copy usage from vanilla before using them.

### AI

- `ai_check_interval` is the cost control. High numbers for expensive decisions. `0` means player only.
- `ai_will_do` is a weight (percent for the check). The repo's AI balance is hand-tuned and documented in `CHANGELOG.md`. Keep AI changes conservative and scale `base` down when unsure.
- Gate AI-only logic on `is_ai = yes`, and do not let the AI spend a resource it needs (health, piety floor) without a trigger.
- Respect game rules that gate AI behaviour (`bm_blood_mage_prevalence`).

### Localization keys

- `<decision>` (title), `<decision>_desc`, `<decision>_tooltip` (selection tooltip), and `<decision>_confirm` (confirm button text).
- Missing keys are not an error at load, only a raw key in the UI, so check each one by hand.
- Search for the key before adding it (`grep -rn "key" localization/english`). Add the same key to the other 7 languages.

## Character interactions

- Live in `common/character_interactions/`. `scope:actor` and `scope:recipient` are always available. Other scopes can be saved by `on_accept`/`on_send` effects.
- Structure: `category`, `desc`, `interface_priority`, `is_shown`, `is_valid_showing_failures_only`, `cost`, `on_accept`, `on_decline`, `ai_targets`, `ai_frequency`, `ai_potential`, `ai_will_do`. Use `auto_accept = yes` when the recipient has no choice.
- `is_shown` is evaluated for every candidate recipient, so keep it fast.
- Costs are charged by `cost = { ... }`. Do not charge again in `on_accept`.
- AI: use `ai_targets` to bound which recipients the AI considers (`self`, `dynasty`, `family`, `courtiers`, ...). `ai_frequency` is months between checks. `ai_potential` is the actor-level gate.
- Use shared effects (`bm_become_blood_mage_effect = yes`) instead of raw `add_trait` where that effect exists.

## Checklist before finishing a decision or interaction

1. Does `is_shown` hide it from everyone who should not see it?
2. Can `is_valid` / `is_valid_showing_failures_only` explain every reason for being greyed out?
3. Is the cost declared once, as a script value if reused?
4. Is the effect safe if run twice, with a missing target, or on an AI?
5. Are `ai_check_interval` and `ai_will_do` (or `ai_*` for interactions) set deliberately?
6. Are localization keys added in all 8 languages?
7. Did you add a `CHANGELOG.md` line?
8. Did `ck3-tiger` stay clean?
