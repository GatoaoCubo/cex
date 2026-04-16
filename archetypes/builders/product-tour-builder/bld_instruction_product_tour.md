---
kind: instruction
id: bld_instruction_product_tour
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for product_tour
quality: 8.9
title: "Instruction Product Tour"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [product_tour, builder, instruction]
tldr: "Step-by-step production process for product_tour"
domain: "product_tour construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Phase 1: RESEARCH  
1. Conduct user interviews to identify pain points and feature discovery gaps.  
2. Analyze competitor product tours for common patterns and usability benchmarks.  
3. Map the product’s core workflow to determine optimal tour sequence and context.  
4. Define trigger events (e.g., onboarding, feature first use) for tour activation.  
5. Document technical constraints (e.g., supported frameworks, analytics integration).  
6. Prioritize features for inclusion based on impact and user engagement potential.  

## Phase 2: COMPOSE  
1. Reference bld_schema_product_tour.md to structure tour metadata (id, name, version).  
2. Define step order using `step_id`, `title`, `content`, and `target_element` fields.  
3. Write tooltip content with concise, action-oriented language (max 2 sentences).  
4. Assign trigger conditions (e.g., `user_first_time: true`, `feature_flag: enabled`).  
5. Specify visual styles (color, icon) per step in `style` block (see bld_output_template_product_tour.md).  
6. Align tour with brand guidelines (tone, terminology, visual hierarchy).  
7. Use bld_output_template_product_tour.md to populate `tour.yaml` with structured data.  
8. Add analytics events for each step (e.g., `step_viewed`, `tooltip_closed`).  
9. Validate YAML syntax and schema compliance with linter tools.  

## Phase 3: VALIDATE  
- [ ] All steps match bld_schema_product_tour.md requirements (required fields, data types).
- [ ] Tooltip content aligns with user research and avoids jargon.
- [ ] Triggers fire correctly in simulated environments (no false positives).
- [ ] Visual design matches brand guidelines and is accessible (contrast, fonts).
- [ ] End-to-end tour flows complete without errors in production preview.
