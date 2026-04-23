---
kind: instruction
id: bld_instruction_multimodal_prompt
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for multimodal_prompt
quality: 8.8
title: "Instruction Multimodal Prompt"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [multimodal_prompt, builder, instruction]
tldr: "Step-by-step production process for multimodal_prompt"
domain: "multimodal_prompt construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - p03_sp_multimodal_prompt_builder
  - multimodal-prompt-builder
  - bld_knowledge_card_multimodal_prompt
  - p10_mem_multimodal_prompt_builder
  - bld_instruction_multi_modal_config
  - bld_collaboration_multi_modal_config
  - p03_sp_multi_modal_config_builder
  - p03_qg_multimodal_prompt
  - p11_qg_multi_modal_config
  - multi-modal-config-builder
---

## Phase 1: RESEARCH  
1. Identify target modalities (vision/audio/text) and their interdependencies.  
2. Analyze domain-specific datasets for cross-modal correlations.  
3. Review existing multimodal benchmarks for pattern consistency.  
4. Map technical constraints (e.g., resolution limits, sampling rates).  
5. Document use cases requiring simultaneous modality injection.  
6. Evaluate prior prompt templates for adaptability.  

## Phase 2: COMPOSE  
1. Initialize schema with `modalities` array (ref: bld_schema_multimodal_prompt.md).  
2. Define `vision` parameters: resolution, object labels, spatial relations.  
3. Define `audio` parameters: duration, frequency ranges, semantic tags.  
4. Define `text` parameters: language, sentiment, entity references.  
5. Align modalities via `cross_ref` keys (e.g., `vision.id == audio.object_id`).  
6. Structure prompt using `INJECT` syntax (ref: bld_output_template_multimodal_prompt.md).  
7. Embed example triples: `<modality>:<value>:<context>`.  
8. Validate schema compliance with bld_schema_multimodal_prompt.md validation rules.  
9. Finalize with modality-specific placeholders for runtime injection.  

## Phase 3: VALIDATE  
[ ] All modalities present in `modalities` array  
[ ] Cross-modal references resolve consistently  
[ ] Technical constraints match dataset capabilities  
[ ] Example triples align with domain use cases  
[ ] Output conforms to bld_output_template_multimodal_prompt.md structure


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_multimodal_prompt_builder]] | related | 0.37 |
| [[multimodal-prompt-builder]] | related | 0.34 |
| [[bld_knowledge_card_multimodal_prompt]] | upstream | 0.33 |
| [[p10_mem_multimodal_prompt_builder]] | downstream | 0.32 |
| [[bld_instruction_multi_modal_config]] | sibling | 0.32 |
| [[bld_collaboration_multi_modal_config]] | downstream | 0.30 |
| [[p03_sp_multi_modal_config_builder]] | related | 0.28 |
| [[p03_qg_multimodal_prompt]] | downstream | 0.26 |
| [[p11_qg_multi_modal_config]] | downstream | 0.25 |
| [[multi-modal-config-builder]] | downstream | 0.25 |
