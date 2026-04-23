---
kind: instruction
id: bld_instruction_onboarding_flow
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for onboarding_flow
quality: 8.9
title: "Instruction Onboarding Flow"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [onboarding_flow, builder, instruction]
tldr: "Step-by-step production process for onboarding_flow"
domain: "onboarding_flow construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - p03_sp_onboarding_flow_builder
  - onboarding-flow-builder
  - kc_onboarding_flow
  - p10_mem_onboarding_flow_builder
  - bld_knowledge_card_onboarding_flow
  - bld_instruction_user_journey
  - bld_collaboration_onboarding_flow
  - bld_instruction_benchmark_suite
  - p05_qg_onboarding_flow
  - bld_instruction_playground_config
---

## Phase 1: RESEARCH  
1. Conduct user interviews to identify pain points during onboarding.  
2. Map current onboarding journey, noting drop-off points and friction.  
3. Define activation milestones (e.g., profile setup, first task completion).  
4. Identify aha-moments by analyzing user behavior post-onboarding.  
5. Benchmark competitors’ onboarding flows for best practices.  
6. Synthesize insights into a user persona and journey map.  

## Phase 2: COMPOSE  
1. Define flow structure using SCHEMA.md (e.g., steps, triggers, success metrics).  
2. Align activation milestones with product goals in OUTPUT_TEMPLATE.md.  
3. Design aha-moments with micro-interactions and clear value propositions.  
4. Write copy for each step, emphasizing clarity and user empowerment.  
5. Integrate conditional logic for personalized onboarding paths.  
6. Embed progress indicators (e.g., percentage complete, milestone badges).  
7. Validate against SCHEMA.md for consistency in data flow and UI elements.  
8. Use OUTPUT_TEMPLATE.md to format artifacts for engineering and design.  
9. Add analytics hooks for tracking milestone completion and drop-offs.  

## Phase 3: VALIDATE  
- [ ] Conduct usability testing with 10+ users to identify friction points.  
- [ ] Verify all activation milestones are achievable within 30 days.  
- [ ] Confirm aha-moments trigger measurable engagement (e.g., 20% increase in task completion).  
- [ ] Ensure artifact complies with SCHEMA.md and OUTPUT_TEMPLATE.md standards.  
- [ ] Obtain stakeholder approval for final flow and success metrics.


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_onboarding_flow_builder]] | related | 0.41 |
| [[onboarding-flow-builder]] | downstream | 0.39 |
| [[kc_onboarding_flow]] | upstream | 0.39 |
| [[p10_mem_onboarding_flow_builder]] | downstream | 0.35 |
| [[bld_knowledge_card_onboarding_flow]] | upstream | 0.35 |
| [[bld_instruction_user_journey]] | sibling | 0.28 |
| [[bld_collaboration_onboarding_flow]] | downstream | 0.28 |
| [[bld_instruction_benchmark_suite]] | sibling | 0.24 |
| [[p05_qg_onboarding_flow]] | downstream | 0.24 |
| [[bld_instruction_playground_config]] | sibling | 0.22 |
