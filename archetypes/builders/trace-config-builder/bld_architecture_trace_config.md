---
kind: architecture
id: bld_architecture_trace_config
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of trace_config — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Trace Config"
version: "1.0.0"
author: n03_builder
tags: [trace_config, builder, examples]
tldr: "Golden and anti-examples for trace config construction, demonstrating ideal structure and common pitfalls."
domain: "trace config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| enabled | Master switch for tracing (true/false) | trace-config-builder | required |
| sample_rate | Fraction of requests to trace (0.0-1.0) | trace-config-builder | required |
| export_format | Trace exporter: otlp, langsmith, console, json_file | trace-config-builder | required |
| export_path | Endpoint URL or filesystem path for trace output | trace-config-builder | required |
| capture_prompts | Whether to record full prompt content in spans | trace-config-builder | required |
| capture_responses | Whether to record full response content in spans | trace-config-builder | required |
| span_attributes | Custom attributes attached to each span (nucleus, kind, tokens) | trace-config-builder | required |
| retention_days | How long traces are kept before deletion | trace-config-builder | required |
| error_classification | How errors are categorized in spans (transient, permanent, rate_limit) | trace-config-builder | recommended |
| metadata | config id, version, pillar, scope, author, created date | trace-config-builder | required |
## Dependency Graph
```
trace_config --consumed_by--> cex_8f_runner.py (instruments 8F stages with spans)
trace_config --consumed_by--> cex_sdk/tracing/ (implements tracing interface)
trace_config --consumed_by--> cex_quality_monitor.py (reads trace data for quality snapshots)
trace_config --consumed_by--> cex_crew_runner.py (traces prompt assembly and LLM calls)
env_config (P09) --feeds--> trace_config (provides OTLP endpoint, LangSmith API key via env vars)
quality_gate (P11) --independent-- trace_config (quality_gate scores artifacts; trace_config observes execution)
log_config --independent-- trace_config (log_config formats log messages; trace_config captures spans)
```
| From | To | Type | Data |
|------|----|------|------|
| env_config | trace_config | feeds | OTLP endpoint URL, LangSmith API key via env vars |
| trace_config | cex_8f_runner.py | consumed_by | span names for F1-F8, token accounting, timings |
| trace_config | cex_sdk/tracing/ | consumed_by | exporter config, sample rate, capture rules |
| trace_config | cex_quality_monitor.py | consumed_by | trace data for quality regression detection |
| trace_config | cex_crew_runner.py | consumed_by | LLM call spans, prompt assembly timing |
## Boundary Table
| trace_config IS | trace_config IS NOT |
|----------------|---------------------|
| A specification of HOW execution is traced for debugging and observability | A quality_gate (P11) — quality_gate scores artifact quality, not execution |
| Covers exporters, sample rates, capture rules, and retention | A log_config — log_config formats and routes log messages |
| Follows selective capture: trace spans always, capture content selectively | A metric_config — metric_config defines counters and gauges |
| Declares span attributes for 8F function-level tracing | An alert_config — alert_config defines thresholds and notification rules |
| Specifies privacy controls for prompt/response capture | A session_backend (P10) — session_backend persists state; trace_config observes execution |
| Defines retention policies with hot/warm/cold tiers | A compression_config (P10) — compression reduces context; trace_config records it |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Control | enabled, sample_rate | Whether and how often to trace |
| Capture | capture_prompts, capture_responses, span_attributes | What data to record |
| Export | export_format, export_path | Where traces go |
| Lifecycle | retention_days, error_classification | How long traces live, how errors are categorized |
