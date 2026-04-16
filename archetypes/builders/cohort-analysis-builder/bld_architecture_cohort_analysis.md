---
kind: architecture
id: bld_architecture_cohort_analysis
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of cohort_analysis -- inventory, dependencies
quality: 9.0
title: "Architecture Cohort Analysis"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [cohort_analysis, builder, architecture]
tldr: "Component map of cohort_analysis -- inventory, dependencies"
domain: "cohort_analysis construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Component Inventory
| ISO Name            | Role                                | Pillar | Status  |
|---------------------|-------------------------------------|--------|---------|
| bld_manifest        | Defines analysis structure          | P07    | Active  |
| bld_instruction     | Specifies processing rules          | P07    | Active  |
| bld_system_prompt   | Sets LLM interaction guidelines     | P07    | Active  |
| bld_schema          | Enforces data format standards      | P07    | Active  |
| bld_quality_gate    | Validates output integrity          | P07    | Active  |
| bld_output_template | Structures final deliverables       | P07    | Active  |
| bld_examples        | Provides reference use cases        | P07    | Active  |
| bld_knowledge_card  | Documents domain-specific insights  | P07    | Active  |
| bld_architecture    | Maps component relationships        | P07    | Active  |
| bld_collaboration   | Enables team coordination           | P07    | Active  |
| bld_config          | Manages runtime parameters          | P07    | Active  |
| bld_memory          | Stores session context              | P07    | Active  |
| bld_tools           | Integrates external analysis tools  | P07    | Active  |

## Dependencies
| From              | To                  | Type           |
|-------------------|---------------------|----------------|
| bld_manifest      | bld_config          | configuration  |
| bld_instruction   | bld_schema          | structural     |
| bld_quality_gate  | bld_schema          | validation     |
| bld_output_template | bld_examples     | templating     |
| bld_tools         | data_lake           | data access    |
| bld_memory        | bld_tools           | tool integration |

## Architectural Position
cohort_analysis sits at the core of P07, orchestrating structured data exploration by harmonizing schema enforcement, quality validation, and collaborative workflows. It bridges domain-specific knowledge (via knowledge_cards) with technical execution (via tools), ensuring consistent, reusable analysis pipelines aligned with CEX's operational rigor.
