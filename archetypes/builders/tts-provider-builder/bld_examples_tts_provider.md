---
kind: examples
id: bld_examples_tts_provider
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of tts_provider artifacts
quality: 8.8
title: "Examples Tts Provider"
version: "1.0.0"
author: wave1_builder_gen
tags: [tts_provider, builder, examples]
tldr: "Golden and anti-examples of tts_provider artifacts"
domain: "tts_provider construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Golden Example
```yaml
name: tts_provider
description: Integrates with Azure Cognitive Services Text-to-Speech
version: 1.2.0
parameters:
  - name: api_key
    type: string
    description: Azure API key for TTS service
  - name: endpoint
    type: string
    format: uri
    description: Azure TTS endpoint URL
  - name: voice
    type: string
    enum: ["en-US-JennyNeural", "fr-FR-DeniseNeural"]
    description: Voice model to use
```

## Anti-Example 1: Missing Critical Parameters
```yaml
name: tts_provider
description: Incomplete TTS integration
version: 0.1.0
parameters:
  - name: voice
    type: string
    enum: ["en-US-JennyNeural"]
```
## Why it fails
Lacks authentication parameters (api_key) and endpoint URL, making the integration non-functional. No way to connect to any TTS service.

## Anti-Example 2: Mixing Responsibilities
```yaml
name: tts_provider
description: Overloaded TTS configuration
version: 1.0.0
parameters:
  - name: prosody_config
    type: object
    properties:
      pitch: number
      rate: number
```
## Why it fails
Violates boundary constraints by including prosody_config parameters which belong to voice_pipeline, not tts_provider. Mixes integration configuration with voice personality settings.
