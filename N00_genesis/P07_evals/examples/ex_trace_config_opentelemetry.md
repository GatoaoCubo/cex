---
id: p07_tc_opentelemetry
kind: trace_config
pillar: P07
title: "Example — OpenTelemetry Trace Configuration"
version: 1.0.0
created: 2026-04-06
updated: 2026-04-06
author: builder_agent
enabled: true
sample_rate: 1.0
export_format: otlp
export_path: "http://localhost:4318/v1/traces"
capture_prompts: false
capture_responses: false
retention_days: 7
domain: trace_config
quality: 9.1
tags: [trace-config, opentelemetry, observability, tracing, spans]
tldr: "OpenTelemetry trace config — 100% sampling, OTLP export to localhost:4318, 8F function-level spans, 7-day retention."
when_to_use: "Development/staging environments where full observability of 8F pipeline execution is needed"
keywords: [trace, opentelemetry, otlp, spans, observability, 8f, pipeline]
density_score: null
---

# Trace Config: OpenTelemetry

## Configuration
| Parameter | Value | Rationale |
|-----------|-------|-----------|
| enabled | true | Active tracing |
| sample_rate | 1.0 | 100% in dev; reduce to 0.1 in production |
| export_format | otlp | Standard OpenTelemetry Protocol |
| export_endpoint | localhost:4318 | OTLP HTTP receiver (Jaeger/Tempo) |
| capture_prompts | false | Privacy: prompts may contain user data |
| capture_responses | false | Size: responses can be 4KB+ |
| retention_days | 7 | Balance storage vs debuggability |

## Span Structure (8F Pipeline)
```
pipeline (root span)
├── F1_CONSTRAIN    [kind, pillar, max_bytes]
├── F2_BECOME       [builder, iso_count]
├── F3_INJECT       [kc_count, example_count, match_score]
├── F4_REASON       [approach, sections, reasoning_tokens]
├── F5_CALL         [tools_ready, similar_count]
├── F6_PRODUCE      [bytes, sections, density]
├── F7_GOVERN       [score, gates_pass, gates_total, 12lp]
└── F8_COLLABORATE  [path, compiled, committed, signal]
```

## Span Attributes
| Attribute | Type | Example |
|-----------|------|---------|
| cex.nucleus | string | "n03" |
| cex.kind | string | "agent" |
| cex.builder | string | "agent-builder" |
| cex.model | string | "claude-opus-4-6" |
| cex.tokens_in | int | 15000 |
| cex.tokens_out | int | 3200 |
| cex.quality_score | float | 8.5 |
| cex.mission | string | "BRAND_LAUNCH" |

## Selective Capture Rules
| Condition | Capture Prompts | Capture Responses |
|-----------|----------------|-------------------|
| F7 score >= 8.0 | false | false |
| F7 score < 8.0 | true | true |
| F7 HARD gate fail | true | true |
| Error/exception | true | true |

## Backend Options
| Backend | Protocol | Storage | UI |
|---------|----------|---------|-----|
| Jaeger | OTLP | Badger/Cassandra | built-in |
| Grafana Tempo | OTLP | S3/GCS | Grafana |
| Console | stdout | none | terminal |
| JSON file | file | .cex/traces/ | jq |

## Boundary
trace_config IS: observability rules for what execution data to capture, sample, and export during agent runs.
trace_config IS NOT: a reasoning trace (captured thought process), a quality gate (pass/fail rules), or a session backend (state persistence).
