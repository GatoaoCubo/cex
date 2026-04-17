---
kind: architecture
id: bld_architecture_legal_vertical
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of legal_vertical -- inventory, dependencies
quality: 9.0
title: "Architecture Legal Vertical"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [legal_vertical, builder, architecture]
tldr: "Component map of legal_vertical -- inventory, dependencies"
domain: "legal_vertical construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Component Inventory
| ISO Name             | Role                                      | Pillar | Kind             | Status |
|----------------------|-------------------------------------------|--------|------------------|--------|
| bld_manifest         | Builder identity, capabilities            | P01    | type_builder     | Active |
| bld_instruction      | Step-by-step production process           | P03    | instruction      | Active |
| bld_system_prompt    | Agent persona and rules                   | P03    | system_prompt    | Active |
| bld_schema           | Formal schema, naming, constraints        | P06    | schema           | Active |
| bld_quality_gate     | HARD+SOFT scoring gates                   | P11    | quality_gate     | Active |
| bld_output_template  | Output structure with placeholders        | P05    | output_template  | Active |
| bld_examples         | Reference artifacts for in-context use    | P01    | knowledge_card   | Active |
| bld_knowledge_card   | Domain knowledge for INJECT phase         | P01    | knowledge_card   | Active |
| bld_architecture     | Component map and dependencies            | P08    | architecture     | Active |
| bld_collaboration    | Cross-nucleus handoff patterns            | P12    | collaboration    | Active |
| bld_config           | Naming, paths, limits                     | P09    | config           | Active |
| bld_memory           | Learned patterns and pitfalls             | P10    | memory           | Active |
| bld_tools            | CEX tools + external references           | P04    | tools            | Active |

## Dependencies
| From           | To              | Type       |
|----------------|-----------------|------------|
| bld_instruction| bld_schema      | Data       |
| bld_quality_gate| bld_config     | Configuration |
| bld_output_template| bld_schema | Data       |
| bld_tools      | legal_db        | External   |
| bld_memory     | bld_config      | Configuration |

## Architectural Position
The legal_vertical-builder (P01) serves as the compliance and governance backbone of the CEX ecosystem, ensuring all legal workflows, standards, and enforcement mechanisms are rigorously encoded, validated, and integrated across the system.
