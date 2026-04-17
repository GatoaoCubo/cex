---
kind: instruction
id: bld_instruction_bias_audit
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for bias_audit
quality: 8.9
title: "Instruction Bias Audit"
version: "1.0.0"
author: wave1_builder_gen
tags: [bias_audit, builder, instruction]
tldr: "Step-by-step production process for bias_audit"
domain: "bias_audit construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Phase 1: RESEARCH  

This ISO drives a bias audit: measuring fairness across demographic slices.
1. Define audit scope: identify systems, datasets, and decision points under evaluation.  
2. Collect training/validation data and model outputs for analysis.  
3. Identify sensitive attributes (e.g., race, gender) and protected groups.  
4. Select fairness metrics (e.g., demographic parity, equalized odds).  
5. Conduct statistical analysis to detect disparities in model outcomes.  
6. Document methodology, assumptions, and limitations of the audit.  

## Phase 2: COMPOSE  
1. Outline artifact structure using SCHEMA.md (sections: methodology, metrics, results).  
2. Write audit objectives and scope based on research findings.  
3. Describe data sources, preprocessing steps, and model versions analyzed.  
4. Define fairness metrics and thresholds from SCHEMA.md.  
5. Populate results tables with quantitative fairness evaluations.  
6. Insert visualizations (e.g., disparity heatmaps) from OUTPUT_TEMPLATE.md.  
7. Discuss implications of findings, including trade-offs between fairness and performance.  
8. Reference audit tools, libraries, and validation procedures used.  
9. Finalize artifact using OUTPUT_TEMPLATE.md formatting guidelines.  

## Phase 3: VALIDATE  
1. [ ] Verify all SCHEMA.md requirements are addressed.  
2. [ ] Confirm data accuracy and alignment with research phase.  
3. [ ] Ensure metrics match definitions in Phase 1 and SCHEMA.md.  
4. [ ] Check compliance with OUTPUT_TEMPLATE.md structure.  
5. [ ] Obtain peer review for methodological rigor and clarity.
