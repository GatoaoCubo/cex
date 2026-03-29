---
kind: output_template
id: bld_output_template_chunk_strategy
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a chunk_strategy artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
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
{{overview_content}}
## Method
{{method_content}}
## Parameters
{{parameters_content}}
## Integration
{{integration_content}}

