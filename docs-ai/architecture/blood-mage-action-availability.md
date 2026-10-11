# Blood Mage vs Blood Knight Action Availability

Living technical specification comparing actions available to Blood Mages (`lifestyle_blood_mage`) and Blood Knights (`lifestyle_blood_knight`).

## Executive Summary

- **What:** Comparative availability matrix across decisions, rituals, targeted interactions, combat mechanics, and trait tracks.
- **Rule of Thumb:**
  - **Blood Mage:** Full mastery over Lifeforce distillation (Superior tier), creation of Blood Golems, lethal/mass prisoner draining, courtier draining, high-tier trait theft (ranks 3–5), remote blood curses, kin blood blessings, and deadly healing.
  - **Blood Knight:** Battlefield martial specialists who harvest Lifeforce through direct single-combat kills, military victories, and annual ambient condensing (~33% roll). Access to Minor and Major Blood Magic rituals (including `lifestyle_blood_empowerment`), self-healing (minor & major), ally healing (minor only), non-lethal prisoner lifedrain (via prowess duel), captive trait theft (up to rank 2), and education elevation up to 4★. Can create fellow Blood Knights or elevate to Blood Mage.

---

## Master Availability Table

| Action | Mage | Knight |
| --- | :---: | :---: |
| **Decisions & Hubs** | | |
| Manifest Lifeforce (`bm_manifest_lifeforce_decision`) | ✅ | ✅ |
| Manifest Superior Lifeforce (`bm_manifest_superior_lifeforce_decision`) | ✅ | ❌ |
| Seek Power (`seek_power_decision` / `seek_power_decision_wanderer`) | ✅ | ❌ |
| Seek Power as Blood Knight (`seek_power_decision_blood_knight`) | ❌ | ✅ |
| Cast Minor Blood Magic Hub (`bm_cast_blood_magic_minor_decision`) | ✅ | ✅ |
| Cast Major Blood Magic Hub (`bm_cast_blood_magic_major_decision`) | ✅ | ✅ |
| Cast Superior Blood Magic Hub (`bm_cast_blood_magic_superior_decision`) | ✅ | ❌ |
| Create Blood Golem (`blood_golem_creation_decision`) | ✅ | ❌ |
| Mass Lifedrain Prisoners (`mass_lifedrain_prisoners_decision`) | ✅ | ❌ |
| Become Blood Cultist (`become_blood_cultist_decision`) | ✅ | ❌ |
| Repair Blóðtrú Reformation (`bm_repair_blodtru_reformation_decision`) | ✅ | ✅ |
| Elevate to Blood Mage (`bm_elevate_to_blood_mage_decision`) | ❌ | ✅ |
| **Minor Rituals (within Minor Hub)** | | |
| Channel Minor Lifeforce | ✅ | ✅ |
| Attune Lifeforce (Affinity Selection) | ✅ | ✅ |
| Condense Lifeforce (Minor + Piety -> Major) | ✅ | ✅ |
| Purge Bodily Impurities (Cure Wounds/Scars/Bad Traits) | ✅ | ✅ |
| **Major Rituals (within Major Hub)** | | |
| Blood Empowerment (Unlock `lifestyle_blood_empowerment`) | ✅ | ✅ |
| Improve Education (Tiers 1★ to 4★) | ✅ | ✅ |
| Inscribe Minor Blood Rune | ✅ | ✅ |
| Inscribe Major Blood Rune | ✅ | ✅ |
| Empower Bloodline (House Prowess / Stats) | ✅ | ✅ |
| Manifest Perfection (Congenital Traits to Rank 3) | ✅ | ✅ |
| **Superior Rituals (within Superior Hub)** | | |
| Master Education (Legendary 5★) | ✅ | ❌ |
| Embrace New Education (Secondary Education) | ✅ | ❌ |
| Inscribe Superior Blood Rune | ✅ | ❌ |
| Manifest Transcendent Perfection (Congenital Traits Ranks 4–5) | ✅ | ❌ |
| Forge Blood Golem | ✅ | ❌ |
| **Targeted Character Interactions** | | |
| Make Blood Knight (`make_blood_knight_interaction`) | ✅ | ✅ |
| Empower Blood Knight (`empower_blood_knight_interaction`) | ✅ | ❌ |
| Grant Blood Magic (`grant_blood_magic_interaction`) | ✅ | ❌ |
| Ask for Blood Magic (`ask_for_blood_magic_interaction`) | ❌ | ✅ |
| Steal Blood Magic from Prisoner (`bm_get_blood_magic_from_prisoner_interaction`) | ❌ | ✅ |
| Heal Ailment: Minor on Self (`bm_heal_ailment`) | ✅ | ✅ |
| Heal Ailment: Major on Self (`bm_heal_ailment`) | ✅ | ✅ |
| Heal Ailment: Deadly on Self (`bm_heal_ailment`) | ✅ | ❌ |
| Heal Ailment: Minor on Others (`bm_heal_ailment`) | ✅ | ✅ |
| Heal Ailment: Major & Deadly on Others (`bm_heal_ailment`) | ✅ | ❌ |
| Lifedrain Prisoner (`lifedrain_prisoner_event_interaction`) | ✅ (Lethal Major) | ❌ |
| Minor Lifedrain (`lifedrain_courtier_event_interaction`) | ✅ (Courtiers & Prisoners) | ✅ (Prisoners only) |
| Drain Trait from Prisoner (`trait_drain_prisoner_event_interaction`) | ✅ (Up to rank 5) | ✅ (Up to rank 2) |
| Grant Lifeforce Stacks (`grant_lifeforce_interaction`) | ✅ | ❌ |
| Restore Drained Courtier (`grant_lifeforce_interaction_reversed`) | ✅ | ❌ |
| Bless Bloodline (`bm_bless_bloodline_interaction`) | ✅ | ❌ |
| Cast Blood Curse (`bm_curse_blood_interaction`) | ✅ | ❌ |
| **Combat & Passive Harvesting** | | |
| Single Combat Kill Lifeforce Harvest (+5 Slaughter XP, +1 Minor Lifeforce) | ❌ | ✅ |
| Battle Victory (+4/+3 Vanguard XP, 33% Minor Lifeforce) | ❌ | ✅ |
| Battle Defeat Survival (+1 Vanguard XP, +1 Enlightenment XP) | ❌ | ✅ |
| Tournament Completion / Victory (+3 Slaughter XP) | ❌ | ✅ |
| Annual Ambient Lifeforce Roll (~33% Minor Lifeforce) | ❌ | ✅ |
| **Trait Tracks Available** | | |
| Ancient (`ancient`) | ✅ | ✅ |
| Benediction (`benediction`) | ✅ | ✅ |
| Enlightenment (`enlightenment`) | ✅ | ✅ |
| Bloodline (`bloodline`) | ✅ | ❌ |
| Hematurgy (`hematurgy`) | ✅ | ❌ |
| Vanguard (`vanguard`) | ❌ | ✅ |
| Slaughter (`slaughter`) | ❌ | ✅ |
| Blood Empowerment Tracks (Dynasty, Mastery, Presence, Prosperity, Shadows) | ✅ | ✅ |

---

## Key Differences

### Mage-Exclusive Actions
1. **Superior Blood Magic:** Superior Lifeforce distillation, 5★ master education, secondary education, superior runes, and blood golem creation.
2. **Lethal & Mass Harvesting:** Lethal major prisoner draining (`lifedrain_prisoner_event_interaction`), mass prisoner draining, draining unlanded courtiers, high-tier trait draining (ranks 3–5), and remote blood curses.
3. **Advanced Restoration & Dynasty:** Curing deadly ailments on self/others, curing major ailments on others, restoring drained courtiers, granting Lifeforce to allies, and blessing kin's blood.
4. **Blood Mage Bestowal:** Bestowing `lifestyle_blood_mage` via interaction, empowering sworn blood knights with martial track XP.

### Knight-Exclusive Actions
1. **Martial Lifeforce Harvesting:** Gaining Minor Lifeforce on single-combat duel fatalities and winning army battles (commander +4 / knight +3 Vanguard XP, 33% Minor Lifeforce).
2. **Passive Ambient Vitality:** ~33% annual ambient roll (`blood_mage_yearly_events.004`) to condense Minor Lifeforce (strictly exclusive to Blood Knights; Mages do not receive ambient Lifeforce).
3. **Martial Progression:** Gaining XP through tournaments, army leadership, and duel victories in `vanguard` and `slaughter` tracks.
4. **Blood Knight Seek Power:** Dedicated 1-year cooldown wilderness hunt targeting martial XP and lifeforce.
5. **Ascension Path:** Elevating to full Blood Mage via `bm_elevate_to_blood_mage_decision` (requiring Learning > 30, piety rank 3, and 500 Piety), asking an allied Blood Mage for elevation, or stealing blood magic from an imprisoned mage.

### Shared Actions
1. **Active Lifeforce Generation:** Generating Lifeforce through `bm_manifest_lifeforce_decision` (Learning check for both).
2. **Minor Rituals:** Attunement, channeling minor lifeforce, condensing Minor into Major Lifeforce, and purging bodily impurities/wounds.
3. **Major Rituals:** Unlocking and advancing `lifestyle_blood_empowerment`, education upgrades up to 4★, minor/major blood runes, empowering bloodline, and manifesting congenital traits to rank 3.
4. **Prisoner Siphoning & Trait Theft:** Non-lethal minor lifedrain on imprisoned captives (Mages test Intrigue/Learning; Knights test Prowess) and stealing congenital traits from prisoners up to rank 2.
5. **Knight Creation:** Bestowing `lifestyle_blood_knight` upon sworn knights/courtiers.
6. **Restorative Self-Healing:** Curing minor and major ailments on self; curing minor ailments on allies.
7. **Shared Trait Tracks:** Advancing `ancient`, `benediction`, and `enlightenment` tracks.

---

## Where the details live

| Concept | File |
| --- | --- |
| Decision definitions | `common/decisions/` (`bm_manifest_*.txt`, `bm_cast_blood_magic_*.txt`, `bm_seek_power_*.txt`) |
| Character interactions | `common/character_interactions/` (`bm_*.txt`) |
| Minor ritual events | `events/bm_cast_blood_magic_minor_events.txt` |
| Major ritual events | `events/bm_cast_blood_magic_major_events.txt` |
| Superior ritual events | `events/bm_cast_blood_magic_superior_events.txt` |
| Blood Knight elevation | `common/decisions/become_mage/bm_elevate_blood_knight_decision.txt`<br>`events/bm_blood_knight_elevation_events.txt` |
| Combat on-actions & harvesting | `common/on_action/bm_duel_on_actions.txt`<br>`common/on_action/bm_combat_on_actions.txt` |
| Trait definitions & tracks | `common/traits/bm_blood_mage_trait.txt`<br>`common/traits/bm_blood_knight_trait.txt` |
