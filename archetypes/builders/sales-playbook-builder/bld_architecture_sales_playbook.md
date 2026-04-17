---
kind: architecture
id: bld_architecture_sales_playbook
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of sales_playbook -- inventory, dependencies
quality: 9.0
title: "Architecture Sales Playbook"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [sales_playbook, builder, architecture]
tldr: "Component map of sales_playbook -- inventory, dependencies"
domain: "sales_playbook construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Component Inventory
| ISO Name             | Role                          | Pillar | Status  |
|----------------------|-------------------------------|--------|---------|
| bld_manifest         | Playbook structure definition | P11    | Active  |
| bld_instruction      | Sales process guidance        | P03    | Active  |
| bld_system_prompt    | LLM interaction framework     | P03    | Active  |
| bld_schema           | Data model specification      | P06    | Active  |
| bld_quality_gate     | Validation rules              | P11    | Active  |
| bld_output_template  | Formatting standards          | P05    | Active  |
| bld_examples         | Use case repository           | P07    | Active  |
| bld_knowledge_card   | Domain-specific insights      | P01    | Active  |
| bld_architecture     | System blueprint              | P08    | Active  |
| bld_collaboration    | Team coordination logic       | P12    | Active  |
| bld_config           | Parameter management          | P09    | Active  |
| bld_memory           | Context retention mechanism   | P10    | Active  |
| bld_tools            | Utility functions             | P04    | Active  |

## Dependencies
| From              | To                  | Type        |
|-------------------|---------------------|-------------|
| bld_manifest      | bld_instruction     | Reference   |
| bld_system_prompt | bld_schema          | Dependency  |
| bld_quality_gate  | bld_output_template | Validation  |
| bld_knowledge_card| bld_examples        | Data Source |
| bld_config        | bld_memory          | Configuration |
| bld_tools         | external LLM        | Integration |

## Architectural Position
The sales_playbook-builder (P03) serves as the central orchestration layer for sales strategy automation within the CEX ecosystem, enabling dynamic generation of customer-facing playbooks through structured ISO interactions. It integrates domain-specific knowledge (bld_knowledge_card) with configurable workflows (bld_config) to produce validated, reusable sales assets aligned with enterprise-grade compliance and operational standards.
