---
kind: schema
id: bld_schema_changelog
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for changelog
quality: 9.1
title: "Schema Changelog"
version: "1.1.0"
author: wave1_builder_gen_v2
tags: [changelog, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for changelog. Keep a Changelog format, SemVer 2.0."
domain: "changelog construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_schema_integration_guide
  - bld_schema_reranker_config
  - bld_schema_usage_report
  - bld_schema_pitch_deck
  - bld_schema_quickstart_guide
  - bld_schema_benchmark_suite
  - bld_schema_dataset_card
  - bld_schema_sandbox_spec
  - bld_schema_contributor_guide
  - bld_schema_api_reference
---

## Frontmatter Fields
### Required
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string | yes | | Must match ID Pattern |
| kind | string | yes | | Always "changelog" |
| pillar | string | yes | | P01 |
| title | string | yes | | Human-readable name (e.g., "MyApp Changelog") |
| version | string | yes | | SemVer X.Y.Z (no leading v) |
| release_date | string | yes | | ISO 8601 YYYY-MM-DD |
| created | string | yes | | ISO 8601 YYYY-MM-DD |
| updated | string | yes | | ISO 8601 YYYY-MM-DD |
| author | string | yes | | Maintainer username |
| domain | string | yes | | Product domain |
| quality | null | yes | null | Never self-score; peer review assigns |
| tags | list | yes | | Keywords (e.g., security, feature) |
| tldr | string | yes | | Summary of changes (<=200 chars, ASCII only) |

### Recommended
| Field | Type | Notes |
|-------|------|-------|
| related_prs | list | PR/issue IDs linked to this release |
| reviewers | list | Peer reviewer usernames |
| breaking | boolean | true if MAJOR version bump |

## ID Pattern
^p01_ch_[a-z][a-z0-9_]+\\.md$

## Body Structure (Keep a Changelog)
1. **[Unreleased]** -- In-progress changes not yet versioned
2. **[X.Y.Z] - YYYY-MM-DD** -- Version header (linked to diff)
3. **### Added** -- New capabilities (imperative: "Add X")
4. **### Changed** -- Modified behavior (imperative: "Change Y")
5. **### Deprecated** -- Features marked for removal with target version
6. **### Removed** -- Deleted features (BREAKING; imperative: "Remove Z")
7. **### Fixed** -- Bug fixes with issue ID (imperative: "Fix A")
8. **### Security** -- Vulnerability patches with CVE ID
9. **### Migration** -- Step-by-step upgrade guide (MAJOR versions only)

## Constraints
- All required fields must be present and valid YAML.
- ID must match exact regex pattern.
- version must be X.Y.Z (SemVer 2.0; no leading v, no pre-release suffix in production).
- MAJOR version bump requires Migration section in body.
- Breaking entries must be prefixed "BREAKING:" for scanner detection.
- quality must remain null (assigned by peer review only).
- tldr must be <= 200 characters and ASCII-only.
- Each change entry uses imperative mood.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_integration_guide]] | sibling | 0.65 |
| [[bld_schema_reranker_config]] | sibling | 0.63 |
| [[bld_schema_usage_report]] | sibling | 0.63 |
| [[bld_schema_pitch_deck]] | sibling | 0.63 |
| [[bld_schema_quickstart_guide]] | sibling | 0.62 |
| [[bld_schema_benchmark_suite]] | sibling | 0.62 |
| [[bld_schema_dataset_card]] | sibling | 0.60 |
| [[bld_schema_sandbox_spec]] | sibling | 0.59 |
| [[bld_schema_contributor_guide]] | sibling | 0.59 |
| [[bld_schema_api_reference]] | sibling | 0.59 |
