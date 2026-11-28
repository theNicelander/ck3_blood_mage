# Religion (`common/religion/`, CK3 1.21+)

Vanilla ref: `/Users/clarabotet/Petur/ck3-full/common/religion`. Spec: `docs-ai/architecture/blood-mage-religions.md`.
1.20 uses split top-level folders; never nest `faiths = {}` in religion blocks.

- **Layout & rules**:
  - `religion_family_types/` (`rf_blodtru`): needs 4 tenet bg icons (`tenet_{heretical_,neutral_,unknown_,}background_icon`).
  - `religion_types/` (`blodtru_religion`): `religion_details` (`family`, `graphical_faith`, `piety_icon_group`), holy site limits (`main_holy_site`, `eminent_holy_sites_max`, `holy_sites_max`), doctrines, traits.
  - `faith_types/` (`bm_faith_types.txt`): `faith_details` (`religion`, `color`, `icon`), `main_rite`, `eminent_holy_sites`, `holy_sites`, `tenets`, `doctrines`.
  - `rite_types/` (`bm_rite_types.txt`): 1:1 mainline rite per faith linked via `main_rite` (prevents unlocalized `dynamic_rite_%i`). Mainline rites inherit faith name.
  - `holy_site_types/`: use `county_holder_character_modifier` (local) + `faith_character_modifier` (eminent). Legacy `character_modifier` invalid in 1.20.
  - `doctrine_group_types/`: `category = special`, `doctrine_lock = religion|faith|rite|none`; no nested doctrine lists.
  - `doctrine_types/`: mandatory `doctrine_group_type = <group>`; flags in `parameters = { <flag> }` (`has_doctrine_parameter`). Hidden flag doctrines need `icon`, loc, `visible = no`, `doctrine_group_type`.
- **Hierarchy**: family → religion → faith → rite (lower overrides higher).
- **Mutation**: `add_doctrine` is global; guard with `NOT = { has_doctrine = x }`.
- **Add faith checklist**: define in `bm_faith_types.txt` → 1:1 rite in `bm_rite_types.txt` → holy sites → hook `common/scripted_effects/bm_religion_conversion_effects.txt` → English loc (`<faith>`, `_adj`, `_adherent`, `_adherent_plural`, `_desc`, god/afterlife) → grep `common/religion/ localization/english/`.
