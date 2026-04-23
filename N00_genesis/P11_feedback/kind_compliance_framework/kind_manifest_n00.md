---
id: n00_compliance_framework_manifest
kind: knowledge_card
pillar: P11
nucleus: n00
title: "Compliance Framework -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, compliance_framework, p11, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_safety_policy
  - bld_schema_search_strategy
  - bld_schema_usage_report
  - bld_schema_integration_guide
  - bld_schema_compliance_framework
  - bld_schema_voice_pipeline
  - bld_schema_reranker_config
  - bld_schema_action_paradigm
  - bld_schema_quickstart_guide
  - bld_schema_multimodal_prompt
---

<!-- 8F: F1=knowledge_card P11 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A compliance_framework provides regulatory mapping and attestation documentation for AI systems, establishing which regulations apply, how the system satisfies each requirement, and what evidence artifacts demonstrate compliance. It is the master regulatory register that compliance_checklist and conformity_assessment items derive from.

## Pillar
P11 -- feedback

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `compliance_framework` |
| pillar | string | yes | Always `P11` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| regulations | array | yes | List of applicable regulations with jurisdiction and version |
| applicability_scope | string | yes | Which systems/nuclei this framework covers |
| control_mapping | array | yes | Maps regulation articles to CEX artifacts/controls |
| attestation_owner | string | yes | DRI (directly responsible individual or nucleus) |
| last_reviewed | date | yes | Date of most recent framework review |
| next_review | date | yes | Scheduled next review date |

## When to use
- When establishing the regulatory baseline for a new CEX deployment
- When a new regulation (e.g. EU AI Act) requires mapping to existing controls
- When preparing for enterprise sales requiring compliance documentation

## Builder
`archetypes/builders/compliance_framework-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind compliance_framework --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: cf_eu_ai_act_cex_v1
kind: compliance_framework
pillar: P11
nucleus: n07
title: "Example Compliance Framework"
version: 1.0
quality: null
---
# EU AI Act Compliance Framework
regulations: [{name: EU_AI_Act, jurisdiction: EU, version: "2024/1689"}]
applicability_scope: "all CEX nuclei handling personal data"
attestation_owner: n07
last_reviewed: "2026-04-17"
```

## Related kinds
- `compliance_checklist` (P11) -- operational checklist derived from this framework
- `conformity_assessment` (P11) -- EU AI Act-specific assessment under this framework
- `ai_rmf_profile` (P11) -- NIST RMF mapping complementing regulatory framework

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_safety_policy]] | upstream | 0.49 |
| [[bld_schema_search_strategy]] | upstream | 0.48 |
| [[bld_schema_usage_report]] | upstream | 0.46 |
| [[bld_schema_integration_guide]] | upstream | 0.46 |
| [[bld_schema_compliance_framework]] | upstream | 0.46 |
| [[bld_schema_voice_pipeline]] | upstream | 0.45 |
| [[bld_schema_reranker_config]] | upstream | 0.45 |
| [[bld_schema_action_paradigm]] | upstream | 0.44 |
| [[bld_schema_quickstart_guide]] | upstream | 0.44 |
| [[bld_schema_multimodal_prompt]] | upstream | 0.44 |
