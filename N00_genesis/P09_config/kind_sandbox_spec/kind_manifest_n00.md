---
id: n00_sandbox_spec_manifest
kind: knowledge_card
8f: F3_inject
pillar: P09
nucleus: n00
title: "Sandbox Spec -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, sandbox_spec, p09, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_sandbox_spec
  - bld_schema_sandbox_config
  - bld_schema_reranker_config
  - bld_schema_benchmark_suite
  - bld_schema_playground_config
  - bld_schema_integration_guide
  - bld_schema_usage_report
  - bld_schema_search_strategy
  - bld_schema_action_paradigm
  - bld_schema_dataset_card
---

<!-- 8F: F1=knowledge_card P09 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A sandbox_spec is a higher-level enterprise pilot procurement document that describes the isolated sandbox environment offered to a prospect or enterprise customer for evaluation: what capabilities are included, SLAs, data isolation guarantees, provisioning timeline, and exit criteria. It bridges the gap between technical sandbox_config and business procurement requirements.

## Pillar
P09 -- config

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `sandbox_spec` |
| pillar | string | yes | Always `P09` |
| title | string | yes | Human-readable spec name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| customer | string | yes | Target customer or segment |
| duration_days | integer | yes | Pilot duration |
| included_nuclei | list | yes | Which nuclei are available in the pilot |
| data_isolation | enum | yes | shared_namespace \| dedicated_namespace \| dedicated_cluster |
| sla_availability_pct | float | no | Uptime SLA for the pilot (e.g. 99.0) |
| success_criteria | list | yes | Measurable criteria that define pilot success |
| exit_conditions | list | no | Conditions under which pilot is terminated early |
| sandbox_config_ref | string | yes | Reference to underlying sandbox_config |

## When to use
- Scoping an enterprise pilot offer with specific capability and isolation guarantees
- Defining success criteria for a proof-of-concept engagement
- Creating a procurement-ready document that maps to sandbox_config settings

## Builder
`archetypes/builders/sandbox_spec-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind sandbox_spec --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: sandbox_spec_enterprise_pilot_q2
kind: sandbox_spec
pillar: P09
nucleus: n06
title: "Q2 Enterprise Pilot Sandbox Spec"
version: 1.0
quality: null
---
customer: AcmeCorp
duration_days: 30
included_nuclei: [n01, n03, n04]
data_isolation: dedicated_namespace
sla_availability_pct: 99.0
success_criteria:
  - "Produce 10 quality artifacts with score >= 8.5"
  - "Complete 1 full 8F mission autonomously"
sandbox_config_ref: sandbox_config_n05_ci
```

## Related kinds
- `sandbox_config` (P09) -- the technical implementation this spec describes
- `playground_config` (P09) -- lighter-weight interactive evaluation alternative
- `white_label_config` (P09) -- branded sandbox for partner pilot deployments

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_sandbox_spec]] | upstream | 0.50 |
| [[bld_schema_sandbox_config]] | upstream | 0.48 |
| [[bld_schema_reranker_config]] | upstream | 0.46 |
| [[bld_schema_benchmark_suite]] | upstream | 0.45 |
| [[bld_schema_playground_config]] | upstream | 0.44 |
| [[bld_schema_integration_guide]] | upstream | 0.44 |
| [[bld_schema_usage_report]] | upstream | 0.44 |
| [[bld_schema_search_strategy]] | upstream | 0.43 |
| [[bld_schema_action_paradigm]] | upstream | 0.43 |
| [[bld_schema_dataset_card]] | upstream | 0.43 |
