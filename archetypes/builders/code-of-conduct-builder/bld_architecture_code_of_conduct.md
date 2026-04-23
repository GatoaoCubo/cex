---
kind: architecture
id: bld_architecture_code_of_conduct
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of code_of_conduct -- inventory, dependencies
quality: 9.0
title: "Architecture Code of Conduct"
version: "1.0.0"
author: n04_knowledge
tags: [code_of_conduct, builder, architecture]
tldr: "Component map of code_of_conduct -- inventory, dependencies"
domain: "code_of_conduct construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.87
related:
  - bld_architecture_app_directory_entry
  - bld_architecture_github_issue_template
  - bld_architecture_legal_vertical
  - bld_architecture_roi_calculator
  - bld_architecture_benchmark_suite
  - bld_architecture_api_reference
  - bld_architecture_fintech_vertical
  - bld_architecture_memory_benchmark
  - bld_architecture_healthcare_vertical
  - bld_architecture_ai_rmf_profile
---

## Component Inventory
| ISO Name            | Role                                          | Pillar | Status |
|---------------------|-----------------------------------------------|--------|--------|
| bld_manifest        | Builder identity, capabilities, routing       | P05    | Active |
| bld_instruction     | 3-phase production process (Research, Compose, Validate) | P03 | Active |
| bld_system_prompt   | LLM persona and ALWAYS/NEVER rules            | P03    | Active |
| bld_schema          | Frontmatter fields + body structure (SSOT)    | P06    | Active |
| bld_quality_gate    | HARD gates (H01-H08) + SOFT scoring (D01-D05) | P11    | Active |
| bld_output_template | Production template with var guidance         | P05    | Active |
| bld_examples        | Golden + anti-examples with failure analysis  | P07    | Active |
| bld_knowledge_card  | Domain knowledge: CoC standards + pitfalls    | P01    | Active |
| bld_architecture    | This document: ISO map + dependencies         | P08    | Active |
| bld_collaboration   | Cross-builder workflow coordination           | P12    | Active |
| bld_config          | Naming, paths, limits, hooks                  | P09    | Active |
| bld_memory          | Learned patterns and pitfalls (memory)          | P10  | Active |
| bld_tools           | Production + validation tools (CEX-native)    | P04    | Active |

## Dependencies
| From              | To                          | Type         |
|-------------------|-----------------------------|--------------|
| bld_manifest      | bld_config                  | configuration|
| bld_instruction   | bld_schema                  | reference    |
| bld_output_template | bld_schema                | dependency   |
| bld_quality_gate  | bld_schema                  | validation   |
| bld_quality_gate  | bld_examples                | reference    |
| bld_system_prompt | bld_instruction             | guides       |
| bld_memory        | bld_quality_gate            | improvement  |

## Architectural Position
code_of_conduct sits in P05 (PRODUCE) as a community governance artifact. It is the trust foundation for open-source contributor ecosystems, produced by this builder and consumed by repositories, maintainers, and community participants. It interacts with contributor_guide-builder (technical onboarding) and github_issue_template-builder (issue reporting workflow) as complementary OSS community doc builders.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_app_directory_entry]] | sibling | 0.78 |
| [[bld_architecture_github_issue_template]] | sibling | 0.77 |
| [[bld_architecture_legal_vertical]] | sibling | 0.72 |
| [[bld_architecture_roi_calculator]] | sibling | 0.71 |
| [[bld_architecture_benchmark_suite]] | sibling | 0.70 |
| [[bld_architecture_api_reference]] | sibling | 0.69 |
| [[bld_architecture_fintech_vertical]] | sibling | 0.68 |
| [[bld_architecture_memory_benchmark]] | sibling | 0.68 |
| [[bld_architecture_healthcare_vertical]] | sibling | 0.68 |
| [[bld_architecture_ai_rmf_profile]] | sibling | 0.68 |
