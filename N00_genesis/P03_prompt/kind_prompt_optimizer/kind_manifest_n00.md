---
id: n00_prompt_optimizer_manifest
kind: knowledge_card
pillar: P03
nucleus: n00
title: "Prompt Optimizer -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, prompt_optimizer, p03, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_prompt_optimizer
  - bld_schema_multimodal_prompt
  - bld_schema_reranker_config
  - bld_schema_action_prompt
  - bld_schema_integration_guide
  - bld_schema_benchmark_suite
  - bld_schema_usage_report
  - bld_schema_kind
  - bld_schema_prompt_technique
  - bld_schema_search_strategy
---

<!-- 8F: F1=knowledge_card P03 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A prompt_optimizer is an automated prompt improvement and compilation tool that analyzes existing prompt artifacts, identifies inefficiencies (redundancy, ambiguity, token waste), and produces improved versions with measurable quality gains. It applies DSPy-style prompt compilation patterns and CEX quality gates to iteratively refine prompts. The output is an optimized prompt artifact with a before/after quality delta report.

## Pillar
P03 -- prompt

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `prompt_optimizer` |
| pillar | string | yes | Always `P03` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| target_prompt_id | string | yes | ID of the prompt artifact to optimize |
| optimization_axes | list | yes | What to improve: clarity, density, token_efficiency, specificity |
| quality_delta_target | float | yes | Minimum improvement score required (e.g. 0.5 points) |
| max_iterations | integer | no | Maximum optimization cycles before accepting best result |

## When to use
- When an existing prompt_template or system_prompt produces inconsistent or low-quality outputs
- When running the `cex_prompt_optimizer.py` tool to batch-improve builder ISOs
- When F7 GOVERN scores reveal prompt-level root causes for quality failures

## Builder
`archetypes/builders/prompt_optimizer-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind prompt_optimizer --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: po_system_prompt_n03_v1
kind: prompt_optimizer
pillar: P03
nucleus: n03
title: "N03 System Prompt Optimizer"
version: 1.0
quality: null
---
target_prompt_id: sp_n03_engineering_v1
optimization_axes: [clarity, token_efficiency, specificity]
quality_delta_target: 0.5
max_iterations: 3
```

## Related kinds
- `prompt_template` (P03) -- primary artifact type that prompt_optimizer improves
- `prompt_version` (P03) -- version snapshot created after each optimization cycle
- `quality_gate` (P07) -- evaluation gate that measures optimization success
- `learning_record` (P11) -- captures patterns discovered during optimization

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_prompt_optimizer]] | downstream | 0.41 |
| [[bld_schema_multimodal_prompt]] | downstream | 0.40 |
| [[bld_schema_reranker_config]] | downstream | 0.39 |
| [[bld_schema_action_prompt]] | downstream | 0.39 |
| [[bld_schema_integration_guide]] | downstream | 0.38 |
| [[bld_schema_benchmark_suite]] | downstream | 0.38 |
| [[bld_schema_usage_report]] | downstream | 0.37 |
| [[bld_schema_kind]] | downstream | 0.37 |
| [[bld_schema_prompt_technique]] | downstream | 0.37 |
| [[bld_schema_search_strategy]] | downstream | 0.37 |
