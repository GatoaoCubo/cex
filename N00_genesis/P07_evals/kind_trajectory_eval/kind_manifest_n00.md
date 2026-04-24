---
id: n00_trajectory_eval_manifest
kind: knowledge_card
8f: F3_inject
pillar: P07
nucleus: n00
title: "Trajectory Eval -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, trajectory_eval, p07, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_trajectory_eval
  - bld_schema_benchmark_suite
  - bld_schema_reranker_config
  - bld_schema_dataset_card
  - bld_schema_usage_report
  - bld_schema_eval_metric
  - bld_schema_integration_guide
  - bld_schema_thinking_config
  - bld_schema_e2e_eval
  - bld_schema_quickstart_guide
---

<!-- 8F: F1=knowledge_card P07 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Trajectory eval defines an agent trajectory evaluation methodology that assesses the quality of an agent's multi-step reasoning and action sequence, not just its final output. It specifies how to score individual steps (tool calls, intermediate reasoning, state transitions) and the full trajectory against a reference or ideal path. Used to optimize agentic behavior through process reward models and trajectory fine-tuning.

## Pillar
P07 -- Evals

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `trajectory_eval` |
| pillar | string | yes | Always `P07` |
| title | string | yes | Agent name + task + "Trajectory Eval" |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| agent_under_eval | string | yes | Agent ID being evaluated |
| task_description | string | yes | The task the agent performs in the trajectory |
| trajectory_format | enum | yes | json_steps / openai_messages / langchain_trace |
| step_scoring_criteria | list | yes | Per-step scoring dimensions |
| reference_trajectory_id | string | no | ID of golden trajectory used for comparison |
| final_outcome_weight | float | yes | Weight of final outcome vs. process quality (0.0-1.0) |

## When to use
- Evaluating the reasoning quality of an agentic workflow, not just the final artifact
- Building training data for process reward model fine-tuning
- Detecting inefficient or incorrect reasoning patterns in a deployed agent

## Builder
`archetypes/builders/trajectory_eval-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind trajectory_eval --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- N01 intelligence defines; N05 operations captures trajectories
- `{{SIN_LENS}}` -- Analytical Envy: every reasoning step measured and scored
- `{{TARGET_AUDIENCE}}` -- ML engineers optimizing agent reasoning quality
- `{{DOMAIN_CONTEXT}}` -- agent type, task complexity, available reference trajectories

## Example (minimal)
```yaml
---
id: trajectory_eval_n03_build_task
kind: trajectory_eval
pillar: P07
nucleus: n01
title: "N03 Build Task -- 8F Trajectory Eval"
version: 1.0
quality: null
---
agent_under_eval: n03_engineering
task_description: "Build knowledge_card from 5-word intent via 8F pipeline"
trajectory_format: json_steps
final_outcome_weight: 0.40
step_scoring_criteria:
  - {stage: F1_constrain, check: kind_resolved_correctly}
  - {stage: F7_govern, check: quality_gate_run}
```

## Related kinds
- `reward_model` (P07) -- process reward model trained on trajectory eval results
- `e2e_eval` (P07) -- full pipeline test; trajectory_eval adds step-level scoring
- `golden_test` (P07) -- reference trajectory used for comparison

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_trajectory_eval]] | upstream | 0.45 |
| [[bld_schema_benchmark_suite]] | upstream | 0.40 |
| [[bld_schema_reranker_config]] | upstream | 0.39 |
| [[bld_schema_dataset_card]] | upstream | 0.39 |
| [[bld_schema_usage_report]] | upstream | 0.39 |
| [[bld_schema_eval_metric]] | upstream | 0.39 |
| [[bld_schema_integration_guide]] | upstream | 0.39 |
| [[bld_schema_thinking_config]] | upstream | 0.38 |
| [[bld_schema_e2e_eval]] | upstream | 0.38 |
| [[bld_schema_quickstart_guide]] | upstream | 0.38 |
