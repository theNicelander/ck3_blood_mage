---
trigger: model_decision
description: Lifestyle traits, tracks, XP progression, and inheritance mechanics.
---

# Traits

Reference: `common/traits/bm_blood_mage_trait.txt`, `bm_blood_knight_trait.txt`, `bm_blood_power_trait.txt`.

- **Tracks**: Defined via `tracks = { <track> = { <xp> = { <modifiers> } } }`.
  - **Additive Cumulative Stacking**: In CK3 trait tracks, **all reached thresholds add their modifiers together**. Reaching higher XP adds that tier's modifiers ON TOP OF all previous tiers (e.g. reaching 100 XP grants the sum of bonuses from 10, 30, 50, 70, and 100 XP).
  - **Delta Payloads**: Each tier block must declare ONLY the incremental bonus (delta) granted at that milestone, never the full cumulative sum, otherwise modifiers will multiply/stack excessively.
- **XP gain**: Add progression via `add_trait_xp = { trait = <trait> track = <track> value = <int> }`.
- **Inheritance**:
  - `inherit_chance` and `both_parent_has_trait_inherit_chance`: explicit percentage values (`50` = 50%).
  - `genetic = yes`: activates vanilla recessive genetics. Do not mix with custom script inheritance without explicit purpose.
  - `birth` and `random_creation`: baseline percentages.
- **Eligibility**: Restrict acquisition via `potential = { ... }`.
- **Localization**: Every track requires `<trait>_<track>` and `<trait>_<track>_desc` ([ck3-localization.md](ck3-localization.md)).
- Architecture: see `docs-ai/architecture/blood-mage-traits.md`, `blood-mage-prevalence-and-lifecycle.md`.
