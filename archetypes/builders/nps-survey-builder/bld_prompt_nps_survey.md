---
kind: instruction
id: bld_instruction_nps_survey
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for nps_survey
quality: 8.9
title: "Instruction Nps Survey"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [nps_survey, builder, instruction]
tldr: "Step-by-step production process for nps_survey"
domain: "nps_survey construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - kc_nps_survey
  - bld_knowledge_card_nps_survey
  - p03_sp_nps_survey_builder
  - nps-survey-builder
  - bld_instruction_judge_config
  - bld_instruction_playground_config
  - p11_qg_nps_survey
  - bld_output_template_nps_survey
  - bld_examples_nps_survey
  - bld_instruction_llm_judge
---

## Phase 1: RESEARCH  
1. Define survey purpose: Align with P11 governance goals (e.g., customer loyalty, product feedback).  
2. Identify target audience: Segment by user type, tenure, or product usage.  
3. Draft core question: Use standard NPS phrasing (e.g., “How likely are you to recommend [product]?”).  
4. Select scale: Confirm 0–10 numerical scale with verbal anchors (e.g., 0=“Not at all likely,” 10=“Extremely likely”).  
5. Design follow-up: Create open-ended questions for promoters/detractors (e.g., “Why?”).  
6. Determine cadence: Set frequency (e.g., post-interaction, quarterly) and triggers (e.g., transactional events).  

## Phase 2: COMPOSE  
1. Reference SCHEMA.md: Define `survey_id`, `pillar`, `function`, and `version`.  
2. Write question text: Use concise, neutral language per OUTPUT_TEMPLATE.md.  
3. Configure scale: Map numerical values to verbal labels (e.g., 0–2=Detractors, 9–10=Promoters).  
4. Structure follow-up: Add conditional questions based on NPS score (e.g., “What could we improve?” for detractors).  
5. Segment respondents: Apply filters (e.g., `user_type=enterprise`, `region=APAC`).  
6. Set cadence rules: Define timing (e.g., `post_onboarding`, `30_days_after_sign_up`).  
7. Route responses: Link scores to workflows (e.g., `score<3 → support_ticket`, `score>8 → success_team`).  
8. Validate against OUTPUT_TEMPLATE.md: Ensure all fields (e.g., `question`, `scale`, `routing`) are present.  
9. Finalize artifact: Save as `nps_survey.yaml` with metadata (e.g., `created_by`, `last_modified`).  

## Phase 3: VALIDATE  
- [ ] ✅ Schema compliance: All required fields in SCHEMA.md are populated.  
- [ ] ✅ Flow logic: Follow-up questions trigger correctly based on NPS score.  
- [ ] ✅ Segmentation: Filters match target audience definitions (Phase 1, Step 2).  
- [ ] ✅ Routing: Response paths align with governance workflows (e.g., `score<3 → support`).  
- [ ] ✅ Cadence: Timing rules match research phase (Phase 1, Step 6).


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[kc_nps_survey]] | upstream | 0.35 |
| [[bld_knowledge_card_nps_survey]] | upstream | 0.33 |
| [[p03_sp_nps_survey_builder]] | related | 0.32 |
| [[nps-survey-builder]] | downstream | 0.31 |
| [[bld_instruction_judge_config]] | sibling | 0.24 |
| [[bld_instruction_playground_config]] | sibling | 0.24 |
| [[p11_qg_nps_survey]] | downstream | 0.23 |
| [[bld_output_template_nps_survey]] | downstream | 0.22 |
| [[bld_examples_nps_survey]] | downstream | 0.21 |
| [[bld_instruction_llm_judge]] | sibling | 0.21 |
