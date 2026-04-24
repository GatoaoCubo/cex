---
id: n00_safety_hazard_taxonomy_manifest
kind: knowledge_card
8f: F3_inject
pillar: P11
nucleus: n00
title: "Safety Hazard Taxonomy -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, safety_hazard_taxonomy, p11, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_safety_hazard_taxonomy
  - p03_sp_safety_hazard_taxonomy_builder
  - safety-hazard-taxonomy-builder
  - bld_collaboration_safety_hazard_taxonomy
  - bld_schema_multimodal_prompt
  - bld_schema_reranker_config
  - bld_schema_search_strategy
  - bld_schema_dataset_card
  - bld_schema_integration_guide
  - bld_schema_usage_report
---

<!-- 8F: F1=knowledge_card P11 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A safety_hazard_taxonomy defines the structured classification of AI safety hazards using industry standards such as MLCommons AILuminate or Llama Guard taxonomies. It is the canonical hazard vocabulary that content_filter, guardrail, and conformity_assessment artifacts reference when specifying which categories of harm to detect and prevent.

## Pillar
P11 -- feedback

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `safety_hazard_taxonomy` |
| pillar | string | yes | Always `P11` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| taxonomy_source | string | yes | Source standard (MLCommons_AILuminate \| Llama_Guard_3 \| custom) |
| taxonomy_version | string | yes | Version of the source taxonomy |
| categories | array | yes | List of hazard categories with ID, name, description, severity |
| severity_scale | object | yes | Scale definition mapping category to severity level |
| applicable_models | array | no | Models this taxonomy is validated against |
| last_updated | date | yes | Last taxonomy update from source |

## When to use
- When configuring a content_filter or guardrail and selecting hazard categories
- When aligning CEX safety controls with an industry benchmark taxonomy
- When building a conformity_assessment that references specific hazard classes

## Builder
`archetypes/builders/safety_hazard_taxonomy-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind safety_hazard_taxonomy --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: sht_mlcommons_ailuminate_v1
kind: safety_hazard_taxonomy
pillar: P11
nucleus: n07
title: "Example Safety Hazard Taxonomy"
version: 1.0
quality: null
---
# Safety Hazard Taxonomy: MLCommons AILuminate
taxonomy_source: MLCommons_AILuminate
taxonomy_version: "1.0"
categories:
  - id: S1, name: violent_crimes, severity: critical
  - id: S2, name: hate_speech, severity: high
```

## Related kinds
- `guardrail` (P11) -- safety boundary referencing categories from this taxonomy
- `content_filter` (P11) -- filter that maps input/output to these hazard categories
- `threat_model` (P11) -- risk assessment using this taxonomy to classify hazards

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_safety_hazard_taxonomy]] | upstream | 0.53 |
| [[p03_sp_safety_hazard_taxonomy_builder]] | upstream | 0.47 |
| [[safety-hazard-taxonomy-builder]] | related | 0.43 |
| [[bld_collaboration_safety_hazard_taxonomy]] | downstream | 0.43 |
| [[bld_schema_multimodal_prompt]] | upstream | 0.42 |
| [[bld_schema_reranker_config]] | upstream | 0.42 |
| [[bld_schema_search_strategy]] | upstream | 0.41 |
| [[bld_schema_dataset_card]] | upstream | 0.41 |
| [[bld_schema_integration_guide]] | upstream | 0.41 |
| [[bld_schema_usage_report]] | upstream | 0.41 |
