# AGENTS.md — How to write architecture docs

This folder holds one doc per subsystem of the Blood Mages mod. They explain **what each part is for and how the parts fit together**. They are not a copy of the script.

They describe the **current state of the mod and nothing else**. No history, no changelog, no decision log, no "previously" or "now". When something changes, rewrite the text so it is true today. Branch and PR history belongs in `docs-ai/branch-context/`.

## The rule

Document the concept. Link to the code for the numbers.

- **Do write:** the purpose of a part, the player or AI fantasy behind it, how it relates to other parts, and what it feeds into.
- **Don't write:** costs, cooldowns, durations, thresholds, XP values, piety levels, chances, weights, modifier magnitudes, AI `base` values or check intervals. Those live in the decisions, traits, script values and events, and go stale the moment someone rebalances.

Test: if a balance pass would make the sentence wrong, remove the number and point at the file instead.

| Too specific | Right level |
| --- | --- |
| "Costs 500 piety, 1 year cooldown, needs piety level 2" | "Manifest Lifeforce converts spiritual power into Lifeforce, with a risky outcome." |
| "Gives +0.1 health every 10 XP" | "Each track grants a steady bonus that fits its theme, plus milestones." |
| "Seek Power: base 100, interval 3" | "Seek Power is an event chain that can yield extra Lifeforce. Landless adventurers get their own variant." |

## What belongs in a doc

Keep each doc light. Use these headings, in this order:

1. **Purpose.** What the subsystem is and why the mod has it.
2. **Concepts.** The parts, each in a sentence or two. Name the idea and how it differs from its neighbours. For example, say that landless adventurers use a variant of the same action.
3. **Where the details live.** A table of concept to file. This is the one place to be precise about location.
4. **How the parts connect.** Which effects, events, on-actions, stories or GUI tie it together, and the direction of dependency.
5. **Gotchas.** Cross-cutting traps that stay true after rebalancing, such as "add new decisions to the story list too". Skip numeric oddities. Fix those in the script or put them in the PR notes.
6. **Not verified.** What can't be confirmed from files, such as in-game behaviour, AI and UI.

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
| `blood-mage-religions.md` | The Cult of Quintessence religion family, 7 syncretic faiths, mainline rites, and holy sites |

Keep this table in step with the folder.

## Format

- Plain markdown, no BOM needed (the repo's BOM rule covers `.txt`, `.gui` and `.yml`).
- English only. Use backticks for file names and identifiers, and name identifiers exactly as in script. Don't invent identifiers, so grep to confirm they exist.
