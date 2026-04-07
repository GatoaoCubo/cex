---
kind: knowledge_card
id: bld_knowledge_card_e2e_eval
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for e2e_eval production — end-to-end pipeline testing
sources: Cypress, Playwright, test pyramid (Fowler), contract testing patterns
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
