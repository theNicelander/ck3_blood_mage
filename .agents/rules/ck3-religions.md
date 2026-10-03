---
trigger: model_decision
description: Religions, faiths, rites, doctrines, holy sites and cross-mod compatibility in this mod. Read before touching common/religion or faith-related script/localization.
---

# Religions, Faiths and Rites (CK3 1.20)

> The ground truth is `common/religion/` in vanilla 1.20 (`/Users/clarabotet/Petur/ck3-full/common/religion`).
> In 1.20, religion layout was overhauled. Faiths and rites are distinct top-level database types. Never nest faiths inside religion definitions.

## Folder Layout

The 1.20 religion system is split into specialized subdirectories under `common/religion/`:
- `religion_family_types/`: Defines religious families (`rf_quintessence`). Requires the 4 tenet background banner properties (`tenet_background_icon`, `tenet_heretical_background_icon`, `tenet_neutral_background_icon`, `tenet_unknown_background_icon`).
- `religion_types/`: Defines religions (`quintessence_religion`). Requires `religion_details = { family = ... graphical_faith = ... piety_icon_group = ... }`, holy site constraints (`main_holy_site`, `eminent_holy_sites_max`, `holy_sites_max`), doctrines, traits, and holy orders. **Never put `faiths = { ... }` here.**
- `faith_types/`: Defines individual faiths (`quintessence_faith`). Root-level objects with `faith_details = { religion = ... color = ... icon = ... }`, `main_rite = <rite_key>`, `eminent_holy_sites = { ... }`, `holy_sites = { ... }`, `tenets = { ... }`, and `doctrines = { ... }`.
- `rite_types/`: Defines rites (`common/religion/rite_types/`). Every scripted faith defines a matching mainline rite (`faith = <faith_key>`, `color`, `tenets`, `doctrines`) to prevent the engine from generating unlocalized dynamic rites (`dynamic_rite_%i`).
- `holy_site_types/`: Defines holy sites. Must use `county_holder_character_modifier = { ... }` (county holder if same faith) and `faith_character_modifier = { ... }` (global faith bonus when Eminent). Do NOT use legacy `character_modifier = { ... }`.
- `doctrine_group_types/`: Defines doctrine groups (`category = special`, `doctrine_lock = religion|faith|rite|none`). Never put a `doctrine_types = { ... }` list inside a group.
- `doctrine_types/`: Defines individual doctrines. Must declare mandatory `doctrine_group_type = <group_key>`. Doctrine flags live in `parameters = { <flag> }` (bare name, checked via `has_doctrine_parameter`).
- `tenet_types/`: Vanilla tenets live here (syncretism, sacred shadows, etc.). Mod uses vanilla tenets unless adding unique mechanics.

## Structure & Script Rules

- Hierarchy: family → religion → faith → rite; lower levels override higher.
- Faith Holy Sites: Split into `eminent_holy_sites = { ... }` (up to `eminent_holy_sites_max`, default 3; gives global `faith_character_modifier`) and `holy_sites = { ... }` (regular sites; gives local `county_holder_character_modifier`).
- Mainline Rites: Always script a 1:1 mainline rite in `bm_rite_types.txt` for any new faith, and link it via `main_rite = <rite_key>` in `bm_faith_types.txt`.
- Hidden Identity Doctrine: The hidden doctrine carrying `blood_magic_cult_faith` must have complete UI metadata (`icon`, name key, `visible = no`) and link to its group via `doctrine_group_type`.
- Mutating Faiths: `add_doctrine` mutates the faith for all followers globally: always guard with `NOT = { has_doctrine = x }` and `hidden_effect`.

## Compatibility (non-negotiable)

- Don't redefine a vanilla religion or faith: a same-key definition replaces it and every other mod's changes.
- No `replace_path` for religion folders.
- No `faith:<other_mods_faith>` in this repo. Detect optional mods via global variables or doctrine parameters (`blood_magic_cult_faith`); route conversion through the scripted effect (`bm_religion_conversion_effects.txt`) that companion mods can override.
- Native-faith integration lives in optional companion mods outside this repo.

## Localization

Per faith: `<faith>`, `_adj`, `_adherent`, `_adherent_plural`, `_desc`, plus god/afterlife keys. Mainline rites share the parent faith name by default.
