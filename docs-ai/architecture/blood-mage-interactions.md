# Blood Mage Character Interactions

## Executive Summary

- **What:** Targeted character interactions for Lifeforce harvesting, trait theft, healing, retinue empowerment, and teaching blood magic.
- **Rule:** Uses `ai_targets` to avoid global scans. AI vetoes prevent draining close family, spouses, friends, and council.

### Interactions Master Table

| Interaction ID | Target | Cost & Requirements | XP Gain | Mechanical Effect |
| --- | --- | --- | --- | --- |
| `ask_for_blood_magic_interaction` | Friend, lover, soulmate, liege mage | 250 Piety. Recipient requires Superior Lifeforce (consumed). | None | Requests blood magic. Recipient grants via `bm_become_blood_mage_effect` (or elevation). |
| `grant_blood_magic_interaction` | Courtier, family, spouse | 0 Piety + Superior Lifeforce. Recipient non-mage. | +4 bloodline (+5 if child/kin) | Bestows `lifestyle_blood_mage` onto target (or elevates Blood Knight). Consumes Superior Lifeforce. |
| `bm_bless_bloodline_interaction` | Child, dynasty kin | 35 Piety + Minor Lifeforce. Recipient not blessed. | +2 bloodline | Grants `bm_blessed_blood_modifier` (+1 all stats, +10% fertility, +0.25 health) for 10 years. |
| `bm_get_blood_magic_from_prisoner_interaction` | Imprisoned blood mage | Piety. Actor non-mage, target captive mage. | None | Forcibly steals blood magic. Prisoner drained/maimed. |
| `lifedrain_prisoner_interaction` | Dungeon prisoner | Piety (`lifedrain_piety_cost_minor`). | +1 hematurgy | Kills prisoner (`death_lifedrain_reason`). Gives `lifeforce_modifier_minor`. |
| `lifedrain_courtier_event_interaction` | Courtier | Piety (`lifedrain_piety_cost_minor`). | +1 hematurgy | Drains courtier. Gives `lifeforce_modifier_minor`. Target gets `lifedrained_modifier` (health/stat hit). |
| `trait_drain_prisoner_event_interaction` | Dungeon prisoner | Piety. Target has congenital trait actor lacks. | +2 hematurgy | Duel (Prowess/Learning). Win: steals congenital trait. Target drained. |
| `bm_heal_ailment` | Courtier, liege, family, spouse, knight, self | Lifeforce (tier-dependent) + Piety (15 / 35 / 100). Target has ailment. Blood Knights: minor only on others, minor & major on self. | Minor: +2 benediction (Mage) / +2 enlightenment (Knight self) / +1 vanguard & +1 benediction (Knight ally); Major: +4 benediction (Mage) / +4 enlightenment (Knight self); Deadly: +8 benediction (Mage only) | Opens event `bm_heal_ailment.0001` to choose and cure an individual ailment across 37 conditions. |
| `make_blood_knight_interaction` | Knight or courtier (cannot target self) | Blood Mage: 100 Piety + Major Lifeforce; Blood Knight: 200 Prestige + Minor Lifeforce OR 0 Prestige + Major Lifeforce. | Mage: +4 benediction; Knight: +2 vanguard (minor) / +4 vanguard (major) | Bestows `lifestyle_blood_knight` trait onto recipient. |
| `empower_blood_knight_interaction` | Sworn blood knight | Major Lifeforce (+10 XP to vanguard & slaughter) or Minor Lifeforce (+5 XP). | Major: +4 benediction; Minor: +2 benediction | Direct popup modal advancing martial tracks on recipient. |
| `grant_lifeforce_interaction` | Courtier or prisoner | Minor Lifeforce + 25 Piety, or Major Lifeforce + 50 Piety. | Minor: +1 enlightenment; Major: +2 enlightenment | Bestows Lifeforce modifier onto recipient. |
| `grant_lifeforce_interaction_reversed` | Courtier with `lifedrained_modifier` | 25 Piety + Major Lifeforce. | +4 benediction | Restores drained courtier: cleanses debuff, gives minor lifeforce and opinion. |
| `bm_curse_blood_interaction` | Alive character (non-self) | 50 Piety + Minor Lifeforce. Requires >= 10 Hematurgy XP. | Success: +2 hematurgy; Crit: +4 hematurgy; Fail: +1 hematurgy | Skill duel (Intrigue/Learning). Success: inflicts `bm_blood_curse_modifier` (-2 all stats, -1.5 health, -30% fertility, -3 prowess) for 5 yrs; Crit: curses, inflicts ill, and siphons Minor Lifeforce back; Fail: discovered, opinion malus. |
| `bm_debug_character_interaction` | Any character | Debug mode only. | None | Popup modal with 3 options: Make Blood Mage, Make Blood Knight, or Convert to Blóðtrú. |

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
| Cure Ailment (`bm_heal_ailment`) | `common/character_interactions/bm_cure_illness_interactions.txt` |
| Blood Knight (Make & Empower) | `common/character_interactions/bm_blood_knight_interactions.txt` |
| Grant Blood Magic Trait | `common/character_interactions/bm_grant_blood_magic.txt` |
| Bless Kin's Blood | `common/character_interactions/bm_bless_bloodline.txt` |
| Grant Lifeforce Stacks | `common/character_interactions/bm_grant_lifeforce.txt` |
| Cast Blood Curse | `common/character_interactions/bm_curse_blood.txt` |
| Debug interactions | `common/character_interactions/bm_debug_interactions.txt` |

## Gotchas

- **Kinslayer:** Draining family prisoners triggers vanilla kinslayer flags unless execution reasons exist.
- **Hiding Logic:** Interactions hide if the caster lacks the required Lifeforce modifier or minimum track XP.
- **Icons:** Each interaction looks up `gfx/interface/icons/character_interactions/<interaction_key>.dds`. All interactions use identical copies of the fiery blood drop icon (120×120 ARGB8888). Adding, renaming, or removing an interaction requires adding, renaming, or removing its corresponding `.dds` file.
