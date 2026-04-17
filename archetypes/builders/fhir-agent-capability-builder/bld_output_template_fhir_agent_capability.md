---
kind: output_template
id: bld_output_template_fhir_agent_capability
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for fhir_agent_capability production
quality: 9.1
title: "Output Template FHIR Agent Capability"
version: "1.0.0"
author: n06_wave7
tags: [fhir_agent_capability, builder, output_template, fhir, hl7]
tldr: "Template with vars for fhir_agent_capability production"
domain: "fhir_agent_capability construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

```markdown
---
id: p08_fhir_{{capability_slug}}.md
kind: fhir_agent_capability
pillar: P08
title: "FHIR Agent Capability: {{capability_name}}"
version: "1.0.0"
created: "{{date}}"
updated: "{{date}}"
author: "{{author}}"
domain: "{{healthcare_subdomain}}"
quality: null
tags: [fhir, hl7, {{capability_category}}, smart-on-fhir, healthcare]
tldr: "{{one_line_description}}"
fhir_version: "R5"
capability_category: {{capability_category}}
smart_scopes:
  - "{{scope_1}}"
  - "{{scope_2}}"
phi_handling: {{phi_handling}}
cds_hooks:
  - "{{hook_id_1}}"
phi_retention_policy: "{{retention_policy}}"
audit_log_resource: "{{audit_event_extension_ref}}"
ai_transparency_ref: "{{transparency_extension_ref}}"
fhir_server_ref: "{{capability_statement_url}}"
---

## Capability Overview
**Clinical Function**: {{capability_description}}
**HL7 AI Office Category**: {{capability_category}}
**Patient Population**: {{patient_population}}
**FHIR Version**: R5

| Attribute | Value |
|-----------|-------|
| EHR Integration | {{ehr_integration_method}} |
| Deployment Model | {{deployment_model}} |
| Certification Status | {{certification_status}} |

## FHIR Resource Access
| Resource | Operations | Scope | Notes |
|----------|-----------|-------|-------|
| {{resource_1}} | {{operations_1}} | {{scope_1}} | |
| {{resource_2}} | {{operations_2}} | {{scope_2}} | |
| {{resource_3}} | {{operations_3}} | {{scope_3}} | |

## SMART on FHIR Authorization
**Version**: SMART on FHIR v2
**Authorization Flow**: {{auth_flow}}

| Scope | Resource | Action | Justification |
|-------|----------|--------|---------------|
| {{scope_1}} | {{resource_1}} | {{action_1}} | {{why_needed_1}} |
| {{scope_2}} | {{resource_2}} | {{action_2}} | {{why_needed_2}} |

## PHI-Handling Declaration
- **PHI Handling Level**: {{phi_handling}}
- **Data Retention Policy**: {{retention_policy}}
- **De-identification Standard**: {{deidentification_standard}}
- **Audit Log Resource**: `{{audit_event_extension_ref}}`
- **HIPAA Compliance Notes**: {{hipaa_notes}}

## CDS Hooks Integration
| Hook ID | Trigger Context | Prefetch Keys | Response Type |
|---------|----------------|---------------|---------------|
| {{hook_id_1}} | {{trigger_1}} | {{prefetch_1}} | {{response_type_1}} |

## AI Transparency
- **Model ID**: {{model_id}}
- **Training Data Statement**: {{training_data_statement}}
- **Explainability Method**: {{explainability_method}}
- **Bias Audit Reference**: {{bias_audit_ref}}
- **HL7 AI Transparency Extension**: `{{transparency_extension_ref}}`

## EHR Compatibility
| EHR System | Version | Test Status | Notes |
|------------|---------|-------------|-------|
| {{ehr_1}} | {{ehr_version_1}} | {{test_status_1}} | |
| {{ehr_2}} | {{ehr_version_2}} | {{test_status_2}} | |
```
