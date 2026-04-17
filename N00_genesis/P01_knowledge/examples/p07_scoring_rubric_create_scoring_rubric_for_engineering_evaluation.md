---
id: p07_sr_engineering_quality
kind: scoring_rubric
pillar: P07
title: "Rubric: Engineering Quality Assessment"
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: "scoring-rubric-builder"
framework: "Engineering Quality"
target_kinds: [agent, cli_tool, code_executor, api_client, workflow]
dimensions_count: 5
total_weight: 100
threshold_golden: 9.5
threshold_publish: 8.0
threshold_review: 7.0
automation_status: "semi-automated"
domain: "engineering"
quality: 9.1
tags: [scoring-rubric, engineering, code-quality, technical-assessment]
tldr: "5-dimension engineering rubric: technical correctness 30%, practices 25%, completeness 20%, documentation 15%, performance 10%"
density_score: 0.89
calibration_set: [p07_gt_agent_react_codebase, p07_gt_cli_deployment_tool]
inter_rater_agreement: 0.82
appeals_process: "Submit to engineering lead with technical rationale and test evidence for re-evaluation"
linked_artifacts:
  primary: "quality-gate-builder"
  related: [p11_qg_agent_publish, p11_qg_cli_tool_publish, p05_code_executor]
---
## Framework Overview

Engineering Quality Assessment evaluates technical artifacts across 5 orthogonal dimensions that capture both functional correctness and engineering excellence. Designed for code-based artifacts including agents, tools, executors, and workflows. Complements binary quality gates by providing nuanced scoring for technical depth, maintainability, and production readiness.

Target artifacts: agents with code components, CLI tools, code executors, API clients, deployment workflows, and similar engineering deliverables.

## Dimensions

| Dimension | Weight | Scale | Criteria | Example (10) | Example (5) |
|-----------|--------|-------|----------|-------------|-------------|
| Technical Correctness | 30% | 0-10 | Functions without errors, handles edge cases, produces expected outputs | Zero bugs, all test cases pass, graceful error handling | Core functionality works, minor bugs in edge cases |
| Engineering Practices | 25% | 0-10 | Code structure, patterns, separation of concerns, modularity | Clean architecture, SOLID principles, proper abstractions | Basic structure, some coupling, adequate patterns |
| Completeness | 20% | 0-10 | All requirements implemented, configuration options, extensibility | 100% requirements met, configurable, extensible | Core requirements met, missing some options |
| Documentation | 15% | 0-10 | Code comments, README, API docs, usage examples | Comprehensive docs, inline comments, examples work | Basic README, sparse comments, minimal examples |
| Performance | 10% | 0-10 | Efficiency, resource usage, scalability considerations | Optimized algorithms, minimal resource usage, scales well | Adequate performance, no obvious bottlenecks |

## Thresholds

| Tier | Score | Action |
|------|-------|--------|
| GOLDEN | >= 9.5 | Deploy to production, add to reference library, benchmark candidate |
| PUBLISH | >= 8.0 | Merge to main, available for team use, monitor in staging |
| REVIEW | >= 7.0 | Return with specific technical feedback, request improvements |
| REJECT | < 7.0 | Major rework required, architectural review needed |

## Calibration

**GOLDEN (9.7)**: React codebase agent - zero compilation errors, comprehensive test suite (98% coverage), modular architecture with clean interfaces, detailed API documentation with working examples, optimized for large codebases with efficient indexing.

**PUBLISH (8.2)**: CLI deployment tool - core deployment works reliably, follows standard CLI patterns, handles common error cases, basic help documentation, adequate performance for typical use cases.

**REVIEW (7.3)**: API client - basic functionality works, some error handling gaps, inconsistent naming conventions, minimal documentation, performance untested at scale.

**REJECT (5.1)**: Code executor - frequent runtime errors, monolithic structure, no error handling, no documentation, memory leaks under load.

## Automation

| Dimension | Status | Tool |
|-----------|--------|------|
| Technical Correctness | automated | test_runner.py (unit/integration tests), linter output |
| Engineering Practices | semi-automated | SonarQube metrics + manual architecture review |
| Completeness | semi-automated | Requirements checklist + manual feature verification |
| Documentation | semi-automated | Doc coverage tools + manual clarity assessment |
| Performance | manual | Profiling tools + manual scalability analysis |

## References

- Google Engineering Practices: https://google.github.io/eng-practices/
- Clean Code principles (Martin 2008)
- SOLID design principles
- CEX engineering standards v2.1