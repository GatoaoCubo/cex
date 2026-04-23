---
kind: architecture
id: bld_architecture_enterprise_sla
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of enterprise_sla -- inventory, dependencies
quality: 9.0
title: "Architecture Enterprise Sla"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [enterprise_sla, builder, architecture]
tldr: "Component map of enterprise_sla -- inventory, dependencies"
domain: "enterprise_sla construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_architecture_compliance_checklist
  - bld_architecture_subscription_tier
  - bld_architecture_self_improvement_loop
  - bld_architecture_ab_test_config
  - bld_architecture_audit_log
  - bld_architecture_roi_calculator
  - bld_architecture_sales_playbook
  - bld_architecture_discovery_questions
  - bld_architecture_api_reference
  - bld_architecture_onboarding_flow
---

## Component Inventory
| ISO Name              | Role                          | Pillar | Status  |
|-----------------------|-------------------------------|--------|---------|
| bld_manifest          | SLA structure definition      | P11    | Active  |
| bld_instruction       | Operational guidelines        | P11    | Active  |
| bld_system_prompt     | User interaction framework    | P11    | Active  |
| bld_schema            | Data model specification      | P11    | Active  |
| bld_quality_gate      | Compliance validation         | P11    | Active  |
| bld_output_template   | SLA formatting rules          | P11    | Active  |
| bld_examples          | Sample SLA scenarios          | P11    | Active  |
| bld_knowledge_card    | Domain-specific reference     | P11    | Active  |
| bld_architecture      | System integration blueprint  | P11    | Active  |
| bld_collaboration     | Stakeholder alignment         | P11    | Active  |
| bld_config            | Configuration management      | P11    | Active  |
| bld_memory            | Historical SLA tracking       | P11    | Active  |
| bld_tools             | Automation utilities          | P11    | Active  |

## Dependencies
| From              | To                  | Type         |
|-------------------|---------------------|--------------|
| bld_manifest      | bld_schema          | Data         |
| bld_instruction   | bld_examples        | Reference    |
| bld_quality_gate  | bld_schema          | Validation   |
| bld_output_template | bld_schema       | Formatting   |
| bld_collaboration | bld_memory          | Historical   |
| bld_config        | external_policy_engine | Integration |

## Architectural Position
enterprise_sla serves as the central orchestrator for service-level agreement (SLA) construction within the CEX pillar P11, ensuring alignment between operational requirements, compliance frameworks, and stakeholder expectations through structured validation, dynamic configuration, and historical tracking mechanisms.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_compliance_checklist]] | sibling | 0.86 |
| [[bld_architecture_subscription_tier]] | sibling | 0.82 |
| [[bld_architecture_self_improvement_loop]] | sibling | 0.81 |
| [[bld_architecture_ab_test_config]] | sibling | 0.77 |
| [[bld_architecture_audit_log]] | sibling | 0.75 |
| [[bld_architecture_roi_calculator]] | sibling | 0.65 |
| [[bld_architecture_sales_playbook]] | sibling | 0.60 |
| [[bld_architecture_discovery_questions]] | sibling | 0.58 |
| [[bld_architecture_api_reference]] | sibling | 0.58 |
| [[bld_architecture_onboarding_flow]] | sibling | 0.57 |
