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
| `make_blood_knight_interaction` | Knight, courtier, or self | 100 Piety + Major Lifeforce. | +2 benediction | Bestows `lifestyle_blood_knight` trait. |
| `empower_blood_knight_interaction` | Sworn blood knight or self | Major Lifeforce (+10 XP) or Minor Lifeforce (+5 XP). | +2 / +1 benediction | Direct popup modal advancing all 3 combat tracks. |

## Key Mechanics & AI Logic

- **AI Harvesting Vetoes:** `factor = 0` blocks AI mages from draining close family, children, spouses, friends, lovers, knights, councillors, dynasty members, and high-opinion courtiers (opinion > 20) unless rival or nemesis. Enforced across both lifedrain interactions and prisoner trait-draining.
- **AI Teaching Priority:** AI rulers grant blood magic in order: spouse first (+100), children (+75), liege (+50), knights (+35), councillors (+25), dynasty (+25).
- **Story Panel Sync:** Granting warrior/champion status automatically updates the Blood Retinue in the Blood Magic panel.
- **Personal Rituals as Decisions:** Personal blood magic rituals targeting the character themselves (Channel Minor Lifeforce, Attunement, Manifest Lifeforce, Blood Empowerment, Education enhancement, and Blood Runes) are decisions under `bm_decision_group` in `common/decisions/cast_magic/bm_cast_blood_magic_*.txt`.
- **Debug Logging Standard:** Character interactions log to `logs/debug.log` using standardized prefixes:
  - `BloodMageInteraction: <name> | Actor: <name> (ID:<id>, <Player|AI>) -> Recipient: <name> (ID:<id>, <Player|AI>) | Rel: <relation> | Tag: <role_tag> | Opinion: <opinion>`
  - `BloodMageSelfCast: <name> | Actor: <name> (ID:<id>, <Player|AI>)`
  - `BloodMageExecution: lifedrain | Executioner: <name> ... -> Victim: <name> ...`

## Where the details live

| Interaction Group | File |
| --- | --- |
| Become a Blood Mage (request or prisoner) | `common/character_interactions/bm_become_a_blood_mage.txt` |
| Harvest Lifeforce (prisoner & courtier) | `common/character_interactions/bm_drain_lifeforce.txt` |
| Drain Traits from Prisoners | `common/character_interactions/bm_drain_trait.txt` |
| Cure Illness (minor, major, benediction) | `common/character_interactions/bm_cure_illness_interactions.txt` |
| Blood Knight (Make & Empower) | `common/character_interactions/bm_blood_knight_interactions.txt` |
| Grant Blood Magic Trait | `common/character_interactions/bm_grant_blood_magic.txt` |
| Grant Lifeforce Stacks | `common/character_interactions/bm_grant_lifeforce.txt` |
| Debug interactions | `common/character_interactions/bm_debug_interactions.txt` |

## Gotchas

- **Kinslayer:** Draining family prisoners triggers vanilla kinslayer flags unless execution reasons exist.
- **Hiding Logic:** Interactions hide if the caster lacks the required Lifeforce modifier or minimum track XP.
