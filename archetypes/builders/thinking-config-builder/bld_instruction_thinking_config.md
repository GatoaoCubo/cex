---
kind: instruction
id: bld_instruction_thinking_config
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for thinking_config
quality: 9.0
title: "Instruction Thinking Config"
version: "1.0.0"
author: wave1_builder_gen
tags: [thinking_config, builder, instruction]
tldr: "Step-by-step production process for thinking_config"
domain: "thinking_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Phase 1: RESEARCH  

This ISO configures a thinking budget: how many tokens the model may spend on internal reasoning before emitting.
1. Analyze existing thinking_config templates for P09 constraints  
2. Identify token budget thresholds from historical performance data  
3. Map required parameters to schema constraints in SCHEMA.md  
4. Evaluate tradeoffs between token limits and processing speed  
5. Document edge cases for constrained thinking scenarios  
6. Cross-reference with P09 compliance checklists  

## Phase 2: COMPOSE  
1. Initialize config file with `kind: thinking_config` header  
2. Define `max_token_budget` using values from research phase  
3. Apply schema constraints from SCHEMA.md to parameter blocks  
4. Set `thinking_depth` to 3-5 based on performance benchmarks  
5. Embed token allocation rules in `budget_rules` section  
6. Write `constraint_triggers` using OUTPUT_TEMPLATE.md format  
7. Add version control metadata to config footer  
8. Validate parameter ranges against schema min/max values  
9. Finalize config with P09 compliance annotations  

## Phase 3: VALIDATE  
[ ] Check syntax against SCHEMA.md  
[ ] Verify at least 3 budget tiers defined with numeric thresholds  
[ ] Confirm fallback strategy documented for budget exhaustion  
[ ] Confirm timeout upper bound is set  
[ ] Verify boundary note distinguishes from reasoning_strategy and context_window_config  
[ ] Validate id matches pattern: p09_thk_[a-z0-9_]+  
[ ] Run H01-H08 quality gate checks before delivering  

## Properties

| Property | Value |
|----------|-------|
| Kind | `instruction` |
| Pillar | P03 |
| Domain | thinking_config construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
