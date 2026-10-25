---
trigger: model_decision
description: Decisions, character interactions and AI (cost, is_shown, is_valid, cooldown, effects, tooltips, ai_will_do, ai_check_interval, ai_targets).
---

# Decisions, interactions, AI

Copy a neighbouring file in `common/decisions/` or `common/character_interactions/`. CK3 AI is hardcoded; script only shifts selection likelihood.

## Script traps

- Never deduct `cost` inside `effect`; the engine charges the declared `cost`. Reused costs go in `common/script_values/`.
- `is_shown` runs constantly: cheap exclusionary triggers first. Prefer native `cooldown = { ... }` over flags.
- Effects must be safe if fired twice, on missing scopes, or by AI.
- Put cost and affordability triggers in `is_valid`, not only `ai_will_do`. Never use `is_ai = yes` to skip validity or costs.
- Tooltips: `custom_tooltip = { text = key }` for non-obvious outcomes; concise, concrete terms ("Lifeforce"). Flavour only in `<id>_desc`.
- Outcomes that grant modifiers, traits, XP or stats go inside `send_interface_toast`; avoid `custom_tooltip` inside toasts.
- Loc sibling keys: see `ck3-localization.md`.

## AI control points

| Context | Keys |
| --- | --- |
| Decision | `ai_check_interval` (months; `0` = player-only), `ai_will_do` (% chance per check), `ai_potential` (hard gate) |
| Interaction | `ai_targets` (`self`, `dynasty`, `family`, `spouses`, `children`, `courtiers`, `councillors`, `liege`), `ai_frequency`, `ai_potential`, `ai_will_do`, `ai_accept` |
| Event option | `ai_chance = { base = N modifier = { ... } }` (relative weights) |

```ck3
ai_will_do = {
	base = -10
	modifier = { add = 20 has_trait = ambitious }     # additive first
	modifier = { factor = 0 has_trait = wounded_1 }   # vetoes last
}
```

- `add` shifts the running score; `factor` multiplies it. Triggers inside `modifier` are ANDed; cheap first.
- Personality: `ai_value_modifier = { ai_greed = 0.5 }` (`ai_boldness|compassion|energy|greed|honor|rationality|sociability|vengefulness|zeal`).
- Balance is hand-tuned: do not raise `base` or shorten intervals without reason. AI must check health, Lifeforce, piety and target opinion before harmful actions; reuse scripted modifiers.
- AI frequency cannot be verified statically; state it in the summary.

## Checklist

`is_shown` hides non-qualifying scopes · grey-out reasons in `is_valid` · cost declared once · `ai_*` explicit · all loc sibling keys defined.
