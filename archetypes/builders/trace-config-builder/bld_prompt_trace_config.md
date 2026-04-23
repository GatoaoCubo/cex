---
kind: instruction
id: bld_instruction_trace_config
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for trace_config
pattern: 3-phase pipeline (research -> compose -> validate)
quality: 9.2
title: "Instruction Trace Config"
version: "1.0.0"
author: n03_builder
tags: [trace_config, builder, examples]
tldr: "Golden and anti-examples for trace config construction, demonstrating ideal structure and common pitfalls."
domain: "trace config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_instruction_session_backend
  - bld_instruction_retriever_config
  - bld_instruction_memory_scope
  - bld_instruction_output_validator
  - bld_instruction_context_doc
  - bld_instruction_prompt_version
  - bld_instruction_chunk_strategy
  - bld_instruction_handoff_protocol
  - bld_instruction_search_tool
  - bld_instruction_constraint_spec
---

# Instructions: How to Produce a trace_config
## Phase 1: RESEARCH
1. Identify the target: which agent, nucleus, or pipeline needs execution tracing?
2. Determine the environment: development (full capture), staging (moderate), production (selective)
3. Catalog what should be traced: 8F pipeline stages, tool calls, LLM invocations, memory operations
4. Classify data sensitivity: do prompts contain PII? Are responses proprietary? Are tool results sensitive?
5. Determine export destination: local console (dev), JSON file (staging), OTLP endpoint (prod), LangSmith (eval)
6. Assess storage budget: how many GB/day of trace data is acceptable?
7. Define retention requirements: hot (7d, fast query), warm (30d, compressed), cold (90d+, archival)
8. Check existing trace_configs via brain_query [IF MCP] for the same scope — do not duplicate
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill the template following SCHEMA constraints
3. Fill all required frontmatter fields; set `quality: null` — never self-score
4. Write **Tracing Specification** section: enabled flag, sample rate, exporter, rationale
5. Write **Capture Rules** section: what is captured (spans, tokens, latency) and what is excluded (prompts, PII)
6. Write **Span Attributes** section: 8F function mapping, costm attributes, error classification
7. Write **Retention Policy** section: hot/warm/cold tiers, days per tier, cleanup strategy
8. Write **Privacy Controls** section: PII redaction rules, prompt/response capture policy, consent
9. Confirm body <= 4096 bytes
## Phase 3: VALIDATE
1. Check QUALITY_GATES.md — verify each HARD gate manually
2. Confirm YAML frontmatter parses without errors
3. Confirm `id` matches `^p07_tc_[a-z][a-z0-9_]+$`
4. Confirm enabled is boolean
5. Confirm sample_rate is between 0.0 and 1.0
6. Confirm export_format is one of: otlp, langsmith, console, json_file
7. Confirm retention_days is a positive integer
8. Confirm capture_prompts and capture_responses are explicitly set (not omitted)
9. Confirm `quality` is null
10. Confirm body <= 4096 bytes
11. Cross-check: is this a tracing config? If this is artifact quality scoring it belongs in `quality_gate`. If this is log formatting it belongs in `log_config`. If this is counter/gauge definition it belongs in `metric_config`. This artifact specifies HOW execution is traced, not HOW artifacts are scored.
12. If score < 8.0: revise in the same pass before outputting

## ISO Loading

```yaml
loader: cex_skill_loader
injection_point: F3_compose
priority: high
```

```bash
python _tools/cex_skill_loader.py --verify trace
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `instruction` |
| Pillar | P03 |
| Domain | trace config construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_session_backend]] | sibling | 0.46 |
| [[bld_instruction_retriever_config]] | sibling | 0.46 |
| [[bld_instruction_memory_scope]] | sibling | 0.46 |
| [[bld_instruction_output_validator]] | sibling | 0.45 |
| [[bld_instruction_context_doc]] | sibling | 0.44 |
| [[bld_instruction_prompt_version]] | sibling | 0.44 |
| [[bld_instruction_chunk_strategy]] | sibling | 0.44 |
| [[bld_instruction_handoff_protocol]] | sibling | 0.43 |
| [[bld_instruction_search_tool]] | sibling | 0.43 |
| [[bld_instruction_constraint_spec]] | sibling | 0.42 |
