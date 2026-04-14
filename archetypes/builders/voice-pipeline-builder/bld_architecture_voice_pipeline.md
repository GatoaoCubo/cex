---
kind: architecture
id: bld_architecture_voice_pipeline
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of voice_pipeline -- ISO inventory, dependencies, pillar position
quality: 9.1
title: "Architecture: voice-pipeline-builder"
version: "1.1.0"
author: n01_audit
tags: [voice_pipeline, builder, architecture, P08]
tldr: "Builder ISO inventory (13 components) and pillar position for voice_pipeline artifacts."
domain: "voice_pipeline construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
---

## Builder ISO Inventory (13 components)

| ISO File | Kind | llm_function | Role |
|----------|------|--------------|------|
| bld_manifest_voice_pipeline.md | type_builder | BECOME | Builder identity, capabilities, routing |
| bld_schema_voice_pipeline.md | schema | CONSTRAIN | ID pattern, required fields, body structure |
| bld_system_prompt_voice_pipeline.md | system_prompt | BECOME | Persona, ALWAYS/NEVER rules, output format |
| bld_instruction_voice_pipeline.md | instruction | REASON | Step-by-step production process |
| bld_knowledge_card_voice_pipeline.md | knowledge_card | INJECT | Domain knowledge: protocols, providers, latency |
| bld_quality_gate_voice_pipeline.md | quality_gate | GOVERN | H01-H08 HARD gates + SOFT scoring |
| bld_output_template_voice_pipeline.md | output_template | PRODUCE | Pipeline stages, data flow, fallback, latency table |
| bld_examples_voice_pipeline.md | examples | GOVERN | Golden (real providers) + anti-examples |
| bld_architecture_voice_pipeline.md | architecture | CONSTRAIN | This file: ISO inventory + dependencies |
| bld_collaboration_voice_pipeline.md | collaboration | COLLABORATE | Crew roles, receives-from, produces-for |
| bld_memory_voice_pipeline.md | memory | INJECT | Learned patterns, anti-patterns, impact data |
| bld_tools_voice_pipeline.md | tools | CALL | CEX tools + file system operations |
| bld_config_voice_pipeline.md | config | CONSTRAIN | Naming (p04_vp_*), paths, limits, hooks |

## Dependencies

| From | To | Relationship |
|------|----|--------------|
| system_prompt | schema | Applies ID pattern, kind, pillar constraints |
| quality_gate | schema | H02 checks ID pattern from schema |
| output_template | schema | Template frontmatter mirrors schema required fields |
| examples | output_template | Golden example follows output_template structure |
| instruction | schema + output_template | References both in Phase 2 COMPOSE |
| memory | knowledge_card | Complements domain knowledge with production experience |

## Architectural Position

`voice_pipeline` sits in pillar **P04** (Tools/Capabilities) as the architectural
specification for offline voice agent systems. It defines HOW the 5 stages (audio
preprocessing, STT, NLU, dialogue management, TTS) connect -- not provider-specific configs.

- **Above**: individual provider configs (`stt_provider`, `tts_provider`)
- **Adjacent to**: `realtime_session` (live LLM streaming), `vad_config`, `prosody_config`,
  `audio_tool` (signal processing)
- **Below**: agent orchestration (`agent_card`, `workflow`)
- **Distinct from**: `realtime_session` (live LLM bidirectional stream vs. offline pipeline)

Consumed by: deployment engineers instantiating STT/TTS providers for call centers,
smart home assistants, voice-enabled applications.

## Properties

| Property | Value |
|----------|-------|
| Kind | `architecture` |
| Pillar | P08 |
| Domain | voice_pipeline construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Properties

| Property | Value |
|----------|-------|
| Kind | `architecture` |
| Pillar | P08 |
| Domain | voice_pipeline construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
