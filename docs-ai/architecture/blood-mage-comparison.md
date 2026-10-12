# Blood Mage vs Blood Knight Breakdown

Living technical specification comparing actions and capabilities between Blood Mages (`lifestyle_blood_mage`) and Blood Knights (`lifestyle_blood_knight`).

## Blood Mage

### Decisions & Rituals

| Action | Description |
| --- | --- |
| Cast Superior Blood Magic Hub (`bm_cast_blood_magic_superior_decision`) | Opens superior rites modal; requires `lifestyle_blood_mage`, Superior Lifeforce, Devotion level >= 2. |
| Manifest Superior Lifeforce (`bm_manifest_superior_lifeforce_decision`) | Distills 1 Minor + 1 Major Lifeforce into Superior Lifeforce via Learning duel (costs 250 Piety; Devotion level >= 3). |
| Seek Power (`seek_power_decision` / `seek_power_decision_wanderer`) | Wilderness hunt event chain harvesting Lifeforce and school XP (2-yr cooldown landed, 1-yr wanderer). |
| Create Blood Golem (`blood_golem_creation_decision`) | Spawns and shapes synthetic courtier in `bm_house_golem` (costs 500 Piety + Superior Lifeforce; 3-yr cooldown). |
| Mass Lifedrain Prisoners (`mass_lifedrain_prisoners_decision`) | Executes all dungeon captives to harvest Lifeforce and Hematurgy XP (`death_lifedrain_reason`). |
| Become Blood Cultist (`become_blood_cultist_decision`) | Religious decision converting ruler and realm to Blóðtrú faith (costs 250 Piety + 1 Major Lifeforce; 10-yr cooldown). |
| Master Education (5★) | Upgrades 4★ education to legendary 5★ tier via mental duel (costs scaled Piety + Superior Lifeforce; 2-yr cooldown). |
| Embrace New Education | Grants secondary 1-star education trait (costs 1000 Piety + Superior Lifeforce; 2-yr cooldown). |
| Inscribe Superior Blood Rune | Inscribes tier 3 blood rune (+10 Ancient XP; costs Superior Lifeforce; 5-yr cooldown). |
| Manifest Transcendent Perfection | Manifests congenital traits at ranks 4 and 5 (+6 Bloodline XP, +2 Enlightenment XP; costs Superior Lifeforce; 3-yr cooldown). |
| Forge Blood Golem (Rite) | In-hub superior rite crafting a blood golem (+5 Bloodline XP; costs Superior Lifeforce). |
| Commune with Bloodline | Calls on ancestral blood for realm-wide `bm_bloodline_communion` modifier (+2 Bloodline XP; costs 50 Piety + Minor Lifeforce; 3-yr cooldown). |

### Interactions & Tracks

| Action | Description |
| --- | --- |
| Grant Blood Magic (`grant_blood_magic_interaction`) | Bestows `lifestyle_blood_mage` on uninitiated mortal or elevates Blood Knight (costs Superior Lifeforce; +4–5 Bloodline XP). |
| Empower Blood Knight (`empower_blood_knight_interaction`) | Modal interaction granting +10 martial XP (Major Lifeforce) or +5 martial XP (Minor Lifeforce) to sworn knight. |
| Lethal Major Lifedrain (`lifedrain_prisoner_event_interaction`) | Executes dungeon captive for Major Lifeforce and +1 Hematurgy XP (`death_lifedrain_reason`). |
| Drain Courtier (`lifedrain_courtier_event_interaction`) | Siphons Minor Lifeforce from free courtier, inflicting `lifedrained_modifier` debuff and +1 Hematurgy XP. |
| High-Tier Trait Theft (`trait_drain_prisoner_event_interaction`) | Steals rank 3+ congenital traits (Genius, Beautiful, Herculean) from captive mortals via skill duel. |
| Grant Lifeforce (`grant_lifeforce_interaction`) | Bestows Minor or Major Lifeforce modifier onto courtier or prisoner. |
| Restore Drained Courtier (`grant_lifeforce_interaction_reversed`) | Cleanses `lifedrained_modifier` debuff, grants Minor Lifeforce and +4 Benediction XP (costs 25 Piety + Major Lifeforce). |
| Bless Bloodline (`bm_bless_bloodline_interaction`) | Grants `bm_blessed_blood_modifier` (+1 all stats, +10% fertility, +0.25 health) to kin for 10 yrs (costs 35 Piety + Minor Lifeforce; +2 Bloodline XP). |
| Cast Blood Curse (`bm_curse_blood_interaction`) | Remote curse via Intrigue/Learning duel inflicting `bm_blood_curse_modifier` (-2 all stats, -1.5 health, -30% fertility, -3 prowess) for 5 yrs (costs 50 Piety + Minor Lifeforce; >= 10 Hematurgy XP). |
| Heal Deadly Ailments (`bm_heal_ailment`) | Cures fatal ailments (bubonic plague, cancer, consumption) on self and allies (costs 100 Piety + Superior Lifeforce; +8 Benediction XP). |
| Heal Major Ailments on Others (`bm_heal_ailment`) | Cures major ailments (blind, incapable, infirm, gout) on allies (costs 35 Piety + Major Lifeforce; +4 Benediction XP). |
| Bloodline Track (`bloodline`) | Exclusive track: +1 domain limit & +10% gold at 30/60/90 XP, construction speed/cost, development, stewardship per prestige rank. |
| Hematurgy Track (`hematurgy`) | Exclusive track: +1 hostile scheme at 50/100 XP, hostile scheme speed/success, natural dread baseline, tyranny decay. |

---

## Blood Knight

### Decisions & Combat Harvesting

| Action | Description |
| --- | --- |
| Seek Power as Blood Knight (`seek_power_decision_blood_knight`) | Dedicated 1-year cooldown wilderness expedition awarding martial XP (`slaughter`, `vanguard`, `enlightenment`) and harvesting Lifeforce. |
| Elevate to Blood Mage (`bm_elevate_to_blood_mage_decision`) | Ritual ascension trial to convert into `lifestyle_blood_mage` (requires Learning > 30, piety rank 3, Minor or Major Lifeforce; costs 500 Piety; transfers XP 1:1, converts 50% martial). |
| Single Combat Fatality Harvest | Killing an opponent in lethal single combat awards +5 Slaughter XP and grants 1 Minor Lifeforce. |
| Battlefield Victory Harvest | Winning army battles awards +4 Vanguard XP (commander) or +3 Vanguard XP (knight), and grants a 33% chance to gain 1 Minor Lifeforce. |
| Battlefield Defeat Survival | Surviving an army defeat awards +1 Vanguard XP and +1 Enlightenment XP. |
| Tournament Completion / Victory | Completing or winning a tournament awards +3 Slaughter XP. |
| Annual Ambient Lifeforce Roll | Passive ~33% chance per year (`blood_mage_yearly_events.004`) to condense 1 Minor Lifeforce ambiently (+1 Enlightenment XP, +1 Ancient XP). Blood Mages do not receive ambient Lifeforce. |

### Interactions & Tracks

| Action | Description |
| --- | --- |
| Ask for Blood Magic (`ask_for_blood_magic_interaction`) | Requests elevation from a friendly, lover, or liege Blood Mage holding Superior Lifeforce (costs 250 Piety). |
| Steal Blood Magic from Prisoner (`bm_get_blood_magic_from_prisoner_interaction`) | Forcibly siphons blood magic from an imprisoned Blood Mage via duel to elevate oneself. |
| Vanguard Track (`vanguard`) | Exclusive track: army advantage (+1/tier), martial stat (+1 at even tiers), army speed (+2%/tier), pursuit (+3%/tier), martial per prestige rank at 50/100 XP. |
| Slaughter Track (`slaughter`) | Exclusive track: single combat prowess (+2/tier), knight effectiveness (+10%/tier), dread gain (+5%/tier), prowess per prestige rank at 50/100 XP. |

---

## Shared between both

### Decisions & Rituals

| Action | Description |
| --- | --- |
| Manifest Lifeforce (`bm_manifest_lifeforce_decision`) | Learning duel to manifest Lifeforce (+3 Enlightenment XP; yields Minor or Major Lifeforce; costs 100 Piety; 1-yr cooldown). |
| Cast Minor Blood Magic Hub (`bm_cast_blood_magic_minor_decision`) | Opens minor rites modal (requires Minor Lifeforce). |
| Cast Major Blood Magic Hub (`bm_cast_blood_magic_major_decision`) | Opens major rites modal (requires Major Lifeforce, Devotion level >= 1). |
| Repair Blóðtrú Reformation (`bm_repair_blodtru_reformation_decision`) | Clears broken temporal headship titles for unformed Blóðtrú faiths. |
| Channel Minor Lifeforce | Consumes Minor Lifeforce + 75 Piety for +1 Enlightenment XP and temporary stat boosts. |
| Attune Lifeforce | Consumes Minor Lifeforce + 25 Piety to align with a specific track for accelerated XP growth. |
| Condense Lifeforce | Forges 1 Minor Lifeforce + 100 Piety into 1 Major Lifeforce (+2 Ancient XP). |
| Purge Bodily Impurities | Consumes Minor Lifeforce + 50 Piety to remove wounds, scars, illnesses, lovers pox, gout, and negative congenital traits. |
| Blood Empowerment | Consumes Major Lifeforce + 150 Piety to unlock secondary lifestyle trait `lifestyle_blood_empowerment` (+3 Enlightenment XP). |
| Improve Education (1★ to 4★) | Mental duel consuming Major Lifeforce + scaled Piety to advance education tier up to 4★ (+5 Enlightenment XP; 2-yr cooldown). |
| Inscribe Minor Blood Rune | Consumes Major Lifeforce + Minor Lifeforce to inscribe personal minor rune modifier (+4 Ancient XP; 5-yr cooldown). |
| Inscribe Major Blood Rune | Consumes Major Lifeforce + Minor Lifeforce + 200 Piety to upgrade to major rune modifier (+5 Ancient XP; 5-yr cooldown). |
| Empower Bloodline | Consumes Major Lifeforce + 350 Piety to bestow house-wide stat buffs (+5 Bloodline XP for Mage; +5 Vanguard XP for Knight; 3-yr cooldown). |
| Manifest Perfection | Consumes Major Lifeforce + 200 Piety to manifest positive congenital traits (Beauty, Physique, Intellect) up to rank 3 (2-yr cooldown). |

### Interactions & Tracks

| Action | Description |
| --- | --- |
| Make Blood Knight (`make_blood_knight_interaction`) | Bestows `lifestyle_blood_knight` on sworn knight/courtier (Mage: 100 Piety + Major Lifeforce; Knight: 200 Prestige + Minor Lifeforce OR 0 Prestige + Major Lifeforce). |
| Heal Minor Ailments on Self (`bm_heal_ailment`) | Cleanses minor wounds or illnesses on oneself using Minor Lifeforce + 15 Piety (+2 Enlightenment XP). |
| Heal Major Ailments on Self (`bm_heal_ailment`) | Cleanses major ailments (weak, wounded_2, incapable) on oneself using Major Lifeforce + 35 Piety (+4 Enlightenment XP). |
| Heal Minor Ailments on Others (`bm_heal_ailment`) | Cleanses minor conditions on allies using Minor Lifeforce + 15 Piety (+2 Benediction XP for Mage; +1 Vanguard & +1 Benediction XP for Knight). |
| Non-Lethal Minor Prisoner Lifedrain (`lifedrain_courtier_event_interaction` on captives) | Siphons Minor Lifeforce from dungeon captives without execution (Mages test Intrigue/Learning; Knights test Prowess). |
| Captive Trait Theft (`trait_drain_prisoner_event_interaction` ranks 1–2) | Steals tier 1 or tier 2 congenital traits (Quick, Comely, Hale) from dungeon captives via skill duel. |
| Ancient Track (`ancient`) | Longevity, health penalty negations at 50/100 XP, lifestyle XP bonus (+5%/tier), dynasty prestige, age prowess lock at 100 XP. |
| Benediction Track (`benediction`) | Healing bonuses, positive opinion scaling, and monthly prestige. |
| Enlightenment Track (`enlightenment`) | Monthly piety (+0.2/tier), piety percentage gain (+5%/tier), learning scaling per devotion level at 50/100 XP, age prowess lock at 100 XP. |
| Blood Empowerment Tracks | All 5 empowerment tracks (`dynasty`, `mastery`, `presence`, `prosperity`, `shadows`) accessible to both Mages and Knights. |
