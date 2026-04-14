---
kind: examples
id: bld_examples_plugin
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of plugin artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.1
title: "Examples Plugin"
version: "1.0.0"
author: n03_builder
tags: [plugin, builder, examples]
tldr: "Golden and anti-examples for plugin construction, demonstrating ideal structure and common pitfalls."
domain: "plugin construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Examples: plugin-builder

This ISO defines a plugin contract: the extension surface a host uses to load, register, and invoke external capability.
## Golden Example
INPUT: "Create a plugin for exporting metrics to external monitoring systems"
OUTPUT:
```yaml
id: p04_plug_metrics_exporter
kind: plugin
pillar: P04
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder"
interface: "MetricsExporterInterface"
lifecycle: [on_load, on_enable, on_disable, on_unload, on_config_change]
enabled: true
api_surface_count: 4
dependencies: []
domain: "observability"
quality: null
tags: [plugin, metrics, exporter, P04, observability, monitoring]
tldr: "Exports agent metrics (tool usage, latency, errors) to external monitoring endpoints"
isolation: "shared"
hot_reload: true
config_schema:
  endpoint_url:
    type: "string"
    default: "http://localhost:9090/metrics"
    required: true
    description: "Monitoring endpoint URL"
  flush_interval_ms:
    type: "integer"
    default: 10000
    required: false
    description: "How often to flush buffered metrics"
  format:
    type: "string"
    default: "prometheus"
    required: false
    description: "Export format (prometheus, json, statsd)"
version_constraints: ">=1.0.0"
priority: 50
keywords: [metrics-export, monitoring, prometheus, observability-plugin]
density_score: 0.90
```
## Interface Contract
Implements: MetricsExporterInterface
Contract: accepts metric events (counter, gauge, histogram) and exports them to external endpoints.
Required methods:
- record_metric: accept metric name, value, labels, and buffer for export
- flush: send all buffered metrics to configured endpoint
- health_check: verify endpoint connectivity
## API Surface
| Method | Input | Output | Description | Idempotent |
|--------|-------|--------|-------------|------------|
| record_metric | name: str, value: float, labels: dict | void | Buffer metric for next flush | false |
| flush | none | {exported: int, errors: int} | Send buffered metrics to endpoint | true |
| health_check | none | {status: str, latency_ms: int} | Check endpoint connectivity | true |
| get_stats | none | {buffered: int, exported: int} | Return export statistics | true |
## Configuration
```yaml
endpoint_url: "http://localhost:9090/metrics"  # Monitoring endpoint
flush_interval_ms: 10000                        # Flush every 10s
format: "prometheus"                             # Export format
```
## Lifecycle Hooks
- **on_load**: Initialize metric buffer, validate endpoint_url format
- **on_enable**: Start flush timer, verify endpoint with health_check
- **on_disable**: Flush remaining metrics, stop timer
- **on_unload**: Final flush, release buffer memory
- **on_config_change**: Update endpoint/interval without restart (hot-reload)
## Dependencies
None (standalone plugin, no external plugin dependencies).
## Testing
- Unit: mock endpoint, verify record_metric buffers and flush serializes correctly
- Integration: spin up local Prometheus, verify metrics appear after flush
- Mock: MetricsExporterInterface mock for downstream consumers
WHY THIS IS GOLDEN:
- quality: null (H05 pass) | id p04_plug_ pattern (H02 pass) | kind: plugin (H04 pass)
- 23 fields present (H06 pass) | api_surface_count: 4 matches table (H07 pass)
- lifecycle includes on_load + on_unload (H08 pass) | hot_reload + on_config_change (H09 pass)
- tldr: 79ch (S01 pass) | tags: 6 items (S02 pass) | Interface Contract present (S03 pass)
- API Surface 4 rows (S04 pass) | Configuration present (S05 pass) | Lifecycle 5 events (S06 pass)
- Dependencies present (S07 pass) | Testing present (S08 pass) | isolation: shared (S09 pass)
- config_schema 3 fields (S10 pass) | version_constraints set (S11 pass) | density: 0.90 (S12 pass)
## Anti-Example
INPUT: "Make a plugin"
BAD OUTPUT:
```yaml
id: cool_plugin
kind: extension
pillar: P02
lifecycle: []
api_surface_count: 0
quality: 9.0
tags: [plugin]
tldr: "This plugin is designed to extend the system with various capabilities and features."
