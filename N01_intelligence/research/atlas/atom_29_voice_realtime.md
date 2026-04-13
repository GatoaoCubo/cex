---
id: atom_29_voice_realtime
kind: knowledge_card
pillar: P01
title: "Voice & Realtime Agent -- Complete Vocabulary and Architecture Atlas"
version: 0.1.0
quality: 8.8
tags: [voice, realtime, speech-to-speech, VAD, WebRTC, WebSocket, TTS, STT, prosody, emotion, streaming, audio, telephony, SIP]
sources:
  - https://developers.openai.com/api/docs/guides/realtime
  - https://developers.openai.com/api/docs/guides/realtime-websocket
  - https://developers.openai.com/api/docs/guides/realtime-conversations
  - https://developers.openai.com/api/docs/guides/voice-agents
  - https://dev.hume.ai/docs/speech-to-speech-evi/overview
  - https://elevenlabs.io/docs/eleven-agents/overview
  - https://ai.google.dev/gemini-api/docs/live-api
  - https://hamming.ai/resources/best-voice-agent-stack
  - https://docs.cartesia.ai/build-with-cartesia/tts-models/latest
  - https://deepgram.com/learn/voice-agent-api-generally-available
  - https://github.com/fixie-ai/ultravox
  - https://github.com/kyutai-labs/moshi
  - https://docs.pipecat.ai/server/services/s2s/openai
  - https://docs.livekit.io/agents/models/realtime/plugins/openai/
  - https://cartesia.ai/sonic
date: 2026-04-13
domain: voice-realtime-agents
---

# Voice & Realtime Agent -- Complete Vocabulary and Architecture Atlas

## 1. Domain Overview

Voice and realtime agents represent the convergence of speech processing, large
language models, and low-latency streaming infrastructure. The field has rapidly
evolved from cascading STT-LLM-TTS pipelines to native speech-to-speech (S2S)
models that reason directly on audio tokens.

**Two fundamental architectures:**

| Architecture | Pipeline | Latency | Tradeoff |
|---|---|---|---|
| Cascading | STT -> LLM -> TTS (3 stages) | 2-4s E2E | Full tool calling, any LLM, mature |
| Speech-to-Speech (S2S) | Audio-in -> Audio-out (1 model) | 200-500ms | Lower latency, limited tool support |
| Hybrid | S2S for greetings, cascade for complex tasks | Variable | Best of both, complex routing |

**Key providers (2025-2026):**

| Provider | Product | Architecture | Key Differentiator |
|---|---|---|---|
| OpenAI | Realtime API (gpt-realtime) | Native S2S | Semantic VAD, function calling during speech |
| Google | Gemini Live API | Native S2S | 70 languages, affective dialog, 30 HD voices |
| Hume AI | EVI (Empathic Voice Interface) | S2S with prosody model | Emotion detection + empathic response |
| ElevenLabs | ElevenAgents | Cascade (proprietary turn-taking) | 5000+ voices, 31 languages, SIP trunk |
| Deepgram | Voice Agent API (Nova-3 + Aura-2) | Cascade (unified API) | Sub-200ms TTFB, domain vocabulary |
| Cartesia | Sonic-3 | TTS component (SSM-based) | 40ms TTFA, State Space Model architecture |
| Fixie AI | Ultravox | Half-cascade (audio-in, text-out) | Open-weight, multimodal projector |
| Kyutai | Moshi | Full S2S (multi-stream) | 160ms theoretical latency, full-duplex |

---

## 2. Transport Layer Vocabulary

### 2.1 WebSocket

| Term | Definition | Context |
|---|---|---|
| **WebSocket (WSS)** | Persistent bidirectional TCP connection over TLS for realtime data exchange | All voice APIs offer WSS; server-to-server preferred |
| **Client event** | JSON message sent from client to server over WebSocket | OpenAI: `session.update`, `input_audio_buffer.append` |
| **Server event** | JSON message sent from server to client over WebSocket | OpenAI: `response.output_audio.delta`, `response.done` |
| **Event-driven protocol** | Bidirectional message exchange without request-response pairing | Realtime APIs define custom event schemas atop WebSocket |
| **Base64-encoded audio** | Binary audio data encoded as ASCII text for JSON transport | WebSocket requires text framing; audio is base64 in JSON payloads |
| **Heartbeat / keepalive** | Periodic ping to prevent connection timeout | WebSocket idle timeout typically 60s-300s |

### 2.2 WebRTC

| Term | Definition | Context |
|---|---|---|
| **WebRTC** | Browser-native protocol for peer-to-peer real-time communication | OpenAI Realtime supports WebRTC for client-side apps |
| **SDP (Session Description Protocol)** | Format describing media capabilities in offer/answer exchange | WebRTC session negotiation: client offers, server answers |
| **ICE (Interactive Connectivity Establishment)** | Protocol for NAT traversal; gathers candidate addresses | Browser ICE agent tests local, server-reflexive, relay candidates |
| **ICE candidate** | A potential network path (host, srflx, relay) for media | Gathered during connection setup, exchanged via signaling |
| **TURN server** | Relay server for media when direct peer connection fails | Required for ~15% of connections behind symmetric NAT |
| **STUN server** | Discovers public IP/port for server-reflexive candidates | Lightweight; fails if symmetric NAT blocks |
| **SFU (Selective Forwarding Unit)** | Server that routes media streams without transcoding | LiveKit, Daily, Twilio use SFUs for voice agent infrastructure |
| **DTLS (Datagram Transport Layer Security)** | Encryption for WebRTC media channels | Mandatory in WebRTC; secures RTP packets |
| **Opus codec** | Royalty-free audio codec (RFC 6716); 6-510 kbit/s, 2.5-60ms frames | Default WebRTC audio codec; adapts to network conditions |
| **Ephemeral token** | Short-lived credential for client-side WebRTC session | OpenAI `/v1/realtime/client_secrets`; avoid exposing API key |

### 2.3 SIP / Telephony

| Term | Definition | Context |
|---|---|---|
| **SIP (Session Initiation Protocol)** | Signaling protocol for VoIP call setup/teardown | ElevenLabs SIP trunk; OpenAI SIP connection |
| **SIP trunk** | Virtual phone line connecting voice agent to PSTN | Enterprise telephony integration |
| **PSTN (Public Switched Telephone Network)** | Traditional phone network | Voice agents bridge PSTN via SIP gateway |
| **IVR (Interactive Voice Response)** | Automated phone menu system | Legacy pattern being replaced by voice agents |
| **G.711 u-law / a-law** | 8kHz, 8-bit audio codecs for telephony | OpenAI supports `g711_ulaw` and `g711_alaw` formats |
| **PCM16** | 16-bit pulse-code modulation, uncompressed audio | Standard interchange format; OpenAI input/output default |
| **RTP (Real-time Transport Protocol)** | Protocol for delivering audio/video over IP | Carries encoded audio between endpoints |

---

## 3. Voice Activity Detection (VAD) & Turn-Taking

### 3.1 VAD Modes

| Term | Definition | Context |
|---|---|---|
| **VAD (Voice Activity Detection)** | Algorithm distinguishing speech from silence/noise | Core component in all voice agents |
| **Semantic VAD** | Uses a semantic classifier to detect utterance completion based on meaning | OpenAI default; detects "I'd like to order..." as incomplete |
| **Server VAD** | Detects end-of-turn via configurable silence duration | OpenAI alternative; simpler but less context-aware |
| **Client-side VAD** | VAD running in browser/app before sending audio to server | Reduces bandwidth; Silero VAD popular open-source option |
| **Push-to-talk (PTT)** | User explicitly signals start/end of speech via button | OpenAI: set `turn_detection: null`, manually commit buffer |
| **Endpointing** | Determining the exact moment a speaker finishes an utterance | Critical for latency; too early = cut-off, too late = lag |
| **Barge-in** | User interrupts model while it is speaking | Gemini, OpenAI, ElevenLabs all support automatic barge-in |

### 3.2 VAD Configuration Parameters (OpenAI)

| Parameter | Type | Definition |
|---|---|---|
| `turn_detection.type` | enum | `semantic_vad` / `server_vad` / `null` (disabled) |
| `threshold` | float | Activity sensitivity level (0.0-1.0) |
| `prefix_padding_ms` | int | Milliseconds of audio to include before detected speech onset |
| `silence_duration_ms` | int | Milliseconds of silence before declaring end-of-turn |
| `semantic_eagerness` | float | How aggressively the model responds (lower = waits longer) |

### 3.3 Turn-Taking

| Term | Definition | Context |
|---|---|---|
| **Turn-taking** | Protocol governing who speaks when in a conversation | Managed by orchestration layer or model itself |
| **Full-duplex** | Both parties can speak simultaneously | Moshi is natively full-duplex; most APIs are half-duplex |
| **Half-duplex** | Only one party speaks at a time; barge-in interrupts model | Standard for OpenAI Realtime, ElevenLabs |
| **Interruption handling** | Canceling model output when user starts speaking | OpenAI: auto-cancels response, truncates audio |
| **conversation.item.truncate** | OpenAI event to trim assistant audio after interruption | Aligns transcript with what user actually heard |
| **End-of-turn detection** | Determining when speaker yields the floor | Hume EVI uses tone-of-voice for state-of-the-art detection |
| **Overlap detection** | Identifying when both speakers talk simultaneously | Moshi handles natively; others treat as interruption |

---

## 4. Audio Buffer & Streaming

### 4.1 Input Audio Buffer (OpenAI Realtime)

| Event / Concept | Definition |
|---|---|
| `input_audio_buffer.append` | Client sends base64-encoded audio chunk to server buffer |
| `input_audio_buffer.commit` | Client finalizes buffered audio as a user message (manual mode) |
| `input_audio_buffer.clear` | Client resets audio buffer (discard uncommitted audio) |
| **15 MB limit** | Maximum size per audio buffer append |
| **Auto-commit** | When VAD enabled, server automatically commits on end-of-turn |

### 4.2 Output Audio Streaming

| Event / Concept | Definition |
|---|---|
| `response.output_audio.delta` | Incremental audio chunk from model (base64-encoded) |
| `response.output_audio_transcript.delta` | Realtime text transcript of model's audio output |
| `response.output_text.delta` | Incremental text output (for text modality) |
| `response.done` | Response generation complete |
| `response.cancel` | Client requests cancellation of in-progress response |
| **Audio playback management** | Client must handle playback, interruption truncation, buffering |

### 4.3 Audio Formats

| Format | Sample Rate | Bit Depth | Use Case |
|---|---|---|---|
| PCM16 (LE) | 16kHz (input) / 24kHz (output) | 16-bit | OpenAI, Gemini default |
| G.711 u-law | 8kHz | 8-bit | Telephony (PSTN) |
| G.711 a-law | 8kHz | 8-bit | Telephony (EU) |
| Opus | 8-48kHz (adaptive) | Variable | WebRTC transport |
| WAV | Variable | Variable | File-based processing |
| MP3 | Variable | Variable | Stored audio output |

---

## 5. Session & Conversation Model

### 5.1 OpenAI Realtime Session

| Term | Definition |
|---|---|
| **Session** | Stateful connection with 60-minute maximum duration |
| `session.update` | Client event to modify session parameters mid-conversation |
| **instructions** | System prompt for the session (voice persona, behavior) |
| **modalities** | Array of enabled I/O types: `["audio", "text"]` |
| **voice** | Output voice selection: `alloy`, `ash`, `marin`, `cedar`, etc. |
| `max_response_output_tokens` | Cap on generated tokens per response |
| `temperature` | Output randomness control (0.0-2.0) |
| **input_audio_transcription** | Config for transcribing user audio (model selection) |
| **noise_reduction** | Server-side noise filtering for input audio |

### 5.2 Conversation Items

| Item Type | Definition |
|---|---|
| `message` | User or assistant text/audio content |
| `function_call` | Model-initiated tool invocation |
| `function_call_output` | Client-provided result of function execution |
| **Content types** | `input_text`, `input_audio`, `input_image`, `text`, `audio` |
| `conversation.item.create` | Client inserts item into conversation history |
| `conversation.item.added` | Server confirms item addition |
| `conversation.item.done` | Item processing complete |
| `response.create` | Client triggers model response generation |

### 5.3 Gemini Live API Session

| Term | Definition |
|---|---|
| **BidiGenerateContent** | Bidirectional streaming RPC for Gemini Live |
| **Session resumption** | Reconnect to interrupted conversation |
| **go_away** | Server signal that session will close soon |
| **Proactive audio** | Model initiates speech without user prompt |
| **Affective dialog** | Model adapts tone to match user's emotional expression |

---

## 6. Function Calling in Voice Context

| Term | Definition | Context |
|---|---|---|
| **Voice function calling** | Model invokes tools during realtime audio conversation | OpenAI gpt-realtime, Gemini Live, ElevenLabs agents |
| **Background function execution** | Tool runs while model continues speaking | gpt-realtime: long-running calls no longer block speech |
| **Parallel function calls** | Multiple tools invoked simultaneously | Standard in OpenAI Realtime; reduces latency |
| **tool_choice** | Controls whether/which tools model can invoke | `auto`, `required`, `none`, or specific function name |
| **tools array** | JSON Schema definitions of available functions | Configured at session level or per-response |
| **System tools** | Platform-provided tools (e.g., ElevenLabs conversation flow control) | Auto-included in LLM tool parameter |
| **Conversation flow tools** | Tools that control agent state (transfer, end call, wait) | ElevenLabs: LLM decides when to invoke |

---

## 7. Prosody, Emotion & Voice Control

### 7.1 Prosody

| Term | Definition | Context |
|---|---|---|
| **Prosody** | Suprasegmental features of speech: pitch, rhythm, stress, intonation | Hume measures; SSML controls; S2S models preserve |
| **Pitch** | Fundamental frequency (F0) of voice | SSML `<prosody pitch="high">` |
| **Rate / Tempo** | Speed of speech delivery | SSML `<prosody rate="slow">` |
| **Volume** | Loudness of speech output | SSML `<prosody volume="loud">` |
| **Emphasis** | Stress on specific words | SSML `<emphasis level="strong">` |
| **Contour** | Pitch variation pattern over an utterance | SSML `<prosody contour="(0%,+20Hz)(50%,-10Hz)">` |
| **Cadence** | Natural rhythm pattern including pauses and pacing | Deepgram Aura replicates human cadences |
| **Disfluencies** | Natural speech fillers: "uh", "um", hesitations | Deepgram Aura generates these for naturalness |

### 7.2 SSML (Speech Synthesis Markup Language)

| Term | Definition |
|---|---|
| **SSML** | W3C XML standard for controlling speech synthesis output |
| `<speak>` | Root element of SSML document |
| `<prosody>` | Controls pitch, rate, volume, contour |
| `<emphasis>` | Adds stress to enclosed text |
| `<break>` | Inserts pause; `time` or `strength` attribute |
| `<say-as>` | Interpret content as date, number, telephone, etc. |
| `<phoneme>` | Specify exact pronunciation via IPA or X-SAMPA |
| `<sub>` | Substitution: read abbreviation as full word |
| `<voice>` | Switch voice within a single utterance |
| `<audio>` | Embed pre-recorded audio clip |
| `mstts:express-as` | Azure extension: emotional style (cheerful, empathy, calm) |

### 7.3 Emotion Detection & Expression

| Term | Definition | Context |
|---|---|---|
| **Expression measures** | Quantified emotional signals per utterance | Hume EVI: scores per sentence |
| **Top-K emotions** | Ranked list of detected emotions with confidence scores | Hume prosody model output |
| **eLLM (Empathic Large Language Model)** | Multimodal LLM that processes language + expression measures | Hume hume-evi-2; guides TTS prosody |
| **Affective computing** | Field of detecting/simulating human emotion via sensors | Academic discipline underlying Hume, Gemini affective dialog |
| **Sentiment analysis (audio)** | Classifying emotional valence from voice signal | Positive/negative/neutral from prosody features |
| **Style tokens** | Learned embeddings representing global speaking style | TTS control mechanism; Tacotron-family |
| **Variance adaptor** | Module controlling pitch, duration, energy in TTS | FastSpeech2 architecture component |
| **Steerable TTS** | TTS that accepts natural-language style instructions | GPT-4o-mini-TTS: "speak warmly and slowly" |

---

## 8. Speech-to-Speech (S2S) Model Architecture

### 8.1 Architecture Patterns

| Pattern | Description | Examples |
|---|---|---|
| **Cascading (STT -> LLM -> TTS)** | Three discrete stages; text as intermediary | Deepgram Nova + GPT-4 + Aura; Pipecat default |
| **Half-cascade (audio-in, text-out)** | Audio encoder feeds LLM directly; TTS separate | Ultravox (multimodal projector -> LLM -> text) |
| **Native S2S** | Single model ingests and emits audio tokens directly | OpenAI gpt-realtime, Moshi |
| **Codec-based S2S** | Neural audio codec compresses speech to discrete tokens | Moshi/Mimi, SpeechGPT, AudioLM |

### 8.2 Key S2S Models

| Model | Org | Architecture | Latency | Key Innovation |
|---|---|---|---|---|
| **gpt-realtime** | OpenAI | Native multimodal | ~300ms | Semantic VAD + parallel function calling |
| **Gemini Live** | Google | Native multimodal | ~250ms | Affective dialog, 70 languages, proactive audio |
| **Moshi** | Kyutai | Multi-stream codec LM | 160-200ms | Full-duplex, dual audio stream, Mimi codec |
| **Ultravox** | Fixie AI | Multimodal projector | ~300ms | Open-weight, extends any LLM with audio input |
| **hume-evi-2** | Hume AI | S2S with prosody model | ~300ms | Emotion-aware generation, expression measures |

### 8.3 Neural Audio Codecs

| Term | Definition | Context |
|---|---|---|
| **Neural audio codec** | NN that compresses audio to discrete tokens at low bitrate | Enables LLM-style generation over audio |
| **Mimi** | Kyutai's streaming neural audio codec with residual quantization | Used by Moshi; 160ms frame size |
| **EnCodec** | Meta's neural audio codec (predecessor to Mimi) | Foundation for several S2S systems |
| **Residual Vector Quantization (RVQ)** | Multi-level quantization for progressive audio quality | Codecs use 4-16 RVQ levels |
| **Audio tokens** | Discrete symbolic representation of audio segments | LLM generates audio tokens; vocoder synthesizes |
| **Vocoder / Unit vocoder** | Converts discrete tokens back to continuous audio waveform | Final stage in codec-based S2S |
| **State Space Model (SSM)** | Alternative to Transformer for sequence modeling; O(n) inference | Cartesia Sonic uses SSM for 40ms TTFA |

---

## 9. Latency Metrics

| Metric | Full Name | Definition | Target |
|---|---|---|---|
| **TTFB** | Time to First Byte | Server response start after request | < 200ms (TTS) |
| **TTFA** | Time to First Audio | First playable audio chunk | Cartesia: 40ms |
| **TTFW** | Time to First Word | First intelligible word in response | < 500ms |
| **TTFT** | Time to First Token | LLM emits first token after prompt | Gemini Flash: ~300ms |
| **E2E latency** | End-to-End latency | User stops speaking -> first response audio | Cascade: 2-4s; S2S: 200-500ms |
| **P50 / P95 / P99** | Percentile latency | Distribution-based reliability metrics | P99 matters for user experience |
| **Round-trip latency** | Total audio-in to audio-out time | Deepgram stack: < 3000ms |

---

## 10. Voice Agent Frameworks & Orchestration

### 10.1 Frameworks

| Framework | Type | Key Concept | Transport |
|---|---|---|---|
| **Pipecat** | Open-source (Daily) | Frame-based streaming pipeline | WebRTC via Daily |
| **LiveKit Agents** | Open-source | Plugin-based agent rooms | WebRTC via LiveKit SFU |
| **Vapi** | Managed platform | Declarative agent config | WebRTC / SIP |
| **Retell** | Managed platform | Low-code voice agents | WebSocket / phone |
| **OpenAI Agents SDK** | SDK | RealtimeAgent + VoicePipeline | WebRTC / WebSocket |

### 10.2 Pipecat Vocabulary

| Term | Definition |
|---|---|
| **Frame** | Typed data unit in Pipecat pipeline (AudioFrame, TextFrame, ImageFrame) |
| **Processor** | Pipeline stage that transforms frames |
| **UserStartedSpeakingFrame** | VAD event indicating speech onset |
| **UserStoppedSpeakingFrame** | VAD event indicating speech offset |
| **BotSpeakingFrame** | Agent audio output frame |
| **Pipeline** | Ordered chain of processors: VAD -> STT -> LLM -> TTS -> output |
| **Transport** | Media I/O layer (Daily, WebSocket, local audio) |

### 10.3 LiveKit Vocabulary

| Term | Definition |
|---|---|
| **Room** | Virtual space where participants exchange media |
| **Participant** | User or agent connected to a room |
| **Track** | Individual media stream (audio, video) |
| **Agent Worker** | Server process hosting voice agent logic |
| **Plugin** | Modular component (STT, TTS, LLM) in agent pipeline |
| **Selective Forwarding** | SFU routes streams without transcoding |

---

## 11. STT (Speech-to-Text) Vocabulary

| Term | Definition | Context |
|---|---|---|
| **ASR (Automatic Speech Recognition)** | Converting spoken audio to text | Industry term; STT is the product term |
| **Streaming STT** | Incremental transcription as audio arrives | Required for realtime; vs. batch transcription |
| **WER (Word Error Rate)** | Percentage of incorrectly transcribed words | Deepgram Nova-3: 6.84% WER benchmark |
| **Interim results / partial transcripts** | Preliminary transcription before utterance complete | Enables low-latency downstream processing |
| **Endpointing (STT)** | Detecting end of utterance to finalize transcript | Distinct from VAD; semantic vs. silence-based |
| **Speaker diarization** | Identifying which speaker said what | Multi-speaker scenarios |
| **Confidence score** | Per-word or per-segment reliability metric | Used for fallback/retry logic |
| **Custom vocabulary / keywords** | Domain-specific terms boosted in recognition | Medical, legal, financial terminology |
| **Code-switching** | Speaker alternates between languages mid-utterance | Multilingual STT challenge |
| **Whisper** | OpenAI's open-source ASR model | Foundational; many providers fine-tune variants |
| **gpt-4o-transcribe** | OpenAI's latest STT model (2025) | Outperforms Whisper on benchmarks |

---

## 12. TTS (Text-to-Speech) Vocabulary

| Term | Definition | Context |
|---|---|---|
| **Speech synthesis** | Generating spoken audio from text | Academic term for TTS |
| **Voice cloning** | Reproducing a specific speaker's voice from samples | ElevenLabs, Cartesia: few-second samples |
| **Zero-shot voice cloning** | Cloning from a single audio sample without fine-tuning | Codec models enable this |
| **Voice library** | Catalog of pre-built synthetic voices | ElevenLabs: 5000+ voices |
| **HD voices** | High-definition voice models with richer prosody | Gemini: 30 HD voices |
| **Streaming TTS** | Audio chunks emitted as text is generated | Required for realtime; vs. full-utterance synthesis |
| **TTFA (Time to First Audio)** | Latency from text input to first audio chunk | Cartesia Sonic-3: 40ms |
| **Steerable TTS** | Style controlled via natural language instructions | GPT-4o-mini-TTS: "speak in a whisper" |
| **Voice design** | Creating custom voices via parameter adjustment | Hume: voice design tool |
| **Multilingual TTS** | Single model synthesizes multiple languages | Gemini: 70 languages; Sonic-3: 15 languages |
| **Expressiveness** | Range of emotional/stylistic variation in output | Cartesia: fine-grained volume, speed, emotion control |

---

## 13. Safety, Guardrails & Moderation

| Term | Definition | Context |
|---|---|---|
| **Audio moderation** | Detecting harmful content in voice input/output | Distinct from text moderation; audio-native |
| **Voice persona guardrails** | Constraining agent to stay in character | System prompt + instruction hierarchy |
| **Prompt injection (voice)** | User speaks adversarial instructions to hijack agent | Emerging attack vector for voice agents |
| **Instruction hierarchy** | Priority ordering: system > developer > user instructions | OpenAI voice agents follow standard hierarchy |
| **Human-in-the-loop (HITL)** | Human approval required for certain agent actions | Critical for high-stakes voice workflows |
| **Call recording consent** | Legal requirement to notify parties of recording | Jurisdiction-dependent; agent must announce |
| **Data retention policy** | Rules governing storage/deletion of conversation audio | ElevenLabs: configurable retention |
| **PII detection** | Identifying personal information in speech | Names, SSNs, credit cards in audio stream |

---

## 14. Evaluation & Quality

| Term | Definition | Context |
|---|---|---|
| **MOS (Mean Opinion Score)** | 1-5 subjective audio quality rating | Standard TTS quality metric |
| **PESQ (Perceptual Evaluation of Speech Quality)** | Algorithmic speech quality measurement | ITU-T P.862 standard |
| **Naturalness** | How human-like synthesized speech sounds | Primary TTS evaluation dimension |
| **Intelligibility** | How clearly speech can be understood | Critical for telephony/noisy environments |
| **Instruction-following accuracy** | How well model follows system prompt in voice mode | OpenAI gpt-realtime: +18.6pp improvement |
| **Tool-calling accuracy** | Correct function invocation during voice conversation | OpenAI gpt-realtime: +12.9pp improvement |
| **Entity extraction accuracy** | Correctly capturing names, dates, numbers from speech | Key metric for voice agent task completion |
| **Task completion rate** | Percentage of conversations achieving intended goal | End-to-end voice agent success metric |
| **Regression testing** | Validating agent after prompt/config changes | Hamming AI, ElevenLabs: automated test suites |
| **A/B testing** | Comparing agent configurations with live traffic | ElevenLabs Experiments feature |

---

## 15. CEX Kind Mapping

### 15.1 Existing Kinds That Apply

| CEX Kind | Voice/Realtime Application |
|---|---|
| `audio_tool` | STT engine, TTS engine, audio analysis, voice cloning tool |
| `streaming_config` | WebSocket/WebRTC streaming parameters, audio format, sample rate |
| `api_client` | Typed client for Realtime API, Hume EVI, ElevenLabs, Deepgram |
| `webhook` | Inbound call events, conversation completion callbacks |
| `mcp_server` | Voice agent MCP tools (call transfer, CRM lookup) |
| `toolkit` | Voice agent toolkit: STT + LLM + TTS + VAD tools bundled |
| `multi_modal_config` | Audio modality routing, format encoding rules |
| `rate_limit_config` | Realtime API RPM/TPM, concurrent session limits |
| `trace_config` | Voice pipeline observability: latency spans per stage |
| `hitl_config` | Human review triggers for voice agent actions |
| `context_window_config` | Audio token budget, conversation history management |
| `experiment_config` | Voice agent A/B testing configuration |

### 15.2 Proposed New Kinds

| Proposed Kind | Pillar | Description | Justification |
|---|---|---|---|
| `voice_agent_config` | P09 | Voice persona, VAD mode, turn detection, session params, voice selection | No existing kind covers realtime session config holistically |
| `vad_config` | P09 | VAD type (semantic/server/client), threshold, padding, silence duration, eagerness | Fine-grained voice activity detection tuning |
| `stt_config` | P09 | STT provider, model, language, custom vocabulary, streaming mode, confidence threshold | Distinct from `audio_tool`; this is config not tool definition |
| `tts_config` | P09 | TTS provider, voice ID, SSML support, speed, pitch, emotion style, streaming format | Controls synthesis behavior independent of tool |
| `voice_pipeline` | P12 | Ordered stage chain: VAD -> STT -> LLM -> TTS -> transport, with latency targets | Orchestration pattern for cascading voice architecture |
| `telephony_config` | P09 | SIP trunk, phone number, PSTN gateway, IVR fallback, call recording policy | Enterprise voice agent deployment config |
| `prosody_profile` | P03 | Pitch range, rate, volume, emphasis patterns, emotional style, SSML template | Reusable voice personality definition |
| `audio_codec_config` | P09 | Codec type (Opus/PCM/G.711), sample rate, bitrate, RVQ levels, frame size | Transport-layer audio encoding parameters |
| `emotion_model_config` | P02 | Emotion detection model, expression measure mapping, top-K config, prosody features | Hume-style affective computing configuration |

### 15.3 Kind Boundary Clarifications

| New Kind | NOT the same as | Boundary |
|---|---|---|
| `voice_agent_config` | `agent` | `agent` defines identity/capabilities; `voice_agent_config` defines voice-specific runtime params |
| `vad_config` | `streaming_config` | `streaming_config` is transport; `vad_config` is speech detection logic |
| `stt_config` | `audio_tool` | `audio_tool` defines a callable STT tool; `stt_config` configures its parameters |
| `tts_config` | `audio_tool` | Same pattern: tool vs. config separation |
| `voice_pipeline` | `workflow` | `workflow` is generic task orchestration; `voice_pipeline` is audio-specific stage chain |
| `prosody_profile` | `prompt_template` | `prompt_template` is text; `prosody_profile` is voice styling |

---

## 16. Cross-Reference: Industry Terms vs. CEX Metaphors

| Industry Term | What Users Might Say | CEX Mapping |
|---|---|---|
| Voice Activity Detection | "when should the bot listen?" | `vad_config` kind |
| Turn-taking | "conversation flow" | `voice_agent_config.turn_detection` |
| Barge-in | "interrupt the bot" | `voice_agent_config.interruption_handling` |
| Endpointing | "when did they stop talking?" | `vad_config.silence_duration_ms` |
| Cascading pipeline | "the STT-LLM-TTS chain" | `voice_pipeline` kind |
| Speech-to-speech | "direct voice model" | Architecture pattern, not a kind |
| Prosody control | "how the voice sounds" | `prosody_profile` kind |
| Steerable TTS | "make it sound happy" | `tts_config.style_instructions` |
| SSML | "markup for voice" | `prosody_profile.ssml_template` |
| Ephemeral token | "temp API key for browser" | `secret_config` kind |
| SIP trunk | "phone line for the bot" | `telephony_config` kind |

---

## 17. Architecture Decision Map

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

## 18. Glossary (Alphabetical)

| Term | Category | Definition |
|---|---|---|
| A/B testing | Eval | Comparing agent variants with live traffic |
| Affective dialog | Emotion | Model adapts tone to user emotion (Gemini) |
| ASR | STT | Automatic Speech Recognition |
| Audio codec | Transport | Encoder/decoder for audio compression |
| Audio token | S2S | Discrete symbolic unit representing audio |
| Barge-in | Turn-taking | User interrupts model mid-speech |
| BidiGenerateContent | Gemini | Bidirectional streaming RPC for Live API |
| Cascading pipeline | Architecture | STT -> LLM -> TTS sequential processing |
| Client event | Protocol | Message from client to server |
| Codec-based S2S | Architecture | LLM generates audio codec tokens |
| Confidence score | STT | Per-word recognition reliability |
| DTLS | Security | Encryption for WebRTC media |
| Disfluency | Prosody | Natural speech fillers (uh, um) |
| E2E latency | Metrics | Total user-to-response time |
| eLLM | Hume | Empathic Large Language Model |
| Emotion detection | Prosody | Classifying affect from voice signal |
| EnCodec | Codec | Meta's neural audio codec |
| Endpointing | VAD | Detecting utterance completion |
| Ephemeral token | Auth | Short-lived session credential |
| Expression measures | Hume | Quantified emotional signals per sentence |
| Full-duplex | Turn-taking | Both parties speak simultaneously |
| G.711 | Codec | 8kHz telephony audio format |
| Half-duplex | Turn-taking | One speaker at a time with interruption |
| ICE | WebRTC | NAT traversal protocol |
| IVR | Telephony | Interactive Voice Response system |
| Mimi | Codec | Kyutai streaming neural audio codec |
| MOS | Eval | Mean Opinion Score (1-5 quality) |
| Neural audio codec | S2S | NN audio compressor for token generation |
| Noise reduction | Audio | Server-side input audio filtering |
| Opus | Codec | Royalty-free adaptive audio codec |
| PCM16 | Format | 16-bit uncompressed audio |
| PESQ | Eval | Algorithmic speech quality metric |
| Prosody | Voice | Pitch, rhythm, stress, intonation |
| PSTN | Telephony | Public phone network |
| Push-to-talk | VAD | Manual speech start/end control |
| RTP | Transport | Real-time media transport protocol |
| RVQ | Codec | Residual Vector Quantization |
| SDP | WebRTC | Session Description Protocol |
| SFU | Infrastructure | Selective Forwarding Unit |
| SIP | Telephony | Session Initiation Protocol |
| SSML | Prosody | Speech Synthesis Markup Language |
| SSM | Architecture | State Space Model (Cartesia Sonic) |
| STT | Speech | Speech-to-Text conversion |
| STUN | WebRTC | NAT address discovery server |
| Semantic VAD | VAD | Meaning-aware end-of-turn detection |
| Server VAD | VAD | Silence-based end-of-turn detection |
| Speaker diarization | STT | Identifying who said what |
| Speech-to-speech | Architecture | Direct audio-in to audio-out model |
| Steerable TTS | TTS | Style via natural language instructions |
| Streaming TTS | TTS | Incremental audio output |
| TTFA | Metrics | Time to First Audio |
| TTFB | Metrics | Time to First Byte |
| TTFT | Metrics | Time to First Token |
| TTFW | Metrics | Time to First Word |
| TURN | WebRTC | Relay server for NAT traversal |
| Turn-taking | Conversation | Who speaks when protocol |
| VAD | Speech | Voice Activity Detection |
| Voice cloning | TTS | Reproducing a specific speaker's voice |
| Vocoder | S2S | Token-to-waveform converter |
| WER | Eval | Word Error Rate |
| WebRTC | Transport | Browser real-time communication |
| WebSocket | Transport | Persistent bidirectional connection |
