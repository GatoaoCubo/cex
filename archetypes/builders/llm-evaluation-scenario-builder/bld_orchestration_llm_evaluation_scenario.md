---
kind: collaboration
id: bld_collaboration_llm_evaluation_scenario
pillar: P12
llm_function: COLLABORATE
purpose: How llm_evaluation_scenario-builder works in crews with other builders
quality: 8.9
title: "Collaboration LLM Evaluation Scenario"
version: "1.0.0"
author: n06_wave7
tags: [llm_evaluation_scenario, builder, collaboration, helm]
tldr: "How llm_evaluation_scenario-builder works in crews with other builders"
domain: "llm_evaluation_scenario construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - llm-evaluation-scenario-builder
  - bld_architecture_kind
  - bld_collaboration_safety_hazard_taxonomy
  - bld_collaboration_builder
  - kind-builder
  - bld_collaboration_kind
  - bld_collaboration_eval_dataset
  - bld_collaboration_agent_computer_interface
  - p03_sp_llm_evaluation_scenario_builder
  - bld_collaboration_prompt_technique
---

## Crew Role
Composes atomic HELM evaluation scenario specifications. Receives task instances and metric definitions from sibling builders; produces scenario specs consumed by experiment orchestration.

## Receives From
| Builder                 | What                        | Format    |
|-------------------------|-----------------------------|-----------|
| eval_dataset-builder    | Task instance set           | YAML      |
| eval_metric-builder     | Primary metric definition   | YAML      |
| prompt_template-builder | Adapter template reference  | Markdown  |
| N01 Intelligence        | HELM taxonomy research      | Markdown  |

## Produces For
| Builder                    | What                          | Format   |
|----------------------------|-------------------------------|----------|
| experiment_config-builder  | Scenario spec for run config  | YAML     |
| benchmark-builder          | Scenario entry for suite      | Markdown |
| llm_judge-builder          | Eval criteria reference       | Markdown |

## Boundary
Does NOT produce full benchmark suites (use `benchmark-builder`).
Does NOT define raw evaluation datasets (use `eval_dataset-builder`).
Does NOT score artifacts (use `cex_score.py`).
Does NOT configure inference infrastructure (use N05 Operations).
Legal review of dataset licenses is handled by compliance team, not this builder.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[llm-evaluation-scenario-builder]] | upstream | 0.38 |
| [[bld_architecture_kind]] | upstream | 0.35 |
| [[bld_collaboration_safety_hazard_taxonomy]] | sibling | 0.33 |
| [[bld_collaboration_builder]] | sibling | 0.32 |
| [[kind-builder]] | upstream | 0.31 |
| [[bld_collaboration_kind]] | sibling | 0.31 |
| [[bld_collaboration_eval_dataset]] | sibling | 0.31 |
| [[bld_collaboration_agent_computer_interface]] | sibling | 0.30 |
| [[p03_sp_llm_evaluation_scenario_builder]] | upstream | 0.29 |
| [[bld_collaboration_prompt_technique]] | sibling | 0.29 |
