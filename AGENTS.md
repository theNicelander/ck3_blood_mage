# AGENTS.md — Blood Mages (CK3 mod)

Guidelines for AI agents working in this repository. CK3 script is a custom Paradox format with strict, silent failure modes. When in doubt, follow the patterns already in this repo and vanilla CK3 rather than inventing syntax.

## What this mod is

- A Crusader Kings III mod targeting **CK3 1.19.\*** (see `descriptor.mod`).
- It adds the `lifestyle_blood_mage` trait (5 disciplines/tracks: ancient, enlightenment, bloodline, benediction, hematurgy), Major/Minor Lifeforce, decisions and character interactions, blood golems, the Crimson Empowerment trait, a Cult of Quintessence religion family, game rules, and a custom Blood Magic panel in the Situations window.
- Pure script, GUI, localization and gfx. There is no build step and no compiled code.
- `scripts/` holds a Steam Workshop publishing helper (bash). Never touch `.env`, credentials, or `*.vdf` files.

## Detailed rules (read the one that matches your task)

Deeper CK3 patterns live in `.agents/rules/`:

- `ck3-scripting.md`: scopes, iterators, effects, triggers, scripted effects, script values, events.
- `ck3-decisions.md`: decisions and character interactions, with a checklist.
- `ck3-religions.md`: religions, faiths, doctrines and holy sites, including the 1.19 layout.
- `ck3-characters.md`: traits, XP tracks, characters, stories.
- `ck3-ai.md`: `ai_will_do`, `ai_check_interval`, interaction targeting, weights.
- `ck3-script-values.md`: script values, math, scopes, localization formatting.
- `pr-context.md`: persisting branch/PR context, core concepts, and key decisions in `docs-ai/<pr-name>.md`.

## Branch awareness

Parts of this file describe the **1.19 line** (PR #94): the `religion_types` layout, `bm_become_blood_mage_effect`, the game rules, the story cycle and GUI. A branch based on the older `main` may still have `religions/`, `religion_families/`, `holy_sites/` and a bare `add_trait = lifestyle_blood_mage`. **Check what the current branch actually contains before applying a rule**, and do not mix layouts. When porting a change from the PR, port its dependencies (shared effects, localization, game rules) with it.

## Repository layout

| Path | Purpose |
|---|---|
| `common/<type>/` | Game data. Subfolders mirror vanilla (`traits`, `decisions`, `character_interactions`, `scripted_effects`, `scripted_triggers`, `scripted_modifiers`, `script_values`, `modifiers`, `on_action`, `story_cycles`, `scripted_guis`, `game_rules`, `religion/*`, ...) |
| `common/religion/` | 1.19 layout: `religion_types`, `religion_family_types`, `holy_site_types`, `doctrine_types`, `doctrine_group_types`. Do **not** use the old `religions/`, `holy_sites/` and `religion_families/` folders. |
| `events/` | Event files, one namespace per file |
| `gui/` | `.gui` files. `window_situation_list.gui` is a **full copy of the vanilla window**. Treat it as fragile. |
| `gfx/` | Icons, portrait modifiers (`gfx/portraits/trait_portrait_modifiers/`) |
| `localization/<language>/` | `.yml` per language. English is the source. |
| `llm_context/` | Reference notes about CK3 for LLMs (traits, modifiers, effects). Read them before writing new content. |
| `docs/` | Images used by README/Workshop. Put images here only. |
| `docs-ai/` | Written documentation for humans and agents (e.g. PR reviews, `docs-ai/<pr-name>.md` branch/PR context docs). Put new `.md` docs here, not in `docs/`. |
| `steam-workshop/`, `description.txt`, `description.md`, `README.md`, `CHANGELOG.md` | Release material |

## Naming conventions

- Prefix **every** new file and identifier with `bm_` (or the existing `blood_mage_`, `bm_` namespaces) to avoid clashes with vanilla and other mods. One file per feature, named `bm_<feature>.txt`.
- Do not reuse vanilla filenames unless you intend to overwrite them. Vanilla loads files alphabetically, and **later definitions of the same key win** (for most types). An unprefixed file is a deliberate override.
- Event namespaces: declare `namespace = <name>` at the top, and name events `<namespace>.<number>`. Namespace names in this repo are mixed, so look at the neighbouring file.
- Scripted effects/triggers end in `_effect` / `_trigger` (existing code is not fully consistent) and are called with `= yes`: `bm_become_blood_mage_effect = yes`.
- Game rules use `bm_` keys and their settings are `has_game_rule = bm_<rule>_<setting>`.

## File format rules (these break the game if wrong)

1. **Encoding**: all `.txt`, `.gui` and `.yml` files are **UTF-8 with BOM**, matching existing files. Check with `file <path>` before and after editing. Never strip the BOM, and don't add a BOM in the middle of a file.
2. **Line endings**: many files use CRLF. Preserve each file's existing line endings. Do not convert whole files, because it destroys the diff.
3. **Indentation**: existing files mix tabs and 4 spaces. Match the file you are editing. Do not reformat unrelated lines.
4. **Braces**: Paradox script is `key = value` and `key = { ... }`. Operators are `=`, `>`, `<`, `>=`, `<=`, `!=` (and `?=` for "only if scope exists"). There are no commas or semicolons. An unbalanced `}` can break the rest of the file silently.
5. **Comments** start with `#`. Preserve existing comments. Add `#tiger-ignore(key=...)` only with a justification comment, as existing code does.
6. **Trailing newline**: end every file with a newline.

## Scripting rules

- **Scopes matter.** Every trigger and effect works in a specific scope (`character`, `title`, `faith`, `culture`, ...). `root`, `prev` and `this` change meaning inside nested blocks. Saved scopes are `scope:name`. In a character interaction, `scope:actor` and `scope:recipient` are available. In a decision, `root` is the deciding character. If unsure which scope a block is in, do not guess. Look at a vanilla example or `llm_context/`.
- **Triggers vs effects.** Triggers go in `trigger`, `limit`, `is_shown`, `is_valid`, `potential`, `ai_potential`. Effects go in `effect`, `immediate`, `option`, `after`. Do not put effects inside trigger blocks, or the reverse.
- **Conditionals**: `if = { limit = { ... } ... }`, `else_if = { limit = { ... } }`, `else = { ... }`. A `limit` is required on `if` and `else_if`. In triggers use `trigger_if = { limit = ... }` / `trigger_else`. Do not mix the effect and trigger forms.
- Use `OR`, `AND`, `NOT`, `NOR`, `NAND` blocks explicitly. A top-level block is an implicit `AND`.
- `random = { chance = N ... }` takes a percentage 0–100. For trait generation fields like `birth` and `random_creation`, the value is also a percentage (0.25 = 0.25%).
- **Script values** are defined in `common/script_values/` and used as `scope:x.my_value` or directly in math. Prefer a script value over magic numbers repeated in several places (see `bm_xp_requirement_values.txt`, `bm_*_piety_cost.txt`).
- **Reuse the shared effects** instead of copying code. For example, always use `bm_become_blood_mage_effect = yes` rather than `add_trait = lifestyle_blood_mage`. The shared effect also creates the story cycle for the roster UI, and bypassing it breaks that.
- **Trait experience** is changed with `add_trait_xp = { trait = lifestyle_blood_mage track = <track> value = N }`. The track names are the five disciplines above.
- Respect the **game rules** (`has_game_rule = ...`) for features that have one: prevalence, appearance, lore, and initiation requirements. New behaviour that changes defaults needs a game rule, with the existing behaviour as the default.
- **AI**: decisions and interactions need `ai_check_interval`, and `ai_will_do` / `ai_potential` as appropriate. `ai_check_interval = 0` disables AI use. Keep AI changes conservative. This mod's AI balance was tuned by hand (see `CHANGELOG.md`).
- **Do not hard-depend on other mods.** Optional compatibility must use checks such as `has_global_variable = AGOT_is_loaded` or doctrine parameters (`blood_magic_cult_faith`), never direct references to another mod's traits, faiths or titles. An unknown token is a script error for players without that mod. Optional submods live outside this repo.
- Do not use removed or changed 1.19 syntax. Check the vanilla 1.19 files, `ck3-tiger` output, or in-game `error.log`.

## Localization rules

- English is the source language. Supported languages: english, french, german, korean, polish, russian, simp_chinese, spanish (`translation-config.json`).
- Header line is `l_<language>:` on the first line. Keys are indented one or more spaces: `  my_key: "Text"` or `  my_key:0 "Text"`. Match the surrounding file.
- Escape quotes inside text as `\"` and newlines as `\n`.
- Every key used in script (titles, descs, option names, trigger/effect tooltips, modifier names, traits, game rules) needs an entry. Modifier descriptions use `<modifier_key>_desc`. Event text uses `<event_id>.t`, `.desc`, `.a` (or follow the repo's `.title` / `.desc` / `.a` style).
- Use **mod-scoped keys** (`bm_...`). Do not reuse or override vanilla keys. Duplicate keys across files cause conflicts. Search for the key before adding it: `grep -rn "my_key" localization/english`.
- Formatting and references: `[GetTrait('x').GetName(...)]`, `$other_key$`, `#bold text#!`, `@icon!`, `#tooltip:key text#!`. Check that brackets balance.
- When adding or changing an English string, **add the key to every other language folder**. If you can't translate it, copy the English text rather than leaving the key missing, and say so in your summary. Don't machine-translate religious terms without checking existing translations.
- Event localization lives in `localization/<lang>/event_localization/`.

## GUI rules

- GUI files use the same brace syntax but a different vocabulary (`widget`, `vbox`, `hbox`, `text_single`, `datacontext`, `tooltip`, `using = ...`, data-binding in `[...]`). Errors show up only in game.
- `gui/window_situation_list.gui` replaces the vanilla file path exactly. A CK3 patch that changes vanilla's file will not be reflected here. Any edit must stay inside the Blood Mage sections and keep the vanilla parts byte-identical.
- Mod-specific text icons live in `gui/bm_*_texticons.gui`. Add new icons there, with a `bm_` prefix.

## Workflow for changes

1. When working on a branch or PR, check `docs-ai/<pr-name>.md` to load the current state, core concepts, and key decisions before starting work. Read relevant existing files and `llm_context/` before writing.
2. Make the smallest change that works. Do not reformat, rename or reorder unrelated code.
3. If you add a new key, effect, trigger or value, search the repo to confirm it is not already defined (`grep -rn "name =" common`).
4. Update localization (all languages, see above).
5. Add a line to `CHANGELOG.md` under the current unreleased version for any user-visible change, and update `README.md` if the feature is documented there.
6. Keep `docs-ai/<pr-name>.md` updated with the current state (summary/motivation, core concepts/high-level additions, key decisions). Omit minor edits like renames or file moves.
7. Validate:
   - `git diff --check` for whitespace errors.
   - **CK3-Tiger** (`ck3-tiger`) against the matching game version is the main static validator. Treat new errors as blockers. Existing warnings (deprecated `ai_potential`, legacy religion localization) are known.
   - Ask the user to check `error.log` in `Documents/Paradox Interactive/Crusader Kings III/logs/` after a test run. You cannot launch the game.
8. Tell the user what you could not verify. In-game behaviour (UI layout, AI behaviour, portraits) cannot be confirmed from the files alone.

## Things to avoid

- Don't change `descriptor.mod` (`name`, `remote_file_id`, `version`) unless asked. It controls the Workshop identity.
- Don't edit or delete `thumbnail*.png`, `steam-workshop/` images, or files in `docs/` without being asked.
- Don't commit secrets (`.env`, `*.vdf`, logs).
- Don't add `genetic = yes`, `good`, or a `group` to the Blood Mage trait without discussing it. That was a deliberate trait-inheritance decision, and it affects the UI and inheritance.
- Don't delete third-party compatibility code (for example Blood of Numenor handling or the AGOT checks) without asking.
- Don't invent effect, trigger or scope names. If you are not certain one exists in 1.19, find it in vanilla files or the `script_docs` output and cite where.
- Don't add `replace_path` entries in `descriptor.mod`. They wipe vanilla content.

## Useful references

- CK3 modding wiki: <https://ck3.paradoxwikis.com/Modding> (and sub-pages: Effects, Triggers, Scopes, Events, Decisions, Localization, Traits, Game rules). The wiki can lag behind the current patch.
- In-game docs: run the game with `-debug_mode` and use the `script_docs` console command to dump `effects.log`, `triggers.log` and `event_scopes.log` for your exact version.
- Vanilla files in the game install under `game/` are the ground truth for syntax.
- CK3-Tiger: <https://github.com/amtep/ck3-tiger>
