---
kind: architecture
id: bld_architecture_vad_config
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of vad_config -- inventory, dependencies
quality: 9.0
title: "Architecture Vad Config"
version: "1.0.0"
author: wave1_builder_gen
tags: [vad_config, builder, architecture]
tldr: "Component map of vad_config -- inventory, dependencies"
domain: "vad_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_architecture_tts_provider
  - bld_architecture_reasoning_strategy
  - bld_architecture_memory_architecture
  - bld_architecture_quantization_config
  - bld_architecture_dataset_card
  - bld_architecture_webinar_script
  - bld_architecture_realtime_session
  - bld_architecture_consolidation_policy
  - bld_architecture_procedural_memory
  - bld_architecture_contributor_guide
---

## Builder ISO Inventory (13 ISOs)

| ISO File | Kind | llm_function | Role |
|---|---|---|---|
| bld_manifest_vad_config.md | type_builder | BECOME | Identity, capabilities, routing |
| bld_system_prompt_vad_config.md | system_prompt | BECOME | Builder persona and rules |
| bld_instruction_vad_config.md | instruction | REASON | Step-by-step production process |
| bld_knowledge_card_vad_config.md | knowledge_card | INJECT | Domain knowledge (VAD engines, specs) |
| bld_schema_vad_config.md | schema | CONSTRAIN | Formal schema -- single source of truth |
| bld_quality_gate_vad_config.md | quality_gate | GOVERN | HARD/SOFT scoring gates |
| bld_output_template_vad_config.md | output_template | PRODUCE | Template with vars |
| bld_architecture_vad_config.md | architecture | CONSTRAIN | Component map (this file) |
| bld_examples_vad_config.md | examples | GOVERN | Golden + anti-examples |
| bld_collaboration_vad_config.md | collaboration | COLLABORATE | Crew integration |
| bld_config_vad_config.md | config | CONSTRAIN | Naming, paths, limits |
| bld_memory_vad_config.md | learning_record | INJECT | Learned patterns + pitfalls |
| bld_tools_vad_config.md | tools | CALL | Available production tools |

## Dependencies

| From | To | Type |
|------|----|------|
| bld_system_prompt | bld_manifest | Identity |
| bld_instruction | bld_schema | Validation |
| bld_output_template | bld_schema | Constraint |
| bld_quality_gate | bld_schema | Gate reference |
| bld_examples | bld_output_template | Validation |
| bld_collaboration | bld_manifest | Routing |

## Architectural Position  
vad_config resides in the audio preprocessing layer of the CEX ecosystem, defining detection thresholds and sensitivity settings that gate audio into downstream STT providers. It acts as the first filter in voice pipelines -- separating speech from silence/noise -- and interfaces with stt_provider_builder (downstream consumer) and voice_pipeline_builder (orchestrator) while enforcing P09 configuration standards.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_tts_provider]] | sibling | 0.61 |
| [[bld_architecture_reasoning_strategy]] | sibling | 0.43 |
| [[bld_architecture_memory_architecture]] | sibling | 0.41 |
| [[bld_architecture_quantization_config]] | sibling | 0.40 |
| [[bld_architecture_dataset_card]] | sibling | 0.40 |
| [[bld_architecture_webinar_script]] | sibling | 0.40 |
| [[bld_architecture_realtime_session]] | sibling | 0.39 |
| [[bld_architecture_consolidation_policy]] | sibling | 0.39 |
| [[bld_architecture_procedural_memory]] | sibling | 0.37 |
| [[bld_architecture_contributor_guide]] | sibling | 0.37 |
