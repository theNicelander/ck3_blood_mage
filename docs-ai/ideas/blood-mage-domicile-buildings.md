# Ideas: Blood Mage & Blóðtrú Domicile Buildings

Living proposal for adding custom domicile buildings tailored specifically for **Adventurer Camps** (`camp`) and **Noble Estates** (`estate`) belonging to Blood Mages or followers of the Blóðtrú religion.

Introduced in CK3 1.20 (Roads to Power), the domicile system allows unlanded adventurers and administrative noble families to upgrade their permanent base of operations.

---

## 1. Engine & Implementation Foundation

### Gating Logic
Domicile buildings support the `can_construct_potential` trigger, ensuring these structures **only appear in the UI** for qualifying characters:

```pdx
can_construct_potential = {
    OR = {
        has_trait = lifestyle_blood_mage
        faith = { religion = religion:bm_blodtru_religion }
    }
}
```

### File Layout
- `common/domiciles/buildings/bm_domicile_buildings.txt` (defines the buildings, tiers, costs, modifiers)
- `localization/english/bm_domicile_buildings_l_english.yml` (names and lore descriptions)
- Graphical assets can reuse existing vanilla tent/estate DDS icons and intersection masks.

---

## 2. Adventurer Camp: Primary Building Line

### `bm_camp_sanguine_crucible` (The Sanguine Crucible / Field Altar)
A dedicated 4-tier external building line constructed in camp external slots.

| Tier | Building Key | Cost & Construction | Modifiers & Effects | Special Flavor / Parameters |
| :--- | :--- | :--- | :--- | :--- |
| **I** | `bm_camp_crucible_01`<br>*(Hemomantic Brazier)* | 75 Gold<br>180 Days | `monthly_piety = 0.2`<br>`provisions_gain_mult = 0.05` | Grants 1 internal slot.<br>Camp glows with low crimson embers. |
| **II** | `bm_camp_crucible_02`<br>*(Alchemical Distillation Vat)* | 150 Gold<br>240 Days | `health = 0.2`<br>`character_travel_safety = 5`<br>`stress_loss_mult = 0.1` | Infuses camp rations and remedies with lifeforce extracts. |
| **III** | `bm_camp_crucible_03`<br>*(The Sanguine Well)* | 300 Gold<br>360 Days | `provisions_capacity_add = 150`<br>`knight_effectiveness_mult = 0.10`<br>`monthly_lifestyle_xp_gain_mult = 0.05` | Grants 2 additional internal slots.<br>Empowers Crimson Warriors in camp. |
| **IV** | `bm_camp_crucible_04`<br>*(Monolith of the Crimson God)* | 500 Gold<br>480 Days | `dread_baseline_add = 15`<br>`character_travel_speed_mult = 0.10`<br>`monthly_dynasty_prestige_mult = 0.05` | Custom parameter: unlocks special camp decisions/interactions or buffs harvest yields. |

---

## 3. Adventurer Camp: Internal Specialist Modules

Specialist modules installed into internal slots inside standard camp tents (e.g. Barber Tent, Supply Tent, Baggage Train).

### 1. `bm_camp_embalming_slab` (Vessel Embalming Station)
- **Slot Type**: Internal slot of `barber_tent`
- **Requires**: Blood Mage trait or Blóðtrú faith
- **Modifiers**:
  - `wound_recovery_mult = 0.20` (+20% wound healing speed)
  - `character_travel_safety = 4`
  - `disease_resistance = 0.15`
- **Lore**: A morbid surgical setup where wounded followers and knights are stabilized using coagulating blood sorcery.

### 2. `bm_camp_blood_rations` (Sanguine Rations & Preserves)
- **Slot Type**: Internal slot of `supply_tent`
- **Requires**: Blood Mage trait or Blóðtrú faith
- **Modifiers**:
  - `provisions_loss_mult = -0.10` (-10% provision consumption rate)
  - `supply_capacity_mult = 0.25`
  - `travel_attrition_reduction_mult = 0.05`
- **Lore**: Rations cured and enchanted with dark vitae, sustaining travelers far longer than standard grain and salted meat.

### 3. `bm_camp_runed_armory` (Blood-Etched Forge)
- **Slot Type**: Internal slot of `baggage_train` or `camp_training_grounds`
- **Requires**: Blood Mage trait or Blóðtrú faith
- **Modifiers**:
  - `maa_damage_mult = 0.06`
  - `maa_toughness_mult = 0.06`
  - `knight_effectiveness_mult = 0.08`
- **Lore**: Weapons and armor inscribed with sanguine runes, granting supernatural cutting power to camp warriors.

### 4. `bm_camp_shrine_ancestors` (Shrine of the First Progenitor)
- **Slot Type**: Internal slot of `camp_main` or `bm_camp_sanguine_crucible`
- **Requires**: Blóðtrú faith
- **Modifiers**:
  - `monthly_piety = 0.5`
  - `same_faith_opinion = 5`
  - `clergy_opinion = 5`
- **Lore**: A traveling reliquary containing the sacred blood of Blóðtrú saints and ancient mages.

---

## 4. Noble Family Estate Buildings (Administrative / Landed Domiciles)

For blood mages ruling within an Administrative Empire (or holding a Family Estate domicile):

### 1. `bm_estate_sanguis_scriptorium` (The Sanguis Scriptorium)
- **Allowed Types**: `estate`
- **Slot Type**: External slot
- **Modifiers**:
  - `development_growth = 0.05`
  - `owned_scheme_secrecy_add = 10`
  - `hostile_scheme_resistance_add = 6`
  - `monthly_lifestyle_xp_gain_mult = 0.05`
- **Lore**: A secluded occult library beneath the estate where grimoires of blood magic and ancestral genealogical records are studied.

### 2. `bm_estate_crypt_dynasty` (Crypt of the Crimson Dynasty)
- **Allowed Types**: `estate`
- **Slot Type**: External slot
- **Modifiers**:
  - `positive_random_genetic_chance = 0.06`
  - `positive_inactive_inheritance_chance = 0.06`
  - `dynasty_opinion = 5`
  - `monthly_dynasty_prestige_mult = 0.05`
- **Lore**: The mummified remains of ancient bloodline forebears rest in chambers lined with runic inscriptions, reinforcing the potency of their heirs' blood.

---

## 5. Summary of Benefits & Gameplay Impact

1. **True Adventurer Viability**: Gives unlanded blood mages a tangible way to invest their gold into occult power without needing to hold baronies or counties.
2. **Camp Self-Sufficiency**: Provides travel safety, provision endurance, and high-tier medical care on the road.
3. **Thematic Identity**: Visually and mechanically distinguishes a blood mage mercenary company or wandering occultist band from ordinary adventurers.
