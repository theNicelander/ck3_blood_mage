# Localization (`localization/`)

- **English only**: edit `localization/english/` exclusively; other languages generated separately. Grep loc to verify intended mechanics.
- **Sibling keys** (never omit):
  - Decision: `<id>`, `_desc`, `_tooltip`, `_confirm`
  - Trait track: `<trait>_<track>`, `<trait>_<track>_desc`
  - Faith: `<faith>`, `_adj`, `_adherent`, `_adherent_plural`, `_desc`
- **Format**: UTF-8 BOM, trailing newline. Never use `\x27` hex escapes (illegal break error) or `\"` escaped double quotes (`Stray characters after closing quote` in `check_repo.py`); use literal `'`.
- **Trigger loc scoping**: `custom_description` cannot resolve bare `[recipient.GetShortUIName]`. Pass `subject = scope:recipient` + `[CHARACTER.GetShortUIName]` (`object` → `[TARGET_CHARACTER.GetShortUIName]`).
- **Important actions**: never put `($NUM$)` or `(NUM)` in `_combined_group_label` (engine appends count; `$NUM$` renders raw).
- **No hover-text bloat**: keep option hover text (`current_description`, decision/event tooltips) to a concise 1-liner; never repeat stats, costs, multi-tier tables, or native triggers (`piety_level`, `has_trait`, `has_character_modifier`, `gold`, etc.) that CK3 already renders in the effect/cost panel.
- **Vanilla trait & healing terms**: use exact vanilla/CK3 wiki trait names (`Wounded`, `Severely Injured`, `Brutally Mauled`; never `Wounded I/II/III`) and category names (`health traits`, `coping traits`, `old-age traits`; never `ailments` or `afflictions`). Use plain `Heal` in UI/options instead of `Mend`, `Purge`, `Cleanse`, `Cure`, `Eradicate`, or `Dispel`.
