---
kind: architecture
id: bld_architecture_healthcare_vertical
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of healthcare_vertical -- inventory, dependencies
quality: 9.0
title: "Architecture Healthcare Vertical"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [healthcare_vertical, builder, architecture]
tldr: "Component map of healthcare_vertical -- inventory, dependencies"
domain: "healthcare_vertical construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_architecture_legal_vertical
  - bld_architecture_fintech_vertical
  - bld_architecture_app_directory_entry
  - bld_architecture_roi_calculator
  - bld_architecture_benchmark_suite
  - bld_architecture_api_reference
  - bld_architecture_discovery_questions
  - bld_architecture_memory_benchmark
  - bld_architecture_sales_playbook
  - bld_architecture_github_issue_template
---

## Component Inventory
| ISO Name              | Role                                  | Pillar | Kind             | Status |
|-----------------------|---------------------------------------|--------|------------------|--------|
| bld_manifest          | Builder identity, capabilities        | P01    | type_builder     | Active |
| bld_instruction       | Step-by-step production process       | P03    | instruction      | Active |
| bld_system_prompt     | Agent persona and rules               | P03    | system_prompt    | Active |
| bld_schema            | Formal schema, naming, constraints    | P06    | schema           | Active |
| bld_quality_gate      | HARD+SOFT scoring gates               | P11    | quality_gate     | Active |
| bld_output_template   | Output structure with placeholders    | P05    | output_template  | Active |
| bld_examples          | Reference artifacts for in-context use| P01    | knowledge_card   | Active |
| bld_knowledge_card    | Domain knowledge for INJECT phase     | P01    | knowledge_card   | Active |
| bld_architecture      | Component map and dependencies        | P08    | architecture     | Active |
| bld_collaboration     | Cross-nucleus handoff patterns        | P12    | collaboration    | Active |
| bld_config            | Naming, paths, limits                 | P09    | config           | Active |
| bld_memory            | Learned patterns and pitfalls         | P10    | memory           | Active |
| bld_tools             | CEX tools + external references       | P04    | tools            | Active |

## Dependencies
| From            | To                  | Type       |
|-----------------|---------------------|------------|
| bld_config      | bld_schema          | Reference  |
| bld_system_prompt | bld_knowledge_card | Dependency |
| bld_quality_gate | bld_output_template | Validation |
| bld_instruction | bld_tools           | Execution  |
| bld_memory      | bld_config          | Configuration |

## Architectural Position
healthcare_vertical-builder operates as a specialized implementation layer within CEX P01, translating clinical requirements into compliant, interoperable systems using FHIR and HL7 standards. It ensures secure data handling, integrates with EHR workflows, and aligns with HIPAA and GDPR through embedded quality gates and knowledge cards, positioning it as a critical enabler for healthcare-specific AI deployment.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_legal_vertical]] | sibling | 0.82 |
| [[bld_architecture_fintech_vertical]] | sibling | 0.81 |
| [[bld_architecture_app_directory_entry]] | sibling | 0.71 |
| [[bld_architecture_roi_calculator]] | sibling | 0.71 |
| [[bld_architecture_benchmark_suite]] | sibling | 0.70 |
| [[bld_architecture_api_reference]] | sibling | 0.69 |
| [[bld_architecture_discovery_questions]] | sibling | 0.69 |
| [[bld_architecture_memory_benchmark]] | sibling | 0.68 |
| [[bld_architecture_sales_playbook]] | sibling | 0.67 |
| [[bld_architecture_github_issue_template]] | sibling | 0.67 |
