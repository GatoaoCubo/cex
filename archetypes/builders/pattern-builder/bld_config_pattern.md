---
kind: config
id: bld_config_pattern
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
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
title: "Config Pattern"
version: "1.0.0"
author: n03_builder
tags: [pattern, builder, examples]
tldr: "Golden and anti-examples for pattern construction, demonstrating ideal structure and common pitfalls."
domain: "pattern construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_config_retriever_config
  - bld_config_memory_scope
  - bld_config_prompt_version
  - bld_config_output_validator
  - bld_config_quality_gate
  - bld_config_handoff_protocol
  - bld_config_constraint_spec
  - bld_config_hook_config
  - bld_config_chunk_strategy
  - bld_config_learning_record
---
# Config: pattern Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p08_pat_{slug}.md` | `p08_pat_continuous_batching.md` |
| Builder directory | kebab-case | `pattern-builder/` |
| Frontmatter fields | snake_case | `related_patterns`, `anti_patterns` |
| Slug | lowercase + underscores | `continuous_batching` |
Rule: id MUST equal filename stem.
## File Paths
1. Output: `cex/P08_architecture/examples/p08_pat_{slug}.md`
2. Compiled: `cex/P08_architecture/compiled/p08_pat_{slug}.yaml`
## Size Limits (aligned with SCHEMA)
1. Body: max 4096 bytes
2. Total: ~5300 bytes (frontmatter + body)
3. Density: >= 0.80
## Pattern-Specific Constraints
1. Name: 2-5 words, Title Case (e.g., "Continuous Batching", "Signal Monitor")
2. Problem recurrence: must describe a situation that happens repeatedly
3. Forces minimum: at least 2 competing tensions
4. Consequences balance: MUST include at least 1 cost/drawback alongside benefits
5. Examples minimum: at least 2 concrete, named applications
6. Solution concreteness: must describe HOW (steps or diagram), not just WHAT
7. Anti-patterns: specific wrong approaches, not generic warnings
8. No prescriptive language: "consider" not "you must" (patterns recommend, laws mandate)

## Metadata

```yaml
id: bld_config_pattern
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-config-pattern.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `config` |
| Pillar | P09 |
| Domain | pattern construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_retriever_config]] | sibling | 0.45 |
| [[bld_config_memory_scope]] | sibling | 0.42 |
| [[bld_config_prompt_version]] | sibling | 0.42 |
| [[bld_config_output_validator]] | sibling | 0.41 |
| [[bld_config_quality_gate]] | sibling | 0.40 |
| [[bld_config_handoff_protocol]] | sibling | 0.39 |
| [[bld_config_constraint_spec]] | sibling | 0.39 |
| [[bld_config_hook_config]] | sibling | 0.39 |
| [[bld_config_chunk_strategy]] | sibling | 0.38 |
| [[bld_config_learning_record]] | sibling | 0.35 |
