---
kind: knowledge_card
id: bld_knowledge_card_voice_pipeline
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for voice_pipeline production
quality: 9.2
title: "Knowledge Card: Voice Pipeline"
version: "1.1.0"
author: n01_audit
tags: [voice_pipeline, builder, knowledge_card, STT, TTS, WebRTC, RTP, SIP]
tldr: "Voice pipeline domain: providers, protocols (WebRTC/RTP/SIP), latency targets, error recovery, compliance patterns."
domain: "voice_pipeline construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
---

## Domain Overview

`voice_pipeline` artifacts define the system-level architecture for offline voice agent
processing: audio preprocessing -> STT -> NLU -> dialogue management -> TTS. Unlike
`realtime_session` (live LLM bidirectional stream), voice_pipeline is a modular, provider-
agnostic specification designed to be instantiated with real STT/TTS providers.

Production deployments use: Deepgram, AssemblyAI, or OpenAI Whisper v3 for STT; ElevenLabs,
Google Cloud TTS, Amazon Polly, or OpenAI TTS-1 for synthesis; Rasa, Dialogflow CX, or
AWS Lex v2 for NLU; telephony via Twilio Voice Media Streams (SRTP/RTP), LiveKit, Daily.

## Stage Reference

| Stage | Role | Example Providers | Latency Target |
|-------|------|-------------------|----------------|
| Audio Preprocessing | Noise reduction (RNNoise, WebRTC VAD), normalization, segmentation | SpeexDSP, WebRTC VAD, RNNoise | <= 20 ms |
| STT (ASR) | Audio -> transcript; streaming preferred | Deepgram Nova-2 (<300ms), AssemblyAI, OpenAI Whisper v3 | <= 300 ms first token |
| NLU | Intent + entity extraction | Rasa Open Source, Dialogflow CX, AWS Lex v2, spaCy + custom | <= 50 ms |
| Dialogue Management | Multi-turn context, response selection | LangChain, LlamaIndex, custom FSM, Microsoft Bot Framework | <= 100 ms |
| TTS | Text -> audio; streaming preferred | ElevenLabs Turbo v2.5, Google Cloud TTS, Amazon Polly Neural, OpenAI TTS-1 | <= 200 ms first chunk |

## Transport Protocols

| Protocol | Use Case | RFC / Standard | Notes |
|----------|----------|---------------|-------|
| WebRTC | Browser-to-backend voice; includes DTLS-SRTP | RFC 8829 | NAT traversal via ICE; best for web clients |
| RTP/RTCP | Real-time audio transport; telephony | RFC 3550 | Pair with SRTP (RFC 3711) for encryption |
| SRTP | Encrypted RTP for media streams | RFC 3711 | Required for HIPAA/GDPR media in transit |
| SIP | Session initiation for telephony | RFC 3261 | Used by Twilio, Vonage, Asterisk |
| WebSocket | Streaming audio to cloud STT (Deepgram, AssemblyAI) | IETF RFC 6455 | Streaming ASR API transport |
| gRPC | Server-side streaming STT/TTS | gRPC spec | Google Cloud STT/TTS native transport |

## Key Concepts

| Concept | Definition | Source |
|---------|------------|--------|
| Audio Preprocessing | Noise reduction, normalization, VAD, segmentation before STT | WebRTC Audio Processing, SpeexDSP |
| Streaming ASR | Chunk-based audio processing; first token latency << full utterance | Deepgram, AssemblyAI streaming docs |
| Word Error Rate (WER) | ASR accuracy metric: (S+D+I)/N; target < 10% for customer service | NIST Speech evaluation standards |
| Provider Abstraction | Interface layer that allows swapping STT/TTS without pipeline changes | System design pattern |
| Fallback Chain | Primary provider -> secondary -> scripted error; no silent failure | Operations best practice |
| Intent + Slot Filling | NLU output: what user wants (intent) + parameters (slots/entities) | Rasa, Dialogflow CX docs |
| SSML | Speech Synthesis Markup Language: controls TTS prosody, emphasis, pauses | W3C SSML 1.1 |
| VAD (Voice Activity Detection) | Detects speech start/end in audio stream | WebRTC VAD, Silero VAD |

## Latency Budgets

| Deployment | STT | NLU | DM | TTS | E2E Target |
|------------|-----|-----|----|-----|-----------|
| Contact center | 300ms | 50ms | 150ms | 250ms | ~800ms |
| Smart home | 500ms | 80ms | 200ms | 300ms | ~1100ms |
| IVR (telephony) | 400ms | 60ms | 100ms | 200ms | ~760ms |
| Voice search | 200ms | 40ms | 50ms | N/A | ~300ms |

## Industry Standards

- WebRTC (RFC 8829) -- peer connection, ICE, DTLS
- RTP/RTCP (RFC 3550) -- real-time media transport
- SRTP (RFC 3711) -- encrypted media
- SIP (RFC 3261) -- session initiation, telephony
- SSML 1.1 (W3C) -- speech synthesis markup
- ISO/IEC 23850:2017 -- speech processing
- W3C Voice Interaction Framework

## Common Patterns

1. **Streaming STT**: Send audio chunks to Deepgram/AssemblyAI WebSocket; first token in 300ms
2. **Provider fallback**: Deepgram fails -> OpenAI Whisper v3 API; zero-downtime for outages
3. **Audio preprocessing gate**: RNNoise + WebRTC VAD before STT; reduces WER by 25-40% in noise
4. **SSML-enhanced TTS**: Use `<break>`, `<prosody>` tags for natural pacing
5. **Telephony via Twilio**: SRTP/RTP on port 5004; SIP trunk to Twilio Voice Media Streams

## Pitfalls

- No audio preprocessing: WER degrades 25-60% in noisy environments (call center, mobile)
- Single-provider lock-in: vendor outage = pipeline down; always define fallback chain
- Silent NLU failure: empty intent passed to dialogue -> garbage TTS response
- Hardcoded vendor API URLs: breaks on provider migration; use config injection
- Missing SRTP for telephony: HIPAA/GDPR non-compliance for healthcare/financial voice data

## Properties

| Property | Value |
|----------|-------|
| Kind | `knowledge_card` |
| Pillar | P01 |
| Domain | voice_pipeline construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
