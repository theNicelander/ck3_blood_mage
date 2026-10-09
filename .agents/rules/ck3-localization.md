---
trigger: always_on
description: Localization rules: English only, sibling keys, UTF-8 BOM format.
---

# Localization

- **English only**: Edit `localization/english/` exclusively. Other languages generated separately.
- **Loc documents script**: Script defines mechanics; `localization/english/` defines player-facing behavior. Grep identifier in `localization/english/` to understand intended behavior.
- **Sibling key requirement**: Every entity requires complete sibling keys:
  - Decision: `<id>`, `<id>_desc`, `<id>_tooltip`, `<id>_confirm`.
  - Trait track: `<trait>_<track>`, `<trait>_<track>_desc`.
  - Faith: `<faith>`, `_adj`, `_adherent`, `_adherent_plural`, `_desc`.
  Never add a key without its siblings.
- **Format**: `.yml` must be UTF-8 **with BOM** and trailing newline. Missing keys display raw in UI with no load-time warning.
- Keep comments short; quote loc text directly for context.
