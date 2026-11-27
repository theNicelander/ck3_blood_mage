# common/artifacts/ - Blood Mages

- **Zero vanilla overwrites**: define only `bm_`-prefixed templates in `common/artifacts/templates/`.
- **Blood Mage gating**: use `bm_blood_artifact_template` (`can_equip = { always = yes }`, `can_benefit = { is_blood_mage_any_tier_trigger = yes }`, `fallback = { monthly_prestige = 0.1 }`).
- **Verified inventory `type` + `visuals` pairs** (no missing feature-gen errors):
  - Weapon: `type = sword`, `visuals = sword`
  - Regalia: `type = regalia_simple`, `visuals = regalia`
  - Armor: `type = armor_plate`, `visuals = armor`
  - Crown: `type = helmet_simple`, `visuals = crown`
  - Trinket: `type = miscellaneous`, `visuals = ring`
- **In-place upgrades**: inside artifact scope, use `set_artifact_rarity = masterwork|famed|illustrious`, `add_artifact_modifier = <key>`, and `set_variable` to track forged/tempered state.
- **Modifiers**: all artifact modifier keys must pass `scripts/check_modifiers.py` (`character` allowlist).
