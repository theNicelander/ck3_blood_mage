---
trigger: model_decision
description: AI behavior for decisions, interactions, and events (ai_will_do, ai_check_interval, ai_targets, personality).
---

# CK3 AI modding

CK3 core AI is hardcoded. Script influences selection likelihood only.

## AI control points

| Context | Keys |
| --- | --- |
| Decision | `ai_check_interval`, `ai_will_do`, `ai_potential` (deprecated in 1.19, still parsed) |
| Character interaction | `ai_targets`, `ai_frequency`, `ai_potential`, `ai_will_do`, `ai_accept` |
| Event option | `ai_chance = { base = N modifier = { ... } }` (relative weight vs other options) |
| Scheme / activity | Specific keys; see vanilla `game/common/<type>/*.info` |

## Weight blocks

```ck3
ai_will_do = {
	base = -10                              # starting value
	modifier = { add = 20 has_trait = ambitious }      # flat addition
	modifier = { factor = 0 has_trait = wounded_1 }    # 0 = absolute veto
	my_scripted_ai_modifier = yes           # common/scripted_modifiers/
}
```

- `add`: shifts running score. `factor`: multiplies running score (`factor = 0` vetoes).
- Modifiers evaluate triggers with implicit `AND`. Cheap triggers first.
- Decisions: `ai_will_do` is percentage chance per check. Events: `ai_chance` values are relative weights.
- Personality scaling: `ai_value_modifier = { <value> = <mult> }`.
  Values: `ai_boldness`, `ai_compassion`, `ai_energy`, `ai_greed`, `ai_honor`, `ai_rationality`, `ai_sociability`, `ai_vengefulness`, `ai_zeal`.

## Check frequency & filtering

- `ai_check_interval = N`: Months between decision checks. `0` = AI disabled.
- `ai_targets`: Restricts interaction candidates (`self`, `dynasty`, `family`, `spouses`, `children`, `courtiers`, `councillors`, `liege`). Critical for performance.
- `ai_potential`: Hard gate. If false, engine skips `ai_will_do`.

## Hard constraints

1. **Conservative tuning**: Balance is hand-tuned. Never raise `base` or lower check intervals without explicit need.
2. **Self-preservation**: Check health, Lifeforce, piety, and target opinion before harmful actions. Reuse scripted modifiers.
3. **Player-only**: Set `ai_check_interval = 0` (decisions) or omit/restrict `ai_potential` (interactions).
4. **Game rules**: Route trait acquisition through mod's rule-aware scripted effects.
5. **No phantom costs**: Put affordability checks in `is_valid`, not just `ai_will_do`.
6. **No AI bypass**: Never use `is_ai = yes` to skip validity or resource costs.
7. **Runtime audit**: AI decision frequency cannot be verified statically; test with `-debug_mode`. State in summary.
