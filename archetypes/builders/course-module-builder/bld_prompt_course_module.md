---
kind: instruction
id: bld_instruction_course_module
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for course_module
quality: 8.8
title: "Instruction Course Module"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [course_module, builder, instruction]
tldr: "Step-by-step production process for course_module"
domain: "course_module construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_instruction_planning_strategy
  - course-module-builder
  - p03_sp_course_module_builder
  - p05_kc_course_module
  - bld_instruction_playground_config
  - bld_knowledge_card_course_module
  - bld_instruction_judge_config
  - bld_instruction_safety_policy
  - bld_instruction_benchmark_suite
  - bld_instruction_reward_model
---

## Phase 1: RESEARCH  
1. Identify target audience and learning outcomes for the module.  
2. Analyze existing course materials for gaps and redundancies.  
3. Research subject matter expertise and industry standards.  
4. Define assessment types (e.g., quizzes, projects) aligned with objectives.  
5. Gather feedback from stakeholders on module scope.  
6. Document required resources (e.g., videos, datasets).  

## Phase 2: COMPOSE  
1. Outline module structure using SCHEMA.md (title, objectives, content).  
2. Draft learning objectives using action verbs (e.g., "analyze," "design").  
3. Write instructional content with SCORM-compliant formatting.  
4. Align assessments with objectives (e.g., formative, summative).  
5. Use OUTPUT_TEMPLATE.md for consistent section headings and metadata.  
6. Embed interactive elements (e.g., drag-and-drop, branching scenarios).  
7. Ensure compliance with schema fields: `module_id`, `duration`, `prerequisites`.  
8. Add metadata tags for searchability (e.g., `topic`, `difficulty_level`).  
9. Proofread for clarity, grammar, and alignment with research phase outputs.  

## Phase 3: VALIDATE  
- [ ] ✅ Verify learning objectives match assessments and content.  
- [ ] ✅ Confirm SCHEMA.md fields are complete and accurate.  
- [ ] ✅ Test interactive elements for functionality and accessibility.  
- [ ] ✅ Validate against OUTPUT_TEMPLATE.md formatting rules.  
- [ ] ✅ Obtain stakeholder approval for final artifact.


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_planning_strategy]] | sibling | 0.30 |
| [[course-module-builder]] | downstream | 0.29 |
| [[p03_sp_course_module_builder]] | related | 0.28 |
| [[p05_kc_course_module]] | downstream | 0.27 |
| [[bld_instruction_playground_config]] | sibling | 0.27 |
| [[bld_knowledge_card_course_module]] | upstream | 0.26 |
| [[bld_instruction_judge_config]] | sibling | 0.26 |
| [[bld_instruction_safety_policy]] | sibling | 0.25 |
| [[bld_instruction_benchmark_suite]] | sibling | 0.24 |
| [[bld_instruction_reward_model]] | sibling | 0.24 |
