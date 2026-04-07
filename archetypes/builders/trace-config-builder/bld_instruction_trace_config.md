---
kind: instruction
id: bld_instruction_trace_config
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for trace_config
pattern: 3-phase pipeline (research -> compose -> validate)
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
