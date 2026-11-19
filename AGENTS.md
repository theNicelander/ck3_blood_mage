# AGENTS.md — Blood Mages (CK3 1.20+)

Pure script, loc, gfx; no build. Vanilla ref: `/Users/clarabotet/Petur/ck3-full`. CK3 fails silently — never invent syntax; verify in vanilla or `script_docs`.

## Principles

- **Zero vanilla overwrites**: modular only. Unprefixed vanilla filename = override; never do by accident.
- **Earned power**: stats/lifespan cost Lifeforce, piety, sacrifice, risk.
- **Concise UI**: say "Lifeforce" (not "vitality"), "blood" (not crimson/sanguine), `"Back"` for cancel. Flavour only in narrative `_desc`.
- **Notification icon**: all `bm_action_*` notifications use `@bm_ancient_discipline_icon!` (Blood Mage signature icon).
- **Nothing hidden, often unavailable**: keep options visible + greyed (`show_as_unavailable`); hide only if prerequisite unreached or permanently completed/superseded.
- **Native triggers over `custom_tooltip`**: never wrap standard triggers (`piety`, `piety_level`, `gold`, `has_trait`, `has_character_modifier`, etc.) in `custom_tooltip`.
- **Toasts**: wrap player-facing modifier, trait, XP, stat grants in `send_interface_toast`.
- **Single source of truth & caveman AI docs**: one place per rule (link, never duplicate); terse caveman prose in rules/skills/`AGENTS.md`.

## Naming, format & tools

- Prefix new files/IDs `bm_` (`bm_<feature>.txt`, `_effect`/`_trigger`, `has_game_rule = bm_<rule>_<setting>`). Rename IDs on rework unless told otherwise.
- `.txt`/`.gui`/`.yml`: UTF-8 **with BOM**, trailing newline, balanced braces; preserve CRLF/indentation/comments.
- Inspect: `python3 scripts/read_ck3.py {read|block|search}` (handles BOM).
- Modifiers: allowlist-only (`scripts/modifiers_{character,county,domicile}_allowlist.json`); add verified vanilla via `python3 scripts/check_modifiers.py --add <mod> --scope <character|county|domicile>`.
- Validate: `python3 scripts/check_repo.py`. Logs/errors: skill `debug-ck3-logs` (always snapshot `error.log`/`debug.log` first).

## Never

- Edit `descriptor.mod` (`name`, `remote_file_id`, `version`), `.env`, `*.vdf`, or add `replace_path`.
- Delete third-party compat code (AGOT, Blood of Numenor) unasked, or reference other-mod keys unguarded (`has_global_variable = AGOT_is_loaded` or doctrine params).
- Commit/push to `main` (if on `main`, branch `v1.21.<N+1>` first).
- Blanket stage (`git add .`, `-A`, `commit -a`) — parallel agents share tree.
- Merge PR unless user explicitly asks (squash via `gh pr merge --squash`, never locally).
- Read `docs-ai/archive/`, `docs-ai/ideas/`, `docs-ai/base-game-lists/`, `.agents/cost.md` unless asked.

## Workflow & agent guards

- **Commit every turn (MANDATORY)**: parallel agents share this working tree. Before ending ANY turn that edited files, explicitly `git add <only your files>`, commit, and push to `<branch>`. Never leave uncommitted edits waiting for follow-up.
- **Argon planner**: if using Gemini Argon, ask `"You are using Argon, do you want to continue Yes/No"` first; never edit files on Argon (investigate/ask/plan only).
- **Clarify first**: ask on rough ideas; never execute on unverified assumptions. Suggest a skill for newly investigated vanilla systems.
- **Flow**: `git branch --show-current` → read `docs-ai/branch-context/<branch>.md` + matching `docs-ai/architecture/` doc → edit → finish via skill `manage-pr`.
