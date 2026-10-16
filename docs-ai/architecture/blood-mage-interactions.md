# Blood Mage Character Interactions

Living technical specification for character interactions in the Blood Mage mod.

## Executive Summary

- **What:** Targeted character interactions for Lifeforce harvesting, trait theft, healing, retinue empowerment, and teaching blood magic.
- **Rule:** Uses `ai_targets` to avoid global scans. AI vetoes prevent draining close family, spouses, friends, and council.

### Interactions Master Table

| Interaction ID | Target | Cost & Requirements | XP Gain | Mechanical Effect |
| --- | --- | --- | --- | --- |
| `ask_for_blood_magic_interaction` | Friend, lover, soulmate, liege mage | 250 Piety. Recipient requires Superior Lifeforce (consumed). Actor lacks Blood Mage and Blood Knight. | None | Requests blood magic. Recipient grants via `bm_become_blood_mage_effect`. |
| `grant_blood_magic_interaction` | Courtier, family, spouse | Major Lifeforce + 100 Piety OR Minor Lifeforce + 250 Piety. Actor is Blood Mage; recipient lacks Blood Mage and Blood Knight. | Major: +4 bloodline (+5 if child/kin); Minor: +2 bloodline | Bestows `lifestyle_blood_mage` onto target. |
| `make_blood_knight_interaction` | Sworn knight or courtier | Major Lifeforce + 100 Piety OR Minor Lifeforce + 250 Piety. Actor is Blood Knight; recipient lacks Blood Mage and Blood Knight. | Major: +4 vanguard; Minor: +2 vanguard | Bestows `lifestyle_blood_knight` onto target. |
| `bm_bless_bloodline_interaction` | Child, dynasty kin | 35 Piety + Minor Lifeforce. Recipient not blessed. | Mage: +2 bloodline; Knight: +2 vanguard | Grants `bm_blessed_blood_modifier` (+1 all stats, +10% fertility, +0.25 health) for 10 years. |
| `bm_get_blood_magic_from_prisoner_interaction` | Imprisoned blood mage | 100 Piety. Actor lacks Blood Mage and Blood Knight. | None | Forcibly steals blood magic via Learning/Prowess/Intrigue duel. Prisoner drained/maimed. |
| `lifedrain_prisoner_interaction` | Dungeon prisoner | Piety (`lifedrain_piety_cost_minor`). | +1 hematurgy | Kills prisoner (`death_lifedrain_reason`). Gives `lifeforce_modifier_minor`. |
| `lifedrain_courtier_event_interaction` | Free courtier or prisoner | Piety (`lifedrain_piety_cost_minor`). Blood Mage or Blood Knight. | +1 hematurgy (Mage) / +1 slaughter (Knight) | Siphons Minor Lifeforce (Mage: Intrigue/Learning; Knight: Prowess). Target gets `lifedrained_modifier` (health/stat hit). |
| `trait_drain_prisoner_event_interaction` | Dungeon prisoner | Piety. Blood Mage or Blood Knight. Target has congenital trait actor lacks (ranks 1–5). | +2 hematurgy (Mage) / +2 slaughter (Knight) | Duel (Learning). Win: steals congenital trait. Target drained/executed. |
| `bm_heal_ailment` | Courtier, liege, family, spouse, knight, lover, friend, councillor, self | Lifeforce (tier-dependent) + Piety (15 / 35 / 100). Target has ailment. Available to both Blood Mages and Blood Knights for all tiers (Minor, Major, Deadly). | Minor: +2 benediction (Mage) / +2 enlightenment (Knight self) / +1 vanguard & +1 benediction (Knight ally); Major: +4 benediction (Mage) / +4 enlightenment (Knight self) / +2 vanguard & +2 benediction (Knight ally); Deadly: +8 benediction (Mage & Knight) | Opens event `bm_heal_ailment.0001` to choose and cure an individual ailment across 37 conditions. |
| `empower_blood_knight_interaction` | Sworn blood knight | Major Lifeforce (+10 XP to vanguard & slaughter) or Minor Lifeforce (+5 XP). Blood Knight caster only. | Major: +4 benediction; Minor: +2 benediction | Direct popup modal advancing martial tracks on recipient. |
| `grant_lifeforce_interaction` | Courtier or prisoner | Minor Lifeforce + 25 Piety, or Major Lifeforce + 50 Piety. | Minor: +1 enlightenment; Major: +2 enlightenment | Bestows Lifeforce modifier onto recipient. |
| `grant_lifeforce_interaction_reversed` | Courtier with `lifedrained_modifier` | 25 Piety + Major Lifeforce. | +4 benediction | Restores drained courtier: cleanses debuff, gives minor lifeforce and opinion. |
| `bm_curse_blood_interaction` | Alive character (non-self) | 50 Piety + Minor Lifeforce. Requires >= 10 Hematurgy XP. | Success: +2 hematurgy; Crit: +4 hematurgy; Fail: +1 hematurgy | Skill duel (Intrigue/Learning). Success: inflicts `bm_blood_curse_modifier` (-2 all stats, -1.5 health, -30% fertility, -3 prowess) for 5 yrs; Crit: curses, inflicts ill, and siphons Minor Lifeforce back; Fail: discovered, opinion malus. |
| `bm_debug_character_interaction` | Any character | Debug mode only. | None | Popup modal with 3 options: Make Blood Mage, Make Blood Knight, or Convert to Blóðtrú. |

## Key Mechanics & AI Logic

- **AI Hostile Magic Vetoes:** `factor = 0` blocks AI mages and knights from using hostile magic (`lifedrain_prisoner`, `lifedrain_courtier`, `trait_drain_prisoner`, `curse_blood`, `bm_get_blood_magic_from_prisoner`) against councillors, liege, lovers/soulmates, spouses/consorts, dynasty members, close family, children, wards, knights, and high-opinion targets (opinion > 20) unless they are a rival or nemesis.
- **AI Positive Magic Prioritisation & Rival Veto:** `factor = 0` strictly vetoes performing positive magic (`bm_heal_ailment`, `bless_bloodline`, `make_blood_knight`, `empower_blood_knight`, `grant_blood_magic`, `grant_lifeforce_reversed`) on rivals and nemeses.
- **Class Parity in Initiation:** Knights create Knights via `make_blood_knight_interaction`; Mages create Mages via `grant_blood_magic_interaction`. Costs are symmetric: Major Lifeforce + 100 Piety OR Minor Lifeforce + 250 Piety.
- **Story Panel Sync:** Granting warrior/champion status automatically updates the Blood Retinue in the Blood Magic panel.
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
| Cure Ailment Alert (`bm_action_can_heal`) | `common/important_actions/bm_important_actions.txt` |
| Blood Knight (Make & Empower) | `common/character_interactions/bm_blood_knight_interactions.txt` |
| Grant Blood Magic Trait | `common/character_interactions/bm_grant_blood_magic.txt` |
| Bless Kin's Blood | `common/character_interactions/bm_bless_bloodline.txt` |
| Grant Lifeforce Stacks | `common/character_interactions/bm_grant_lifeforce.txt` |
| Cast Blood Curse | `common/character_interactions/bm_curse_blood.txt` |
| Debug interactions | `common/character_interactions/bm_debug_interactions.txt` |
