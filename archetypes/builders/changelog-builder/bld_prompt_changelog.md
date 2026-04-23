---
kind: instruction
id: bld_instruction_changelog
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for changelog
quality: 8.9
title: "Instruction Changelog"
version: "1.1.0"
author: wave1_builder_gen_v2
tags: [changelog, builder, instruction]
tldr: "Step-by-step production process for changelog"
domain: "changelog construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_schema_changelog
  - bld_output_template_changelog
  - bld_examples_changelog
  - bld_knowledge_card_changelog
  - p01_qg_changelog
  - kc_changelog
  - p10_mem_changelog_builder
  - changelog-builder
  - p03_sp_changelog_builder
  - p04_ct_bump_version
---

## Phase 1: RESEARCH
1. Identify the version being documented using SemVer (MAJOR.MINOR.PATCH per semver.org).
2. Determine version bump type: MAJOR (breaking changes), MINOR (new features), PATCH (fixes only).
3. Collect Added entries: new features or capabilities introduced.
4. Collect Changed entries: modifications to existing functionality.
5. Collect Deprecated entries: features flagged for future removal with removal timeline.
6. Collect Removed entries: features deleted in this release.
7. Collect Fixed entries: bug fixes with issue IDs and PR references.
8. Collect Security entries: vulnerability patches with CVE references where applicable.
9. Cross-reference previous changelog entries for consistent terminology.

## Phase 2: COMPOSE
1. Create new entry per bld_schema_changelog.md field spec.
2. Set version header: `## [X.Y.Z] - YYYY-MM-DD` (Keep a Changelog format).
3. Maintain `## [Unreleased]` section at top for in-progress changes.
4. Populate `### Added` section with new capabilities (imperative: "Add X").
5. Populate `### Changed` section with modified behavior (imperative: "Change Y").
6. Populate `### Deprecated` section with removal notices and target version.
7. Populate `### Removed` section with deleted features (imperative: "Remove Z").
8. Populate `### Fixed` section with issue ID and resolution (imperative: "Fix A").
9. Populate `### Security` section with CVE ID and affected versions.
10. For MAJOR versions, add `### Migration` section with step-by-step upgrade path.
11. Prefix breaking-change entries with "BREAKING:" for scanner visibility.
12. Use bld_output_template_changelog.md for markdown structure.

## Phase 3: VALIDATE
- [ ] SemVer format X.Y.Z (no leading `v`) in frontmatter version field.
- [ ] All 6 Keep a Changelog sections present (Added/Changed/Deprecated/Removed/Fixed/Security).
- [ ] MAJOR bump includes Migration section with actionable steps.
- [ ] Breaking change entries prefixed with "BREAKING:".
- [ ] Each entry uses imperative mood: "Add X", "Fix Y", "Remove Z".
- [ ] Peer review confirms accuracy against issue tracker and PRs.


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_changelog]] | downstream | 0.44 |
| [[bld_output_template_changelog]] | downstream | 0.43 |
| [[bld_examples_changelog]] | downstream | 0.41 |
| [[bld_knowledge_card_changelog]] | upstream | 0.41 |
| [[p01_qg_changelog]] | downstream | 0.40 |
| [[kc_changelog]] | upstream | 0.38 |
| [[p10_mem_changelog_builder]] | downstream | 0.30 |
| [[changelog-builder]] | upstream | 0.28 |
| [[p03_sp_changelog_builder]] | related | 0.27 |
| [[p04_ct_bump_version]] | downstream | 0.23 |
