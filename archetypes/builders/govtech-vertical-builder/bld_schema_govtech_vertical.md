---
kind: schema
id: bld_schema_govtech_vertical
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for govtech_vertical
quality: 9.1
title: "Schema Govtech Vertical"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [govtech_vertical, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for govtech_vertical"
domain: "govtech_vertical construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Frontmatter Fields
### Required
| Field | Type | Required | Default | Notes |
|---|---|---|---|---|
| id | string | yes |  | Must match ID Pattern |
| kind | string | yes |  | Always "govtech_vertical" |
| pillar | string | yes |  | Always "P01" |
| title | string | yes |  | Human-readable name |
| version | string | yes | "1.0" | Semantic versioning |
| created | datetime | yes |  | ISO 8601 format |
| updated | datetime | yes |  | ISO 8601 format |
| author | string | yes |  | Owner/organization |
| domain | string | yes |  | Govtech subdomain (e.g., "digital_identity") |
| quality | null | yes | null | Never self-score; peer review assigns |
| tags | list | yes | [] | Keywords for discovery |
| tldr | string | yes |  | Summary in 1 sentence |
| jurisdiction | string | yes |  | Legal territory of application |
| implementation_status | string | yes |  | "draft", "pilot", "live" |

### Recommended
| Field | Type | Notes |
|---|---|---|
| stakeholder | list | Key organizations/roles involved |
| compliance_framework | string | Regulatory standards adhered to |

## ID Pattern
^p01_gv_[a-z][a-z0-9_]+.md$

## Body Structure
1. **Overview**
   - Purpose, scope, and objectives of the govtech initiative.

2. **Jurisdictional Scope**
   - Geopolitical boundaries and legal context.

3. **Implementation Status**
   - Current phase, milestones, and timelines.

4. **Stakeholder Engagement**
   - Partners, users, and governance models.

5. **Compliance Framework**
   - Laws, regulations, and ethical guidelines.

6. **Technical Dependencies**
   - Infrastructure, APIs, and interoperability requirements.

## Constraints
- Jurisdiction must align with ISO 3166-1 alpha-2 codes.
- Compliance_framework must reference official regulatory documents.
- Implementation_status must be one of: "draft", "pilot", "live".
- Tags must include at least one govtech-related keyword.
- tldr must be ≤ 200 characters.
- All datetime fields must use UTC timezone.
