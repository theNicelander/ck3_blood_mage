---
trigger: model_decision
description: Patterns for CK3 character and trait scripting (traits with tracks, XP, inheritance, create_character, modifiers, flags, variables, stories). Read before editing traits or effects that change characters.
---

# CK3 characters and traits

Sources: CK3 wiki (Characters modding), vanilla traits, and `common/traits/` in this repo. See also `llm_context/traits.txt` and `llm_context/trait-inheritance.txt`.

## Traits

- Defined in `common/traits/`. Core fields: `category` (`lifestyle` for tracked traits), `icon`, `desc`, `flag`, modifier blocks, and for tracked traits `tracks = { <track> = { <xp threshold> = { modifiers } } }`.
- **Track XP**: `add_trait_xp = { trait = lifestyle_blood_mage track = hematurgy value = 5 }`. `trait_xp` / `has_trait_xp` read it. Track names are the five disciplines (ancient, enlightenment, bloodline, benediction, hematurgy).
- **Inheritance**: `inherit_chance` and `both_parent_has_trait_inherit_chance` are percentages. `birth` and `random_creation` are also percentages, so `0.25` means 0.25%. The trait uses manual inheritance and **must not gain `genetic = yes`, `good`, or `group` without discussion**.
- `potential = { ... }` limits who can ever have the trait. The prevalence game rule uses it.
- Always grant the trait with the shared effect (`bm_become_blood_mage_effect = yes` on 1.19 lines) and not with a bare `add_trait`. The shared effect creates the story cycle for the roster UI.
- Traits you remove or rename in vanilla may break `has_trait` checks. Verify names against vanilla 1.19 (for example `lunatic_1` instead of `lunatic`).

## Character effects and triggers

- Traits: `add_trait = x`, `remove_trait = x`, `has_trait = x`, `add_trait_xp`.
- Modifiers: `add_character_modifier = { modifier = x years = N }`, `remove_character_modifier = x`, `has_character_modifier = x`. A modifier's text needs `x` and `x_desc` localization.
- Flags and variables: `add_character_flag`, `has_character_flag`, `set_variable`, `var:x`. Flags are for temporary state. Variables for numbers and scopes.
- Resources: `add_piety`, `add_prestige`, `add_gold`, `piety_level`, `current_weighted_gold`. Do not subtract a cost that the decision or interaction already charges.
- Relations and opinion: `add_opinion = { target = scope:x modifier = my_opinion opinion = 20 }` (the modifier must exist in `common/opinion_modifiers/`), `has_relation_*`, `set_relation_*`.
- Health: `add_trait = wounded_1`, `remove_trait = infirm`, `make_wounded`. Check the exact 1.19 ailment names (`withering_mind`, `clouded_eyes`, `fragile_bones`, `faltering_heart`).
- Death: `death = { death_reason = my_reason killer = scope:x }`. The reason must be defined in `common/deathreasons/`.

## Creating characters

```
create_character = {
	template = bm_blood_golem_template      # preferred: reuse a scripted_character_template
	location = root.capital_province
	dynasty = root.dynasty
	save_scope_as = new_golem               # saved so later effects can use scope:new_golem
	after_creation = { add_trait = strong }
}
```

- Prefer `common/scripted_character_templates/` over giant inline blocks, so the same character can be created from multiple paths.
- Save the new character with `save_scope_as` inside `create_character`. Use it afterwards through `scope:name`.
- Without `location` or `employer`, characters may spawn into limbo. Choose one.
- `age`, `gender`/`female`, `culture`, `faith`, `random_traits`, `trait`, and `dna` are all optional. Check vanilla for exact spelling. Names change between versions.
- Do not create characters inside iterators or `while` without a cap.

## Stories and rosters (this mod)

- The Blood Magic panel in the Situations window depends on a **story cycle** attached to the Blood Mage. Anything that gives the trait or creates a golem/retinue member must go through the shared effects so the story is created or reconciled.
- Story state is read by `common/scripted_guis/` and displayed with customizable localization. When adding fields, update the story effects, scripted GUI, localization, and `window_situation_list.gui`, in that order.
- Keep `window_situation_list.gui` edits inside the Blood Mage sections. The rest is a byte-identical copy of vanilla.

## Quick safety checklist

- Is every scope in the block the right type (character vs faith vs title)?
- Does anything dereference a link that could be empty (`liege`, `spouse`, `scope:x`)? Use `?=` or `exists`.
- Does the effect behave if the target already has the trait/modifier?
- Does a new modifier/trait/flag key have localization in all languages?
