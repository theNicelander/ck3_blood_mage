---
trigger: model_decision
description: How to define and work with CK3 religions, faiths, doctrines and holy sites in this mod, including the 1.19 folder layout and compatibility rules. Read before touching common/religion or faith-related script and localization.
---

# CK3 religions, faiths and doctrines

Sources: CK3 wiki (Religions modding, which is tagged outdated), vanilla `game/common/religion/`, and `common/religion/` in this repo.

> [!WARNING]
> The wiki, and many search results, describe the **pre-1.19 layout** (`religion_families/`, `religions/`, `holy_sites/`). In 1.19 these were renamed. Check which layout the current branch uses before adding files. Never keep both layouts, because duplicates silently conflict.

## Folder layout

| 1.19 | Pre-1.19 (do not use on 1.19) |
|---|---|
| `common/religion/religion_family_types/` | `religion_families/` |
| `common/religion/religion_types/` | `religions/` |
| `common/religion/holy_site_types/` | `holy_sites/` |
| `common/religion/doctrine_types/` and `doctrine_group_types/` | doctrines in `religions/` |

Hierarchy: **religion family → religion → faith**. Properties at a lower level override the higher one (faith > religion > family).

## Defining content

- A **religion family** holds shared settings (`graphical_faith`, `doctrine_background_icon`, `hostility_doctrine`, ...).
- A **religion** holds `family`, doctrine groups, holy-order names, and a `faiths = { ... }` block.
- A **faith** needs a full doctrine set: one from each required doctrine group, plus the tenets. A faith with missing groups errors at load. Copy the full set from a similar vanilla faith, or from `bm_religion.txt`.
- Each faith also needs: `color`, `icon` (and `reformed_icon` for the reformed variant), `holy_site = x` entries (generally several, defined in `holy_site_types`), and `religious_head`. The `localization = { ... }` block names god, afterlife, and so on.
- **Holy sites** (`holy_site_types`) link a county and barony and carry a `character_modifier`. County keys must exist in the base map, but see the compatibility rules below.
- **Icons**: faith icons are 100×100 `.dds` files under `gfx/interface/icons/faith/` (doctrine group icons under `gfx/interface/icons/faith_doctrine_groups/`). Reference by filename.
- **Doctrine parameters**: `parameters = { my_param = yes }` on a doctrine. Check with `has_doctrine_parameter = my_param` (on a faith scope or character). This is the hook for optional cross-mod integration, for example `blood_magic_cult_faith`.
- The new hidden doctrine in this mod exists only to carry that parameter. Its `visible = no` and its UI metadata (icon, name key) must still be complete.

## Using religion in script

- Character level: `has_faith = faith:x`, `faith = { ... }`, `religion = { ... }`, `set_character_faith = faith:x`, `religion_tag = x` (inside faith or religion scope), `has_religion = religion:x`.
- Faith level: `has_doctrine = tenet_x`, `has_doctrine_parameter = x`, `add_doctrine = x` (mutates the faith for **everyone**, so guard with `NOT = { has_doctrine = x }` first and use `hidden_effect`).
- Never write `faith:other_mods_faith` in this repo's script. That is a hard dependency. Detect optional mods with global variables or doctrine parameters, and route conversions through scripted effects that the optional companion can override.
- Conversion routing lives in a scripted effect that picks the target faith from the character's previous family (see `bm_religion_conversion_effects.txt` on the 1.19 line).

## Localization for religions

Every religion, faith, family and doctrine needs its key set in all 8 languages. Typical keys per faith: `<faith>`, `<faith>_adj`, `<faith>_adherent`, `<faith>_adherent_plural`, `<faith>_desc`, and the god/afterlife keys the localization block references. Tiger's known "incomplete legacy religion localization" warnings are acknowledged. Do not add new ones.

## Compatibility rules (non-negotiable for this mod)

- The base mod must **not** overlay vanilla or overhaul religion databases. Native-faith integration lives in optional companion mods outside this repo.
- Do not redefine a vanilla religion in this repo. A same-key definition replaces vanilla's entire religion and every mod's changes to it.
- `descriptor.mod` must not carry `replace_path` entries for religion folders.
- Anything that depends on AGOT, Blood of Numenor or any other mod is guarded by a global variable such as `AGOT_is_loaded`, and never by direct references.
