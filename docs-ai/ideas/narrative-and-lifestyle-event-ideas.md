# Ideas: Narrative & Lifestyle Events

Living brainstorm document outlining narrative event chains, yearly pulse events, and character flavor events for the Blood Mages mod. Inspired by vanilla CK3 lifestyle, court, activity, and stress events while remaining integrated into mod systems (Lifeforce, Bloodline, Golems, and trait tracks).

---

## 1. "The Whispering Fountain" (Court & Lifestyle Pulse Event)

- **Vanilla Inspiration:** Learning lifestyle events (*Strange Flora*, *The Celestial Sphere*, *Wandering Mystic*) and court intrigue/weirdness pulses (*Strange Odors*, *Cat in the Court*).
- **Narrative Hook:** Courtiers and servants notice bizarre occurrences around the ruler's private sanctum—wine left out coagulates into dark viscous residue, or palace birds drop from the parapets drained dry without puncture marks. Whispers of sorcery spread through the halls.
- **CK3 Systems & Hooks:**
  - **Trigger:** Yearly pulse or court pulse for characters with `has_trait = lifestyle_blood_mage`.
  - **Option A (*Cover it up / Hematurgy*):** Spend minor Lifeforce / perform a cleansing ritual (intrigue + hematurgy check). Keeps it hidden, gains Hematurgy XP, but adds stress.
  - **Option B (*Harness the phenomenon / Enlightenment*):** Study the ambient resonance. Grants Learning lifestyle XP and Enlightenment track XP, but rolls a secret: courtier uncovers your occult practices.
  - **Option C (*Frame a rival / Intrigue*):** Direct suspicion toward a pious or troublesome vassal/rival courtier (`add_courtier_opinion` hit, gain a hook, or imprison them on fabricated charges).

---

## 2. "The Price of Perfection" (Family & Ward Education Event)

- **Vanilla Inspiration:** Ward education pulses (*Child studying late*, *Child exhibits unnatural cruelty / genius*, *Meet Peers*).
- **Narrative Hook:** Watching your young child or ward struggle with martial drills, illness, or complex scholarship, you feel the instinctual hum of Lifeforce in your veins. You could secretly weave your vitality into their marrow—or force their awakening.
- **CK3 Systems & Hooks:**
  - **Trigger:** Education pulse when ward has a blood mage guardian, or guardian is landed blood mage with child courtier.
  - **Option A (*Infuse them / Benediction*):** Consume a Minor Lifeforce modifier to grant the ward a positive modifier (`bm_blood_blessed_child`: health & stat growth boost, higher chance of positive congenital or education outcomes upon reaching adulthood).
  - **Option B (*Force their awakening / Bloodline*):** An intense, painful ritual requiring high Bloodline track XP. Success awards the child `lifestyle_blood_mage` early; failure inflicts illness or a rival relationship with the child.
  - **Option C (*Restrain yourself*):** Suffer stress (if ambitious/zealous) or lose stress (if compassionate), gaining normal prestige/piety.

---

## 3. "The Vessel's Remorse" (Post-Drain / Prisoner Narrative Event)

- **Vanilla Inspiration:** Dread / Cannibal / Guilt events (haunting visions after executions, *The Tell-Tale Heart* style stress events, ghosts of victims mocking the ruler).
- **Narrative Hook:** Days after harvesting a noble captive or traveler via *Mass Lifedrain* or *Trait Drain*, the stolen soul refuses to settle quietly. You catch their reflection staring back at you from a scrying bowl, or their cadence slipping into your speech when angry.
- **CK3 Systems & Hooks:**
  - **Trigger:** On-action delayed event after running `bm_mass_lifedrain` or `trait_drain_prisoner_event_interaction`.
  - **Option A (*Subjugate their will / Ancient*):** Prowess or Learning duel against the deceased's lingering psychic imprint. Success converts the turbulence into permanent dread and Ancient XP; failure inflicts the `haunted` or `stressed_1` trait.
  - **Option B (*Exorcising purification / Benediction*):** Expend gold or piety to quiet the soul, trading raw essence for tranquility and piety.
  - **Option C (*Embrace the madness*):** Gain a temporary combat / intrigue buff representing erratic, wild ferocity, at the cost of opinion penalties with close family.

---

## 4. "The False Blood" (Activity / Travel / Feast Event)

- **Vanilla Inspiration:** Travel danger events (*Mysterious Hermit*, *Bandits*, *Haggling merchant*) and feast intrigue (*Poison in the cup*, *Challenging a toast*).
- **Narrative Hook:** During a royal feast or pilgrimage/travel route, a wandering occultist or shadowy apothecary approaches offering an amphora of "preserved ancestral ichor" purportedly excavated from a catacomb or battleground.
- **CK3 Systems & Hooks:**
  - **Trigger:** Travel event hook or Feast activity pulse (`common/activities/`).
  - **Option A (*Taste and analyze / Learning & Hematurgy check*):**
    - *Success:* Recognize an authentic ancient draught; grants a Major Lifeforce modifier or an occult relic.
    - *Failure:* Tainted foul swill; character suffers illness or food poisoning.
  - **Option B (*Drain the charlatan on the spot*):** Seize them for audacity. Execute or imprison them immediately; chance of harvesting Lifeforce if they possess hidden occult talent.
  - **Option C (*Subsume their craft into the realm*):** Recruit them as a court physician or antiquarian with an occult aptitude trait.

---

## 5. "Blood Oath of the Golem" (Golem Subsystem Event)

- **Vanilla Inspiration:** Court artifact creation events, court weapon master pulses, and royal pet/champion bonding events (hound defending the lord, sworn bodyguard oaths).
- **Narrative Hook:** A created Blood Golem standing silent vigil in your solar begins demonstrating eerie mannerisms reminiscent of the donor whose life was expended to shape it—reaching protectively toward your heir, or glaring menacingly at your spymaster.
- **CK3 Systems & Hooks:**
  - **Trigger:** Pulse event for landed rulers who have active golem characters/modifiers in court.
  - **Option A (*Attune it as a dedicated House Guardian*):** Tie its essence directly to the Dynasty Head. The Golem gains a permanent modifier granting personal scheme defense and guardian prowess for your lineage.
  - **Option B (*Recalibrate the construct / Hematurgy*):** Erase all traces of lingering ego to ensure pure, unthinking obedience. Grants dread and eliminates berserk risk, but consumes minor Lifeforce.
  - **Option C (*Investigate who it remembers*):** Uncovers a secret plot or past conspiracy that the deceased donor was involved in before their demise.
