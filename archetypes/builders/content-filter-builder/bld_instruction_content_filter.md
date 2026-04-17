---
kind: instruction
id: bld_instruction_content_filter
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for content_filter
quality: 8.9
title: "Instruction Content Filter"
version: "1.0.0"
author: wave1_builder_gen
tags: [content_filter, builder, instruction]
tldr: "Step-by-step production process for content_filter"
domain: "content_filter construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Phase 1: RESEARCH  

This ISO defines a content filter -- the moderation rules that gate output or input.
1. Analyze input/output data formats (e.g., JSON, XML, text) for content_filter.  
2. Identify governance policies (e.g., censorship rules, NSFW thresholds).  
3. Evaluate existing filtering tools (e.g., regex, NLP models, keyword lists).  
4. Map content lifecycle stages (ingestion → filtering → output).  
5. Benchmark performance metrics (latency, accuracy, throughput).  
6. Document edge cases (e.g., multilingual content, obfuscation techniques).  

## Phase 2: COMPOSE  
1. Define schema in SCHEMA.md (fields: `filter_id`, `policy`, `rules`, `priority`).  
2. Write rule sets using regex/NLP patterns per OUTPUT_TEMPLATE.md.  
3. Assign governance policies to filter stages (e.g., pre-processing, post-processing).  
4. Configure pipeline components (e.g., parser, sanitizer, classifier).  
5. Implement rule validation logic (e.g., syntax checks, policy conflicts).  
6. Integrate logging/metrics for filter performance tracking.  
7. Test with sample data from Phase 1 research.  
8. Refine rules based on test outcomes.  
9. Finalize artifact with version control and metadata.  

## Phase 3: VALIDATE  
- [ ] ✅ Schema compliance checked against SCHEMA.md  
- [ ] ✅ Rule sets pass syntax and policy consistency checks  
- [ ] ✅ Output matches OUTPUT_TEMPLATE.md structure  
- [ ] ✅ Pipeline handles edge cases from Phase 1  
- [ ] ✅ Governance policies align with domain requirements
