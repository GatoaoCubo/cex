---
kind: output_template
id: bld_output_template_prompt_version
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a prompt_version artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
quality: 9.0
title: "Output Template Prompt Version"
version: "1.0.0"
author: n03_builder
tags: [prompt_version, builder, examples]
tldr: "Golden and anti-examples for prompt version construction, demonstrating ideal structure and common pitfalls."
domain: "prompt version construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Output Template: prompt_version
```yaml
id: p03_pv_{{slug}}
kind: prompt_version
pillar: P03
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
name: "{{name}}}}"
prompt_ref: "{{prompt_ref}}}}"
quality: null
tags: [prompt_version, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
description: "{{description}}}}"
metrics: "{{metrics}}}}"
ab_group: "{{ab_group}}}}"
parent_version: "{{parent_version}}}}"
status: "{{status}}}}"
model_tested: "{{model_tested}}}}"
```
## Overview
`{{overview_content}}`
## Prompt Snapshot
`{{prompt_snapshot_content}}`
## Metrics
`{{metrics_content}}`
## Lineage
`{{lineage_content}}`

## Template Standards

1. Define all required sections for this output kind
2. Include frontmatter schema with mandatory fields
3. Provide structural markers for post-validation
4. Specify format constraints for markdown YAML JSON
5. Reference the validation_schema for automated checks

## Properties

| Property | Value |
|----------|-------|
| Kind | `output_template` |
| Pillar | P05 |
| Domain | prompt version construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
