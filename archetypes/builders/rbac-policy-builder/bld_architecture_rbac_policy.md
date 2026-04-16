---
kind: architecture
id: bld_architecture_rbac_policy
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of rbac_policy -- inventory, dependencies
quality: 9.0
title: "Architecture Rbac Policy"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [rbac_policy, builder, architecture]
tldr: "Component map of rbac_policy -- inventory, dependencies"
domain: "rbac_policy construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Component Inventory
| ISO Name              | Role                          | Pillar | Status |
|-----------------------|-------------------------------|--------|--------|
| bld_manifest          | Defines policy structure      | P09    | Active |
| bld_instruction       | Specifies user instructions   | P09    | Active |
| bld_system_prompt     | Sets system behavior rules    | P09    | Active |
| bld_schema            | Enforces data format          | P09    | Active |
| bld_quality_gate      | Validates policy compliance   | P09    | Active |
| bld_output_template   | Structures policy outputs     | P09    | Active |
| bld_examples          | Provides policy use cases     | P09    | Active |
| bld_knowledge_card    | Documents policy logic        | P09    | Active |
| bld_architecture      | Maps policy to system layers  | P09    | Active |
| bld_collaboration     | Manages stakeholder input     | P09    | Active |
| bld_config            | Stores policy parameters      | P09    | Active |
| bld_memory            | Tracks policy execution state | P09    | Active |
| bld_tools             | Integrates policy enforcement | P09    | Active |

## Dependencies
| From              | To                  | Type         |
|-------------------|---------------------|--------------|
| bld_manifest      | bld_instruction     | Data         |
| bld_manifest      | bld_system_prompt   | Control      |
| bld_quality_gate  | bld_output_template | Validation   |
| bld_config        | bld_memory          | Configuration|
| bld_tools         | policy_engine       | Integration  |

## Architectural Position
rbac_policy sits at the core of CEX pillar P09, orchestrating role-based access control by translating stakeholder requirements (via bld_instruction, bld_collaboration) into enforceable policies through schema validation (bld_schema), quality checks (bld_quality_gate), and integration with external enforcement tools (policy_engine). It ensures alignment with P09's governance objectives by maintaining traceability across policy lifecycle stages.
