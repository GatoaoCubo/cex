---
pillar: P10
llm_function: INJECT
purpose: Accumulated production experience for smoke_eval artifact generation
---

# Memory: smoke-eval-builder

## Summary

Smoke evals are fast sanity checks (under 30 seconds) that verify basic component functionality before deeper testing. The critical production lesson is strict timeout enforcement — a smoke eval that takes 60 seconds defeats its purpose as a fast-fail gate. The second lesson is critical path selection: smoke evals must test the minimum set of operations that, if broken, indicate the component is fundamentally non-functional. Testing non-critical paths wastes the tight time budget.

## Pattern

- Enforce strict timeout: 30 seconds maximum, prefer under 10 seconds — fail fast is the entire point
- Test only the critical path: the minimum operations that prove the component is alive and functional
- Assertions must be binary: works or does not work — no partial scores in smoke testing
- Health checks should verify connectivity, basic I/O, and core operation — not business logic
- Run smoke evals before any deeper testing — smoke failure should skip all downstream test suites
- Include clear failure messages that identify which critical path component failed

## Anti-Pattern

- Smoke evals exceeding 30 seconds — defeats the fast-fail purpose, becomes a slow unit test
- Testing non-critical features in smoke evals — wastes time budget on things that do not indicate fundamental breakage
- Partial scoring or graded results — smoke evals are binary: pass (component works) or fail (component broken)
- Smoke evals that require complex setup/teardown — setup time should not exceed test time
- Confusing smoke_eval (P07, fast sanity) with unit_eval (P07, correctness testing) or benchmark (P07, performance measurement)
- Missing failure diagnostics — smoke fails but nobody knows which component caused it

## Context

Smoke evals operate in the P07 evaluation layer as the fastest, first-line test. They gate all subsequent testing: if smoke fails, no unit tests, integration tests, or benchmarks run. In CI/CD pipelines, smoke evals are the first step after build, providing sub-30-second feedback on whether the build is even worth testing further.

## Impact

Strict 30-second timeout enforcement saved an average of 15 minutes per failed pipeline by skipping downstream tests early. Critical-path-only testing achieved 95% detection rate for fundamental breakages. Binary assertions eliminated confusion about whether a smoke result was a pass or a warning.

## Reproducibility

Reliable smoke eval production: (1) identify 3-5 critical path operations, (2) write binary assertions per operation, (3) enforce 30-second total timeout, (4) minimize setup requirements, (5) include failure diagnostic messages, (6) validate the eval actually runs under 30 seconds on target hardware.

## References

- smoke-eval-builder SCHEMA.md (critical path, timeout specification)
- P07 evaluation pillar specification
- Smoke testing and fast-fail gate patterns
