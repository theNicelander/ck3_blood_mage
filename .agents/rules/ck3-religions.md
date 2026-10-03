---
trigger: model_decision
description: Religions, faiths, doctrines, holy sites and cross-mod compatibility in this mod. Read before touching common/religion or faith-related script/localization.
---

# Religions and faiths

> Wiki and search results often describe a different folder layout than this repo. **The ground truth is `game/common/religion/` in the vanilla install plus the existing `common/religion/` here.** Check it before adding files. Duplicate layouts conflict silently.

## Structure

- Hierarchy: family → religion → faith; lower levels override higher.
- A faith needs a complete doctrine set (copy from `bm_religion.txt` or a similar vanilla faith), `color`, `icon` (+ `reformed_icon`), several `holy_site` entries, `religious_head`, and a `localization` block.
- Icons: 100×100 `.dds` under `gfx/interface/icons/faith/` (doctrine groups: `faith_doctrine_groups/`).
- The hidden doctrine carrying `blood_magic_cult_faith` must still have complete UI metadata (icon, name key) despite `visible = no`.
- `add_doctrine` mutates the faith for everyone: guard with `NOT = { has_doctrine = x }` and `hidden_effect`.

## Compatibility (non-negotiable)

- Don't redefine a vanilla religion: a same-key definition replaces it and every other mod's changes.
- No `replace_path` for religion folders.
- No `faith:<other_mods_faith>` in this repo. Detect optional mods via global variables or doctrine parameters; route conversion through the scripted effect (`bm_religion_conversion_effects.txt`) that companion mods can override.
- Native-faith integration lives in optional companion mods outside this repo.

## Localization

Per faith, all 8 languages: `<faith>`, `_adj`, `_adherent`, `_adherent_plural`, `_desc`, plus god/afterlife keys. Don't add new "incomplete legacy religion localization" warnings.
