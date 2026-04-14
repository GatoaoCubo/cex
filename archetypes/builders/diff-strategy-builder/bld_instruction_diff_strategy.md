---
kind: instruction
id: bld_instruction_diff_strategy
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for diff_strategy
quality: null
title: "Instruction Diff Strategy"
version: "1.0.0"
author: wave1_builder_gen
tags: [diff_strategy, builder, instruction]
tldr: "Step-by-step production process for diff_strategy"
domain: "diff_strategy construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Phase 1: RESEARCH  
1. Analyze existing diff strategies for application-specific use cases.  
2. Identify current limitations in matching algorithms (e.g., precision, scalability).  
3. Evaluate alternative algorithms (e.g., LCS, Myers, histogram-based).  
4. Benchmark performance against baseline metrics (time, memory, accuracy).  
5. Document application context (data size, update frequency, tolerance for false positives).  
6. Prioritize requirements: speed, accuracy, resource constraints.  

## Phase 2: COMPOSE  
1. Define artifact structure per SCHEMA.md (name, version, parameters).  
2. Specify input/output formats (e.g., JSON, binary diffs).  
3. Implement core diff logic using selected algorithm.  
4. Integrate with application via API or plugin interface.  
5. Parameterize thresholds (e.g., similarity score, chunk size).  
6. Write unit tests for edge cases (identical, conflicting, partial matches).  
7. Format documentation per OUTPUT_TEMPLATE.md (usage, examples).  
8. Review code for adherence to P04 standards (modularity, extensibility).  
9. Package artifact with metadata (author, dependencies, version history).  

## Phase 3: VALIDATE  
- [ ] ✅ Validate schema compliance with SCHEMA.md  
- [ ] ✅ Test algorithm accuracy against benchmark datasets  
- [ ] ✅ Confirm integration with target application  
- [ ] ✅ Verify performance under stress (large datasets, high concurrency)  
- [ ] ✅ Obtain peer approval for final artifact
