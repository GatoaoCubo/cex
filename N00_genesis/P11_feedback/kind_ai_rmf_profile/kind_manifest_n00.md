---
id: n00_ai_rmf_profile_manifest
kind: knowledge_card
8f: F3_inject
pillar: P11
nucleus: n00
title: "AI RMF Profile -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, ai_rmf_profile, p11, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_ai_rmf_profile
  - bld_schema_safety_policy
  - bld_schema_multimodal_prompt
  - bld_schema_action_paradigm
  - bld_schema_reranker_config
  - bld_schema_usage_report
  - bld_schema_diff_strategy
  - bld_schema_integration_guide
  - bld_schema_benchmark_suite
  - bld_schema_dataset_card
---

<!-- 8F: F1=knowledge_card P11 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
An ai_rmf_profile is a NIST AI Risk Management Framework profile artifact that maps an AI system's controls and practices to the four core functions: GOVERN, MAP, MEASURE, and MANAGE. It documents organizational accountability, risk identification, risk quantification, and mitigation actions required for responsible AI governance.

## Pillar
P11 -- feedback

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `ai_rmf_profile` |
| pillar | string | yes | Always `P11` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| system_name | string | yes | Name of the AI system being profiled |
| rmf_version | string | yes | NIST AI RMF version (e.g. "1.0") |
| govern_controls | array | yes | GOVERN function: policies, roles, accountability |
| map_controls | array | yes | MAP function: risk context, categorization |
| measure_controls | array | yes | MEASURE function: metrics, testing, monitoring |
| manage_controls | array | yes | MANAGE function: treatment, response, recovery |
| profile_tier | enum | yes | informative \| normative \| organizational |

## When to use
- When preparing an AI system for enterprise procurement requiring NIST AI RMF compliance
- When documenting risk governance for a high-risk AI system
- When aligning CEX nucleus operations with federal AI policy requirements

## Builder
`archetypes/builders/ai_rmf_profile-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind ai_rmf_profile --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: rmf_cex_enterprise_v1
kind: ai_rmf_profile
pillar: P11
nucleus: n07
title: "Example AI RMF Profile"
version: 1.0
quality: null
---
# NIST AI RMF 1.0 Profile: CEX Enterprise
system_name: CEX Enterprise Brain
rmf_version: "1.0"
profile_tier: normative
govern_controls: [{control: AI-GOV-01, status: implemented}]
```

## Related kinds
- `compliance_framework` (P11) -- broader regulatory mapping that RMF profile fits within
- `threat_model` (P11) -- hazard assessment aligned with MAP function
- `safety_policy` (P11) -- organizational safety rules aligned with GOVERN function

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_ai_rmf_profile]] | upstream | 0.52 |
| [[bld_schema_safety_policy]] | upstream | 0.47 |
| [[bld_schema_multimodal_prompt]] | upstream | 0.46 |
| [[bld_schema_action_paradigm]] | upstream | 0.45 |
| [[bld_schema_reranker_config]] | upstream | 0.45 |
| [[bld_schema_usage_report]] | upstream | 0.44 |
| [[bld_schema_diff_strategy]] | upstream | 0.44 |
| [[bld_schema_integration_guide]] | upstream | 0.44 |
| [[bld_schema_benchmark_suite]] | upstream | 0.43 |
| [[bld_schema_dataset_card]] | upstream | 0.43 |
