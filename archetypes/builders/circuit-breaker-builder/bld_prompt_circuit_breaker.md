---
quality: 8.7
quality: 8.0
kind: instruction
id: bld_instruction_circuit_breaker
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for circuit_breaker
pattern: 3-phase pipeline (define -> compose -> validate)
title: "Instruction Circuit Breaker"
version: "1.0.0"
author: n03_builder
tags: [circuit_breaker, builder, instruction]
tldr: "3-phase: define failure thresholds and state machine, compose with cooldown and probe config, validate gates."
domain: "circuit breaker construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
related:
  - bld_instruction_output_validator
  - bld_instruction_fallback_chain
  - bld_instruction_memory_scope
  - bld_instruction_enum_def
  - bld_instruction_retriever_config
  - bld_instruction_chunk_strategy
  - bld_instruction_handoff_protocol
  - bld_instruction_trace_config
  - bld_instruction_search_tool
  - bld_instruction_context_doc
---

# Instructions: How to Produce a circuit_breaker

## Phase 1: DEFINE
1. Identify the dependency being protected (API name, service, model provider)
2. Determine failure_rate_threshold: percentage of calls that must fail to trip (e.g. 50%)
3. Choose sliding_window_type: COUNT_BASED (last N calls) or TIME_BASED (last N seconds)
4. Set sliding_window_size: number of calls or seconds for the window
5. Set minimum_number_of_calls: minimum calls before failure rate is computed
6. Set cooldown_duration: seconds/minutes circuit stays OPEN before half-open probe
7. Define probe_count: how many test calls in HALF-OPEN state before closing
8. Specify fallback_response: what to return while circuit is OPEN (error msg, cached value, default)
9. List monitored_exceptions: which error types count as failures (e.g. HTTP 5xx, timeout, ConnectionError)
10. Define slow_call_threshold: duration in ms above which call is counted as slow failure (optional)

## Phase 2: COMPOSE
1. Read SCHEMA.md and OUTPUT_TEMPLATE.md
2. Fill frontmatter: all required fields (quality: null)
3. Set id: `p09_cb_{service_slug}` -- verify pattern `^p09_cb_[a-z][a-z0-9_]+$`
4. Write Overview section: what dependency is protected and why
5. Write State Machine section: CLOSED/OPEN/HALF-OPEN transitions with thresholds
6. Write Cooldown section: duration, probe count, recovery criteria
7. Write Fallback section: what is returned during open state
8. Verify body <= 3072 bytes

## Phase 3: VALIDATE
1. Confirm id matches `^p09_cb_[a-z][a-z0-9_]+$`
2. Confirm kind == circuit_breaker
3. Confirm failure_rate_threshold is a positive integer in range [1, 100]
4. Confirm cooldown_duration is a positive integer (seconds)
5. Confirm probe_count is a positive integer
6. Confirm all 4 body sections present: Overview, State Machine, Cooldown, Fallback
7. Cross-check: not rate_limit_config (no RPM/TPM quotas), not fallback_chain (not ordered provider list)
8. Confirm quality: null
9. Revise if score < 8.0


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_output_validator]] | sibling | 0.33 |
| [[bld_instruction_fallback_chain]] | sibling | 0.33 |
| [[bld_instruction_memory_scope]] | sibling | 0.32 |
| [[bld_instruction_enum_def]] | sibling | 0.32 |
| [[bld_instruction_retriever_config]] | sibling | 0.32 |
| [[bld_instruction_chunk_strategy]] | sibling | 0.31 |
| [[bld_instruction_handoff_protocol]] | sibling | 0.31 |
| [[bld_instruction_trace_config]] | sibling | 0.31 |
| [[bld_instruction_search_tool]] | sibling | 0.31 |
| [[bld_instruction_context_doc]] | sibling | 0.31 |
