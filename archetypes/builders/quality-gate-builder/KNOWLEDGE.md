---
pillar: P01
llm_function: INJECT
purpose: Standards and patterns for quality_gate production
---

# Domain Knowledge: quality_gate

## Foundational Concepts
Quality gates originate from manufacturing (stage-gate process, Cooper 1990).
In software: CI/CD gates (lint, test, coverage). In AI/LLM: pre-publish validation.

## CEX Gate Pattern (proven)
validate_kc.py v2.0 established the HARD/SOFT pattern:
- 10 HARD gates: binary pass/fail, ANY failure blocks publish
- 20 SOFT gates: weighted 0-10 score, contribute to final grade
- Scoring: GOLDEN >= 9.5, PUBLISH >= 8.0, REVIEW >= 7.0, REJECT < 7.0

## Industry Patterns
| Pattern | Source | CEX alignment |
|---------|--------|---------------|
| Stage-Gate | Cooper 1990 | Phase gates between build stages |
| CI/CD Quality Gates | GitHub Actions, GitLab CI | Automated pre-merge checks |
| SonarQube Quality Gates | SonarSource | Metric thresholds (coverage, duplication) |
| DORA Metrics | Google DevOps Research | Deployment frequency, lead time, MTTR, change failure |

## Key Principles
- Gates must be AUTOMATABLE (no human judgment in the loop)
- Gates must be INDEPENDENT (verifier cannot be the producer)
- Gates must have BYPASS (emergency override with audit trail)
- Scoring weights must be EXPLICIT (no hidden preferences)
- HARD gates are non-negotiable; SOFT gates allow tradeoffs

## Boundary Precision
| Type | What it does | NOT this |
|------|-------------|----------|
| quality_gate (P11) | Defines WHAT must pass and at what threshold | Does NOT implement the check (that's validator P06) |
| validator (P06) | Implements the check in code | Does NOT define the criteria (that's gate P11) |
| scoring_rubric (P07) | Defines HOW to evaluate quality dimensions | Does NOT enforce pass/fail (that's gate P11) |

## References
- Cooper, R. G. (1990). Stage-gate systems for new product development.
- https://docs.sonarqube.org/latest/user-guide/quality-gates/
- validate_kc.py v2.0 (CEX internal, HARD/SOFT pattern reference)
