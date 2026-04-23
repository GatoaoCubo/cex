---
kind: instruction
id: bld_instruction_audio_tool
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for audio_tool
pattern: 3-phase pipeline (research -> compose -> validate)
quality: 9.2
title: "Instruction Audio Tool"
version: "1.0.0"
author: n03_builder
tags: [audio_tool, builder, examples]
tldr: "Golden and anti-examples for audio tool construction, demonstrating ideal structure and common pitfalls."
domain: "audio tool construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p03_sp_audio_tool_builder
  - p10_lr_audio_tool_builder
  - p11_qg_audio_tool
  - bld_instruction_output_validator
  - bld_knowledge_card_audio_tool
  - bld_instruction_retriever_config
  - audio-tool-builder
  - bld_schema_audio_tool
  - bld_instruction_memory_scope
  - bld_instruction_chunk_strategy
---

# Instructions: How to Produce an audio_tool
## Phase 1: RESEARCH
1. Identify the audio processing direction: input (STT), output (TTS), analysis, or bidirectional
2. Select models matching the direction — Whisper/Deepgram/AssemblyAI for STT; ElevenLabs/Google/Azure for TTS
3. List all supported audio formats per direction (input accepts which formats; output produces which formats)
4. Define languages with BCP-47 codes and note quality tier per model (high/medium/low)
5. Determine sample_rate (16000 Hz standard for STT, 22050/44100 for TTS), max_duration, streaming support
6. Check if word_timestamps are needed (STT diarization use cases)
7. Check for existing audio_tool artifacts to avoid duplicates
8. Confirm capability slug for id: snake_case, lowercase, no hyphens
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill `{{vars}}` following SCHEMA constraints
3. Fill frontmatter: all required fields (quality: null — never self-score)
4. Write Overview section: what the tool does, who uses it, primary direction
5. Write Direction section: processing flow — audio bytes in / text out for STT; text in / audio bytes out for TTS
6. Write Models section: table with model id, provider, accuracy tier, latency class, cost tier
7. Write Formats section: compatibility matrix — which formats are accepted (input) vs produced (output)
8. Write Languages section: BCP-47 codes with quality tier per model
9. Verify body <= 2048 bytes
10. Verify id matches `^p04_audio_[a-z][a-z0-9_]+$`
## Phase 3: VALIDATE
1. Check QUALITY_GATES.md — verify each HARD gate manually
2. Confirm YAML frontmatter parses without errors
3. Confirm id matches `p04_audio_` prefix pattern
4. Confirm kind == audio_tool
5. Confirm direction is one of: input, output, analysis, bidirectional
6. Confirm models list in frontmatter matches model entries in ## Models section
7. Confirm formats are subset of allowed enum (mp3, wav, ogg, flac, webm, m4a, aac, pcm)
8. Confirm languages use BCP-47 codes (not free text like "English")
9. HARD gates: frontmatter valid, id pattern matches, direction declared, models listed, formats specified, languages listed
10. Cross-check: is this truly audio (not image/video)? Not a notifier? Not a CLI tool?
11. Score against QUALITY_GATES.md — revise if score < 8.0 before outputting

## ISO Loading

```yaml
loader: cex_skill_loader
injection_point: F3_compose
priority: high
```

```bash
python _tools/cex_skill_loader.py --verify audio
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `instruction` |
| Pillar | P03 |
| Domain | audio tool construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_audio_tool_builder]] | downstream | 0.54 |
| [[p10_lr_audio_tool_builder]] | downstream | 0.48 |
| [[p11_qg_audio_tool]] | downstream | 0.47 |
| [[bld_instruction_output_validator]] | sibling | 0.45 |
| [[bld_knowledge_card_audio_tool]] | upstream | 0.45 |
| [[bld_instruction_retriever_config]] | sibling | 0.44 |
| [[audio-tool-builder]] | downstream | 0.44 |
| [[bld_schema_audio_tool]] | downstream | 0.43 |
| [[bld_instruction_memory_scope]] | sibling | 0.43 |
| [[bld_instruction_chunk_strategy]] | sibling | 0.43 |
