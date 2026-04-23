---
kind: collaboration
id: bld_collaboration_diff_strategy
pillar: P12
llm_function: COLLABORATE
purpose: How diff_strategy-builder works in crews with other builders
quality: 8.9
title: "Collaboration Diff Strategy"
version: "1.0.0"
author: wave1_builder_gen
tags: [diff_strategy, builder, collaboration]
tldr: "How diff_strategy-builder works in crews with other builders"
domain: "diff_strategy construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_collaboration_parser
  - parser-builder
  - bld_collaboration_dataset_card
  - bld_collaboration_search_strategy
  - bld_collaboration_self_improvement_loop
  - bld_collaboration_response_format
  - p01_kc_formatter
  - bld_architecture_parser
  - bld_collaboration_output_validator
  - bld_collaboration_action_paradigm
---

## Crew Role
Determines the optimal algorithmic approach for identifying
discrepancies between source and target states.

## Receives From
| Builder | What | Format |
| :--- | :--- | :--- |
| parser | Normalized Data | AST/JSON/Tree |
| analyzer | Structural Metadata | Metrics/Schema |
| policy-engine | Matching Constraints | Rule-set |

## Produces For
| Builder | What | Format |
| :--- | :--- | :--- |
| diff-executor | Matching Algorithm | Strategy Config |
| edit-formatter | Change Identification | Delta Map |
| validator | Comparison Criteria | Verification Logic |

## Boundary
Does not perform raw text parsing (handled by parser)
nor define the final output syntax or serialization
(handled by edit_format).

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_parser]] | sibling | 0.30 |
| [[parser-builder]] | upstream | 0.27 |
| [[bld_collaboration_dataset_card]] | sibling | 0.25 |
| [[bld_collaboration_search_strategy]] | sibling | 0.24 |
| [[bld_collaboration_self_improvement_loop]] | sibling | 0.24 |
| [[bld_collaboration_response_format]] | sibling | 0.23 |
| [[p01_kc_formatter]] | upstream | 0.23 |
| [[bld_architecture_parser]] | upstream | 0.23 |
| [[bld_collaboration_output_validator]] | sibling | 0.23 |
| [[bld_collaboration_action_paradigm]] | sibling | 0.23 |
