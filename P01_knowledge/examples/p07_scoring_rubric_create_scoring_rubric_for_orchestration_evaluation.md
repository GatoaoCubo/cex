---
id: p07_sr_orchestration_quality
kind: scoring_rubric
pillar: P07
title: "Rubric: Orchestration Quality"
version: "1.0.0"
created: "2026-04-01"
updated: "2026-04-01"
author: "scoring-rubric-builder"
framework: "orchestration_quality"
target_kinds: [workflow, mission_spec, grid_execution, orchestration_plan]
dimensions_count: 4
total_weight: 100
threshold_golden: 9.5
threshold_publish: 8.0
threshold_review: 7.0
automation_status: "semi-automated"
domain: "orchestration"
quality: 8.9
tags: [scoring-rubric, orchestration, n07, evaluation, coordination]
tldr: "4-dimension rubric for orchestration: coordination 30%, efficiency 25%, reliability 25%, completeness 20%"
density_score: 0.89
calibration_set: [p07_gt_grid_mission_complete, p07_gt_handoff_n03_agent]
inter_rater_agreement: 0.82
appeals_process: "Submit to N07 orchestrator with execution logs and rationale for re-evaluation"
linked_artifacts:
  primary: "workflow-builder"
  related: [p11_qg_orchestration, p12_wf_mission_pipeline]
---
## Framework Overview

Orchestration Quality evaluates how effectively complex multi-nucleus missions are coordinated, executed, and completed. Designed specifically for CEX orchestration artifacts including workflows, mission specs, grid executions, and orchestration plans. This rubric measures the quality of coordination between nuclei (N01-N07), resource efficiency, fault tolerance, and mission completion rates.

## Dimensions

| Dimension | Weight | Scale | Criteria | Example (10) | Example (5) |
|-----------|--------|-------|----------|-------------|-------------|
| Coordination | 30% | 0-10 | Handoff clarity, signal management, nucleus synchronization | All handoffs explicit with clear deliverables, signals tracked, zero coordination failures | Some handoffs unclear, occasional signal loss, 1-2 minor coordination gaps |
| Efficiency | 25% | 0-10 | Parallel execution, resource utilization, minimal waste | 85%+ parallel execution, CPU/memory optimized, zero idle nuclei | 60% parallel execution, some resource waste, occasional idle nuclei |
| Reliability | 25% | 0-10 | Error handling, fault tolerance, recovery mechanisms | Complete error handling, auto-recovery from failures, 99%+ success rate | Basic error handling, manual recovery needed, 85% success rate |
| Completeness | 20% | 0-10 | Mission scope coverage, deliverable fulfillment, goal achievement | 100% of mission scope delivered, all goals achieved, zero gaps | 85% scope delivered, most goals achieved, minor gaps in deliverables |

## Thresholds

| Tier | Score | Action |
|------|-------|--------|
| GOLDEN | >= 9.5 | Promote to reference orchestration patterns, add to best practices |
| PUBLISH | >= 8.0 | Deploy to production orchestration pool |
| REVIEW | >= 7.0 | Return with specific dimension feedback for improvement |
| REJECT | < 7.0 | Redesign orchestration approach, re-evaluate coordination strategy |

## Calibration

- **GOLDEN (9.7)**: p07_gt_grid_mission_complete — 6 nuclei coordinated flawlessly, 92% parallel execution, zero failures, 100% scope delivered
- **PUBLISH (8.4)**: Typical successful grid execution with clear handoffs, 75% parallel execution, 1 recoverable failure, 95% scope delivered
- **REVIEW (7.3)**: Grid with coordination issues, 55% parallel execution, manual recovery needed, 80% scope delivered
- **REJECT (4.2)**: Failed coordination, sequential execution, multiple failures, 40% scope delivered

## Automation

| Dimension | Status | Tool |
|-----------|--------|------|
| Coordination | semi-automated | bash _spawn/dispatch.sh status + manual handoff review |
| Efficiency | automated | Resource monitoring scripts, parallel execution metrics |
| Reliability | semi-automated | Error log analysis + manual failure pattern review |
| Completeness | manual | Human review of deliverables against mission scope |

## References

- CEX Orchestration Patterns: N07 nucleus architecture
- Grid Execution Logs: .cex/runtime/signals/ analysis
- Nucleus Coordination Protocol: _spawn/dispatch.sh implementation