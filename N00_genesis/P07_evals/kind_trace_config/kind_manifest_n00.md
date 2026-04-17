---
id: n00_trace_config_manifest
kind: knowledge_card
pillar: P07
nucleus: n00
title: "Trace Config -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, trace_config, p07, n00, archetype, template]
density_score: 1.0
---

<!-- 8F: F1=knowledge_card P07 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Trace config defines the observability configuration for the 8F pipeline, specifying which spans to instrument, what attributes to capture per stage, the trace export destination, and sampling strategy. It enables distributed tracing across nucleus calls, tool invocations, and compilation steps using OpenTelemetry conventions. Trace data feeds performance analysis, bottleneck identification, and cost attribution.

## Pillar
P07 -- Evals

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `trace_config` |
| pillar | string | yes | Always `P07` |
| title | string | yes | System name + "Trace Config" |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| tracer_name | string | yes | OpenTelemetry tracer name |
| export_endpoint | string | yes | OTLP endpoint or local file path |
| sampling_rate | float | yes | Fraction of traces sampled (0.0-1.0) |
| spans | list | yes | Named spans with attributes captured per 8F stage |
| propagation_format | enum | yes | w3c / b3 / jaeger |

## When to use
- Instrumenting a new 8F pipeline for performance visibility
- Debugging a latency spike in a multi-nucleus workflow
- Building cost attribution by tracing token usage per pipeline stage

## Builder
`archetypes/builders/trace_config-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind trace_config --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- N05 operations implements; N01 intelligence analyzes traces
- `{{SIN_LENS}}` -- Gating Wrath: no pipeline call escapes measurement
- `{{TARGET_AUDIENCE}}` -- platform engineers and N07 orchestrator monitoring pipeline health
- `{{DOMAIN_CONTEXT}}` -- pipeline stages, trace backend, sampling budget

## Example (minimal)
```yaml
---
id: trace_config_cex_8f_pipeline
kind: trace_config
pillar: P07
nucleus: n05
title: "CEX 8F Pipeline Trace Config"
version: 1.0
quality: null
---
tracer_name: "cex.8f.pipeline"
sampling_rate: 0.10
propagation_format: w3c
export_endpoint: "http://localhost:4317"
spans:
  - {name: F1_constrain, attributes: [kind, pillar, nucleus]}
  - {name: F6_produce, attributes: [bytes_generated, density]}
  - {name: F8_collaborate, attributes: [compile_status, signal_sent]}
```

## Related kinds
- `eval_framework` (P07) -- framework that consumes trace data for eval analysis
- `benchmark` (P07) -- uses trace data to compute latency and cost metrics
- `streaming_config` (P05) -- streaming events may share the same trace context
