---
name: add-icon-asset
description: >-
  Add or copy DDS icons (interactions, traits, faiths, track icons, rune/spell icons) from base game.
---

# DDS icons & assets

- Base game gfx: `/Users/clarabotet/Library/Application Support/Steam/steamapps/common/Crusader Kings III/game/gfx` (`ck3-full` has no DDS). Put review shortlists in gitignored `local-assets/<topic>/`.
- Styles: `modifiers/*` flat 1-color shield (green good, red bad); `building_types/*` `128×128` flat `#000000` monochrome stencil (~`112×112` centered fill, transparent negative-space cutouts — CK3 GUI shader tints dynamically); `traits/*` framed art; `icon_*.dds` frameless illustrations (prefer for runes/spells).
- Mod conventions:
  - Generic fiery blood drop (`gfx/interface/icons/bm_blood_magic_icon.dds`): use for events, decisions, and GUI texticons (keep `trait_level_tracks/ancient.dds` for the `ancient` track only).
  - Modifiers (`gfx/interface/icons/modifiers/`): `bm_blood_magic` (white: blessings/dynasty/rites), `bm_blood_magic_positive` (green `(114,137,91)`: lifeforce), `bm_blood_magic_negative` (red `(145,71,68)`: drain/curses/strain). Generate from pure `#FFFFFF` on `#000000` master → 60×60 mottled texture + drop shadow → uncompressed 32-bit BGRA `.dds`.
  - Building icons (`gfx/interface/icons/building_types/`): generate pure `#000000` on `#FFFFFF` flat stencil (zero color/shading/gradients) → crop tight & scale to ~`112×112` centered in `128×128` → write `(0,0,0,A)` 32-bit BGRA `.dds` → visually compare side-by-side against decoded vanilla `building_types/*.dds` before committing. Check no `type_icon` collides with shared vanilla sub-buildings in the same district.
  - Traits (`gfx/interface/icons/traits/`): `bm_blood_mage.dds`, `bm_interactions.dds`.
  - Interactions (`.../character_interactions/`): copy `traits/bm_interactions.dds` → `<interaction_key>.dds` (120×120 blood drop).
  - Faiths (`.../faith/`): copy `bm_blodtru.dds`.
  - Trait tracks (`.../trait_level_tracks/`): `ancient` (`bm_interactions.dds`), `benediction` (physician), `enlightenment` (saint/ancestor), `bloodline` (augustus), `hematurgy` (murderer), `bloodlust` (raider/reaver).
- Sync rename/delete of interactions with their `.dds` (no orphans or missing textures).
