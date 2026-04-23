---
kind: instruction
id: bld_instruction_referral_program
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for referral_program
quality: 8.9
title: "Instruction Referral Program"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [referral_program, builder, instruction]
tldr: "Step-by-step production process for referral_program"
domain: "referral_program construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - p03_sp_referral_program_builder
  - bld_examples_referral_program
  - referral-program-builder
  - bld_knowledge_card_referral_program
  - p11_qg_referral_program
  - p10_mem_referral_program_builder
  - bld_collaboration_referral_program
  - bld_output_template_referral_program
  - bld_schema_referral_program
  - bld_knowledge_card_reward_model
---

## Phase 1: RESEARCH  
1. Analyze target audience demographics and referral behavior patterns.  
2. Benchmark existing referral programs for viral coefficient benchmarks (e.g., 1.5–3.0).  
3. Calculate required reward thresholds to achieve desired user acquisition rates.  
4. Identify legal constraints (e.g., anti-spam laws, reward tax implications).  
5. Model user journey maps to identify high-impact referral touchpoints.  
6. Conduct A/B testing on incentive structures (e.g., cash vs. in-game items).  

## Phase 2: COMPOSE  
1. Define schema in SCHEMA.md: `referral_program { viral_coefficient: float, reward_structure: map }`.  
2. Map OUTPUT_TEMPLATE.md fields: `referral_code`, `user_id`, `reward_claimed`.  
3. Set viral_coefficient formula: `referrals_per_user * conversion_rate`.  
4. Design tiered rewards (e.g., 10% discount for 1st referral, 20% for 5+).  
5. Embed constraints: max 5 referrals per user, 30-day reward window.  
6. Code referral tracking logic with SQL triggers for real-time updates.  
7. Implement anti-fraud checks: IP throttling, referral code uniqueness.  
8. Write API endpoints for reward redemption and status checks.  
9. Document edge cases: expired codes, duplicate claims, reward caps.  

## Phase 3: VALIDATE  
- [ ] Verify viral_coefficient ≥ 1.2 using historical data simulations.  
- [ ] Confirm reward_structure aligns with SCHEMA.md constraints.  
- [ ] Test referral code generation uniqueness (0% collisions).  
- [ ] Validate legal compliance with GDPR/CCPA for user data.  
- [ ] Stress-test system with 100k concurrent referrals (≤2s latency).


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_referral_program_builder]] | related | 0.37 |
| [[bld_examples_referral_program]] | downstream | 0.36 |
| [[referral-program-builder]] | downstream | 0.36 |
| [[bld_knowledge_card_referral_program]] | upstream | 0.35 |
| [[p11_qg_referral_program]] | downstream | 0.33 |
| [[p10_mem_referral_program_builder]] | downstream | 0.28 |
| [[bld_collaboration_referral_program]] | downstream | 0.28 |
| [[bld_output_template_referral_program]] | downstream | 0.26 |
| [[bld_schema_referral_program]] | downstream | 0.26 |
| [[bld_knowledge_card_reward_model]] | upstream | 0.24 |
