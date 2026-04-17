---
id: n00_runtime_rule_manifest
kind: knowledge_card
pillar: P09
nucleus: n00
title: "Runtime Rule -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, runtime_rule, p09, n00, archetype, template]
density_score: 1.0
---

<!-- 8F: F1=knowledge_card P09 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A runtime_rule defines operational constraints that govern agent execution at runtime: timeouts, retry limits, circuit breaker thresholds, and resource ceilings. It ensures that autonomous nucleus execution respects system stability boundaries and fails gracefully rather than hanging indefinitely or consuming unbounded resources.

## Pillar
P09 -- config

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `runtime_rule` |
| pillar | string | yes | Always `P09` |
| title | string | yes | Human-readable rule name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| scope | list | yes | Which nuclei or tools this rule governs |
| timeout_ms | integer | yes | Max execution time before timeout error |
| max_retries | integer | yes | Retry attempts on failure |
| retry_delay_ms | integer | no | Delay between retries (ms) |
| circuit_breaker | object | no | Circuit breaker settings |
| circuit_breaker.failure_threshold | integer | no | Failures before circuit opens |
| circuit_breaker.reset_timeout_s | integer | no | Seconds before circuit half-opens |
| max_memory_mb | integer | no | Memory ceiling before OOM kill |
| on_timeout | enum | no | kill \| signal \| log |

## When to use
- Setting timeouts for nucleus executions to prevent indefinite blocking
- Configuring circuit breakers for external API calls that may fail
- Establishing resource limits for local model inference processes

## Builder
`archetypes/builders/runtime_rule-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind runtime_rule --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: runtime_rule_nucleus_default
kind: runtime_rule
pillar: P09
nucleus: n07
title: "Default Nucleus Runtime Rules"
version: 1.0
quality: null
---
scope: [n01, n02, n03, n04, n05, n06]
timeout_ms: 2700000
max_retries: 2
retry_delay_ms: 5000
circuit_breaker:
  failure_threshold: 3
  reset_timeout_s: 120
on_timeout: signal
```

## Related kinds
- `pattern` (P08) -- retry-with-backoff patterns that runtime_rule configures
- `rate_limit_config` (P09) -- rate limits that interact with retry logic
- `invariant` (P08) -- runtime rules that are non-negotiable become invariants
