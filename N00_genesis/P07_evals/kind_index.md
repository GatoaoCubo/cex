---
id: n00_p07_kind_index
kind: knowledge_card
pillar: P07
nucleus: n00
title: "P07 Evals -- Kind Index"
version: 1.0
quality: 9.0
tags: [index, p07, archetype, n00]
density_score: 1.0
related:
  - kc_intent_resolution_map
  - bld_architecture_kind
  - bld_collaboration_llm_evaluation_scenario
  - kind-builder
  - bld_collaboration_kind
  - bld_collaboration_builder
  - bld_collaboration_golden_test
  - p03_pc_cex_universal
  - bld_collaboration_eval_dataset
  - self_audit_n05_codex_2026_04_15
---

<!-- 8F: F1=knowledge_card P07 F2=knowledge-card-builder F3=kinds_meta+schema F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Master index of all 23 kinds in pillar P07. Reference for /mentor, nucleus builders, and the 8F pipeline.

## Pillar: P07 Evals
Quality assurance and evaluation infrastructure: benchmarks, LLM judges, eval datasets, scoring rubrics, regression checks, and red-team evaluations. The measurement layer that closes the quality loop.

## Kinds in P07

| Kind | Purpose | Primary Nucleus | Builder |
|------|---------|-----------------|---------|
| `benchmark` | Performance measurement (latency, cost, quality) | N05 | `benchmark-builder` |
| `benchmark_suite` | Composite benchmark definition with multiple tasks | N05 | `benchmark_suite-builder` |
| `bias_audit` | Fairness evaluation methodology and results | N05 | `bias_audit-builder` |
| `cohort_analysis` | Cohort analysis spec for retention measurement and LTV modeling | N05 | `cohort_analysis-builder` |
| `e2e_eval` | Teste end-to-end (pipeline completo) | N05 | `e2e_eval-builder` |
| `eval_dataset` | Test case collection | N05 | `eval_dataset-builder` |
| `eval_framework` | End-to-end evaluation framework integration | N05 | `eval_framework-builder` |
| `eval_metric` | Individual evaluation metric definition | N05 | `eval_metric-builder` |
| `experiment_tracker` | Experiment configuration and results tracking | N05 | `experiment_tracker-builder` |
| `golden_test` | Reference test case (quality 9.5+) | N05 | `golden_test-builder` |
| `judge_config` | LLM judge configuration for automated evaluation | N05 | `judge_config-builder` |
| `llm_evaluation_scenario` | HELM Stanford CRFM evaluation scenario: task instances, metric mapping | N05 | `llm_evaluation_scenario-builder` |
| `llm_judge` | Config LLM-as-Judge | N05 | `llm_judge-builder` |
| `memory_benchmark` | Memory system quality evaluation suite | N05 | `memory_benchmark-builder` |
| `red_team_eval` | Teste adversarial | N05 | `red_team_eval-builder` |
| `regression_check` | Comparacao contra baseline | N05 | `regression_check-builder` |
| `reward_model` | Process/outcome reward model configuration | N05 | `reward_model-builder` |
| `scoring_rubric` | Evaluation criterion (5D, 12LP, custom) | N05 | `scoring_rubric-builder` |
| `smoke_eval` | Quick sanity test (< 30s) | N05 | `smoke_eval-builder` |
| `trace_config` | Trace/span configuration for 8F pipeline observability | N05 | `trace_config-builder` |
| `trajectory_eval` | Agent trajectory evaluation methodology | N05 | `trajectory_eval-builder` |
| `unit_eval` | Agent/prompt unit test | N05 | `unit_eval-builder` |
| `usage_report` | Usage analytics report spec for billing and CFO dashboards | N05 | `usage_report-builder` |

## Usage
```python
# Build any of these via 8F:
python _tools/cex_8f_runner.py "your intent" --kind {kind} --execute
```

## CoC Hierarchy Note
These 23 kinds follow the convention-over-configuration hierarchy: each instance
(N01-N07) inherits this schema and fills the variables for its sin lens.
N00_genesis holds the canonical archetype; nuclei hold the instantiated versions.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[kc_intent_resolution_map]] | sibling | 0.44 |
| [[bld_architecture_kind]] | downstream | 0.35 |
| [[bld_collaboration_llm_evaluation_scenario]] | downstream | 0.34 |
| [[kind-builder]] | downstream | 0.34 |
| [[bld_collaboration_kind]] | downstream | 0.33 |
| [[bld_collaboration_builder]] | downstream | 0.30 |
| [[bld_collaboration_golden_test]] | downstream | 0.29 |
| [[p03_pc_cex_universal]] | upstream | 0.27 |
| [[bld_collaboration_eval_dataset]] | downstream | 0.27 |
| [[self_audit_n05_codex_2026_04_15]] | related | 0.27 |
