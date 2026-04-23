---
kind: collaboration
id: bld_collaboration_safety_hazard_taxonomy
pillar: P12
llm_function: COLLABORATE
purpose: How safety_hazard_taxonomy-builder works in crews with other builders
quality: 9.0
title: "Collaboration Safety Hazard Taxonomy"
version: "1.0.0"
author: n01_wave7
tags: [safety_hazard_taxonomy, builder, collaboration, MLCommons, AILuminate, Llama-Guard, hazard-category]
tldr: "How safety_hazard_taxonomy-builder works in crews with other builders"
domain: "safety_hazard_taxonomy construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - safety-hazard-taxonomy-builder
  - bld_collaboration_ai_rmf_profile
  - p03_sp_safety_hazard_taxonomy_builder
  - bld_collaboration_llm_evaluation_scenario
  - bld_architecture_kind
  - bld_collaboration_gpai_technical_doc
  - bld_collaboration_code_of_conduct
  - bld_instruction_safety_hazard_taxonomy
  - bld_collaboration_agent_computer_interface
  - bld_collaboration_builder
---

## Crew Role
Produces formal safety hazard taxonomy artifacts aligned to MLCommons AILuminate v1.0 and Llama Guard 4, providing the classification foundation layer for downstream safety systems.

## Receives From
| Builder | What | Format |
|---------|------|--------|
| N01 Intelligence | MLCommons AILuminate research and Llama Guard 4 updates | Knowledge Card |
| content_filter-builder | Existing filter categories for alignment verification | Markdown |
| compliance_framework-builder | Legal requirements per jurisdiction for regulatory mapping | Markdown |
| red_team_eval-builder | Known attack patterns per hazard category for boundary refinement | Markdown |

## Produces For
| Builder | What | Format |
|---------|------|--------|
| content_filter-builder | Hazard categories and severity thresholds for filter config | Markdown |
| guardrail-builder | Hazard classification for enforcement boundary rules | Markdown |
| eval_dataset-builder | Hazard category definitions for test prompt labeling | Markdown |
| red_team_eval-builder | Formal taxonomy as target classification for red team ops | Markdown |
| scoring_rubric-builder | Severity levels for safety evaluation rubrics | Markdown |

## Boundary
Does NOT produce runtime filtering configurations (use content_filter-builder), enforcement rules (use guardrail-builder), test datasets (use eval_dataset-builder), or safety benchmark scores (use benchmark-builder). This builder provides DEFINITIONS -- enforcement is always downstream. Red team operations and safety evaluation are managed by AI safety teams.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[safety-hazard-taxonomy-builder]] | upstream | 0.45 |
| [[bld_collaboration_ai_rmf_profile]] | sibling | 0.42 |
| [[p03_sp_safety_hazard_taxonomy_builder]] | upstream | 0.42 |
| [[bld_collaboration_llm_evaluation_scenario]] | sibling | 0.38 |
| [[bld_architecture_kind]] | upstream | 0.33 |
| [[bld_collaboration_gpai_technical_doc]] | sibling | 0.33 |
| [[bld_collaboration_code_of_conduct]] | sibling | 0.30 |
| [[bld_instruction_safety_hazard_taxonomy]] | upstream | 0.29 |
| [[bld_collaboration_agent_computer_interface]] | sibling | 0.29 |
| [[bld_collaboration_builder]] | sibling | 0.29 |
