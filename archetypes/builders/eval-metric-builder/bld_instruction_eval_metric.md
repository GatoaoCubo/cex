---
kind: instruction
id: bld_instruction_eval_metric
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for eval_metric
quality: 8.8
title: "Instruction Eval Metric"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [eval_metric, builder, instruction]
tldr: "Step-by-step production process for eval_metric"
domain: "eval_metric construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Phase 1: RESEARCH  
1. Identify domain-specific KPIs aligned with P07 governance goals.  
2. Analyze historical data to determine baseline metric thresholds.  
3. Define success criteria (e.g., accuracy, fairness, scalability).  
4. Survey stakeholders for metric prioritization and weighting.  
5. Review existing evaluation frameworks for compatibility.  
6. Document data sources and quality requirements.  

## Phase 2: COMPOSE  
1. Set up environment with SCHEMA.md dependencies.  
2. Name metric using `P07_<DOMAIN>_<MEASURE>` convention.  
3. Map metric to SCHEMA.md fields: `id`, `description`, `formula`.  
4. Write calculation logic in Python (reference OUTPUT_TEMPLATE.md).  
5. Implement edge case handling (e.g., null values, outliers).  
6. Embed metadata: governance owner, data lineage, version.  
7. Validate against OUTPUT_TEMPLATE.md structure.  
8. Add unit tests for formula and edge cases.  
9. Finalize artifact with governance approval.  

## Phase 3: VALIDATE  
- [ ] ✅ Schema compliance (SCHEMA.md)  
- [ ] ✅ Formula passes unit tests  
- [ ] ✅ Edge cases handled (nulls, outliers)  
- [ ] ✅ Metric aligns with P07 governance goals  
- [ ] ✅ Stakeholder approval for definition and weights
