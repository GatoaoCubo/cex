---
kind: config
id: bld_config_context_window_config
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
effort: medium
max_turns: 20
disallowed_tools: []
fork_context: fork
hooks:
  pre_build: null
  post_build: null
permission_scope: nucleus
quality: 9.0
title: "Config Context Window Config"
version: "1.0.0"
author: n03_builder
tags: [context_window_config, builder, examples]
tldr: "Golden and anti-examples for context window config construction, demonstrating ideal structure and common pitfalls."
domain: "context window config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_instruction_context_window_config
  - bld_examples_context_window_config
  - bld_config_retriever_config
  - bld_config_prompt_version
  - bld_collaboration_context_window_config
  - bld_config_constraint_spec
  - bld_config_quality_gate
  - bld_config_hook_config
  - bld_config_memory_scope
  - bld_tools_context_window_config
---
# Config: context_window_config Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p03_cwc_{model_slug}.yaml` | `p03_cwc_opus_rag_heavy.yaml` |
| Builder directory | kebab-case | `context-window-config-builder/` |
| Frontmatter fields | snake_case | `total_tokens`, `overflow_strategy` |
Rule: id MUST equal filename stem.
## File Paths
1. Output: `P03_prompt/examples/p03_cwc_{model}.yaml`
2. Compiled: `P03_prompt/compiled/p03_cwc_{model}.yaml`
## Size Limits
1. Total file: max 2048 bytes
2. tldr: <= 160 chars
## Budget Validation Rules
1. sum(all_budgets) + output_reserve <= total_tokens
2. output_reserve >= 2000 (absolute minimum)
3. Default split: system=10%, examples=15%, context=40%, query=5%, output=30%
4. RAG-heavy: context gets 50%+, examples reduced
5. Few-shot-heavy: examples get 25%+, context reduced

## Metadata

```yaml
id: bld_config_context_window_config
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-config-context-window-config.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `config` |
| Pillar | P09 |
| Domain | context window config construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_context_window_config]] | upstream | 0.43 |
| [[bld_examples_context_window_config]] | upstream | 0.43 |
| [[bld_config_retriever_config]] | sibling | 0.39 |
| [[bld_config_prompt_version]] | sibling | 0.36 |
| [[bld_collaboration_context_window_config]] | downstream | 0.35 |
| [[bld_config_constraint_spec]] | sibling | 0.34 |
| [[bld_config_quality_gate]] | sibling | 0.34 |
| [[bld_config_hook_config]] | sibling | 0.33 |
| [[bld_config_memory_scope]] | sibling | 0.33 |
| [[bld_tools_context_window_config]] | upstream | 0.33 |
