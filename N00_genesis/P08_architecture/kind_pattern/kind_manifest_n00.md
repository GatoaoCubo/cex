---
id: n00_pattern_manifest
kind: knowledge_card
8f: F3_inject
pillar: P08
nucleus: n00
title: "Pattern -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, pattern, p08, n00, archetype, template]
density_score: 0.99
related:
  - bld_schema_reranker_config
  - bld_schema_integration_guide
  - bld_schema_pattern
  - bld_schema_pitch_deck
  - bld_schema_benchmark_suite
  - bld_schema_usage_report
  - bld_schema_dataset_card
  - bld_schema_search_strategy
  - bld_schema_sandbox_spec
  - bld_schema_sandbox_config
---

<!-- 8F: F1=knowledge_card P08 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A pattern is a reusable architectural or operational solution to a recurring problem, documented in a form that builders can inject into their context and apply without reinvention. Examples include continuous batching, RAG retrieval patterns, circuit breaker, and retry-with-backoff. Patterns accelerate production by encoding proven approaches as first-class CEX artifacts.

## Pillar
P08 -- architecture

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `pattern` |
| pillar | string | yes | Always `P08` |
| title | string | yes | Human-readable pattern name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| problem | string | yes | The recurring problem this pattern solves |
| solution | string | yes | How the pattern solves it |
| trade_offs | string | yes | Known downsides or constraints |
| when_to_use | list | yes | Conditions that indicate this pattern applies |
| when_not_to_use | list | no | Anti-use-cases |
| implementation_sketch | string | no | Pseudocode or structural outline |
| examples | list | no | Real implementations in the codebase |

## When to use
- Documenting a solution that has been successfully applied 2+ times across nuclei
- Providing builders with a proven approach before they start F6 PRODUCE
- Building a pattern library for common AI engineering challenges

## Builder
`archetypes/builders/pattern-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind pattern --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: pattern_retry_backoff
kind: pattern
pillar: P08
nucleus: n05
title: "Retry with Exponential Backoff"
version: 1.0
quality: null
---
problem: Transient API failures cause mission aborts
solution: Retry failed calls with exponential backoff up to max_retries
trade_offs: Adds latency; masks persistent failures if max_retries too high
when_to_use: [rate_limit_errors, network_timeouts, 5xx_responses]
implementation_sketch: |
  for attempt in range(max_retries):
      try: return call()
      except TransientError: sleep(2**attempt)
```

## Related kinds
- `workflow` (P12) -- workflows that implement patterns as sequenced steps
- `bugloop` (P11) -- applies retry patterns to auto-fix loops
- `runtime_rule` (P09) -- encodes pattern parameters (max_retries, backoff_ms) as config

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_reranker_config]] | upstream | 0.46 |
| [[bld_schema_integration_guide]] | upstream | 0.45 |
| [[bld_schema_pattern]] | upstream | 0.44 |
| [[bld_schema_pitch_deck]] | upstream | 0.44 |
| [[bld_schema_benchmark_suite]] | upstream | 0.43 |
| [[bld_schema_usage_report]] | upstream | 0.43 |
| [[bld_schema_dataset_card]] | upstream | 0.42 |
| [[bld_schema_search_strategy]] | upstream | 0.42 |
| [[bld_schema_sandbox_spec]] | upstream | 0.42 |
| [[bld_schema_sandbox_config]] | upstream | 0.42 |
