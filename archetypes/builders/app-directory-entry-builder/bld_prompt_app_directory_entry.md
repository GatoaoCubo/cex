---
kind: instruction
id: bld_instruction_app_directory_entry
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for app_directory_entry
quality: 8.8
title: "Instruction App Directory Entry"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [app_directory_entry, builder, instruction]
tldr: "Step-by-step production process for app_directory_entry"
domain: "app_directory_entry construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - kc_app_directory_entry
  - p05_qg_app_directory_entry
  - app-directory-entry-builder
  - bld_knowledge_card_app_directory_entry
  - p10_mem_app_directory_entry_builder
  - p03_sp_app_directory_entry_builder
  - bld_instruction_interactive_demo
  - bld_instruction_kind
  - bld_instruction_output_validator
  - p04_skill_verify
---

## Phase 1: RESEARCH  
1. Identify app’s core value proposition and target audience.  
2. Analyze competitors’ directory entries for tagline structure.  
3. Collect 3–5 high-res screenshots (UI/UX flow, key features).  
4. Document install steps (platform-specific, 2–4 concise bullet points).  
5. Verify demo link accessibility and compliance with free-tier terms.  
6. Confirm legal requirements (privacy policy, licensing).  

## Phase 2: COMPOSE  
1. Use SCHEMA.md to define metadata fields (name, category, tags).  
2. Write tagline (max 25 chars, action-oriented, no jargon).  
3. Insert screenshots in ORDER: splash screen, feature highlight, UI demo.  
4. Format install steps as numbered list (e.g., “Download from App Store”).  
5. Embed demo link (HTTPS, no external redirects).  
6. Add metadata: version, OS compatibility, app size.  
7. Apply OUTPUT_TEMPLATE.md structure (header, body, footer sections).  
8. Replace placeholders with validated content.  
9. Proofread for typos, schema alignment, and free-tier eligibility.  

## Phase 3: VALIDATE  
[ ] ✅ Check schema compliance (all required fields present).  
[ ] ✅ Verify screenshot resolution (≥1024x768px, no watermarks).  
[ ] ✅ Confirm install steps match app’s actual workflow.  
[ ] ✅ Test demo link (loads in browser, no 404 errors).  
[ ] ✅ Ensure tagline adheres to 25-char limit and tone guidelines.


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[kc_app_directory_entry]] | upstream | 0.39 |
| [[p05_qg_app_directory_entry]] | downstream | 0.39 |
| [[app-directory-entry-builder]] | downstream | 0.34 |
| [[bld_knowledge_card_app_directory_entry]] | upstream | 0.31 |
| [[p10_mem_app_directory_entry_builder]] | downstream | 0.30 |
| [[p03_sp_app_directory_entry_builder]] | related | 0.25 |
| [[bld_instruction_interactive_demo]] | sibling | 0.23 |
| [[bld_instruction_kind]] | sibling | 0.22 |
| [[bld_instruction_output_validator]] | sibling | 0.22 |
| [[p04_skill_verify]] | downstream | 0.22 |
