---
kind: output_template
id: bld_output_template_thinking_config
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for thinking_config production
quality: 8.5
title: "Output Template Thinking Config"
version: "1.0.0"
author: wave1_builder_gen
tags: [thinking_config, builder, output_template]
tldr: "Output template for thinking config: frontmatter field guide, required body sections, filled example, and quality gate checklist for extended thinking and budget token settings."
domain: "thinking_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_examples_thinking_config
  - bld_config_thinking_config
  - bld_collaboration_thinking_config
  - thinking-config-builder
  - bld_schema_thinking_config
  - bld_output_template_dataset_card
  - bld_instruction_thinking_config
  - p03_sp_thinking_config_builder
  - p11_qg_thinking_config
  - bld_memory_thinking_config
---

This ISO configures a thinking budget: how many tokens the model may spend on internal reasoning before emitting.

```yaml
name: {{name}}
description: {{description}}
version: {{version}}
author: {{author}}
date: {{date}}

objectives:
  - {{objective_1}}
  - {{objective_2}}

steps:
  - {{step_1}}
  - {{step_2}}

constraints:
  - {{constraint_1}}
  - {{constraint_2}}

outputs:
  - {{output_1}}
  - {{output_2}}
```

## Quality Gate Checklist

| Gate | Check | Pass Condition |
|------|-------|---------------|
| H01 | Frontmatter complete | All required fields present with valid types |
| H02 | ID matches filename | id field equals filename stem |
| H03 | Naming convention | Follows p09_thk_{{name}}.yaml pattern |
| H04 | Body sections present | All required sections non-empty |
| H05 | Size within limits | Total <= 2048 bytes |
| H06 | No placeholder text | No {{var}} unreplaced |
| H07 | quality: null | Never self-scored |

## Properties

| Property | Value |
|----------|-------|
| Kind | `output` |
| Pillar | P05 |
| Domain | thinking config construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_thinking_config]] | downstream | 0.29 |
| [[bld_config_thinking_config]] | downstream | 0.28 |
| [[bld_collaboration_thinking_config]] | downstream | 0.26 |
| [[thinking-config-builder]] | downstream | 0.24 |
| [[bld_schema_thinking_config]] | downstream | 0.24 |
| [[bld_output_template_dataset_card]] | sibling | 0.23 |
| [[bld_instruction_thinking_config]] | upstream | 0.19 |
| [[p03_sp_thinking_config_builder]] | upstream | 0.18 |
| [[p11_qg_thinking_config]] | downstream | 0.17 |
| [[bld_memory_thinking_config]] | downstream | 0.17 |
