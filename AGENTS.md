# AGENTS.md — Blood Mages (CK3 mod)

CK3 script fails silently. Follow patterns already in this repo and in vanilla 1.20 rather than inventing syntax.

## What this is

- CK3 mod for **1.20.\***. Pure script, localization, gfx. No build step.
- Adds traits: `lifestyle_blood_mage` (tracks: ancient, enlightenment, bloodline, benediction, hematurgy), `lifestyle_blood_empowerment` (tracks: dynasty, mastery, presence, prosperity, shadows), and `lifestyle_blood_knight` (tracks: slaughter, vanguard, resilience). Track XP sources, costs, and gains catalog: `docs-ai/architecture/blood-mage-track-xp.md`.
- Features: Lifeforce resource, spell decisions/interactions, blood golems, Blood Retinue, Blóðtrú religion family, Blood Runes & blood universities, and game rules.
- `scripts/` holds repo validation and Steam Workshop helpers. Never touch `.env`, credentials or `*.vdf`.

## Guiding principles

- **Rule of cool**: Low-fantasy blood magic integrated seamlessly into CK3 systems.
- **Zero vanilla overwrites**: Pure modular additions; strictly compatible with total conversions and other mods.
- **Earned power over godmode**: Lifespan extension and physical/mental trait improvements (intellect, beauty, physique) require earned Lifeforce, piety, and ritual sacrifice, with tangible risks.
- **Concise and direct over fluffy flavour**: UI text, tooltips, alerts, action descriptions, and mechanics must be concise and to the point. Always use concrete terms like "Lifeforce" rather than vague synonyms like "vitality" or "vital arts". Keep flavour text strictly confined to narrative descriptions in decisions and events.
- **Nothing hidden, but often unavailable (Always show grayed out)**: Spells, rites, and character options should remain visible and grayed out (`show_as_unavailable = { ... }`) whenever possible so players can always see what capabilities exist and what requirements (Lifeforce, Piety, Devotion, Cooldown) are needed to reach them. Only hide an option when its prerequisite stage has not been reached or when it has been permanently completed or superseded.
- **Clarify before building**: When making plans, always ask multiple follow-up questions. User ideas are often rough, exploratory, or ungrounded; never run on unverified assumptions—clarify ambiguities and explicitly state assumptions before implementing.
- **Commit planned work**: Plans must always conclude with committing the changes at the end. Since plans are well thought out, commit the finished implementation; any subsequent adjustments, user feedback, or follow-up iterations belong in a separate commit. Commits must strictly include only relevant files modified in your conversation.

## Context layers

| Layer                                    | Answers                                                    | Scope                                                        |
| ---------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------ |
| Rules `.agents/rules/*.md`               | How do I write this kind of CK3 thing without breaking it? | Generic CK3 plus hard repo constraints. No `bm_` identifiers |
| Skills `.agents/skills/<name>/SKILL.md`  | What are the steps for task X here?                        | Repeatable multi-file procedures                             |
| Architecture `docs-ai/architecture/*.md` | How does this mod implement it?                            | Mod only. Start at its `README.md`                           |

Active rules: `ck3-scripting.md` (always on), `ck3-localization.md` (always on), `pr-context.md` (always on), `ck3-decisions.md`, `ck3-ai.md`, `ck3-events.md`, `ck3-traits.md`, `ck3-religions.md`, `single-combat.md`.

## Layout

- `common/`, `events/`, `gui/`, `gfx/`, `localization/<language>/` mirror vanilla.
- `.agents/rules`: generic CK3 notes. `.agents/skills`: task procedures.
- `docs/`: images only. `docs-ai/`: written documentation for humans and agents.
- `docs-ai/architecture/`: one doc per subsystem (e.g. `blood-mage-story.md`), always describing the **current state of the mod** and nothing else: no history, changelog or decision log. **Read the matching doc before changing that part of the codebase, and update it in the same change so it stays true.** Add a doc when you introduce a subsystem, and delete or rewrite text that is no longer true. High-density technical specs (costs, requirements, XP, benefits, tables; zero roleplay fluff). See `docs-ai/architecture/AGENTS.md`.
- `docs-ai/ideas/`: brainstorms, proposals, and roadmaps. Speculative; do not treat as current game state.
- `docs-ai/branch-context/`: branch and PR working state, trade-offs, and decision records. One mandatory `<branch>.md` per branch.
- `CHANGELOG.md`: living changelog with one line per branch version matching the branch name (e.g. `* v1.20.40: <short description>`), caveman style, reverse chronological: latest changes at top.
- `RELEASE_NOTES.md`: public-facing living release notes for players and Steam Workshop, summarizing net features and bugfixes since v1.15. Keep updated using skill `update-release-notes`.
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

See `.agents/rules/ck3-localization.md` (english only, sibling keys, loc documents the script, concise & direct wording, concrete "Lifeforce" term over fluffy "vitality", never include ($NUM$) in group labels).

## DDS Icons & Assets

- Basegame `.dds` source (copy vanilla icons from here): `/Users/clarabotet/Library/Application Support/Steam/steamapps/common/Crusader Kings III/game/gfx` (e.g. `interface/icons/traits/`, `interface/icons/modifiers/`). `/Users/clarabotet/Petur/ck3-full` has no DDS files. Put candidate shortlists for user review in the gitignored `local-assets/<topic>/`.
- Vanilla DDS styles (by filename prefix): `modifiers/*` = flat one-colour shield glyph (green good, red bad), plain. `traits/*` = detailed illustrated art on a round or square background frame. `icon_*.dds` (e.g. `interface/icons/icon_gold.dds`) = clean, simple, standalone illustrations without a frame (like the bag of gold). Prefer `icon_*` for new rune/spell icons unless a framed look is wanted.
- DDS files within a category are copy-paste identical:
  - **Traits** (`gfx/interface/icons/traits/`): Distinctive icons: `bm_blood_mage.dds` (Blood Mage), `bm_blood_knight.dds` (Blood Knight), `bm_interactions.dds` (Blood Empowerment).
  - **Interactions** (`gfx/interface/icons/character_interactions/`): All use identical copies of `bm_interactions.dds` (120×120 fiery blood drop).
  - **Faiths** (`gfx/interface/icons/faith/`): Shared identical DDS icons across the religion family (copied from `bm_blodtru.dds`).
  - **Trait Level Tracks** (`gfx/interface/icons/trait_level_tracks/`): Distinctive icons per track (`ancient` fiery blood drop from `bm_interactions.dds`, `benediction` physician, `enlightenment` saint/ancestor, `bloodline` augustus, `hematurgy` murderer, `vanguard` faith warrior, `slaughter` raider/reaver).
- When adding a new interaction, copy `gfx/interface/icons/traits/bm_interactions.dds` to `<interaction_key>.dds`.
- When removing or renaming interactions, always remove or rename the corresponding `.dds` file to prevent missing textures or orphan assets.

## Never

- Change `descriptor.mod` (`name`, `remote_file_id`, `version`) or add `replace_path`.
- Delete third-party compat code (Blood of Numenor, AGOT checks) without asking. Never reference another mod's traits, faiths or titles directly; guard with `has_global_variable = AGOT_is_loaded` or doctrine parameters.
- Invent effect, trigger or scope names. Find them in vanilla or `script_docs` output and cite where.
- Switch branches or create new branches unless explicitly instructed by the user. Stay in the current branch. Never create separate branches to isolate work.
- Blanket stage (`git add .`, `git add -A`, `git commit -a`) when uncommitted changes exist from other agents or tasks. Multiple AIs work in parallel on this repo: only stage and commit files modified in your current conversation. "Commit ignoring other changes" means leave other modified files untouched and uncommitted, never create a separate branch.
- Execute plans on unverified assumptions without asking clarifying follow-up questions first.
- Create plans without a final commit step, or leave planned changes uncommitted upon completion.

## Workflow

Multiple AIs work in parallel on this repo, so keep in mind that there maybe other changes in the branch. If that's the case, ingore them unless relevant to you. Don't commit files you didn't touch, unless asked to.

1. `git branch --show-current`; read `docs-ai/branch-context/<branch>.md` (**create if missing**, see `pr-context.md`), matching rule(s), and matching `docs-ai/architecture/*.md` (start at its `README.md`).
2. Plan & clarify: when making plans, always ask multiple follow-up questions. Probe ungrounded ideas, confirm assumptions, and clarify ambiguities before coding. Plans must always conclude with committing at the end. Smallest change that works. Check existing identifiers with `grep -rn`.
3. Use the matching skill for the task (`add-blood-magic-decision`, `add-decision-option-widget`, `add-faith`, `add-trait-track`, `add-game-rule`, `update-release-notes`).
4. Update matching architecture doc in `docs-ai/architecture/` in the same change so it stays true to current state.
5. Update `CHANGELOG.md`: living document, prepend single-line short high-level description matching current branch name (e.g. `* v1.20.40: <short description>`), caveman style, net branch status only (fold superseded changes, drop reverts). Reverse chronological: latest changes at top.
6. For player-facing additions or bugfixes, update `RELEASE_NOTES.md` per skill `update-release-notes`.
7. **Always** update `docs-ai/branch-context/<branch>.md` to net branch state, however small the task.
8. Run `python3 scripts/check_repo.py` (enforces 1 and 7). State in the final summary what you could not verify.
9. **Commit**: Stage and commit ONLY files modified in your active conversation (`git add <file1> <file2> && git commit -m "..."`). Because plans are well thought out, commit the finished plan implementation at the end; subsequent feedback or modifications must be committed in separate commits. Never blanket stage (`git add .`), as multiple agents operate concurrently.
