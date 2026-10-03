# Blood Golems

> Living document. Follow `AGENTS.md` in this folder: concepts only, no numbers. Update it when golem creation, templates, duels, or death mechanics change.

## Purpose

Blood Golems are artificial beings forged from raw vitality, dark magic, and physical sacrifice. A blood mage can construct a golem to serve as a tireless, absolutely loyal knight, champion, or bodyguard. The golem's martial prowess and attributes are tailored during its creation ritual through a series of mystical shaping duels.

## Concepts

- **Creation Decision.** Initiated via `blood_golem_creation_decision` under the Blood Mage decision group, requiring sufficient experience in blood magic.
- **The Golem House.** All created blood golems belong to the dedicated Golem house, establishing their artificial nature and tying into the rosters tracked in `blood-mage-dynasty.md` and `blood-mage-story.md`.
- **Character Template.** Golems are spawned using `blood_golem_template` in `bm_character_templates.txt`, which configures baseline physical attributes, culture, and faith.
- **Shaping Ritual and Duels.** Creation event `blood_golem.001` spawns the construct and launches `blood_golem.002`. Through this event, the creator spends piety to mold the golem with desirable physical and martial traits (e.g. Athletic, Blademaster, Berserker, Physique, Martial Education) using the scripted effect `golem_duel_effect`.
- **Failed Creation.** If the creator fails during the binding process or is physically overwhelmed, the creation ritual aborts with potential injury or death (`death_blood_golem_failed`).

## Where the details live

| Piece | File |
| --- | --- |
| Creation decision | `common/decisions/bm_create_blood_golem.txt` (`blood_golem_creation_decision`) |
| Creation & shaping events | `events/bm_blood_golem_events.txt` (`blood_golem.001`, `blood_golem.002`) |
| Shaping duel effect | `common/scripted_effects/bm_golem_duel_effect.txt` (`golem_duel_effect`) |
| Trait piety cost scaling | `common/script_values/bm_golem_piety_values.txt` |
| Golem character template | `common/scripted_character_templates/bm_character_templates.txt` (`blood_golem_template`) |
| Golem house definition | `common/dynasty_houses/bm_dynasty_houses.txt` |
| Story roster integration | `common/scripted_effects/bm_blood_mage_story_list_effects.txt` |

## How the parts connect

- When `blood_golem_creation_decision` is taken, it consumes Lifeforce and triggers `blood_golem.001`.
- The immediate block uses `create_character` with `blood_golem_template`, assigns the construct to the creator's court, and transitions to `blood_golem.002`.
- `blood_golem.002` offers repeated choices to bestow martial traits onto the golem. Each option invokes `golem_duel_effect`, checking creator skills and deducting piety scaled by `bm_golem_piety_values.txt`.
- After creation completes, `bm_refresh_blood_magic_rosters_effect` adds the golem to the creator's story roster, allowing easy management from the Blood Magic panel.

## Gotchas

- The golem is created as an adult courtier in the creator's realm.
- Golems cannot reproduce or inherit titles under standard configurations due to their artificial template flags and house mechanics.
- If the creator dies, surviving golems remain in the court as loyal retainers unless dismissed or killed.

## Not verified

AI rulers successfully navigating multiple sequential trait options in `blood_golem.002` without depleting all piety reserves.
