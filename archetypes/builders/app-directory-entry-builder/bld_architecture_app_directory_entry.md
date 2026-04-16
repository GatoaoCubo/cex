---
kind: architecture
id: bld_architecture_app_directory_entry
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of app_directory_entry -- inventory, dependencies
quality: 9.0
title: "Architecture App Directory Entry"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [app_directory_entry, builder, architecture]
tldr: "Component map of app_directory_entry -- inventory, dependencies"
domain: "app_directory_entry construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Component Inventory
| ISO Name             | Role                                                      | Pillar | Status  |
|----------------------|-----------------------------------------------------------|--------|---------|
| bld_manifest         | Builder identity, capabilities, routing                   | P05    | Active  |
| bld_instruction      | 3-phase production process (Research, Compose, Validate)  | P03    | Active  |
| bld_system_prompt    | LLM persona and ALWAYS/NEVER rules                        | P03    | Active  |
| bld_schema           | Frontmatter fields + body structure (SSOT)                | P06    | Active  |
| bld_quality_gate     | HARD gates (H01-H08) + SOFT scoring (D01-D08)             | P11    | Active  |
| bld_output_template  | Production template with var guidance                     | P05    | Active  |
| bld_examples         | Golden + anti-examples with failure analysis              | P07    | Active  |
| bld_knowledge_card   | Domain knowledge: app directory standards + pitfalls      | P01    | Active  |
| bld_architecture     | This document: ISO map + dependencies                     | P08    | Active  |
| bld_collaboration    | Cross-builder workflow coordination                       | P12    | Active  |
| bld_config           | Naming, paths, limits, hooks                              | P09    | Active  |
| bld_memory           | Learned patterns and pitfalls (memory)                    | P10    | Active  |
| bld_tools            | Production + validation tools (CEX-native)                | P04    | Active  |

## Dependencies
| From               | To                   | Type         |
|--------------------|----------------------|--------------|
| bld_manifest       | bld_instruction      | Control Flow |
| bld_schema         | bld_output_template  | Data Flow    |
| bld_quality_gate   | bld_examples         | Validation   |
| bld_config         | bld_memory           | Configuration|
| bld_tools          | external API         | Integration  |

## Architectural Position
app_directory_entry serves as the central registry and coordination hub for P05's builder ISOs, enabling structured application development through standardized manifests, quality gates, and cross-component dependencies, aligning with CEX's focus on modular, reusable, and auditable software constructs.
