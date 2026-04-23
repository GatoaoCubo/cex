---
kind: architecture
id: bld_architecture_quantization_config
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of quantization_config -- inventory, dependencies
quality: 9.0
title: "Architecture Quantization Config"
version: "1.0.0"
author: wave1_builder_gen
tags: [quantization_config, builder, architecture]
tldr: "Component map of quantization_config -- inventory, dependencies"
domain: "quantization_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_architecture_memory_architecture
  - bld_architecture_webinar_script
  - bld_architecture_vad_config
  - bld_architecture_tts_provider
  - bld_architecture_dataset_card
  - bld_architecture_reasoning_strategy
  - bld_architecture_consolidation_policy
  - bld_architecture_contributor_guide
  - bld_architecture_procedural_memory
  - bld_knowledge_card_kind
---

## Builder ISO Inventory (13 ISOs)

| ISO File | Kind | 8F Stage | Role |
| :--- | :--- | :--- | :--- |
| bld_manifest_quantization_config.md | type_builder | F2 BECOME | Builder identity, capabilities, routing |
| bld_instruction_quantization_config.md | instruction | F4 REASON | Step-by-step production phases |
| bld_system_prompt_quantization_config.md | system_prompt | F2 BECOME | Persona + scope rules for the builder agent |
| bld_schema_quantization_config.md | schema | F1 CONSTRAIN | Frontmatter field definitions (SSOT) |
| bld_quality_gate_quantization_config.md | quality_gate | F7 GOVERN | HARD + SOFT artifact validation |
| bld_tools_quantization_config.md | tools | F5 CALL | CEX tools available during production |
| bld_output_template_quantization_config.md | output_template | F6 PRODUCE | Field-guided YAML template |
| bld_examples_quantization_config.md | examples | F3 INJECT | Golden + anti-examples |
| bld_knowledge_card_quantization_config.md | knowledge_card | F3 INJECT | Domain knowledge (GPTQ, AWQ, GGUF, bitsandbytes) |
| bld_architecture_quantization_config.md | architecture | F1 CONSTRAIN | ISO inventory + dependency map (this file) |
| bld_collaboration_quantization_config.md | collaboration | F8 COLLABORATE | Upstream/downstream crew relationships |
| bld_config_quantization_config.md | config | F1 CONSTRAIN | Naming, paths, limits |
| bld_memory_quantization_config.md | memory | F3 INJECT | Learned pitfalls and patterns |

## Dependencies
| ISO | Depends On | Reason |
| :--- | :--- | :--- |
| bld_instruction | bld_schema, bld_output_template | Must reference current field names |
| bld_quality_gate | bld_schema, bld_config | ID pattern and required fields sourced here |
| bld_examples | bld_schema | Examples must follow schema field names |
| bld_output_template | bld_schema | Template placeholders must match schema |

## Pillar Placement
quantization_config lives in P09 (Config). Target artifacts are YAML config files consumed
by quantization frameworks (AutoGPTQ, AutoAWQ, bitsandbytes, llama.cpp).
Domain: ML model compression -- NOT data compression (ZIP/deflate).

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_memory_architecture]] | sibling | 0.41 |
| [[bld_architecture_webinar_script]] | sibling | 0.41 |
| [[bld_architecture_vad_config]] | sibling | 0.41 |
| [[bld_architecture_tts_provider]] | sibling | 0.40 |
| [[bld_architecture_dataset_card]] | sibling | 0.40 |
| [[bld_architecture_reasoning_strategy]] | sibling | 0.39 |
| [[bld_architecture_consolidation_policy]] | sibling | 0.38 |
| [[bld_architecture_contributor_guide]] | sibling | 0.36 |
| [[bld_architecture_procedural_memory]] | sibling | 0.36 |
| [[bld_knowledge_card_kind]] | upstream | 0.36 |
