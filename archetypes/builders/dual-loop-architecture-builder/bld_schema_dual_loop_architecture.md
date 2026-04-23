---
kind: schema
id: bld_schema_dual_loop_architecture
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for dual_loop_architecture
quality: 9.1
title: "Schema Dual Loop Architecture"
version: "1.0.0"
author: wave1_builder_gen
tags: [dual_loop_architecture, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for dual_loop_architecture"
domain: "dual_loop_architecture construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_schema_reranker_config
  - bld_schema_usage_report
  - bld_schema_sandbox_config
  - bld_schema_pitch_deck
  - bld_schema_benchmark_suite
  - bld_schema_dataset_card
  - bld_schema_customer_segment
  - bld_schema_agent_profile
  - bld_schema_multimodal_prompt
  - bld_schema_action_paradigm
---

## Frontmatter Fields

This ISO applies to the dual loop pattern, coordinating an outer orchestrator with one or more inner worker loops.
### Required
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string | yes | - | Unique identifier following ID pattern |
| kind | string | yes | "dual_loop_architecture" | CEX kind classification |
| pillar | string | yes | "P08" | Pillar reference |
| title | string | yes | - | Human-readable name |
| version | string | yes | "1.0" | Schema version |
| created | datetime | yes | - | ISO 8601 timestamp |
| updated | datetime | yes | - | ISO 8601 timestamp |
| author | string | yes | - | Responsible party |
| domain | string | yes | - | Application domain |
| quality | string | yes | "draft" | Quality assurance level |
| tags | array | yes | [] | Metadata keywords |
| tldr | string | yes | - | Summary paragraph |
| primary_loop | string | yes | - | Core processing loop |
| secondary_loop | string | yes | - | Supporting feedback loop |

### Recommended
| Field | Type | Notes |
|-------|------|-------|
| description | string | Detailed architecture explanation |
| references | array | External documentation links |
| status | string | Deployment stage (e.g., "production") |

## ID Pattern
^p08_dl_[a-zA-Z0-9_]+\.md$

## Body Structure
1. **Architecture Overview**
   High-level description of dual-loop interactions and purpose.

2. **Primary Loop Components**
   Detailed breakdown of core processing elements and their roles.

3. **Secondary Loop Components**
   Explanation of feedback mechanisms and supporting systems.

4. **Integration Points**
   Mapping of interfaces between primary and secondary loops.

5. **Validation Criteria**
   Metrics and tests ensuring loop synchronization and reliability.

## Constraints
- All required fields must be present and non-empty
- ID must match regex pattern exactly
- File size must not exceed 5120 bytes
- Sections must follow defined order
- Domain-specific fields must use valid technical terminology
- Tags must include at least one keyword from domain-specific vocabulary

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_reranker_config]] | sibling | 0.65 |
| [[bld_schema_usage_report]] | sibling | 0.65 |
| [[bld_schema_sandbox_config]] | sibling | 0.65 |
| [[bld_schema_pitch_deck]] | sibling | 0.64 |
| [[bld_schema_benchmark_suite]] | sibling | 0.64 |
| [[bld_schema_dataset_card]] | sibling | 0.64 |
| [[bld_schema_customer_segment]] | sibling | 0.62 |
| [[bld_schema_agent_profile]] | sibling | 0.62 |
| [[bld_schema_multimodal_prompt]] | sibling | 0.62 |
| [[bld_schema_action_paradigm]] | sibling | 0.61 |
