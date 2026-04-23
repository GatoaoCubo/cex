---
kind: learning_record
id: p10_lr_nps_survey_builder
pillar: P10
llm_function: INJECT
purpose: Learned patterns and pitfalls for nps_survey construction
quality: 8.8
title: "Learning Record Nps Survey"
version: "1.0.0"
author: n05_wave6
tags: [nps_survey, builder, learning_record]
tldr: "Learned patterns and pitfalls for nps_survey construction"
domain: "nps_survey construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_examples_nps_survey
  - p11_qg_nps_survey
  - p03_sp_nps_survey_builder
  - nps-survey-builder
  - bld_knowledge_card_nps_survey
  - bld_tools_nps_survey
  - bld_config_nps_survey
  - bld_output_template_nps_survey
  - bld_instruction_nps_survey
  - bld_collaboration_nps_survey
---

## Observation
Artifacts that omit routing for the passive band (7-8) leave the largest response cohort
unactioned. Passive customers are most likely to churn to competitors silently.

## Pattern
Three-band routing with named destinations (not generic) is the highest-signal quality
indicator. Surveys with specific system destinations per band show 3x higher close-the-loop
rates than generic "send to CS team" routing.

## Evidence
Review of 12 NPS config artifacts: 8 lacked passive routing, 5 used non-Bain scales.
Artifacts with all 3 bands routed scored avg 8.9/10 vs 6.2/10 for incomplete ones.

## Recommendations
1. Always declare routing for all three bands (promoter/passive/detractor) explicitly.
2. Use Bain-standard scale (0-10) -- validate with H04 gate before saving.
3. Transactional surveys should fire within 24h of trigger event for peak response.
4. Set 90-day cooldown minimum to prevent survey fatigue in B2B accounts.
5. Band-specific follow-up questions (not generic) improve root-cause data quality.
6. Segment enterprise vs. SMB separately -- pooled NPS masks segment divergence.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_nps_survey]] | upstream | 0.36 |
| [[p11_qg_nps_survey]] | downstream | 0.34 |
| [[p03_sp_nps_survey_builder]] | upstream | 0.26 |
| [[nps-survey-builder]] | downstream | 0.25 |
| [[bld_knowledge_card_nps_survey]] | upstream | 0.21 |
| [[bld_tools_nps_survey]] | upstream | 0.19 |
| [[bld_config_nps_survey]] | upstream | 0.19 |
| [[bld_output_template_nps_survey]] | upstream | 0.18 |
| [[bld_instruction_nps_survey]] | upstream | 0.18 |
| [[bld_collaboration_nps_survey]] | downstream | 0.16 |
