---
kind: config
id: bld_config_compression_config
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
quality: 9.0
title: "Config Compression Config"
version: "1.0.0"
author: n03_builder
tags: [compression_config, builder, examples]
tldr: "Golden and anti-examples for compression config construction, demonstrating ideal structure and common pitfalls."
domain: "compression config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_instruction_compression_config
  - bld_knowledge_card_compression_config
  - p03_sp_compression_config_builder
  - bld_schema_compression_config
  - p01_kc_compression_config
  - bld_examples_compression_config
  - p10_lr_compression_config_builder
  - bld_config_retriever_config
  - bld_config_memory_scope
  - bld_config_chunk_strategy
---
# Config: compression_config Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p10_cc_{{name}}.yaml` | `p10_cc_aggressive.yaml` |
| Builder directory | kebab-case | `compression-config-builder/` |
| Frontmatter fields | snake_case | `trigger_ratio`, `preserve_types` |
| Strategy names | snake_case, lowercase | `rolling_window`, `priority_keep` |
| Preset names | snake_case, lowercase, descriptive | `aggressive`, `conservative`, `balanced` |
Rule: id MUST equal filename stem. Hyphens in id = HARD FAIL.
## File Paths
- Output: `cex/P10_memory/examples/p10_cc_{{name}}.yaml`
- Compiled: `cex/P10_memory/compiled/p10_cc_{{name}}.yaml`
## Size Limits (aligned with SCHEMA)
- Body: max 4096 bytes
- Total (frontmatter + body): ~5500 bytes
- Density: >= 0.80 (no filler)
## Strategy Enum
| Value | When to use |
|-------|-------------|
| summarize | Semantic compression — LLM summarizes older messages into a condensed block |
| truncate_oldest | Positional — drop oldest messages first, keep newest |
| rolling_window | Sliding window — keep last N messages or N tokens |
| priority_keep | Weighted — each message type has a priority; compress lowest first |
| tiered | Multi-stage — execute compression stages in order until target ratio is met |
## Trigger Ratio Conventions
| Range | Label | When to use |
|-------|-------|-------------|
| 0.90-0.99 | aggressive | Compress early — maximize headroom for long tasks |
| 0.80-0.89 | balanced | Default — good trade-off between context and headroom |
| 0.50-0.79 | conservative | Compress late — preserve maximum context at cost of headroom |
| < 0.50 | INVALID | Never trigger below 50% — wastes compute, loses information |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_compression_config]] | upstream | 0.35 |
| [[bld_knowledge_card_compression_config]] | upstream | 0.34 |
| [[p03_sp_compression_config_builder]] | upstream | 0.32 |
| [[bld_schema_compression_config]] | upstream | 0.31 |
| [[p01_kc_compression_config]] | downstream | 0.31 |
| [[bld_examples_compression_config]] | upstream | 0.30 |
| [[p10_lr_compression_config_builder]] | downstream | 0.29 |
| [[bld_config_retriever_config]] | sibling | 0.28 |
| [[bld_config_memory_scope]] | sibling | 0.28 |
| [[bld_config_chunk_strategy]] | sibling | 0.28 |
