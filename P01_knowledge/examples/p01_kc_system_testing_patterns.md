---
id: p01_kc_system_testing_patterns
kind: knowledge_card
kc_type: domain_kc
pillar: P01
title: "System Testing Patterns for Agent and LLM Pipelines"
version: "1.0.0"
created: "2026-04-12"
updated: "2026-04-12"
author: "n03"
domain: software_testing
subdomain: quality_assurance
quality: null
tags: [system-testing, e2e, integration, smoke, regression, golden-test, cex-sdk]
tldr: "7 canonical system-test patterns: smoke, regression, e2e, contract, golden, load, chaos — each maps to a CEX eval kind and a distinct assertion target."
when_to_use: "Designing test suites, auditing coverage gaps, or selecting test kinds for a new component, pipeline, or CEX nucleus."
keywords: [smoke-eval, regression-check, e2e-eval, golden-test, contract-test]
long_tails:
  - which test pattern to use for a new LLM pipeline component
  - difference between smoke test and regression test in agent systems
  - how to map CEX eval kinds to standard QA patterns
axioms:
  - ALWAYS run smoke before regression; a failing smoke invalidates all deeper tests
  - NEVER use golden tests for non-deterministic outputs without a fuzzy match threshold
  - IF adding a new nucleus THEN add contract tests at every input/output boundary
linked_artifacts:
  primary: null
  related: [p01_kc_rag_fundamentals, p07_benchmark_cex_sdk]
density_score: 0.87
data_source: "https://martinfowler.com/articles/microservice-testing/"
---

# System Testing Patterns for Agent and LLM Pipelines

## Quick Reference
```yaml
topic: system_testing_patterns
scope: Agent pipelines, LLM systems, CEX nuclei
owner: n05
criticality: high
pattern_count: 7
cex_tool: cex_system_test.py (54 tests)
```

## Pattern Reference Table

| Pattern | When to Apply | Key Assertion | CEX Kind | Failure Cost |
|---------|--------------|---------------|----------|--------------|
| Smoke | After any deploy or nucleus boot | Critical paths return non-error | `smoke_eval` | Blocks all other tests |
| Regression | Before merge, after refactor | Outputs match prior baseline | `regression_check` | High — silent drift |
| End-to-End | Full mission or pipeline change | User goal achieved end-to-end | `e2e_eval` | High — integration gap |
| Contract | At service/nucleus boundaries | I/O schema matches declared spec | `validation_schema` | Medium — breaks consumers |
| Golden | Deterministic output components | Output byte-matches snapshot | `golden_test` | Low — easy to update |
| Load | Before scaling or peak events | Latency + throughput within SLA | `benchmark` | High if missed |
| Chaos | Resilience audits, pre-release | System recovers from injected fault | `guardrail` | Critical if production |

## Test Pyramid Position

| Layer | Pattern | Coverage Target | Failure Cost | Run Frequency |
|-------|---------|----------------|-------------|---------------|
| Top (System) | Chaos, Load | 5-10% of suite | Highest | Weekly |
| Mid (Integration) | E2E, Contract | 20-30% | High | Per PR |
| Base (Component) | Smoke, Regression, Golden | 60-70% | Medium | Per commit |

## CEX Tool Map

| cex_system_test.py check | Pattern | Nucleus |
|--------------------------|---------|---------|
| Builder boot validation | Smoke | N03, N05 |
| Artifact frontmatter schema | Contract | N03, N04 |
| Compiled output diff | Regression | N05 |
| Signal round-trip | E2E | N07 |
| Quality score stability | Golden | N05 |
| Token budget enforcement | Load | N07 |
| Dispatch recovery on crash | Chaos | N07 |

## Anti-Patterns

- Over-mocking: mocking nucleus I/O hides real integration failures at boundaries
- Skipping smoke: running 54 regression checks before smoke wastes time on a dead system
- No contract tests: schema drift between nuclei discovered only in production
- Golden tests on LLM text: byte-match fails on rephrasing; use semantic similarity >= 0.92

## References

- Fowler, "Microservice Testing": https://martinfowler.com/articles/microservice-testing/
- CEX tool: `_tools/cex_system_test.py` (54 tests, covers all 7 patterns)
- CEX kinds: `smoke_eval`, `regression_check`, `e2e_eval`, `golden_test`, `benchmark`, `guardrail`
- Related KC: `p01_kc_rag_fundamentals` (pipeline structure tested by E2E pattern)