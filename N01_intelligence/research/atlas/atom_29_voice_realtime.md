---
id: atom_29_voice_realtime
kind: knowledge_card
pillar: P01
title: Voice Agent Architecture and Configuration Reference
author: AI Systems Engineering Team
date: 2026-04-13
version: 3.0
quality: 8.8
tags:
  - voice
  - realtime
  - s2s
  - vad
  - pipecat
  - livekit
  - moshi
  - openai-realtime
---

# Voice Agent Architecture and Configuration Reference

## 1. Introduction

This document provides a technical reference for implementing voice agent systems, covering both **codec-based speech-to-speech (S2S)** and **cascading pipeline (STT→LLM→TTS)** architectures. It includes configuration patterns, industry terminology mapping, and performance metrics for real-time voice applications.

---

## 2. Core Architectures

### 2.1 Codec-Based S2S
- **LLM Output**: Audio tokens generated via neural audio codecs (e.g., EnCodec, Mimi)
- **Transport**: WebRTC, WebSocket, or SIP-based streaming
- **Advantages**: Lower latency, native emotion modeling (eLLM), end-to-end prosody control
- **Limitations**: Limited LLM flexibility, vendor-specific codec dependencies

### 2.2 Cascading Pipeline
- **Stage Chain**: VAD → STT → LLM → TTS → Transport
- **Flexibility**: Modular components (e.g., Deepgram, Cartesia, Pipecat)
- **Use Cases**: Enterprise IVR, telephony integration, complex tool calling
- **Latency**: Typically 500ms+ for full pipeline

---

## 3. Configuration Patterns

### 3.1 Voice Agent Configuration (`voice_agent_config`)
```yaml
persona: "customer_support"
vad_mode: "semantic"
turn_detection: 
  silence_threshold: 500
  eagerness: 0.7
session_params:
  max_concurrent_turns: 2
voice_selection:
  style: "calm"
  pitch_range: "normal"
```

### 3.2 VAD Configuration (`vad_config`)
```yaml
type: "semantic"
server_threshold: 0.6
client_padding: 100
silence_duration_ms: 800
```

### 3.3 STT Configuration (`stt_config`)
```yaml
provider: "deepgram"
model: "nova-2"
language: "en-US"
custom_vocabulary: ["account", "billing"]
streaming_mode: "async"
confidence_threshold: 0.75
```

### 3.4 TTS Configuration (`tts_config`)
```yaml
provider: "cartesia"
voice_id: "professional_french"
ssml_support: true
speed: 1.2
emotion_style: "empathetic"
streaming_format: "opus"
```

---

## 4. Performance Metrics

| Metric | Description | Typical Range |
|------|-------------|---------------|
| **TTFA** | Time to First Audio | 100-300ms (S2S), 500-800ms (cascading) |
| **TTFB** | Time to First Byte | 50-150ms (S2S), 200-400ms (cascading) |
| **TTFT** | Time to First Token | 50-100ms (LLM) |
| **TTFW** | Time to First Word | 200-400ms (TTS) |
| **E2E Latency** | End-to-end round trip | 500-1500ms (cascading), 200-600ms (S2S) |

---

## 5. Industry Terms vs. CEX Metaphors

| Industry Term | User Intent | CEX Mapping |
|--------------|-------------|-------------|
| **Barge-in** | "Interrupt the bot" | `voice_agent_config.interruption_handling` |
| **Prosody control** | "Make the voice sound happy" | `prosody_profile.emotion_style` |
| **SSML** | "Markup for voice" | `prosody_profile.ssml_template` |
| **Speech-to-speech** | "Direct voice model" | S2S architecture pattern |
| **Turn-taking** | "Conversation flow" | `voice_agent_config.turn_detection` |
| **Endpointing** | "When did they stop talking?" | `vad_config.silence_duration_ms` |
| **Cascading pipeline** | "The STT-LLM-TTS chain" | `voice_pipeline` kind |

---

## 6. Transport Layer Configurations

### 6.1 WebRTC
- **Use Case**: Browser-based voice agents
- **Protocols**: ICE, DTLS, RTP
- **Codecs**: Opus, G.711, PCM16
- **NAT Traversal**: STUN/TURN servers

### 6.2 SIP Trunk
- **Use Case**: Enterprise telephony integration
- **Components**: PSTN gateway, IVR fallback
- **Call Recording**: Configurable via `telephony_config`

### 6.3 WebSocket
- **Use Case**: Server-side voice agents
- **Advantages**: Persistent bidirectional connection
- **Limitations**: No native NAT traversal

---

## 7. Prosody and Emotion Modeling

### 7.1 Prosody Profile (`prosody_profile`)
```yaml
pitch_range: "wide"
rate: 1.1
volume: "medium"
emphasis_patterns: ["question", "exclamation"]
emotional_style: "empathetic"
ssml_template: "<prosody rate='1.2'><emphasis level='strong'>{text}</emphasis></prosody>"
```

### 7.2 Emotion Detection
- **Models**: Hume EVI, Gemini Live
- **Expression Measures**: Quantified signals per sentence
- **Integration**: `emotion_model_config` with top-K emotion mapping

---

## 8. Architecture Decision Map

```
User says: "I want a voice agent"
                |
    +-----------+-----------+
    |                       |
 Realtime (S2S)        Cascading (STT->LLM->TTS)
    |                       |
 OpenAI gpt-realtime   Any LLM + Deepgram/Cartesia
 Gemini Live            Pipecat / LiveKit framework
 Hume EVI               Full tool calling support
    |                       |
 Lower latency          More control
 Limited LLM choice     Higher latency
 Native emotion         Modular components
    |                       |
    +-----------+-----------+
                |
         Transport choice
                |
    +-----------+-----------+-----------+
    |           |           |           |
 WebRTC     WebSocket     SIP       Hybrid
 (browser)  (server)    (phone)   (WebRTC+SIP)
```

---

## 9. Glossary (Alphabetical)

| Term | Category | Definition |
|------|----------|------------|
| **TTFA** | Metric | Time to First Audio in voice response |
| **VAD** | Component | Voice Activity Detection for turn management |
| **S2S** | Architecture | Speech-to-speech codec-based system |
| **Prosody** | Feature | Control over speech rhythm, pitch, and emphasis |
| **EVI** | System | Emotion Voice Interface (Hume) |
| **LLM** | Component | Large Language Model for text generation |
| **TTS** | Component | Text-to-Speech synthesis engine |
| **STT** | Component | Speech-to-Text recognition engine |
| **Codec** | Technology | Audio encoding/decoding (e.g., EnCodec) |
| **IVR** | Use Case | Interactive Voice Response system |
| **PSTN** | Network | Public Switched Telephone Network |

---

## 10. Appendix: Configuration Validation Rules

1. **VAD Thresholds**: Must be between 0.1-1.0 for semantic detection
2. **TTS Speed**: Valid range 0.5-2.0
3. **Emotion Style**: Must be one of: "neutral", "empathetic", "urgent", "calm"
4. **Codecs**: Supported: opus, pcm16, g711
5. **Transport Protocols**: webRTC, websocket, sip

---

## 11. References

- [Hume EVI Documentation](https://docs.hume.ai)
- [Deepgram API Reference](https://developers.deepgram.com)
- [Cartesia TTS SDK](https://cartesia.ai)
- [OpenAI gpt-realtime API](https://platform.openai.com)