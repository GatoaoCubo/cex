---
id: n00_healthcare_vertical_manifest
kind: knowledge_card
pillar: P01
nucleus: n00
title: "Healthcare Vertical -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, healthcare_vertical, p01, n00, archetype, template]
density_score: 1.0
---

<!-- 8F: F1=knowledge_card P01 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Healthcare Vertical packages domain knowledge for the Health Technology and clinical sector: HIPAA/LGPD compliance requirements, clinical terminology (ICD-10, HL7 FHIR), KPIs for hospital and health plan operators, and buyer personas. Enables nuclei to generate compliance-aware healthcare content and analyses without repeated domain briefing.

## Pillar
P01 -- Knowledge

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `healthcare_vertical` |
| pillar | string | yes | Always `P01` |
| title | string | yes | Vertical name and care setting |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| sub_verticals | list | no | Hospital, health plan, pharma, digital health |
| key_kpis | list | yes | Patient NPS, readmission rate, cost per claim |
| regulatory | list | yes | HIPAA, LGPD, ANVISA, CFM, HL7 FHIR |
| standards | list | no | ICD-10, SNOMED CT, LOINC, CID-10 |
| buyer_personas | list | yes | CMO, hospital CIO, health plan director |

## When to use
- When building AI solutions for healthcare or clinical environments
- When generating HIPAA/LGPD-compliant content or workflows
- When analyzing digital health market opportunities

## Builder
`archetypes/builders/healthcare_vertical-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind healthcare_vertical --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this (N01, N06)
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- healthcare operators, clinical IT teams
- `{{DOMAIN_CONTEXT}}` -- care setting and clinical specialty

## Example (minimal)
```yaml
---
id: healthcare_vertical_digital_health_brazil
kind: healthcare_vertical
pillar: P01
nucleus: n01
title: "Digital Health Brazil"
version: 1.0
quality: null
---
sub_verticals: [telemedicine, health_plan, hospital]
key_kpis: [patient_NPS, readmission_rate, cost_per_claim]
regulatory: [LGPD, CFM_telemedicine, ANVISA]
standards: [CID-10, HL7_FHIR, TISS]
buyer_personas: [hospital_CIO, health_plan_director]
```

## Related kinds
- `context_doc` (P01) -- broader clinical domain context
- `legal_vertical` (P01) -- regulatory and compliance overlap
- `customer_segment` (P02) -- healthcare ICPs
