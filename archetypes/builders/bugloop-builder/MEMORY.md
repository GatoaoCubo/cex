---
pillar: P10
llm_function: INJECT
purpose: Patterns remembered between production sessions
---

# Memory: bugloop-builder

## Common Mistakes
1. Inflated confidence — setting 0.9+ for non-deterministic failures (memory leaks, data corruption)
2. escalation.threshold > cycle_count — escalation becomes unreachable, bugs silently repeat
3. auto_fix=true with confidence < 0.7 — unsafe auto-fix violates HARD invariant H11+H12
4. rollback.enabled=false with fix.strategy=rollback_first — logical contradiction
5. detect.pattern=".*" — too broad, matches unrelated failures, generates false fix attempts
6. verify.assertions=[] — no pass criteria, verification always passes vacuously
7. fix.max_attempts > cycle_count — attempts exceed cycle budget, unreachable state
8. Confusing bugloop with quality_gate — gate BLOCKS, loop CORRECTS; different phases

## Proven Bugloop Patterns
| Domain | detect.method | fix.strategy | confidence | cycle_count |
|--------|--------------|-------------|-----------|-------------|
| KC validation | test_failure | patch_and_retry | 0.88 | 5 |
| API schema drift | static_analysis | rollback_first | 0.72 | 3 |
| Embedding stale | log_scan | patch_and_retry | 0.91 | 4 |
| Runtime OOM | runtime_trace | rollback_first | 0.55 | 2 |
| Lint failures | static_analysis | patch_and_retry | 0.95 | 3 |

## Confidence Calibration Reference
| Failure class | Confidence range | auto_fix safe? |
|---------------|-----------------|----------------|
| Deterministic + reversible | 0.85-0.95 | YES |
| Schema/format errors | 0.70-0.88 | YES with assertions |
| Runtime non-deterministic | 0.40-0.65 | NO — manual fix |
| Data integrity issues | 0.10-0.40 | NO — always escalate |

## Escalation Target Patterns
| Target | Use case |
|--------|---------|
| signal_bus:bugloop_escalation | Async signal to monitoring system |
| slack:#eng-alerts | Human notification channel |
| pagerduty:service_id | On-call escalation for production |
| queue:manual_review | Async human review queue |

## Production Counter
| Metric | Value |
|--------|-------|
| Bugloops produced | 0 |
