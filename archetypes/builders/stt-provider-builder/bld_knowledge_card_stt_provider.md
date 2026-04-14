---
kind: knowledge_card
id: bld_knowledge_card_stt_provider
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for stt_provider production
quality: 9.2
title: "Knowledge Card Stt Provider"
version: "1.0.0"
author: wave1_builder_gen
tags: [stt_provider, builder, knowledge_card]
tldr: "Domain knowledge for stt_provider production"
domain: "stt_provider construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Domain Overview  
Speech-to-text (STT) provider integration connects applications to third-party ASR services, enabling transcription of audio inputs at varying latency and accuracy tiers. The market splits into cloud hyperscalers and specialized vendors:

**Cloud hyperscalers**: AWS Transcribe (WER ~5-8% English), Google Speech-to-Text v2 (WER ~4-6%, streaming latency ~200ms), Azure Speech Service (WER ~4-7%, custom models via Azure AI).

**Specialized vendors**: Deepgram (Nova-2 model, WER ~3-4%, 200ms streaming latency, $0.0043/min), OpenAI Whisper (open-source, large-v3 WER ~2.7% on LibriSpeech, no streaming), AssemblyAI (Conformer-2, WER ~4%, real-time streaming at $0.0065/min), Rev.ai (WER ~4.5%, human+AI hybrid option), Speechmatics (WER ~3.5%, 49+ languages).

**On-premise/self-hosted**: NVIDIA Riva (NeMo-based, GPU-accelerated, <100ms on A100), Kaldi (legacy toolkit, high customizability), Vosk (offline, lightweight for embedded), faster-whisper (CTranslate2 optimized Whisper, 4x faster inference).

Use cases span voice assistants, call center analytics, meeting transcription, accessibility tooling, and IoT voice commands. Key challenges: latency vs. accuracy trade-off, multilingual support, speaker diarization, data privacy (GDPR, HIPAA audio retention rules).  

## Key Concepts  
| Concept                | Definition                                                                 | Source                     |  
|-----------------------|----------------------------------------------------------------------------|----------------------------|  
| ASR (Automatic Speech Recognition) | Technology converting spoken language to text                                | ITU-T Recommendation P.501 |  
| API Gateway           | Middleware for routing, authenticating, and managing STT API requests       | AWS API Gateway Docs       |  
| WebSockets            | Protocol for bidirectional, real-time communication with STT services        | RFC 6455                   |  
| WebRTC                | Framework for low-latency audio streaming to STT providers                   | W3C WebRTC Specification   |  
| Language Code         | Identifier (e.g., `en-US`, `es-ES`) specifying the target language           | ISO 639-1                  |  
| Transcription Format  | Output structure (e.g., JSON, SRGS) defining time-stamped text segments      | W3C SRGS                   |  
| Latency Metrics       | Measurement of delay between audio input and transcription output            | Google Cloud Metrics Docs  |  
| Error Handling        | Mechanisms for managing API failures, timeouts, and invalid audio inputs     | REST API Best Practices    |  
| Billing Model         | Pricing structure (e.g., per-minute, per-character) for STT service usage    | AWS Pricing Docs           |  
| Provider-Specific Features | Customizable parameters (e.g., speaker diarization, noise suppression)     | Azure Speech Service Docs  |  

## Vendor Benchmark Matrix (2024)  
| Provider | WER (en-US) | Streaming Latency | Price (USD/min) | Diarization | Languages |
|---|---|---|---|---|---|
| Deepgram Nova-2 | ~3-4% | ~200ms | $0.0043 | Yes | 30+ |
| OpenAI Whisper large-v3 | ~2.7% | No streaming | open-source | No | 99+ |
| Google STT v2 | ~4-6% | ~200ms | $0.016 | Yes | 125+ |
| AWS Transcribe | ~5-8% | ~300ms | $0.024 | Yes | 37+ |
| Azure Speech | ~4-7% | ~200ms | $0.016 | Yes | 100+ |
| AssemblyAI Conformer-2 | ~4% | ~300ms | $0.0065 | Yes | 17+ |
| Rev.ai | ~4.5% | ~400ms | $0.020 | Yes | 36+ |
| NVIDIA Riva (on-prem) | ~3-5% | <100ms | self-hosted | Yes | 9 |

## Industry Standards  
- ITU-T P.501: Speech recognition system evaluation  
- ISO/IEC 24612: Common voice and speech data exchange  
- WebRTC: Real-time communication protocols  
- W3C SRGS: Speech recognition grammar specification  
- W3C Web Speech API: Browser-based STT standards  

## Common Patterns  
1. Use REST for synchronous transcription and WebSockets for streaming.  
2. Implement language detection before sending audio to STT APIs.  
3. Apply provider-specific noise suppression filters pre-transcription.  
4. Use WebRTC for real-time low-latency audio capture and transmission.  
5. Implement retry logic for transient API errors (e.g., 5xx responses).  
6. Cache language model configurations to reduce API overhead.  

## Pitfalls  
- Overlooking provider-specific rate limits leading to service degradation.  
- Assuming uniform accuracy across languages without validating model support.  
- Hardcoding API endpoints instead of using configurable abstraction layers.  
- Ignoring audio preprocessing (e.g., normalization) before STT ingestion.  
- Failing to secure API keys and sensitive transcription data in transit.
