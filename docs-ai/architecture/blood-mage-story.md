# Blood Mage Story (`bm_blood_mage_story`)

> Living document. Follow `AGENTS.md` in this folder: concepts only, no numbers. Update it when the story, its rosters or its creation points change.

## Purpose

A per-character story cycle that backs the "Blood Magic" panel. It gives a blood mage one place to see their servants and reach their key actions.

## Concepts

- **The panel.** It shows the mage's blood golems, their crimson retinue, and living dynasty members who are blood mages, along with compact situation-exclusive actions (hidden from the main decisions view with `is_invisible = yes`).
- **Rosters.** The golem list is made of the courtiers in the golem house. The retinue is made of courtiers who have been empowered as crimson warriors or champions. The dynasty roster contains all living members of the mage's dynasty who possess the blood mage trait.
- **Lifeforce counters.** The refresh also recounts Lifeforce modifier stacks, because script can't read a modifier's stack count.
- **Lifetime.** The story is created once per blood mage, rebuilt on setup and ended when the owner dies.

## Mod conventions

- **Adding a story field.** Update in order: story effects, scripted GUI, localization, then `window_situation_list.gui` (Blood Mage sections only).
- **Situation decisions.** Only situation-exclusive hidden decisions are kept in the story's decision list to keep the panel compact. Non-hidden decisions belong in the main decisions view.

## Where the details live

| Piece | File |
| --- | --- |
| Story definition | `common/story_cycles/bm_blood_mage_story.txt` |
| Create-if-missing effect (`bm_ensure_blood_mage_story_effect`) | `common/scripted_effects/bm_blood_mage_lifecycle_effects.txt` |
| Roster and stack refresh | `common/scripted_effects/bm_blood_mage_story_list_effects.txt` |
| Script values | `bm_blood_mage_story_values.txt` |
| Localization | `localization/english/bm_blood_mage_story_l_english.yml` |
| Creation on-actions | `bm_blood_mage_story_on_actions.txt`, `bm_yearly_pulse.txt`, `bm_blood_mage_prevalence_on_actions.txt` |

## How the parts connect

- On-actions (game start, birth, yearly pulse and trait acquisition) make sure each blood mage owns the story.
- The refresh effect rebuilds the rosters from the owner's court and writes them to the story.
- The panel's decision list points at decisions described in `blood-mage-decisions.md`.

## Gotchas

- The rosters are snapshots. Call `bm_refresh_blood_magic_rosters_effect` after anything that adds or removes golems or retinue members.
- The refresh temporarily removes Lifeforce modifiers, so keep it free of side effects that react to them.
- A new blood magic decision must be added to the story's decision list to show in the panel.

## Not verified

In-game rendering of the panel hasn't been confirmed from files alone. The on-action file names come from earlier docs and grep hits. I didn't open them.
