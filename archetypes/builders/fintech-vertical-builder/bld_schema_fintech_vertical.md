---
kind: schema
id: bld_schema_fintech_vertical
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for fintech_vertical
quality: 9.1
title: "Schema Fintech Vertical"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [fintech_vertical, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for fintech_vertical"
domain: "fintech_vertical construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Frontmatter Fields
### Required
| Field      | Type   | Required | Default | Notes                              |
|------------|--------|----------|---------|------------------------------------|
| id         | string | yes      | null    | Must match ID Pattern              |
| kind       | string | yes      | null    | Always "fintech_vertical"          |
| pillar     | string | yes      | null    | Always "P01"                       |
| title      | string | yes      | null    | Descriptive name                   |
| version    | string | yes      | "1.0"   | Semantic versioning                |
| created    | date   | yes      | null    | ISO 8601                           |
| updated    | date   | yes      | null    | ISO 8601                           |
| author     | string | yes      | null    | Owner                              |
| domain     | string | yes      | null    | Fintech subdomain (e.g., "payments") |
| quality    | null   | yes      | null    | Never self-score; peer review assigns |
| tags       | array  | yes      | []      | Keywords                           |
| tldr       | string | yes      | null    | Summary                            |
| service_type | string | yes | null | E.g., "neobanking", "lending" |
| regulatory_scope | string | yes | null | E.g., "global", "EU-only" |

### Recommended
| Field              | Type   | Notes                          |
|--------------------|--------|--------------------------------|
| compliance_status  | string | E.g., "ISO 27001 certified"    |
| user_base          | string | E.g., "B2B", "B2C", "B2B2C"    |
| integration_support| array  | E.g., ["API", "SDK"]           |
| security_standards | array  | E.g., ["PCI-DSS", "GDPR"]      |

## ID Pattern
^p01_fv_[a-z][a-z0-9_]+.md$

## Body Structure
1. **Service Offering**
   - Core financial products/services
   - Target audience (e.g., SMEs, consumers)

2. **Regulatory Compliance**
   - Jurisdictions served
   - Certifications/standards met

3. **Technology Stack**
   - Key platforms, APIs, or infrastructure

4. **Integration Capabilities**
   - Third-party tools supported
   - Onboarding processes

5. **Risk Profile**
   - Operational, legal, or cybersecurity risks

6. **Growth Metrics**
   - User growth, transaction volume, or revenue

## Constraints
- ID must be unique and match the ID Pattern
- All required fields must be present and valid
- Version must follow semantic versioning (e.g., "1.2.3")
- Regulatory_scope must align with domain-specific compliance
- Quality must be assigned by peer review, not self-reported
- service_type must be from a predefined list (e.g., "payments", "lending")
