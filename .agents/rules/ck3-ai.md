---
trigger: model_decision
description: How to write AI behaviour for CK3 decisions, interactions and event options (ai_will_do, ai_check_interval, ai_targets, weights, personality values). Read before adding or changing any ai_* block.
---

# CK3 AI modding patterns

Sources: CK3 wiki (AI modding, fetched through search because the page itself was not directly readable) and this repo's tuned AI. Much of CK3's AI is hardcoded. Script can only influence **how likely** the AI is to pick an action.

## Where AI is controlled

| Context                    | Keys                                                                                                    |
| -------------------------- | ------------------------------------------------------------------------------------------------------- |
| Decision                   | `ai_check_interval`, `ai_will_do`, `ai_potential` (deprecated warning in 1.19; existing uses are known) |
| Character interaction      | `ai_targets`, `ai_frequency`, `ai_potential`, `ai_will_do`, `ai_accept` (the recipient's acceptance)    |
| Event option               | `ai_chance = { base = N modifier = { ... } }` (relative weights between options)                        |
| Scheme / activity / others | Own keys. Read the `.info` file in vanilla `game/common/<type>/`                                        |

## Weight blocks

```
ai_will_do = {
	base = -10                              # starting value
	modifier = { add = 20 has_trait = ambitious }      # flat change when the triggers pass
	modifier = { factor = 0 has_trait = wounded_1 }    # multiply; 0 vetoes the action
	ai_willingness_to_do_postitive_magic = yes # a scripted modifier (see bm_ai_value_modifiers.txt)
}
```

- `add` shifts the number. `factor` multiplies the running total. `factor = 0` is the standard veto. `base` is where it starts.
- Triggers inside a `modifier` are an implicit `AND`. A failing trigger stops evaluation of that modifier block, so put the cheapest first.
- Each `modifier` is applied independently. Order matters for `factor` versus `add`.
- For decisions, `ai_will_do` is read as a percentage chance each time the check interval fires. For event options, `ai_chance` values are **relative weights** (10 vs 30 is 25% vs 75%).
- Use `ai_value_modifier = { ai_zeal = 0.5 }` (personality-weighted adds) to tie behaviour to character personality. Common values are `ai_boldness`, `ai_compassion`, `ai_energy`, `ai_greed`, `ai_honor`, `ai_rationality`, `ai_sociability`, `ai_vengefulness`, `ai_zeal`.

## Check frequency

- `ai_check_interval = N` (decisions) is in months. `0` means the AI never evaluates it. Use a large interval for expensive triggers.
- `ai_frequency = N` (interactions) works similarly, and `ai_targets` limits who the AI may target (`self`, `dynasty`, `family`, `spouses`, `children`, `courtiers`, `councillors`, `liege`, ...). Narrow targets are the biggest performance win.
- `ai_potential` is a pre-filter. If it fails, the AI never reaches `ai_will_do`.

## Rules for this repo

1. **Conservative changes.** This mod's AI balance was tuned by hand and is logged in `CHANGELOG.md`. Do not raise `base` or shorten intervals without a stated reason.
2. **Self-preservation first.** The AI should check its own health, resources (piety/lifeforce) and its opinion of the target before harmful or costly actions. Copy the pattern in `bm_ai_value_modifiers.txt` rather than writing new inline checks.
3. **Player-only actions** use `ai_check_interval = 0` (decisions) or no `ai_potential = { always = yes }` (interactions).
4. **Respect the prevalence game rule.** AI acquisition and retention of the Blood Mage trait must go through the rule-aware effects and modifiers (`bm_blood_mage_prevalence_*` on the 1.19 line) and not hard-coded chances.
5. **No hidden AI costs.** If an interaction charges a cost, the AI must be unable to take it when it cannot afford it (check in `is_valid` and not only in `ai_will_do`).
6. **Do not use `is_ai = yes` to bypass validity.** Validity and cost apply to the AI too.
7. **Test with `-debug_mode`.** Watch whether the AI actually uses the decision or interaction over several game years. You cannot verify this from the files, so say so in your summary.
