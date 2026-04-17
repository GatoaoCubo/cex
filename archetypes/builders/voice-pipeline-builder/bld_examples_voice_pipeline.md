---
kind: examples
id: bld_examples_voice_pipeline
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of voice_pipeline artifacts (real provider names, not placeholders)
quality: 9.1
title: "Examples: voice-pipeline-builder"
version: "1.1.0"
author: n01_audit
tags: [voice_pipeline, builder, examples, deepgram, elevenlabs, rasa, dialogflow]
tldr: "Golden: contact center pipeline with Deepgram+Rasa+ElevenLabs. Anti-examples: placeholder providers, missing preprocessing, no fallback."
domain: "voice_pipeline construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
---

## Golden Example: Contact Center Voice Pipeline

```yaml
---
kind: voice_pipeline
id: p04_vp_contact_center_en
pillar: P04
title: "Contact Center Voice Pipeline (English)"
version: "1.0.0"
created: 2026-04-13
updated: 2026-04-13
author: n03_builder
domain: "customer support"
language: en
sample_rate: 16000
quality: null
tags: [voice_pipeline, customer_support, deepgram, rasa, elevenlabs]
tldr: "5-stage English contact center pipeline: RNNoise+VAD preprocessing, Deepgram Nova-2 STT, Rasa NLU, LangChain DM, ElevenLabs TTS."
---
```

### Pipeline Stages

| Stage | Provider | Input | Output |
|-------|----------|-------|--------|
| Audio Preprocessing | RNNoise + WebRTC VAD | Raw PCM 16kHz | Cleaned PCM 16kHz |
| STT | Deepgram Nova-2 (WebSocket streaming) | Cleaned PCM | JSON transcript |
| NLU | Rasa Open Source 3.x | Transcript text | Intent + entities |
| Dialogue Management | LangChain + GPT-4o | Intent + session history | Response text |
| TTS | ElevenLabs Turbo v2.5 (streaming) | Response text | MP3/PCM audio stream |

### Why it passes

- All 5 stages present including audio preprocessing ✓
- Real provider names (Deepgram Nova-2, Rasa, ElevenLabs Turbo) ✓
- Provider abstraction: each stage uses interface, not hardcoded API ✓
- `quality: null` in frontmatter ✓
- ID matches `^p04_vp_[a-z0-9_]+$` ✓

---

## Anti-Example 1: Placeholder Provider Names

```yaml
---
kind: voice_pipeline
id: p04_vp_basic
pillar: P04
title: "Basic Voice Pipeline"
quality: null
---
components:
  - name: speech_recognition
    type: stt
    providers: [providerA, providerB]
  - name: text_to_speech
    type: tts
    providers: [providerX, providerY]
```

### Why it fails

`providerA`, `providerB`, `providerX`, `providerY` are placeholders.
They provide zero production guidance. Engineers cannot instantiate this pipeline.
Must use real names: Deepgram Nova-2, AssemblyAI, OpenAI Whisper for STT;
ElevenLabs, Google Cloud TTS, Amazon Polly for TTS.

**Also fails**: Missing NLU, dialogue management, and audio preprocessing stages.

---

## Anti-Example 2: Missing Audio Preprocessing

```yaml
---
kind: voice_pipeline
id: p04_vp_no_preproc
pillar: P04
title: "Unprocessed Voice Pipeline"
quality: null
---
stages:
  - name: stt
    provider: deepgram_nova2
  - name: nlu
    provider: dialogflow_cx
  - name: tts
    provider: google_cloud_tts
```

### Why it fails

No audio preprocessing stage. In noisy environments (call center background noise,
mobile ambient sound), WER increases by 25-60% without preprocessing.
RNNoise or WebRTC VAD MUST precede STT. Also missing dialogue management stage.

---

## Anti-Example 3: Single-Provider, No Fallback

```yaml
---
kind: voice_pipeline
id: p04_vp_locked
pillar: P04
title: "Single-Provider Pipeline"
quality: null
---
stages:
  - name: stt
    provider: deepgram_nova2        # only provider, no fallback
  - name: nlu
    provider: dialogflow_cx         # only provider, no fallback
  - name: tts
    provider: elevenlabs_turbo      # only provider, no fallback
```

### Why it fails

No fallback chains defined. When Deepgram has an outage (avg 2-3x/year for any SaaS),
pipeline goes down completely. Recovery time: 15+ minutes mean (manual intervention).
With fallback to OpenAI Whisper v3: zero-downtime automatic failover.

## Properties

| Property | Value |
|----------|-------|
| Kind | `examples` |
| Pillar | P07 |
| Domain | voice_pipeline construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
