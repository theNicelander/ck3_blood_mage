# Traits (`common/traits/`)

Refs: `bm_blood_mage_trait.txt`, `bm_blood_power_trait.txt`. Specs: `docs-ai/architecture/blood-mage-traits.md`, `blood-mage-track-xp*.md`.

- **Additive cumulative tracks**: reached XP thresholds stack together. Declare **incremental deltas only** at each milestone, never cumulative totals.
- **XP**: `add_trait_xp = { trait = <t> track = <k> value = <int> }`.
- **Lifestyle traits**: use `random_creation_weight = 0`; never set `good = yes` or `random_creation` on non-genetic traits.
- **Inheritance**: `inherit_chance` / `both_parent_has_trait_inherit_chance` take percents (`50` = 50%). Don't mix `genetic = yes` with custom script inheritance unintentionally. Restrict via `potential = {}`.
- **Add/alter track checklist**: update trait file → grep all XP-gated checks for track names → update `common/scripted_effects/bm_trait_track_xp_gain_effects.txt` → add `<trait>_<track>` + `_desc` in `bm_traits_l_english.yml` → grep `common/ events/ localization/english/` + `scripts/check_repo.py`.
