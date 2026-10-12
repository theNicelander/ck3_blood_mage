# Blood Mage vs Blood Knight Comparison

Living technical specification comparing actions and capabilities available to Blood Mages (`lifestyle_blood_mage`) and Blood Knights (`lifestyle_blood_knight`).

## Specific to Blood mages

### Decisions & Hubs
- **Cast Superior Blood Magic Hub (`bm_cast_blood_magic_superior_decision`):** Opens superior rites modal; requires `lifestyle_blood_mage`, Superior Lifeforce, and Devotion level >= 2.
- **Manifest Superior Lifeforce (`bm_manifest_superior_lifeforce_decision`):** Distills 1 Minor + 1 Major Lifeforce into Superior Lifeforce via Learning duel (costs 250 Piety, requires Devotion level >= 3).
- **Create Blood Golem (`blood_golem_creation_decision`):** Standalone decision to forge a synthetic courtier in cadet house `bm_house_golem` (costs 500 Piety + Superior Lifeforce; 3-year cooldown).
- **Mass Lifedrain Prisoners (`mass_lifedrain_prisoners_decision`):** Mass sacrifice decision executing dungeon captives to harvest Lifeforce and Hematurgy XP.

### Superior Rituals (within Superior Hub)
- **Master Education (5★):** Upgrades a 4★ education trait to legendary 5★ tier via mental duel (costs scaled Piety + Superior Lifeforce; 2-year cooldown).
- **Embrace New Education:** Grants a secondary 1-star education trait (costs 1000 Piety + Superior Lifeforce; 2-year cooldown).
- **Inscribe Superior Blood Rune:** Inscribes tier 3 blood rune (+10 Ancient XP; costs Superior Lifeforce; 5-year cooldown).
- **Manifest Transcendent Perfection:** Manifests congenital traits at ranks 4 and 5 (+6 Bloodline XP, +2 Enlightenment XP; costs Superior Lifeforce; 3-year cooldown).
- **Forge Blood Golem:** In-hub rite to craft and shape a blood golem (+5 Bloodline XP; costs Superior Lifeforce).

### Targeted Character Interactions
- **Grant Blood Magic (`grant_blood_magic_interaction`):** Bestows `lifestyle_blood_mage` on uninitiated courtier/kin or elevates a Blood Knight (costs Superior Lifeforce; grants +4–5 Bloodline XP).
- **Lethal Major Lifedrain (`lifedrain_prisoner_event_interaction`):** Executes dungeon captive for Major Lifeforce and +1 Hematurgy XP (`death_lifedrain_reason`).
- **Grant Lifeforce (`grant_lifeforce_interaction`):** Bestows Minor or Major Lifeforce modifier onto a courtier or prisoner.
- **Restore Drained Courtier (`grant_lifeforce_interaction_reversed`):** Removes `lifedrained_modifier` debuff, grants Minor Lifeforce, opinion bonus, and +4 Benediction XP (costs 25 Piety + Major Lifeforce).
- **Cast Blood Curse (`bm_curse_blood_interaction`):** Remote hostile curse via Intrigue/Learning duel, inflicting `bm_blood_curse_modifier` (-2 all stats, -1.5 health, -30% fertility, -3 prowess) for 5 years (costs 50 Piety + Minor Lifeforce; requires >= 10 Hematurgy XP).
- **Heal Deadly Ailments (`bm_heal_ailment`):** Cures fatal conditions (e.g. bubonic plague, cancer, consumption) on self and others (costs 100 Piety + Superior Lifeforce; +8 Benediction XP).

### Exclusive Trait Tracks
- **Bloodline (`bloodline`):** Domain limit (+1 at 30/60/90 XP), gold income (+10% at 30/60/90 XP), construction cost/speed, development growth, stewardship per prestige level, and dynasty prestige.
- **Hematurgy (`hematurgy`):** Hostile scheme slots (+1 at 50/100 XP), hostile scheme speed/success, natural dread baseline, dread gain, and monthly tyranny decay.

---

## Specific to Knights

### Combat & Battlefield Harvesting
- **Single Combat Duel Fatality:** Killing an opponent in single combat awards +5 `slaughter` XP and immediately grants 1 Minor Lifeforce.
- **Battlefield Victory:** Winning a battle as army commander awards +4 `vanguard` XP (or +3 as knight) and grants a 33% chance to gain 1 Minor Lifeforce.
- **Battlefield Defeat Survival:** Surviving an army defeat awards +1 `vanguard` XP and +1 `enlightenment` XP.
- **Tournament Completion / Victory:** Participating in or winning tournaments awards +3 `slaughter` XP.

### Passive Vitality Generation
- **Annual Ambient Lifeforce Roll:** Passive ~33% chance per year (`blood_mage_yearly_events.004`) to condense 1 Minor Lifeforce ambiently (+1 Enlightenment XP, +1 Ancient XP). Blood Mages do not receive ambient Lifeforce.

### Decisions & Wilderness Exploration
- **Elevate to Blood Mage (`bm_elevate_to_blood_mage_decision`):** Ritual decision attempting full ascension into `lifestyle_blood_mage` via Learning or Prowess trial (requires Learning > 30, piety rank 3, Minor or Major Lifeforce; costs 500 Piety). Carries over Ancient, Benediction, and Enlightenment XP 1:1, and converts 50% Vanguard -> Bloodline and Slaughter -> Hematurgy.

### Targeted Character Interactions
- **Empower Blood Knight (`empower_blood_knight_interaction`):** Directly boosts sworn Blood Knight's martial tracks (+10 XP with Major Lifeforce, +5 XP with Minor Lifeforce; grants +4 or +2 Benediction XP to caster).
- **Ask for Blood Magic (`ask_for_blood_magic_interaction`):** Requests elevation from a friendly, lover, or liege Blood Mage holding Superior Lifeforce (costs 250 Piety).
- **Steal Blood Magic from Prisoner (`bm_get_blood_magic_from_prisoner_interaction`):** Forcibly siphons blood magic from an imprisoned Blood Mage via duel to elevate oneself.

### Exclusive Trait Tracks
- **Vanguard (`vanguard`):** Army command advantage (+1/tier), martial stat (+1 at even tiers), army movement speed (+2%/tier), pursuit (+3%/tier), and martial per prestige level at 50/100 XP.
- **Slaughter (`slaughter`):** Single combat prowess (+2/tier), knight effectiveness (+10%/tier), dread gain (+5%/tier), and prowess per prestige level at 50/100 XP.

---

## Shared between both

### Decisions & Core Hubs
- **Seek Power in Nature's Domain (`seek_power_decision`):** Wilderness expedition harvesting Lifeforce and school XP (2-year cooldown landed, 1-year unlanded/wanderer).
- **Become Blood Cultist (`become_blood_cultist_decision`):** Religious decision converting ruler and realm to Blóðtrú faith branch (costs 250 Piety + 1 Major Lifeforce; 10-year cooldown).
- **Manifest Lifeforce (`bm_manifest_lifeforce_decision`):** Learning duel to stoke inner blood, granting +3 Enlightenment XP and yielding Minor Lifeforce (or Major Lifeforce on critical success; costs 100 Piety; 1-year cooldown).
- **Cast Minor Blood Magic Hub (`bm_cast_blood_magic_minor_decision`):** Opens minor blood magic rites selection modal (requires Minor Lifeforce).
- **Cast Major Blood Magic Hub (`bm_cast_blood_magic_major_decision`):** Opens major blood magic rites selection modal (requires Major Lifeforce and Devotion level >= 1).
- **Repair Blóðtrú Reformation (`bm_repair_blodtru_reformation_decision`):** Clears broken temporal headship titles for unformed Blóðtrú faiths.

### Minor Rituals (within Minor Hub)
- **Channel Minor Lifeforce:** Consumes Minor Lifeforce + 75 Piety to gain +1 Enlightenment XP and temporary stat boosts.
- **Attune Lifeforce:** Consumes Minor Lifeforce + 25 Piety to align with a specific trait track for accelerated growth.
- **Condense Lifeforce:** Forges 1 Minor Lifeforce + 100 Piety into 1 Major Lifeforce (+2 Ancient XP).
- **Purge Bodily Impurities:** Consumes Minor Lifeforce + 50 Piety to remove minor wounds, scars, illness, lovers pox, gout, and negative physical/intellectual/beauty traits.

### Major Rituals (within Major Hub)
- **Blood Empowerment:** Consumes Major Lifeforce + 150 Piety to unlock the secondary lifestyle trait `lifestyle_blood_empowerment` (+3 Enlightenment XP).
- **Improve Education (Tiers 1★ to 4★):** Mental duel consuming Major Lifeforce + scaled Piety to advance education tier up to 4★ (+5 Enlightenment XP; 2-year cooldown).
- **Inscribe Minor Blood Rune:** Consumes Major Lifeforce + Minor Lifeforce to inscribe personal minor blood rune modifier (+4 Ancient XP; 5-year cooldown).
- **Inscribe Major Blood Rune:** Consumes Major Lifeforce + Minor Lifeforce + 200 Piety to upgrade to major blood rune modifier (+5 Ancient XP; 5-year cooldown).
- **Empower Bloodline:** Consumes Major Lifeforce + 350 Piety to bestow dynasty-wide stat buffs (+5 Bloodline XP for Mage; +5 Vanguard XP for Knight; 3-year cooldown).
- **Manifest Perfection:** Consumes Major Lifeforce + 200 Piety to manifest positive congenital traits (Beauty, Physique, Intellect) up to rank 3 (2-year cooldown).

### Targeted Character Interactions
- **Make Blood Knight (`make_blood_knight_interaction`):** Bestows `lifestyle_blood_knight` onto an uninitiated sworn knight or courtier.
  - *Mage cost:* 100 Piety + Major Lifeforce (+4 Benediction XP).
  - *Knight cost:* 200 Prestige + Minor Lifeforce (+2 Vanguard XP) OR 0 Prestige + Major Lifeforce (+4 Vanguard XP).
- **Bless Bloodline (`bm_bless_bloodline_interaction`):** Grants `bm_blessed_blood_modifier` (+1 all stats, +10% fertility, +0.25 health) to child or dynasty kin for 10 years (costs 35 Piety + Minor Lifeforce; +2 Bloodline XP for Mage, +2 Vanguard XP for Knight).
- **Drain Courtier or Prisoner (`lifedrain_courtier_event_interaction`):** Siphons Minor Lifeforce from free courtier or prisoner, inflicting `lifedrained_modifier` debuff (Mages test Intrigue/Learning for +1 Hematurgy XP; Knights test Prowess for +1 Slaughter XP; 3-month cooldown).
- **High-Tier Trait Theft (`trait_drain_prisoner_event_interaction` ranks 1–5):** Steals congenital traits up to rank 5 (Genius, Beautiful, Herculean) from captive mortals via skill duel (Mages and Knights; 60-day cooldown).
- **Heal Minor Ailments on Self (`bm_heal_ailment`):** Cleanses minor wounds or illnesses on oneself using Minor Lifeforce + 15 Piety (+2 Enlightenment XP).
- **Heal Major Ailments on Self (`bm_heal_ailment`):** Cleanses major conditions (e.g. `weak`, `wounded_2`, `incapable`) on oneself using Major Lifeforce + 35 Piety (+4 Enlightenment XP).
- **Heal Minor Ailments on Others (`bm_heal_ailment`):** Cleanses minor conditions on courtiers, family, spouse, liege, or knights using Minor Lifeforce + 15 Piety (+2 Benediction XP for Mage; +1 Vanguard & +1 Benediction XP for Knight).
- **Heal Major Ailments on Others (`bm_heal_ailment`):** Cleanses major conditions (e.g. `blind`, `incapable`, `infirm`, `wounded_2`) on courtiers, family, spouse, liege, or knights using Major Lifeforce + 35 Piety (+4 Benediction XP for Mage; +2 Vanguard & +2 Benediction XP for Knight).

### Shared Trait Tracks & Empowerment
- **Ancient (`ancient`):** Longevity, health penalty negations at 50/100 XP, lifestyle XP bonus (+5%/tier), dynasty prestige, and prowess preservation past age 45 at 100 XP.
- **Benediction (`benediction`):** Healing ailment bonuses, positive opinion scaling, and monthly prestige.
- **Enlightenment (`enlightenment`):** Monthly piety (+0.2/tier), piety percentage gain (+5%/tier), learning scaling per devotion level at 50/100 XP, and prowess preservation past age 45 at 100 XP.
- **Blood Empowerment Trait (`lifestyle_blood_empowerment`):** All 5 empowerment tracks (`dynasty`, `mastery`, `presence`, `prosperity`, `shadows`) are fully accessible to both Mages and Knights.
