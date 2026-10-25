# AGENTS.md — Blood Mages (CK3 mod)

CK3 script fails silently. Follow patterns in this repo and vanilla 1.20 (`/Users/clarabotet/Petur/ck3-full`); never invent syntax.

## What this is

- CK3 mod for **1.20.\***. Pure script, localization, gfx. No build step.
- Traits: `lifestyle_blood_mage` (tracks: ancient, enlightenment, bloodline, benediction, hematurgy), `lifestyle_blood_power` (dynasty, fury, mastery, presence, prosperity, shadows), `lifestyle_blood_knight` (slaughter, vanguard, resilience).
- Features: Lifeforce resource, spell decisions/interactions, blood golems, Blood Retinue, Blóðtrú religions, Blood Runes & Temples, game rules.
- `scripts/` holds validation and Steam Workshop helpers. Never touch `.env`, credentials or `*.vdf`.

## Principles

- **Zero vanilla overwrites**: modular additions, compatible with total conversions. An unprefixed filename matching vanilla is an override; never do it by accident.
- **Earned power**: lifespan and stat gains require Lifeforce, piety, ritual sacrifice, and tangible risk.
- **Concise UI text**: say "Lifeforce", not "vitality". Flavour only in decision/event narrative descriptions.
- **Nothing hidden, often unavailable**: keep spells, rites, options visible and greyed out (`show_as_unavailable`) with their requirements. Hide only when the prerequisite stage is not reached or the option is completed/superseded.
- **Clarify before building**: ask follow-up questions on rough ideas; state assumptions. Plans end with commit and push.
- **Planner model**: if the active model is Gemini Argon, never edit files; only investigate, ask, and plan.

## Layout & docs

- `common/`, `events/`, `gui/`, `gfx/`, `localization/<language>/` mirror vanilla. Religion uses the 1.20 layout `common/religion/{religion_family_types,religion_types,faith_types,rite_types,holy_site_types,doctrine_group_types,doctrine_types}`; older branches may have `religions/`, `religion_families/`, `holy_sites/`. Check which one the branch has; never mix.
- `.agents/rules/`: CK3 how-to (no `bm_` ids). `.agents/skills/`: task procedures.
- `docs-ai/architecture/`: current-state spec per subsystem; start at its `README.md`, read the matching doc before changing that code, update it in the same change (rules: its `AGENTS.md`).
- `docs-ai/branch-context/<branch>.md`: mandatory PR-style branch doc (skill `manage-pr`).
- `RELEASE_NOTES.md`: player notes + version history (skill `update-release-notes`).
- **Do not read unless asked**: `docs-ai/archive/` (old branch docs), `docs-ai/ideas/`, `docs-ai/base-game-lists/`, `.agents/cost.md`.

| Rules (`.agents/rules/`) | When |
| --- | --- |
| `ck3-scripting.md`, `ck3-localization.md` | always |
| `ck3-decisions.md` (incl. AI), `ck3-events.md`, `ck3-traits.md`, `ck3-religions.md`, `single-combat.md`, `ck3-error-catalog.md` | on demand |

| Skills (`.agents/skills/`) | Task |
| --- | --- |
| `manage-pr` | finish change, branch doc, commit, push, PR |
| `add-blood-magic-decision`, `add-decision-option-widget`, `add-faith`, `add-trait-track`, `add-game-rule`, `add-icon-asset` | add that thing |
| `document-subsystem`, `update-release-notes`, `caveman` | docs / notes / terse voice |

## Naming & format (enforced by `scripts/check_repo.py`)

- Prefix every new file and identifier `bm_`; one file per feature `bm_<feature>.txt`. Effects/triggers end `_effect`/`_trigger`. Rules: `has_game_rule = bm_<rule>_<setting>`.
- `.txt`, `.gui`, `.yml`: UTF-8 **with BOM**, trailing newline, balanced braces. Keep each file's line endings (many CRLF) and indentation; don't reformat unrelated lines; keep comments.
- Read files with `python3 scripts/read_ck3.py read <file> [--lines a:b]`, `block <file> <name>`, `search <pattern> --vanilla [--subpath common/religion]` (handles BOM/encoding).
- Game errors: `tail -n 100 ~/Documents/"Paradox Interactive"/"Crusader Kings III"/logs/error.log`.
- Localization: English only; see `ck3-localization.md`.
- Icons/DDS: skill `add-icon-asset`.

## Never

- Change `descriptor.mod` (`name`, `remote_file_id`, `version`) or add `replace_path`.
- Delete third-party compat code (Blood of Numenor, AGOT) without asking; never reference another mod's traits/faiths/titles directly (guard with `has_global_variable = AGOT_is_loaded` or doctrine parameters).
- Invent effect, trigger or scope names; cite vanilla or `script_docs`.
- Switch or create branches unless told. Stay on the current branch.
- Blanket stage (`git add .`, `-A`, `commit -a`): other agents work in parallel; stage, commit and push only files you changed.
- Execute plans on unverified assumptions.

## Workflow

1. `git branch --show-current`; read `docs-ai/branch-context/<branch>.md` (create if missing), matching rule(s) and architecture doc.
2. Plan smallest change; grep existing identifiers; use the matching skill.
3. Update the architecture doc, branch doc, and release notes as needed, run checks, commit, push: skill `manage-pr`.
