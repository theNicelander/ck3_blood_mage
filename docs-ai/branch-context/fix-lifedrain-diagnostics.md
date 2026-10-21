# fix-lifedrain-diagnostics: Lifedrain diagnostics and stored Lifeforce requirement

## Summary & Motivation

Lifedrain execution logs use script-target syntax inside data expressions, causing missing-type errors on CK3 1.20.1.2. The negative stored Lifeforce requirement incorrectly repeats its positive text.

## Core Concepts & Changes

- Resolve the six executioner/victim name, ID and player-status references through `SCOPE.sC(...)` in `lifedrain_execution_effect` diagnostics.
- Preserve the existing character-existence guard and all execution effects, rewards, costs, penalties and cooldowns.
- Keep the upstream `subject = scope:recipient` / `CHARACTER` tooltip binding; correct only the negative requirement wording.
- Update the interaction architecture reference, engine-error catalog, changelog and player release notes.

## Key Decisions

- Base this focused PR on upstream `main` at `b7cd0c8c8ae1394b2a600e3928fd4e85376917e3`; exclude unrelated Russian-localization branch changes and other mods.
- Preserve English localization keys, UTF-8 BOMs, indentation and line endings. Other languages remain generated separately.

## Validation

- Run `python scripts/check_repo.py` against a private snapshot of the pinned upstream base plus this patch.
- Check that only the diagnostic string changes in the execution effect, all six invalid data references are replaced, and the existing nullable-scope guard remains.
- Verify both tooltip keys use `CHARACTER` and the caller supplies `subject = scope:recipient`.
- In-game validation on CK3 1.20.1.2 remains pending: execute one prisoner and mass-lifedrain, inspect `logs/error.log` and `logs/debug.log`, then inspect Siphon Stored Lifeforce on targets with and without reserves.
