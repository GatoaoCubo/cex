---
kind: architecture
id: bld_architecture_benchmark_suite
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of benchmark_suite -- inventory, dependencies
quality: 9.0
title: "Architecture Benchmark Suite"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [benchmark_suite, builder, architecture]
tldr: "Component map of benchmark_suite -- inventory, dependencies"
domain: "benchmark_suite construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_architecture_memory_benchmark
  - bld_architecture_app_directory_entry
  - bld_architecture_legal_vertical
  - bld_architecture_roi_calculator
  - bld_architecture_api_reference
  - bld_architecture_fintech_vertical
  - bld_architecture_github_issue_template
  - bld_architecture_discovery_questions
  - bld_architecture_sdk_example
  - bld_architecture_healthcare_vertical
---

## Component Inventory
| ISO Name             | Role                          | Pillar | Status  |
|----------------------|-------------------------------|--------|---------|
| bld_manifest         | Builder identity and routing  | P07    | Active  |
| bld_instruction      | Step-by-step production guide | P03    | Active  |
| bld_system_prompt    | Builder persona and rules     | P03    | Active  |
| bld_schema           | Formal data contract (SSOT)   | P06    | Active  |
| bld_quality_gate     | HARD/SOFT scoring gates       | P11    | Active  |
| bld_output_template  | Output skeleton with vars     | P05    | Active  |
| bld_examples         | Sample input/output pairs     | P07    | Active  |
| bld_knowledge_card   | Domain knowledge injection    | P01    | Active  |
| bld_architecture     | ISO inventory and deps        | P08    | Active  |
| bld_collaboration    | Crew coordination protocol    | P12    | Active  |
| bld_config           | Runtime configuration         | P09    | Active  |
| bld_memory           | Learned patterns (memory ISO) | P10    | Active  |
| bld_tools            | Tool registry for F5 CALL     | P04    | Active  |

## Dependencies
| From              | To                  | Type         |
|-------------------|---------------------|--------------|
| bld_manifest      | bld_config          | Configuration|
| bld_instruction   | bld_system_prompt   | Data         |
| bld_quality_gate  | bld_schema          | Validation   |
| bld_output_template | bld_examples      | Template     |
| bld_tools         | CI/CD pipeline      | Integration  |

## Architectural Position
benchmark_suite serves as the central orchestrator in P07, standardizing benchmark creation through structured definitions, quality gates, and collaboration frameworks. It ensures consistency across system prompts, schemas, and output formats while enabling adaptability via configurable tools and memory mechanisms, aligning with CEX's focus on rigorous evaluation and reproducible results.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_memory_benchmark]] | sibling | 0.78 |
| [[bld_architecture_app_directory_entry]] | sibling | 0.74 |
| [[bld_architecture_legal_vertical]] | sibling | 0.73 |
| [[bld_architecture_roi_calculator]] | sibling | 0.73 |
| [[bld_architecture_api_reference]] | sibling | 0.73 |
| [[bld_architecture_fintech_vertical]] | sibling | 0.71 |
| [[bld_architecture_github_issue_template]] | sibling | 0.70 |
| [[bld_architecture_discovery_questions]] | sibling | 0.70 |
| [[bld_architecture_sdk_example]] | sibling | 0.69 |
| [[bld_architecture_healthcare_vertical]] | sibling | 0.69 |
