---
trigger: model_decision
description: CK3 1.21 districts, duchy capital building slots, district_level_requirement, and sharing vanilla sub-buildings safely.
---

# CK3 1.21 Districts & Buildings

- **District-first slots**: Holdings place districts (`common/districts/`), not bare buildings (`type = regular|special|duchy_capital|holding|great_district|trade_post|entrepot`). Never put `type = duchy_capital` directly on building definitions.
- **Sub-building slots**: Unlocked by `building_slots_for_host_district = N` in the primary building's `province_modifier` (vanilla duchy primaries: 4 tiers granting `1→2→3→4` slots + `province_size_baseline_add = 10/30/50/80`). Omitting `buildings = { ... }` + slot modifier yields a valid single-building district.
- **Sub-building tier gating**: Use generic `district_level_requirement = 2..4` on Tiers II–IV (not hard-coded primary building checks).
- **Sharing vanilla sub-buildings trap**: Before adding vanilla sub-buildings to a custom district's `buildings = { ... }`, inspect Tier 2+ in vanilla `00_duchy_capital_buildings.txt` and `01_duchy_office_buildings.txt`:
  - **Safe (generic `district_level_requirement`)**: `endowment_district`, `military_duchy_capital_district`, `ducal_residence_district`, `bailiwick_district` sub-buildings (`consistory_01`, `almonry_general_01`, `pilgrimage_office_01`, `burial_site_01`, `charnel_grounds_01`, `great_megalith_01`, `tower_of_silence_01`, `military_academy_01`, `leisure_palace_01`, `royal_forest_01`, `royal_garden_01`, `ducal_chase_01`, `reckoning_school_01`, `examination_hall_01`, etc.).
  - **Unsafe (hard-locked to vanilla primaries on T2+)**: `dragon_kiln_01`, `staple_court_01`, `court_of_the_towns_01`, `alnagers_office_01`, `admiralty_court_01`, `grain_exchange_01`, `town_liberties_court_01` (`has_building_or_higher = staple_district_02` / `governance_district_02`).
- **Modifier allowlist**: `building_slots_for_host_district`, `province_size_baseline_add`, and `epidemic_resistance` belong in `modifiers_county_allowlist.json` (`--scope county`).
