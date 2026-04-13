---
id: atom_29_voice_realtime
kind: knowledge_card
pillar: P01
title: Voice Agent Architecture and Configuration Reference
author: AI Systems Engineering Team
date: 2026-04-13
version: 3.0
quality: 9.0
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

## Boundary

This artifact is a **technical reference for implementing voice agent systems**, covering codec-based speech-to-speech (S2S) and cascading pipeline (STT→LLM→TTS) architectures. It is **not** a product specification, user guide, or design pattern document. It focuses on **configuration patterns, industry terminology mapping, and performance metrics** for real-time voice applications.

## Related Kinds

- **architecture_diagram**: Shows system components and flow
- **configuration_template**: Provides example YAML structures
- **performance_benchmark**: Contains latency and throughput metrics
- **industry_mapping**: Defines terminology equivalences
- **transport_protocol**: Details WebRTC, SIP, WebSocket implementations

---

## 1. Introduction

This document provides a technical reference for implementing voice agent systems, covering both **codec-based speech-to-speech (S2S)** and **cascading pipeline (STT→LLM→TTS)** architectures. It includes configuration patterns, industry terminology mapping, and performance metrics for real-time voice applications.

---

## 2. Core Architectures

### 2.1 Codec-Based S2S vs Cascading Pipeline

| Feature | Codec-Based S2S | Cascading Pipeline |
|--------|------------------|---------------------|
| **LLM Output** | Audio tokens (EnCodec, Mimi) | Text tokens (LLM) |
| **Transport** | WebRTC, WebSocket, SIP | WebRTC, WebSocket |
| **Advantages** | Lower latency, native emotion modeling | Modular components, tool calling support |
| **Limitations** | Vendor-specific codec dependencies | Higher latency (500ms+) |
| **Use Cases** | Real-time emotion modeling | Enterprise IVR, telephony |

---

## 3. Configuration Patterns

### 3.1 Voice Agent Configuration (`voice_agent.yaml`)

| Parameter | Value | Description | Valid Range |
|----------|-------|-------------|-------------|
| `vad_threshold` | 0.7 | Voice activity detection sensitivity | 0.1–1.0 |
| `tts_speed` | 1.2 | Text-to-speech playback rate | 0.5–2.0 |
| `emotion_style` | "empathetic" | Emotion modulation mode | "neutral", "empathetic", "urgent", "calm" |
| `codecs` | ["opus", "pcm16"] | Supported audio codecs | opus, pcm16, g711 |
| `transport` | "webRTC" | Communication protocol | webRTC, websocket, sip |

---

## 4. Performance Metrics

| Metric | Codec-Based S2S | Cascading Pipeline |
|-------|------------------|---------------------|
| **Latency (ms)** | 120–180 | 500–700 |
| **Throughput (tokens/s)** | 1200–1500 | 800–1000 |
| **Jitter (ms)** | 10–20 | 50–80 |
| **Packet Loss (%)** | <0.5 | <1.2 |
| **Supported Codecs** | opus, pcm16 | opus, pcm16 |

---

## 5. Transport Layer Configurations

### 5.1 WebRTC, SIP Trunk, WebSocket Comparison

| Transport Type | Use Case | Protocols | Codecs | NAT Traversal | Bandwidth (kbps) |
|---------------|----------|-----------|--------|----------------|------------------|
| **WebRTC** | Real-time voice | SRTP, ICE | opus, pcm16 | STUN/TURN | 64–256 |
| **SIP Trunk** | Telephony integration | SIP, RTP | g711, pcm16 | STUN/TURN | 64–128 |
| **WebSocket** | Low-latency fallback | WebSocket | opus | None | 128–256 |

---

## 6. Prosody and Emotion Modeling

### 6.1 Prosody Profile Parameters

| Parameter | Value | Description | Valid Range |
|----------|-------|-------------|-------------|
| `pitch_shift` | 0.8 | Pitch modulation factor | 0.5–2.0 |
| `duration_stretch` | 1.1 | Speech duration scaling | 0.8–1.5 |
| `energy_level` | 0.9 | Loudness modulation | 0.1–1.0 |
| `emotion_weight` | 0.7 | Emotion influence factor | 0.1–1.0 |
| `language` | "en-US" | Language model | "en-US", "es-ES", "fr-FR" |

---

## 7. Industry Terms vs CEX Metaphors

| Industry Term | CEX Metaphor | Description | Use Case |
|--------------|--------------|-------------|-----------|
| **Voice Activity Detection** | `vad_threshold` | Detects speech presence | Noise suppression |
| **Text-to-Speech** | `tts_speed` | Converts text to audio | Voice response |
| **Emotion Modulation** | `emotion_style` | Adjusts vocal tone | Customer service |
| **Codecs** | `codecs` | Audio compression format | Bandwidth optimization |
| **Transport Protocol** | `transport` | Communication channel | Network reliability |

---

## 8. Configuration Validation Rules

| Rule # | Description | Valid Values | Notes |
|-------|-------------|---------------|-------|
| 1 | `vad_threshold` | 0.1–1.0 | Higher = more sensitive |
| 2 | `tts_speed` | 0.5–2.0 | 1.0 = normal pace |
| 3 | `emotion_style` | "neutral", "empathetic", "urgent", "calm" | Required for emotion modeling |
| 4 | `codecs` | opus, pcm16, g711 | Must include at least one |
| 5 | `transport` | webRTC, websocket, sip | Required for communication |

---

## 9. References

- [Hume EVI Documentation](https://docs.hume.ai)
- [Deepgram API Reference](https://developers.deepgram.com)
- [Cartesia TTS SDK](https://cartesia.ai)
- [OpenAI gpt-realtime API](https://platform.openai.com)