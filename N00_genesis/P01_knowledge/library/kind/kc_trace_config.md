---
id: p01_kc_trace_config
kind: knowledge_card
type: kind
pillar: P07
title: "Trace Config -- Deep Knowledge for trace_config"
version: 1.0.0
created: 2026-04-05
updated: 2026-04-05
author: n07-orchestrator
domain: trace_config
quality: 9.1
tags: [trace_config, p07, GOVERN, kind-kc, observability, tracing]
tldr: "Configuration for agent execution tracing -- controls what gets logged, sampled, and exported for debugging and evals"
when_to_use: "Setting up observability for agent runs, configuring trace sampling, or debugging pipeline failures"
keywords: [trace, config, observability, logging, spans, OpenTelemetry, debug]
feeds_kinds: [trace_config]
density_score: null
---

# Trace Config

## Spec
```yaml
kind: trace_config
pillar: P07
llm_function: GOVERN
max_bytes: 3072
naming: p07_tc_{{name}}.yaml
core: false
```

## Purpose

A trace config defines what execution data is captured during agent runs. Traces record timing, token usage, tool calls, errors, and quality scores for each function in the 8F pipeline. Without tracing, you cannot debug why a build failed or identify slow functions.

## Anatomy

| Field | Purpose | Example |
|-------|---------|---------|
| enabled | Global tracing toggle | `true` |
| sample_rate | Fraction of runs to trace | `1.0` (all), `0.1` (10%) |
| export_format | Trace output format | `json`, `otlp`, `console` |
| export_path | Where traces are written | `.cex/traces/` |
| capture_prompts | Include full prompts in traces | `false` (privacy) |
| capture_responses | Include full LLM responses | `false` (size) |
| span_attributes | Extra fields to record | `[nucleus, kind, builder, model]` |
| retention_days | Auto-delete traces after | `7` |

## Key Patterns

1. **Function-level spans**: One span per 8F function (F1 through F8), nested under pipeline span
2. **Token accounting**: Record input/output tokens per LLM call for cost tracking
3. **Error classification**: Tag errors as recoverable (retry) vs fatal (abort) in trace
4. **Selective capture**: Capture prompts only for failed runs (debug without privacy cost)

## CEX Integration

- `cex_8f_runner.py` records `state.timings` per function (proto-trace)
- `cex_sdk/tracing/` provides span-based tracing with export
- Traces feed `cex_quality_monitor.py` for regression detection
- `cex_evolve.py` experiment log is a specialized trace format
