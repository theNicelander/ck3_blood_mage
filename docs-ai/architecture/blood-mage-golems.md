# Blood Golems

## Executive Summary

- **What:** Artificial construct courtiers forged from Lifeforce. Absolute loyalty, specialized knights and champions.
- **Creation Decision:** Standalone decision `blood_golem_creation_decision` (`bm_create_blood_golem.txt`) or via `bm_cast_blood_magic_superior_decision` (Forge Blood Golem option). Cost: 500 piety + Superior Lifeforce. Req: 50 track XP (`required_xp_blood_golem`). Cooldown: 3 years. Awards +5 `bloodline` XP.
- **Template & House:** Spawned via `blood_golem_template` into dedicated house `bm_house_golem` (dynasty `dynn_bm_golem`). Cannot inherit or marry.
- **Shaping Ritual:** Event `blood_golem.002` allows molding traits (Berserker, Blademaster, Athletic, Physique, Education) via skill duels (`golem_duel_effect`). Costs piety. Risk of injury or fatal backlash (`death_blood_golem_failed`).

### Golem Lifecycle Matrix

| Phase | Script Entity | Function |
| --- | --- | --- |
| **Creation** | `blood_golem_creation_decision` / `bm_cast_blood_magic_superior.001` | Decision/Event: consumes 500p + Superior Lifeforce, awards +5 bloodline XP. Fires `blood_golem.001`. |
| **Spawn** | `blood_golem_template` | Spawns adult construct courtier in `bm_house_golem`. |
| **Shaping** | `blood_golem.002` | Event loop: spends piety to add martial traits via Learning duel checks (`golem_duel_effect`). |
| **Roster** | `bm_refresh_blood_magic_rosters_effect` | Adds golem to Blood Magic story panel roster. |
| **Failure** | `death_blood_golem_failed` | Death/injury reason if shaping ritual backfires. |

## Where the details live

| Piece | File |
| --- | --- |
| Creation decision | `common/decisions/cast_magic/bm_create_blood_golem.txt` (`blood_golem_creation_decision`) |
| Creation & shaping events | `events/bm_blood_golem_events.txt` (`blood_golem.001`, `blood_golem.002`) |
| Shaping duel effect | `common/scripted_effects/bm_golem_duel_effect.txt` (`golem_duel_effect`) |
| Trait piety values | `common/script_values/bm_golem_piety_values.txt` |
| Golem template | `common/scripted_character_templates/bm_character_templates.txt` (`blood_golem_template`) |
| Golem house | `common/dynasty_houses/bm_dynasty_houses.txt` (`bm_house_golem`) |
| Roster integration | `common/scripted_effects/bm_blood_mage_story_list_effects.txt` |

## Key Mechanics & Gotchas

- **House Membership:** Roster tracks golems strictly by membership in `bm_house_golem`.
- **Sterility / Succession:** Golem template flags prevent reproduction and title inheritance.
- **Story Panel Sync:** Always call `bm_refresh_blood_magic_rosters_effect` after creating or modifying golems.
