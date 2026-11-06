# Additional Lifestyles — Custom Tracks & Mechanic Ideas

> [!NOTE]
> Source: Steam Workshop Item `3433842378` (`Additional Lifestyles` for CK3 1.20).
> Extracted for inspiration on lifestyle tracks, perk progression, and character interactions.

---

## 1. Mod Architecture Overview

The mod expands the vanilla lifestyle system by adding a **4th thematic tree** and a **5th stat-mastery tree** to each of the 6 lifestyles (Diplomacy, Martial, Stewardship, Intrigue, Learning, Wanderer):

1. **4th Thematic Trees:** Complete with 7–9 unique perks, custom character interactions, decisions, casus bellis, and a capstone Lifestyle Trait.
2. **5th "Skill & Mastery" Trees:** 7-perk linear progression trees that grant incremental stat increases and lifestyle-themed resources (Renown, Dread, Gold, Clout/Influence, Wisdom/Piety, Travel Safety) culminating in the `Shrewd` or `Strong` congenital trait.

---

## 2. The 6 Thematic Lifestyle Trees

### A. Diplomacy Tree 4: Worldly (`gpt_wordly`)
*Theme: Multi-discipline journeying, activity mastery, cross-lifestyle hobby progression, and realm peace.*

* **Perks:**
  * **Travel Enthusiast (`gpt_diplomacy_perk_01`):** Unlocks the *Offer Tribute* interaction (pay gold to secure a temporary truce with a neighboring ruler).
  * **Hunt Enthusiast (`gpt_diplomacy_perk_02`):** `+2` Prowess, `+0.25` Health Penalty Negation, `+20%` Hunter, Falconer, and Bow track XP.
  * **Duel Enthusiast (`gpt_diplomacy_perk_03`):** `+2` Prowess, `+0.25` Health, `+20%` Foot, Horse, and Blademaster track XP.
  * **War Enthusiast (`gpt_diplomacy_perk_04`):** `+2` Martial, `+0.10` Winter Movement Speed, `+8` Winter Advantage, `+20%` Wit track XP.
  * **Religion Enthusiast (`gpt_diplomacy_perk_05`):** `+2` Learning, `-35%` Faith Conversion Piety Cost, `+20%` Pilgrim track XP.
  * **Scheme Enthusiast (`gpt_diplomacy_perk_06`):** `+2` Intrigue, `+10` Scheme Secrecy, `+10` Hostile Scheme Success, `+20%` Physician track XP.
  * **Heraldry Enthusiast (`gpt_diplomacy_perk_07`):** Unlocks the *Ennoblement* interaction (spend prestige/piety to elevate an unlanded lowborn courtier to noble status).
  * **Worldly (`gpt_diplomacy_perk_08`):** Grants the `gpt_wordly` lifestyle trait.
* **Capstone Trait (`gpt_wordly`):**
  * `+20%` Cultural Head Acceptance Gain Mult
  * `+10` Travel Companion Opinion
  * `+5` General Opinion

---

### B. Martial Tree 4: Homelander (`gpt_homelander`)
*Theme: Defensive warfare, home territory advantage, claimant intimidation, and mobilizing vassal levies.*

* **Perks:**
  * **Inspiring Speeches (`gpt_martial_perk_01`):** Unlocks the *Raise War Taxes* decision (temporarily raise tax extraction during wartime).
  * **Defensive Tactics (`gpt_martial_perk_02`):** Increases advantage in owned and capital provinces, defensive siege hold duration.
  * **Surprise Attacks (`gpt_martial_perk_03`):** Army movement speed and advantage bonuses when fighting defensive battles.
  * **Warden Contracts (`gpt_martial_perk_04`):** Enhances *Call Vassal to War* interaction (allows directly summoning powerful vassals as military allies in defensive wars).
  * **Fanatical Loyalists (`gpt_martial_perk_05`):** Unlocks the *Intimidate Claimant* interaction (force primary title claimants to renounce claims through martial/dread challenge).
  * **Archery Competitions (`gpt_martial_perk_06`):** Bow advantage and tournament archery skill boosts.
  * **Horseback Racings (`gpt_martial_perk_07`):** Cavalry combat advantage, travel speed, and tournament equestrian bonuses.
  * **Homelander (`gpt_martial_perk_08`):** Grants the `gpt_homelander` lifestyle trait.
* **Capstone Trait (`gpt_homelander`):**
  * `+2` Martial
  * `+2` Levy Attack & `+2` Levy Toughness
  * `+4` Controlled Province Advantage
  * `+10%` Army Maintenance Mult

---

### C. Stewardship Tree 4: Founder (`gpt_founder`)
*Theme: House dominance, succession security, designating heirs, art patronage, and barony management.*

* **Perks:**
  * **Religious Unity (`gpt_stewardship_perk_01`):** County faith conversion speed and clergy opinion bonuses.
  * **Cultural Unity (`gpt_stewardship_perk_02`):** County cultural acceptance and assimilation speed.
  * **Traditional Ways (`gpt_stewardship_perk_03`):** Unlocks the *Secure Succession* interaction (persuade powerful vassals to pledge early fealty to your designated heir).
  * **House Barons (`gpt_stewardship_perk_04`):** Increased tax and levy contributions from barony holders belonging to your house.
  * **Art Patronage (`gpt_stewardship_perk_05`):** Increases court grandeur baseline, artifact durability, and inspirational artisan quality.
  * **Charitable Relief (`gpt_stewardship_perk_06`):** Decreases peasant unrest, increases popular opinion and county development growth.
  * **Dynasty Privileges (`gpt_stewardship_perk_07`):** Unlocks the *Designate Heir* interaction (freely nominate and switch your primary realm heir without absolute crown authority).
  * **Founder (`gpt_stewardship_perk_08`):** Grants the `gpt_founder` lifestyle trait.
* **Capstone Trait (`gpt_founder`):**
  * `+2` Stewardship
  * `+10` Dynasty Opinion
  * `+1.0` Monthly Dynasty Prestige (Renown)

---

### D. Intrigue Tree 4: Deceiver (`gpt_deceiver`)
*Theme: Propaganda, slandering enemies, embezzling treasuries, and counterfeiting piety/prestige.*

* **Perks:**
  * **Natural Liar (`gpt_intrigue_perk_01`):** Boosts scheme secrecy and softens opinion penalties when secrets are exposed.
  * **Storyteller (`gpt_intrigue_perk_02`):** Accelerates rumor spreading and personal smear effectiveness.
  * **Mischief-Maker (`gpt_intrigue_perk_03`):** Unlocks the *Spread Lies* interaction (launch a smear campaign targeting an enemy ruler's prestige and legitimacy).
  * **Forgery of Iconography (`gpt_intrigue_perk_04`):** `+3.0` Monthly Piety, but `-10` Clergy and Zealot Opinion.
  * **Forgery of Heraldry (`gpt_intrigue_perk_05`):** `+3.0` Monthly Prestige, but `-10` Independent Ruler and Courtly Opinion.
  * **Master of Plots (`gpt_intrigue_perk_06`):** Unlocks the *Embezzle* interaction (siphon gold directly from realm treasuries or vassal accounts).
  * **Counterfeiter (`gpt_intrigue_perk_07`):** `+2.0` Monthly Gold income, but `-30` Liege Opinion and `-10` Parochial Opinion.
  * **Deceiver (`gpt_intrigue_perk_08`):** Grants the `gpt_deceiver` lifestyle trait.
* **Capstone Trait (`gpt_deceiver`):**
  * `-10%` Tyranny Gain Mult
  * `+1` Intrigue per Level of Fame / Prestige Level
  * `+1` Intrigue per Level of Devotion / Piety Level

---

### E. Learning Tree 4: Cosmopolitan (`gpt_cosmopolitan`)
*Theme: Republican governance, elective succession, classical knowledge, and urban development.*

* **Perks:**
  * **Republican Bias (`gpt_learning_perk_01`):** Unlocks the *Basic Elections* decision (voluntarily adopt elective laws in feudal/clan realms).
  * **Religious Tolerance (`gpt_learning_perk_02`):** Reduces different-faith opinion penalties and increases interfaith marriage acceptance.
  * **Cultural Tolerance (`gpt_learning_perk_03`):** Accelerates cultural acceptance gain and softens different-culture popular opinion penalties.
  * **Practical Syncretism (`gpt_learning_perk_04`):** Lowers faith reformation and tradition divergence costs.
  * **Welcoming Exiles (`gpt_learning_perk_05`):** High-stat foreign wanderers and deposed characters regularly arrive at your court.
  * **Visit Metropolis (`gpt_learning_perk_06`):** Unlocks advanced *Special Elections* decisions.
  * **Applied Classical History (`gpt_learning_perk_07`):** Unlocks the *Visit Metropolis* interaction (travel to ancient capitals for innovation boosts and learning XP).
  * **Cosmopolitan (`gpt_learning_perk_08`):** Grants the `gpt_cosmopolitan` lifestyle trait.
* **Capstone Trait (`gpt_cosmopolitan`):**
  * `+40%` Republic Government Tax Contribution Mult
  * `-40%` City Holding Build Gold Cost
  * `+5%` Domain Tax Mult

---

### F. Wanderer Tree 4: Scoundrel (`gpt_scoundrel`)
*Theme: Ruthless villainy, prisoner exploitation, slave thralls, hostage raiding, and dread warlord.*

* **Perks:**
  * **Twisted Morality (`gpt_wanderer_perk_01`):** Unlocks the *Brand Criminal* interaction (manufacture criminal charges against subjects via intrigue challenge).
  * **Evil Intentions (`gpt_wanderer_perk_02`):** Increases dread gain and reduces tyranny decay.
  * **Vicious Company (`gpt_wanderer_perk_03`):** `+4` Prowess, `+4` Martial, `+4` Intrigue, but `-2` Diplomacy, `-2` Learning.
  * **Unbound Hedonism (`gpt_wanderer_perk_04`):** Unlocks the *Defile* interaction (forcible impregnation interaction on prisoners of opposite gender).
  * **Onslaught (`gpt_wanderer_perk_05`):** `+40%` Enemy Hard Casualty Modifier, `+5` Commander Advantage.
  * **Terror Tactics (`gpt_wanderer_perk_06`):** `+25%` Siege Morale Loss, `+10%` Army Siege Value, `+10` Dread Baseline.
  * **Enthraller (`gpt_wanderer_perk_07`):** Unlocks the *Break* interaction (permanently break a prisoner's personality into an obedient slave/courtier).
  * **Cult Leader (`gpt_wanderer_perk_08`):** Unlocks the *Raid for Captives* Casus Belli, `+1` Max Murder Schemes, `+20` Scheme Secrecy.
  * **Scoundrel (`gpt_wanderer_perk_09`):** Grants the `gpt_scoundrel` lifestyle trait.
* **Capstone Trait (`gpt_scoundrel`):**
  * `+2%` Knight Effectiveness per point of Tyranny
  * `+1%` Knight Effectiveness per point of Dread
  * `+0.5%` Monthly Prestige Gain per point of Dread
  * `-10` General Opinion, `+25` AI Boldness, `-25` AI Compassion

---

## 3. The 5th "Stat & Skill Mastery" Trees

Each lifestyle includes a linear 7-perk progression tree providing incremental core stats and lifestyle resources, ending with a congenital trait:

| Lifestyle | Tree Name | Progression Steps (Perks 1–6) | Capstone Perk (Perk 7) |
| :--- | :--- | :--- | :--- |
| **Diplomacy** | `gpt_dip_skill` (Renown) | `+1` Diplomacy & `+0.5`–`0.75` Monthly Prestige per perk | `Shrewd` trait |
| **Martial** | `gpt_mar_skill` (Dread) | `+1` Martial & `+5` Dread Baseline per perk | `Shrewd` trait |
| **Stewardship** | `gpt_stw_skill` (Barter) | `+1` Stewardship & `+0.25`–`0.5` Monthly Gold per perk | `Shrewd` trait |
| **Intrigue** | `gpt_int_skill` (Clout) | `+1` Intrigue & `+0.5` Monthly Dynasty Prestige / Influence per perk | `Shrewd` trait |
| **Learning** | `gpt_ler_skill` (Wisdom) | `+1` Learning & `+0.5` Monthly Piety per perk | `Shrewd` trait |
| **Wanderer** | `gpt_wan_skill` (Survival) | `+1` Prowess & `+5` Travel Safety per perk | `Strong` trait |

---

## 4. Key Takeaways & Ideas for Blood Mages

### Ideas for Blood Mage Character Interactions
* **Intimidate / Enthrall (from Homelander & Scoundrel):**
  * Blood Mages could use Lifeforce to intimidate claimants into renouncing claims, or mind-break prisoners into obedient thralls.
* **Offer Blood / Siphon (from Worldly & Deceiver):**
  * Diplomatic blood pacts (offering enchanted blood to secure non-aggression truces) or embezzling Lifeforce from vassals.
