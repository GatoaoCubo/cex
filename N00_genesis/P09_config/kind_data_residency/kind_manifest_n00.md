---
id: n00_data_residency_manifest
kind: knowledge_card
8f: F3_inject
pillar: P09
nucleus: n00
title: "Data Residency -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, data_residency, p09, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_data_residency
  - bld_schema_dataset_card
  - bld_schema_reranker_config
  - bld_schema_usage_report
  - bld_schema_integration_guide
  - bld_schema_sandbox_spec
  - bld_schema_quickstart_guide
  - bld_schema_benchmark_suite
  - bld_schema_tts_provider
  - bld_schema_sandbox_config
---

<!-- 8F: F1=knowledge_card P09 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A data_residency configuration specifies geographic and jurisdictional constraints on where data may be stored, processed, and transmitted. It enables GDPR, LGPD, HIPAA, and regional compliance by constraining which cloud regions, providers, and storage backends are permitted for a given data category or customer segment.

## Pillar
P09 -- config

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `data_residency` |
| pillar | string | yes | Always `P09` |
| title | string | yes | Human-readable config name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| jurisdiction | list | yes | Applicable legal frameworks (GDPR, LGPD, HIPAA) |
| allowed_regions | list | yes | Cloud regions where data may reside (e.g. eu-west-1) |
| blocked_regions | list | no | Explicitly forbidden regions |
| allowed_providers | list | no | Cloud providers permitted (aws, gcp, azure) |
| data_categories | list | yes | Types of data this applies to (PII, PHI, financial) |
| encryption_at_rest | boolean | yes | Require encryption for stored data |
| encryption_in_transit | boolean | yes | Require TLS for data in motion |
| audit_log_required | boolean | no | Whether access must be logged |

## When to use
- Deploying CEX for a customer in the EU where GDPR applies
- Configuring healthcare deployments that must keep PHI in specific regions
- Setting up multi-region deployments with jurisdiction-aware routing

## Builder
`archetypes/builders/data_residency-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind data_residency --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: data_residency_eu_gdpr
kind: data_residency
pillar: P09
nucleus: n05
title: "EU GDPR Data Residency Config"
version: 1.0
quality: null
---
jurisdiction: [GDPR]
allowed_regions: [eu-west-1, eu-central-1]
data_categories: [PII, usage_logs]
encryption_at_rest: true
encryption_in_transit: true
audit_log_required: true
```

## Related kinds
- `secret_config` (P09) -- secrets must also respect data residency constraints
- `rbac_policy` (P09) -- access controls for data in regulated regions
- `fhir_agent_capability` (P08) -- FHIR compliance includes data residency requirements

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_data_residency]] | upstream | 0.52 |
| [[bld_schema_dataset_card]] | upstream | 0.43 |
| [[bld_schema_reranker_config]] | upstream | 0.42 |
| [[bld_schema_usage_report]] | upstream | 0.42 |
| [[bld_schema_integration_guide]] | upstream | 0.42 |
| [[bld_schema_sandbox_spec]] | upstream | 0.41 |
| [[bld_schema_quickstart_guide]] | upstream | 0.40 |
| [[bld_schema_benchmark_suite]] | upstream | 0.40 |
| [[bld_schema_tts_provider]] | upstream | 0.40 |
| [[bld_schema_sandbox_config]] | upstream | 0.39 |
