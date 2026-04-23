---
id: p07_sr_5d_orchestration
kind: scoring_rubric
pillar: P07
title: "Rubric: 5D Orchestration Evaluation"
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: "scoring-rubric-builder"
framework: "5D"
target_kinds: [workflow, dag, dispatch_rule, handoff_protocol, spawn_config]
dimensions_count: 5
total_weight: 100
threshold_golden: 9.5
threshold_publish: 8.0
threshold_review: 7.0
automation_status: "semi-automated"
domain: "orchestration"
quality: 9.1
tags: [scoring-rubric, orchestration, 5d, evaluation, p07, workflow]
tldr: "5D orchestration rubric: correctness 35%, reliability 25%, efficiency 20%, scalability 15%, maintainability 5%"
density_score: 0.91
calibration_set: [p07_gt_workflow_dispatch, p07_gt_dag_orchestration]
inter_rater_agreement: 0.87
appeals_process: "Dispute to N07 with annotated counterexample; re-evaluated within 24h by second reviewer"
linked_artifacts:
  primary: "workflow-builder"
  related: [p11_qg_orchestration_artifacts, p12_workflow_create_workflow_for_orchestration_pipeline]
related:
  - p11_qg_workflow
  - bld_knowledge_card_workflow
  - p12_wf_orchestration_pipeline
  - p01_kc_workflow
  - p12_wf_create_orchestration_agent
  - p11_qg_orchestration_artifacts
  - p03_sp_workflow-builder
  - bld_memory_workflow
  - p08_ac_orchestrator
  - dispatch
---
## Framework Overview

5D Orchestration evaluates P12 artifacts (workflow, dag, dispatch_rule, handoff_protocol, spawn_config) that coordinate multi-nucleus execution in CEX. Correctness dominates (35%) because a wrong dispatch cascades across nuclei; reliability ranks second (25%) because graceful degradation prevents total system failure. Efficiency, scalability, and maintainability complete coverage of runtime behavior.

Not applicable to: knowledge_card, agent, prompt_template, or single-nucleus artifacts. Use `p07_sr_5d_builder_nucleus` for those.

## Dimensions

| Dimension | Weight | Scale | Criteria | Example (10) | Example (5) |
|-----------|--------|-------|----------|-------------|-------------|
| Correctness | 35% | 0-10 | All nucleus routing targets exist; no dead-end handoffs; execution path matches declared intent | Workflow routes N03→N05→N07; all nucleus IDs valid; handoff files confirmed present; no unreachable branches | Correct happy-path routing but one fallback branch targets nonexistent N08 |
| Reliability | 25% | 0-10 | Explicit `on_failure` action, retry count, fallback nucleus, and timeout defined for every dispatch step | All 4 dispatch steps have `on_failure`, `retry: 2`, fallback nucleus named, `timeout_sec` specified | Happy path complete; failure branches present for 2/4 steps; 2 steps silent-fail with no recovery |
| Efficiency | 20% | 0-10 | Steps parallelized where dependency graph allows; no redundant sequential steps; estimated latency minimized | DAG runs N01+N03 in parallel (independent inputs), merges at N07; zero concurrent-capable steps run sequentially | 5 nuclei run sequentially despite 3 being independent; adds ~3× unnecessary latency |
| Scalability | 15% | 0-10 | spawn_config caps defined; queue backpressure documented; artifact handles 10× load without structural redesign | `max_parallel: 6`, `queue_depth: 50`, `backpressure: block` defined; graceful at 60 concurrent tasks | No concurrency limits; unbounded fan-out under load; no backpressure mechanism |
| Maintainability | 5% | 0-10 | Steps named with intent; non-obvious routing decisions commented; version field present with changelog | Every step has `intent:` field; routing deviations commented; `version: "1.2.0"` with changelog entry | Step names: step_1, step_2; no comments; version field absent |

## Thresholds

| Tier | Score | Range | Action |
|------|-------|-------|--------|
| GOLDEN | >= 9.5 | 9.5–10.0 | Promote to calibration set; use as dispatch reference template |
| PUBLISH | >= 8.0 | 8.0–9.4 | Merge to P12 pool; available for nucleus dispatch |
| REVIEW | >= 7.0 | 7.0–7.9 | Return to author with per-dimension delta; re-submit after fixes |
| REJECT | < 7.0 | 0–6.9 | Rebuild from scratch; attach rubric score sheet as failure evidence |

## Calibration

- **GOLDEN (9.7)**: `p12_workflow_create_workflow_for_orchestration_pipeline.md` — correctness 10 (all nuclei valid, handoffs verified), reliability 9 (4/5 failure paths defined), efficiency 10 (parallel N01+N03), scalability 10 (explicit caps), maintainability 9 (intent fields present, minor changelog gap)
- **PUBLISH (8.4)**: dispatch_rule with correct routing, 3/4 failure paths defined, sequential where parallel possible, spawn caps absent
- **REVIEW (7.1)**: workflow with correct happy path, 1/4 failure branches, all sequential, no concurrency config, generic step names
- **REJECT (4.8)**: DAG with one undefined nucleus target, no failure handling, no timeout, no version field, no comments

## Automation

| Dimension | Status | Tool / Check |
|-----------|--------|-------------|
| Correctness | semi-automated | `cex_doctor.py --kind workflow` validates nucleus IDs; handoff file existence via `signal_writer.py` grep |
| Reliability | semi-automated | Grep for `on_failure`, `retry`, `timeout` keys; human confirms all steps covered |
| Efficiency | manual | Human reviews DAG topology for parallelism opportunities; `cex_8f_motor.py` flags sequential-only graphs |
| Scalability | semi-automated | Grep for `max_parallel`, `queue_depth`, `backpressure`; human validates numeric bounds are non-zero |
| Maintainability | automated | `cex_doctor.py` checks `version` field; grep for `intent:` presence across all step definitions |

## References

- CEX dispatch protocol: `.claude/rules/n07-orchestrator.md`
- 8F pipeline: `.claude/rules/n03-8f-enforcement.md`
- P12 pillar schema: `P12_orchestration/_schema.yaml`
- Related rubric: `p07_sr_5d_builder_nucleus.md` (generic artifact evaluation)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p11_qg_workflow]] | downstream | 0.34 |
| [[bld_knowledge_card_workflow]] | upstream | 0.32 |
| [[p12_wf_orchestration_pipeline]] | downstream | 0.32 |
| [[p01_kc_workflow]] | downstream | 0.31 |
| [[p12_wf_create_orchestration_agent]] | downstream | 0.30 |
| [[p11_qg_orchestration_artifacts]] | downstream | 0.29 |
| [[p03_sp_workflow-builder]] | upstream | 0.29 |
| [[bld_memory_workflow]] | downstream | 0.28 |
| [[p08_ac_orchestrator]] | downstream | 0.27 |
| [[dispatch]] | downstream | 0.26 |
