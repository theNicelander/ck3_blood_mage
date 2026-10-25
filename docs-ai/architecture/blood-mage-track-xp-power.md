# Blood Mage Track XP: Power (`lifestyle_blood_power`)

Tracks: `dynasty`, `fury`, `mastery`, `presence`, `prosperity`, `shadows` (6). Shared rules: [hub](blood-mage-track-xp.md).

| XP | Cost | Action | Source | Req | CD |
| --- | --- | --- | --- | --- | --- |
| +10 in chosen track (+1 `enlightenment`) | 150 Piety + Major (`lifeforce_modifier_major`) | Channel Blood Power | Major grimoire option `bm_cast_blood_magic_major.001` -> `bm_blood_power_event.001` | `piety_level >= 1`, Major lifeforce held | None |
| 0 (manual advancement only) | None | Passive Growth | None | None | None |
| +15 to +150 per quarter (+5 to +50 per month equiv) across Lifestyles | None | Quarterly Blood Power Pulse (`quarterly_playable_pulse`) | on-action `blood_mage_yearly_events.005` | Playable character, has `lifestyle_blood_power` with track XP | 3 months |
