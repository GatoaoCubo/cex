---
kind: instruction
id: bld_instruction_interactive_demo
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for interactive_demo
quality: 8.8
title: "Instruction Interactive Demo"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [interactive_demo, builder, instruction]
tldr: "Step-by-step production process for interactive_demo"
domain: "interactive_demo construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - interactive-demo-builder
  - bld_knowledge_card_interactive_demo
  - p03_sp_interactive_demo_builder
  - p10_mem_interactive_demo_builder
  - bld_collaboration_interactive_demo
  - bld_tools_interactive_demo
  - bld_output_template_interactive_demo
  - bld_instruction_course_module
  - kc_interactive_demo
  - bld_instruction_app_directory_entry
---

## Phase 1: RESEARCH  
1. Conduct user interviews to identify key demo interaction points  
2. Analyze competitor demos for common interaction patterns  
3. Define demo objectives and success metrics (e.g., conversion rates)  
4. Map user journey through product features with wireframes  
5. Evaluate technical constraints (e.g., API limits, load times)  
6. Gather feedback from stakeholders on demo scope  

## Phase 2: COMPOSE  
1. Outline demo structure using bld_schema_interactive_demo.md `demo_flow` format  
2. Write talk track for each guided-tour step (max 2 sentences)  
3. Embed interactive elements (buttons, sliders) with event handlers  
4. Align content with bld_output_template_interactive_demo.md `step_template` format  
5. Add branching logic for user-driven exploration paths  
6. Integrate product API endpoints for real-time data display  
7. Write error-handling scripts for failed interactions  
8. Add accessibility features (keyboard navigation, ARIA labels)  
9. Finalize with demo metadata (duration, target audience)  

## Phase 3: VALIDATE  
- [ ] Conduct usability testing with 5+ users  
- [ ] Verify alignment with bld_schema_interactive_demo.md required fields  
- [ ] Confirm interactive elements function across devices  
- [ ] Validate talk track matches scripted user scenarios  
- [ ] Ensure compliance with P05 accessibility standards


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[interactive-demo-builder]] | downstream | 0.40 |
| [[bld_knowledge_card_interactive_demo]] | upstream | 0.37 |
| [[p03_sp_interactive_demo_builder]] | related | 0.32 |
| [[p10_mem_interactive_demo_builder]] | downstream | 0.28 |
| [[bld_collaboration_interactive_demo]] | downstream | 0.27 |
| [[bld_tools_interactive_demo]] | downstream | 0.25 |
| [[bld_output_template_interactive_demo]] | downstream | 0.25 |
| [[bld_instruction_course_module]] | sibling | 0.24 |
| [[kc_interactive_demo]] | upstream | 0.24 |
| [[bld_instruction_app_directory_entry]] | sibling | 0.24 |
