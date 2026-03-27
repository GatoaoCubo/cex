---
pillar: P01
llm_function: INJECT
purpose: Standards and patterns for smoke_eval production
sources: [smoke testing theory, CI/CD pipelines, health check patterns]
---

# Domain Knowledge: smoke_eval

## Foundational Concepts
Smoke testing originates from hardware testing ("does it catch fire when powered on?").
In software: quick sanity checks that verify basic functionality before investing in deeper tests.
In CEX: fast checks (<30s) that gate deeper evaluation — if smoke fails, skip unit/e2e tests.

## Industry Patterns
| Source | What it defines | CEX alignment |
|--------|----------------|---------------|
| CI/CD smoke stage | First test stage in pipeline | Gate before unit tests |
| Health endpoints | /health, /ready, /live | health_check field |
| Canary deploys | Quick validation after deploy | Post-deployment smoke |
| Circuit breakers | Fast failure detection | fast_fail: true |

## Key Principles
- SPEED over depth: 30s maximum, no exceptions
- BINARY outcome: pass or fail (no partial scores)
- FAST-FAIL: abort on first failure (no point continuing)
- CRITICAL PATH: only test what matters most
- GATE function: block deeper tests if smoke fails
- PREREQUISITES: document what must exist before running

## CEX-Specific Extensions
| Field | Justification | Closest equivalent |
|-------|--------------|-------------------|
| critical_path | Ordered minimum checks | CI stage dependencies |
| fast_fail | Abort on first failure | Circuit breaker pattern |
| frequency | How often to run | Cron schedule |

## Boundary vs Nearby Types
| Type | What it is | Why it is NOT smoke_eval |
|------|------------|--------------------------|
| unit_eval (P07) | Deep correctness test | Tests thoroughly; smoke is shallow |
| e2e_eval (P07) | Pipeline integration test | Tests full flow; smoke tests parts |
| benchmark (P07) | Performance measurement | Measures metrics; smoke checks binary |
| quality_gate (P11) | Pass/fail barrier with score | Blocks with score; smoke just checks |

## References
- Smoke Testing: https://en.wikipedia.org/wiki/Smoke_testing_(software)
- Health Check Patterns: https://microservices.io/patterns/observability/health-check-api.html
