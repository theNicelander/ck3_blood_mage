---
trigger: model_decision
description: Lifestyle traits, tracks, XP progression, and inheritance mechanics.
---

# Traits

Reference: `common/traits/bm_blood_mage_trait.txt`, `bm_blood_knight_trait.txt`, `bm_blood_power_trait.txt`.

- **Tracks**: Defined via `tracks = { <track> = { <xp> = { <modifiers> } } }`.
  - **Tier Replacement, Not Stacking**: The CK3 engine does **NOT** accumulate or stack tier modifiers additively. Only the modifier block of the highest reached XP threshold is active.
  - **Full Payload Per Block**: Any modifier intended to persist across multiple tiers (piety, stats, caps, health, advantage) must be explicitly re-declared at its full cumulative value in every subsequent tier block. Any modifier omitted at a higher tier is revoked when reaching that tier.
  - Modifying a tier or adding an intermediate milestone requires updating all affected threshold blocks.
- **XP gain**: Add progression via `add_trait_xp = { trait = <trait> track = <track> value = <int> }`.
- **Inheritance**:
  - `inherit_chance` and `both_parent_has_trait_inherit_chance`: explicit percentage values (`50` = 50%).
  - `genetic = yes`: activates vanilla recessive genetics. Do not mix with custom script inheritance without explicit purpose.
  - `birth` and `random_creation`: baseline percentages.
- **Eligibility**: Restrict acquisition via `potential = { ... }`.
- **Localization**: Every track requires `<trait>_<track>` and `<trait>_<track>_desc` ([ck3-localization.md](ck3-localization.md)).
- Architecture: see `docs-ai/architecture/blood-mage-traits.md`, `blood-mage-prevalence-and-lifecycle.md`.
