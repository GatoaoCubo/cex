---
kind: config
id: bld_config_audio_tool
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
effort: medium
max_turns: 25
disallowed_tools: []
fork_context: null
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: nucleus
quality: 9.0
title: "Config Audio Tool"
version: "1.0.0"
author: n03_builder
tags: [audio_tool, builder, examples]
tldr: "Golden and anti-examples for audio tool construction, demonstrating ideal structure and common pitfalls."
domain: "audio tool construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_knowledge_card_audio_tool
  - bld_instruction_audio_tool
  - p03_sp_audio_tool_builder
  - p10_lr_audio_tool_builder
  - bld_examples_audio_tool
  - bld_schema_audio_tool
  - bld_collaboration_audio_tool
  - audio-tool-builder
  - p01_kc_audio_tool
  - stt-provider-builder
---
# Config: audio_tool Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p04_audio_{capability_slug}.md` | `p04_audio_speech_transcription.md` |
| Builder directory | kebab-case | `audio-tool-builder/` |
| Frontmatter fields | snake_case | `sample_rate`, `word_timestamps`, `voice_id` |
| Capability slug | snake_case, lowercase, no hyphens | `speech_transcription`, `tts_synthesis` |
| Model identifiers | snake_case, provider prefix where ambiguous | `whisper_large_v3`, `eleven_multilingual_v2` |
| Language codes | BCP-47 standard | `en`, `pt-BR`, `es`, `fr`, `zh` |
Rule: id MUST equal filename stem. Hyphens in id = HARD FAIL.
Rule: language codes MUST be BCP-47, never free-text ("English" -> HARD FAIL).
## File Paths
- Output: `cex/P04_tools/examples/p04_audio_{capability_slug}.md`
- Compiled: `cex/P04_tools/compiled/p04_audio_{capability_slug}.yaml`
## Size Limits (aligned with SCHEMA)
- Body: max 2048 bytes
- Total (frontmatter + body): ~4000 bytes
- Density: >= 0.80 (no filler)
## Direction Enum
| Value | Meaning | Input | Output |
|-------|---------|-------|--------|
| input | Speech-to-text | audio bytes | text string |
| output | Text-to-speech | text string | audio bytes |
| analysis | Feature extraction | audio bytes | JSON features |
| bidirectional | STT + TTS | audio or text | text or audio |
## Format Enum (allowed values)
| Value | Type | Notes |
|-------|------|-------|
| mp3 | lossy | Common upload format; widely supported |
| wav | lossless | PCM; highest STT accuracy |
| ogg | open | Vorbis codec; good web support |
| flac | lossless | Compressed lossless; STT only |
| webm | open | Browser MediaRecorder default |
| m4a | lossy | Apple; AAC codec |
| aac | lossy | Efficient compression |
| pcm | raw | Lowest latency; raw samples |
## Sample Rate Conventions
| Value | When to use |
|-------|-------------|
| 16000 | STT standard — best accuracy across all models |
| 22050 | TTS medium quality — balanced size/fidelity |
| 44100 | TTS high quality — CD-quality audio output |
| 8000 | Telephony — VoIP/PSTN narrow-band scenarios |
Rule: every audio_tool MUST declare at least direction, models, formats, and languages.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_audio_tool]] | upstream | 0.56 |
| [[bld_instruction_audio_tool]] | upstream | 0.49 |
| [[p03_sp_audio_tool_builder]] | upstream | 0.48 |
| [[p10_lr_audio_tool_builder]] | downstream | 0.46 |
| [[bld_examples_audio_tool]] | upstream | 0.43 |
| [[bld_schema_audio_tool]] | upstream | 0.43 |
| [[bld_collaboration_audio_tool]] | downstream | 0.41 |
| [[audio-tool-builder]] | upstream | 0.41 |
| [[p01_kc_audio_tool]] | upstream | 0.39 |
| [[stt-provider-builder]] | upstream | 0.35 |
