---
kind: knowledge_card
id: bld_knowledge_card_changelog
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for changelog production
quality: 9.2
title: "Knowledge Card Changelog"
version: "1.1.0"
author: wave1_builder_gen_v2
tags: [changelog, builder, knowledge_card]
tldr: "Domain knowledge for changelog production -- Keep a Changelog, SemVer 2.0, migration notes"
domain: "changelog construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Domain Overview
Changelogs are structured records of product changes that enable users to assess upgrade impact and migration effort. The de-facto standard is Keep a Changelog (keepachangelog.com) which defines six change categories per release. Version numbering follows SemVer 2.0 (semver.org): MAJOR for breaking changes, MINOR for backward-compatible features, PATCH for backward-compatible fixes.

Industry references include Stripe API versioning (date-based API versions with explicit migration guides per breaking change), GitHub Releases (changelog as first-class release artifact), and conventional commits (feat/fix/chore prefixes that map to SemVer bumps).

## Key Concepts
| Concept | Definition | Source |
|---------|-----------|--------|
| SemVer | MAJOR.MINOR.PATCH versioning where MAJOR = breaking, MINOR = feature, PATCH = fix | semver.org 2.0 |
| Added | New features or capabilities not previously present | Keep a Changelog |
| Changed | Changes to existing behavior (non-breaking) | Keep a Changelog |
| Deprecated | Features still present but marked for removal in a future MAJOR release | Keep a Changelog |
| Removed | Features deleted in this release (always MAJOR bump) | Keep a Changelog |
| Fixed | Bug fixes for existing behavior | Keep a Changelog |
| Security | Patches for vulnerabilities; include CVE ID when public | Keep a Changelog |
| Unreleased | Changes committed but not yet versioned into a release | Keep a Changelog |
| Breaking Change | Any change requiring user code modification to maintain current behavior | SemVer 2.0 |
| Migration Guide | Step-by-step instructions for upgrading across a MAJOR version boundary | Stripe API docs pattern |
| Conventional Commits | Commit message spec (feat/fix/BREAKING CHANGE) that auto-generates changelogs | conventionalcommits.org |

## Industry Standards
- Keep a Changelog (keepachangelog.com) -- six section format
- Semantic Versioning 2.0.0 (semver.org) -- version bump rules
- Conventional Commits 1.0.0 (conventionalcommits.org) -- commit-to-changelog mapping
- Stripe API versioning model -- date-versioned APIs with per-version migration guides
- GitHub Releases API -- versioned artifacts with release notes as structured data
- CHANGELOG.md convention -- single canonical file at repo root per git project standards

## Common Patterns
1. Six-section structure per release: Added/Changed/Deprecated/Removed/Fixed/Security.
2. Keep `[Unreleased]` at top for in-progress tracking; rename to version on release.
3. Link version header to GitHub diff: `## [1.2.0] - 2024-01-15` -> diff URL.
4. Prefix breaking entries with "BREAKING:" for automated scanner detection.
5. For API-versioned products (Stripe model): include migration code snippet per breaking change.
6. Machine-readable changelog: use consistent headers for changelog parsing tools.

## Pitfalls
- Inconsistent formatting across releases (switch template versions mid-project).
- Omitting Deprecated section, leading to surprise removals in the next MAJOR.
- Version bump mismatch: adding features under a PATCH increment.
- Vague entries: "improved performance" vs "Reduce API response time from 800ms to 120ms (p99)".
- Missing migration guide for MAJOR versions, forcing users to read diffs.
- Not updating [Unreleased] during development, causing lost change history.
