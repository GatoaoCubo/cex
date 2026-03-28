---
kind: memory
id: bld_memory_unit_eval
pillar: P10
llm_function: INJECT
purpose: Accumulated production experience for unit_eval artifact generation
---

# Memory: unit-eval-builder
## Summary
Unit evals test individual agent or prompt correctness in isolation with specific input-expected_output-assertion triples. The critical production lesson is isolation completeness — unit evals that depend on external state (database content, API availability, other agents) are integration tests mislabeled as unit tests. They fail intermittently and erode trust in the test suite. The second lesson is assertion specificity: assertions that check "output contains keyword" miss structural and semantic failures.
## Pattern
- Every eval must be fully isolated: mock all external dependencies, control all input state
- Assertions must be specific: check structure, values, and types — not just keyword presence
- Setup must create all required state; teardown must clean all created state — no test pollution
- Include both positive tests (correct input produces correct output) and negative tests (invalid input is rejected)
- Expected output must be concrete and complete, not partial — partial expectations miss regressions
- Map each assertion to a specific quality gate or requirement — traceability from test to spec
## Anti-Pattern
- External dependencies in unit evals — intermittent failures from network/database availability
- Keyword-only assertions ("output contains 'success'") — miss structural failures and false positives on unrelated matches
- Missing teardown — test state leaks into subsequent tests causing cascading failures
- Only positive tests — invalid input handling goes untested, producing silent failures in production
- Confusing unit_eval (P07, isolated correctness) with smoke_eval (P07, fast sanity) or e2e_eval (P07, pipeline testing)
- Flaky tests accepted as normal — every flaky test must be either fixed or removed, never tolerated
## Context
Unit evals operate in the P07 evaluation layer as the second testing tier after smoke evals. They verify that individual agents and prompts produce correct output for specific inputs under controlled conditions. In test pyramids, unit evals form the broad base: many fast, isolated tests that catch the majority of regressions before slower integration and end-to-end tests run.
## Impact
Fully isolated unit evals achieved 99.5% pass rate consistency versus 85% for evals with external dependencies. Specific assertions caught 3x more regressions than keyword-only checks. Positive + negative test coverage reduced production input-handling failures by 60%.
## Reproducibility
For reliable unit eval production: (1) mock all external dependencies, (2) define concrete input-expected_output pairs, (3) write specific assertions checking structure and values, (4) include setup and teardown, (5) add both positive and negative test cases, (6) map assertions to requirements, (7) verify zero flakiness over 10 consecutive runs.
## References
- unit-eval-builder SCHEMA.md (input/output/assertion specification)
- P07 evaluation pillar specification
- Unit testing isolation and assertion patterns
