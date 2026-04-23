---
id: n00_quickstart_guide_manifest
kind: knowledge_card
pillar: P05
nucleus: n00
title: "Quickstart Guide -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, quickstart_guide, p05, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_integration_guide
  - bld_schema_quickstart_guide
  - bld_schema_contributor_guide
  - bld_schema_onboarding_flow
  - bld_schema_reranker_config
  - bld_schema_usage_report
  - bld_schema_action_paradigm
  - bld_schema_search_strategy
  - bld_schema_benchmark_suite
  - bld_schema_product_tour
---

<!-- 8F: F1=knowledge_card P05 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Quickstart guide produces an end-to-end onboarding document that gets a developer or user from zero to their first working result in under 5 minutes. It covers prerequisites, installation, configuration, and first meaningful action with copy-paste commands and expected output at each step. The guide optimizes for time-to-value, not completeness; edge cases are deferred to the integration guide.

## Pillar
P05 -- Output

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `quickstart_guide` |
| pillar | string | yes | Always `P05` |
| title | string | yes | Product + "Quickstart" |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| target_time_min | int | yes | Target completion time in minutes (max 5) |
| prerequisites | list | yes | Required installs/accounts before starting |
| steps | list | yes | Numbered steps with command, expected output, notes |
| first_result | string | yes | Exact artifact or output user achieves on completion |
| next_steps | list | yes | Links to integration guide, API reference, tutorials |

## When to use
- Launching a new API, SDK, or product that needs developer adoption
- Replacing a README with a structured, time-boxed onboarding experience
- Reducing support tickets by eliminating the "how do I get started" question

## Builder
`archetypes/builders/quickstart_guide-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind quickstart_guide --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- N04 knowledge writes; N05 operations validates commands
- `{{SIN_LENS}}` -- Knowledge Gluttony: every step is precise, tested, copy-paste ready
- `{{TARGET_AUDIENCE}}` -- developer or end user with zero prior product knowledge
- `{{DOMAIN_CONTEXT}}` -- product type, install method, target OS, first meaningful action

## Example (minimal)
```yaml
---
id: quickstart_guide_cex_sdk
kind: quickstart_guide
pillar: P05
nucleus: n04
title: "CEX SDK -- 5-Minute Quickstart"
version: 1.0
quality: null
---
target_time_min: 5
prerequisites: [Python 3.10+, git, Claude API key]
first_result: "First knowledge card built via 8F pipeline"
```

## Related kinds
- `integration_guide` (P05) -- deep-dive that follows quickstart completion
- `contributor_guide` (P05) -- for contributors; quickstart is for users
- `onboarding_flow` (P05) -- quickstart may be step 1 of a broader onboarding flow

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_integration_guide]] | downstream | 0.49 |
| [[bld_schema_quickstart_guide]] | downstream | 0.49 |
| [[bld_schema_contributor_guide]] | downstream | 0.43 |
| [[bld_schema_onboarding_flow]] | downstream | 0.42 |
| [[bld_schema_reranker_config]] | downstream | 0.41 |
| [[bld_schema_usage_report]] | downstream | 0.41 |
| [[bld_schema_action_paradigm]] | downstream | 0.40 |
| [[bld_schema_search_strategy]] | downstream | 0.40 |
| [[bld_schema_benchmark_suite]] | downstream | 0.39 |
| [[bld_schema_product_tour]] | downstream | 0.39 |
