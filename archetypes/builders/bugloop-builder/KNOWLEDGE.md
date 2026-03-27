---
pillar: P01
llm_function: INJECT
purpose: Standards and patterns for bugloop production
---

# Domain Knowledge: bugloop

## Foundational Concepts
Bugloops implement the MTTR (Mean Time To Recovery) minimization pattern from SRE.
Core idea: automated feedback loops reduce human toil for known failure classes.
CEX pattern: detect.pattern identifies a KNOWN failure signature; unknown failures escalate.

## Detect > Fix > Verify Cycle
```
[DETECT: signal fires]
     |
     v
[FIX: apply strategy, attempt N]
     |
     +-- success? --> [VERIFY: run test_suite]
     |                     |
     |                pass? --> [COMMIT/CONTINUE]
     |                fail? --> [retry or escalate]
     |
     +-- max_attempts reached --> [ESCALATE]
     |
     +-- rollback.enabled? --> [ROLLBACK then escalate]
```

## Fix Strategies
| Strategy | When to Use | Risk |
|----------|-------------|------|
| patch_and_retry | Known deterministic bug with safe patch | Low — patch is reversible |
| rollback_first | Unknown root cause; stability > freshness | Medium — loses recent changes |
| isolate_then_fix | Bug in one module, rest must stay live | High — requires isolation boundary |

## Confidence Calibration
| Domain | Typical Confidence | Rationale |
|--------|--------------------|-----------|
| Linting / style errors | 0.95 | Deterministic, no side effects |
| Test fixture failures | 0.85 | Known patterns, low blast radius |
| API schema drift | 0.75 | Requires schema diffing accuracy |
| Runtime memory leaks | 0.55 | Non-deterministic, prefer manual |
| Data corruption | 0.30 | High stakes, always manual |

## Detection Methods
| Method | Trigger | Pattern Example |
|--------|---------|-----------------|
| static_analysis | on_commit | `^E[0-9]{3}:` (flake8 error codes) |
| runtime_trace | continuous | `OOMKilled` in pod logs |
| test_failure | on_commit | `FAILED tests/.*::test_` |
| log_scan | scheduled | `ERROR.*database connection` |

## CEX Proven Patterns
- KC pipeline: test_failure + on_commit + patch_and_retry, confidence 0.88
- API validator: static_analysis + on_deploy + rollback_first, confidence 0.72
- Embedding refresh: log_scan + scheduled + patch_and_retry, confidence 0.91

## Boundary Precision
| Type | What it does | NOT this |
|------|-------------|----------|
| bugloop (P11) | Automated correction cycle for KNOWN failure patterns | Does NOT define pass/fail threshold (quality_gate) |
| quality_gate (P11) | Defines WHAT must pass at what threshold | Does NOT fix failures (bugloop) |
| optimizer (P11) | Improves metrics continuously (no failure required) | Does NOT react to failures (bugloop) |
| guardrail (P11) | Prevents UNSAFE actions from executing | Does NOT correct post-failure (bugloop) |
| validator (P06) | Implements the detection check in code | Does NOT define the cycle policy (bugloop) |

## SRE References
- Google SRE Book ch.13: Emergency Response — toil reduction via automation
- DORA MTTR metric: time from incident detection to service restoration
- Chaos Engineering principle: known failure modes should have automated recovery
- CEX internal: signal_writer.py pattern for automated fix confirmation

## Anti-Patterns to Avoid
1. Setting confidence=0.95 for a non-deterministic failure — inflated confidence causes silent bad fixes
2. escalation.threshold > cycle_count — escalation becomes unreachable
3. fix.strategy=rollback_first with rollback.enabled=false — contradiction blocks recovery
4. detect.pattern=".*" — catches everything, fixes nothing useful
5. verify.assertions=[] — verification phase has no pass criteria
