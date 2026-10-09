# Russian localization

## Summary & Motivation

Complete player-facing Russian localization for the current CK3 1.20 mod, with automatic
checks that keep it aligned with the English source.

## Core Concepts & High-Level Changes

- Mirrored all English localization files, including events, religions, holy sites and debug UI.
- Repaired missing wilderness cooldown and Tenerife labels; separated requesting magic from granting it.
- Corrected the new-education description to describe acquiring another education trait.
- Added a dependency-free localization checker and a GitHub Actions validation workflow.
- Aligned README compatibility and prevalence documentation with current definitions.

## Key Decisions

- Keep identifiers, dynamic expressions, aliases, icons and formatting commands unchanged.
- Maintain English and Russian together in this fork; game language chooses the localization.
- Keep the upstream descriptor and gameplay balance; no version bump or new compatibility claim.
- Runtime UI layout and CK3 execution require an in-game test; static checks do not establish compatibility.
