---
id: n00_compliance_checklist_manifest
kind: knowledge_card
pillar: P11
nucleus: n00
title: "Compliance Checklist -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, compliance_checklist, p11, n00, archetype, template]
density_score: 1.0
---

<!-- 8F: F1=knowledge_card P11 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A compliance_checklist provides a structured checklist for SOC2, GDPR, HIPAA, or EU AI Act audits, mapping specific controls to evidence artifacts and pass/fail status. It enables compliance teams and AI systems to systematically verify that all required controls are implemented, documented, and tested before an audit.

## Pillar
P11 -- feedback

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `compliance_checklist` |
| pillar | string | yes | Always `P11` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| framework | array | yes | Frameworks covered (SOC2 \| GDPR \| HIPAA \| EU_AI_ACT) |
| controls | array | yes | List of control items with ID, description, evidence_ref, status |
| audit_date | date | no | Target audit date |
| owner | string | yes | Role or nucleus responsible for this checklist |
| pass_count | integer | no | Controls passing (computed) |
| fail_count | integer | no | Controls failing (computed) |

## When to use
- Before an external compliance audit (SOC2, GDPR, HIPAA)
- When onboarding a new enterprise customer requiring compliance attestation
- When implementing EU AI Act requirements for high-risk AI systems

## Builder
`archetypes/builders/compliance_checklist-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind compliance_checklist --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: cc_soc2_type2_2026
kind: compliance_checklist
pillar: P11
nucleus: n05
title: "Example Compliance Checklist"
version: 1.0
quality: null
---
# SOC2 Type II Compliance Checklist
framework: [SOC2]
owner: n05
controls:
  - id: CC6.1, description: "Logical access controls", evidence_ref: al_cex_soc2_production, status: pass
```

## Related kinds
- `audit_log` (P11) -- evidence artifact referenced by compliance controls
- `compliance_framework` (P11) -- framework mapping that feeds checklist structure
- `conformity_assessment` (P11) -- EU AI Act specific assessment complementing this checklist
