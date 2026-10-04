---
trigger: model_decision
description: Writing CK3 traits with tracks, XP, inheritance and level modifiers. Read before touching common/traits.
---

# Traits

Read the existing lifestyle trait file in `common/traits/` for working syntax.

- Lifestyle traits have `tracks = { <track> = { <xp> = { modifiers } } }`. Per-level blocks are written out by hand, so changing a bonus means editing every level.
- XP is added with `add_trait_xp = { trait = X track = Y value = N }`.
- Inheritance: `inherit_chance` and `both_parent_has_trait_inherit_chance` are explicit percentages. `genetic = yes` routes through CK3's recessive system. Don't mix without a reason. `birth` and `random_creation` are percentages, and Tiger may warn on non-genetic traits (needs a justified `#tiger-ignore`).
- `potential` gates who may have the trait.
- Each track needs localization for name and description (`ck3-localization.md`).
- This mod's trait, tracks and inheritance are described in `docs-ai/architecture/`. Start at its `README.md`.
