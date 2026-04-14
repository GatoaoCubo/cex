---
kind: examples
id: bld_examples_vad_config
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of vad_config artifacts
quality: 8.8
title: "Examples Vad Config"
version: "1.0.0"
author: wave1_builder_gen
tags: [vad_config, builder, examples]
tldr: "Golden and anti-examples of vad_config artifacts"
domain: "vad_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Golden Example
```yaml
---
kind: vad_config
version: 1.0
---
sensitivity: 0.75
noise_suppression: true
aggressiveness: 3
min_speech_duration: 0.5
max_speech_gap: 1.2
```

## Anti-Example 1: Missing required parameters
```yaml
---
kind: vad_config
version: 1.0
---
noise_suppression: false
aggressiveness: 5
```
## Why it fails
Missing `sensitivity` and `min_speech_duration` parameters make configuration incomplete. VAD requires these to function reliably, leading to unpredictable detection behavior.

## Anti-Example 2: Mixing VAD with STT parameters
```yaml
---
kind: vad_config
version: 1.0
---
sensitivity: 0.8
transcription_engine: "whisper"
language: "en"
```
## Why it fails
Includes `transcription_engine` and `language` parameters which belong to STT components, not VAD. This violates the boundary constraint and creates configuration conflicts.
