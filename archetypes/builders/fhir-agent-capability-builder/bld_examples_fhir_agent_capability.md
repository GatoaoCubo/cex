---
kind: examples
id: bld_examples_fhir_agent_capability
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of fhir_agent_capability artifacts
quality: 9.1
title: "Examples FHIR Agent Capability"
version: "1.0.0"
author: n06_wave7
tags: [fhir_agent_capability, builder, examples, fhir, hl7, smart-on-fhir]
tldr: "Golden and anti-examples of fhir_agent_capability artifacts"
domain: "fhir_agent_capability construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Golden Example

```markdown
---
id: p08_fhir_cds_sepsis_early_warning.md
kind: fhir_agent_capability
pillar: P08
fhir_version: R5
capability_category: CDS
smart_scopes:
  - "patient/Patient.read"
  - "patient/Observation.read"
  - "patient/Condition.read"
phi_handling: full-phi
phi_retention_policy: "Session-only; no data retained after encounter close. HIPAA minimum necessary standard."
audit_log_resource: "hl7.fhir.r5.extensions#AuditEvent-AI-influence"
ai_transparency_ref: "hl7.fhir.uv.aiTransparency#AIObservation"
cds_hooks: ["patient-view", "order-sign"]
quality: null
---

## Capability Overview
**Clinical Function**: Real-time sepsis early warning scoring for ICU patients using NEWS2 + qSOFA criteria.
**HL7 AI Office Category**: CDS (Clinical Decision Support)
**Patient Population**: Adult ICU inpatients (18+)

## SMART on FHIR Authorization
| Scope | Resource | Action | Justification |
|-------|----------|--------|---------------|
| patient/Patient.read | Patient | read | Demographics for age/weight-adjusted thresholds |
| patient/Observation.read | Observation | read | Vital signs: HR, RR, SpO2, temperature, BP |
| patient/Condition.read | Condition | read | Active diagnoses for comorbidity adjustment |

## PHI-Handling Declaration
- **PHI Handling Level**: full-phi
- **Data Retention**: Session-only, HIPAA minimum necessary
- **De-identification**: Not applicable (real-time CDS, no storage)
- **Audit Log**: AuditEvent-AI-influence extension on every CDS trigger
```

## Anti-Example 1: Over-scoped Permissions

```markdown
smart_scopes:
  - "system/*.read"
  - "system/*.write"
```

**Why it fails**: Violates minimum-privilege principle (D02 = 0). SMART on FHIR v2 prohibits wildcard scopes for AI agents unless approved by the FHIR server administrator for specific system-level use cases. This scope grants read/write to ALL FHIR resources, exposing unrelated patient data.

## Anti-Example 2: Missing PHI Declaration

```markdown
---
fhir_version: R5
capability_category: summarization
smart_scopes: ["patient/Patient.read", "patient/DocumentReference.read"]
# phi_handling: MISSING
---
Summarizes patient discharge notes.
```

**Why it fails**: H07 (PHI-handling required). The agent reads Patient and DocumentReference resources containing PHI. Missing phi_handling declaration means no retention policy, no audit log, and no HIPAA compliance basis. Fails HARD gate H07 and HARD gate H08.

## Anti-Example 3: Wrong FHIR Version

```markdown
---
fhir_version: R4  <!-- INVALID: only R5 and R4B supported -->
capability_category: coding
smart_scopes: ["patient/Condition.read"]
---
Maps diagnoses to ICD-10 codes.
```

**Why it fails**: H04. FHIR R4 lacks the AI agent resource extensions introduced in R4B/R5. Declaring R4 means the AI Transparency and Agent-as-Resource patterns cannot be applied, making the capability declaration incompatible with HL7 AI Office 2025 requirements.
