# Blood Mage Character Interactions

## Executive Summary

- **What:** Targeted character interactions for Lifeforce harvesting, trait theft, healing, retinue empowerment, and teaching blood magic.
- **Rule:** Uses `ai_targets` to avoid global scans. AI vetoes prevent draining close family, spouses, friends, and council.

### Interactions Master Table

| Interaction ID | Target | Cost & Requirements | XP Gain | Mechanical Effect |
| --- | --- | --- | --- | --- |
| `ask_for_blood_magic_interaction` | Friend, lover, soulmate, liege mage | Piety. Actor lacks trait, recipient has it. | None | Requests blood magic. Recipient grants via `bm_become_blood_mage_effect`. |
| `grant_blood_magic_interaction` | Courtier, family, spouse | Piety + Major Lifeforce. Recipient non-mage. | +2 benediction | Bestows `lifestyle_blood_mage` onto target via `bm_become_blood_mage_effect`. |
| `bm_get_blood_magic_from_prisoner_interaction` | Imprisoned blood mage | Piety. Actor non-mage, target captive mage. | None | Forcibly steals blood magic. Prisoner drained/maimed. |
| `lifedrain_prisoner_interaction` | Dungeon prisoner | Piety (`lifedrain_piety_cost_minor`). | +1 hematurgy | Kills prisoner (`death_lifedrain_reason`). Gives `lifeforce_modifier_minor`. |
| `lifedrain_courtier_event_interaction` | Courtier | Piety (`lifedrain_piety_cost_minor`). | +1 hematurgy | Drains courtier. Gives `lifeforce_modifier_minor`. Target gets `lifedrained_modifier` (health/stat hit). |
| `trait_drain_prisoner_event_interaction` | Dungeon prisoner | Piety. Target has congenital trait actor lacks. | +2 hematurgy | Duel (Prowess/Learning). Win: steals congenital trait. Target drained. |
| `heal_disease_minor` | Courtier, family, self | Minor Lifeforce. Target has minor ailment. | +1 benediction | Cures minor disease, wound, or illness. |
| `heal_disease_major` | Courtier, family, self | Major Lifeforce. Target has severe illness. | +2 benediction | Cures major illnesses, cancers, severe wounds. |
| `heal_disease_benediction` | Courtier, family, self | Major Lifeforce. Req: 50 Benediction XP. | +3 benediction | Cures permanent ailments (blind, maimed, infirm, lunatic_1, etc.). |
| `grant_lifeforce_interaction` | Other blood mage | Minor/Major Lifeforce. | +1-2 benediction | Transmutates Lifeforce stack to recipient blood mage. |
| `grant_crimson_warrior_interaction` | Knight or courtier | Piety + Minor Lifeforce. | +1 benediction | Gives `lifeforce_modifier_crimson_warrior` (+5 prowess, -0.2 health, -2 life exp). |
| `grant_crimson_champion_interaction` | Knight or courtier | Piety + Major Lifeforce. | +2 benediction | Gives `lifeforce_modifier_crimson_champion` (+10 prowess, -1.0 health, -7 life exp). |
| `bm_cast_blood_magic_self_channel_minor_lifeforce` | Self | Piety + Minor Lifeforce. | +1 enlightenment | Triggers temporary attribute enhancement (`bm_channel_lifeforce_enlightenment_minor.001`). |
| `bm_cast_blood_magic_self_attune_lifeforce` | Self | Piety + Minor Lifeforce. | None | Opens attunement selection (`bm_attune_lifeforce.001`). |
| `bm_cast_blood_magic_self_manifest_lifeforce` | Self | Piety. CD: 1 yr. | +5 enlightenment | Learning duel to generate Lifeforce. |
| `bm_cast_blood_magic_self_major_crimson_empowerment` | Self | Piety + Major Lifeforce. | +3 enlightenment | Triggers Crimson Empowerment track advancement (`bm_crimson_empowerment_event.001`). |
| `bm_cast_blood_magic_self_major_improve_education` | Self | Piety + Major Lifeforce. CD: 2 yrs. | +5 enlightenment | Upgrades existing education trait tier (`bm_education_enhancement.001`). |
| `bm_cast_blood_magic_self_major_new_education` | Self | Piety + Major Lifeforce. CD: 2 yrs. | +5 enlightenment | Unlocks a second education trait branch at tier 1 (`bm_education_new.001`). |
| `bm_cast_blood_magic_self_major_blood_rune` | Self | Piety + Major & Minor Lifeforce. CD: 5 yrs. | +5 benediction | Inscribes or upgrades body runes (`bm_crimson_rune.001`). |

## Key Mechanics & AI Logic

- **AI Harvesting Vetoes:** `factor = 0` blocks AI mages from draining close family, children, spouses, friends, lovers, knights, councillors, and high-opinion courtiers.
- **AI Teaching Priority:** AI rulers grant blood magic in strict order: spouse first, then children, then liege, then councillors.
- **Story Panel Sync:** Granting warrior/champion status automatically updates the Crimson Retinue in the Blood Magic panel.
- **Self-Interactions Only:** All personal blood magic rituals targeting the character themselves are invoked exclusively by right-clicking the character via self-character interactions. No duplicate decisions are used.
- **Request Description:** `ask_for_blood_magic_interaction` uses `ask_for_blood_magic_interaction_desc`: the actor receives magic from the recipient. Granting magic uses a separate description for the opposite direction.

## Where the details live

| Interaction Group | File |
| --- | --- |
| Become a Blood Mage (request or prisoner) | `common/character_interactions/bm_become_a_blood_mage.txt` |
| Harvest Lifeforce (prisoner & courtier) | `common/character_interactions/bm_drain_lifeforce.txt` |
| Drain Traits from Prisoners | `common/character_interactions/bm_drain_trait.txt` |
| Cure Illness (minor, major, benediction) | `common/character_interactions/bm_cure_illness_interactions.txt` |
| Grant Crimson Retinue (warrior, champion) | `common/character_interactions/bm_grant_blood_infused_prowess.txt` |
| Grant Blood Magic Trait | `common/character_interactions/bm_grant_blood_magic.txt` |
| Grant Lifeforce Stacks | `common/character_interactions/bm_grant_lifeforce.txt` |
| Self Magic (Minor rituals & harvesting) | `common/character_interactions/bm_cast_blood_magic_self_minor.txt` |
| Self Magic (Major rituals & empowerments) | `common/character_interactions/bm_cast_blood_magic_self_major.txt` |
| Debug interactions | `common/character_interactions/bm_debug_interactions.txt` |

## Gotchas

- **Kinslayer:** Draining family prisoners triggers vanilla kinslayer flags unless execution reasons exist.
- **Hiding Logic:** Interactions hide if the caster lacks the required Lifeforce modifier or minimum track XP.
