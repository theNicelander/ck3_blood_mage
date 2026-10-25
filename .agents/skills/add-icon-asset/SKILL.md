---
name: add-icon-asset
description: >-
  Add or copy DDS icons (interactions, traits, faiths, track icons, rune/spell icons) from the base game.
---

# DDS icons & assets

- Base game source: `/Users/clarabotet/Library/Application Support/Steam/steamapps/common/Crusader Kings III/game/gfx` (`/Users/clarabotet/Petur/ck3-full` has no DDS). Put shortlists for review in gitignored `local-assets/<topic>/`.
- Vanilla styles: `modifiers/*` flat one-colour shield glyph (green good, red bad); `traits/*` illustrated art on a round/square frame; `icon_*.dds` (e.g. `interface/icons/icon_gold.dds`) clean frameless illustrations. Prefer `icon_*` for new rune/spell icons.
- DDS within a category are copy-paste identical:
  - Traits (`gfx/interface/icons/traits/`): `bm_blood_mage.dds`, `bm_blood_knight.dds`, `bm_interactions.dds` (Blood Empowerment).
  - Interactions (`.../character_interactions/`): copies of `bm_interactions.dds` (120×120 blood drop). New interaction: copy `traits/bm_interactions.dds` to `<interaction_key>.dds`.
  - Faiths (`.../faith/`): copies of `bm_blodtru.dds`.
  - Trait tracks (`.../trait_level_tracks/`): per-track icons (`ancient` blood drop from `bm_interactions.dds`, `benediction` physician, `enlightenment` saint/ancestor, `bloodline` augustus, `hematurgy` murderer, `vanguard` faith warrior, `slaughter` raider/reaver).
- Removing or renaming an interaction: remove or rename its `.dds` too (no orphan assets, no missing textures).
