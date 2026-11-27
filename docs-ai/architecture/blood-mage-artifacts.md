# Blood Magic Artifacts

Living technical specification for forged Blood Artifacts and Egill Skallagrimsson's tempering duel.

## Overview

- **Template (`bm_blood_artifact_template`):** `can_equip = { always = yes }`, `can_benefit = { is_blood_mage_any_tier_trigger = yes }`, `fallback = { monthly_prestige = 0.1 }`.
- **Forge Decision (`bm_forge_blood_artifact_decision`):** Costs `250` Piety + `100` Gold + `1` Major Lifeforce (`3`-year cooldown `bm_forge_artifact_cooldown`), `+3` `wisdom` XP. 2-step event (`bm_blood_artifact.0001` -> `.0002`) picks 1 of 5 inventory slots (`sword`, `regalia_simple`, `armor_plate`, `helmet_simple`, `miscellaneous`) and 1 of 6 Blood Disciplines (`radiance`, `fury`, `fortune`, `cunning`, `wisdom`, `ancient`) to create a **Masterwork** Blood Artifact (`var:bm_is_forged_blood_artifact = yes`, `var:bm_blood_artifact_discipline = flag:<disc>`).
- **Egill Tempering Duel (`bm_temper_blood_artifact_decision`):** Shown when carrying an untempered forged Blood Artifact; requires `250` Piety, `1` Superior Lifeforce, `5`-year cooldown (`bm_temper_artifact_cooldown`), and physical presence at Reykjavik (`c_vestisland`) or Tsushima (`c_tsushima`) (`bm_is_at_blood_magic_initiation_site_trigger`).
  - `bm_blood_artifact.0010` selects an untempered artifact; `.0011` challenges Egill Skallagrimsson to either **Single Combat (Prowess)** (`configure_start_single_combat_effect` -> `.0012` / `.0013`) or an **Arcane Contest (Learning)** (`duel`).
  - **Victory:** Upgrades artifact rarity to **Illustrious** (`set_artifact_rarity = illustrious`), adds `bm_artifact_tempered_<disc>_modifier`, sets `var:bm_artifact_tempered = yes` (max 1 temper per artifact), and grants `+5` `fury` (Prowess) or `+5` `wisdom` (Learning) XP.
  - **Defeat:** Wounds caster (`increase_wounds_no_death_effect`), `+25` Stress, Superior Lifeforce remains consumed.

## Where the details live

| Piece | File |
| --- | --- |
| Artifact template | `common/artifacts/templates/bm_artifact_templates.txt` |
| Slot, discipline & tempered modifiers | `common/modifiers/bm_artifact_modifiers.txt` |
| Creation & tempering effects | `common/scripted_effects/bm_blood_artifact_effects.txt` |
| Shared Egill build (`bm_create_egill_effect`, `bm_vanish_egill_effect`) | `common/scripted_effects/bm_egill_effects.txt` |
| Forge & temper decisions | `common/decisions/cast_magic/bm_blood_artifact_decisions.txt` |
| Forging & duel events | `events/bm_blood_artifact_events.txt` |
| Localization | `localization/english/bm_blood_artifacts_l_english.yml` |

## Gotchas
- Event scopes do not persist across decisions, so `exists = scope:` guards for spawned NPCs never hit. Egill is created per chain by `bm_create_egill_effect` (shared by geyser + tempering duels) and removed by `bm_vanish_egill_effect`; SCE duel keeps him via flag `bm_temper_sce_pending` until `.0012`/`.0013`.
