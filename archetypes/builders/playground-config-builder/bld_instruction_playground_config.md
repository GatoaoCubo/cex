---
kind: instruction
id: bld_instruction_playground_config
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for playground_config
quality: 8.8
title: "Instruction Playground Config"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [playground_config, builder, instruction]
tldr: "Step-by-step production process for playground_config"
domain: "playground_config construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Phase 1: RESEARCH  
1. Identify user intent and evaluation goals for the playground.  
2. Map technical constraints (e.g., resource limits, API versions).  
3. Analyze existing configs for compatibility and reuse.  
4. Document security policies (e.g., access controls, data isolation).  
5. Benchmark performance thresholds for interactive scenarios.  
6. Define success metrics for product evaluation.  

## Phase 2: COMPOSE  
1. Set up environment with SCHEMA.md as the structural blueprint.  
2. Define root parameters (e.g., `sandbox_id`, `evaluation_mode`).  
3. Structure config sections: `constraints`, `resources`, `security`.  
4. Populate `constraints` with P09-specific rules from research.  
5. Embed resource limits from Phase 1 benchmarks.  
6. Apply security policies from Phase 1 to `security` section.  
7. Validate against SCHEMA.md using a linter tool.  
8. Format output using OUTPUT_TEMPLATE.md syntax.  
9. Add metadata (e.g., `created_by`, `version`).  

## Phase 3: VALIDATE  
- [ ] ✅ Schema compliance check (SCHEMA.md).  
- [ ] ✅ Constraint enforcement test (mock scenarios).  
- [ ] ✅ Template syntax validation (OUTPUT_TEMPLATE.md).  
- [ ] ✅ Security policy audit (Phase 1 policies).  
- [ ] ✅ Performance benchmark alignment (Phase 1 metrics).
