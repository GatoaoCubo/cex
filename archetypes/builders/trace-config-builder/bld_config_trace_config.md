---
kind: config
id: bld_config_trace_config
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
title: "Config Trace Config"
version: "1.0.0"
author: n03_builder
tags: [trace_config, builder, examples]
tldr: "Golden and anti-examples for trace config construction, demonstrating ideal structure and common pitfalls."
domain: "trace config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_examples_trace_config
  - bld_knowledge_card_trace_config
  - bld_output_template_trace_config
  - p07_tc_opentelemetry
  - bld_config_memory_scope
  - bld_config_prompt_version
  - bld_config_retriever_config
  - bld_config_env_config
  - bld_config_output_validator
  - bld_collaboration_trace_config
---
# Config: trace_config Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p07_tc_{{name}}.yaml` | `p07_tc_production.yaml` |
| Builder directory | kebab-case | `trace-config-builder/` |
| Frontmatter fields | snake_case | `sample_rate`, `capture_prompts` |
| Span names | dot-separated hierarchy | `cex.8f.f1_constrain`, `cex.tool.call` |
| Attribute keys | dot-separated, lowercase | `cex.nucleus`, `cex.kind`, `cex.tokens.total` |
Rule: id MUST equal filename stem. Hyphens in id = HARD FAIL.
## File Paths
- Output: `cex/P07_testing/examples/p07_tc_{{name}}.yaml`
- Compiled: `cex/P07_testing/compiled/p07_tc_{{name}}.yaml`
## Size Limits (aligned with SCHEMA)
- Body: max 4096 bytes
- Total (frontmatter + body): ~5500 bytes
- Density: >= 0.80 (no filler)
## Export Format Enum
| Value | Endpoint | When to use |
|-------|---------|-------------|
| console | stdout | Development — immediate visibility |
| json_file | Local path | Staging — inspectable, no server needed |
| otlp | OTLP/gRPC endpoint | Production — Jaeger, Tempo, Honeycomb |
| langsmith | LangSmith API | Evaluation — prompt quality analysis |
## Sample Rate Conventions
| Environment | Rate | Rationale |
|-------------|------|-----------|
| development | 1.0 | Trace everything — debugging needs full visibility |
| staging | 0.20 | 1 in 5 — catch regressions without storage burden |
| production | 0.05-0.10 | 1 in 10-20 — cost-effective, statistically meaningful |
| evaluation | 1.0 | Trace everything — quality analysis needs complete data |
## Span Hierarchy
| Level | Span Name | Attributes |
|-------|-----------|-----------|
| Root | `cex.pipeline` | nucleus, kind, intent |
| L1 | `cex.8f.{function}` | function_name (F1-F8), duration_ms |
| L2 | `cex.llm.call` | model, tokens_in, tokens_out, latency_ms |
| L2 | `cex.tool.call` | tool_name, status, duration_ms |
| L3 | `cex.memory.read` | memory_type, hit_count |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_trace_config]] | upstream | 0.39 |
| [[bld_knowledge_card_trace_config]] | upstream | 0.34 |
| [[bld_output_template_trace_config]] | upstream | 0.31 |
| [[p07_tc_opentelemetry]] | upstream | 0.30 |
| [[bld_config_memory_scope]] | sibling | 0.26 |
| [[bld_config_prompt_version]] | sibling | 0.25 |
| [[bld_config_retriever_config]] | sibling | 0.24 |
| [[bld_config_env_config]] | sibling | 0.23 |
| [[bld_config_output_validator]] | sibling | 0.23 |
| [[bld_collaboration_trace_config]] | downstream | 0.23 |
