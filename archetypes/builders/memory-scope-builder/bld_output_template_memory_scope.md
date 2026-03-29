---
kind: output_template
id: bld_output_template_memory_scope
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a memory_scope artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
---

# Output Template: memory_scope
```yaml
id: p02_memscope_{{slug}}
kind: memory_scope
pillar: P02
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
name: "{{name}}}}"
memory_types: "{{memory_types}}}}"
backend: "{{backend}}}}"
ttl: "{{ttl}}}}"
quality: null
tags: [memory_scope, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
description: "{{description}}}}"
scope: "{{scope}}}}"
max_entries: "{{max_entries}}}}"
eviction_policy: "{{eviction_policy}}}}"
encryption: "{{encryption}}}}"
shared_with: "{{shared_with}}}}"
```
## Overview
{{overview_content}}
## Memory Types
{{memory_types_content}}
## Backend Config
{{backend_config_content}}
## Lifecycle
{{lifecycle_content}}

