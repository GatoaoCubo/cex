---
kind: instruction
id: bld_instruction_ab_test_config
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for ab_test_config
quality: 8.9
title: "Instruction Ab Test Config"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [ab_test_config, builder, instruction]
tldr: "Step-by-step production process for ab_test_config"
domain: "ab_test_config construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Phase 1: RESEARCH  
1. Identify conversion goal (e.g., CTR, form submission rate).  
2. Analyze historical data for baseline metrics.  
3. Define success metrics and statistical significance thresholds.  
4. Determine test variables (e.g., button color, copy text).  
5. Assess technical feasibility (e.g., tracking, variant rendering).  
6. Secure stakeholder alignment on experiment scope.  

## Phase 2: COMPOSE  
1. Set config structure using SCHEMA.md (experiment ID, start/end dates).  
2. Define primary and secondary metrics (e.g., conversion rate, bounce rate).  
3. Specify variant groups (control, treatment A/B) with unique identifiers.  
4. Align variable changes with OUTPUT_TEMPLATE.md (e.g., HTML/CSS modifications).  
5. Assign traffic allocation percentages (e.g., 50% control, 25% each variant).  
6. Document hypothesis and expected impact (e.g., "Red button increases CTR by 15%").  
7. Add technical implementation notes (e.g., A/B script tags, cookie domains).  
8. Validate schema compliance (required fields: experiment_name, variant_weights).  
9. Finalize config with version control commit message (e.g., "AB-123: Launch checkout flow test").  

## Phase 3: VALIDATE  
- [ ] ✅ Schema fields (experiment_name, start_date) present and valid.  
- [ ] ✅ Variant weights sum to 100% with no negative values.  
- [ ] ✅ Metrics align with RESEARCH phase goals (e.g., form submissions).  
- [ ] ✅ Technical notes include tracking implementation details.  
- [ ] ✅ No conflicting variables in variant definitions (e.g., duplicate CSS classes).
