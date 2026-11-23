# Localization (`localization/`)

- **English only**: edit `localization/english/` exclusively; other languages generated separately. Grep loc to verify intended mechanics.
- **Sibling keys** (never omit):
  - Decision: `<id>`, `_desc`, `_tooltip`, `_confirm`
  - Trait track: `<trait>_<track>`, `<trait>_<track>_desc`
  - Faith: `<faith>`, `_adj`, `_adherent`, `_adherent_plural`, `_desc`
- **Format**: UTF-8 BOM, trailing newline. Never use `\x27` hex escapes (illegal break error) or `\"` escaped double quotes (`Stray characters after closing quote` in `check_repo.py`); use literal `'`.
- **Trigger loc scoping**: `custom_description` cannot resolve bare `[recipient.GetShortUIName]`. Pass `subject = scope:recipient` + `[CHARACTER.GetShortUIName]` (`object` → `[TARGET_CHARACTER.GetShortUIName]`).
- **Important actions**: never put `($NUM$)` or `(NUM)` in `_combined_group_label` (engine appends count; `$NUM$` renders raw).
- **No redundant requirement strings**: let CK3 format native triggers (`piety_level`, `has_trait`, `has_character_modifier`, `gold`, etc.).
