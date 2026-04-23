---
id: p11_schema_curation_nudge
kind: validation_schema
pillar: P11
llm_function: CONSTRAIN
purpose: F1 CONSTRAIN schema for curation_nudge artifacts
quality: 8.5
title: "Schema: Curation Nudge"
version: "1.0.0"
author: n03_hermes_w1_8
tags: [schema, curation_nudge, builder, p11, memory, hermes]
domain: "curation_nudge construction"
created: "2026-04-18"
updated: "2026-04-18"
density_score: 0.90
related:
  - p06_schema_env_contract
  - p03_ch_content_pipeline
  - p06_schema_health_response
  - p03_ch_kc_to_notebooklm
  - bld_examples_workflow_primitive
  - bld_schema_validation_schema
  - n06_schema_brand_config
  - bld_schema_model_registry
  - bld_schema_input_schema
  - bld_output_template_function_def
---

## Frontmatter Schema

```yaml
id:
  type: string
  required: true
  pattern: "^cn_[a-z0-9_]+$"
  example: "cn_turn_count"

kind:
  type: string
  required: true
  const: "curation_nudge"

pillar:
  type: string
  required: true
  const: "P11"

title:
  type: string
  required: true
  pattern: "^Curation Nudge: .+"

trigger:
  type: object
  required: true
  properties:
    type:
      type: string
      required: true
      enum: [turn_count, density_threshold, tool_call_count, user_correction]
    threshold:
      type: integer
      required: true
      minimum: 5
      default: 10
      note: "Minimum 5 to prevent spam. user_correction may use 1."

cadence:
  type: object
  required: true
  properties:
    min_interval_turns:
      type: integer
      required: true
      minimum: 1
      default: 5
    max_per_session:
      type: integer
      required: true
      minimum: 1
      maximum: 10
      default: 3

prompt_template:
  type: string
  required: true
  must_contain: ["{{observation}}"]
  note: "Runtime substitutes {{observation}} with the specific knowledge fragment"

target_memory:
  type: object
  required: true
  properties:
    destination:
      type: string
      required: true
      enum: [MEMORY.md, entity_memory, knowledge_card]
    auto_write_if_confirmed:
      type: boolean
      required: true
      default: true

version:
  type: string
  required: true
  pattern: "^[0-9]+\\.[0-9]+\\.[0-9]+$"

quality:
  type: null
  required: true
  const: null

tags:
  type: array
  required: true
  items:
    type: string
  must_include: [hermes_origin, nudge, proactive, memory]

upstream_source:
  type: string
  required: false
  example: "NousResearch/hermes-agent"
```

## Naming Convention
```
p11_cn_{{trigger_type}}.yaml
```
Where `trigger_type` is a lowercase slug (e.g., `turn_count`, `density_threshold`, `user_correction`).

## Size Constraint
- Max bytes: 2048
- Target density: >= 0.85 (tables and structured content preferred over prose)

## HARD Gates
| ID | Check |
|----|-------|
| H01 | `kind == "curation_nudge"` |
| H02 | `trigger.threshold >= 5` (positive integer, minimum 5) |
| H03 | `trigger.type` in `{turn_count, density_threshold, tool_call_count, user_correction}` |
| H04 | `target_memory.destination` in `{MEMORY.md, entity_memory, knowledge_card}` |
| H05 | `prompt_template` contains `{{observation}}` |
| H06 | `quality == null` |

## Body Sections (required)
1. `## Nudge: {{trigger}}` -- human-readable name
2. `### Trigger Configuration` -- parameter table
3. `### Prompt Template` -- code block with template text
4. `### Target Memory` -- destination and auto-write config
5. `### Boundaries` -- NOT-items (4 minimum)
6. `### Usage in agent session` -- code block

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p06_schema_env_contract]] | upstream | 0.42 |
| [[p03_ch_content_pipeline]] | upstream | 0.31 |
| [[p06_schema_health_response]] | upstream | 0.30 |
| [[p03_ch_kc_to_notebooklm]] | upstream | 0.30 |
| [[bld_examples_workflow_primitive]] | upstream | 0.30 |
| [[bld_schema_validation_schema]] | upstream | 0.29 |
| [[n06_schema_brand_config]] | upstream | 0.27 |
| [[bld_schema_model_registry]] | upstream | 0.27 |
| [[bld_schema_input_schema]] | upstream | 0.27 |
| [[bld_output_template_function_def]] | upstream | 0.26 |
