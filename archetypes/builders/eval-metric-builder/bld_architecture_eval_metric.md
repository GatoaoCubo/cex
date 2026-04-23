---
kind: architecture
id: bld_architecture_eval_metric
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of eval_metric -- inventory, dependencies
quality: 9.0
title: "Architecture Eval Metric"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [eval_metric, builder, architecture]
tldr: "Component map of eval_metric -- inventory, dependencies"
domain: "eval_metric construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_architecture_usage_report
  - bld_architecture_eval_framework
  - bld_architecture_cohort_analysis
  - bld_architecture_judge_config
  - bld_architecture_benchmark_suite
  - bld_architecture_discovery_questions
  - bld_architecture_memory_benchmark
  - bld_architecture_api_reference
  - bld_architecture_roi_calculator
  - bld_architecture_sdk_example
---

## Component Inventory
| ISO Name             | Role                          | Pillar | Status  |
|----------------------|-------------------------------|--------|---------|
| bld_manifest         | Defines evaluation structure  | P07    | Active  |
| bld_instruction      | Specifies construction rules  | P07    | Active  |
| bld_system_prompt    | Guides metric generation logic| P07    | Active  |
| bld_schema           | Enforces data format standards| P07    | Active  |
| bld_quality_gate     | Validates metric compliance   | P07    | Active  |
| bld_output_template  | Structures result formatting  | P07    | Active  |
| bld_examples         | Provides sample metric outputs| P07    | Active  |
| bld_knowledge_card   | Embeds domain-specific rules  | P07    | Active  |
| bld_architecture     | Maps metric to system layers  | P07    | Active  |
| bld_collaboration    | Coordinates cross-component workflows | P07 | Active  |
| bld_config           | Stores builder parameters     | P07    | Active  |
| bld_memory           | Maintains state across builds | P07    | Active  |
| bld_tools            | Integrates external validation| P07    | Active  |

## Dependencies
| From             | To               | Type         |
|------------------|------------------|--------------|
| bld_manifest     | bld_instruction  | Reference    |
| bld_schema       | bld_quality_gate | Validation   |
| bld_output_template | bld_examples   | Dependency   |
| bld_tools        | JSON Schema Validator | External |
| bld_config       | bld_memory       | Configuration|

## Architectural Position
eval_metric sits at the core of P07's CEX pillar, ensuring evaluation metrics are rigorously constructed, validated, and aligned with system prompts, quality gates, and domain-specific knowledge. It bridges builder components with external tools, enabling consistent metric generation across compliance, performance, and collaboration workflows.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_usage_report]] | sibling | 0.82 |
| [[bld_architecture_eval_framework]] | sibling | 0.81 |
| [[bld_architecture_cohort_analysis]] | sibling | 0.81 |
| [[bld_architecture_judge_config]] | sibling | 0.80 |
| [[bld_architecture_benchmark_suite]] | sibling | 0.61 |
| [[bld_architecture_discovery_questions]] | sibling | 0.60 |
| [[bld_architecture_memory_benchmark]] | sibling | 0.60 |
| [[bld_architecture_api_reference]] | sibling | 0.59 |
| [[bld_architecture_roi_calculator]] | sibling | 0.57 |
| [[bld_architecture_sdk_example]] | sibling | 0.56 |
