---
trigger: model_decision
description: Decisions, character interactions and AI behaviour in this mod (costs, validity, ai_* blocks). Read before touching common/decisions, common/character_interactions or any ai_* block.
---

# Decisions, interactions, AI

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
- Reuse `bm_ai_value_modifiers.txt` (self-preservation: health, piety/lifeforce, opinion of target) instead of inline checks.
- Cost and affordability checks go in `is_valid`, not only `ai_will_do`. The AI obeys validity and cost.
- Trait acquisition/retention by AI goes through the prevalence rule (`bm_blood_mage_prevalence_*`), not hard-coded chances.
- Interactions: bound the AI with `ai_targets`; narrow targets are the biggest performance win.
- Can't verify AI behaviour from files. Say so in the summary.

## Checklist

1. Hidden from everyone it shouldn't show to?
2. Every grey-out reason explained?
3. Cost declared once?
4. `ai_*` set deliberately?
5. Loc keys in all 8 languages, `CHANGELOG.md` line added, Tiger clean?
