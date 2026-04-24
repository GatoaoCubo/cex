---
id: p01_kc_perception_tools
kind: knowledge_card
8f: F3_inject
type: domain
pillar: P01
title: "Perception Tools — Audio Processing, Vision/Image, CLI Automation, Background Daemons"
version: 1.0.0
created: 2026-03-29
updated: 2026-03-29
author: builder_agent
domain: perception
origin: manual
quality: 9.1
tags: [audio, vision, tts, stt, whisper, cli, daemon, subprocess, image, multimodal]
tldr: "Perception tools give agents sensory capabilities — audio I/O (STT/TTS), vision analysis, CLI subprocess control, and persistent background daemons"
when_to_use: "Building or classifying components that process audio, images, run CLI tools, or manage background services"
keywords: [audio_tool, vision_tool, cli_tool, daemon, whisper, tts, gpt4v, subprocess]
long_tails:
  - "How to map Whisper STT and ElevenLabs TTS to CEX audio_tool kind"
  - "Which vision analysis tools map to CEX vision_tool kind"
  - "How to classify background daemons and CLI wrappers in CEX taxonomy"
axioms:
  - "Perception tools transform unstructured sensory input (audio, pixels) into structured data agents can reason over"
  - "CLI tools wrap subprocess calls with typed input/output contracts — never shell-inject raw user strings"
  - "Daemons are long-lived processes with health checks, graceful shutdown, and restart policies"
linked_artifacts:
  primary: null
  related: [p01_kc_external_integrations, p01_kc_langchain_patterns]
feeds_kinds:
  - audio_tool      # Whisper STT, ElevenLabs/Azure TTS, audio format conversion
  - vision_tool     # GPT-4V, Claude vision, OCR, image classification, screenshot analysis
  - cli_tool        # Subprocess wrappers, CLI parsers, command builders
  - daemon          # systemd/pm2/Windows Service, health checks, restart policies
density_score: 0.86
related:
  - p01_kc_audio_tool
  - bld_collaboration_audio_tool
  - audio-tool-builder
  - bld_architecture_audio_tool
  - p03_sp_audio_tool_builder
  - bld_knowledge_card_audio_tool
  - p01_kc_multi_modal_config
  - p10_lr_audio_tool_builder
  - bld_knowledge_card_multi_modal_config
  - p04_audio_whisper
---

# Perception Tools

## Quick Reference
```yaml
topic: Perception & Sensory Tool Patterns
scope: Audio (STT/TTS), vision/image analysis, CLI subprocess, daemon management
source: cross-domain (OpenAI Whisper, ElevenLabs, Claude Vision, subprocess docs)
criticality: medium-high
```

## Key Concepts

| Concept | Category | CEX Kind | Role |
|---------|----------|----------|------|
| Whisper STT | Audio | audio_tool | Speech-to-text transcription (local or API) |
| ElevenLabs TTS | Audio | audio_tool | Text-to-speech with voice cloning |
| Azure TTS | Audio | audio_tool | Cloud TTS with SSML and neural voices |
| Audio Converter | Audio | audio_tool | FFmpeg-based format/bitrate/sample-rate conversion |
| Voice Activity Detection | Audio | audio_tool | VAD for segmenting speech from silence |
| GPT-4V / Claude Vision | Vision | vision_tool | Multimodal image understanding and description |
| OCR Engine | Vision | vision_tool | Tesseract/Cloud OCR for text extraction from images |
| Image Classifier | Vision | vision_tool | Label assignment from image features |
| Screenshot Analyzer | Vision | vision_tool | UI element detection and layout understanding |
| Subprocess Runner | CLI | cli_tool | `subprocess.run()` with timeout, capture, error handling |
| Command Builder | CLI | cli_tool | Typed CLI argument construction (no shell injection) |
| Output Parser | CLI | cli_tool | Structured extraction from CLI stdout/stderr |
| systemd Service | Daemon | daemon | Linux persistent process with journald logging |
| pm2 Process | Daemon | daemon | Node.js process manager with cluster mode |
| Windows Service | Daemon | daemon | SCM-managed background process on Windows |
| Health Check Loop | Daemon | daemon | Periodic liveness/readiness probes |

## Patterns

| Trigger | Action |
|---------|--------|
| Transcribe audio input | Detect format -> convert if needed -> Whisper STT -> return text + timestamps |
| Generate speech output | Select voice -> render text via TTS API -> stream or save audio file |
| Analyze image content | Encode image as base64 -> send to vision model -> parse structured response |
| Extract text from image | Preprocess (contrast, deskew) -> OCR -> post-process (spell check, layout) |
| Run CLI tool safely | Build args list (no shell=True) -> subprocess.run with timeout -> parse output |
| Manage background daemon | Start with health check -> monitor with watchdog -> graceful shutdown on SIGTERM |

## Anti-Patterns

- Using `shell=True` with user-provided input in subprocess calls (command injection)
- Sending raw binary audio to STT without format detection/conversion
- Blocking the main event loop with synchronous vision API calls
- Running daemons without health checks or restart policies
- Hardcoding voice IDs or model names instead of configuration
- Ignoring audio sample rate mismatches (causes distorted transcriptions)

## CEX Mapping

```text
[audio_tool: STT] -> text -> [agent reasoning] -> text -> [audio_tool: TTS] -> audio
[vision_tool] -> structured_description -> [agent reasoning] -> action
[cli_tool] -> subprocess -> stdout -> [parser] -> structured_data
[daemon] -> long_running_loop -> [health_check] -> restart_if_needed
```

## References

- source: OpenAI Whisper (github.com/openai/whisper), ElevenLabs API, Claude Vision docs
- related: p01_kc_external_integrations

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_audio_tool]] | sibling | 0.50 |
| [[bld_collaboration_audio_tool]] | downstream | 0.45 |
| [[audio-tool-builder]] | downstream | 0.43 |
| [[bld_architecture_audio_tool]] | downstream | 0.42 |
| [[p03_sp_audio_tool_builder]] | downstream | 0.41 |
| [[bld_knowledge_card_audio_tool]] | sibling | 0.39 |
| [[p01_kc_multi_modal_config]] | sibling | 0.37 |
| [[p10_lr_audio_tool_builder]] | downstream | 0.36 |
| [[bld_knowledge_card_multi_modal_config]] | sibling | 0.36 |
| [[p04_audio_whisper]] | downstream | 0.34 |
