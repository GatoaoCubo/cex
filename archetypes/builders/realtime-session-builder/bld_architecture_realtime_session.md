---
kind: architecture
id: bld_architecture_realtime_session
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of realtime_session -- ISO inventory, dependencies, pillar position
quality: 9.1
title: "Architecture: realtime-session-builder"
version: "1.1.0"
author: n01_audit
tags: [realtime_session, builder, architecture, P08]
tldr: "Builder ISO inventory (13 components) and pillar position for realtime_session artifacts."
domain: "realtime_session construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
---

## Builder ISO Inventory (13 components)

| ISO File | Kind | llm_function | Role |
|----------|------|--------------|------|
| bld_manifest_realtime_session.md | type_builder | BECOME | Builder identity, capabilities, routing |
| bld_schema_realtime_session.md | schema | CONSTRAIN | ID pattern, required fields, body structure |
| bld_system_prompt_realtime_session.md | system_prompt | BECOME | Persona, ALWAYS/NEVER rules, output format |
| bld_instruction_realtime_session.md | instruction | REASON | Step-by-step production process |
| bld_knowledge_card_realtime_session.md | knowledge_card | INJECT | Domain knowledge: protocols, providers, events |
| bld_quality_gate_realtime_session.md | quality_gate | GOVERN | H01-H10 HARD gates + D1-D10 SOFT scoring |
| bld_output_template_realtime_session.md | output_template | PRODUCE | Session config JSON + ephemeral token + latency table |
| bld_examples_realtime_session.md | examples | GOVERN | Golden (OpenAI WebSocket) + anti-examples |
| bld_architecture_realtime_session.md | architecture | CONSTRAIN | This file: ISO inventory + dependencies |
| bld_collaboration_realtime_session.md | collaboration | COLLABORATE | Crew roles, receives-from, produces-for |
| bld_memory_realtime_session.md | memory | INJECT | Learned patterns, anti-patterns, impact data |
| bld_tools_realtime_session.md | tools | CALL | CEX tools + external APIs for production |
| bld_config_realtime_session.md | config | CONSTRAIN | Naming (p04_rs_*), paths, limits, hooks |

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

`realtime_session` sits in pillar **P04** (Tools/Capabilities) as the session config layer
for LLM bidirectional audio streaming. It is:

- **Above**: transport-layer configs (`transport_config`) and audio signal processors (`audio_tool`)
- **Adjacent to**: `voice_pipeline` (offline STT/NLU/TTS architecture), `stt_provider`,
  `tts_provider`, `vad_config`, `prosody_config`
- **Below**: agent orchestration (`agent_card`, `workflow`)
- **Distinct from**: `session_state` (runtime persistence) and `session_backend` (server infra)

Consumed by: frontend engineers integrating OpenAI Realtime API / Gemini Live, and
voice agent developers using LiveKit Agents, Daily, or Vapi.

## Properties

| Property | Value |
|----------|-------|
| Kind | `architecture` |
| Pillar | P08 |
| Domain | realtime_session construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
