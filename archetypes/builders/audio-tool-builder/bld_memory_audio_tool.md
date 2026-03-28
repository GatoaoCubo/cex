---
id: p10_lr_audio_tool_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: edison
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
satellite: edison
keywords: [audio tool, STT, TTS, direction, language codes, BCP-47, model naming, format, sample rate, streaming]
---

## Summary
Audio tools are consumed by voice interfaces, content pipelines, and agents that select STT or TTS paths at runtime. The difference between a tool that routes correctly and one that causes silent format mismatches comes down to three decisions made at spec time: direction declaration, BCP-47 language codes, and explicit model identifiers matching provider documentation.
A tool that omits direction (or uses a non-enum value), lists languages as free text, or uses model names that differ from the provider API (e.g., "GPT-4o" for audio, "Whisper" instead of "whisper_large_v3") will cause integration failures that are expensive to diagnose.
## Pattern
**Explicit direction, BCP-47 languages, exact model identifiers.**
Direction schema (enum):
- input: STT — audio bytes in, text out
- output: TTS — text in, audio bytes out
- analysis: feature extraction — audio in, JSON features out
- bidirectional: both STT and TTS supported
Language code rules:
- Always BCP-47: `en`, `pt-BR`, `es`, `fr-CA`, `zh`, `ja`
- Never free text: "English", "Portuguese", "Chinese" — breaks lookup
- Include quality tier per model when coverage varies (high/medium/low)
Model naming rules:
- Use exact provider API identifiers: `whisper_large_v3`, `deepgram_nova_2`, `eleven_multilingual_v2`
- Never use marketing names: "Whisper Large", "ElevenLabs Multilingual" — spec drift
- Mirror frontmatter `models` list exactly to ## Models table entries
Sample rate rules:
- Declare `sample_rate: 16000` for all STT tools — models assume 16kHz input
- Declare `sample_rate: 22050` or `44100` for TTS output quality contract
Body budget (2048 bytes max): Overview (150) + Direction (200) + Models (400) + Formats (300) + Languages (400) = ~1450.
## Anti-Pattern
- Omitting direction field entirely (caller cannot determine STT vs TTS path).
- Using "English" instead of "en" for language codes (BCP-47 compliance failure).
- Model names like "Whisper" or "ElevenLabs" instead of exact API identifiers.
- Claiming streaming support without declaring `streaming: true` in frontmatter.
- Including formats not in the allowed enum (e.g., "audio/mpeg" mime type notation).
- Conflating audio_tool with notifier: audio_tool processes signals; notifier delivers messages.
- Conflating audio_tool with vision_tool: audio processes sound; vision processes images/video.
## Context
Body limit 2048B (larger than cli_tool 1024B). Write direction+models in frontmatter first. BCP-47 codes mandatory — map to provider API params.
