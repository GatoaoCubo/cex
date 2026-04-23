---
kind: architecture
id: bld_architecture_subscription_tier
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of subscription_tier -- inventory, dependencies
quality: 9.0
title: "Architecture Subscription Tier"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [subscription_tier, builder, architecture]
tldr: "Component map of subscription_tier -- inventory, dependencies"
domain: "subscription_tier construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_architecture_self_improvement_loop
  - bld_architecture_compliance_checklist
  - bld_architecture_ab_test_config
  - bld_architecture_audit_log
  - bld_architecture_enterprise_sla
  - bld_architecture_roi_calculator
  - bld_architecture_api_reference
  - bld_architecture_sales_playbook
  - bld_architecture_discovery_questions
  - bld_architecture_quickstart_guide
---

## Component Inventory
| ISO Name             | Role                          | Pillar | Status |
|----------------------|-------------------------------|--------|--------|
| bld_manifest         | Core configuration definition | P11    | Active |
| bld_instruction      | Instruction generation logic  | P11    | Active |
| bld_system_prompt    | System-level guidance         | P11    | Active |
| bld_schema           | Data structure validation     | P11    | Active |
| bld_quality_gate     | Quality assurance checks      | P11    | Active |
| bld_output_template  | Output formatting             | P11    | Active |
| bld_examples         | Sample data provision         | P11    | Active |
| bld_knowledge_card   | Knowledge management          | P11    | Active |
| bld_architecture     | Structural design             | P11    | Active |
| bld_collaboration    | Team coordination             | P11    | Active |
| bld_config           | Configuration management      | P11    | Active |
| bld_memory           | Data retention                 | P11    | Active |
| bld_tools            | Tool integration              | P11    | Active |

## Dependencies
| From           | To               | Type         |
|----------------|------------------|--------------|
| bld_config     | bld_manifest     | Configuration|
| bld_quality_gate | bld_schema     | Validation   |
| bld_output_template | bld_instruction | Formatting   |
| bld_tools      | bld_memory       | Storage      |
| bld_collaboration | bld_knowledge_card | Knowledge Sharing |

## Architectural Position
subscription_tier is a foundational component in CEX pillar P11, orchestrating tier-specific configurations, ensuring consistency, quality, and collaboration across subscription levels through integrated tools, memory systems, and schema validation.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_self_improvement_loop]] | sibling | 0.84 |
| [[bld_architecture_compliance_checklist]] | sibling | 0.84 |
| [[bld_architecture_ab_test_config]] | sibling | 0.81 |
| [[bld_architecture_audit_log]] | sibling | 0.78 |
| [[bld_architecture_enterprise_sla]] | sibling | 0.77 |
| [[bld_architecture_roi_calculator]] | sibling | 0.68 |
| [[bld_architecture_api_reference]] | sibling | 0.62 |
| [[bld_architecture_sales_playbook]] | sibling | 0.60 |
| [[bld_architecture_discovery_questions]] | sibling | 0.60 |
| [[bld_architecture_quickstart_guide]] | sibling | 0.59 |
