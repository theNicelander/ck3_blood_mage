---
name: add-trait-track
description: >-
  Add or alter lifestyle trait track on Blood Mage or Blood Empowerment trait.
---

# Add or change a trait track

Context: `docs-ai/architecture/blood-mage-traits.md`, `blood-mage-blood-empowerment.md`, `blood-mage-progression.md`, [ck3-traits](../../rules/ck3-traits.md).

## Steps

1. Trait definition: update track and every level block in `common/traits/bm_blood_mage_trait.txt` (or `bm_blood_empowerment_trait.txt`).
2. Update all XP-gated checks testing all tracks (`grep` existing track names).
3. Update XP helper effects in `common/scripted_effects/bm_trait_track_xp_gain_effects.txt`.
4. English loc: track name and description in `bm_traits_l_english.yml`.
5. Update docs and validate.

## Verify

- Track name matches everywhere: `grep -rn "<track_name>" common/ events/ localization/english/`.
- Run `python3 scripts/check_repo.py`.
