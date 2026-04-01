---
id: p07_sr_engineering_quality
kind: scoring_rubric
pillar: P07
title: "Rubric: Engineering Quality"
version: "1.0.0"
created: "2026-04-01"
updated: "2026-04-01"
author: "scoring-rubric-builder"
framework: "Engineering Quality"
target_kinds: [agent, tool, system_prompt, code_executor, workflow, cli_tool, api_client]
dimensions_count: 5
total_weight: 100
threshold_golden: 9.5
threshold_publish: 8.0
threshold_review: 7.0
automation_status: "semi-automated"
domain: "engineering"
quality: 8.9
tags: [scoring-rubric, engineering, code-quality, architecture, evaluation]
tldr: "5-dimension engineering rubric: technical correctness 30%, code quality 25%, architecture 20%, documentation 15%, testing 10%"
density_score: 0.88
calibration_set: [p07_gt_agent_claude_api, p07_gt_workflow_ci_cd]
inter_rater_agreement: 0.82
appeals_process: "Submit to N05 operations nucleus with code review rationale for re-evaluation"
linked_artifacts:
  primary: "agent-builder"
  related: [p11_qg_engineering_artifacts, p07_gt_code_review]
---
## Framework Overview

Engineering Quality evaluates technical artifacts across 5 orthogonal dimensions critical for production-ready engineering systems. Designed for code-based artifacts including agents, tools, workflows, and system components that require functional correctness, maintainability, and operational reliability. Complements engineering quality gates (P11) by providing nuanced scoring framework beyond pass/fail validation.

## Dimensions

| Dimension | Weight | Scale | Criteria | Example (10) | Example (5) |
|-----------|--------|-------|----------|-------------|-------------|
| Technical Correctness | 30% | 0-10 | Functional accuracy, error handling, edge case coverage | Zero bugs, handles all edge cases, proper error boundaries | Works for happy path, minimal error handling |
| Code Quality | 25% | 0-10 | Readability, structure, maintainability, conventions | Clean abstractions, consistent style, self-documenting | Mixed conventions, some unclear logic |
| Architecture | 20% | 0-10 | Design patterns, scalability, separation of concerns | SOLID principles, clear interfaces, extensible design | Basic structure, some coupling issues |
| Documentation | 15% | 0-10 | API docs, inline comments, usage examples, deployment guides | Complete API docs, examples, deployment steps | Basic README, minimal inline comments |
| Testing | 10% | 0-10 | Unit tests, integration tests, coverage, test quality | >90% coverage, edge cases tested, clear test names | Basic happy path tests, <70% coverage |

## Thresholds

| Tier | Score | Action |
|------|-------|--------|
| GOLDEN | >= 9.5 | Promote to production, use as reference implementation |
| PUBLISH | >= 8.0 | Merge to codebase, standard code review approval |
| REVIEW | >= 7.0 | Return with specific improvement recommendations |
| REJECT | < 7.0 | Major refactor required before re-submission |

## Calibration

- GOLDEN (9.7): p07_gt_agent_claude_api — robust error handling, clean interfaces, full test suite, comprehensive docs
- PUBLISH (8.2): typical production agent with solid functionality, adequate tests, basic documentation
- REVIEW (7.3): working prototype with good core logic but missing edge case handling and tests
- REJECT (4.5): proof-of-concept with hardcoded values, no error handling, no tests, minimal docs

## Automation

| Dimension | Status | Tool |
|-----------|--------|------|
| Technical Correctness | semi-automated | Unit tests + manual edge case review |
| Code Quality | automated | ESLint/pylint + complexity metrics |
| Architecture | manual | Human review for design patterns |
| Documentation | semi-automated | Doc coverage check + manual quality review |
| Testing | automated | Coverage reports + test quality metrics |

## References

- Clean Code: A Handbook of Agile Software Craftsmanship (Martin, 2008)
- SOLID Principles of Object-Oriented Design
- Google Engineering Practices: Code Review Guidelines
- CEX N05 Operations Nucleus: Engineering Standards v2.1