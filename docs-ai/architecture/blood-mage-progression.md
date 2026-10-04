# Blood Mage Progression

> Living document. Follow `AGENTS.md` in this folder: concepts only, no numbers. Update it when XP gain, gating, cost scaling, or AI weighting changes.

## Purpose

Progression governs how a blood mage expands their mastery across different schools of blood magic. Rather than automatic level-ups, experience is acquired dynamically by actively casting spells and engaging in blood rituals. Progression also provides gating values for advanced rituals, dynamic cost scaling, and AI weighting modifiers.

## Concepts

- **Dynamic Track Experience.** Gaining experience in `lifestyle_blood_mage` is triggered via `add_xp_bm_dynamic`, awarding XP to the specific track aligned with the action taken:
  - *Hematurgy:* Gained by harvesting and manipulating raw vital fluid.
  - *Benediction:* Gained by healing, infusing prowess, and blessing others.
  - *Bloodline:* Gained by channeling vitality into the dynastic house.
  - *Enlightenment:* Gained by expanding mental faculties and attuning vitality.
  - *Ancient:* Gained slowly over time through age, deep study, and ancient attunement.
- **Ritual XP Requirements.** High-level rituals (such as crafting Blood Golems, manifesting Lifeforce, or acquiring additional education traits) gate their availability behind cumulative or track-specific XP thresholds.
- **Cost Scaling.** `bm_cost_modifiers.txt` adjusts the gold, piety, or prestige costs of blood magic actions based on character traits, skills, and supernatural attunement.
- **AI Value Modifiers.** `bm_ai_value_modifiers.txt` adjusts how appealing blood magic actions are to AI rulers based on personality archetypes, ambition, and supernatural inclination.

## Mod conventions

- **XP helper.** XP is added through `add_trait_xp` with the track name (see `bm_trait_track_xp_gain_effects.txt`), never by setting values by hand.
- **Shared script values** live in `common/script_values/`: piety costs per action (`bm_drain_piety_cost.txt`, `bm_education_enhancement_piety_cost.txt`, `bm_golem_piety_values.txt`, `bm_blood_rune_cost.txt`), requirement gates (`bm_xp_requirement_values.txt`), duel maths (`bm_drain_duel_values.txt`) and panel values (`bm_blood_mage_story_values.txt`). Reuse them instead of repeating numbers.
- **AI self-preservation** reuses the scripted modifiers in `common/scripted_modifiers/bm_ai_value_modifiers.txt` (health, piety or lifeforce, opinion of the target) instead of inline checks.

## Where the details live

| Piece | File |
| --- | --- |
| Dynamic XP scripted effects | `common/scripted_effects/bm_trait_track_xp_gain_effects.txt` |
| Ritual requirement script values | `common/script_values/bm_xp_requirement_values.txt` |
| Cost scaling scripted modifiers | `common/scripted_modifiers/bm_cost_modifiers.txt` |
| AI decision/interaction evaluation | `common/scripted_modifiers/bm_ai_value_modifiers.txt` |
| Trait track definitions | `common/traits/bm_blood_mage_trait.txt` |

## How the parts connect

- Casting interactions and decisions call scripted effects in `bm_blood_magic_used_effects.txt` and `bm_trait_track_xp_gain_effects.txt`.
- Progression thresholds defined in `bm_xp_requirement_values.txt` serve as triggers in decisions (`bm_create_blood_golem.txt`, `bm_manifest_lifeforce.txt`) and interactions (`bm_cast_blood_magic_self_major.txt`).
- AI decision-making layers evaluate `bm_ai_value_modifiers.txt` alongside prevalence game rules to decide whether to pursue blood magic opportunities.
- For the full breakdown of track perks and milestones, see `blood-mage-traits.md`.

## Gotchas

- Adding a new blood magic action requires assigning it to a relevant track via `add_xp_bm_dynamic` to keep progression rewarding.
- Golem creation and education rituals check cumulative or specific track XP; ensure script value references match the intended track.
- Trait tracks cannot exceed maximum XP; additional XP granted beyond the cap is discarded by CK3's engine.

## Not verified

AI willingness to consistently prioritize high-tier blood magic rituals over standard lifestyle focuses under complex personality combinations.
