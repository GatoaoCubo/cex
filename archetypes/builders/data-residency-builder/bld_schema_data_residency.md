---
kind: schema
id: bld_schema_data_residency
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for data_residency
quality: 9.1
title: "Schema Data Residency"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [data_residency, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for data_residency"
domain: "data_residency construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_schema_dataset_card
  - bld_schema_usage_report
  - bld_schema_reranker_config
  - bld_schema_pitch_deck
  - bld_schema_safety_policy
  - bld_schema_benchmark_suite
  - bld_schema_audit_log
  - bld_schema_sandbox_config
  - bld_schema_quickstart_guide
  - bld_schema_integration_guide
---

## Frontmatter Fields
### Required
| Field | Type | Required | Default | Notes |
|---|---|---|---|---|
| id | string | yes |  | Unique identifier |
| kind | string | yes |  | Must be `data_residency` |
| pillar | string | yes |  | Must be `P09` |
| title | string | yes |  | Descriptive title |
| version | string | yes |  | Semantic version (e.g., `1.0.0`) |
| created | datetime | yes |  | ISO 8601 format |
| updated | datetime | yes |  | ISO 8601 format |
| author | string | yes |  | Responsible party |
| domain | string | yes |  | Data domain (e.g., `finance`) |
| quality | null | yes | null | Never self-score; peer review assigns |
| tags | list | yes |  | Keywords for categorization |
| tldr | string | yes |  | Summary of policy |
| data_location | string | yes |  | Jurisdiction where data resides |
| compliance_framework | string | yes |  | Regulatory standards (e.g., GDPR) |
| data_encryption | string | yes |  | Encryption protocols applied |

### Recommended
| Field | Type | Notes |
|---|---|---|
| data_retention_policy | string | Retention duration rules |
| third_party_sharing | boolean | Whether data is shared externally |
| audit_frequency | string | Scheduled audit intervals |

## ID Pattern
^p09_dr_[a-z][a-z0-9_]+.md$

## Body Structure
1. **Data Residency Policy**
   Define legal and operational rules for data storage locations.

2. **Compliance Frameworks**
   List regulations (e.g., GDPR, CCPA) governing data residency.

3. **Data Encryption Standards**
   Specify encryption algorithms and key management practices.

4. **Data Location Mapping**
   Map data categories to physical/jurisdictional storage locations.

5. **Audit Requirements**
   Outline procedures for verifying compliance with residency rules.

## Constraints
- Data location must be explicitly declared and verifiable.
- Compliance frameworks must align with the data’s jurisdiction.
- Encryption standards must meet or exceed industry benchmarks.
- Audit logs must be retained for at least 5 years.
- Third-party sharing requires explicit opt-in and legal safeguards.
- Version history must be maintained for all policy changes.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_dataset_card]] | sibling | 0.65 |
| [[bld_schema_usage_report]] | sibling | 0.65 |
| [[bld_schema_reranker_config]] | sibling | 0.63 |
| [[bld_schema_pitch_deck]] | sibling | 0.62 |
| [[bld_schema_safety_policy]] | sibling | 0.62 |
| [[bld_schema_benchmark_suite]] | sibling | 0.62 |
| [[bld_schema_audit_log]] | sibling | 0.61 |
| [[bld_schema_sandbox_config]] | sibling | 0.61 |
| [[bld_schema_quickstart_guide]] | sibling | 0.60 |
| [[bld_schema_integration_guide]] | sibling | 0.60 |
