---
name: debug-ck3-logs
description: >-
  Snapshot and audit CK3 error.log, debug.log, and crash dumps (exception.txt/meta.yml), and look up known engine error signatures.
  Use first whenever inspecting logs, diagnosing CTDs/startup crashes, debugging silent script failures, or tracing BloodMage* debug_log output.
---

# Debug CK3 Logs & Error Catalog

## 1. Snapshot FIRST (mandatory)

CK3 overwrites `error.log` and `debug.log` on every game launch. **Before any analysis**, snapshot both into gitignored `local-assets/logs/<timestamp>/` and read/grep the snapshot:

```bash
TS=$(date +%Y%m%d-%H%M%S)
mkdir -p "local-assets/logs/$TS"
cp ~/Documents/"Paradox Interactive"/"Crusader Kings III"/logs/error.log "local-assets/logs/$TS/error.log"
cp ~/Documents/"Paradox Interactive"/"Crusader Kings III"/logs/debug.log "local-assets/logs/$TS/debug.log"
```

## 2. Audit

- `error.log`: grep mod prefixes (`bm_`, `blodtru`, mod filenames) + `tail -n 100`.
- `debug.log`: grep `BloodMageInteraction:|BloodMageSelfCast:|BloodMageDecision:|BloodMageExecution:`.

## 2b. Crash dumps (CTDs)

On startup or runtime crash, inspect the latest folder in `~/Documents/Paradox Interactive/Crusader Kings III/crashes/` (`ls -lt` needs `BypassSandbox: true`; `read_file` reads the files directly):

- `exception.txt`: demangled stack trace (pinpoints engine subsystem, e.g. `NPdxMesh::CMeshType::AddMeshToEntity` / `NAssetFactory::LoadAssetsWithProgress` = 3D `.mesh`/`.asset` crash).
- `meta.yml`: exact CK3 version + full active mod list (`Mod_1..N`). Cross-reference the last `error.log` lines against active mods to separate Blood Mages from third-party playset mods.

## 3. Engine error catalog

Living list: on new error, add 1 row (`signature → cause → fix`).

| Signature | Cause → Fix |
| --- | --- |
| `Failed to find type 'recipient'` (trigger loc) | Not root type in trigger loc → pass `subject = scope:recipient` in `custom_description`; use `[CHARACTER.GetShortUIName]` (`object` → `[TARGET_CHARACTER...]`). |
| `Failed to find type 'recipient'` / `does not contain a 'CharacterInteractionConfirmationWindow' data context` (`send_option` loc) | `send_option` `localization` has no `recipient` or GUI window context → use `[GetPlayer.Custom('...')]` for self-only, or `is_shown`-gated `send_option`s with static loc keys for targeted interactions. |
| `Unknown trigger: show_as_unavailable` | Nested in `trigger` → make sibling of `trigger` directly in `option`. |
| `Theme key X ... does not exist` | Invented theme → use vanilla `00_event_themes.txt` (`love`, `family`, `war`, `faith`, `dread`, `witchcraft`, `medicine`, ...). |
| `Event target link 'primary_heir' returned an unset scope` | Heirless actor → use `is_primary_heir_of = scope:actor` or `scope:actor ?= { primary_heir ?= { ... } }`. |
| `Character '(no character)' is not valid in ...` (`debug_log`) | Unset scope in tooltip/empty loop → guard `if = { limit = { exists = scope:x } }`. |
| `Illegal localization break character ('x')` | `\x27` in `.yml` → use literal `'`. |
| `Invalid database object 'x'` | Deleted modifier/trait still referenced → grep & purge triggers, effects, custom loc, loc. |
| `Trait X is marked as good / random creation ... not genetic` | Lifestyle trait has `good = yes`/`random_creation` → remove both; use `random_creation_weight = 0`. |
| AI does forbidden action despite `factor = 0` | Later `add` resurrects score → put `add` first, `factor = 0` vetoes last, + `is_ai` gate in `is_valid_showing_failures_only`. |
| `trigger_else_if with no trigger_else` | Missing terminator → end chain with `trigger_else = { always = no }`. |
| `Unknown trigger: min` (in `modifier`/`ai_will_do`) | `min`/`max` only in script values → use `base` + `modifier = { add = ... }` or script value. |
| `Unknown trigger: employed_as_court_position_of` | Invented → use `any_court_position_employer = { this = scope:actor }`, `has_court_position`, `has_any_court_position`. |
| `Cannot find blood_golem in trait database` | Not a trait → check `house ?= house:bm_house_golem`. |
| `Modifier 'x' was not used by the script or code` | Orphan modifier in `common/modifiers/` → hook into effect or delete + its loc. |
| `Unknown effect: set_character_flag` | CK2 syntax → use `add_character_flag`. |
| `Undefined event target 'recipient'` in `ai_potential` | Runs in actor scope pre-target → move recipient check to `is_valid_showing_failures_only` or `ai_will_do`. |
| `missing localization 'character_named_script_value_greater_or_equal_first'` | Bare script value comparison in trigger tooltip → wrap in `custom_description = { text = ... }`. |
| `remove_trait ... Not found in database 14CTraitDatabase` | Non-vanilla trait key (e.g. `infertile` vs `sterile`) → verify in `00_traits.txt`. |
| `Scoped object is not valid. Type: (no character)` (barony loop) | Empty barony has no holder → guard `barony ?= { holder ?= { ... } }`. |
| `Gfx culture X in Y doesn't match existing sequence` | Multi-entry `*_gfx` order mismatch → match vanilla order or inherit standard (`norse`). |
| `Data error in loc string ... [ROOT.Char...]` / `[root...]` (decision `debug_log`) | Loc promotes on `root` fail in decision `debug_log` → plain string + `debug_log_scopes = yes` in `hidden_effect`. |
| `Cannot find harelip/lisp/blademaster_1/hunter_1` | Vanilla names: `lisping` (no `harelip`), tracked traits `lifestyle_blademaster`/`lifestyle_hunter`. |
| `free_small_botch` / `NPdxMesh::CMeshType::AddMeshToEntity` (`exception.txt`) | Corrupt/outdated 3D `.mesh`/`.asset` mod on new CK3 patch → check last `pdxassetutil.cpp` lines in `error.log` + `meta.yml` mod list (not Blood Mages; BM ships no 3D meshes). |
