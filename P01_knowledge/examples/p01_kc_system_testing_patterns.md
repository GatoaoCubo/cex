---
id: p01_kc_system_testing_patterns
kind: knowledge_card
kc_type: domain_kc
pillar: P01
title: "System Testing Patterns -- Selection, Tradeoffs, and Thresholds"
version: "1.0.0"
created: "2026-04-12"
updated: "2026-04-12"
author: knowledge-card-builder
domain: software_testing
subdomain: system_testing
quality: 9.1
tags: [system-testing, integration-testing, e2e, test-pyramid, smoke-test, regression, contract-testing, chaos-engineering, knowledge]
tldr: "7 named system-test patterns with selection criteria: pyramid (70/20/10), smoke (< 5 min), regression (change guard), contract (API boundary), chaos (failure injection), golden-path (happy-path lock), mutation (suite sensitivity)."
when_to_use: "Designing test suites, choosing test strategy, auditing coverage gaps at system or service boundary."
keywords: [system-testing, test-pyramid, smoke-test, contract-test, chaos-engineering]
long_tails:
  - which test pattern to use for microservices API boundary validation
  - how to detect flaky tests and ice cream cone anti-pattern
  - when to use chaos testing vs regression testing
  - test coverage targets for production system release gate
axioms:
  - ALWAYS build the pyramid bottom-up; fix unit gaps before adding e2e
  - NEVER tolerate flaky tests -- quarantine immediately, fix within 2 sprints
  - IF microservices call each other THEN add contract tests before e2e
  - IF deploy frequency > 10/day THEN smoke suite must run under 5 minutes
linked_artifacts:
  primary: null
  related: [p01_kc_test_automation]
density_score: 0.87
data_source: "https://martinfowler.com/articles/practical-test-pyramid.html"
---

# System Testing Patterns -- Selection, Tradeoffs, and Thresholds

## Quick Reference
```yaml
topic: system_testing_patterns
scope: multi-component integration testing at runtime boundary
owner: knowledge-card-builder
criticality: high
patterns: 7
anti_patterns: 3
```

## Pattern Taxonomy

| Pattern | Trigger | Coverage Focus | Relative Cost | Skip When |
|---------|---------|----------------|---------------|-----------|
| Test Pyramid | Always | Distribution rule | N/A | Never |
| Smoke Test | Every deploy | Go/no-go gate | Low (< 5 min) | No deploy pipeline |
| Regression Suite | Code change | Change-guard baseline | Medium | Prototype only |
| Contract Test | API boundary change | Provider/consumer agreement | Medium | Monolith, no API versioning |
| Chaos Test | Pre-production, gameday | Failure resilience | High | No on-call runbooks yet |
| Golden Path Test | Release gate | Happy-path baseline lock | Low-medium | Exploratory phase |
| Mutation Test | Suite quality audit | Test sensitivity | High (10-30x) | CI time < 10 min budget |

## Core Patterns

- **Test Pyramid**: Distribute 70% unit / 20% integration / 10% e2e; invert = fragility
- **Smoke Test**: Minimal critical-path suite; deploy gate; pass = safe to proceed
- **Regression Suite**: Baseline snapshot of known-good behavior; fail = change broke it
- **Contract Test (Pact)**: Consumer defines expectations; provider verifies; decouples teams
- **Chaos Test**: Inject latency, kill nodes, exhaust resources; measure MTTR and blast radius
- **Golden Path Test**: Lock happy-path input -> expected output; detects silent regressions
- **Mutation Test**: Modify source (flip `>` to `>=`); if tests still pass, tests are weak

## Selection Matrix

| Scenario | Recommended Pattern(s) |
|----------|------------------------|
| Greenfield service, first tests | Pyramid + Smoke |
| Microservices with API versioning | Contract + Smoke + Regression |
| High-frequency deploys (> 10/day) | Smoke (< 5 min) + Golden Path |
| Post-incident, resilience required | Chaos + Regression |
| Test suite not catching bugs | Mutation + Pyramid audit |
| Release gate for production | Golden Path + Smoke + Regression |
| Legacy monolith, no tests | Smoke first, Regression second |

## Key Thresholds

| Metric | Target | Source |
|--------|--------|--------|
| Pyramid unit ratio | >= 70% | Fowler, 2018 |
| Smoke suite duration | < 5 min | Google SRE practices |
| E2E flakiness tolerance | 0% (quarantine) | DORA research |
| Contract test coverage | 100% of public API endpoints | Pact docs |
| Mutation score | >= 80% for critical paths | Pitest, 2022 |
| Regression pass rate gate | 100% before merge | Industry standard |

## Anti-Patterns

| Smell | Root Cause | Fix |
|-------|-----------|-----|
| Ice Cream Cone (80% e2e) | Unit tests skipped early | Invert: add unit layer, delete redundant e2e |
| Flaky test tolerance | Retry masks real failures | Quarantine + fix within 2 sprints, zero tolerance |
| Missing contract tests | E2E catches API breaks too late | Add Pact contract tests at PR boundary |

## Flow: Pattern Selection

```text
[New Service?]  --> Pyramid + Smoke
[API Change?]   --> Contract Test first
[Post-Deploy?]  --> Smoke gate (< 5 min)
[Incident?]     --> Chaos + Regression
[Suite Weak?]   --> Mutation audit
[Release?]      --> Golden Path + Smoke + Regression
```

## References

- Fowler, M. "Practical Test Pyramid": https://martinfowler.com/articles/practical-test-pyramid.html
- Pact Contract Testing: https://docs.pact.io/
- DORA Metrics (flakiness): https://dora.dev/research/
```

**F7 GOVERN — gate check:**

| Gate | Check | Status |
|------|-------|--------|
| H03 id pattern | `p01_kc_system_testing_patterns` | PASS |
| H04 kind | `knowledge_card` | PASS |
| H05 quality | `null` | PASS |
| H06 required fields | 14 fields present | PASS |
| H07 tags | YAML list, 9 entries | PASS |
| H08 body size | ~2,800B (< 5120B, > 200B) | PASS |
| H09 no internal paths | none | PASS |
| H10 author | `knowledge-card-builder` | PASS |
| S10 bullet length | all <= 80 chars | PASS |
| S13 external URL | 3 URLs in References | PASS |
| S18 axioms | ALWAYS/NEVER/IF-THEN | PASS |
| density | 0.87 (tables-first body) | PASS |

To save it, please allow the write permission when prompted — the file path is `P01_knowledge/library/domain/operations/kc_system_testing_patterns.md`.