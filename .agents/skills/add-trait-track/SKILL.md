---
name: add-trait-track
description: >-
  Use this skill when adding or changing a lifestyle trait track on the Blood
  Mage trait.
---

# Add or change a trait track

Read first: `docs-ai/architecture/blood-mage-traits.md`, `blood-mage-crimson-empowerment.md`, `blood-mage-progression.md` and [ck3-traits](../../rules/ck3-traits.md).

## Steps

1. Edit the track and every level in `common/traits/bm_blood_mage_trait.txt`.
2. Update every XP-gated check that tests all tracks (grep for the existing track names).
3. Update the XP helper effects in `common/scripted_effects/bm_trait_track_xp_gain_effects.txt`.
4. English loc for track name and description in `bm_traits_l_english.yml`.
5. Update the traits doc (`update-docs`), then `validate-change`.

## Verify

- `grep -rn "<track name>" common events localization/english` shows every place that lists tracks.
