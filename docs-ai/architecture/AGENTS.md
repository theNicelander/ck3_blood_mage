# AGENTS.md — How to write architecture docs

This folder holds one doc per subsystem of the Blood Mages mod. They explain **what each part is for and how the parts fit together**. They are not a copy of the script. `README.md` in this folder indexes them by source path. Generic CK3 guidance lives in `.agents/rules/`, not here: these docs cover only this mod.

They describe the **current state of the mod and nothing else**. No history, no changelog, no decision log, no "previously" or "now". When something changes, rewrite the text so it is true today. Branch and PR history belongs in `docs-ai/branch-context/`.

## The rule

Document the concepts and benefits. Link to the code for tunable costs and thresholds.

- **Do write:** the purpose of a part, the player or AI fantasy behind it, how it relates to other parts, and what it feeds into.
- **Do write trait, track & modifier benefits:** document what benefits a trait, track, or modifier gives, and how much experience an action awards (e.g. "doing this gives X experience in that track").
- **Track & step summaries:** when describing tracks (such as Blood Mage or Crimson Empowerment), provide a simple table towards the beginning showing what the benefits are of each track and step. Since most tracks feature 10 tiers that grant identical bonuses until a milestone is reached, summarize them compactly (e.g. "Levels 10–100 give X; milestones at 50 and 100 add Y") instead of repeating every identical tier.
- **Don't write:** tunable costs (piety, gold, lifeforce amounts), resource requirements, cooldowns, durations, gating thresholds, chances, weights, AI `base` values or check intervals. Those live in the decisions, script values and events, and go stale the moment someone rebalances.

| Too specific | Right level |
| --- | --- |
| "Costs 500 piety, 1 year cooldown, needs piety level 2" | "Manifest Lifeforce converts spiritual power into Lifeforce, with a risky outcome." |
| "Draining Lifeforce costs 250 piety, requires 50 prowess, 5 year cooldown" | "Draining Lifeforce grants 1 hematurgy XP and harvests vitality from the target." |
| "Copy-pasting 10 identical blocks of +0.1 health" | "Levels 10–40 and 60–90 give +0.1 health and +2 life expectancy; level 50 adds a skill milestone." |

## What belongs in a doc

Keep each doc accessible for humans and LLMs. Start with a short **Executive Summary** at the top of trait and progression docs, followed by simplified details:

1. **Executive Summary** (especially for traits, bloodlines, and major subsystems):
   - **How to get it:** Quick route/trigger into the trait or feature.
   - **What it does:** Core benefits and mechanical role.
   - **How to level it up:** Active casting, passive pulses, and XP rewards.
   - **Simplified Benefits Table:** A compact table showing tracks, step benefits, and milestones.
2. **Purpose.** What the subsystem is and why the mod has it.
3. **Concepts.** Simplified narrative and structural explanations. Feel free to shorten or streamline text so key concepts are immediately clear.
4. **Mod conventions** (optional, between Concepts and Where the details live).
5. **Where the details live.** A table of concept to file. This is the one place to be precise about location.
6. **How the parts connect.** Which effects, events, on-actions, stories or GUI tie it together, and the direction of dependency.
7. **Gotchas.** Cross-cutting traps that stay true after rebalancing.
8. **Not verified.** What can't be confirmed from files, such as in-game behaviour, AI and UI.

## Keeping them current

- These are living documents. Read the matching doc before changing a subsystem, and update it in the same change.
- Update when a concept is added, removed, renamed in meaning or rewired. Don't update for tuning.
- Add a new doc when a subsystem is introduced or substantially reworked. Name it `blood-mage-<subsystem>.md`.
- Don't duplicate. If a rule is already in `.agents/rules/`, link to it. Branch and PR history belongs in `docs-ai/branch-context/`, not here.

## Current docs

| Doc | Covers |
| --- | --- |
| `blood-mage-story.md` | The Blood Magic panel (story cycle) and its rosters |
| `blood-mage-decisions.md` | The actions a blood mage can take and the routes into blood magic |
| `blood-mage-traits.md` | The two lifestyle traits and their progression tracks |
| `blood-mage-dynasty.md` | Bloodline house modifiers and the Golem house |
| `blood-mage-lifeforce.md` | The Lifeforce resource, positive/negative modifiers, and harvesting |
| `blood-mage-progression.md` | Dynamic XP gains, requirement gates, cost scaling, and AI weighting |
| `blood-mage-interactions.md` | Character interactions (draining, granting, curing, and self-casting) |
| `blood-mage-blood-runes.md` | Crimson Runes and blood university duchy buildings |
| `blood-mage-golems.md` | Blood golem lifecycle, creation decision, shaping duels, and template |
| `blood-mage-crimson-empowerment.md` | The Crimson Empowerment trait, self-advancement, and warrior retinue |
| `blood-mage-duels-and-education.md` | Duel calculations, trait draining, education enhancement, and mass lifedrain |
| `blood-mage-prevalence-and-lifecycle.md` | Trait acquisition, birth inheritance, yearly pulses, and retention audits |
| `blood-mage-game-rules.md` | Campaign game rules (prevalence, alterations, and religion availability) |
| `blood-mage-events-overview.md` | Mapping of all event files to their triggering mechanisms and sibling docs |
| `blood-mage-shared-scripting.md` | Shared triggers, opinion modifiers, nicknames, death reasons, icons, and compat |
| `blood-mage-trait-inheritance.md` | Direct trait inheritance, birth prevalence auditing, and lineage modifiers |
| `blood-mage-religions.md` | The Blóðtrú religion family, unified faith, mainline rites, and holy sites |

Keep this table and `README.md` in step with the folder.

## Format

- Plain markdown, no BOM needed (the repo's BOM rule covers `.txt`, `.gui` and `.yml`).
- English only. Use backticks for file names and identifiers, and name identifiers exactly as in script. Don't invent identifiers, so grep to confirm they exist.
