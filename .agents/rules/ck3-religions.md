---
trigger: model_decision
description: Religion, faith, rite, doctrine, and holy site architecture (CK3 1.20).
---

# Religions, Faiths and Rites (CK3 1.20)

Vanilla reference: `/Users/clarabotet/Petur/ck3-full/common/religion`.
1.20 uses split top-level database types. Never nest faiths in religion blocks.

## Directory structure (`common/religion/`)

- `religion_family_types/`: Top-level families (`rf_blodtru`). Requires 4 tenet background icon properties (`tenet_background_icon`, `tenet_heretical_background_icon`, `tenet_neutral_background_icon`, `tenet_unknown_background_icon`).
- `religion_types/`: Religions (`blodtru_religion`). Requires `religion_details` (`family`, `graphical_faith`, `piety_icon_group`), holy site limits (`main_holy_site`, `eminent_holy_sites_max`, `holy_sites_max`), doctrines, traits. **No `faiths = { ... }` blocks.**
- `faith_types/`: Faiths (`blodtru_faith`). Defines `faith_details` (`religion`, `color`, `icon`), `main_rite`, `eminent_holy_sites`, `holy_sites`, `tenets`, `doctrines`.
- `rite_types/`: Rites. Every scripted faith requires 1:1 mainline rite (`faith = <key>`, `color`, `tenets`, `doctrines`) to prevent unlocalized `dynamic_rite_%i` generation.
- `holy_site_types/`: Sites. Must use `county_holder_character_modifier` (holder) and `faith_character_modifier` (eminent). Legacy `character_modifier` invalid in 1.20.
- `doctrine_group_types/`: Groups (`category = special`, `doctrine_lock = religion|faith|rite|none`). No nested doctrine lists.
- `doctrine_types/`: Doctrines. Mandatory `doctrine_group_type = <group_key>`. Flags go in `parameters = { <flag> }` (checked via `has_doctrine_parameter`).
- `tenet_types/`: Tenets. Use vanilla tenets unless adding custom mechanics.

## Rules

- **Hierarchy**: family → religion → faith → rite. Lower level overrides higher.
- **Holy sites**: `eminent_holy_sites` gives global `faith_character_modifier`. Regular `holy_sites` gives local `county_holder_character_modifier`.
- **Mainline rites**: Always link via `main_rite = <rite_key>`.
- **Faith mutation**: `add_doctrine` affects all followers globally. Always guard: `NOT = { has_doctrine = x }`.
- **Hidden doctrines**: Flag doctrines require complete metadata (`icon`, loc key, `visible = no`, `doctrine_group_type`).

## Compatibility

- Never redefine vanilla faith or religion keys (overwrites entire entity).
- Never use `replace_path` for religion folders.
- No direct references to third-party faiths (`faith:<other>`). Guard with global variables or route via scripted effects.

## Localization

Per faith: `<faith>`, `_adj`, `_adherent`, `_adherent_plural`, `_desc`, god and afterlife keys. Mainline rites inherit faith name.
