---
kind: knowledge_card
id: bld_knowledge_card_audio_tool
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for audio_tool production — audio processing tool specification
sources: OpenAI Whisper docs, ElevenLabs API, Google Speech-to-Text, Azure Cognitive Speech, Deepgram docs, AssemblyAI docs
---

# Domain Knowledge: audio_tool
## Executive Summary
Audio tools process audio signals: converting speech to text (STT), generating speech from text (TTS), or analyzing audio features (speaker diarization, emotion, language detection). They are direction-specific, model-bound, format-constrained, and language-scoped. Audio tools are NOT notifiers (message delivery), NOT vision_tools (image/video), NOT cli_tools (terminal executables).
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P04 (tools) |
| llm_function | CALL (invocable) |
| Directions | input (STT), output (TTS), analysis, bidirectional |
| Standard sample_rate | 16000 Hz (STT), 22050/44100 Hz (TTS) |
| Max body | 2048 bytes |
| Language codes | BCP-47 (en, pt-BR, es, fr, de, ja, zh, ko, it, nl) |
## Direction Reference
| Direction | Meaning | Input | Output |
|-----------|---------|-------|--------|
| input | Speech-to-text (STT) | audio bytes | text string |
| output | Text-to-speech (TTS) | text string | audio bytes |
| analysis | Feature extraction | audio bytes | structured JSON |
| bidirectional | STT + TTS both | audio or text | text or audio |
## Model Reference
| Model ID | Provider | Direction | Notes |
|----------|----------|-----------|-------|
| whisper_large_v3 | OpenAI | input | Best multilingual accuracy, 99 languages |
| whisper_large_v3_turbo | OpenAI | input | 8x faster, slight accuracy trade-off |
| tts_1 | OpenAI | output | Low latency, 6 voices |
| tts_1_hd | OpenAI | output | High fidelity, 6 voices |
| eleven_multilingual_v2 | ElevenLabs | output | 29 languages, voice cloning |
| eleven_turbo_v2_5 | ElevenLabs | output | Ultra-low latency (<400ms) |
| google_chirp | Google | input | 100+ languages, Chirp architecture |
| google_chirp_2 | Google | input | Next-gen, better noise robustness |
| azure_neural_hd | Azure | output | 140+ voices, SSML support |
| azure_whisper | Azure | input | Whisper-based Azure deployment |
| deepgram_nova_2 | Deepgram | input | <300ms latency, streaming |
| deepgram_nova_2_medical | Deepgram | input | Medical vocabulary specialization |
| assemblyai_best | AssemblyAI | input | Best accuracy, speaker diarization |
| assemblyai_nano | AssemblyAI | input | Fast + cheap, lower accuracy |
## Format Compatibility
| Format | STT Input | TTS Output | Notes |
|--------|-----------|------------|-------|
| mp3 | yes | yes | Most common; lossy compression |
| wav | yes | yes | Lossless PCM; best STT accuracy |
| ogg | yes | yes | Open format; good web compatibility |
| flac | yes | no | Lossless compressed; STT only |
| webm | yes | no | Browser MediaRecorder default |
| m4a | yes | no | Apple ecosystem; AAC codec |
| aac | yes | yes | Efficient lossy compression |
| pcm | yes | yes | Raw samples; lowest latency |
## Language Coverage
| BCP-47 | Language | Whisper | Deepgram | ElevenLabs | AssemblyAI |
|--------|----------|---------|---------|------------|------------|
| en | English | high | high | high | high |
| pt-BR | Portuguese (BR) | high | medium | high | medium |
| es | Spanish | high | medium | high | medium |
| fr | French | high | medium | high | medium |
| de | German | high | medium | high | medium |
| ja | Japanese | medium | low | medium | low |
| zh | Chinese | medium | low | medium | low |
| ko | Korean | medium | low | medium | low |
| it | Italian | high | low | high | low |
## Patterns
- **STT pipeline**: audio bytes -> sample_rate normalize -> model transcribe -> text + timestamps out
- **TTS pipeline**: text string -> SSML optional -> model synthesize -> audio bytes + format out
- **Streaming STT**: chunked audio in -> partial transcript events out (Deepgram WebSocket, AssemblyAI WebSocket)
- **Sample rate**: always normalize to 16000 Hz before STT to avoid accuracy degradation
- **Word timestamps**: available in Whisper, Deepgram, AssemblyAI — enables subtitle generation, speaker sync
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Using GPT-4o as audio model id | GPT-4o is an LLM, not a standalone audio model identifier |
| direction: "stt" (wrong enum) | Valid values are: input, output, analysis, bidirectional |
| languages: ["English"] (free text) | Must use BCP-47: "en" — free text breaks downstream routing |
| formats: ["audio/*"] (wildcard) | Must be explicit enum members — wildcards unvalidatable |
| Conflating audio_tool with notifier | Notifier delivers messages; audio_tool processes audio signals |
| No sample_rate declared | Defaults are ambiguous; STT accuracy varies 16000 vs 44100 |
| Claiming streaming without declaring streaming: true | Silent capability misrepresentation |
## Application
1. Determine direction: what goes in and what comes out?
2. Select models: match direction + language coverage + latency requirement
3. Specify formats: which formats does the caller need to send/receive?
4. List languages: BCP-47 codes only, note quality tier differences per model
5. Declare streaming, sample_rate, max_duration — these affect integration contracts
6. Validate: id pattern, kind, direction enum, model names against provider reference
