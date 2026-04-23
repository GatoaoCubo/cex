---
kind: architecture
id: bld_architecture_audit_log
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of audit_log -- inventory, dependencies
quality: 9.0
title: "Architecture Audit Log"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [audit_log, builder, architecture]
tldr: "Component map of audit_log -- inventory, dependencies"
domain: "audit_log construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_architecture_ab_test_config
  - bld_architecture_compliance_checklist
  - bld_architecture_subscription_tier
  - bld_architecture_self_improvement_loop
  - bld_architecture_enterprise_sla
  - bld_architecture_roi_calculator
  - bld_architecture_discovery_questions
  - bld_architecture_sdk_example
  - bld_architecture_onboarding_flow
  - bld_architecture_api_reference
---

## Component Inventory
| ISO Name             | Role                          | Pillar | Status  |
|----------------------|-------------------------------|--------|---------|
| bld_manifest         | Defines audit log structure   | P11    | Active  |
| bld_instruction      | Specifies logging procedures  | P11    | Active  |
| bld_system_prompt    | Guides AI audit behavior      | P11    | Active  |
| bld_schema           | Enforces data format rules    | P11    | Active  |
| bld_quality_gate     | Validates log integrity       | P11    | Active  |
| bld_output_template  | Structures log output         | P11    | Active  |
| bld_examples         | Provides audit log samples    | P11    | Active  |
| bld_knowledge_card   | Stores audit policies         | P11    | Active  |
| bld_architecture     | Defines system layering       | P11    | Active  |
| bld_collaboration    | Manages team audit workflows  | P11    | Active  |
| bld_config           | Centralizes audit settings    | P11    | Active  |
| bld_memory           | Tracks audit history          | P11    | Active  |
| bld_tools            | Integrates audit utilities    | P11    | Active  |

## Dependencies
| From              | To                  | Type       |
|-------------------|---------------------|------------|
| bld_manifest      | bld_schema          | Data       |
| bld_instruction   | bld_system_prompt   | Control    |
| bld_quality_gate  | bld_output_template | Validation |
| bld_config        | bld_memory          | Configuration |
| bld_tools         | audit_db            | External   |

## Architectural Position
audit_log sits at the core of CEX pillar P11, ensuring compliance, transparency, and traceability by centralizing audit data flows, enforcing policy adherence through quality gates, and enabling cross-component validation across the builder ISOs.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_ab_test_config]] | sibling | 0.78 |
| [[bld_architecture_compliance_checklist]] | sibling | 0.78 |
| [[bld_architecture_subscription_tier]] | sibling | 0.77 |
| [[bld_architecture_self_improvement_loop]] | sibling | 0.76 |
| [[bld_architecture_enterprise_sla]] | sibling | 0.69 |
| [[bld_architecture_roi_calculator]] | sibling | 0.60 |
| [[bld_architecture_discovery_questions]] | sibling | 0.60 |
| [[bld_architecture_sdk_example]] | sibling | 0.56 |
| [[bld_architecture_onboarding_flow]] | sibling | 0.55 |
| [[bld_architecture_api_reference]] | sibling | 0.54 |
