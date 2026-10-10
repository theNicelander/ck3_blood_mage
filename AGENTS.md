# AGENTS.md — Blood Mages (CK3 mod)

CK3 script fails silently. Follow patterns already in this repo and in vanilla 1.20 rather than inventing syntax.

## What this is

- CK3 mod for **1.20.***. Pure script, localization, gfx. No build step.
- Adds traits: `lifestyle_blood_mage` (tracks: ancient, enlightenment, bloodline, benediction, hematurgy), `lifestyle_blood_empowerment` (tracks: dynasty, mastery, presence, prosperity, shadows), and `lifestyle_blood_knight` (tracks: slaughter, vanguard, resilience). Track XP sources, costs, and gains catalog: `docs-ai/architecture/blood-mage-track-xp.md`.
- Features: Lifeforce resource, spell decisions/interactions, blood golems, Blood Retinue, Blóðtrú religion family, Blood Runes & blood universities, and game rules.
- `scripts/` holds repo validation and Steam Workshop helpers. Never touch `.env`, credentials or `*.vdf`.

## Guiding principles

- **Rule of cool**: Low-fantasy blood magic integrated seamlessly into CK3 systems.
- **Zero vanilla overwrites**: Pure modular additions; strictly compatible with total conversions and other mods.
- **Earned power over godmode**: Lifespan extension and physical/mental trait improvements (intellect, beauty, physique) require earned Lifeforce, piety, and ritual sacrifice, with tangible risks.

## Context layers

| Layer | Answers | Scope |
| --- | --- | --- |
| Rules `.agents/rules/*.md` | How do I write this kind of CK3 thing without breaking it? | Generic CK3 plus hard repo constraints. No `bm_` identifiers |
| Skills `.agents/skills/<name>/SKILL.md` | What are the steps for task X here? | Repeatable multi-file procedures |
| Architecture `docs-ai/architecture/*.md` | How does this mod implement it? | Mod only. Start at its `README.md` |

Active rules: `ck3-scripting.md` (always on), `ck3-localization.md` (always on), `ck3-decisions.md`, `ck3-ai.md`, `ck3-events.md`, `ck3-traits.md`, `ck3-religions.md`, `single-combat.md`, `pr-context.md`.

## Layout

- `common/`, `events/`, `gui/`, `gfx/`, `localization/<language>/` mirror vanilla.
- `.agents/rules`: generic CK3 notes. `.agents/skills`: task procedures.
- `docs/`: images only. `docs-ai/`: written documentation for humans and agents.
- `docs-ai/architecture/`: one doc per subsystem (e.g. `blood-mage-story.md`), always describing the **current state of the mod** and nothing else: no history, changelog or decision log. **Read the matching doc before changing that part of the codebase, and update it in the same change so it stays true.** Add a doc when you introduce a subsystem, and delete or rewrite text that is no longer true. High-density technical specs (costs, requirements, XP, benefits, tables; zero roleplay fluff). See `docs-ai/architecture/AGENTS.md`.
- `docs-ai/ideas/`: brainstorms, proposals, and roadmaps. Speculative; do not treat as current game state.
- `docs-ai/branch-context/`: branch and PR working state, trade-offs, and decision records.
- `CHANGELOG.md`: living changelog representing current branch net state since 1.20 (one line per PR merge, caveman style).
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

1. Read `docs-ai/branch-context/<branch>.md` if it exists, matching rule(s), and matching `docs-ai/architecture/*.md` (start at its `README.md`).
2. Smallest change that works. Check existing identifiers with `grep -rn`.
3. Use the matching skill for the task (`add-blood-magic-decision`, `add-faith`, `add-trait-track`, `add-game-rule`).
4. Update matching architecture doc in `docs-ai/architecture/` in the same change so it stays true to current state.
5. Update `CHANGELOG.md` and `AGENTS.md` changelog: living document, one line per PR merge, caveman style, net branch status only (fold superseded changes, drop reverts).
6. Run `python3 scripts/check_repo.py`. State in the final summary what you could not verify.

## Living changelog (branch net state since 1.20)

Always reflects current branch state. Simple line per PR merge. Superseded changes folded, reverts dropped. Caveman style.

- PR #95: CK3 1.20 baseline compat, layout modernization, AI agent rules.
- PR #97: English-only localization source. Drop non-English stubs for auto-generation.
- PR #98: Reorganize decision and AI agent rules.
- PR #99: Trait definition syntax fixes, descriptor update.
- PR #100: Pre-commit repository format checks, religion script fixes.
- PR #101: Streamline agent rules documentation.
- PR #102: Reykjavik duel decision to challenge occult hermit.
- PR #103: Consolidate Blóðtrú faith with Ancestor Worship tenet.
- PR #105: Rename religion family and core faith to Blóðtrú.
- PR #106: Split East Asian branch into Xuédào (Chinese) and Ketsudō (Japanese) faiths.
- PR #107: Standardize holy site modifiers. Add debug interactions.
- PR #108: Repeatable minor lifedrain. Unrestricted manifest lifeforce.
- PR #109: Lifeforce harvest from single combat duels.
- PR #110: Agent token cost pre-commit check. Add caveman skill.
- PR #113: Debug logging for blood magic operations.
- PR #114: Blood Shrine building chain for holdings and domiciles.
- PR #118: Keep self-cast blood magic in decisions tab.
- PR #119: DRY triggers, illness/drain bugfixes, fix duchy building typo.
- PR #120: Rename Crimson and Sanguine entities to Blood across mod.
- PR #121: Consolidate self-magic decisions into Minor and Major hub events.
- PR #122: Add Superior Lifeforce tier; require for Blood Golem creation.
- PR #123: Major channel ritual to manifest congenital traits.
- PR #124: Rebalance blood empowerment tracks. Standardize trait baselines.
- PR #125: Rebalance blood mage tracks, cap opinion bonuses, normalize economic scaling.
- PR #126: Superior blood magic rites, Egill duel integration, runtime error fixes.
- PR #127: Allow Blood Knights to cast minor blood magic and seek power.
- PR #128: Add historical Egill Skallagrímsson character bookmark.
- PR #129: Redesign Blood Knight as standalone lifestyle trait (Slaughter, Vanguard, Resilience) with elevation bridge; rework healing to unified event flow; redistribute track XP.
