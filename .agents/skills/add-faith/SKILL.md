---
name: add-faith
description: >-
  Add Blóðtrú faith, rite, or holy site.
---

# Add a faith

Context: `docs-ai/architecture/blood-mage-religions.md`, [ck3-religions](../../rules/ck3-religions.md).

## Steps

1. Faith definition: `common/religion/faith_types/bm_faith_types.txt`.
2. Mainline rite: define 1:1 in `rite_types/bm_rite_types.txt`; link via `main_rite`.
3. Holy sites: define in `holy_site_types/`. Use `county_holder_character_modifier` (local) and `faith_character_modifier` (eminent).
4. Heritage conversion: hook into `common/scripted_effects/bm_religion_conversion_effects.txt`.
5. English loc: `<faith>`, `_adj`, `_adherent`, `_adherent_plural`, `_desc`, god and afterlife keys.
6. Update docs and validate.

## Verify

- Faith and rite keys resolve in script and loc: `grep -rn "<faith>" common/religion/ localization/english/`.
