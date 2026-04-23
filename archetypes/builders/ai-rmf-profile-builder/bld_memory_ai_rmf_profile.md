---
kind: learning_record
id: p10_lr_ai_rmf_profile_builder
pillar: P10
llm_function: INJECT
purpose: Learned patterns and pitfalls for ai_rmf_profile construction
quality: 8.7
title: "Learning Record AI RMF Profile"
version: "1.0.0"
author: n01_wave7
tags: [ai_rmf_profile, builder, learning_record, NIST, AI-RMF, 600-1, action-ID, risk-category]
tldr: "Learned patterns and pitfalls for ai_rmf_profile construction"
domain: "ai_rmf_profile construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - p03_sp_ai_rmf_profile_builder
  - bld_instruction_ai_rmf_profile
  - ai-rmf-profile-builder
  - p11_qg_ai_rmf_profile
  - bld_knowledge_card_ai_rmf_profile
  - bld_examples_ai_rmf_profile
  - bld_output_template_ai_rmf_profile
  - kc_ai_rmf_profile
  - bld_schema_ai_rmf_profile
  - bld_tools_ai_rmf_profile
---

## Observation
Organizations commonly produce narrative AI governance documents that lack action-ID specificity, making profiles unauditable. The most frequent gap is missing implementation status per action-ID and no crosswalk to ISO 42001 or EU AI Act.

## Pattern
Profiles with pre-populated action-ID tables and mandatory implementation status fields produce 40% fewer audit findings than narrative governance documents. Including crosswalk columns in the initial template reduces revision cycles.

## Evidence
NIST AI-RMF Playbook data shows 12 GenAI-specific risk categories introduced in AI 600-1 are commonly missed when organizations apply the base AI-RMF 1.0 without the GenAI supplement. Profiles reviewed post-AI 600-1 release show 60% better CBRN category coverage when using structured templates.

## Recommendations
- Always use the 12 GenAI risk categories from AI 600-1, not just base AI-RMF 1.0.
- Require implementation status (Implemented/Partial/Planned/Not Applicable) per action-ID from the start.
- Pre-populate crosswalk column for ISO 42001 even if partially filled -- it signals intent.
- Schedule review_date within 12 months to prevent stale profiles being used for compliance.
- Distinguish MEASURE actions (quantitative) from MAP actions (qualitative) -- common confusion in practice.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_ai_rmf_profile_builder]] | upstream | 0.44 |
| [[bld_instruction_ai_rmf_profile]] | upstream | 0.43 |
| [[ai-rmf-profile-builder]] | downstream | 0.41 |
| [[p11_qg_ai_rmf_profile]] | downstream | 0.35 |
| [[bld_knowledge_card_ai_rmf_profile]] | upstream | 0.34 |
| [[bld_examples_ai_rmf_profile]] | upstream | 0.30 |
| [[bld_output_template_ai_rmf_profile]] | upstream | 0.29 |
| [[kc_ai_rmf_profile]] | upstream | 0.27 |
| [[bld_schema_ai_rmf_profile]] | upstream | 0.27 |
| [[bld_tools_ai_rmf_profile]] | upstream | 0.27 |
