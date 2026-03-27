---
pillar: P01
llm_function: INJECT
purpose: Standards and patterns for e2e_eval production
sources: [Cypress, Playwright, Selenium, CEX pipeline patterns]
---

# Domain Knowledge: e2e_eval

## Foundational Concepts
End-to-end testing verifies complete system behavior from entry to exit.
In web: Cypress/Playwright testing full user flows through browser.
In CEX: testing complete agent pipelines from initial input through all stages to final validated output.

## Industry Patterns
| Source | What it defines | CEX alignment |
|--------|----------------|---------------|
| Cypress | Browser E2E with fixtures | data_fixtures, environment |
| Playwright | Multi-browser parallel tests | parallel flag, stages |
| Test Pyramid | E2E at top (fewest, slowest) | Complements smoke + unit |
| Contract Testing | Interface verification | Stage input/output contracts |

## Key Principles
- Test the FLOW, not individual components (that is unit_eval)
- Stages must be CONNECTED (output of N feeds input of N+1)
- Data fixtures ensure REPRODUCIBILITY (same input = same output)
- Cleanup prevents STATE POLLUTION between test runs
- Environment must be SPECIFIED (tests are env-dependent)
- Timeout must account for full pipeline duration (default 300s)

## CEX-Specific Extensions
| Field | Justification | Closest equivalent |
|-------|--------------|-------------------|
| stages | Ordered pipeline steps | Cypress test steps |
| data_fixtures | Reproducible test data | Cypress fixtures |
| pipeline | What is being tested | Cypress spec name |

## Boundary vs Nearby Types
| Type | What it is | Why it is NOT e2e_eval |
|------|------------|------------------------|
| unit_eval (P07) | Tests one agent isolated | Single scope, not pipeline |
| smoke_eval (P07) | Quick sanity < 30s | Shallow, not comprehensive |
| benchmark (P07) | Performance measurement | Metrics, not correctness |
| workflow (P12) | Defines the pipeline | Definition, not test |

## References
- Cypress E2E: https://docs.cypress.io/
- Playwright: https://playwright.dev/
- Test Pyramid: https://martinfowler.com/articles/practical-test-pyramid.html
