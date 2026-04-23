---
kind: architecture
id: bld_architecture_usage_report
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of usage_report -- inventory, dependencies
quality: 9.0
title: "Architecture Usage Report"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [usage_report, builder, architecture]
tldr: "Component map of usage_report -- inventory, dependencies"
domain: "usage_report construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_architecture_eval_metric
  - bld_architecture_cohort_analysis
  - bld_architecture_eval_framework
  - bld_architecture_judge_config
  - bld_architecture_benchmark_suite
  - bld_architecture_discovery_questions
  - bld_architecture_onboarding_flow
  - bld_architecture_memory_benchmark
  - bld_architecture_roi_calculator
  - bld_architecture_sdk_example
---

## Component Inventory
| ISO Name              | Role                          | Pillar | Status  |
|-----------------------|-------------------------------|--------|---------|
| bld_manifest          | Defines report structure      | P07    | Active  |
| bld_instruction       | Specifies generation rules    | P07    | Active  |
| bld_system_prompt     | Provides LLM guidance         | P07    | Active  |
| bld_schema            | Enforces data format          | P07    | Active  |
| bld_quality_gate      | Validates output compliance   | P07    | Active  |
| bld_output_template   | Structures final report       | P07    | Active  |
| bld_examples          | Supplies reference data       | P07    | Active  |
| bld_knowledge_card    | Embeds domain-specific info   | P07    | Active  |
| bld_architecture      | Maps report to system layers  | P07    | Active  |
| bld_collaboration     | Manages cross-component sync  | P07    | Active  |
| bld_config            | Stores runtime parameters     | P07    | Active  |
| bld_memory            | Tracks session state          | P07    | Active  |
| bld_tools             | Integrates external utilities | P07    | Active  |

## Dependencies
| From          | To            | Type      |
|---------------|---------------|-----------|
| bld_manifest  | bld_config    | config    |
| bld_instruction | bld_system_prompt | control |
| bld_quality_gate | bld_schema | data      |
| bld_output_template | bld_examples | data  |
| bld_tools     | bld_memory    | control   |

## Architectural Position
usage_report sits at the intersection of data aggregation and compliance enforcement in CEX P07, translating raw system interactions into structured, auditable reports through a pipeline of specialized builders, ensuring transparency and regulatory alignment across execution layers.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_eval_metric]] | sibling | 0.83 |
| [[bld_architecture_cohort_analysis]] | sibling | 0.82 |
| [[bld_architecture_eval_framework]] | sibling | 0.82 |
| [[bld_architecture_judge_config]] | sibling | 0.81 |
| [[bld_architecture_benchmark_suite]] | sibling | 0.62 |
| [[bld_architecture_discovery_questions]] | sibling | 0.61 |
| [[bld_architecture_onboarding_flow]] | sibling | 0.59 |
| [[bld_architecture_memory_benchmark]] | sibling | 0.59 |
| [[bld_architecture_roi_calculator]] | sibling | 0.58 |
| [[bld_architecture_sdk_example]] | sibling | 0.58 |
