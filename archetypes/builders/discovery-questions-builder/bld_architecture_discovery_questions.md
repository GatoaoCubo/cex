---
kind: architecture
id: bld_architecture_discovery_questions
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of discovery_questions -- inventory, dependencies
quality: 9.0
title: "Architecture Discovery Questions"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [discovery_questions, builder, architecture]
tldr: "Component map of discovery_questions -- inventory, dependencies"
domain: "discovery_questions construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_architecture_roi_calculator
  - bld_architecture_sdk_example
  - bld_architecture_api_reference
  - bld_architecture_onboarding_flow
  - bld_architecture_sales_playbook
  - bld_architecture_legal_vertical
  - bld_architecture_benchmark_suite
  - bld_architecture_quickstart_guide
  - bld_architecture_fintech_vertical
  - bld_architecture_healthcare_vertical
---

## Component Inventory
| ISO Name             | Role                          | Pillar | Status |
|----------------------|-------------------------------|--------|--------|
| bld_manifest         | Defines builder structure     | P11    | Active |
| bld_instruction      | Specifies task parameters     | P03    | Active |
| bld_system_prompt    | Sets LLM interaction rules    | P03    | Active |
| bld_schema           | Enforces data format          | P06    | Active |
| bld_quality_gate     | Validates output compliance   | P11    | Active |
| bld_output_template  | Structures final responses    | P05    | Active |
| bld_examples         | Provides training samples     | P07    | Active |
| bld_knowledge_card   | Embeds domain-specific info   | P01    | Active |
| bld_architecture     | Maps builder components       | P08    | Active |
| bld_collaboration    | Manages team input workflows  | P12    | Active |
| bld_config           | Stores runtime parameters     | P09    | Active |
| bld_memory           | Tracks session context        | P10    | Active |
| bld_tools            | Integrates external utilities | P04    | Active |

## Dependencies
| From              | To                  | Type       |
|-------------------|---------------------|------------|
| bld_instruction   | bld_manifest        | Definition |
| bld_system_prompt | bld_knowledge_card  | Reference  |
| bld_quality_gate  | bld_schema          | Validation |
| bld_output_template | bld_config       | Configuration |
| bld_tools         | LLM API             | External   |

## Architectural Position
discovery_questions sits at the core of CEX P01, enabling structured question generation through ISO-driven modularity. It integrates with knowledge, configuration, and validation components to ensure alignment with domain-specific requirements, while collaboration and memory ISOs sustain iterative refinement and contextual continuity.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_roi_calculator]] | sibling | 0.75 |
| [[bld_architecture_sdk_example]] | sibling | 0.75 |
| [[bld_architecture_api_reference]] | sibling | 0.74 |
| [[bld_architecture_onboarding_flow]] | sibling | 0.74 |
| [[bld_architecture_sales_playbook]] | sibling | 0.72 |
| [[bld_architecture_legal_vertical]] | sibling | 0.71 |
| [[bld_architecture_benchmark_suite]] | sibling | 0.71 |
| [[bld_architecture_quickstart_guide]] | sibling | 0.71 |
| [[bld_architecture_fintech_vertical]] | sibling | 0.71 |
| [[bld_architecture_healthcare_vertical]] | sibling | 0.69 |
