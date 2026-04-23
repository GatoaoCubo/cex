---
kind: architecture
id: bld_architecture_compliance_checklist
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of compliance_checklist -- inventory, dependencies
quality: 9.0
title: "Architecture Compliance Checklist"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [compliance_checklist, builder, architecture]
tldr: "Component map of compliance_checklist -- inventory, dependencies"
domain: "compliance_checklist construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_architecture_subscription_tier
  - bld_architecture_self_improvement_loop
  - bld_architecture_ab_test_config
  - bld_architecture_enterprise_sla
  - bld_architecture_audit_log
  - bld_architecture_roi_calculator
  - bld_architecture_sales_playbook
  - bld_architecture_discovery_questions
  - bld_architecture_api_reference
  - bld_architecture_quickstart_guide
---

## Component Inventory
| ISO Name              | Role                          | Pillar | Status |
|-----------------------|-------------------------------|--------|--------|
| bld_manifest          | Core structure definition     | P11    | Active |
| bld_instruction       | Compliance guidelines         | P11    | Active |
| bld_system_prompt     | User interaction framework    | P11    | Active |
| bld_schema            | Data format specification     | P11    | Active |
| bld_quality_gate      | Validation rules              | P11    | Active |
| bld_output_template   | Result formatting             | P11    | Active |
| bld_examples          | Sample compliance scenarios   | P11    | Active |
| bld_knowledge_card    | Regulatory reference          | P11    | Active |
| bld_architecture      | System blueprint              | P11    | Active |
| bld_collaboration     | Stakeholder alignment         | P11    | Active |
| bld_config            | Parameter management          | P11    | Active |
| bld_memory            | State retention              | P11    | Active |
| bld_tools             | Compliance enforcement        | P11    | Active |

## Dependencies
| From          | To              | Type       |
|---------------|-----------------|------------|
| bld_manifest  | bld_schema      | Structural |
| bld_instruction | bld_system_prompt | Functional |
| bld_quality_gate | bld_config   | Validation |
| bld_output_template | bld_examples | Data |
| bld_tools     | external_policy_engine | Integration |

## Architectural Position
The compliance_checklist-builder serves as the central orchestration layer within CEX Pillar P11, ensuring systematic alignment of all components with regulatory requirements. It integrates with P11-specific tools and external validation systems to enforce consistency, automate audits, and maintain traceability across the compliance lifecycle.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_subscription_tier]] | sibling | 0.84 |
| [[bld_architecture_self_improvement_loop]] | sibling | 0.83 |
| [[bld_architecture_ab_test_config]] | sibling | 0.80 |
| [[bld_architecture_enterprise_sla]] | sibling | 0.80 |
| [[bld_architecture_audit_log]] | sibling | 0.78 |
| [[bld_architecture_roi_calculator]] | sibling | 0.66 |
| [[bld_architecture_sales_playbook]] | sibling | 0.59 |
| [[bld_architecture_discovery_questions]] | sibling | 0.59 |
| [[bld_architecture_api_reference]] | sibling | 0.59 |
| [[bld_architecture_quickstart_guide]] | sibling | 0.57 |
