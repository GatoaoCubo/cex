---
id: atom_29_voice_realtime
kind: knowledge_card
pillar: P01
title: Voice Agent Architecture and Configuration Reference
author: AI Systems Engineering Team
date: 2026-04-13
version: 4.0
quality: 8.7
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
- [OpenAI Realtime API Reference](https://platform.openai.com/docs/api-reference/realtime)
- [OpenAI Realtime VAD Guide](https://platform.openai.com/docs/guides/realtime-vad)
- [OpenAI Realtime Client Events](https://platform.openai.com/docs/api-reference/realtime-client-events)
- [OpenAI Realtime Server Events](https://platform.openai.com/docs/api-reference/realtime-server-events)
- [Pipecat Pipeline Architecture](https://docs.pipecat.ai/guides/learn/pipeline)
- [Pipecat DeepWiki](https://deepwiki.com/pipecat-ai/pipecat)
- [LiveKit Agents Framework](https://github.com/livekit/agents)
- [LiveKit Silero VAD Plugin](https://docs.livekit.io/agents/logic/turns/vad/)
- [LiveKit Turn Detection](https://docs.livekit.io/agents/build/turns/turn-detector/)
- [LiveKit EOU Blog](https://blog.livekit.io/using-a-transformer-to-improve-end-of-turn-detection)
- [Moshi arXiv Paper](https://arxiv.org/abs/2410.00037)
- [Moshi Kyutai GitHub](https://github.com/kyutai-labs/moshi)
- [Silero VAD GitHub](https://github.com/snakers4/silero-vad)
- [Picovoice VAD Comparison 2026](https://picovoice.ai/blog/best-voice-activity-detection-vad/)
- [TEN VAD (TEN Framework)](https://github.com/TEN-framework/ten-vad)

---

## 10. OpenAI Realtime API v2 -- Event Reference

Source: [OpenAI Realtime API Reference](https://platform.openai.com/docs/api-reference/realtime)

### 10.1 Client Events (sent by client to server)

| Event | Purpose |
|-------|---------|
| `session.update` | Modify session config: model, voice, modalities, VAD, tools, instructions |
| `input_audio_buffer.append` | Stream raw audio bytes (base64 PCM16 or g711) to server buffer |
| `input_audio_buffer.commit` | Manually commit buffered audio as conversation item (non-VAD mode) |
| `input_audio_buffer.clear` | Flush input buffer without creating an item |
| `conversation.item.create` | Insert message, function call, or function result into conversation |
| `conversation.item.truncate` | Truncate assistant audio to sync with client playback after barge-in |
| `conversation.item.delete` | Remove an item from conversation history |
| `response.create` | Trigger a new model response (overrides session response config) |
| `response.cancel` | Cancel an in-progress response |

### 10.2 Server Events (emitted by server to client)

| Event | Category | Description |
|-------|----------|-------------|
| `error` | Control | Recoverable error; session remains open |
| `session.created` | Lifecycle | First event on connection; contains default session config |
| `session.updated` | Lifecycle | Confirms session.update applied; returns full effective config |
| `conversation.created` | Lifecycle | New conversation initialized |
| `conversation.item.created` | Conversation | New item added (user message, assistant turn, function call) |
| `conversation.item.input_audio_transcription.completed` | Audio | STT transcript ready for committed audio item |
| `conversation.item.input_audio_transcription.delta` | Audio | Streaming transcript delta |
| `conversation.item.input_audio_transcription.failed` | Audio | Transcription error |
| `conversation.item.truncated` | Conversation | Confirms item truncation |
| `conversation.item.deleted` | Conversation | Confirms item deletion |
| `input_audio_buffer.committed` | Audio | Server committed audio to conversation |
| `input_audio_buffer.cleared` | Audio | Buffer cleared |
| `input_audio_buffer.speech_started` | VAD | VAD detected start of user speech |
| `input_audio_buffer.speech_stopped` | VAD | VAD detected end of user speech |
| `response.created` | Response | Response created, status=in_progress |
| `response.done` | Response | Response complete; status: completed/cancelled/failed/incomplete |
| `response.output_item.added` | Response | New output item added to response |
| `response.output_item.done` | Response | Output item finalized |
| `response.content_part.added` | Response | Content part added (audio, text, or transcript) |
| `response.content_part.done` | Response | Content part complete |
| `response.text.delta` | Streaming | Text token delta |
| `response.text.done` | Streaming | Full text complete |
| `response.audio_transcript.delta` | Streaming | Audio transcript token delta |
| `response.audio_transcript.done` | Streaming | Full audio transcript complete |
| `response.audio.delta` | Streaming | Audio bytes delta (base64) |
| `response.audio.done` | Streaming | Audio generation complete |
| `response.function_call_arguments.delta` | Tools | Function call argument streaming |
| `response.function_call_arguments.done` | Tools | Function call complete |
| `output_audio_buffer.audio_started` | Audio | Output audio playback started |
| `output_audio_buffer.audio_stopped` | Audio | Output audio playback stopped |
| `output_audio_buffer.cleared` | Audio | Output buffer cleared (on barge-in or client request) |
| `rate_limits.updated` | Control | Rate limit counters updated |

### 10.3 Turn Detection (VAD) via session.update

**server_vad** (energy-based, default):
```json
{
  "turn_detection": {
    "type": "server_vad",
    "threshold": 0.5,
    "prefix_padding_ms": 300,
    "silence_duration_ms": 500,
    "create_response": true,
    "interrupt_response": true
  }
}
```

| Parameter | Default | Range | Notes |
|-----------|---------|-------|-------|
| `threshold` | 0.5 | 0.0-1.0 | Higher = louder audio required; better for noisy envs |
| `silence_duration_ms` | 500 | 200-2000 | Lower = faster response, more false triggers |
| `prefix_padding_ms` | 300 | 0-1000 | Audio before speech onset included in utterance |

**semantic_vad** (transformer-based; gpt-4o-realtime required):
```json
{
  "turn_detection": {
    "type": "semantic_vad",
    "eagerness": "auto",
    "create_response": true,
    "interrupt_response": true
  }
}
```

| `eagerness` | Max wait | Notes |
|-------------|----------|-------|
| `low` | 8s | Waits longer; better for complex sentences |
| `medium` / `auto` | 4s | Balanced default |
| `high` | 2s | Responds quickly; may interrupt longer utterances |

**server_vad vs semantic_vad**:

| Dimension | server_vad | semantic_vad |
|-----------|-----------|-------------|
| Algorithm | Energy/amplitude threshold | Transformer language model |
| False triggers | Common on filler words ("um", "uh") | Understands incomplete sentences |
| Model requirement | Any gpt-4o-realtime | gpt-4o-realtime only |
| Best for | Low-latency, noisy environments | Natural conversation |

---

## 11. Pipecat Frame-Based Pipeline Architecture

Source: [Pipecat Docs](https://docs.pipecat.ai/guides/learn/pipeline), [Pipecat DeepWiki](https://deepwiki.com/pipecat-ai/pipecat)

### 11.1 Frame Taxonomy

Everything in Pipecat is a Frame. Three priority classes:

| Class | Queue behavior | Examples |
|-------|---------------|---------|
| `SystemFrame` | Bypasses all queues -- immediate | `StartFrame`, `EndFrame`, `CancelFrame`, `InterruptionFrame` |
| `DataFrame` | Queued, in-order | `InputAudioRawFrame`, `OutputAudioRawFrame`, `TextFrame`, `LLMTextFrame`, `TranscriptionFrame` |
| `ControlFrame` | Queued, in-order | `LLMContextFrame`, `LLMRunFrame`, response boundary markers |

`UninterruptibleFrame` mixin: preserves critical frames (function results, state updates) through interruptions.

### 11.2 Bidirectional Frame Flow

```
DOWNSTREAM: Transport Input -> STT -> LLMUserAgg -> LLM -> LLMAssistantAgg -> TTS -> Transport Output
UPSTREAM:   Transport Output <- InterruptionFrame (VAD) <- any processor
```

Each FrameProcessor implements:
```python
async def process_frame(self, frame: Frame, direction: FrameDirection):
    await self.push_frame(output_frame, direction)
```

### 11.3 AI Service Categories

| Category | Provider Count | Key Providers |
|----------|----------------|---------------|
| STT | 19+ | Deepgram, AssemblyAI, Google, Azure, AWS Transcribe, Whisper |
| LLM | 18+ | OpenAI, Anthropic, Google Gemini, Groq, Ollama |
| TTS | 25+ | Cartesia, ElevenLabs, Deepgram Aura, PlayHT, AWS Polly |
| S2S | 5 | OpenAI Realtime, Gemini Live, AWS Nova Sonic |
| Vision | 2+ | Moondream, Google Vision |

### 11.4 Observability System

| Observer | Purpose |
|----------|---------|
| `RTVIObserver` | RTVI protocol event emission |
| `TurnTrackingObserver` | Turn boundary analytics |
| `UserBotLatencyObserver` | TTFA/TTFB measurement |
| `TurnTraceObserver` | OpenTelemetry tracing |

### 11.5 Transport Adapters

| Transport | Class | Protocol |
|-----------|-------|---------|
| Daily.co | `daily.CallClient` | WebRTC |
| LiveKit | `livekit.rtc.Room` | WebRTC |
| FastAPI | WebSocket handler | WS |
| Local | File/Mic I/O | PCM |

---

## 12. LiveKit Agents -- Room/Track/Plugin System

Source: [LiveKit Agents](https://github.com/livekit/agents), [LiveKit Docs](https://docs.livekit.io/agents/)

### 12.1 Room Architecture

Agents join LiveKit rooms as full WebRTC participants. SFU (Selective Forwarding Unit) routes media only to necessary participants -- horizontal scaling without media processing overhead.

```
AgentServer
  |-- WorkerPool
        |-- Worker 1 -> Room A
        |      |-- AudioTrack (subscribe: user input)
        |      |-- AudioTrack (publish: TTS output)
        |-- Worker 2 -> Room B
```

### 12.2 RoomIO Subsystems

| Subsystem | Interface | Purpose |
|-----------|-----------|---------|
| Input stream | `AudioInput` | Subscribe to user track, buffer pre-connect audio |
| Output stream | `AudioOutput` | Publish TTS audio as track |
| Transcript sync | `TextOutput` | Sync STT transcripts with audio playback |
| Participant lifecycle | event hooks | Handle join/leave, track subscribe/unsubscribe |

### 12.3 Plugin Architecture

```python
from livekit.plugins import openai, silero, deepgram, cartesia, turn_detector

agent = VoicePipelineAgent(
    vad=silero.VAD.load(),
    stt=deepgram.STT(),
    llm=openai.LLM(model="gpt-4o"),
    tts=cartesia.TTS(),
    turn_detector=turn_detector.EOUModel(),
)
```

Changing a provider = one line change. No pipeline rewiring.

### 12.4 Silero VAD Plugin Configuration

```python
silero.VAD.load(
    min_speech_duration=0.05,       # seconds; min duration to classify as speech
    min_silence_duration=0.55,      # seconds; silence before speech end declared
    prefix_padding_duration=0.5,    # seconds; audio before speech onset kept
    max_buffered_speech=60.0,       # seconds; max buffer before force-flush
    activation_threshold=0.5,       # 0.0-1.0; Silero probability threshold
    sample_rate=16000,              # 8000 or 16000 Hz only
    # deactivation defaults to max(activation_threshold - 0.15, 0.01)
)
```

### 12.5 EOU (End-of-Utterance) Semantic Turn Detection

LiveKit's EOU model is a 135M-parameter transformer (SmolLM v2 base) fine-tuned for turn completion prediction. Uses sliding window of last 4 conversation turns.

Recommended combination: Silero VAD + EOU model together for best accuracy.

Source: [LiveKit EOU blog](https://blog.livekit.io/using-a-transformer-to-improve-end-of-turn-detection)

---

## 13. VAD Cross-Provider Reference

Source: [Picovoice VAD Comparison 2026](https://picovoice.ai/blog/best-voice-activity-detection-vad/), [Silero VAD](https://github.com/snakers4/silero-vad)

### 13.1 Accuracy Benchmark (at 5% FPR)

| Provider | TPR @ 5% FPR | Architecture | Latency/Frame | Open Source |
|----------|-------------|-------------|--------------|-------------|
| Cobra (Picovoice) | 98.9% | DNN on-device | <1ms CPU | No |
| Silero VAD | 87.7% | PyTorch DNN | <1ms CPU (30ms) | Yes |
| WebRTC VAD (Google) | 50.0% | GMM signal processing | <0.5ms CPU | Yes |
| TEN VAD | N/A | DNN, 10-16ms frames | low-latency | Yes |

At 5% FPR: WebRTC misses 1 in 2 speech frames; Silero misses 1 in 8; Cobra misses 1 in 100.

### 13.2 Configuration Snippets

**WebRTC VAD:**
```python
import webrtcvad
vad = webrtcvad.Vad(aggressiveness=3)  # 0=least, 3=most aggressive
# frame: 160/320/480 samples at 16kHz (10/20/30ms)
```

**Silero VAD:**
```python
model, utils = torch.hub.load('snakers4/silero-vad', 'silero_vad', onnx=True)
threshold = 0.5            # speech probability threshold (0.0-1.0)
sampling_rate = 16000      # 8000 or 16000 only
window_size_samples = 512  # frame size in samples
```

**OpenAI server_vad:**
```json
{"type": "server_vad", "threshold": 0.5, "silence_duration_ms": 500}
```

**OpenAI semantic_vad:**
```json
{"type": "semantic_vad", "eagerness": "auto"}
```

**LiveKit Silero:**
```python
silero.VAD.load(activation_threshold=0.5, min_silence_duration=0.55)
```

---

## 14. Moshi S2S Architecture -- Deep Dive

Source: [Moshi arXiv:2410.00037](https://arxiv.org/abs/2410.00037), [Kyutai GitHub](https://github.com/kyutai-labs/moshi)

### 14.1 Architecture Overview

Full-duplex S2S foundation model -- no cascading pipeline. Simultaneously listens and speaks, modeling both user and system audio as parallel streams.

```
User audio stream (continuous)
  + System audio stream (Moshi's own previous speech)
         |
    Mimi Codec (encoder) -- 80ms frames, 12.5Hz
         |
    Temporal Transformer (7B, 32L) -- temporal dependencies
         |
    Depth Transformer (6L) -- inter-codebook deps per timestep
         |
    Inner Monologue -- text token BEFORE audio tokens
         |
    Mimi Codec (decoder) -> Audio output
```

### 14.2 Temporal Transformer Specs

| Parameter | Value |
|-----------|-------|
| Layers | 32 |
| Attention heads | 32 |
| Model dimension | 4,096 |
| MLP dimension | 11,264 |
| Context length | 4,096 tokens |
| Position encoding | RoPE |
| Normalization | RMSNorm |
| Attention | FlashAttention |
| Activation | Gated Linear Units (SiLU) |
| Initialized from | Helium 7B text LM |

### 14.3 Depth Transformer Specs

| Parameter | Value |
|-----------|-------|
| Layers | 6 |
| Attention heads | 16 |
| Model dimension | 1,024 |
| MLP dimension | 4,096 |
| Function | Inter-codebook dependency per timestep |

### 14.4 Mimi Codec Architecture

| Component | Detail |
|-----------|--------|
| Architecture | SeaNet (causal convolutions) |
| Encoder strides | 4 blocks: factors 4, 5, 6, 8 |
| Bottleneck | 8 transformer layers before + after quantization |
| Quantization | Split RVQ: 1 semantic VQ (WavLM-distilled) + 7 acoustic quantizers |
| Codebook size | 2,048 entries each |
| Bitrate | 1.1 kbps at 12.5Hz |
| Frame size | 80ms |
| Training | Adversarial-only (feature + discriminator losses) |

### 14.5 Inner Monologue Mechanism

Per-frame prediction sequence: `[text_token] -> [semantic_codebook] -> [acoustic_codebooks 1..7]`

Text tokens are Whisper-transcribed, time-aligned to 12.5Hz, and predicted before audio tokens at each timestep. Enables: improved factuality, zero-shot streaming ASR + TTS, real-time compatible generation.

### 14.6 Dual-Stream Modeling

| Dimension | Detail |
|-----------|--------|
| Streams | 2: user audio + Moshi audio |
| Representation | Separate semantic + acoustic sequences per stream |
| Turn-taking | No explicit speaker boundaries -- overlap/interruption natural |
| Training | Diarized single-speaker audio + Fisher dataset (true separate channels) |

### 14.7 Latency Profile

| Stage | Latency |
|-------|---------|
| Mimi frame size | 80ms |
| Acoustic delay | 80ms |
| Theoretical E2E | 160ms |
| Practical E2E (L4 GPU) | 200ms |
| Human conversation avg | 230ms (10 languages) |

### 14.8 Moshi vs Alternatives

| Dimension | Moshi | OpenAI Realtime | Cascading Pipeline |
|-----------|-------|----------------|-------------------|
| Architecture | Native dual-stream | Codec-based tokens | Modular STT+LLM+TTS |
| Latency | 200ms | ~300ms | 500-1500ms |
| Full-duplex | Yes | Yes | No (half-duplex) |
| LLM flexibility | Fixed (Helium-7B) | Fixed (gpt-4o-realtime) | Any LLM |
| Tool calling | Limited | Native | Full |
| Open source | Yes (Kyutai) | No | Yes (components) |
| Customizable voice | No | Yes (voice param) | Yes (TTS provider) |

---

## 15. Voice-Agent Architecture Decision Tree (Extended)

```
LATENCY REQUIREMENT?
  <200ms -> Moshi (200ms practical, full-duplex, open source)
  <300ms -> OpenAI Realtime (gpt-4o-realtime, native tool calls)
  <500ms -> Pipecat or LiveKit cascading (modular, any LLM)
  flexible -> standard cascading (maximum control)

FULL-DUPLEX NEEDED?
  Yes -> Moshi or OpenAI Realtime
  No  -> Cascading pipeline

TOOL CALLING NEEDED?
  Yes -> OpenAI Realtime (native) OR cascading (full)
  No  -> Moshi OK

OPEN SOURCE REQUIRED?
  Yes -> Moshi (Kyutai) or Pipecat + Silero + open LLM
  No  -> Any provider

FRAMEWORK CHOICE:
  Pipecat               LiveKit
  - 25+ TTS providers   - Room/SFU model
  - 19+ STT providers   - EOU semantic turn detection
  - Frame-based pipes   - Multi-party voice rooms
  - Observer metrics    - Managed infra option
  - Daily/LK/WS/local   - Worker pool scaling

VAD SELECTION:
  Accuracy priority  -> Cobra VAD (98.9% TPR)
  Speed + open src   -> Silero VAD (87.7% TPR, <1ms)
  Zero-dependency    -> WebRTC VAD (GMM, 50% TPR, fastest)
  OpenAI Realtime    -> server_vad (energy) or semantic_vad (transformer)
  LiveKit agents     -> Silero + EOU model (recommended combo)

TRANSPORT:
  Browser  -> WebRTC (ICE/DTLS/RTP, Opus)
  Server   -> WebSocket (persistent, bidirectional)
  Phone    -> SIP (PSTN gateway, IVR fallback)
  Scale    -> LiveKit SFU (selective forwarding, horizontal scale)
```

---

