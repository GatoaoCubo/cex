---
id: p01_kc_system_testing_patterns
kind: knowledge_card
kc_type: domain_kc
pillar: P01
title: "System Testing Patterns: Smoke to Chaos"
version: "1.0.0"
created: "2026-04-12"
updated: "2026-04-12"
author: "knowledge-card-builder"
domain: software-testing
subdomain: system-validation
quality: null
tags: [testing, system-test, integration, e2e, smoke, chaos, qa, patterns]
tldr: "7 system-test patterns — smoke to chaos — with trigger conditions, failure signals, and cost/coverage tradeoffs."
when_to_use: "When designing a test strategy, selecting a test type, or auditing coverage gaps in a suite."
keywords: [smoke-test, regression, integration-test, e2e, chaos-engineering]
long_tails:
  - "when to use smoke vs sanity test in CI pipeline"
  - "how to choose between integration and end-to-end tests"
  - "chaos engineering vs performance testing difference"
axioms:
  - "ALWAYS run smoke before regression — fail fast on broken deployments"
  - "NEVER use E2E as the primary coverage layer — maintenance cost is O(n^2)"
  - "IF failure isolation matters THEN prefer integration over E2E"
linked_artifacts:
  primary: null
  related: [p07_qg_artifact_quality_gate]
density_score: 0.87
data_source: "https://martinfowler.com/articles/practical-test-pyramid.html"
---

# System Testing Patterns: Smoke to Chaos

## Quick Reference
```yaml
topic: system_testing_patterns
scope: 7 canonical test types for system-level validation
owner: qa-engineering
criticality: high
```

## Pattern Taxonomy

| Pattern | Intent | Trigger | Key Failure Signal |
|---------|--------|---------|-------------------|
| **Smoke** | Verify system boots and critical paths exist | Post-deploy, pre-regression | Service unreachable, 5xx on main routes |
| **Sanity** | Confirm recent change did not break adjacent area | Post-hotfix, pre-release | Regression in previously passing critical path |
| **Regression** | Detect reintroduced defects across full baseline | Pre-release, nightly | Known-good scenario fails after commit |
| **Integration** | Validate contracts between two components | Post-merge of cross-service change | Mismatched schema, unexpected side effect |
| **E2E** | Simulate complete user journey across stack | Release gate, critical workflow change | Journey fails at any node in the flow |
| **Performance** | Measure throughput, latency under target load | Pre-release, infra change | p99 latency exceeds SLO, CPU saturation |
| **Chaos** | Confirm resilience under controlled failure injection | Quarterly or post-incident | System degrades unacceptably under partial failure |

## Selection Decision Tree

```
New deployment?
  YES -> run Smoke first
         PASS -> run Regression
         FAIL -> stop, rollback

Hotfix on single component?
  YES -> run Sanity (not full Regression)

Cross-service contract changed?
  YES -> Integration test for both sides

User-visible critical workflow changed?
  YES -> E2E on that workflow

Infra scaled or algo changed?
  YES -> Performance test under peak load model

SLA / DR audit?
  YES -> Chaos (schedule, not on every deploy)
```

## Tradeoff Matrix

| Pattern | Speed | Coverage | Maintenance Cost | Failure Isolation |
|---------|-------|----------|-----------------|-------------------|
| Smoke | High | Low | Low | High |
| Sanity | High | Low | Low | High |
| Regression | Med | High | Med | Med |
| Integration | Med | Med | Med | High |
| E2E | Low | High | High | Low |
| Performance | Low | Narrow | Med | High |
| Chaos | Low | Narrow | High | Med |

## Anti-Patterns

| Anti-Pattern | Consequence | Fix |
|-------------|-------------|-----|
| E2E as primary layer | Flaky suite, O(n^2) maintenance as paths grow | Move coverage to Integration; reserve E2E for 3-5 critical journeys |
| Skipping Smoke in CD | Regression suite wastes time on broken deploys | Gate regression on Smoke PASS |
| Chaos without steady-state baseline | No way to define "unacceptable degradation" | Define SLO thresholds before first chaos run |

## Boundary Note

This KC covers system-level tests (post-build, running against real or containerized services).
Out of scope: unit tests, mutation testing, property-based testing, TDD practices.

## References

- Source: https://martinfowler.com/articles/practical-test-pyramid.html
- Chaos principles: https://principlesofchaos.org/
- Related: IEEE 829 Test Documentation Standard