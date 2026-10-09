# AGENTS.md — How to write architecture docs

This folder holds one doc per subsystem of the Blood Mages mod. They explain **what each part is for and how the parts fit together**. They are not a copy of the script. `README.md` in this folder indexes them by source path. Generic CK3 guidance lives in `.agents/rules/`, not here: these docs cover only this mod.

They describe the **current state of the mod and nothing else**. No history, no changelog, no decision log, no "previously" or "now". When something changes, rewrite the text so it is true today. Branch and PR history belongs in `docs-ai/branch-context/`.

## The rule: Caveman-Style Technical Reference

Write high-density, concise technical documentation. Zero fluff, zero roleplay prose. Both humans and LLMs need direct facts: what it is, how to get it, exact costs, requirements, cooldowns, XP gains, and benefits.

- **Do write direct specs:** State `Cost`, `Cooldown`, `Req`, `XP Gain`, and `Benefits` explicitly.
- **Do write dense summaries:** Use bullet points and compact markdown tables. Strip storytelling, creative lore metaphors, and conversational filler.
- **Track & step summaries:** For multi-tier tracks (e.g. 10 levels of 10 XP), state the repeating base step bonus once and highlight milestones (e.g. levels 50 and 100) instead of copy-pasting identical rows.

| Verbose / Fluffy (Banned) | Caveman Style (Required) |
| --- | --- |
| "A blood mage is not a class chosen at a menu, it is a path where vitality bends to the caster's desires..." | "Core identity trait `lifestyle_blood_mage`. Unlocks spell decisions, story panel, and 5 XP tracks." |
| "Manifest Lifeforce converts spiritual devotion into vital essence with great personal peril." | "`bm_manifest_lifeforce`: Decision. Cost: 250 piety. Cooldown: none. Gain: Lifeforce. Risk: Wounded/Death." |
| "Draining Lifeforce takes the life fluid from captive mortals to grow in hematurgy." | "`drain_lifeforce`: Interaction. Cost: 25 piety. XP: +1 hematurgy. Gain: `lifeforce_modifier_minor`." |
| "Copy-pasting 10 identical blocks of +0.1 health" | "Levels 10–40, 60–90: +0.1 health, +2 life expectancy. Milestones: lvl 50 (+1 school stat/prowess per piety), lvl 100 (prowess age lock)." |

## Subsystem Document Structure

Every architecture document must begin with a concise **Executive Summary**:

1. **Executive Summary:**
   - **What it is:** 1–2 lines defining the core feature/trait and base stats.
   - **How to get it:** Exact effect, decision, interaction, or trigger.
   - **How to level / advance:** Triggering actions, Lifeforce costs, and XP gains.
   - **Data Table:** Compact table of tracks/modifiers, step benefits, and milestones.
2. **Key Mechanics:** Direct bullet points for decisions, interactions, rosters, or spell gates.
3. **Where the details live:** Concept-to-file path mapping table.
4. **Gotchas:** Hard technical traps, edge cases, and script interactions.
5. **Not verified:** Unverified in-game behavior or AI edge cases.

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
| `blood-mage-blood-runes.md` | Blood Runes and blood university duchy buildings |
| `blood-mage-golems.md` | Blood golem lifecycle, creation decision, shaping duels, and template |
| `blood-mage-blood-empowerment.md` | The Blood Empowerment trait, self-advancement, and warrior retinue |
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
