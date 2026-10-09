---
trigger: model_decision
description: Decisions and character interactions (cost, is_shown, is_valid, cooldown, effects, tooltips).
---

# Decisions and interactions

Structure: copy neighboring file in `common/decisions/` or `common/character_interactions/`.

## Script traps

- **Never deduct `cost` inside `effect`**. Engine charges declared `cost` automatically.
- `is_shown` evaluates constantly. Put cheap exclusionary triggers first.
- Reused costs: declare in `common/script_values/`.
- Prefer native `cooldown = { ... }` over custom character flags.
- Re-entrancy: effects must be safe if fired twice, targeting missing scopes, or run by AI.
- Tooltips: `custom_tooltip = { text = key }` for non-obvious outcomes. Missing loc keys render raw in UI.

## AI constraints

- Player-only: set `ai_check_interval = 0` (decisions) or restrict `ai_potential` (interactions).
- Tuning: do not raise `base` or shorten check interval without stated reason.
- Put cost and affordability triggers in `is_valid`, not just `ai_will_do`.
- Bound interactions with `ai_targets`.
- See [ck3-ai.md](ck3-ai.md).

## Checklist

1. Hidden from non-qualifying scopes (`is_shown`)?
2. Grey-out conditions explained in `is_valid`?
3. Cost declared once in cost block?
4. `ai_*` explicitly defined?
5. English loc defined for all sibling keys ([ck3-localization.md](ck3-localization.md))?
