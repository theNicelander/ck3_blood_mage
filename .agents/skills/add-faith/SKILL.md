---
name: add-faith
description: >-
  Use this skill when adding a Quintessence faith, rite or holy site to the
  Blood Mages mod.
---

# Add a faith

Read first: `docs-ai/architecture/blood-mage-religions.md` and [ck3-religions](../../rules/ck3-religions.md).

## Steps

1. Add the faith in `common/religion/faith_types/bm_faith_types.txt`.
2. Add a 1:1 mainline rite in `rite_types/bm_rite_types.txt` and link it with `main_rite`.
3. Holy sites: eminent and regular, with the right modifier types (see the rule).
4. Route conversion for the new heritage in `common/scripted_effects/bm_religion_conversion_effects.txt`.
5. English loc keys: faith, `_adj`, `_adherent`, `_adherent_plural`, `_desc`, god and afterlife keys.
6. Run `update-docs`, then `validate-change`.

## Verify

- The faith key appears in `faith_types`, the rite and the loc file.
- `ck3-tiger` reports no new religion errors.
