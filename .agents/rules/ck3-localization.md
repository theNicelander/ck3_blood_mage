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
- **No Hexadecimal Escapes**: Never use `\x27` or raw hex escape sequences in `.yml` files. The CK3 localization parser does not decode hex escapes and throws illegal break character errors. Use literal apostrophes `'`.
- **Trigger Localization Scoping**: Strings referenced by `custom_description` in character interactions/decisions cannot resolve bare `[recipient.GetShortUIName]`. Always specify `subject = scope:recipient` in script and use `[CHARACTER.GetShortUIName]` (or `[TARGET_CHARACTER.GetShortUIName]` with `object = ...`).
- **Living Catalog**: When identifying new localization pitfalls or syntax errors, record them under `## Common Engine Errors & Pitfalls` in `.agents/rules/ck3-scripting.md`.
- **Concise & direct style (Lifeforce over fluffy flavour)**:
  - Stop using fluffy flavour words like "vitality", "vital arts", "life essence", or vague synonyms when describing actions, alerts, tooltips, or costs. Always be concise, direct, and specify the concrete game term **Lifeforce** (e.g. "spend Lifeforce to heal them", not "channel your vitality").
  - Flavour text belongs strictly in narrative descriptions (e.g. `<decision>_desc` or `<event>.desc` story paragraphs). Outside those narrative bodies, all UI text, tooltips, action descriptions, and toasts must be to the point.
- **Current Situation & Important Actions**:
  - Never put `($NUM$)` or `(NUM)` in `_combined_group_label` (or any group label). The CK3 engine automatically appends the item count to grouped headers in the UI; adding `$NUM$` fails to interpolate and renders raw `(NUM)`.
  - Group and action descriptions must be actionable and concise (e.g. "Several important figures in your life or realm are currently wounded or afflicted by illness. You can spend Lifeforce to heal them.").
- Keep comments short; quote loc text directly for context.
