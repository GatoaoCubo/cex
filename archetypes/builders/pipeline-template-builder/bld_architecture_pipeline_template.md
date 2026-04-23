---
quality: 8.2
quality: 7.8
kind: architecture
id: bld_architecture_pipeline_template
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of pipeline_template -- inventory, dependencies
title: "Architecture Pipeline Template"
version: "1.0.0"
author: n03_hermes_w1_5
tags: [pipeline_template, builder, architecture, hermes, scenario_indexed]
tldr: "Component map of pipeline_template -- inventory, dependencies"
domain: "pipeline_template construction"
created: "2026-04-18"
updated: "2026-04-18"
density_score: 0.87
related:
  - bld_architecture_crew_template
  - bld_architecture_role_assignment
  - bld_architecture_roi_calculator
  - bld_architecture_benchmark_suite
  - bld_architecture_app_directory_entry
  - bld_architecture_llm_evaluation_scenario
  - bld_architecture_churn_prevention_playbook
  - bld_architecture_github_issue_template
  - bld_architecture_discovery_questions
  - bld_architecture_legal_vertical
---

## Component Inventory
| ISO Name              | Role                          | Pillar | Status  |
|-----------------------|-------------------------------|--------|---------|
| bld_manifest          | Builder identity              | P12    | Active  |
| bld_instruction       | Production phases             | P03    | Active  |
| bld_system_prompt     | LLM persona + rules           | P03    | Active  |
| bld_schema            | Frontmatter + body contract   | P06    | Active  |
| bld_quality_gate      | HARD/SOFT scoring             | P11    | Active  |
| bld_output_template   | Concrete template             | P05    | Active  |
| bld_examples          | Golden + anti-examples        | P07    | Active  |
| bld_knowledge_card    | Domain knowledge              | P01    | Active  |
| bld_architecture      | This file                     | P08    | Active  |
| bld_collaboration     | Crew/workflow wiring          | P12    | Active  |
| bld_config            | Naming, limits                | P09    | Active  |
| bld_memory            | Learning record               | P10    | Active  |
| bld_tools             | Production + validation tools | P04    | Active  |

## Dependencies
| From              | To                          | Type         |
|-------------------|-----------------------------|--------------|
| bld_manifest      | bld_config                  | configuration|
| bld_instruction   | bld_system_prompt           | dependency   |
| bld_output_template | bld_schema                | dependency   |
| bld_quality_gate  | bld_examples                | validation   |
| bld_collaboration | workflow-builder            | composition  |
| bld_collaboration | crew-template-builder       | boundary     |
| bld_collaboration | supervisor-builder          | runtime      |
| bld_tools         | cex_compile.py              | integration  |

## Architectural Position
pipeline_template is the scenario-indexed recipe primitive of CEX P12 orchestration. It sits between role definition (role_assignment, P02) and runtime execution (supervisor, P12). Unlike crew_template (flexible topology, N-role teams), pipeline_template encodes a deterministic stage sequence for a specific software engineering scenario. The 7-scenario catalog from OpenCode-Hermes maps directly to the 7 canonical pipeline_template instances: each scenario gets one canonical template, reducing orchestration decisions from "what stages?" to "which scenario?".

Runtime stack: pipeline_template (recipe) + team_charter (mission contract) + supervisor (executor). The template provides the WHAT (stages, gates, loop), the charter provides the WHO (codebase, task, deadline), and the supervisor provides the HOW (model routing, signal handling).

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_crew_template]] | sibling | 0.72 |
| [[bld_architecture_role_assignment]] | sibling | 0.68 |
| [[bld_architecture_roi_calculator]] | sibling | 0.63 |
| [[bld_architecture_benchmark_suite]] | sibling | 0.62 |
| [[bld_architecture_app_directory_entry]] | sibling | 0.62 |
| [[bld_architecture_llm_evaluation_scenario]] | sibling | 0.62 |
| [[bld_architecture_churn_prevention_playbook]] | sibling | 0.61 |
| [[bld_architecture_github_issue_template]] | sibling | 0.61 |
| [[bld_architecture_discovery_questions]] | sibling | 0.61 |
| [[bld_architecture_legal_vertical]] | sibling | 0.60 |
