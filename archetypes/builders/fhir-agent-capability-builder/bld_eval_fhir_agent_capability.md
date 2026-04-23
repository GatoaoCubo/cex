---
kind: quality_gate
id: p08_qg_fhir_agent_capability
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for fhir_agent_capability
quality: 9.0
title: "Quality Gate FHIR Agent Capability"
version: "1.0.0"
author: n06_wave7
tags: [fhir_agent_capability, builder, quality_gate, fhir, hl7, hipaa]
tldr: "Quality gate with HARD and SOFT scoring for fhir_agent_capability"
domain: "fhir_agent_capability construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_examples_fhir_agent_capability
  - bld_instruction_fhir_agent_capability
  - p03_sp_fhir_agent_capability_builder
  - bld_schema_fhir_agent_capability
  - bld_knowledge_card_fhir_agent_capability
  - p10_lr_fhir_agent_capability_builder
  - bld_output_template_fhir_agent_capability
  - fhir-agent-capability-builder
  - kc_fhir_agent_capability
  - bld_tools_fhir_agent_capability
---

## Quality Gate

## Definition
| Metric | Threshold | Operator | Scope |
|--------|-----------|----------|-------|
| FHIR capability compliance | 100% | equals | All EHR onboarding registrations |

## HARD Gates
| ID  | Check | Fail Condition |
|-----|-------|----------------|
| H01 | YAML frontmatter valid | Invalid YAML syntax or missing required fields |
| H02 | ID matches `^p08_fhir_[a-z][a-z0-9_]+\.md$` | Pattern mismatch |
| H03 | kind = "fhir_agent_capability" | Kind field incorrect or absent |
| H04 | fhir_version is R5 or R4B | Earlier version or missing |
| H05 | capability_category in HL7 taxonomy | Unrecognized or missing category |
| H06 | smart_scopes follow SMART on FHIR v2 format | Malformed scope strings |
| H07 | phi_handling declared | Missing when patient resources accessed |
| H08 | audit_log_resource present when phi_handling=full-phi | HIPAA compliance gap |

## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|-----|-----------|--------|---------------|
| D01 | Schema completeness (required + recommended fields) | 0.25 | All present = 1.0, missing recommended = 0.7, missing required = 0 |
| D02 | Minimum-privilege scope discipline (no over-scoped permissions) | 0.25 | Least-privilege scopes = 1.0, some over-scope = 0.5, write-all = 0 |
| D03 | PHI-handling depth (retention policy, de-id standard, audit log) | 0.20 | All three = 1.0, two = 0.7, one = 0.3, missing = 0 |
| D04 | CDS Hooks integration (hook IDs, context, prefetch) | 0.15 | Full spec = 1.0, partial = 0.5, absent (CDS use case) = 0 |
| D05 | AI Transparency extension (model_id, training statement) | 0.15 | Complete = 1.0, partial = 0.5, missing = 0 |

## Actions
| Label | Score | Action |
|-------|-------|--------|
| GOLDEN  | >= 9.5 | Auto-register with FHIR server registry |
| PUBLISH | >= 8.0 | Register after compliance review |
| REVIEW  | >= 7.0 | Manual review by healthcare compliance team |
| REJECT  | < 7.0  | Return to builder; HIPAA risk flagged |

## Bypass
| Condition | Approver | Audit Trail |
|-----------|----------|-------------|
| Research/sandbox environment (no real PHI) | Healthcare AI Lead | Sandbox declaration + IRB number |

## Examples

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

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
