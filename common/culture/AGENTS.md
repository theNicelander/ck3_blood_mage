# Culture & Traditions (`common/culture/`)

Refs: `bm_icelandic.txt`, `bm_culture_traditions.txt`. Spec: `docs-ai/architecture/blood-mage-culture.md`.

- **Trade `sell_price_mult` scale (CK3 1.21)**: multiplies gross sale price; vanilla traditions use `0.0075`–`0.03` (fish/iron/horses `0.02`, max `0.03` rice/beer; Tier 5 Great Plaza `0.015`). Values in this range are normal, not underpowered.
- **Prosperity & fascination benchmarks**: vanilla traditions never grant flat `prosperity_growth` (only `prosperity_growth_factor`, `+10%`–`+20%` global) or positive `cultural_head_fascination_mult` (all vanilla uses are negative). Treat positive values as deliberate signature buffs.
- **Replacement guard in `can_pick`**: wrap mutually exclusive `NOT = { has_cultural_tradition = <x> }` checks in `trigger_if = { limit = { OR = { NOT = { exists = scope:replacing } NOT = { scope:replacing = culture_tradition:<x> } } } ... }` so cultures holding `<x>` can replace it directly.
- **Ethos penalty `desc` keys**: match the exact `NOR = { culture_pillar:ethos_* }` list to a vanilla key in `cultural_traditions_l_english.yml` (e.g. `not_communal_bureaucratic_or_stoic_desc`) or add a `bm_` key; never reuse a mismatched ethos tooltip.
- **Port parameter overlap**: `tradition_fp1_coastal_warriors` already grants `port_district_stationed_maa_bonus` and `port_district_enabled_for_tribals`, and vanilla locks it out of `tradition_seafaring` (`seafarers_port_building_slot`, `seafarers_port_maa_control`). Check overlap before bundling port parameters.
