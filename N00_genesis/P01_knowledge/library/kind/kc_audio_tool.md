---
id: p01_kc_audio_tool
kind: knowledge_card
type: kind
pillar: P04
title: "Audio Tool — Deep Knowledge for audio_tool"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: operations_agent
domain: audio_tool
quality: 9.1
tags: [audio_tool, P04, CALL, kind-kc]
tldr: "Tool for speech-to-text, text-to-speech, and audio analysis enabling voice-driven agent interactions"
when_to_use: "Building, reviewing, or reasoning about audio_tool artifacts"
keywords: [stt, tts, voice-interface]
feeds_kinds: [audio_tool]
density_score: 1.0
linked_artifacts:
  primary: null
  related: []
related:
  - bld_collaboration_audio_tool
  - audio-tool-builder
  - bld_knowledge_card_audio_tool
  - stt-provider-builder
  - p04_audio_tool_NAME
  - p03_sp_audio_tool_builder
  - p10_lr_audio_tool_builder
  - p01_kc_perception_tools
  - bld_knowledge_card_voice_pipeline
  - p04_audio_whisper
---

# Audio Tool

## Spec
```yaml
kind: audio_tool
pillar: P04
llm_function: CALL
max_bytes: 2048
naming: p04_audio_{{capability}}.md + .yaml
core: false
```

## What It Is
An audio tool processes speech and sound — converting speech to text (STT), text to speech (TTS), or analyzing audio content (transcription, sentiment, speaker diarization). It enables voice-driven interactions with agents. It is NOT a vision_tool (which processes visual input) nor a notifier (which delivers messages via channels). An audio tool handles the audio modality specifically.

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | Custom `BaseTool` wrapping Whisper/ElevenLabs SDK | Audio processing as a callable tool in agent chains |
| LlamaIndex | Custom `FunctionTool` for audio APIs | Wrap audio API as queryable tool |
| CrewAI | `BaseTool` with audio API in `_run()` | Agent tool that processes audio input/output |
| DSPy | Python function calling audio API in `forward()` | Direct API call to audio service within module |
| Haystack | Custom `@component` for audio processing | Audio component in pipeline (e.g., STT → LLM → TTS) |
| OpenAI | `whisper-1` (STT) / `tts-1` (TTS) API endpoints | Native audio endpoints for transcription and speech |
| Anthropic | No native audio — use MCP audio servers | Audio via MCP tools (e.g., ElevenLabs MCP server) |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| provider | enum | "openai" | OpenAI = cheap STT; ElevenLabs = best TTS quality |
| language | string | "pt-BR" | Explicit language = better accuracy but limits multilingual |
| voice_id | string | varies | Custom voice = brand consistency but setup cost |
| max_duration_s | int | 300 | Longer = flexible but higher cost and latency |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| STT-LLM-TTS pipeline | Voice assistant flow | Whisper transcribe → Claude process → ElevenLabs speak |
| Batch transcription | Processing recorded content | Transcribe meeting recordings for knowledge extraction |
| Voice cloning | Brand voice consistency | ElevenLabs voice clone for automated social media narration |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| Real-time STT without VAD | Processes silence, wastes API credits | Add Voice Activity Detection before sending to STT |
| Single provider lock-in | No fallback when provider is down | Abstract behind interface; swap providers without code changes |

## Integration Graph
```
[action_prompt] --> [audio_tool] --> [output_template]
                        |
                  [api_client]
```

## Decision Tree
- IF input is human speech THEN use STT audio_tool (Whisper or similar)
- IF output needs voice THEN use TTS audio_tool (ElevenLabs for quality, OpenAI for cost)
- IF processing recorded content THEN use batch transcription pattern
- DEFAULT: OpenAI Whisper for STT, ElevenLabs for TTS

## Quality Criteria
- GOOD: Clear capability (STT/TTS/analysis), provider configured, language set
- GREAT: Includes fallback provider, VAD for STT, voice consistency for TTS
- FAIL: No language config; no error handling for audio failures; missing provider

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_audio_tool]] | downstream | 0.64 |
| [[audio-tool-builder]] | related | 0.57 |
| [[bld_knowledge_card_audio_tool]] | sibling | 0.55 |
| [[stt-provider-builder]] | related | 0.53 |
| [[p04_audio_tool_NAME]] | related | 0.52 |
| [[p03_sp_audio_tool_builder]] | related | 0.49 |
| [[p10_lr_audio_tool_builder]] | downstream | 0.49 |
| [[p01_kc_perception_tools]] | sibling | 0.45 |
| [[bld_knowledge_card_voice_pipeline]] | sibling | 0.43 |
| [[p04_audio_whisper]] | related | 0.43 |
