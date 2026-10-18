# Blood Mage Character Interactions

Living technical specification for character interactions in the Blood Mage mod.

## Executive Summary

- **What:** Targeted character interactions for Lifeforce harvesting, trait theft, healing, retinue empowerment, and teaching blood magic.
- **Category:** All 17 mod gameplay character interactions are grouped into the dedicated category `interaction_category_bm_blood_magic` ("Blood Magic", `index = 16`, crimson `{ 0.75 0.12 0.12 1 }`) defined in `common/character_interaction_categories/bm_character_interaction_categories.txt`.
- **Rule:** Uses `ai_targets` to avoid global scans. AI vetoes prevent draining close family, spouses, friends, and council.

### Interactions Master Table

| Interaction ID | Target | Cost & Requirements | XP Gain | Mechanical Effect |
| --- | --- | --- | --- | --- |
| `ask_for_blood_magic_interaction` | Friend, lover, soulmate, liege mage | 250 Piety. Recipient requires Superior Lifeforce (consumed). Actor lacks Blood Mage and Blood Knight. | None | Requests blood magic. Recipient grants via `bm_become_blood_mage_effect`. |
| `grant_blood_magic_interaction` | Courtier, family, spouse | Major Lifeforce + 100 Piety OR Minor Lifeforce + 250 Piety. Actor is Blood Mage; recipient lacks Blood Mage and Blood Knight. | Major: +4 bloodline (+5 if child/kin); Minor: +2 bloodline | Bestows `lifestyle_blood_mage` onto target. |
| `make_blood_knight_interaction` | Sworn knight or courtier | Major Lifeforce + 100 Piety OR Minor Lifeforce + 250 Piety. Actor is Blood Knight; recipient lacks Blood Mage and Blood Knight. | Major: +4 vanguard; Minor: +2 vanguard | Bestows `lifestyle_blood_knight` onto target. |
| `bm_bless_bloodline_interaction` | Child, dynasty kin | 35 Piety + Minor Lifeforce. Recipient not blessed with any blessing. | Mage: +2 bloodline; Knight: +2 vanguard | 3-way modal (`send_option`): **Sovereign** (+2 Dip/Stew, +10 Vassal Op, -20% Short Reign, +0.25 Health), **Iron** (+2 Mar, +4 Prowess, +15% Knight Eff, +0.50 Health), or **Crucible** (+25% Fertility, +15% Pos Congenital, -20% Stress Gain, +0.50 Health) for 10 years. |
| `bm_anoint_heir_interaction` | Primary heir or child | 250 Piety + Major Lifeforce. Actor is Blood Mage or Blood Knight. | Mage: +5 bloodline; Knight: +5 vanguard | Consecrates target with permanent `bm_anointed_heir_modifier` (+0.50 Health, +15 Dynasty Opinion, +15% Lifestyle XP, -25% Short Reign Duration). Clears from prior siblings. Hooks into death to awaken class trait, transfer 1 stack of each held Lifeforce tier, and transfer 25% of all active trait track XP upon ruler death. |
| `bm_demand_blood_tithe_interaction` | Adult living house member | 50 Piety, 2-yr CD. Actor is House Head Blood Mage or Blood Knight; target not recently drained. | Mage: +2 bloodline; Knight: +2 vanguard | Siphons **1 Major Lifeforce** (if target is Blood Mage/Knight) or **1 Minor Lifeforce** (mundane kin). Target receives `recently_lifedrained_modifier` and 1-yr `lifeforce_modifier_negative_minor`, plus -25 Opinion unless following a Blood Cult faith or `loyal`. |
| `bm_get_blood_magic_from_prisoner_interaction` | Imprisoned blood mage | 100 Piety. Actor lacks Blood Mage and Blood Knight. | None | Forcibly steals blood magic via Learning/Prowess/Intrigue duel. Prisoner drained/maimed. |
| `lifedrain_prisoner_event_interaction` | Dungeon prisoner | 50 Piety (`lifedrain_piety_cost_major`). Actor is Blood Mage; prisoner not already drained. | +2 hematurgy | Executes prisoner (`death_lifedrain_reason`). Grants `lifeforce_modifier_major` (+25 Gold with Superior **Nábrókarstafur**). |
| `lifedrain_courtier_event_interaction` | Free courtier or prisoner | 25 Piety (`lifedrain_piety_cost_minor`), 3-mo CD. Blood Mage or Blood Knight. | +1 hematurgy (Mage) / +1 slaughter (Knight) | Siphons Minor Lifeforce (Mage: Intrigue/Learning; Knight: Prowess). Target gets `lifedrained_modifier` (health/stat hit). Discovery penalty negated by Superior **Hulinhjálmur**. |
| `trait_drain_prisoner_event_interaction` | Dungeon prisoner | 100–325 Piety + Major Lifeforce. CD: 60d (15d with Superior **Hulinhjálmur**). Blood Mage or Blood Knight. Target has congenital trait actor lacks (ranks 1–5, fecund, giant, pure_blooded). | +2 hematurgy (Mage) / +2 slaughter (Knight) | Duel (Learning). Win: steals congenital trait; target executed (`death_lifedrain_reason`). |
| `bm_heal_ailment` | Courtier, liege, family, spouse, knight, lover, friend, councillor, self | Lifeforce (Minor / Major / Minor+Major) + Piety (15 / 35 / 100; halved by Superior **Drepsóttarstafur**). Target has ailment. Available to both Blood Mages and Blood Knights for all tiers (Minor, Major, Deadly). | Minor: +2 benediction (Mage) / +2 enlightenment (Knight self) / +1 vanguard & +1 benediction (Knight ally); Major: +4 benediction (Mage) / +4 enlightenment (Knight self) / +2 vanguard & +2 benediction (Knight ally); Deadly: +8 benediction (Mage & Knight) | Opens event `bm_heal_ailment.0001` to choose and cure an individual ailment across 37 conditions. |
| `bm_inscribe_rune_other_interaction` | Adult courtier, child, dynasty kin, spouse/consort, sworn knight, Blood Golem, liege | Minor: 0p + Minor LF (Rank 2, >=25 XP); Major: 200p + Major LF (Rank 3, >=50 XP, target has Minor rune); Superior: 400p + Superior LF (**Mage only**, Rank 4, >=100 XP, target has Major rune). CD: 5 yrs (`bm_blood_rune_other_cooldown`). | Minor: +4 benediction; Major: +5 benediction; Superior: +10 benediction | Inscribes or upgrades Blood Rune depth (Minor -> Major -> Superior) on target (`+20` `magic_opinion_positive`). Target receives passive yearly Lifeforce rolls (`blood_mage_yearly_events.003`) and can carve their own Galdrastafir stave once reaching Superior. |
| `empower_blood_knight_interaction` | Sworn blood knight | Major Lifeforce (+10 XP to vanguard & slaughter) or Minor Lifeforce (+5 XP). Blood Knight caster only. | Major: +4 benediction; Minor: +2 benediction | Direct popup modal advancing martial tracks on recipient. |
| `grant_lifeforce_interaction` | Courtier or prisoner | Minor Lifeforce + 25 Piety, or Major Lifeforce + 50 Piety. | Minor: +1 enlightenment; Major: +2 enlightenment | Bestows Lifeforce modifier onto recipient. |
| `grant_lifeforce_interaction_reversed` | Courtier with `lifedrained_modifier` | 25 Piety + Major Lifeforce. | +4 benediction | Restores drained courtier: cleanses debuff, gives minor lifeforce and opinion. |
| `bm_curse_blood_interaction` | Alive character (non-self) | 50 Piety + Minor Lifeforce. Requires Blood Mage with >= 10 Hematurgy XP. CD: 1 yr. | Success: +2 hematurgy; Crit: +4 hematurgy; Fail: +1 hematurgy | Skill duel (Intrigue/Learning). Success: inflicts `bm_blood_curse_modifier` (-2 all stats, -1.5 health, -30% fertility, -3 prowess) for 5 yrs; Crit: curses, inflicts `ill`, and siphons Minor Lifeforce back; Fail: discovered, opinion malus (negated by Superior **Hulinhjálmur**). |
| `bm_reshape_personality_interaction` | Relationship target (courtier, spouse, friend, lover, soulmate, dynasty, ward, knight) | 250 Piety + Major Lifeforce (no Cast Major Blood Magic debuff). Requires Devotion level >= 3. CD: 5 yrs on success, 1 yr on failure. | Success: +4 enlightenment; Fail: +1 enlightenment | **Influence Personality**: Guided two-step ritual (`bm_reshape_personality.0001` & `.0002`) resolved via a Learning duel challenge (50% base at equal Learning, capped at 95% for >= 20 difference, floored at 5% at -20 difference). Success removes target trait, purges opposite traits, and imprints caster trait (no opinion bonus); failure leaves traits unchanged. |
| `bm_manifest_lifeforce_interaction` | Self (actor = recipient) | 100/250/500/1000 Piety across 4 tiers. Blood Mage or Blood Knight, Devotion level >= 2. CD: 1 yr. | +1 / +3 / +5 / +7 enlightenment | Meditative trance converting Piety directly into Lifeforce via Learning contest. |
| `bm_debug_character_interaction` | Any character | Debug mode only. | None | Popup modal with 3 options: Make Blood Mage, Make Blood Knight, or Convert to Blóðtrú. (Retained under `interaction_debug_main`). |

## Key Mechanics & AI Logic

- **Current Situation Healing Alert (`bm_action_can_heal`):** Defined in `common/important_actions/bm_important_actions.txt`. Surfaces a top-bar Current Situation notification whenever the player (Blood Mage or Blood Knight) has sufficient Piety and Lifeforce to heal an afflicted priority target (self, close family, spouse, lovers, friends, liege, councillors, or knights), clicking directly into `bm_heal_ailment`.
- **AI Hostile Magic Vetoes:** `factor = 0` blocks AI mages and knights from using hostile magic (`lifedrain_prisoner`, `lifedrain_courtier`, `trait_drain_prisoner`, `curse_blood`, `bm_get_blood_magic_from_prisoner`) against councillors, liege, lovers/soulmates, spouses/consorts, dynasty members, close family, children, wards, knights, and high-opinion targets (opinion > 20) unless they are a rival or nemesis.
- **AI Positive Magic Prioritisation & Rival Veto:** `factor = 0` strictly vetoes performing positive magic (`bm_heal_ailment`, `bless_bloodline`, `bm_anoint_heir_interaction`, `make_blood_knight`, `empower_blood_knight`, `grant_blood_magic`, `grant_lifeforce_reversed`, `bm_inscribe_rune_other_interaction`) on rivals and nemeses.
- **Class Parity in Initiation:** Knights create Knights via `make_blood_knight_interaction`; Mages create Mages via `grant_blood_magic_interaction`. Costs are symmetric: Major Lifeforce + 100 Piety OR Minor Lifeforce + 250 Piety.
- **Story Panel Sync:** Granting warrior/champion status automatically updates the Blood Retinue in the Blood Magic panel.
- **Debug Logging Standard:** Character interactions log to `logs/debug.log` using standardized prefixes:
  - `BloodMageInteraction: <name> | Actor: <name> (ID:<id>, <Player|AI>) -> Recipient: <name> (ID:<id>, <Player|AI>) | Rel: <relation> | Tag: <role_tag> | Opinion: <opinion>`
  - `BloodMageSelfCast: <name> | Actor: <name> (ID:<id>, <Player|AI>)`
  - `BloodMageExecution: lifedrain | Executioner: <name> ... -> Victim: <name> ...`

## Where the details live

| Interaction Group | File |
| --- | --- |
| Interaction Category Definition | `common/character_interaction_categories/bm_character_interaction_categories.txt` |
| Become a Blood Mage (request or prisoner) | `common/character_interactions/bm_become_a_blood_mage.txt` |
| Harvest Lifeforce (prisoner & courtier) | `common/character_interactions/bm_drain_lifeforce.txt` |
| Drain Traits from Prisoners | `common/character_interactions/bm_drain_trait.txt` |
| Cure Ailment (`bm_heal_ailment`) | `common/character_interactions/bm_cure_illness_interactions.txt` |
| Cure Ailment Alert (`bm_action_can_heal`) | `common/important_actions/bm_important_actions.txt` |
| Inscribe Blood Rune on Other | `common/character_interactions/bm_inscribe_rune_other.txt` |
| Blood Knight (Make & Empower) | `common/character_interactions/bm_blood_knight_interactions.txt` |
| Grant Blood Magic Trait | `common/character_interactions/bm_grant_blood_magic.txt` |
| Bless Kin's Blood | `common/character_interactions/bm_bless_bloodline.txt` |
| Dynasty Interactions (Anoint Heir, Tithe) | `common/character_interactions/bm_dynasty_interactions.txt` |
| Grant Lifeforce Stacks | `common/character_interactions/bm_grant_lifeforce.txt` |
| Cast Blood Curse | `common/character_interactions/bm_curse_blood.txt` |
| Influence Personality | `common/character_interactions/bm_reshape_personality.txt` |
| Manifest Lifeforce (Self) | `common/character_interactions/bm_manifest_lifeforce.txt` |
| Debug interactions | `common/character_interactions/bm_debug_interactions.txt` |
