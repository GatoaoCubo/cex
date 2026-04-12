---
id: p01_kc_system_testing_patterns
kind: knowledge_card
kc_type: meta_kc
pillar: P01
title: "System Testing Patterns — Smoke, Integration, E2E, Regression"
version: "1.0.0"
created: "2026-04-12"
updated: "2026-04-12"
author: "N04"
domain: testing
quality: null
tags: [system-test, integration-test, e2e, regression, smoke-test, validation, cex]
tldr: "4 pattern families gate system quality: smoke (alive?), integration (contracts?), e2e (golden path?), regression (no drift?)."
when_to_use: "Before deploy, after major refactors, as CI gate, or when validating multi-component flows."
keywords: [system-test, smoke-test, integration-test, regression, e2e-test]
long_tails:
  - when to run smoke tests vs integration tests
  - how to classify a system test failure by root cause
  - what patterns cover multi-component validation in CI
axioms:
  - ALWAYS run smoke before integration — a dead process cannot have contract bugs
  - NEVER use unit mocks in e2e tests — mock boundaries invalidate golden path coverage
  - IF regression baseline is missing THEN generate it before merging, not after
linked_artifacts:
  primary: null
  related: [p01_kc_cex_system_test_suite]
density_score: 0.87
data_source: "https://martinfowler.com/articles/practical-test-pyramid.html"
---

# System Testing Patterns — Smoke, Integration, E2E, Regression

## Quick Reference
```yaml
topic: system_testing_patterns
scope: multi-component validation (not unit tests)
owner: N04 / N05
criticality: high
cex_tool: _tools/cex_system_test.py (54 tests)
```

## Pattern Taxonomy

| Pattern | Scope | Trigger | Pass Criteria | Typical Count |
|---------|-------|---------|---------------|---------------|
| Smoke | Process alive, config valid | Every deploy | Exit 0, no crash | 3-10 |
| Integration | Component boundary contracts | PR merge, dependency bump | All contracts satisfied | 10-30 |
| E2E | Full golden path, real I/O | Release gate, nightly | Output matches expected fixture | 5-15 |
| Regression | No drift from baseline | Refactor, model update | Delta within threshold | 20-100 |

## Smoke Tests
- **Purpose**: fastest possible alive-check — is the system bootable?
- **Checks**: process starts, config loads, DB reachable, required env vars set
- **SLA**: must complete in < 30 s; if > 30 s, scope is wrong
- **On failure**: stop pipeline immediately — no value running deeper tests

## Integration Tests
- **Purpose**: validate contracts between two components at their boundary
- **Boundary types**: API schema, event payload, DB row shape, file format
- **Data**: use deterministic fixtures, never prod snapshots
- **Anti-pattern**: testing internal state instead of the boundary output

## End-to-End (E2E) Tests
- **Purpose**: validate complete user-facing flow from input to final output
- **Coverage target**: golden path first; edge cases only after golden passes
- **Environment**: real infra or hermetic replica — no mocks past the boundary
- **Fixture strategy**: record-and-replay for external APIs; seed DB before each run

## Regression Tests
- **Purpose**: detect unintended drift from a known-good baseline snapshot
- **Baseline storage**: commit snapshot artifacts alongside code (`tests/snapshots/`)
- **Diff strategy**: exact match for deterministic outputs; tolerance for LLM outputs
- **Update flow**: human approves diff → commit new baseline → CI green

## Failure Classification

| Failure Type | Root Cause Signal | Resolution Path |
|-------------|-------------------|----------------|
| Smoke fails | Process crash / missing config | Fix env or boot before any other work |
| Integration fails | Schema mismatch / version skew | Align producer and consumer schemas |
| E2E fails | Logic regression or infra gap | Reproduce locally, add unit test, fix |
| Regression fails | Intentional change or model drift | Review diff, approve or revert |
| Flaky | Timing, order dependence, external I/O | Isolate with retry budget, then fix root |

## Decision Matrix

| Situation | Use Pattern |
|-----------|-------------|
| First check after deploy | Smoke |
| New API endpoint added | Integration |
| Full feature shipped to user | E2E (golden path) |
| Prompt or model version bumped | Regression |
| CI gate for every PR | Smoke + Integration |
| Nightly quality gate | All 4 in sequence |
| CEX pipeline validation | `cex_system_test.py` (54 tests, covers all 4) |

## Golden Rules
- ALWAYS run patterns in order: smoke -> integration -> e2e -> regression
- NEVER let a flaky test block CI — quarantine it, file a ticket, fix within 48 h
- ALWAYS tie regression baselines to a commit SHA, not a date
- IF smoke fails in production THEN rollback immediately, do not debug in prod

## References
- Fowler, M. "Practical Test Pyramid": https://martinfowler.com/articles/practical-test-pyramid.html
- CEX tool: `_tools/cex_system_test.py` — 54 tests across all 4 pattern families
- Related: `_tools/cex_hooks.py` — pre-commit smoke gate integration