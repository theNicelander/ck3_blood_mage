# Character Interactions (`common/character_interactions/`)

Copy neighbor. For exclusive modal options (`send_options_exclusive = yes`), use skill `add-interaction-send-options`.

- **Cost & validity**: declare `cost` once; never deduct in `on_accept`. Cheap checks first in `is_shown`; affordability in `is_valid` / `is_valid_showing_failures_only`. Never skip validity with `is_ai = yes`.
- **AI**: `ai_targets` (`self`, `dynasty`, `family`, `spouses`, `children`, `courtiers`, `councillors`, `liege`), `ai_frequency`, `ai_potential` (actor scope only — no `recipient`!), `ai_will_do` (`add` first, `factor = 0` vetoes last), `ai_accept`. Check health/Lifeforce/piety/opinion before harmful acts; state unverified AI frequency in summary.
- **Icons**: copy `gfx/interface/icons/traits/bm_interactions.dds` → `gfx/interface/icons/character_interactions/<name>.dds`. Keep `.dds` synced on rename/delete. Never prefix interaction loc with `@bm_ancient_discipline_icon!` (`category = interaction_category_bm_blood_magic` already sets icon).
- **Debug log** (`on_accept` / executions):
```ck3
# Target interaction:
debug_log = "BloodMageInteraction: <name> (<opt>) | Actor: [actor.GetShortUINameNoTooltip] (ID:[actor.GetID], [Select_CString(actor.IsPlayer, 'Player', 'AI')]) -> Recipient: [recipient.GetShortUINameNoTooltip] (ID:[recipient.GetID], [Select_CString(recipient.IsPlayer, 'Player', 'AI')]) | Rel: [actor.Custom2('RelationToMeShort', recipient)] | Tag: [actor.Custom2('bm_debug_relation_tags', recipient)] | Opinion: [actor.GetOpinionOf( recipient )]"
# Self-cast:
debug_log = "BloodMageSelfCast: <name> (<opt>) | Actor: [actor.GetShortUINameNoTooltip] (ID:[actor.GetID], [Select_CString(actor.IsPlayer, 'Player', 'AI')])"
# Execution (lifedrain_execution_effect): same as target using scope:executioner -> scope:victim, prefix "BloodMageExecution: lifedrain"
```
