---
kind: instruction
id: bld_instruction_roi_calculator
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for roi_calculator
quality: 8.9
title: "Instruction Roi Calculator"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [roi_calculator, builder, instruction]
tldr: "Step-by-step production process for roi_calculator"
domain: "roi_calculator construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Phase 1: RESEARCH  
1. Identify input parameters: initial investment, annual savings, implementation cost, maintenance fees, and time horizon.  
2. Research industry benchmarks for ROI thresholds and TCO components (hardware, software, labor).  
3. Define ROI formula: (Net Profit / Total Investment) × 100. Define TCO formula: Sum of all recurring and one-time costs.  
4. Collect case studies for economic buyer scenarios (e.g., enterprise SaaS, manufacturing automation).  
5. Map dependencies between variables (e.g., scaling effects on TCO).  
6. Validate data sources for accuracy (financial databases, vendor quotes).  

## Phase 2: COMPOSE  
1. Define schema in bld_schema_roi_calculator.md: specify input types, units, and constraints.  
2. Map inputs to ROI/TCO formulas using bld_output_template_roi_calculator.md structure.  
3. Write formula logic for dynamic calculations (e.g., compound annual growth rate).  
4. Build TCO comparison table with columns: cost category, baseline, alternative, delta.  
5. Populate template with placeholder values for user input fields.  
6. Add scenario examples (e.g., 3-year vs 5-year ROI).  
7. Format output for clarity: color-code positive/negative deltas, include charts.  
8. Peer-review formula logic against domain-specific benchmarks.  
9. Finalize artifact with version control and change log.  

## Phase 3: VALIDATE  
1. [ ] Verify formula accuracy with sample data (e.g., 10% ROI, $50k TCO).  
2. [ ] Test edge cases (zero investment, negative savings).  
3. [ ] Confirm TCO comparison aligns with input parameters.  
4. [ ] Ensure output template renders correctly across devices.  
5. [ ] Conduct user acceptance testing with economic buyers.
