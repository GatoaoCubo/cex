---
kind: config
id: bld_config_learning_record
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
title: "Config Learning Record"
version: "1.0.0"
author: n03_builder
tags: [learning_record, builder, examples]
tldr: "Golden and anti-examples for learning record construction, demonstrating ideal structure and common pitfalls."
domain: "learning record construction"
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
  - bld_config_hook_config
  - bld_config_constraint_spec
  - bld_config_chunk_strategy
  - bld_config_pattern
---
# Config: learning_record Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p10_lr_{topic_slug}.md` | `p10_lr_continuous_batching_speedup.md` |
| Builder directory | kebab-case | `learning-record-builder/` |
| Frontmatter fields | snake_case | `linked_artifacts`, `reproducibility` |
| Slug | lowercase + underscores | `continuous_batching_speedup` |
Rule: id MUST equal filename stem.
## File Paths
1. Output: `cex/P10_memory/examples/p10_lr_{slug}.md`
2. Compiled: `cex/P10_memory/compiled/p10_lr_{slug}.yaml`
## Size Limits (aligned with SCHEMA)
1. Body: max 3072 bytes
2. Total: ~4000 bytes (frontmatter + body)
3. Density: >= 0.80
## Learning-Specific Constraints
1. Outcome enum: strictly SUCCESS, PARTIAL, or FAILURE (no synonyms)
2. Score range: 0.0-10.0 (float, never string, never null)
3. Pattern concreteness: each step must be actionable ("use X with Y" not "be careful")
4. Anti-pattern specificity: name the failure mode, not generic warning
5. Timestamp precision: ISO 8601 with timezone when available
6. Agent_group attribution: tag originating agent_group for routing intelligence
7. Deduplication: brain_query before creating (same topic + same outcome = update, not new)

## Metadata

```yaml
id: bld_config_learning_record
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-config-learning-record.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `config` |
| Pillar | P09 |
| Domain | learning record construction |
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
| [[bld_config_prompt_version]] | sibling | 0.41 |
| [[bld_config_output_validator]] | sibling | 0.41 |
| [[bld_config_quality_gate]] | sibling | 0.40 |
| [[bld_config_handoff_protocol]] | sibling | 0.39 |
| [[bld_config_hook_config]] | sibling | 0.39 |
| [[bld_config_constraint_spec]] | sibling | 0.39 |
| [[bld_config_chunk_strategy]] | sibling | 0.38 |
| [[bld_config_pattern]] | sibling | 0.37 |
