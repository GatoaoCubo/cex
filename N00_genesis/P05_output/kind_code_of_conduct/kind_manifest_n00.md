---
id: n00_code_of_conduct_manifest
kind: knowledge_card
pillar: P05
nucleus: n00
title: "Code Of Conduct -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, code_of_conduct, p05, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_code_of_conduct
  - bld_schema_contributor_guide
  - bld_schema_app_directory_entry
  - bld_schema_integration_guide
  - bld_schema_benchmark_suite
  - bld_schema_reranker_config
  - bld_schema_multimodal_prompt
  - bld_schema_usage_report
  - bld_schema_dataset_card
  - code-of-conduct-builder
---

<!-- 8F: F1=knowledge_card P05 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Code of conduct produces a community governance document following the Contributor Covenant pattern (v2.1+). It establishes expected behavior, enforcement mechanisms, and reporting processes for open-source or community-driven projects. The artifact covers pledge, standards, enforcement responsibilities, and attribution.

## Pillar
P05 -- Output

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `code_of_conduct` |
| pillar | string | yes | Always `P05` |
| title | string | yes | Project or community name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| covenant_version | string | yes | Contributor Covenant version (e.g., 2.1) |
| enforcement_email | string | yes | Contact for reporting violations |
| scope | string | yes | Spaces covered (online + offline, repo, events) |
| enforcement_ladder | list | yes | Graduated consequence steps |

## When to use
- Launching an open-source project that needs community governance
- Establishing contributor guidelines for a new community platform
- Updating an existing code of conduct to a newer Contributor Covenant version

## Builder
`archetypes/builders/code_of_conduct-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind code_of_conduct --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- N04 knowledge manages community governance docs
- `{{SIN_LENS}}` -- Knowledge Gluttony: comprehensive, unambiguous coverage
- `{{TARGET_AUDIENCE}}` -- contributors, maintainers, community members
- `{{DOMAIN_CONTEXT}}` -- project type, community size, communication channels

## Example (minimal)
```yaml
---
id: code_of_conduct_cex_community
kind: code_of_conduct
pillar: P05
nucleus: n04
title: "CEX Community Code of Conduct"
version: 1.0
quality: null
---
covenant_version: "2.1"
enforcement_email: "community@example.com"
scope: "GitHub repo, Discord, all community events"
```

## Related kinds
- `contributor_guide` (P05) -- companion doc covering HOW to contribute
- `github_issue_template` (P05) -- enforces code of conduct in issue reporting
- `knowledge_card` (P01) -- community norms can be documented as KCs

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_code_of_conduct]] | downstream | 0.45 |
| [[bld_schema_contributor_guide]] | downstream | 0.44 |
| [[bld_schema_app_directory_entry]] | downstream | 0.44 |
| [[bld_schema_integration_guide]] | downstream | 0.42 |
| [[bld_schema_benchmark_suite]] | downstream | 0.42 |
| [[bld_schema_reranker_config]] | downstream | 0.41 |
| [[bld_schema_multimodal_prompt]] | downstream | 0.41 |
| [[bld_schema_usage_report]] | downstream | 0.41 |
| [[bld_schema_dataset_card]] | downstream | 0.41 |
| [[code-of-conduct-builder]] | related | 0.40 |
