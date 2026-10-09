---
trigger: always_on
description: Core CK3 script rules, script values, and safe engine patterns (1.20).
---

# CK3 scripting

1. **No invented syntax**: CK3 fails silently. Confirm triggers, effects, scopes in vanilla 1.20 (`/Users/clarabotet/Petur/ck3-full`) or `script_docs`.
2. **Percentages**: `random = { chance = N }` and trait `birth` / `random_creation` use percent values (`0.25` = 0.25%).
3. **Scope navigation**: `prev` traverses one level only. Use `save_scope_as` for deep targets.
4. **Null safety**: Guard nullable targets (`liege`, `spouse`, `scope:x`) with `?=` or `exists`.
5. **Mod compatibility**: Non-vanilla keys error without target mod. Guard via global variables (`AGOT_is_loaded`) or doctrine parameters.
6. **Trait audit**: Verify traits and diseases against vanilla 1.20 before writing `has_trait`.
7. **Game rules**: Any non-default behavior requires a game rule. Existing behavior remains default.
8. **Script values**:
   - Centralize numbers used in 2+ locations in `common/script_values/`.
   - Values evaluate in caller's scope. Document scope dependencies in comments.
   - UI-bound values must stay cheap (no iterators/triggers). Use `save_temporary_value_as`.
   - Never use random ranges in costs: re-evaluated every tick.
   - Loc formatting: `[GetPlayer.MakeScope.ScriptValue('x')|0]`.
9. **Inspection**:
   - Files require UTF-8 with BOM (`utf-8-sig`).
   - Use `python3 scripts/read_ck3.py {read|block|search}` to inspect vanilla 1.20 and mod files safely.

Mod architecture: see `docs-ai/architecture/README.md`.
