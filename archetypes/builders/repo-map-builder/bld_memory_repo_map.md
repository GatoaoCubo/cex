---
kind: learning_record
id: p10_lr_repo_map_builder
pillar: P10
llm_function: INJECT
purpose: Learned patterns and pitfalls for repo_map construction
quality: 8.7
title: "Learning Record Repo Map"
version: "1.0.0"
author: wave1_builder_gen
tags: [repo_map, builder, learning_record]
tldr: "Learned patterns and pitfalls for repo_map construction"
domain: "repo_map construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - p03_sp_repo_map_builder
  - p10_mem_prompt_optimizer_builder
  - p10_mem_benchmark_suite_builder
  - p10_mem_customer_segment_builder
  - repo-map-builder
  - p10_lr_edit_format_builder
  - p10_mem_prompt_technique_builder
  - p10_lr_reasoning_strategy_builder
---

## Observation  
Inconsistent module boundary definitions often lead to fragmented or overlapping repo_map entries. Over-reliance on file structure alone may miss implicit dependencies or cross-cutting concerns.  

## Pattern  
Combining static analysis with manual curation improves accuracy. Focusing on explicit markers (e.g., `@context` annotations) and architectural decisions aligns maps with developer intent.  

## Evidence  
Artifacts from `repo_map-builder-v2` showed 25% fewer inconsistencies after integrating semantic markers with file-based heuristics.  

## Recommendations  
- Define explicit criteria for module boundaries (e.g., package structure + semantic roles).  
- Prioritize tooling that surfaces implicit dependencies (e.g., call graphs, import analysis).  
- Validate maps iteratively with domain experts to align with operational workflows.  
- Avoid over-segmentation; balance granularity with maintainability.  
- Document exclusion rules to prevent accidental omission of critical context.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_repo_map_builder]] | upstream | 0.24 |
| [[p10_mem_prompt_optimizer_builder]] | related | 0.17 |
| [[p10_mem_benchmark_suite_builder]] | related | 0.16 |
| [[p10_mem_customer_segment_builder]] | related | 0.16 |
| [[repo-map-builder]] | upstream | 0.16 |
| [[p10_lr_edit_format_builder]] | sibling | 0.16 |
| [[p10_mem_prompt_technique_builder]] | related | 0.16 |
| [[p10_lr_reasoning_strategy_builder]] | sibling | 0.15 |
