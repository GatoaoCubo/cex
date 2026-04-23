---
kind: architecture
id: bld_architecture_pricing_page
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of pricing_page -- inventory, dependencies
quality: 9.0
title: "Architecture Pricing Page"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [pricing_page, builder, architecture]
tldr: "Component map of pricing_page -- inventory, dependencies"
domain: "pricing_page construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_architecture_discovery_questions
  - bld_architecture_onboarding_flow
  - bld_architecture_api_reference
  - bld_architecture_sdk_example
  - bld_architecture_roi_calculator
  - bld_architecture_legal_vertical
  - bld_architecture_sales_playbook
  - bld_architecture_benchmark_suite
  - bld_architecture_quickstart_guide
  - bld_architecture_app_directory_entry
---

## Component Inventory
| ISO Name             | Role                                      | Pillar | Status |
|----------------------|-------------------------------------------|--------|--------|
| bld_manifest         | Defines pricing page structure and metadata | P05    | Active |
| bld_instruction      | Specifies pricing logic and rules         | P03    | Active |
| bld_system_prompt    | Guides AI in generating pricing content   | P03    | Active |
| bld_schema           | Enforces data format validation           | P06    | Active |
| bld_quality_gate     | Ensures content meets quality standards   | P11    | Active |
| bld_output_template  | Formats final pricing page output         | P05    | Active |
| bld_examples         | Provides sample pricing scenarios         | P07    | Active |
| bld_knowledge_card   | Stores pricing-related knowledge assets   | P01    | Active |
| bld_architecture     | Defines builder system architecture       | P08    | Active |
| bld_collaboration    | Manages team workflows and feedback       | P12    | Active |
| bld_config           | Centralizes pricing builder settings      | P09    | Active |
| bld_memory           | Tracks pricing page session data          | P10    | Active |
| bld_tools            | Integrates external pricing utilities     | P04    | Active |

## Dependencies
| From             | To               | Type       |
|------------------|------------------|------------|
| bld_manifest     | bld_config       | Configuration |
| bld_instruction  | bld_schema       | Validation  |
| bld_output_template | bld_examples | Data Source |
| bld_quality_gate | bld_memory       | State Dependency |
| bld_tools        | cex_compile.py   | CEX Tool |

## Architectural Position
The pricing_page serves as the user-facing interface within the CEX P05 ecosystem, enabling dynamic generation of subscription-based pricing models. It integrates with configuration, memory, and validation components to ensure consistent, high-quality pricing content while leveraging external tools for analytics and compliance checks.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_discovery_questions]] | sibling | 0.64 |
| [[bld_architecture_onboarding_flow]] | sibling | 0.64 |
| [[bld_architecture_api_reference]] | sibling | 0.63 |
| [[bld_architecture_sdk_example]] | sibling | 0.63 |
| [[bld_architecture_roi_calculator]] | sibling | 0.62 |
| [[bld_architecture_legal_vertical]] | sibling | 0.61 |
| [[bld_architecture_sales_playbook]] | sibling | 0.61 |
| [[bld_architecture_benchmark_suite]] | sibling | 0.60 |
| [[bld_architecture_quickstart_guide]] | sibling | 0.60 |
| [[bld_architecture_app_directory_entry]] | sibling | 0.60 |
