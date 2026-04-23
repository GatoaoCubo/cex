---
kind: knowledge_card
id: bld_knowledge_card_e2e_eval
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for e2e_eval production — end-to-end pipeline testing
sources: Cypress, Playwright, test pyramid (Fowler), contract testing patterns
quality: 9.1
title: "Knowledge Card E2E Eval"
version: "1.0.0"
author: n03_builder
tags: [e2e_eval, builder, examples]
tldr: "Golden and anti-examples for e2e eval construction, demonstrating ideal structure and common pitfalls."
domain: "e2e eval construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p10_lr_e2e_eval_builder
  - bld_instruction_e2e_eval
  - p03_sp_e2e_eval_builder
  - p01_kc_e2e_eval
  - p11_qg_e2e_eval
  - bld_architecture_e2e_eval
  - bld_examples_e2e_eval
  - e2e-eval-builder
  - bld_collaboration_e2e_eval
  - bld_schema_e2e_eval
---

# Domain Knowledge: e2e_eval
## Executive Summary
E2E evals verify complete pipeline behavior from initial input through all stages to final validated output. They test the FLOW, not individual components — confirming that stages connect correctly and produce expected end results. E2E evals differ from unit evals (single component), smoke evals (quick sanity), and benchmarks (performance metrics).
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P07 (governance/evaluation) |
| Position in test pyramid | Top (fewest, slowest, highest coverage) |
| Default timeout | 300s (full pipeline duration) |
| Key sections | stages, data_fixtures, expected_output, environment, cleanup |
| Stage connection | Output of stage N feeds input of stage N+1 |
| Fixture requirement | Same input MUST produce same output |
## Patterns
- **Stage-connected pipeline**: each stage's output is the next stage's input — verify intermediate outputs, not just final result
- **Data fixtures**: reproducible test data ensures deterministic results across runs
- **Environment specification**: e2e tests are environment-dependent — document exact versions, services, and config
- **Cleanup protocol**: prevent state pollution between runs; reset databases, clear caches, remove temp files
- **Timeout budgeting**: allocate time per stage; total timeout = sum of stage timeouts + buffer
| Source | Concept | Application |
|--------|---------|-------------|
| Cypress | Browser E2E with fixtures | data_fixtures, environment spec |
| Playwright | Multi-browser parallel tests | parallel flag, stage isolation |
| Test pyramid | E2E at top (fewest, slowest) | Complements smoke + unit evals |
| Contract testing | Interface verification | Stage input/output contracts |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Testing individual components | That is unit_eval, not e2e |
| No data fixtures | Non-deterministic results; flaky tests |
| Missing cleanup | State pollution between runs causes false failures |
| No environment spec | "Works in staging, fails in prod" |
| Timeout too short | Pipeline legitimately takes longer; false failure |
| No intermediate assertions | Only final check; hard to diagnose which stage broke |
## Application
1. Define pipeline: which stages participate, in what order
2. Create data fixtures: deterministic input that exercises the full path
3. Set assertions per stage: intermediate output checks, not just final
4. Specify environment: versions, services, config required
5. Configure timeout: per-stage + total with buffer
6. Define cleanup: reset state after each run to prevent pollution
## References
- Cypress: end-to-end testing with fixtures (docs.cypress.io)
- Playwright: multi-browser parallel testing (playwright.dev)
- Fowler: test pyramid (martinfowler.com/articles/forctical-test-pyramid.html)
- Contract testing: stage interface verification patterns

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p10_lr_e2e_eval_builder]] | downstream | 0.54 |
| [[bld_instruction_e2e_eval]] | downstream | 0.50 |
| [[p03_sp_e2e_eval_builder]] | downstream | 0.46 |
| [[p01_kc_e2e_eval]] | sibling | 0.40 |
| [[p11_qg_e2e_eval]] | downstream | 0.39 |
| [[bld_architecture_e2e_eval]] | downstream | 0.37 |
| [[bld_examples_e2e_eval]] | downstream | 0.36 |
| [[e2e-eval-builder]] | downstream | 0.34 |
| [[bld_collaboration_e2e_eval]] | downstream | 0.32 |
| [[bld_schema_e2e_eval]] | downstream | 0.30 |
