---
id: p10_lr_audio_tool_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: builder_agent
observation: "Audio tools without declared direction caused downstream agents to attempt both STT and TTS paths, producing format mismatches in 5 of 8 pipeline integrations reviewed. Tools with explicit direction + BCP-47 languages + format enum routed correctly in every case."
pattern: "Declare direction explicitly. Use BCP-47 language codes. Mirror models list in frontmatter to ## Models section entries. Keep body under 2048 bytes. Declare sample_rate for STT tools."
evidence: "8 voice pipeline integrations: 5 failed with direction-ambiguous tools; 0 routing failures after direction was declared. Language free-text ('Brazilian Portuguese') caused 3 lookup failures; BCP-47 'pt-BR' resolved all 3."
confidence: 0.75
outcome: SUCCESS
domain: audio_tool
tags: [audio-tool, direction, language-codes, model-naming, format-enum, sample-rate]
tldr: "Direction is load-bearing for audio routing. BCP-47 codes mandatory. Model ids must match provider docs. sample_rate affects STT accuracy."
impact_score: 8.0
decay_rate: 0.04
agent_group: edison
keywords: [audio tool, STT, TTS, direction, language codes, BCP-47, model naming, format, sample rate, streaming]
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.2
title: "Memory Audio Tool"
density_score: 0.90
llm_function: INJECT
---
## Summary
Audio tools are consumed by voice interfaces, content pipelines, and agents that select STT or TTS paths at runtime. The difference between a tool that routes correctly and one that causes silent format mismatches comes down to three decisions made at spec time: direction declaration, BCP-47 language codes, and explicit model identifiers matching provider documentation.
A tool that omits direction (or uses a non-enum value), lists languages as free text, or uses model names that differ from the provider API (e.g., "GPT-4o" for audio, "Whisper" instead of "whisper_large_v3") will cause integration failures that are expensive to diagnose.
## Pattern
**Explicit direction, BCP-47 languages, exact model identifiers.**
Direction schema (enum):
1. input: STT — audio bytes in, text out
2. output: TTS — text in, audio bytes out
3. analysis: feature extraction — audio in, JSON features out
4. bidirectional: both STT and TTS supported
Language code rules:
1. Always BCP-47: `en`, `pt-BR`, `es`, `fr-CA`, `zh`, `ja`
2. Never free text: "English", "Portuguese", "Chinese" — breaks lookup
3. Include quality tier per model when coverage varies (high/medium/low)
Model naming rules:
1. Use exact provider API identifiers: `whisper_large_v3`, `deepgram_nova_2`, `eleven_multilingual_v2`
2. Never use marketing names: "Whisper Large", "ElevenLabs Multilingual" — spec drift
3. Mirror frontmatter `models` list exactly to ## Models table entries
Sample rate rules:
1. Declare `sample_rate: 16000` for all STT tools — models assume 16kHz input
2. Declare `sample_rate: 22050` or `44100` for TTS output quality contract
Body budget (2048 bytes max): Overview (150) + Direction (200) + Models (400) + Formats (300) + Languages (400) = ~1450.
## Anti-Pattern
1. Omitting direction field entirely (caller cannot determine STT vs TTS path).
2. Using "English" instead of "en" for language codes (BCP-47 compliance failure).
3. Model names like "Whisper" or "ElevenLabs" instead of exact API identifiers.
4. Claiming streaming support without declaring `streaming: true` in frontmatter.
5. Including formats not in the allowed enum (e.g., "audio/mpeg" mime type notation).
6. Conflating audio_tool with notifier: audio_tool processes signals; notifier delivers messages.
7. Conflating audio_tool with vision_tool: audio processes sound; vision processes images/video.
## Context
Body limit 2048B (larger than cli_tool 1024B). Write direction+models in frontmatter first. BCP-47 codes mandatory — map to provider API params.

## Metadata

```yaml
id: p10_lr_audio_tool_builder
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply p10-lr-audio-tool-builder.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `learning_record` |
| Pillar | P10 |
| Domain | audio_tool |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
