---
id: n00_lifecycle_rule_manifest
kind: knowledge_card
8f: F3_inject
pillar: P11
nucleus: n00
title: "Lifecycle Rule -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, lifecycle_rule, p11, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_lifecycle_rule
  - bld_schema_reranker_config
  - bld_schema_dataset_card
  - bld_schema_integration_guide
  - bld_schema_usage_report
  - bld_schema_multimodal_prompt
  - bld_schema_sandbox_spec
  - bld_schema_benchmark_suite
  - bld_schema_nps_survey
  - bld_schema_search_strategy
---

<!-- 8F: F1=knowledge_card P11 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A lifecycle_rule defines the freshness, archive, and promotion policy for a category of artifacts or data, specifying when items are promoted to higher quality tiers, when they become stale, and when they should be archived or deleted. It governs artifact health over time without requiring manual intervention.

## Pillar
P11 -- feedback

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `lifecycle_rule` |
| pillar | string | yes | Always `P11` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| applies_to | array | yes | Kinds or paths this rule governs |
| freshness_ttl_days | integer | yes | Days before artifact is considered stale |
| promotion_criteria | object | yes | Conditions to promote artifact (quality score, age, usage) |
| archive_after_days | integer | yes | Days after staleness before archiving |
| delete_after_days | integer | no | Days after archiving before permanent deletion |
| review_trigger | enum | yes | time \| quality_drop \| dependency_change \| never |

## When to use
- When setting up automated artifact hygiene for a pillar or nucleus
- When configuring quality-based promotion of artifacts (e.g. null -> reviewed)
- When implementing data retention policies for compliance requirements

## Builder
`archetypes/builders/lifecycle_rule-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind lifecycle_rule --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: lr_knowledge_cards_p01
kind: lifecycle_rule
pillar: P11
nucleus: n04
title: "Example Lifecycle Rule"
version: 1.0
quality: null
---
# Lifecycle Rule: P01 Knowledge Cards
applies_to: [knowledge_card]
freshness_ttl_days: 90
archive_after_days: 365
promotion_criteria: {quality_min: 8.5, min_age_days: 7}
review_trigger: quality_drop
```

## Related kinds
- `consolidation_policy` (P10) -- memory-level lifecycle policy complementing artifact rules
- `quality_gate` (P11) -- gate that triggers lifecycle promotions or demotions
- `reward_signal` (P11) -- signal that can trigger promotion via lifecycle rule

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_lifecycle_rule]] | upstream | 0.45 |
| [[bld_schema_reranker_config]] | upstream | 0.43 |
| [[bld_schema_dataset_card]] | upstream | 0.42 |
| [[bld_schema_integration_guide]] | upstream | 0.41 |
| [[bld_schema_usage_report]] | upstream | 0.41 |
| [[bld_schema_multimodal_prompt]] | upstream | 0.40 |
| [[bld_schema_sandbox_spec]] | upstream | 0.40 |
| [[bld_schema_benchmark_suite]] | upstream | 0.40 |
| [[bld_schema_nps_survey]] | upstream | 0.39 |
| [[bld_schema_search_strategy]] | upstream | 0.39 |
