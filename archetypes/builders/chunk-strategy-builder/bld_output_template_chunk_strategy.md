---
kind: output_template
id: bld_output_template_chunk_strategy
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a chunk_strategy artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
quality: 9.0
title: "Output Template Chunk Strategy"
version: "1.0.0"
author: n03_builder
tags: [chunk_strategy, builder, examples]
tldr: "Golden and anti-examples for chunk strategy construction, demonstrating ideal structure and common pitfalls."
domain: "chunk strategy construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Output Template: chunk_strategy
```yaml
id: p01_chunk_{{slug}}
kind: chunk_strategy
pillar: P01
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
name: "{{name}}}}"
method: "{{method}}}}"
chunk_size: "{{chunk_size}}}}"
chunk_overlap: "{{chunk_overlap}}}}"
separators: "{{separators}}}}"
quality: null
tags: [chunk_strategy, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
description: "{{description}}}}"
tokenizer: "{{tokenizer}}}}"
min_chunk_size: "{{min_chunk_size}}}}"
strip_whitespace: "{{strip_whitespace}}}}"
keep_separator: "{{keep_separator}}}}"
```
## Overview
`{{overview_content}}`
## Method
`{{method_content}}`
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
| Domain | chunk strategy construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
