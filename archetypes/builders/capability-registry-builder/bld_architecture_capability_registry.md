---
kind: architecture
id: bld_architecture_capability_registry
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of capability_registry -- inventory, dependencies
quality: 9.1
title: "Architecture Capability Registry"
version: "1.0.0"
author: n04_wave8
tags: [capability_registry, builder, architecture, agent-discovery]
tldr: "Component map of capability_registry -- inventory, dependencies"
domain: "capability_registry construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_architecture_legal_vertical
  - bld_architecture_app_directory_entry
  - bld_architecture_roi_calculator
  - bld_architecture_benchmark_suite
  - bld_architecture_api_reference
  - bld_architecture_memory_benchmark
  - bld_architecture_fintech_vertical
  - bld_architecture_discovery_questions
  - bld_architecture_churn_prevention_playbook
  - bld_architecture_sdk_example
---

## Component Inventory
| ISO Name                      | Role                                     | Pillar | Status  |
|-------------------------------|------------------------------------------|--------|---------|
| bld_manifest_capability_registry    | Builder identity and routing          | P08    | Active  |
| bld_instruction_capability_registry | Step-by-step production process       | P03    | Active  |
| bld_system_prompt_capability_registry| LLM persona and rules                | P03    | Active  |
| bld_schema_capability_registry      | Data structure definition             | P06    | Active  |
| bld_quality_gate_capability_registry| Validation rules                      | P11    | Active  |
| bld_output_template_capability_registry| Formatting specification           | P05    | Active  |
| bld_examples_capability_registry    | Golden and anti-examples              | P07    | Active  |
| bld_knowledge_card_capability_registry| Domain knowledge injection          | P01    | Active  |
| bld_architecture_capability_registry| System blueprint (this file)         | P08    | Active  |
| bld_collaboration_capability_registry| Workflow coordination               | P12    | Active  |
| bld_config_capability_registry      | Naming, paths, limits                 | P09    | Active  |
| bld_memory_capability_registry      | Learned patterns and pitfalls         | P10    | Active  |
| bld_tools_capability_registry       | External integrations                 | P04    | Active  |

## Dependencies
| From                          | To                                      | Type         |
|-------------------------------|------------------------------------------|--------------|
| bld_instruction               | bld_schema                              | depends-on   |
| bld_instruction               | bld_system_prompt                       | depends-on   |
| bld_output_template           | bld_schema                              | implements   |
| bld_quality_gate              | bld_examples                            | validates-against |
| bld_quality_gate              | bld_schema                              | enforces     |
| bld_collaboration             | bld_memory                              | informs      |
| bld_tools                     | .claude/agents/ (external)              | indexes      |
| bld_tools                     | N0x_*/agents/ (external)               | indexes      |
| bld_tools                     | cex_query.py (external)                 | integrates   |

## Data Flow
```
.claude/agents/*-builder.md        -->  capability-registry-builder
N0x_*/agents/agent_*.md            -->  capability-registry-builder
N0x_*/agent_card_n0x.md           -->  capability-registry-builder
                                         |
                              bld_instruction (scan + extract)
                                         |
                              bld_schema (normalize + validate)
                                         |
                              bld_output_template (render registry)
                                         |
                    p08_cr_{{name}}.md (output: queryable registry)
                                         |
                              N07 crew orchestrator (consumer)
```

## Architectural Position
capability_registry occupies the CONSTRAIN position in P08 (Architecture). It answers "who?" before dispatch answers "how?" -- the prerequisite query layer that prevents blind routing. It is consumed by N07 at F1 CONSTRAIN and by any crew that needs ranked agent selection before executing a wave.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_legal_vertical]] | sibling | 0.62 |
| [[bld_architecture_app_directory_entry]] | sibling | 0.62 |
| [[bld_architecture_roi_calculator]] | sibling | 0.61 |
| [[bld_architecture_benchmark_suite]] | sibling | 0.61 |
| [[bld_architecture_api_reference]] | sibling | 0.61 |
| [[bld_architecture_memory_benchmark]] | sibling | 0.60 |
| [[bld_architecture_fintech_vertical]] | sibling | 0.59 |
| [[bld_architecture_discovery_questions]] | sibling | 0.59 |
| [[bld_architecture_churn_prevention_playbook]] | sibling | 0.59 |
| [[bld_architecture_sdk_example]] | sibling | 0.58 |
