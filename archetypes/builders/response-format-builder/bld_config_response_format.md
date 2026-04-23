---
kind: config
id: bld_config_response_format
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for response_format production
pattern: CONFIG restricts SCHEMA, never contradicts
effort: medium
max_turns: 25
disallowed_tools: []
fork_context: null
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: nucleus
quality: 9.1
title: "Config Response Format"
version: "1.0.0"
author: n03_builder
tags: [response_format, builder, examples]
tldr: "Golden and anti-examples for response format construction, demonstrating ideal structure and common pitfalls."
domain: "response format construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - response-format-builder
  - bld_config_validation_schema
  - bld_config_retriever_config
  - bld_config_output_validator
  - bld_collaboration_response_format
  - bld_config_quality_gate
  - bld_schema_response_format
  - bld_tools_response_format
  - bld_config_memory_scope
  - bld_examples_response_format
---
# Config: response_format Production Rules
## Naming
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact | p05_rf_{format_slug}.yaml | p05_rf_knowledge_card.yaml |
| Builder dir | kebab-case | response-format-builder/ |
| Fields | snake_case | format_type, injection_point, sections_count |
| Format slugs | lowercase_underscores | knowledge_card, model_card, signal_json |
Rule: id MUST equal filename stem.
## File Paths
1. Output: cex/P05_output/examples/p05_rf_{format_slug}.yaml
2. Compiled: cex/P05_output/compiled/p05_rf_{format_slug}.json
## Size Limits (aligned with SCHEMA)
1. Body: max 4096 bytes
2. Density: >= 0.80
3. Sections: >= 1 (recommend 3-7; LLMs struggle above 10)
## Format Policy
1. format_type determines output structure the LLM follows
2. json: highest compliance rate, best for machine consumption
3. yaml: good for config-like output with frontmatter
4. markdown: best for human-readable docs, supports headers/tables
5. csv: tabular data only, simple extraction
6. plaintext: unstructured, use only when no structure needed

## Metadata

```yaml
id: bld_config_response_format
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-config-response-format.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `config` |
| Pillar | P09 |
| Domain | response format construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[response-format-builder]] | upstream | 0.40 |
| [[bld_config_validation_schema]] | sibling | 0.39 |
| [[bld_config_retriever_config]] | sibling | 0.36 |
| [[bld_config_output_validator]] | sibling | 0.36 |
| [[bld_collaboration_response_format]] | upstream | 0.35 |
| [[bld_config_quality_gate]] | sibling | 0.35 |
| [[bld_schema_response_format]] | upstream | 0.35 |
| [[bld_tools_response_format]] | upstream | 0.33 |
| [[bld_config_memory_scope]] | sibling | 0.32 |
| [[bld_examples_response_format]] | upstream | 0.32 |
