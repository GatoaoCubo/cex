---
id: p07_sr_engineering_evaluation
kind: scoring_rubric
pillar: P07
title: "Rubric: Engineering Evaluation"
version: "1.0.0"
created: "2026-04-01"
updated: "2026-04-01"
author: "scoring-rubric-builder"
framework: "engineering_5d"
target_kinds: [agent, code_executor, cli_tool, api_client, workflow, daemon]
dimensions_count: 5
total_weight: 100
threshold_golden: 9.5
threshold_publish: 8.0
threshold_review: 7.0
automation_status: "semi-automated"
domain: "engineering"
quality: 8.9
tags: [scoring-rubric, engineering, code-quality, evaluation]
tldr: "5-dimension engineering rubric: correctness 30%, completeness 25%, quality 20%, documentation 15%, testing 10%"
density_score: 0.87
calibration_set: [p07_gt_agent_high_quality, p07_gt_workflow_standard]
inter_rater_agreement: 0.82
appeals_process: "Submit to engineering lead with code review evidence for re-evaluation"
linked_artifacts:
  primary: "agent-builder"
  related: [p11_qg_engineering_artifacts, p07_gt_code_review]
---
## Framework Overview
Engineering evaluation rubric assesses code-based artifacts across 5 critical dimensions. Designed for agents, executors, tools, APIs, workflows, and daemons where functional correctness, requirement coverage, and maintainability determine production readiness. Balances immediate functionality (correctness) with long-term viability (quality, documentation).

## Dimensions
| Dimension | Weight | Scale | Criteria | Example (10) | Example (5) |
|-----------|--------|-------|----------|-------------|-------------|
| Correctness | 30% | 0-10 | Functional behavior matches specifications, handles edge cases | All test cases pass, graceful error handling, edge cases covered | Core functionality works, some edge case failures |
| Completeness | 25% | 0-10 | All specified requirements implemented with proper interfaces | Every requirement mapped to implementation, all APIs functional | 80% of requirements met, missing non-critical features |
| Quality | 20% | 0-10 | Architecture, code structure, performance, security best practices | Clean architecture, optimized performance, security validated | Readable code, basic structure, no major anti-patterns |
| Documentation | 15% | 0-10 | Usage instructions, API docs, architectural decisions documented | Complete README, API docs, architecture diagrams, examples | Basic README with usage examples, missing API details |
| Testing | 10% | 0-10 | Test coverage, unit tests, integration tests, test quality | >90% coverage, unit + integration + edge case tests | >70% coverage, basic unit tests, some integration |

## Thresholds
| Tier | Score | Action |
|------|-------|--------|
| GOLDEN | >= 9.5 | Production deployment, reference implementation, reuse template |
| PUBLISH | >= 8.0 | Code review approval, staging deployment |
| REVIEW | >= 7.0 | Return for improvements with specific dimension feedback |
| REJECT | < 7.0 | Major refactor required, reassign or restart |

## Calibration
- GOLDEN (9.7): High-performance API client with 95% test coverage, complete OpenAPI docs, error handling for all edge cases, security audit passed
- PUBLISH (8.2): Standard CLI tool with all features implemented, basic docs, 80% test coverage, minor performance optimizations needed
- REVIEW (7.3): Workflow with core functionality complete but missing error handling, incomplete documentation, 60% test coverage
- REJECT (5.1): Agent with basic functionality but crashes on edge cases, no documentation, no tests, security vulnerabilities

## Automation
| Dimension | Status | Tool |
|-----------|--------|------|
| Correctness | semi-automated | Test suite execution + manual edge case review |
| Completeness | automated | Requirements traceability matrix validation |
| Quality | semi-automated | Static analysis + manual architecture review |
| Documentation | automated | Doc coverage tools + manual completeness check |
| Testing | automated | Coverage reports + test quality metrics |

## References
- Clean Code: A Handbook of Agile Software Craftsmanship (Martin, 2008)
- Google Engineering Practices: https://google.github.io/eng-practices/
- OWASP Secure Coding Practices: https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/