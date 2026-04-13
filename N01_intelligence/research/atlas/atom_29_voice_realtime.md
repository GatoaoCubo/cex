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

## 12. OpenAI Realtime API v2 -- Complete Event Reference

Source: [Azure OpenAI Realtime Audio Reference](https://learn.microsoft.com/en-us/azure/foundry/openai/realtime-audio-reference) | [OpenAI Client Events](https://platform.openai.com/docs/api-reference/realtime-client-events)

### 12.1 Client Events (11 total)

| Event | Description |
|-------|-------------|
| `session.update` | Update session default config (model, instructions, VAD mode, tools). Voice field immutable after creation. |
| `input_audio_buffer.append` | Append base64-encoded audio bytes to input buffer. No server ack. Max 15 MiB per event. |
| `input_audio_buffer.commit` | Commit input buffer as new user message item. In server VAD mode this is automatic. |
| `input_audio_buffer.clear` | Discard all bytes in the input buffer. Server responds with input_audio_buffer.cleared. |
| `output_audio_buffer.clear` | (WebRTC only) Clear output audio buffer. Must be preceded by response.cancel. |
| `conversation.item.create` | Insert a new message, function call, or function call response into conversation context. |
| `conversation.item.retrieve` | Retrieve server representation of a specific item (e.g., post-VAD noise-cleaned audio). |
| `conversation.item.delete` | Remove an item from conversation history. |
| `conversation.item.truncate` | Truncate an assistant audio item to sync server context with client playback state on barge-in. |
| `response.create` | Instruct server to generate a response. Supports per-response instruction/temperature override. |
| `response.cancel` | Cancel an in-progress response. Server responds with response.cancelled. |

### 12.2 Server Events (28 total)

**Session / Conversation lifecycle:**

| Event | Description |
|-------|-------------|
| `session.created` | First event on new connection. Returns session with default config. |
| `session.updated` | Returned after session.update. Includes full effective config. |
| `conversation.created` | One conversation per session. Returned immediately after session creation. |
| `conversation.item.created` | Item created (by response generation, buffer commit, or client create). |
| `conversation.item.retrieved` | Response to conversation.item.retrieve. |
| `conversation.item.deleted` | Client deleted an item. Syncs client/server history. |
| `conversation.item.truncated` | Audio item was truncated by client barge-in event. |
| `error` | Client or server error with type, code, and human-readable message. |

**Input audio buffer:**

| Event | Description |
|-------|-------------|
| `input_audio_buffer.speech_started` | (server VAD mode) Speech detected in buffer. |
| `input_audio_buffer.speech_stopped` | (server VAD mode) End of speech detected. |
| `input_audio_buffer.committed` | Buffer committed -- either by client or auto by server VAD. |
| `input_audio_buffer.cleared` | Buffer cleared by client input_audio_buffer.clear. |
| `conversation.item.input_audio_transcription.completed` | ASR transcription of committed audio complete. |
| `conversation.item.input_audio_transcription.failed` | Transcription of user audio failed. |

**Output audio buffer (WebRTC only):**

| Event | Description |
|-------|-------------|
| `output_audio_buffer.started` | Server begins streaming audio to client. |
| `output_audio_buffer.stopped` | Output buffer fully drained, no more audio. |
| `output_audio_buffer.cleared` | Output cleared (user interrupted or client sent output_audio_buffer.clear). |

**Response streaming:**

| Event | Description |
|-------|-------------|
| `response.created` | New response created, state = in_progress. |
| `response.done` | Response complete (all items finalized). |
| `response.output_item.added` | New item created during generation. |
| `response.output_item.done` | Item done streaming. |
| `response.content_part.added` | New content part added to assistant message. |
| `response.content_part.done` | Content part streaming complete. |
| `response.audio.delta` | Incremental audio chunk. |
| `response.audio.done` | Audio generation done. |
| `response.audio_transcript.delta` | Incremental transcript of generated audio. |
| `response.audio_transcript.done` | Transcript of generated audio complete. |
| `response.text.delta` | Incremental text (for text-mode responses). |
| `response.text.done` | Text response complete. |
| `response.function_call_arguments.delta` | Incremental function call arguments. |
| `response.function_call_arguments.done` | Function call arguments complete. |
| `rate_limits.updated` | Rate limit state at start of response (tokens/requests remaining). |

### 12.3 Turn Detection Modes

| Mode | Key Config | Behavior |
|------|------------|----------|
| server_vad | type: server_vad, threshold: 0.5, silence_duration_ms: 500 | Server auto-detects speech start/stop, commits buffer, triggers response |
| semantic_vad | type: semantic_vad, eagerness: auto | Server waits for semantic completeness, not just silence |
| none | turn_detection: null | Client manually commits audio and calls response.create |

---

## 13. Pipecat Frame-Based Pipeline Architecture

Source: [Pipecat Pipeline Guide](https://docs.pipecat.ai/guides/learn/pipeline) | [Frame API Reference](https://reference-server.pipecat.ai/en/stable/api/pipecat.frames.frames.html)

### 13.1 Frame Taxonomy

Everything in Pipecat is a Frame -- audio, text, control signals, errors. Three base classes:

| Frame Class | Queueing | Examples | When to use |
|-------------|----------|---------|-------------|
| SystemFrame | Bypasses queue -- immediate | UserStartedSpeakingFrame, InterruptionFrame, ErrorFrame, InputAudioRawFrame | Urgent signals |
| DataFrame | Queued, ordered | OutputAudioRawFrame, TextFrame, TranscriptionFrame, LLMTextFrame | Normal data flow |
| ControlFrame | Queued, ordered | EndFrame, TTSStartedFrame, LLMFullResponseStartFrame | Pipeline lifecycle |

### 13.2 FrameProcessor Pattern

Processors do not consume frames -- they push them forward, enabling multiple processors on the same stream:

```python
class TranscriptionLogger(FrameProcessor):
    async def process_frame(self, frame, direction):
        await super().process_frame(frame, direction)
        if isinstance(frame, TranscriptionFrame):
            print(f"Transcription: {frame.text}")
        await self.push_frame(frame, direction)
```

### 13.3 Bidirectional Flow

- DOWNSTREAM: Transport.input() -> VAD -> STT -> LLM -> TTS -> Transport.output()
- UPSTREAM: Transport.output() -> (interruption events) -> VAD -> ...

SystemFrame travels both directions immediately. DataFrame/ControlFrame travel downstream only.

### 13.4 Available Transports

Daily (WebRTC), WebSocket, Local (ALSA/PyAudio), FastAPI WebSocket, Twilio Media Streams, RTVI.

---

## 14. LiveKit Agents Framework -- Room / Track / Plugin System

Source: [LiveKit Agents Docs](https://docs.livekit.io/agents/) | [AgentSession Reference](https://docs.livekit.io/agents/build/sessions/)

### 14.1 AgentSession Lifecycle Phases

| Phase | Description |
|-------|-------------|
| initializing | Setup; no audio/video processing |
| starting | I/O connections established; agent transitions to listening |
| running | Active; processing input and generating responses |
| closing | Graceful shutdown; speech drains, I/O cleanup |

### 14.2 Plugin Architecture (Swappable Model Slots)

Each component is a swappable plugin -- swap with a single line change:

```python
session = AgentSession(
    vad=silero.VAD.load(),
    stt=deepgram.STT(model="nova-3"),
    llm=openai.LLM(model="gpt-4o"),
    tts=cartesia.TTS(voice_id="...")
)
```

Plugin slots: vad, stt, llm, tts. Accepts string shorthand ("deepgram/nova-3:en") or custom impl.

### 14.3 RoomIO -- Track Management

RoomIO bridges AgentSession and LiveKit rtc.Room:
- Input stream management (audio/video track subscriptions)
- Output stream management
- Transcript synchronization
- Pre-connect audio buffering
- Participant lifecycle tracking

Default: links to first participant who joins.

### 14.4 Audio Pipeline Flow

```
User audio (WebRTC) -> RoomIO.input -> VAD -> STT -> LLM -> TTS -> RoomIO.output -> WebRTC track
```

### 14.5 Supported Plugins (2025)

| Category | Plugins |
|----------|---------|
| VAD | Silero, WebRTC VAD |
| STT | Deepgram, OpenAI Whisper, AssemblyAI, Google STT |
| LLM | OpenAI, Anthropic, Google Gemini, Mistral, Groq |
| TTS | Cartesia, ElevenLabs, OpenAI TTS, Google TTS, Azure TTS |
| Realtime S2S | OpenAI Realtime, Gemini Multimodal Live |

---

## 15. VAD Provider Deep Comparison

Sources: [Picovoice VAD Benchmark 2025](https://picovoice.ai/blog/best-voice-activity-detection-vad-2025/) | [LiveKit Silero VAD](https://docs.livekit.io/agents/logic/turns/vad/)

### 15.1 Performance Benchmark (ROC Curve)

| VAD Engine | TPR @ 5% FPR | TPR @ 1% FPR | Notes |
|------------|-------------|-------------|-------|
| WebRTC VAD | Baseline | ~45% | Rule-based, adaptive noise threshold |
| Silero VAD | 4x fewer errors vs WebRTC | 80.4% | Neural, 6000+ language corpus |
| Cobra (Picovoice) | 12x fewer errors vs Silero | 95% | Commercial, on-device |

At 25% FPR, WebRTC TPR exceeds Silero -- Silero is more conservative at strict thresholds.

### 15.2 Silero VAD Configuration Parameters (LiveKit plugin)

| Parameter | Default | Effect |
|-----------|---------|--------|
| activation_threshold | 0.5 | Higher = more conservative (fewer false positives) |
| min_speech_duration | 0.05s | Minimum duration to start a new chunk |
| min_silence_duration | 0.55s | Silence window to end an utterance |
| prefix_padding_duration | 0.5s | Audio prepended to each segment |
| max_buffered_speech | 60.0s | Max buffer before forced commit |
| sample_rate | 16000 | 8000 or 16000 Hz |
| force_cpu | true | Disable GPU inference |

### 15.3 OpenAI Realtime VAD Config Examples

```json
// server_vad
{"type": "server_vad", "threshold": 0.5, "prefix_padding_ms": 300, "silence_duration_ms": 500, "create_response": true}

// semantic_vad (eagerness: low | medium | high | auto)
{"type": "semantic_vad", "eagerness": "auto"}
```

### 15.4 VAD Selection Guide

| Use Case | Recommended VAD |
|----------|----------------|
| Browser voice agents | WebRTC VAD (built-in, zero dependency) |
| Production cascading | Silero VAD (best open-source accuracy) |
| Embedded / on-device | Cobra (Picovoice) -- highest accuracy |
| OpenAI Realtime direct | server_vad or semantic_vad |
| Noisy call center | activation_threshold 0.6-0.8, min_silence_duration >= 0.8s |

---

## 16. Moshi S2S Architecture (Kyutai)

Sources: [Moshi Paper arXiv:2410.00037](https://arxiv.org/abs/2410.00037) | [Moshi GitHub](https://github.com/kyutai-labs/moshi) | [Moshi on HuggingFace](https://huggingface.co/docs/transformers/model_doc/moshi)

### 16.1 Core Components

| Component | Description |
|-----------|-------------|
| Helium | Text LLM backbone (7B parameters) |
| Mimi codec | Neural audio codec -- 24kHz audio, 12.5Hz representation, 1.1 kbps, 80ms latency |
| Inner Monologue | Text token predicted before each audio frame (improves factuality) |
| Dual-stream | Separate parallel streams for agent speech and user speech -- full-duplex |

### 16.2 Inner Monologue Per-Frame Prediction

Per-frame sequence: [text token] -> [audio tier 0] -> [audio tier 1] -> ... -> [audio tier N]

Benefits:
- Improves linguistic quality and factuality of generated speech
- Enables derived streaming TTS and ASR (text-audio alignment is explicit)
- Derived streaming ASR via delay between text and audio token prediction

### 16.3 Streaming Performance

| Metric | Value |
|--------|-------|
| Mimi frame size | 80ms |
| Acoustic delay | 80ms |
| Theoretical TTFA | 160ms |
| Practical TTFA | ~200ms (L4 GPU) |
| Mimi bandwidth | 1.1 kbps |
| Sample rate | 24 kHz |

### 16.4 Dual-Stream Model (Full-Duplex)

```
Time ->
Agent stream:  [A_0][A_1][A_2]...
User stream:   [U_0][U_1][U_2]...
Inner mono.:   [T_0][T_1][T_2]...
```

Agent can listen while speaking -- natural overlap without hard turn boundaries.

### 16.5 Moshi vs OpenAI Realtime vs Gemini Live

| Dimension | Moshi | OpenAI Realtime | Gemini Live |
|-----------|-------|-----------------|-------------|
| Latency | ~200ms | ~300-500ms | ~200-400ms |
| Full-duplex | Yes (native) | Partial (barge-in) | Yes |
| Turn model | No turns (streaming) | server_vad / semantic | Server VAD |
| Open source | Yes (weights on HF) | No | No |
| Tool calling | Limited | Full function calling | Full function calling |
| Codec | Mimi 1.1kbps | Opus / PCM16 | Opus |

---

## 17. Architecture Decision Tree (Extended)

```
START: "I want a voice agent"
         |
Q1: Latency requirement?
    < 200ms --> Q2: Open source needed?
                  Yes --> Moshi (full-duplex, self-hosted, ~200ms)
                  No  --> OpenAI Realtime (semantic_vad) or Gemini Live
    < 500ms --> Q3: Framework?
                  Python-first, modular --> LiveKit Agents (swappable plugins)
                  Full frame control   --> Pipecat (SystemFrame/DataFrame/ControlFrame)
                  Telephony / SIP      --> LiveKit + SIP or Twilio + Pipecat
    > 500ms OK --> Standard: Deepgram + GPT-4o + Cartesia, any transport

Q4: Transport?
    Browser     --> WebRTC (LiveKit or Daily + Pipecat)
    Server      --> WebSocket
    Phone/PSTN  --> SIP trunk (Twilio / Vonage)
    Multi-modal --> LiveKit (video + audio + data channels)

Q5: VAD strategy?
    OpenAI Realtime --> server_vad or semantic_vad (built-in)
    Pipecat/LiveKit --> Silero VAD (best open-source accuracy)
    Embedded/device --> Cobra (Picovoice) or Silero force_cpu=True
    Noisy env       --> activation_threshold >= 0.6, min_silence >= 0.8s
```

---

## 18. Glossary Additions

| Term | Category | Definition |
|------|----------|------------|
| Frame | Pipecat | Data container flowing through FrameProcessor pipeline |
| SystemFrame | Pipecat | Immediate-bypass frame for urgent signals (interruptions, errors) |
| DataFrame | Pipecat | Queued frame for ordered data (audio, text, transcripts) |
| FrameProcessor | Pipecat | Base class for pipeline stages; inspects and forwards frames |
| RoomIO | LiveKit | Bridge between AgentSession and LiveKit rtc.Room track management |
| AgentSession | LiveKit | Top-level orchestrator for voice AI app lifecycle |
| Inner Monologue | Moshi | Text token predicted before each audio frame, improving factuality |
| Mimi | Moshi | Neural audio codec; 24kHz -> 12.5Hz, 1.1kbps, 80ms latency |
| Full-duplex | Architecture | Simultaneous send and receive -- no hard turn boundaries |
| Semantic VAD | OpenAI | VAD that waits for semantic completeness, not just silence |
| server_vad | OpenAI | Server-side silence-based VAD in Realtime API |
| AUC | Metric | Area Under ROC Curve -- vendor-neutral VAD accuracy metric |
| TPR | Metric | True Positive Rate -- % of speech correctly detected |
| FPR | Metric | False Positive Rate -- % of silence wrongly classified as speech |

---

## 19. References (Full Updated List)

- [OpenAI Realtime API Reference](https://platform.openai.com/docs/api-reference/realtime)
- [OpenAI Realtime Client Events](https://platform.openai.com/docs/api-reference/realtime-client-events)
- [OpenAI Realtime Server Events](https://platform.openai.com/docs/api-reference/realtime-server-events)
- [Azure OpenAI Realtime Audio Reference](https://learn.microsoft.com/en-us/azure/foundry/openai/realtime-audio-reference)
- [Pipecat Pipeline Architecture](https://docs.pipecat.ai/guides/learn/pipeline)
- [Pipecat Frame API Reference](https://reference-server.pipecat.ai/en/stable/api/pipecat.frames.frames.html)
- [LiveKit Agents Introduction](https://docs.livekit.io/agents/)
- [LiveKit AgentSession Docs](https://docs.livekit.io/agents/build/sessions/)
- [LiveKit Silero VAD Plugin](https://docs.livekit.io/agents/logic/turns/vad/)
- [Picovoice VAD Benchmark 2025](https://picovoice.ai/blog/best-voice-activity-detection-vad-2025/)
- [Silero VAD GitHub](https://github.com/snakers4/silero-vad)
- [Moshi Paper arXiv:2410.00037](https://arxiv.org/abs/2410.00037)
- [Moshi GitHub kyutai-labs](https://github.com/kyutai-labs/moshi)
- [Moshi on HuggingFace](https://huggingface.co/docs/transformers/model_doc/moshi)
- [Hume EVI Documentation](https://docs.hume.ai)
- [Deepgram API Reference](https://developers.deepgram.com)
- [Cartesia TTS SDK](https://cartesia.ai)
