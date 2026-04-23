---
id: n00_conformity_assessment_manifest
kind: knowledge_card
pillar: P11
nucleus: n00
title: "Conformity Assessment -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, conformity_assessment, p11, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_safety_policy
  - bld_schema_benchmark_suite
  - bld_schema_diff_strategy
  - bld_schema_reranker_config
  - bld_schema_usage_report
  - bld_schema_optimizer
  - bld_schema_multimodal_prompt
  - bld_schema_dataset_card
  - bld_schema_customer_segment
  - bld_schema_pitch_deck
---

<!-- 8F: F1=knowledge_card P11 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A conformity_assessment is an EU AI Act Annex IV conformity assessment for high-risk AI systems, documenting system description, risk mitigation measures, validation testing, accuracy metrics, and post-market monitoring plans. It is the mandatory governance artifact for EU market access of high-risk AI systems under Regulation (EU) 2024/1689.

## Pillar
P11 -- feedback

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `conformity_assessment` |
| pillar | string | yes | Always `P11` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| system_description | string | yes | General AI system description per Annex IV |
| risk_category | enum | yes | high_risk \| limited_risk \| minimal_risk |
| intended_purpose | string | yes | Specific intended purpose per Annex IV |
| risk_measures | array | yes | Implemented risk mitigation measures |
| accuracy_metrics | object | yes | Performance benchmarks and accuracy measures |
| human_oversight | string | yes | Human-in-the-loop provisions |
| notified_body | string | no | EU notified body reference if third-party assessment |

## When to use
- When deploying a high-risk AI system in EU markets
- When a CEX nucleus is used in areas listed in Annex III of the EU AI Act
- When preparing technical documentation for CE marking of an AI product

## Builder
`archetypes/builders/conformity_assessment-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind conformity_assessment --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: ca_eu_ai_act_n01_intelligence
kind: conformity_assessment
pillar: P11
nucleus: n01
title: "Example Conformity Assessment"
version: 1.0
quality: null
---
# EU AI Act Annex IV: N01 Intelligence System
risk_category: high_risk
intended_purpose: "AI-assisted business intelligence and competitive analysis"
human_oversight: "All outputs reviewed by human analyst before business decisions"
```

## Related kinds
- `compliance_framework` (P11) -- regulatory framework this assessment operates within
- `gpai_technical_doc` (P11) -- GPAI technical documentation complementing this assessment
- `threat_model` (P11) -- risk assessment aligned with EU AI Act risk measures

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_safety_policy]] | upstream | 0.46 |
| [[bld_schema_benchmark_suite]] | upstream | 0.46 |
| [[bld_schema_diff_strategy]] | upstream | 0.46 |
| [[bld_schema_reranker_config]] | upstream | 0.46 |
| [[bld_schema_usage_report]] | upstream | 0.46 |
| [[bld_schema_optimizer]] | upstream | 0.45 |
| [[bld_schema_multimodal_prompt]] | upstream | 0.45 |
| [[bld_schema_dataset_card]] | upstream | 0.45 |
| [[bld_schema_customer_segment]] | upstream | 0.44 |
| [[bld_schema_pitch_deck]] | upstream | 0.44 |
