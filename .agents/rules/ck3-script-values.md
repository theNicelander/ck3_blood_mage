---
trigger: model_decision
description: How to write and use CK3 script values (common/script_values): math, conditionals, scopes, ranges, caching, and showing values in localization. Read before adding costs, thresholds, XP numbers or any computed number.
---

# CK3 script values

Sources: CK3 wiki (Script values, fetched through search because the page itself was not directly readable) and `common/script_values/` in this repo.

## Structure

```
bm_example_cost = {
	value = 50                                  # starting value
	if = {
		limit = { has_trait = lifestyle_blood_mage }
		add = 25
	}
	multiply = scope:target.age                 # scope links are allowed
	min = 10
	max = 500
	round = yes                                 # or floor = yes / ceiling = yes
}
```

- Operations: `value`, `add`, `subtract`, `multiply`, `divide`, `modulo`, `min`, `max`, `round`/`floor`/`ceiling = yes`.
- Operands can be a literal, another script value, a trigger-like scope value (`add = intrigue`), or a scope chain (`add = scope:recipient.piety_level`). Use `multiply = { value = x multiply = y }` blocks for nested math.
- Operations apply **in order, top to bottom**. Put `min`/`max` and rounding last unless you mean otherwise.
- Conditional math: `if = { limit = { ... } add = N }`, with `else_if`/`else`. `limit` is mandatory.
- `save_temporary_value_as = name` stores an intermediate result and `scope:name` or `scope:name.value` reads it back. Use it to avoid recomputing an expensive sub-expression.
- Ranges: `{ 1 5 }` is a random value in a range. `integer_range` and `fixed_range` are available for random integer/decimal. They are re-rolled **every time** the value is read, so do not use them where a stable number is needed.

## Scope rules

A script value is evaluated in the scope of **whatever uses it**. `bm_x_cost` used in a decision's `cost` runs with `root` being the character. The same value used in an interaction runs under that interaction's scope. If it needs `scope:recipient` or `scope:actor`, it is only valid where those exist. Name such values accordingly (`..._per_recipient`), or document the assumption in a comment.

## When to make a script value

- Any number repeated in two or more places (costs, XP thresholds, drain modifiers, durations).
- Anything that should scale with the character (piety cost by rune level, XP gain by attunement).
- Do **not** wrap a single use of a plain literal.

Follow the existing names and files: `bm_*_piety_cost.txt`, `bm_xp_requirement_values.txt`, `bm_drain_duel_values.txt`, `bm_blood_mage_story_values.txt`.

## Performance

- They are recalculated each time they are read, including every frame if shown in the UI. Keep UI-bound values (the Situation panel) cheap, and avoid iterators in them.
- Prefer `save_temporary_value_as` over repeated sub-expressions.

## Using values elsewhere

- In script: anywhere a number is accepted, `cost = { piety = bm_example_cost }`, `add_piety = bm_example_cost`, `compare_modifier = { value = scope:duel_value multiplier = 5 }`.
- In math blocks: `value = bm_example_cost` or `add = bm_example_cost`.
- In localization: `[GetPlayer.MakeScope.ScriptValue('bm_example_cost')|0]`. The suffix sets the format. `|0` for no decimals and `|1` or `|2` for decimals. Add `|V` for colour. Check the repo's `bm_blood_mage_story_l_english.yml` for working examples.
- In AI weights: `add = bm_example_value` inside a `modifier`.

## Checklist

1. Is the value name `bm_`-prefixed and unique (`grep -rn "name =" common/script_values`)?
2. Does every `scope:` it reads exist wherever it is used?
3. Is order of operations right (multiply before add)?
4. Is it deterministic where it must be (no ranges in costs shown twice)?
5. Is the display format in localization appropriate?
