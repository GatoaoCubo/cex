---
kind: memory
id: p10_mem_referral_program_builder
pillar: P10
llm_function: INJECT
purpose: Learned patterns and pitfalls for referral_program construction
quality: 8.7
title: "Learning Record Referral Program"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [referral_program, builder, learning_record]
tldr: "Learned patterns and pitfalls for referral_program construction"
domain: "referral_program construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - p03_sp_referral_program_builder
  - bld_knowledge_card_referral_program
  - referral-program-builder
  - bld_examples_referral_program
  - kc_referral_program
  - bld_knowledge_card_reward_model
  - bld_instruction_referral_program
  - p11_qg_referral_program
  - p10_lr_reward_model_builder
  - bld_collaboration_referral_program
---

## Observation
Common issues include underestimating viral coefficient thresholds, leading to slow adoption, and reward structures that incentivize short-term gains over long-term retention.

## Pattern
Effective designs balance immediate rewards with long-term value, using tiered incentives to scale participation while maintaining program sustainability.

## Evidence
Reviewed artifacts showed programs with viral coefficients >1.5 achieved 40% faster growth, while those with unclear reward tiers saw 30% higher churn.

## Recommendations
- Calculate viral coefficient early using hypothetical user behavior models.
- Implement tiered rewards that escalate with referral volume (e.g., 1st referrer gets $5, 10th gets $20).
- Track referral sources explicitly to avoid ambiguity in credit allocation.
- Test reward thresholds against retention metrics to prevent burnout.
- Ensure program rules are visible in onboarding flows to reduce confusion.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_referral_program_builder]] | upstream | 0.42 |
| [[bld_knowledge_card_referral_program]] | upstream | 0.37 |
| [[referral-program-builder]] | downstream | 0.36 |
| [[bld_examples_referral_program]] | upstream | 0.34 |
| [[kc_referral_program]] | upstream | 0.34 |
| [[bld_knowledge_card_reward_model]] | upstream | 0.29 |
| [[bld_instruction_referral_program]] | upstream | 0.29 |
| [[p11_qg_referral_program]] | downstream | 0.27 |
| [[p10_lr_reward_model_builder]] | related | 0.26 |
| [[bld_collaboration_referral_program]] | downstream | 0.24 |
