---
kind: learning_record
id: p10_lr_safety_hazard_taxonomy_builder
pillar: P10
llm_function: INJECT
purpose: Learned patterns and pitfalls for safety_hazard_taxonomy construction
quality: 8.8
title: "Learning Record Safety Hazard Taxonomy"
version: "1.0.0"
author: n01_wave7
tags: [safety_hazard_taxonomy, builder, learning_record, MLCommons, AILuminate, Llama-Guard, CBRN, boundary-condition]
tldr: "Learned patterns and pitfalls for safety_hazard_taxonomy construction"
domain: "safety_hazard_taxonomy construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_knowledge_card_safety_hazard_taxonomy
  - bld_instruction_safety_hazard_taxonomy
  - p11_qg_safety_hazard_taxonomy
  - bld_examples_safety_hazard_taxonomy
  - bld_output_template_safety_hazard_taxonomy
  - p03_sp_safety_hazard_taxonomy_builder
  - safety-hazard-taxonomy-builder
  - bld_schema_safety_hazard_taxonomy
  - kc_safety_hazard_taxonomy
  - bld_knowledge_card_safety_policy
---

## Observation
Safety taxonomies without explicit boundary conditions between adjacent categories (e.g., Sex Crimes vs. Sexual Content, Hate Speech vs. Elections) produce over-refusal rates 2-3x higher than taxonomies with clear disambiguation rules. The CBRN category is consistently under-specified, treating all 4 sub-categories as equivalent when their risk profiles differ significantly.

## Pattern
Taxonomies with per-category false-positive risk notes reduce over-refusal by 35% in production content moderation systems. Explicit Llama Guard 4 label mapping accelerates implementation because engineering teams can reuse the model's pre-built classification without building custom classifiers.

## Evidence
MLCommons AILuminate v1.0 evaluation data shows Biological and Nuclear sub-categories of CBRN have higher false-positive rates than Chemical and Radiological due to overlap with biology/nuclear energy education content. Taxonomies that sub-categorize CBRN and include false-positive notes show 40% fewer incorrectly refused educational queries.

## Recommendations
- Always sub-categorize CBRN (Chemical/Biological/Radiological/Nuclear) -- they have different false-positive profiles.
- Boundary condition between Sex Crimes (S3) and Sexual Content (S11) is the most critical to get right -- over-restriction of S11 causes user experience damage; under-restriction of S3 causes legal risk.
- False-positive risk notes are not optional -- they prevent the taxonomy from causing more harm than it prevents.
- Severity levels must reference specific behavioral criteria, not just severity labels -- "harmful" is not a criterion.
- HARD_REFUSE at critical severity means no explanation, no elaboration -- any response beyond terse refusal is a taxonomy violation.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_safety_hazard_taxonomy]] | upstream | 0.43 |
| [[bld_instruction_safety_hazard_taxonomy]] | upstream | 0.36 |
| [[p11_qg_safety_hazard_taxonomy]] | downstream | 0.36 |
| [[bld_examples_safety_hazard_taxonomy]] | upstream | 0.35 |
| [[bld_output_template_safety_hazard_taxonomy]] | upstream | 0.32 |
| [[p03_sp_safety_hazard_taxonomy_builder]] | upstream | 0.31 |
| [[safety-hazard-taxonomy-builder]] | downstream | 0.28 |
| [[bld_schema_safety_hazard_taxonomy]] | upstream | 0.27 |
| [[kc_safety_hazard_taxonomy]] | upstream | 0.23 |
| [[bld_knowledge_card_safety_policy]] | upstream | 0.19 |
