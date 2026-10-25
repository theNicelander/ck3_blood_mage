# Architecture docs: writing rules

One doc per subsystem of the mod. `README.md` is the index (doc → source path → purpose). Generic CK3 guidance lives in `.agents/rules/`, not here.

## Rules

- **Current state only.** No history, changelog, "previously"/"now". Rewrite text so it is true today. History belongs in the PR/branch doc.
- **Specs, not prose.** Compact tables of identifiers, `Cost`, `Cooldown`, `Req`, `XP`, `Benefit`. No roleplay or adjectives. Complete mechanical numbers stay (costs, brackets, XP, cooldowns, duel math).
- **Collapse repeats.** Multi-tier tracks: state the repeating step once, list milestones (10/50/100 XP), not identical rows.
- **Link, don't duplicate.** Point to the owning doc or `.agents/rules/`.
- Identifiers exactly as in script; grep to confirm they exist. Backticks for files and identifiers. English only; plain markdown (no BOM).

## Doc structure

1. **Summary**: 1–3 lines on what it is and how it ties to Lifeforce, Devotion, tracks, Blood Mage vs Blood Knight.
2. **Spec**: tables and short bullets.
3. **Where**: concept → file paths.
4. **Gotchas / not verified**: only when real.

## Maintenance

- Read the matching doc before changing a subsystem; update it in the same change when a concept is added, removed or rewired (not for pure tuning of unlisted values).
- New subsystem = new `blood-mage-<subsystem>.md` plus a `README.md` index row.
