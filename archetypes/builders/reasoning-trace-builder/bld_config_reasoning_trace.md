---
kind: config
id: bld_config_reasoning_trace
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, limits, and operational constraints
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
title: "Config Reasoning Trace"
version: "1.0.0"
author: n03_builder
tags: [reasoning_trace, builder, examples]
tldr: "Golden and anti-examples for reasoning trace construction, demonstrating ideal structure and common pitfalls."
domain: "reasoning trace construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_knowledge_card_reasoning_trace
  - bld_collaboration_reasoning_trace
  - p03_ins_reasoning_trace_builder
  - p01_kc_reasoning_trace
  - p03_sp_reasoning_trace_builder
  - bld_tools_reasoning_trace
  - bld_output_template_reasoning_trace
  - reasoning-trace-builder
  - bld_memory_reasoning_trace
  - bld_schema_reasoning_trace
---
# Config: reasoning_trace Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact file | `p03_rt_{agent}_{timestamp}.yaml` | `p03_rt_research_agent_20260406T143000.yaml` |
| Builder directory | kebab-case | `reasoning-trace-builder/` |
| Trace fields | snake_case | `alternatives_rejected`, `duration_ms` |
| Step labels | sequential integers | `1`, `2`, `3` |
| Agent values | lowercase slug | `research-agent`, `build-sat` |
Rule: use `.yaml` only for this builder — traces are human-readable audit records.
## File Paths
1. Output: `cex/P03_prompt/compiled/p03_rt_{agent}_{timestamp}.yaml`
2. Human reference: `cex/P03_prompt/examples/p03_rt_{agent}_{timestamp}.md`
## Size Limits
1. Preferred trace size: <= 4096 bytes
2. Absolute max: 8192 bytes
3. Steps should be concise: thought + evidence in 1-2 sentences each
4. Cap step count at 10 — more than 10 steps indicates the decision should be decomposed
## Trace Restrictions
1. Required fields must appear exactly as defined in schema
2. Omit optional null/unknown fields instead of writing placeholders
3. `duration_ms` allowed only when timing data is genuinely available
4. Each step MUST have non-empty `thought`, `evidence`, and `confidence`
5. Confidence values must be numeric 0.0-1.0, not strings or percentages
6. Overall confidence is geometric mean of step confidences, not arithmetic mean
## Boundary Restrictions
1. No execution instructions, tool calls, or action items inside the trace
2. No workflow step definitions, DAGs, or sequencing logic
3. No system prompt content, persona definitions, or agent identity
4. No routing tables, dispatch rules, or agent selection logic
## Feedback Loop Rules
1. Traces with overall confidence < 0.5 trigger memory feedback: write learning record
2. Traces with any single step confidence < 0.2 flag that step for human review
3. Traces are immutable once emitted — corrections produce a new trace, never mutate

## Metadata

```yaml
id: bld_config_reasoning_trace
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-config-reasoning-trace.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `config` |
| Pillar | P09 |
| Domain | reasoning trace construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_reasoning_trace]] | upstream | 0.56 |
| [[bld_collaboration_reasoning_trace]] | upstream | 0.54 |
| [[p03_ins_reasoning_trace_builder]] | upstream | 0.52 |
| [[p01_kc_reasoning_trace]] | upstream | 0.52 |
| [[p03_sp_reasoning_trace_builder]] | upstream | 0.52 |
| [[bld_tools_reasoning_trace]] | upstream | 0.49 |
| [[bld_output_template_reasoning_trace]] | upstream | 0.49 |
| [[reasoning-trace-builder]] | upstream | 0.49 |
| [[bld_memory_reasoning_trace]] | downstream | 0.48 |
| [[bld_schema_reasoning_trace]] | upstream | 0.45 |
