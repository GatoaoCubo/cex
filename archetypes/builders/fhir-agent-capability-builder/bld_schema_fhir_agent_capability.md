---
kind: schema
id: bld_schema_fhir_agent_capability
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for fhir_agent_capability
quality: 9.2
title: "Schema FHIR Agent Capability"
version: "1.0.0"
author: n06_wave7
tags: [fhir_agent_capability, builder, schema, fhir, hl7]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for fhir_agent_capability"
domain: "fhir_agent_capability construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Frontmatter Fields

### Required
| Field                | Type         | Required | Default | Notes |
|----------------------|--------------|----------|---------|-------|
| id                   | string       | yes      |         | Follows ID pattern below |
| kind                 | string       | yes      |         | Must be "fhir_agent_capability" |
| pillar               | string       | yes      |         | Must be "P08" |
| title                | string       | yes      |         | Human-readable capability name |
| version              | string       | yes      |         | Semver |
| created              | date         | yes      |         | ISO 8601 |
| updated              | date         | yes      |         | ISO 8601 |
| author               | string       | yes      |         | Builder or nucleus ID |
| domain               | string       | yes      |         | Healthcare sub-domain |
| quality              | null         | yes      | null    | Never self-score |
| tags                 | array        | yes      |         | Includes capability_category + fhir tags |
| tldr                 | string       | yes      |         | One-line capability description |
| fhir_version         | string       | yes      |         | "R5" or "R4B" |
| capability_category  | string       | yes      |         | CDS/summarization/coding/documentation/scheduling |
| smart_scopes         | array        | yes      |         | SMART on FHIR v2 scope strings |
| phi_handling         | string       | yes      |         | "minimal" / "de-identified" / "full-phi" |

### Recommended
| Field                  | Type   | Notes |
|------------------------|--------|-------|
| cds_hooks              | array  | CDS Hooks hook IDs (patient-view, order-select, etc.) |
| phi_retention_policy   | string | Data retention duration and policy reference |
| audit_log_resource     | string | FHIR AuditEvent extension reference |
| ai_transparency_ref    | string | HL7 AI Transparency extension reference |
| fhir_server_ref        | string | FHIR CapabilityStatement URL |

## ID Pattern
`^p08_fhir_[a-z][a-z0-9_]+\.md$`

Example: `p08_fhir_cds_sepsis_alert.md`, `p08_fhir_summarization_discharge.md`

## Body Structure
1. **Capability Overview** -- clinical function, HL7 category, patient population
2. **FHIR Resource Access** -- resources accessed, CRUD operations, version constraints
3. **SMART on FHIR Authorization** -- scopes table, minimum-privilege rationale
4. **PHI-Handling Declaration** -- retention policy, de-identification standard, audit log
5. **CDS Hooks Integration** -- hook IDs, trigger contexts, prefetch keys
6. **AI Transparency** -- model_id, training_data_statement, explainability_method
7. **EHR Compatibility** -- tested EHR systems, FHIR server URL, conformance notes

## Constraints
- id MUST match the regex pattern exactly.
- fhir_version MUST be "R5" or "R4B" (earlier versions not supported).
- capability_category MUST be from HL7 AI Office taxonomy.
- smart_scopes MUST follow format: `{{system}}/{{resource}}.{{action}}`.
- phi_handling MUST be "full-phi" when accessing Patient.id, Observation, or Condition resources.
- audit_log_resource MUST be present when phi_handling = "full-phi".
