---
kind: quality_gate
id: p11_qg_plugin
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of plugin artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.0
title: "Gate: plugin"
version: "1.0.0"
author: "builder_agent"
tags: [quality-gate, plugin, P11, P04, governance, extensibility, lifecycle]
tldr: "Gates for plugin artifacts — interface contract, lifecycle hooks, API surface, and isolation level defined."
domain: plugin
created: "2026-03-27"
updated: "2026-03-27"
density_score: 0.85
related:
  - bld_collaboration_plugin
  - bld_knowledge_card_plugin
  - plugin-builder
  - bld_architecture_plugin
  - p03_sp_plugin_builder
  - bld_tools_plugin
  - bld_schema_plugin
  - bld_memory_plugin
  - p01_kc_plugin
  - bld_output_template_plugin
---

## Quality Gate

# Gate: plugin

This ISO defines a plugin contract: the extension surface a host uses to load, register, and invoke external capability.
## Definition
| Field     | Value                                              |
|-----------|----------------------------------------------------|
| metric    | interface contract clarity + lifecycle completeness |
| threshold | 8.0                                                |
| operator  | >=                                                 |
| scope     | all plugin artifacts (P04)                         |
## HARD Gates
All must pass. Failure on any = final score 0.
| Gate | Check | Why |
|------|-------|-----|
| H01 | YAML frontmatter parses valid YAML | Broken YAML = plugin not loadable |
| H02 | id matches `^p04_plug_[a-z][a-z0-9_]+$` | Namespace compliance |
| H03 | id == filename stem | Brain search relies on this |
| H04 | kind == "plugin" | Type integrity |
| H05 | quality == null | Never self-score |
| H06 | All required fields present: id, kind, pillar, version, created, updated, author, domain, quality, tags, tldr | Completeness |
| H07 | interface field names the host interface or base class this plugin implements | A plugin without a declared interface is an orphan |
| H08 | lifecycle block declares at least on_load and on_unload handlers | Minimum lifecycle for safe load and teardown |
| H09 | api_surface list has >= 1 entry, each with method name, signature, and return type | Callers need a concrete API, not a description |
| H10 | If hot_reload: true, lifecycle MUST include on_config_change handler | Hot-reload without config handler causes stale state |
## SOFT Scoring
| Gate | Check | Weight |
|------|-------|--------|
| S01 | tldr <= 160 chars, non-empty | 1.0 |
| S02 | tags is list, len >= 3, includes "plugin" | 0.5 |
| S03 | density_score >= 0.80 | 0.5 |
| S04 | config_schema block defines >= 1 field with type and default value | 1.0 |
| S05 | dependencies list is present (empty list is valid if none) | 0.5 |
| S06 | isolation_level field states scope of side effects (process, thread, sandboxed, or none) | 1.0 |
| S07 | hot_reload field explicitly set to true or false | 0.5 |
| S08 | version_constraints field states compatible host version range (semver) | 1.0 |
| S09 | error_handling block describes behavior on lifecycle failure (log-and-continue, halt, or retry) | 1.0 |
| S10 | performance_impact field estimates resource overhead (negligible, low, medium, high) | 0.5 |
| S11 | security_notes block states whether plugin has network, filesystem, or subprocess access | 1.0 |
| S12 | No filler phrases ("this plugin", "designed to extend", "various capabilities") | 1.0 |
Weights sum: 9.5. Normalize: divide each by 9.5 before scoring.
## Actions
| Score | Action |
|-------|--------|
| >= 9.5 | GOLDEN — pool as reference plugin implementation for this interface |
| >= 8.0 | PUBLISH — register in plugin registry and enable for loading |
| >= 7.0 | REVIEW — complete config_schema, isolation level, or error handling |
| < 7.0  | REJECT — rework interface contract and lifecycle ofclarations |
## Bypass
| Field | Value |
|-------|-------|
| conditions | Critical capability gap requiring plugin in production before full review when interface is stable |
| approver | p04-chief |
| audit_trail | Log in records/audits/ with interface name, host version, and timestamp |
| expiry | 48h — plugin must pass all gates before next release tag |
| never_bypass | H01 (YAML), H05 (quality null) |

## Examples

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

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
