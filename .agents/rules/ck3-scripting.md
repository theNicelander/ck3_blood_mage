---
trigger: always_on
description: Generic CK3 scripting traps and script values. Always applies when editing common/ or events/.
---

# CK3 scripting

1. CK3 script fails silently. Never invent effect, trigger or scope names. Confirm them in vanilla `game/` files or `script_docs` output and cite where.
2. `random = { chance = N }` and trait `birth` / `random_creation` are percentages (`0.25` = 0.25%).
3. `prev` goes back one level only. Use `save_scope_as` when you need more.
4. Guard possibly empty links (`liege`, `spouse`, `scope:x`) with `?=` or `exists`.
5. Optional-mod keys (faiths, titles, traits) are script errors without that mod. Guard with global variables or doctrine parameters.
6. Verify trait and ailment names against vanilla **1.20** before using them in `has_trait`.
7. New behaviour that changes defaults needs a game rule, and existing behaviour must stay the default.
8. Script values:
   - Make one for any number used in 2+ places.
   - They evaluate in the caller's scope. Document `scope:` requirements (`scope:recipient`, `scope:actor`) in a comment.
   - Keep UI-bound values cheap (no iterators). Use `save_temporary_value_as` for repeated sub-expressions.
   - No random ranges in costs: they re-roll on every read.
   - Display in localization with `[GetPlayer.MakeScope.ScriptValue('x')|0]`.

9. File reading and inspection:
   - CK3 files use UTF-8 with BOM (`utf-8-sig`) and mixed line endings.
   - Use `python3 scripts/read_ck3.py read <file>`, `block <file> <name>`, or `search <pattern>` (or import `scripts.read_ck3`) when analyzing mod or vanilla files (`/Users/clarabotet/Petur/ck3-full`).

Mod-specific conventions (shared effects, story/roster UI, script value files) are in `docs-ai/architecture/`. Start at `docs-ai/architecture/README.md`.
