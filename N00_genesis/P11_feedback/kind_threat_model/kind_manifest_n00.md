---
id: n00_threat_model_manifest
kind: knowledge_card
pillar: P11
nucleus: n00
title: "Threat Model -- Canonical Manifest"
version: 1.0
quality: null
tags: [manifest, threat_model, p11, n00, archetype, template]
---

<!-- 8F: F1=knowledge_card P11 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A threat_model provides a structured hazard and risk assessment for AI systems, identifying attack surfaces, threat actors, potential failure modes, and mitigating controls. It enables systematic security and safety engineering by making implicit risks explicit and traceable to specific mitigations within the CEX architecture.

## Pillar
P11 -- feedback

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `threat_model` |
| pillar | string | yes | Always `P11` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| system_scope | string | yes | System or component being modeled |
| threat_actors | array | yes | Actors with motivation, capability, and access level |
| assets | array | yes | Assets being protected (data, models, APIs, infrastructure) |
| threats | array | yes | Identified threats with ID, description, STRIDE category, likelihood, impact |
| mitigations | array | yes | Controls mapped to each threat with status |
| residual_risk | enum | yes | acceptable \| monitor \| remediate \| accept |
| review_date | date | yes | Date of most recent threat model review |

## When to use
- When designing a new nucleus or integration that handles sensitive data
- When preparing for security review as part of SOC2 or EU AI Act compliance
- When investigating an incident and tracing it back to an identified threat

## Builder
`archetypes/builders/threat_model-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind threat_model --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: tm_cex_api_surface
kind: threat_model
pillar: P11
nucleus: n05
title: "Example Threat Model"
version: 1.0
quality: null
---
# Threat Model: CEX API Surface
system_scope: "CEX public API endpoints"
residual_risk: monitor
threats:
  - id: T1, description: "Prompt injection via user input", category: Tampering, likelihood: high
mitigations:
  - threat: T1, control: content_filter, status: implemented
```

## Related kinds
- `guardrail` (P11) -- mitigation controls referenced in this threat model
- `safety_hazard_taxonomy` (P11) -- taxonomy used to classify threat categories
- `ai_rmf_profile` (P11) -- RMF MAP function that aligns with threat identification
