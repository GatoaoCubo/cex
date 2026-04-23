---
kind: memory
id: p10_mem_data_residency_builder
pillar: P10
llm_function: INJECT
purpose: Learned patterns and pitfalls for data_residency construction
quality: 8.7
title: "Memory Data Residency"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [data_residency, builder, memory]
tldr: "Learned patterns and pitfalls for data_residency construction"
domain: "data_residency construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_knowledge_card_data_residency
  - data-residency-builder
  - p09_kc_data_residency
  - p03_sp_data_residency_builder
  - bld_collaboration_data_residency
  - bld_instruction_data_residency
  - p09_qg_data_residency
  - bld_tools_data_residency
  - bld_output_template_data_residency
  - bld_schema_data_residency
---

## Observation
Common issues include ambiguous region boundaries, conflicting residency rules across systems, and incomplete mapping of data flows to regulatory zones. Overlooking hybrid cloud environments often leads to non-compliance gaps.

## Pattern
Successful configurations use standardized region codes (e.g., ISO 3166-1), enforce strict separation of residency rules from access policies, and validate data flow paths against compliance frameworks.

## Evidence
Reviewed artifacts showed EU regions using ISO codes with explicit data transfer clauses, while Asia-Pacific configurations included localized storage mandates.

## Recommendations
- Adopt ISO-standard region codes to avoid ambiguity.
- Modularize residency rules to isolate compliance logic from infrastructure configs.
- Automate validation of data flow paths against residency specs.
- Document exceptions for cross-border transfers with legal review markers.
- Periodically audit residency mappings against evolving regulatory updates.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_data_residency]] | upstream | 0.46 |
| [[data-residency-builder]] | upstream | 0.44 |
| [[p09_kc_data_residency]] | upstream | 0.40 |
| [[p03_sp_data_residency_builder]] | upstream | 0.38 |
| [[bld_collaboration_data_residency]] | downstream | 0.38 |
| [[bld_instruction_data_residency]] | upstream | 0.32 |
| [[p09_qg_data_residency]] | upstream | 0.27 |
| [[bld_tools_data_residency]] | upstream | 0.27 |
| [[bld_output_template_data_residency]] | upstream | 0.25 |
| [[bld_schema_data_residency]] | upstream | 0.24 |
