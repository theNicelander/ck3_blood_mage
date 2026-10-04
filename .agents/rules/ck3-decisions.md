---
trigger: model_decision
description: Writing or changing CK3 decisions and character interactions (cost, is_shown, is_valid, cooldown, effects, tooltips). Read before touching common/decisions or common/character_interactions.
---

# Decisions and interactions

Copy a nearby decision in `common/decisions/` for structure.

## Traps

- **Never deduct a `cost` in `effect`.** The engine charges it (a double piety charge was a real bug here).
- `is_shown` is evaluated constantly (and per candidate in interactions). Cheap, excluding checks first.
- Costs reused anywhere go in a script value.
- Prefer `cooldown = { ... }` over hand-rolled flags.
- Effects must be safe when run twice, with a missing target, and for the AI.
- Tooltips: `custom_tooltip = { text = key }` for non-obvious lines. Missing keys show raw in UI, not at load.

## AI

- Player-only: disable AI the way vanilla does for that type (`ai_check_interval = 0` for decisions). Check vanilla for interactions.
- Balance is hand-tuned (see `CHANGELOG.md`). Don't raise `base` or shorten intervals without a stated reason.
- Cost and affordability checks go in `is_valid`, not only `ai_will_do`. The AI obeys validity and cost.
- Interactions: bound the AI with `ai_targets`; narrow targets are the biggest performance win.
- Can't verify AI behaviour from files. Say so in the summary.
- Details: `ck3-ai.md`.

## Checklist

1. Hidden from everyone it shouldn't show to?
2. Every grey-out reason explained?
3. Cost declared once?
4. `ai_*` set deliberately?
5. English loc keys added for every sibling key (`ck3-localization.md`), `CHANGELOG.md` line added, Tiger clean?
