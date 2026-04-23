---
kind: architecture
id: bld_architecture_audio_tool
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of audio_tool — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Audio Tool"
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
  - audio-tool-builder
  - p11_qg_audio_tool
  - bld_instruction_audio_tool
  - bld_collaboration_audio_tool
  - bld_knowledge_card_audio_tool
  - p01_kc_audio_tool
  - bld_examples_audio_tool
  - p01_kc_perception_tools
---

## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| direction | STT/TTS/analysis/bidirectional | audio_tool | required |
| model | Audio model identifier | audio_tool | required |
| format | Audio format (mp3, wav, ogg, etc.) | audio_tool | required |
| language | BCP-47 language code | audio_tool | required |
| sample_rate | Hz for model accuracy | audio_tool | recommended |
| streaming | Real-time chunk processing | audio_tool | recommended |
| word_timestamps | Per-word timing output | audio_tool | recommended |
| voice_id | TTS voice identifier | audio_tool | conditional |
| guardrail | Duration/rate limits | P11 | external |
| agent | Invokes audio tool | P02 | consumer |
| notifier | Delivers TTS output | P04 | consumer |
## Dependency Graph
```
format      --depends-->  model
language    --depends-->  model
sample_rate --depends-->  model
model       --produces--> transcript (direction: input)
model       --produces--> audio_bytes (direction: output)
model       --produces--> features (direction: analysis)
streaming   --modifies--> model
word_timestamps --modifies--> model
guardrail   --constrains--> model
agent       --invokes-->  direction
notifier    --consumes--> audio_bytes
```
| From | To | Type | Data |
|------|----|------|------|
| format | model | depends | format accepted by model |
| language | model | depends | in model's supported list |
| sample_rate | model | depends | affects accuracy |
| model | transcript | produces | text output for direction: input |
| model | audio_bytes | produces | audio output for direction: output |
| model | features | produces | JSON features for direction: analysis |
| streaming | model | modifies | enables chunked real-time processing |
| guardrail | model | constrains | max_duration, rate limit enforcement |
| agent | direction | invokes | agent selects direction and submits payload |
| notifier | audio_bytes | consumes | TTS output delivered to user channel |
## Boundary Table
| audio_tool IS | audio_tool IS NOT |
|---------------|------------------|
| Processes audio signals (speech, sound, music) | A visual processr — that is vision_tool |
| Converts speech to text (STT / direction: input) | A message delivery system — that is notifier |
| Generates speech from text (TTS / direction: output) | A terminal utility — that is cli_tool |
| Analyzes audio features (diarization, emotion, lang detect) | A generic HTTP client — that is api_client |
| Bound to specific audio models with known providers | A background persistent process — that is daemon |
| Format and language scoped at spec time | A video processr — that is vision_tool (video frames) |
## Layer Map
| Layer | Components | Purpose |
|-------|-----------|---------|
| configuration | language, sample_rate, voice_id | Scope model behavior |
| interface | direction, format, streaming | Audio surface |
| execution | model, word_timestamps | Process signal |
| governance | guardrail | Duration/rate limits |
| callers | agent, notifier | Runtime consumers |
## Confusion Zones
| Scenario | Seems Like | Actually Is | Rule |
|---|---|---|---|
| Send voice message | audio_tool | notifier | notifier=delivery; audio_tool=process audio |
| Analyze image content | audio_tool | vision_tool | vision_tool=images; audio_tool=sound |
| Run CLI audio converter | audio_tool | cli_tool | cli_tool=shell cmd; audio_tool=model-based |
## Decision Tree
- STT/TTS/audio analysis? → audio_tool
- Image/screenshot analysis? → vision_tool
- Push notification delivery? → notifier
- Shell command? → cli_tool
## Neighbor Comparison
| Dim | audio_tool | vision_tool | Diff |
|---|---|---|---|
| Signal | Sound waves | Pixels | Different modality |
| Models | Whisper/TTS | GPT-4V/OCR | Specialized models |
| Output | Text/audio | JSON/text | audio_tool can produce audio |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_audio_tool_builder]] | upstream | 0.55 |
| [[p10_lr_audio_tool_builder]] | downstream | 0.48 |
| [[audio-tool-builder]] | upstream | 0.46 |
| [[p11_qg_audio_tool]] | downstream | 0.46 |
| [[bld_instruction_audio_tool]] | upstream | 0.43 |
| [[bld_collaboration_audio_tool]] | downstream | 0.42 |
| [[bld_knowledge_card_audio_tool]] | upstream | 0.42 |
| [[p01_kc_audio_tool]] | upstream | 0.38 |
| [[bld_examples_audio_tool]] | upstream | 0.37 |
| [[p01_kc_perception_tools]] | upstream | 0.36 |
