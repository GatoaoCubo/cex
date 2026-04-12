---
id: p01_kc_system_testing_patterns
kind: knowledge_card
pillar: P01
title: "System Testing Patterns"
version: "1.0.0"
created: "2026-04-12"
updated: "2026-04-12"
author: "n04"
domain: software_testing
quality: null
tags: [testing, system-testing, e2e, contract, smoke, regression, chaos, property-based, qa]
tldr: "7 canonical system-testing patterns: smoke, contract, regression, golden, chaos, property-based, E2E. Each targets a distinct failure class at process boundary or above."
when_to_use: "Designing test suites, selecting test strategies, or onboarding engineers to QA taxonomy."
keywords: [smoke-test, contract-test, regression-test, chaos-engineering, property-based-testing]
long_tails:
  - which system testing pattern to use for API boundary validation
  - how to choose between smoke test and regression test
  - when to apply chaos engineering vs property-based testing
  - snapshot testing vs golden file testing difference
axioms:
  - ALWAYS start new projects with smoke tests before adding regression or contract suites
  - NEVER skip golden file tests when serialized output format stability is required
  - IF a service boundary exists THEN add contract tests before E2E tests
  - NEVER run chaos tests in production without a defined SLO baseline first
linked_artifacts:
  primary: null
  related: []
density_score: 0.88
data_source: "https://martinfowler.com/articles/practical-test-pyramid.html"
---

# System Testing Patterns

## Quick Reference
```yaml
topic: system_testing_patterns
scope: backend, API, distributed systems, CLI tools
owner: n04
criticality: high
patterns: 7
boundary: process-level and above (not unit tests)
```

## Pattern Taxonomy

| Pattern | Trigger | Key Tooling | Failure Signal |
|---------|---------|-------------|----------------|
| Smoke | Every deploy | pytest, k6, Docker healthcheck | Deploy gate blocks — service dead |
| Contract | API boundary change | Pact, Schemathesis | Breaking change caught pre-deploy |
| Regression | Before release cut | pytest --last-failed, Newman | Known flow broken — rollback |
| Golden (snapshot) | Output format stabilization | pytest-snapshot, Jest toMatchSnapshot | Unexpected output diff |
| Chaos | Pre-production resilience | Chaos Monkey, Toxiproxy, Gremlin | Cascading failure, SLO breach |
| Property-based | Edge case discovery | Hypothesis (Py), fast-check (JS) | Counterexample found — edge case |
| E2E (user journey) | Critical user flows | Playwright, Cypress, Selenium | Critical path broken for user |

## Pattern Details

### Smoke
- Validates: service boots, health endpoints respond (200), DB reachable
- Scope: happy path only — narrow and fast (< 60 s)
- Anti-pattern: testing edge cases in smoke suite (slows pipeline gate)

### Contract
- Validates: producer/consumer API shape; schema compliance (OpenAPI/Pact)
- Pact: consumer-driven — consumer defines expectations, provider verifies
- Schemathesis: generates test cases from OpenAPI spec automatically

### Regression
- Validates: previously passing scenarios still pass after code change
- Pattern: record-and-replay using fixtures or VCR cassettes
- Gate: run with `--last-failed` first; full suite on merge to main

### Golden (Snapshot)
- Validates: serialized output matches approved baseline file byte-for-byte
- Update flow: diff appears -> human reviews -> `--snapshot-update` if intentional
- Anti-pattern: stale snapshots auto-approved without human review

### Chaos
- Validates: system tolerates infra failures (latency spike, crash, partition)
- Tooling tiers: Toxiproxy (network faults, local), Gremlin (cloud, SaaS)
- Prerequisite: SLO defined (p99 latency, error rate budget) before injection

### Property-Based
- Validates: function invariants hold across auto-generated random inputs
- Hypothesis shrinks failing inputs to minimal counterexample automatically
- Best targets: parsers, serializers, pure transforms, sorting/search functions

### E2E (User Journey)
- Validates: full user flow — UI through backend to persistence layer
- Anti-pattern: testing every edge case E2E (slow, brittle, hard to debug)
- Scope rule: E2E covers the 3-5 most critical user journeys only

## Selection Guide

```text
Starting a new service?
  -> Smoke (always first)
  -> Regression (on first stable release)
  -> Contract (at first external API boundary)

Mature system?
  -> Chaos (resilience audit — top 3 failure modes)
  -> Property-based (pure functions with invariants)
  -> E2E (3-5 critical user journeys max)

Output format must be stable?
  -> Golden/Snapshot tests mandatory
```

## Maturity Ladder

| Stage | Add | Min Coverage Target |
|-------|-----|---------------------|
| 0 — MVP | Smoke | 1 health + 1 core path |
| 1 — Beta | + Regression | All critical user flows |
| 2 — GA | + Contract | All external API surfaces |
| 3 — Scale | + Chaos | Top 3 infra failure modes |
| 4 — Mature | + Property-based | All pure functions with invariants |

## Boundaries

- Does NOT cover: unit tests, load/perf, SAST/DAST security scanning
- Does NOT cover: mutation testing, fuzzing (distinct disciplines)
- Scope: process boundary and above — a network-crossing smoke test is in
  scope; a function-level assertion is not

## References
- Practical Test Pyramid: https://martinfowler.com/articles/practical-test-pyramid.html
- Pact contract testing: https://docs.pact.io/
- Hypothesis property-based: https://hypothesis.readthedocs.io/en/latest/
- Schemathesis OpenAPI fuzzing: https://schemathesis.readthedocs.io/