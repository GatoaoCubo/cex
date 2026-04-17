---
id: n00_fhir_agent_capability_manifest
kind: knowledge_card
pillar: P08
nucleus: n00
title: "FHIR Agent Capability -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, fhir_agent_capability, p08, n00, archetype, template]
density_score: 1.0
---

<!-- 8F: F1=knowledge_card P08 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A fhir_agent_capability is an HL7 FHIR R5 conformant AI agent capability declaration for healthcare integrations. It specifies which FHIR resources the agent can read, write, and search; the terminology systems it understands; and the clinical workflow steps it is authorized to execute, enabling compliant deployment in regulated healthcare environments.

## Pillar
P08 -- architecture

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `fhir_agent_capability` |
| pillar | string | yes | Always `P08` |
| title | string | yes | Human-readable capability name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| fhir_version | string | yes | FHIR spec version (e.g. R5, R4B) |
| resources | list | yes | FHIR resource types the agent operates on |
| resources[].type | string | yes | ResourceType (e.g. Patient, Observation) |
| resources[].interactions | list | yes | Allowed: read, write, search, create, delete |
| terminology_systems | list | no | SNOMED, LOINC, ICD-10 etc. |
| workflow_steps | list | no | Clinical workflow steps agent may perform |
| compliance | list | no | Regulatory standards: HIPAA, GDPR, 21CFR11 |

## When to use
- Deploying an AI agent in a healthcare system that must declare FHIR compliance
- Registering agent capabilities with a FHIR server's CapabilityStatement
- Auditing what clinical data an agent is authorized to access

## Builder
`archetypes/builders/fhir_agent_capability-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind fhir_agent_capability --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: fhir_cap_clinical_summary
kind: fhir_agent_capability
pillar: P08
nucleus: n01
title: "Clinical Summary Agent FHIR Capability"
version: 1.0
quality: null
---
fhir_version: R5
resources:
  - type: Patient
    interactions: [read, search]
  - type: Observation
    interactions: [read, search]
terminology_systems: [SNOMED-CT, LOINC]
compliance: [HIPAA]
```

## Related kinds
- `agent_card` (P08) -- the agent_card that references this FHIR capability declaration
- `permission` (P09) -- governs which agents may access which FHIR resource types
- `data_residency` (P09) -- ensures clinical data stays in compliant regions
