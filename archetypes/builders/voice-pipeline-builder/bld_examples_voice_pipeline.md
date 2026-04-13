---
kind: examples
id: bld_examples_voice_pipeline
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of voice_pipeline artifacts
quality: null
title: "Examples Voice Pipeline"
version: "1.0.0"
author: wave1_builder_gen
tags: [voice_pipeline, builder, examples]
tldr: "Golden and anti-examples of voice_pipeline artifacts"
domain: "voice_pipeline construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Golden Example
```yaml
---
kind: voice_pipeline
version: 1.0
author: VoiceArchitect
description: End-to-end voice agent with modular components
---
components:
  - name: speech_recognition
    type: stt
    providers: [providerA, providerB]
  - name: natural_language_processing
    type: nlp
    models: [intent_classifier, sentiment_analyzer]
  - name: dialogue_management
    type: state_machine
    states: [greeting, task, confirmation]
  - name: text_to_speech
    type: tts
    providers: [providerX, providerY]
  - name: feedback_loop
    type: analytics
    metrics: [accuracy, latency]
```

## Anti-Example 1: Missing Core Components
```yaml
---
kind: voice_pipeline
version: 0.5
author: Newbie
description: Basic voice pipeline
---
components:
  - name: speech_recognition
    type: stt
    providers: [providerA]
  - name: text_to_speech
    type: tts
    providers: [providerX]
```
## Why it fails
Lacks NLP, dialogue management, and feedback systems. Cannot handle complex interactions or adapt to user context.

## Anti-Example 2: Single Provider Lock-In
```yaml
---
kind: voice_pipeline
version: 1.0
author: VendorX
description: Voice pipeline with proprietary components
---
components:
  - name: speech_recognition
    type: stt
    providers: [vendorX_stt]
  - name: text_to_speech
    type: tts
    providers: [vendorX_tts]
```
## Why it fails
No provider flexibility or redundancy. System becomes obsolete if vendor discontinues services, violating modularity principles.
