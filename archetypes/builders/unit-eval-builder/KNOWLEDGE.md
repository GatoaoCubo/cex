---
pillar: P01
llm_function: INJECT
purpose: Standards and patterns for unit_eval production
sources: [pytest, unittest, xUnit, CEX validate_kc.py]
---

# Domain Knowledge: unit_eval

## Foundational Concepts
Unit testing originates from xUnit frameworks (JUnit, pytest, unittest).
Tests one unit in isolation: single function, single agent, single prompt.
In CEX: tests one agent/prompt's correctness by comparing actual output against expected output with gate-mapped assertions.

## Industry Patterns
| Source | What it defines | CEX alignment |
|--------|----------------|---------------|
| pytest | Fixtures, parametrize, assertions | setup/teardown, assertions list |
| xUnit | Arrange-Act-Assert | setup -> input -> assertions |
| Property-based | Hypothesis, QuickCheck | edge_case coverage |
| Snapshot testing | Jest snapshots | expected_output comparison |

## Key Principles
- Test ONE thing per unit_eval (single responsibility)
- Assertions must be CONCRETE (exact values, not "should be good")
- Setup isolates the test from external state
- Teardown prevents test pollution
- Edge cases need separate unit_evals
- Timeout prevents infinite loops (default 60s)

## CEX-Specific Extensions
| Field | Justification | Closest equivalent |
|-------|--------------|-------------------|
| gate_ref | Maps assertion to quality gate | pytest marker |
| target_kind | Scopes test to artifact type | pytest fixture parametrize |
| coverage_scope | Documents what gates are covered | pytest-cov scope |

## Boundary vs Nearby Types
| Type | What it is | Why it is NOT unit_eval |
|------|------------|------------------------|
| smoke_eval (P07) | Quick sanity check <30s | No depth; pass/fail only |
| e2e_eval (P07) | Pipeline integration test | Tests multiple agents together |
| golden_test (P07) | Reference at 9.5+ | Calibration, not verification |
| benchmark (P07) | Performance measurement | Latency/cost, not correctness |

## References
- pytest: https://docs.pytest.org/
- xUnit Patterns: http://xunitpatterns.com/
- CEX validate_kc.py (HARD/SOFT gate pattern)
