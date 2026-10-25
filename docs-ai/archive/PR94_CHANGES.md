# PR #94 (`pr/94`) vs `main` — Review Notes

Branch `pr/94`: 39 commits, 158 files, +7,074 / −3,056.

Of that, localization is roughly +2,960 / −1,740 across 9 languages. Two files are large non-localization additions:
`gui/window_situation_list.gui` (+1,699, a full copy of the vanilla window) and `common/religion/religion_types/bm_religion.txt` (+754, a move of the religion definitions).
Most of the "7k added / 3k removed" is therefore localization and relocated or copied files, not new logic.

## Verdict on the PR description

The description is largely accurate. Each feature below exists in the diff. It leaves out several changes that you should decide on yourself (next section).

| PR claim | Verified? | Evidence |
|---|---|---|
| 1.19 religion folder migration | Yes | `religions/` → `religion_types/`; `holy_sites/` → `holy_site_types/`; `religion_families/` → `religion_family_types/`; new `doctrine_types` and `doctrine_group_types` |
| Prevalence rule (Player Only … More Frequent) | Yes | `bm_blood_mage_prevalence` rule (6 settings), `on_birth_child` on_action, yearly review, scripted modifier, trait `potential` gate. Default is untouched. |
| Appearance rule (none / eyes / eyes+hair) | Yes | `bm_physical_alteration` rule; `bm_trait_modifiers.txt` +177/−45 |
| Lore rule (Historical / AGOT) | Yes | `bm_lore` rule. The only AGOT references in the mod are the pre-existing `AGOT_is_loaded` global variable check and a comment in `bm_triggers.txt`, which is not a static link. |
| Cult-initiation faith requirement | Yes | `bm_initiation_faith_requirement` rule (dedicated cult default / witchcraft accepted) |
| Healing for 1.19 ailments | Yes | `bm_cure_illness_interactions.txt` now handles `withering_mind`, `clouded_eyes`, `fragile_bones`, `faltering_heart`. It also fixes `lunatic` → `lunatic_1`. |
| Double piety charge fix | Plausible | Commit `a57c133`. I did not trace each interaction. |
| Conversion routing by religious family | Yes | `bm_religion_conversion_effects.txt`: Christian, Islamic, Jewish, Eastern, Sinitic, Germanic (Ásatrú), unreformed, with a fallback to the Christian-syncretism faith |
| Hidden `blood_magic_cult_faith` doctrine parameter | Yes | `bm_doctrine_types.txt`, `bm_doctrine_group_types.txt` |
| Native faith integration moved to optional companions | Yes, but see below | Crimson Ka is removed from this repo. The companion mods are **not** in this repo and I could not review them. |
| Situation panel and rosters | Yes | `window_situation_list.gui`, `bm_blood_mage_story` story cycle, scripted GUIs, lifecycle effects, on_actions that create stories on acquisition |
| Obsolete files removed | Yes | `ck3-tiger.conf`, `_character_interactions.info`, and `bm_channel_self_modifiers.txt` (a single modifier file) deleted |
| Publishing helper, credentials excluded | Yes | `scripts/publish-steam-workshop.sh` (464 lines), `.env.dist`, `.gitignore` adds `.env`, `*.vdf`, `*.ck3`, `*.log`, `.serena/` |
| Validation numbers | Not verified | I did not run Tiger or CK3. The AGOT + companion stack tests need mods that are not in the repo. |

## Things the description does not mention (or understates)

1. **The mod's identity is changed in `descriptor.mod`.**
   - `name`: `Blood Mages [Nicelander]` → `Blood Mages - 1.19`.
   - `remote_file_id`: `3470491478` → `3765727801`, which points at the fork's Workshop item rather than yours.
   - Merging as-is would redirect your Workshop identity. The helper script also publishes to a Workshop item chosen through `STEAM_PUBLISHED_FILE_ID`. Decide which item this should target before merging.
2. **The Blood Mage trait is changed.**
   - `genetic = yes`, `good = yes` and `group = lifestyle_blood_mage_group` are removed from `lifestyle_blood_mage`. The Crimson Empowerment trait also loses `good` and `group`.
   - Inheritance now relies only on `inherit_chance` and `both_parent_has_trait_inherit_chance`.
   - This may change how the trait appears in the UI (good/bad colouring, trait grouping) and how it is inherited. The description says existing behavior stays the default, which may not hold here. Test it in game.
   - Two `#tiger-ignore` comments suppress validator warnings about `birth` and `random_creation` on a non-genetic trait.
3. **Blood of Numenor support was deleted.**
   - About 75 lines of Blood of Numenor drain-resistance logic were removed from `bm_drain_duel_values.txt`. This is third-party mod compatibility that you previously supported, and the description doesn't mention it.
   - The old `ck3-tiger.conf` filter that hid those "unknown token" errors was removed with it.
4. **Standalone mod loses the Cult of the Crimson Ka.** The faith moves to the optional "Vanilla Religions" companion, which is not in this repo. The description says "native-faith integration", which doesn't make clear that a faith is lost from the base mod. `README.md` still describes the Crimson Ka (line ~143), so it needs checking against the changelog.
5. **A new "reformation repair" system is added.** It consists of a decision, an event, effects and triggers (`bm_reformation_repair_*`, commit `069a15a` "unblock cult reformation"). The description doesn't mention it.
6. **Full copy of a vanilla GUI file.**
   - `window_situation_list.gui` is a 1,699-line rebase of the vanilla 1.19.0.6 window. It will override any other mod that touches this window and will go stale on each CK3 patch.
   - The PR mentions this in its review notes, and the file's header comment explains why.
7. **Other small changes:**
   - Mod display name and description rewritten (`description.txt`, README).
   - `thumbnail-1.19.png` added.
   - Workshop screenshots added.
   - Debug decisions edited.
8. **Line endings.** The diff shows some files with a UTF-8 BOM and CRLF, and `\ No newline at end of file` fixes. Check `.gitattributes` and editor settings to avoid noisy diffs later.

## Key changes by area

- **Rules (`common/game_rules`)**: `bm_lore`, `bm_physical_alteration`, `bm_blood_mage_prevalence`, `bm_initiation_faith_requirement`, and the renamed religion rule `quintessence_religion`.
- **Religion**: standalone Quintessence faiths are kept. Conversion routing, doctrine parameter, and the reformation repair system are new.
- **Gameplay**: prevalence modifiers on birth, yearly and AI acquisition. Blood Mage acquisition now goes through `bm_become_blood_mage_effect`, which also creates the story. Healing and piety fixes.
- **Interface**: Situation panel, rosters for golems and the Crimson retinue, text icons, tooltips.
- **Portraits**: eyes and hair evolve with total mastery, gated by the appearance rule.
- **Localization**: all 9 languages refreshed, with a full French review.
- **Tooling and docs**: README, CHANGELOG, Workshop description, the publishing script.

## Suggested before merging

- Settle the `descriptor.mod` name and ID question.
- Confirm that removing `genetic` and `group` from the trait is intended. Test the inheritance and the trait UI.
- Decide whether dropping Blood of Numenor support is acceptable.
- Get the companion mods (Vanilla Religions, AGOT) into a place you can review.
- Do the in-game smoke test the PR itself recommends: rules, conversion routing, portraits, healing, Situation panel.
- Run the Tiger validation yourself.
