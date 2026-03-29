---
kind: output_template
id: bld_output_template_retriever_config
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a retriever_config artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
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
{{overview_content}}
## Search Strategy
{{search_strategy_content}}
## Parameters
{{parameters_content}}
## Integration
{{integration_content}}

