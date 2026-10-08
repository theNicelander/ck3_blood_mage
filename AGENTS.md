# AGENTS.md — Blood Mages (CK3 mod)

CK3 script fails silently. Follow patterns already in this repo and in vanilla 1.19 rather than inventing syntax.

## What this is

- CK3 mod for **1.20.\***. Pure script, localization, gfx. No build step.
- Adds the `lifestyle_blood_mage` trait (tracks: ancient, enlightenment, bloodline, benediction, hematurgy), Lifeforce, decisions/interactions, blood golems, Crimson Empowerment, the Blóðtrú religion family, game rules.
- `scripts/` holds a Steam Workshop helper. Never touch `.env`, credentials or `*.vdf`.

## Context layers

| Layer | Answers | Scope |
| --- | --- | --- |
| Rules `.agents/rules/*.md` | How do I write this kind of CK3 thing without breaking it? | Generic CK3 plus hard repo constraints. No `bm_` identifiers |
| Skills `.agents/skills/<name>/SKILL.md` | What are the steps for task X here? | Repeatable multi-file procedures |
| Architecture `docs-ai/architecture/*.md` | How does this mod implement it? | Mod only. Start at its `README.md` |

Rules: `ck3-scripting.md` (always on), `ck3-localization.md` (always on), `ck3-decisions.md`, `ck3-ai.md`, `ck3-events.md`, `ck3-traits.md`, `ck3-religions.md`, `pr-context.md`.

## Layout

- `common/`, `events/`, `gui/`, `gfx/`, `localization/<language>/` mirror vanilla.
- `.agents/rules`: generic CK3 notes. `.agents/skills`: task procedures.
- `docs/`: images only. `docs-ai/`: written docs for humans and agents.
- `docs-ai/architecture/`: one doc per subsystem (e.g. `blood-mage-story.md`), always describing the **current state of the mod** and nothing else: no history, changelog or decision log. **Read the matching doc before changing that part of the codebase, and update it in the same change so it stays true.** Add a doc when you introduce a subsystem, and delete or rewrite text that is no longer true. Include an executive summary and benefit tables; omit tunable costs, requirements, and cooldowns. See `docs-ai/architecture/AGENTS.md`.
- Religion uses the 1.20 layout `common/religion/{religion_family_types,religion_types,faith_types,rite_types,holy_site_types,doctrine_group_types,doctrine_types}`. Branches based on older `main` may still have `religions/`, `religion_families/`, `holy_sites/` and a bare `add_trait = lifestyle_blood_mage`. **Check which layout the branch has. Never mix them.**

## Naming

- Prefix every new file and identifier with `bm_`. One file per feature: `bm_<feature>.txt`.
- An unprefixed filename that matches vanilla is a deliberate override. Don't do it by accident.
- Scripted effects/triggers end in `_effect` / `_trigger`. Game rule settings: `has_game_rule = bm_<rule>_<setting>`.

## Format (enforced by `scripts/check_repo.py`)

- `.txt`, `.gui`, `.yml`: UTF-8 **with BOM**, trailing newline, balanced braces.
- Preserve each file's line endings (many are CRLF) and indentation (tabs/4 spaces mixed). Don't reformat unrelated lines.
- Keep comments.
- Use `scripts/read_ck3.py` (CLI or imported `read_ck3_file`, `find_block`, `search_files`) to read files, extract balanced `{ ... }` blocks, or inspect vanilla (`/Users/clarabotet/Petur/ck3-full`) transparently without encoding or BOM issues:
  - CLI read: `python3 scripts/read_ck3.py read <file> [--lines start:end]`
  - CLI extract block: `python3 scripts/read_ck3.py block <file> <block_name>` (e.g. `block <file> eminent_holy_sites`)
  - CLI vanilla search: `python3 scripts/read_ck3.py search <pattern> --vanilla [--subpath common/religion]`
  - Python import: `from scripts.read_ck3 import read_ck3_file, find_block, search_files`
- Inspect game errors at `~/Documents/Paradox Interactive/Crusader Kings III/logs/error.log` (e.g. `tail -n 100 ~/Documents/"Paradox Interactive"/"Crusader Kings III"/logs/error.log`).

## Localization

See `.agents/rules/ck3-localization.md` (english only, sibling keys, loc documents the script).

## Never

- Change `descriptor.mod` (`name`, `remote_file_id`, `version`) or add `replace_path`.
- Delete third-party compat code (Blood of Numenor, AGOT checks) without asking. Never reference another mod's traits, faiths or titles directly; guard with `has_global_variable = AGOT_is_loaded` or doctrine parameters.
- Invent effect, trigger or scope names. Find them in vanilla or `script_docs` output and cite where.

## Workflow

1. Read `docs-ai/branch-context/<branch>.md` if it exists, the matching rule(s), and the matching `docs-ai/architecture/*.md` (start at its `README.md`).
2. Smallest change that works. `grep -rn` to confirm names aren't already defined.
3. Use the matching skill for the task (`add-blood-magic-decision`, `add-faith`, `add-trait-track`, `add-game-rule`).
4. Run `update-docs`, then `validate-change`. State in the final summary what you could not verify.
