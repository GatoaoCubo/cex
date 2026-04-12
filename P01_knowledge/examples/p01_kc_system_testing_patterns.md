---
id: p01_kc_system_testing_patterns
kind: knowledge_card
pillar: P01
title: "System Testing Patterns: Scope, Coverage, and Failure Classification"
version: "1.1.0"
created: "2026-04-12"
updated: "2026-04-12"
author: "knowledge-card-builder"
domain: software-testing
quality: null
tags: [testing, system-testing, integration, e2e, test-patterns, qa, coverage, knowledge]
tldr: "6 test pattern types mapped by isolation, speed, confidence; scope decision matrix, order heuristics, 5 failure classes, and coverage strategies."
when_to_use: "When designing test suites, classifying failures, choosing test scope, or auditing coverage gaps in a multi-layer system."
keywords: [system-testing, e2e, integration-test, test-coverage, failure-classification]
long_tails:
  - "When to use end-to-end tests vs integration tests vs unit tests"
  - "How to classify test failures by ownership and resolution path"
  - "Execution order for test suites to maximize feedback speed"
  - "Coverage strategies for multi-layer artifact validation pipelines"
axioms:
  - "ALWAYS run fast isolated tests before slow integrated tests"
  - "NEVER report coverage percentage without specifying the coverage dimension"
  - "IF a test fails intermittently, classify as environment before blaming code"
linked_artifacts:
  primary: null
  related: [p07_qg_system_gate, p01_kc_rag_fundamentals]
density_score: 0.88
data_source: "https://martinfowler.com/articles/practical-test-pyramid.html"
---

# System Testing Patterns: Scope, Coverage, and Failure Classification

## Quick Reference
```yaml
topic: system_testing_patterns
scope: multi-layer test design, failure classification, coverage
owner: knowledge-card-builder
criticality: high
```

## Pattern Taxonomy

| Pattern | Scope | Trigger | Isolation | Speed | Confidence Signal |
|---------|-------|---------|-----------|-------|-------------------|
| Unit | Single function/class | Logic change | Full | <1ms | Logic bugs |
| Integration | 2+ components, real deps | API/boundary change | Partial | 10-500ms | Contract bugs |
| System (E2E) | Full stack, real env | Release gate | None | 1-60s | Regression |
| Smoke | Critical paths only | Deploy | None | <30s | Liveness |
| Contract | API schema, SLA boundary | Interface change | Mocked | ~100ms | Compatibility |
| Property | Input space, invariants | Algorithm change | Partial | varies | Edge cases |

## Test Scope Decision Matrix

| Condition | Choose |
|-----------|--------|
| Logic, no I/O, no state | Unit |
| DB query, cache, or external call | Integration |
| User journey, multi-service flow | System/E2E |
| Post-deploy health check | Smoke |
| Cross-team API boundary | Contract |
| State machines, parsers, converters | Property |
| CI speed constraint (<5 min) | Unit + Smoke |
| Release gate | System + Smoke |

## Execution Order Heuristics

| Rule | Rationale | Anti-pattern |
|------|-----------|-------------|
| Unit first, E2E last | Isolate logic failures early | E2E-first wastes 10min on a logic bug |
| Smoke before full suite | Fail fast on infra issues | Full suite on broken env = false failures |
| Stable before flaky | Deterministic signal before probabilistic | Mixed order = noisy CI dashboards |
| Shortest first per layer | Maximize parallel feedback | All long tests together = bottleneck |
| Independent before chained | Avoid cascade masking root cause | Sequential tests = ambiguous failures |

## Coverage Strategies

| Strategy | Measures | Gap Risk | CEX Context |
|----------|----------|----------|-------------|
| Line/statement | Code executed | Misses branch logic | cex_system_test.py (54 tests) |
| Branch | Decision paths | Misses data-driven paths | Schema + frontmatter gate |
| Mutation | Test quality (kill rate) | Expensive, slow | Manual for core pipeline |
| Behavioral | User stories, contracts | Misses edge inputs | 12LP checklist (12 points) |
| Exploratory | Unknown unknowns | Unstructured, hard to repeat | cex_doctor.py scan |

## Failure Classification

| Class | Diagnosis Signal | Ownership | Resolution |
|-------|-----------------|-----------|------------|
| Logic | Deterministic, reproducible | Author | Fix code, add unit test |
| Environment | Intermittent, env-dependent | Infra/DevOps | Pin deps, isolate env |
| Data | Specific input/fixture triggers | Author | Add fixture, sanitize data |
| Timing | Race condition, flaky under load | Author/Infra | Add retry, fix async order |
| Contract | Interface mismatch, schema drift | API owner | Align contract, add contract test |

## CEX Application

- `cex_system_test.py`: 54 tests across integration + system scope
- `cex_doctor.py`: smoke-style health check (builder + schema liveness)
- `cex_hooks.py`: pre-commit gate (ASCII rule + frontmatter contract tests)
- F7 GOVERN: behavioral coverage via 12LP checklist + H01-H07 hard gates
- Failure triage: deterministic = logic class; intermittent = environment class

## References

- Fowler, M. "Practical Test Pyramid": https://martinfowler.com/articles/practical-test-pyramid.html
- Related: p07_qg_system_gate, cex_system_test.py (54 tests), cex_doctor.py