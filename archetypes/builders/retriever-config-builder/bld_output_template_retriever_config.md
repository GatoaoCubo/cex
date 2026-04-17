---
kind: output_template
id: bld_output_template_retriever_config
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a retriever_config artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
quality: 9.0
title: "Output Template Retriever Config"
version: "1.0.0"
author: n03_builder
tags: [retriever_config, builder, examples]
tldr: "Golden and anti-examples for retriever config construction, demonstrating ideal structure and common pitfalls."
domain: "retriever config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Output Template: retriever_config
```yaml
id: p01_retr_{{slug}}
kind: retriever_config
pillar: P01
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
name: "{{name}}}}"
store_type: "{{store_type}}}}"
top_k: "{{top_k}}}}"
search_type: "{{search_type}}}}"
quality: null
tags: [retriever_config, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
description: "{{description}}}}"
hybrid_ratio: "{{hybrid_ratio}}}}"
reranker: "{{reranker}}}}"
filters: "{{filters}}}}"
score_threshold: "{{score_threshold}}}}"
fetch_k: "{{fetch_k}}}}"
```
## Overview
`{{overview_content}}`
## Search Strategy
`{{search_strategy_content}}`
## Parameters
`{{parameters_content}}`
## Integration
`{{integration_content}}`

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
| Domain | retriever config construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
