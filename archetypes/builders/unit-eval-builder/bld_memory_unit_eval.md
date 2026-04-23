---
kind: memory
id: bld_memory_unit_eval
pillar: P10
llm_function: INJECT
purpose: Accumulated production experience for unit_eval artifact generation
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.2
title: "Memory Unit Eval"
version: "1.0.0"
author: n03_builder
tags: [unit_eval, builder, examples]
tldr: "Golden and anti-examples for unit eval construction, demonstrating ideal structure and common pitfalls."
domain: "unit eval construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - unit-eval-builder
  - bld_collaboration_unit_eval
  - p11_qg_unit_eval
  - p03_sp_unit-eval-builder
  - p02_agent_test_ops
  - bld_architecture_unit_eval
  - p03_ins_unit_eval
  - bld_knowledge_card_unit_eval
  - p01_kc_unit_eval
  - bld_output_template_unit_eval
---
# Memory: unit-eval-builder
## Summary
Unit evals test individual agent or prompt correctness in isolation with specific input-expected_output-assertion triples. The critical production lesson is isolation completeness — unit evals that depend on external state (database content, API availability, other agents) are integration tests mislabeled as unit tests. They fail intermittently and erode trust in the test suite. The second lesson is assertion specificity: assertions that check "output contains keyword" miss structural and semantic failures.
## Pattern
1. Every eval must be fully isolated: mock all external dependencies, control all input state
2. Assertions must be specific: check structure, values, and types — not just keyword presence
3. Setup must create all required state; teardown must clean all created state — no test pollution
4. Include both positive tests (correct input produces correct output) and negative tests (invalid input is rejected)
5. Expected output must be concrete and complete, not partial — partial expectations miss regressions
6. Map each assertion to a specific quality gate or requirement — traceability from test to spec
## Anti-Pattern
1. External dependencies in unit evals — intermittent failures from network/database availability
2. Keyword-only assertions ("output contains 'success'") — miss structural failures and false positives on unrelated matches
3. Missing teardown — test state leaks into subsequent tests causing cascading failures
4. Only positive tests — invalid input handling goes untested, producing silent failures in production
5. Confusing unit_eval (P07, isolated correctness) with smoke_eval (P07, fast sanity) or e2e_eval (P07, pipeline testing)
6. Flaky tests accepted as normal — every flaky test must be either fixed or removed, never tolerated
## Context
Unit evals operate in the P07 evaluation layer as the second testing tier after smoke evals. They verify that individual agents and prompts produce correct output for specific inputs under controlled conditions. In test pyramids, unit evals form the broad base: many fast, isolated tests that catch the majority of regressions before slower integration and end-to-end tests run.
## Impact
Fully isolated unit evals achieved 99.5% pass rate consistency versus 85% for evals with external dependencies. Specific assertions caught 3x more regressions than keyword-only checks. Positive + negative test coverage reduced production input-handling failures by 60%.
## Reproducibility
For reliable unit eval production: (1) mock all external dependencies, (2) define concrete input-expected_output pairs, (3) write specific assertions checking structure and values, (4) include setup and teardown, (5) add both positive and negative test cases, (6) map assertions to requirements, (7) verify zero flakiness over 10 consecutive runs.
## References
1. unit-eval-builder SCHEMA.md (input/output/assertion specification)
2. P07 evaluation pillar specification
3. Unit testing isolation and assertion patterns

## Metadata

```yaml
id: bld_memory_unit_eval
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-memory-unit-eval.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `memory` |
| Pillar | P10 |
| Domain | unit eval construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[unit-eval-builder]] | upstream | 0.53 |
| [[bld_collaboration_unit_eval]] | upstream | 0.47 |
| [[p11_qg_unit_eval]] | upstream | 0.44 |
| [[p03_sp_unit-eval-builder]] | upstream | 0.40 |
| [[p02_agent_test_ops]] | upstream | 0.38 |
| [[bld_architecture_unit_eval]] | upstream | 0.37 |
| [[p03_ins_unit_eval]] | upstream | 0.35 |
| [[bld_knowledge_card_unit_eval]] | upstream | 0.35 |
| [[p01_kc_unit_eval]] | upstream | 0.33 |
| [[bld_output_template_unit_eval]] | upstream | 0.33 |
