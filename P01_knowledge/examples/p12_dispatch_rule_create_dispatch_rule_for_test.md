---
id: p12_dr_test
kind: dispatch_rule
pillar: P12
version: 1.0.0
created: 2026-04-02
updated: 2026-04-02
author: dispatch-rule-builder
domain: testing
quality: 9.0
tags: [dispatch, test, qa, executor, coverage, validation, pytest]
tldr: Route test, QA, and validation tasks to executor agent_group for automated test execution
scope: test
keywords: [test, testing, pytest, coverage, qa, validar, testar, fixture, assert, automation, spec, verificar]
agent_group: executor
model: opus
priority: 8
confidence_threshold: 0.72
fallback: builder
conditions:
  exclude_domains: [deploy, monitoring]
load_balance: false
routing_strategy: hybrid
density_score: 0.79
title: "P12 Dispatch Rule Create Dispatch Rule For Test"
---
# test Dispatch Rule

## Purpose
Routes testing, QA, and validation tasks to the executor agent_group. Covers unit tests,
integration tests, coverage reporting, fixture setup, and assertion-based spec validation.
Executor carries test-optimized tooling (pytest, coverage.py) and is the authoritative
target for all automated quality verification workflows.

## Keyword Rationale
Bilingual PT/EN coverage ensures both `testar`/`validar` (Portuguese operator commands)
and `pytest`/`coverage`/`fixture` (English technical terms) activate routing. `spec` and
`assert` catch adjacent sub-tasks like BDD specs and assertion-level debugging.
Generic terms like `test` and `qa` are retained because the confidence threshold (0.72)
filters low-signal matches; these keywords only fire when co-occurring with domain context.

## Fallback Logic
`builder` (N03) handles construction of test scaffolding and test artifact templates when
executor is unavailable. Builder cannot run tests but can produce test files, fixtures,
and test configs — a useful partial degradation that preserves progress without blocking
the pipeline entirely.

## Cross-References

- **Pillar**: P12 (Orchestration)
- **Kind**: `dispatch rule`
- **Artifact ID**: `p12_dr_test`
- **Tags**: [dispatch, test, qa, executor, coverage, validation, pytest]

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P12 | Orchestration domain |
| Kind `dispatch rule` | Artifact type |
| Pipeline | 8F (F1→F8) |

## Artifact Metadata

```yaml
kind: dispatch_rule
pillar: P12
pipeline: 8F
scoring: hybrid_3_layer
compilation: cex_compile
```
