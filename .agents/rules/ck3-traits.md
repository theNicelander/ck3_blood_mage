---
trigger: model_decision
description: Lifestyle traits, tracks, XP progression, and inheritance mechanics.
---

# Traits

Reference: `common/traits/bm_blood_mage_trait.txt`, `bm_crimson_empowerment_trait.txt`.

- **Tracks**: Defined via `tracks = { <track> = { <xp> = { <modifiers> } } }`. Level blocks are explicitly declared; modifying a tier requires updating all affected thresholds.
- **XP gain**: Add progression via `add_trait_xp = { trait = <trait> track = <track> value = <int> }`.
- **Inheritance**:
  - `inherit_chance` and `both_parent_has_trait_inherit_chance`: explicit percentage values (`50` = 50%).
  - `genetic = yes`: activates vanilla recessive genetics. Do not mix with custom script inheritance without explicit purpose.
  - `birth` and `random_creation`: baseline percentages.
- **Eligibility**: Restrict acquisition via `potential = { ... }`.
- **Localization**: Every track requires `<trait>_<track>` and `<trait>_<track>_desc` ([ck3-localization.md](ck3-localization.md)).
- Architecture: see `docs-ai/architecture/blood-mage-traits.md`, `blood-mage-trait-inheritance.md`.
