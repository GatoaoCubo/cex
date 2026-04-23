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
related:
  - p03_sp_content_filter_builder
  - bld_instruction_playground_config
  - bld_instruction_judge_config
  - content-filter-builder
  - bld_instruction_search_strategy
  - bld_instruction_eval_framework
  - bld_instruction_benchmark_suite
  - bld_instruction_reward_model
  - bld_collaboration_content_filter
  - bld_instruction_prompt_optimizer
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


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_content_filter_builder]] | related | 0.32 |
| [[bld_instruction_playground_config]] | sibling | 0.32 |
| [[bld_instruction_judge_config]] | sibling | 0.32 |
| [[content-filter-builder]] | downstream | 0.28 |
| [[bld_instruction_search_strategy]] | sibling | 0.27 |
| [[bld_instruction_eval_framework]] | sibling | 0.27 |
| [[bld_instruction_benchmark_suite]] | sibling | 0.26 |
| [[bld_instruction_reward_model]] | sibling | 0.26 |
| [[bld_collaboration_content_filter]] | downstream | 0.25 |
| [[bld_instruction_prompt_optimizer]] | sibling | 0.25 |
