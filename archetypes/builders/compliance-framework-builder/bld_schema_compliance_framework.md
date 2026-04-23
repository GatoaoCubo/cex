---
kind: schema
id: bld_schema_compliance_framework
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for compliance_framework
quality: 9.1
title: "Schema Compliance Framework"
version: "1.0.0"
author: wave1_builder_gen
tags: [compliance_framework, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for compliance_framework"
domain: "compliance_framework construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_schema_safety_policy
  - bld_schema_sandbox_config
  - bld_schema_pitch_deck
  - bld_schema_compliance_checklist
  - bld_schema_usage_report
  - bld_schema_reranker_config
  - bld_schema_benchmark_suite
  - bld_schema_dataset_card
  - bld_schema_agent_profile
  - bld_schema_quickstart_guide
---

## Frontmatter Fields
### Required
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string | yes | - | Regex: ^p11_cfw_[a-zA-Z0-9_]+\.md$ |
| kind | string | yes | "compliance_framework" | - |
| pillar | string | yes | "P11" | - |
| title | string | yes | - | - |
| version | string | yes | "1.0" | - |
| created | datetime | yes | - | ISO 8601 format |
| updated | datetime | yes | - | ISO 8601 format |
| author | string | yes | - | - |
| domain | string | yes | - | e.g., "anti-money laundering" |
| quality | string | yes | "draft" | Options: draft, reviewed, approved |
| tags | list | yes | [] | - |
| tldr | string | yes | - | Summary of framework |
| regulatory_scope | string | yes | - | Jurisdictional and legal boundaries |
| enforcement_mechanisms | string | yes | - | Penalties and corrective actions |

### Recommended
| Field | Type | Notes |
|-------|------|-------|
| last_reviewed | datetime | ISO 8601 format |
| compliance_officer | string | - |
| audit_frequency | string | e.g., "quarterly" |

## ID Pattern
^p11_cfw_[a-zA-Z0-9_]+\.md$

## Body Structure
1. **Overview**
   - Purpose, scope, and stakeholders of the framework.

2. **Regulatory Scope**
   - Legal requirements, jurisdictions, and applicable regulations.

3. **Compliance Mechanisms**
   - Policies, procedures, and controls to ensure adherence.

4. **Audit and Monitoring**
   - Frequency, methodology, and reporting of audits.

5. **Enforcement and Remediation**
   - Consequences of non-compliance and corrective actions.

6. **Stakeholder Roles**
   - Responsibilities of compliance officers, auditors, and executives.

## Constraints
- All required fields must be present and valid.
- ID must conform to the regex pattern.
- Version must follow semantic versioning (e.g., "1.0.0").
- Regulatory_scope and enforcement_mechanisms must be non-empty.
- Audit_frequency must be a valid time interval (e.g., "monthly").
- Tags must be unique and lowercase.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_safety_policy]] | sibling | 0.73 |
| [[bld_schema_sandbox_config]] | sibling | 0.71 |
| [[bld_schema_pitch_deck]] | sibling | 0.69 |
| [[bld_schema_compliance_checklist]] | sibling | 0.69 |
| [[bld_schema_usage_report]] | sibling | 0.69 |
| [[bld_schema_reranker_config]] | sibling | 0.69 |
| [[bld_schema_benchmark_suite]] | sibling | 0.68 |
| [[bld_schema_dataset_card]] | sibling | 0.68 |
| [[bld_schema_agent_profile]] | sibling | 0.67 |
| [[bld_schema_quickstart_guide]] | sibling | 0.66 |
