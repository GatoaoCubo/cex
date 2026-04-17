---
kind: examples
id: bld_examples_stt_provider
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of stt_provider artifacts
quality: 8.8
title: "Examples Stt Provider"
version: "1.0.0"
author: wave1_builder_gen
tags: [stt_provider, builder, examples]
tldr: "Golden and anti-examples of stt_provider artifacts"
domain: "stt_provider construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Golden Example
```yaml
kind: stt_provider
name: google_stt
description: Integration with Google Cloud Speech-to-Text API
parameters:
  provider: google
  api_key: "AIzaSyD..."
  endpoint: "https://speech.googleapis.com/v1p1beta1/audio:recognize"
  language: "en-US"
  sample_rate: 16000
usage:
  - command: transcribe
    input: audio_file.wav
    output: text_result.txt
```

## Anti-Example 1: Missing Critical Parameters
```yaml
kind: stt_provider
name: broken_stt
description: Incomplete STT config
parameters:
  provider: azure
  endpoint: "https://speech.azure.com/recognize"
```
## Why it fails
Lacks API credentials and essential settings like language code, making authentication and processing impossible.

## Anti-Example 2: Mixing VAD Config
```yaml
kind: stt_provider
name: mixed_stt
description: STT with VAD settings
parameters:
  provider: aws
  api_key: "AKIAXXXXX"
  endpoint: "https://transcribe.aws.com"
  vad_threshold: 0.5
  silence_timeout: 2.0
```
## Why it fails
Includes VAD parameters (vad_threshold, silence_timeout) which belong to voice_pipeline configuration, violating boundary constraints and causing scope confusion.
