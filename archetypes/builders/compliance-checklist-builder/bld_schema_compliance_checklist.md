---
kind: schema
id: bld_schema_compliance_checklist
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for compliance_checklist
quality: 9.1
title: "Schema Compliance Checklist"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [compliance_checklist, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for compliance_checklist"
domain: "compliance_checklist construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Frontmatter Fields
### Required
| Field | Type | Required | Default | Notes |
|---|---|---|---|---|
| id | string | yes | null | Must match ID Pattern |
| kind | string | yes | "compliance_checklist" | Fixed value |
| pillar | string | yes | "P11" | Fixed value |
| title | string | yes | null | Descriptive name |
| version | string | yes | "1.0" | Semantic versioning |
| created | datetime | yes | null | ISO 8601 format |
| updated | datetime | yes | null | ISO 8601 format |
| author | string | yes | null | Owner's name |
| domain | string | yes | null | Compliance area (e.g., "anti-money laundering") |
| quality | null | yes | null | Never self-score; peer review assigns |
| tags | list | yes | [] | Keywords for categorization |
| tldr | string | yes | null | Summary of checklist purpose |
| regulatory_scope | string | yes | null | Applicable regulations |
| audit_frequency | string | yes | null | "quarterly" / "annual" |

### Recommended
| Field | Type | Notes |
|---|---|---|
| compliance_status | string | "draft" / "approved" / "deprecated" |
| review_cycle | string | "biannual" / "custom" |
| responsible_team | string | Department or role owning checklist |

## ID Pattern
^p11_cc_[a-z][a-z0-9_]+.md$

## Body Structure
1. **Scope and Objectives**
   Define the checklist's purpose, covered regulations, and target entities.

2. **Regulatory Requirements**
   List mandatory compliance rules, standards, and legal references.

3. **Audit and Monitoring**
   Specify procedures for audits, data collection, and monitoring frequency.

4. **Corrective Actions**
   Outline steps for addressing non-compliance, escalation paths, and remediation timelines.

5. **Reporting and Documentation**
   Detail required records, reporting formats, and retention policies.

6. **Review and Update**
   Define processes for periodic validation, stakeholder feedback, and version control.

## Constraints
- Regulatory_scope must align with at least one recognized compliance framework.
- Audit_frequency must be one of: "daily", "weekly", "monthly", "quarterly", "annual", "custom".
- Compliance_status must be "draft", "approved", or "deprecated".
- Tags must include at least one domain-specific keyword (e.g., "KYC", "GDPR").
- Version must follow semantic versioning (e.g., "1.2.3").
- All datetime fields must use ISO 8601 format (e.g., "2023-10-05T14:30:00Z").
