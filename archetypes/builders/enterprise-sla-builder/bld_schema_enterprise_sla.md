---
kind: schema
id: bld_schema_enterprise_sla
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for enterprise_sla
quality: 9.1
title: "Schema Enterprise Sla"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [enterprise_sla, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for enterprise_sla"
domain: "enterprise_sla construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Frontmatter Fields
### Required
| Field | Type | Required | Default | Notes |
|---|---|---|---|---|
| id | string | yes |  | Must match ID Pattern |
| kind | string | yes |  | Always `enterprise_sla` |
| pillar | string | yes |  | Always `P11` |
| title | string | yes |  | Human-readable name |
| version | string | yes |  | Semantic version (e.g., `1.0.0`) |
| created | datetime | yes |  | ISO 8601 format |
| updated | datetime | yes |  | ISO 8601 format |
| author | string | yes |  | Owner of the document |
| domain | string | yes |  | Business unit or product |
| quality | null | yes | null | Never self-score; peer review assigns |
| tags | list | yes |  | Keywords for search |
| tldr | string | yes |  | Summary of key terms |
| service_level_objective | string | yes |  | Target uptime or performance |
| compliance_requirements | list | yes |  | Legal or regulatory mandates |

### Recommended
| Field | Type | Notes |
|---|---|---|
| revision_history | list | Track changes over time |
| contact_info | string | Point of contact for SLA |

## ID Pattern
^p11_sla_[a-z][a-z0-9_]+.md$

## Body Structure
1. **Service Level Objectives (SLOs)**
   Define measurable targets for uptime, response time, and resolution time.

2. **Compliance and Legal Requirements**
   List regulatory standards, data protection clauses, and audit procedures.

3. **SLA Renewal and Termination**
   Outline conditions for contract extension, breach penalties, and exit clauses.

4. **Performance Metrics and Reporting**
   Specify KPIs, reporting cadence, and tools for monitoring and transparency.

5. **Escalation Procedures**
   Detail steps for resolving service disruptions, including contact hierarchies and timelines.

## Constraints
- ID must match ^p11_sla_[a-z][a-z0-9_]+.md$ exactly.
- All required fields must be present and non-null.
- Version must follow semantic versioning (e.g., `1.2.3`).
- Compliance_requirements must include at least one item.
- Quality must be assigned by peer review, not self-assigned.
- File size must not exceed 6144 bytes.
