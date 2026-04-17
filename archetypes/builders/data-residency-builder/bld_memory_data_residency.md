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
