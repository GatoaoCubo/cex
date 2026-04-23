---
kind: architecture
id: bld_architecture_role_assignment
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of role_assignment -- inventory, dependencies
quality: 9.0
title: "Architecture Role Assignment"
version: "1.0.0"
author: n03_wave8_builder
tags: [role_assignment, builder, architecture, composable, crewai]
tldr: "Component map of role_assignment -- inventory, dependencies"
domain: "role_assignment construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.87
related:
  - bld_architecture_crew_template
  - bld_architecture_roi_calculator
  - bld_architecture_benchmark_suite
  - bld_architecture_app_directory_entry
  - bld_architecture_churn_prevention_playbook
  - bld_architecture_legal_vertical
  - bld_architecture_memory_benchmark
  - bld_architecture_api_reference
  - bld_architecture_fintech_vertical
  - bld_architecture_github_issue_template
---

## Component Inventory
| ISO Name              | Role                           | Pillar | Status  |
|-----------------------|--------------------------------|--------|---------|
| bld_manifest          | Builder identity               | P02    | Active  |
| bld_instruction       | Production phases              | P03    | Active  |
| bld_system_prompt     | LLM persona + rules            | P03    | Active  |
| bld_schema            | Frontmatter + body contract    | P06    | Active  |
| bld_quality_gate      | HARD/SOFT scoring              | P11    | Active  |
| bld_output_template   | Concrete template              | P05    | Active  |
| bld_examples          | Golden + anti-examples         | P07    | Active  |
| bld_knowledge_card    | Domain knowledge               | P01    | Active  |
| bld_architecture      | This file                      | P08    | Active  |
| bld_collaboration     | Crew wiring (upstream/down)    | P12    | Active  |
| bld_config            | Naming, paths, limits          | P09    | Active  |
| bld_memory            | Learning record                | P10    | Active  |
| bld_tools             | Production + validation tools  | P04    | Active  |

## Dependencies
| From              | To                       | Type          |
|-------------------|--------------------------|---------------|
| bld_manifest      | bld_config               | configuration |
| bld_instruction   | bld_system_prompt        | dependency    |
| bld_output_template | bld_schema             | dependency    |
| bld_quality_gate  | bld_examples             | validation    |
| bld_collaboration | agent-builder            | identity source (agent_id)|
| bld_collaboration | crew-template-builder    | composition (referenced by)|
| bld_collaboration | toolkit-builder          | tools_allowed source |
| bld_tools         | cex_compile.py           | integration   |

## Architectural Position
role_assignment is the atomic role-binding primitive of CEX P02 model pillar, sitting directly beneath crew_template (P12) in the composable-crew stack. Analogy: if crew_template is the class definition of a team, role_assignment is the field declaration for each member. Downstream: supervisor (P12) instantiates roles at runtime, workflow (P12) may reference roles in step specs. Upstream: agent-builder (P02) provides the agent_id registry path, toolkit-builder (P04) provides the native tool set from which tools_allowed is subset-selected. This decoupling enables role reuse across crews and agent swapping without rewriting team compositions.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_crew_template]] | sibling | 0.74 |
| [[bld_architecture_roi_calculator]] | sibling | 0.64 |
| [[bld_architecture_benchmark_suite]] | sibling | 0.63 |
| [[bld_architecture_app_directory_entry]] | sibling | 0.63 |
| [[bld_architecture_churn_prevention_playbook]] | sibling | 0.63 |
| [[bld_architecture_legal_vertical]] | sibling | 0.63 |
| [[bld_architecture_memory_benchmark]] | sibling | 0.62 |
| [[bld_architecture_api_reference]] | sibling | 0.62 |
| [[bld_architecture_fintech_vertical]] | sibling | 0.62 |
| [[bld_architecture_github_issue_template]] | sibling | 0.62 |
