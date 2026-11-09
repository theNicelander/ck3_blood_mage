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

## Modal send options (`send_options_exclusive = yes`)

CK3 AI evaluates combinations of `send_option` flags including `{}` (all options `no`). If `ai_will_do` does not score options and veto `{}`:
1. **Always set `can_invalidate_interaction = yes`** on every `send_option`.
2. **Score options explicitly**: `modifier = { scope:<option_flag> = yes add = N }`.
3. **Absolute empty-set veto**: End `ai_will_do` with a `factor = 0` veto when no option is picked:
   ```ck3
   modifier = {
       NOR = {
           scope:opt_1 = yes
           scope:opt_2 = yes
       }
       factor = 0
   }
   ```
4. **Branch logs in `on_accept`**: Log the chosen option branch in `if / else_if`, and add an `else` branch logging `(NO OPTION)` fallback.

## Debug logging standards

Every interaction, decision, and fatality execution must output structured `debug_log` for retroactive inspection:
- **Interactions (`on_accept`)**:
  ```ck3
  debug_log = "BloodMageInteraction: <name> (<option>) | Actor: [actor.GetShortUINameNoTooltip] (ID:[actor.GetID], [Select_CString(actor.IsPlayer, 'Player', 'AI')]) -> Recipient: [recipient.GetShortUINameNoTooltip] (ID:[recipient.GetID], [Select_CString(recipient.IsPlayer, 'Player', 'AI')]) | Rel: [actor.Custom2('RelationToMeShort', recipient)] | Tag: [actor.Custom2('bm_debug_relation_tags', recipient)] | Opinion: [actor.GetOpinionOf( recipient )]"
  ```
- **Self-cast interactions (`on_accept`)**:
  ```ck3
  debug_log = "BloodMageSelfCast: <name> (<option>) | Actor: [actor.GetShortUINameNoTooltip] (ID:[actor.GetID], [Select_CString(actor.IsPlayer, 'Player', 'AI')])"
  ```
- **Decisions (`effect`)**:
  ```ck3
  debug_log = "BloodMageDecision: <name> (<item>) | Actor: [root.GetShortUINameNoTooltip] (ID:[root.GetID], [Select_CString(root.IsPlayer, 'Player', 'AI')])"
  ```
- **Fatalities/Executions (`lifedrain_execution_effect`)**:
  ```ck3
  debug_log = "BloodMageExecution: lifedrain | Executioner: [scope:executioner.GetShortUINameNoTooltip] (ID:[scope:executioner.GetID], [Select_CString(scope:executioner.IsPlayer, 'Player', 'AI')]) -> Victim: [scope:victim.GetShortUINameNoTooltip] (ID:[scope:victim.GetID], [Select_CString(scope:victim.IsPlayer, 'Player', 'AI')]) | Rel: [scope:executioner.Custom2('RelationToMeShort', scope:victim)] | Tag: [scope:executioner.Custom2('bm_debug_relation_tags', scope:victim)] | Opinion: [scope:executioner.GetOpinionOf( scope:victim )]"
  ```

## Checklist

`is_shown` hides non-qualifying scopes · grey-out reasons in `is_valid` · cost declared once · `ai_*` explicit · `can_invalidate_interaction = yes` on modal options · empty option set vetoed with `factor = 0` · structured `debug_log` present · all loc sibling keys defined.
