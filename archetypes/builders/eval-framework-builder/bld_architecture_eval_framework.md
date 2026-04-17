---
kind: architecture
id: bld_architecture_eval_framework
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of eval_framework -- inventory, dependencies
quality: 9.0
title: "Architecture Eval Framework"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [eval_framework, builder, architecture]
tldr: "Component map of eval_framework -- inventory, dependencies"
domain: "eval_framework construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Component Inventory
| ISO Name           | Role                          | Pillar | Status  |
|--------------------|-------------------------------|--------|---------|
| bld_manifest       | Defines framework structure   | P07    | Active  |
| bld_instruction    | Specifies evaluation tasks    | P07    | Active  |
| bld_system_prompt  | Sets system behavior rules    | P07    | Active  |
| bld_schema         | Defines data structure format | P07    | Active  |
| bld_quality_gate   | Enforces output quality rules | P07    | Active  |
| bld_output_template| Formats evaluation results    | P07    | Active  |
| bld_examples       | Provides sample inputs/outputs| P07    | Active  |
| bld_knowledge_card | Stores domain-specific info   | P07    | Active  |
| bld_architecture   | Documents framework design    | P07    | Active  |
| bld_collaboration  | Manages team coordination     | P07    | Active  |
| bld_config         | Centralizes configuration     | P07    | Active  |
| bld_memory         | Tracks evaluation history     | P07    | Active  |
| bld_tools          | Integrates evaluation utilities| P07   | Active  |

## Dependencies
| From             | To               | Type       |
|------------------|------------------|------------|
| bld_instruction  | bld_manifest     | Reference  |
| bld_quality_gate | bld_schema       | Validation |
| bld_output_template | bld_schema   | Dependency |
| bld_examples     | bld_instruction  | Data Source|
| bld_config       | bld_tools        | Configuration|

## Architectural Position
The eval_framework serves as the central evaluation engine within CEX P07, ensuring consistency, quality, and alignment across all builder ISOs by standardizing processes, enforcing quality gates, and enabling collaborative validation through shared configurations and templates.
