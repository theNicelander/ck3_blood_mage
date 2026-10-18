# Blood Mage Game Rules

## Executive Summary

- **What:** Campaign startup rules configuring AI prevalence, physical appearance, faith requirements, and religion integration.
- **Rule Check Syntax:** `has_game_rule = <setting_id>`.

### Game Rules Master Table

| Rule ID | Settings (`has_game_rule = ...`) | Default Setting | Mechanical Effects |
| --- | --- | --- | --- |
| `bm_blood_mage_prevalence` | `bm_prevalence_player_only`<br>`bm_prevalence_one_in_10000`<br>`bm_prevalence_one_in_1000`<br>`bm_prevalence_default`<br>`bm_prevalence_one_in_100`<br>`bm_prevalence_one_in_10`<br>`bm_prevalence_everyone` | `bm_prevalence_default` | Scales AI adoption weights, birth chances, and yearly retention audits. `player_only` blocks all AI mages. `everyone` gives trait to all newborns. |
| `bm_blood_knight_prevalence` | `bm_blood_knight_prevalence_player_only`<br>`bm_blood_knight_prevalence_one_in_10000`<br>`bm_blood_knight_prevalence_one_in_1000`<br>`bm_blood_knight_prevalence_default`<br>`bm_blood_knight_prevalence_one_in_100`<br>`bm_blood_knight_prevalence_one_in_10`<br>`bm_blood_knight_prevalence_everyone` | `bm_blood_knight_prevalence_default` | Scales AI creation weights, birth chances, and yearly retention audits. `player_only` blocks all AI knights. `everyone` gives trait to all newborns (subservient to Blood Mage). |
| `bm_physical_alteration` | `bm_physical_alteration_off`<br>`bm_physical_alteration_gradual`<br>`bm_physical_alteration_on` | `bm_physical_alteration_on` | Controls portrait appearance changes (eyes and hair combined): off, gradual based on trait XP, or on (instant maximum supernatural values: white eyes and white hair for both Blood Mages and Blood Knights). |
| `blodtru_religion` | `blodtru_religion_enabled`<br>`blodtru_religion_player_only`<br>`blodtru_religion_disabled` | `blodtru_religion_enabled` | Controls Blóðtrú religion family: fully active, restricted to players only, or completely disabled. |
| `bm_starting_counties_faith` | `bm_starting_counties_faith_vanilla`<br>`bm_starting_counties_faith_iceland`<br>`bm_starting_counties_faith_tsushima`<br>`bm_starting_counties_faith_both` | `bm_starting_counties_faith_vanilla` | Configures whether Iceland (`d_iceland`) and/or Tsushima (`c_tsushima`) start converted to regional blood faiths (`blodtru_faith`, `ketsudo_faith`) and holder faith on game start. |
| `bm_starting_holders_blood_mage` | `bm_starting_holders_blood_mage_vanilla`<br>`bm_starting_holders_blood_mage_iceland`<br>`bm_starting_holders_blood_mage_tsushima`<br>`bm_starting_holders_blood_mage_both` | `bm_starting_holders_blood_mage_vanilla` | Configures whether landed county holders in Iceland and/or Tsushima start with the `lifestyle_blood_mage` trait on game start. |
| `bm_initiation_faith_requirement` | `bm_initiation_dedicated_cult`<br>`bm_initiation_cult_or_witchcraft_accepted` | `bm_initiation_dedicated_cult` | Gates self-initiation decision: requires dedicated Blóðtrú faith vs allows any faith accepting witchcraft. |
| `bm_lore` | `bm_lore_historical`<br>`bm_lore_agot` | `bm_lore_historical` | Historical campaign vs AGOT lore integration flavor. |

## Where the details live

| Piece | File |
| --- | --- |
| Game rule definitions | `common/game_rules/bm_game_rules.txt` |
| Text icons | `gui/bm_game_rule_texticons.gui` |
| Localization | `localization/english/bm_game_rules_l_english.yml` |
| AI prevalence modifiers | `common/scripted_modifiers/bm_blood_mage_prevalence_modifiers.txt` |
| Starting counties & holders effects | `common/scripted_effects/bm_starting_counties_effects.txt` |
| Yearly retention audits | `common/scripted_effects/bm_blood_mage_lifecycle_effects.txt` |
| Birth on-actions | `common/on_action/bm_blood_mage_prevalence_on_actions.txt` |

## Key Mechanics & Gotchas

- **AI Auditing:** In `player_only` or low-prevalence modes, yearly pulse strips traits from non-player AI characters who spontaneously acquire it.
- **Rule Syntax:** Always use the setting ID directly in `has_game_rule = <setting_id>` (e.g. `has_game_rule = bm_prevalence_player_only`).
