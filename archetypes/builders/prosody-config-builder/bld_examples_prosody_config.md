---
kind: examples
id: bld_examples_prosody_config
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of prosody_config artifacts
quality: 9.0
title: "Examples Prosody Config"
version: "1.1.0"
author: n03_hybrid_review2
tags: [prosody_config, builder, examples, ssml, elevenlabs, cartesia]
tldr: "Golden and anti-examples covering SSML + provider-native emotion/style tags"
domain: "prosody_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
---

## Golden Example 1 -- SSML (Azure/Google/AWS portable)
```yaml
---
id: p09_prs_calm_professional
kind: prosody_config
pillar: P09
version: 1.0.0
---
baseline:
  pitch: "+0%"
  rate: "100%"
  volume: "medium"
emotions:
  calm_professional:
    ssml: |
      <prosody pitch="+2%" rate="95%" volume="medium">
        <break time="300ms"/>
        {{text}}
      </prosody>
  urgent_alert:
    ssml: |
      <prosody pitch="+8%" rate="115%" volume="loud">
        <emphasis level="strong">{{text}}</emphasis>
      </prosody>
target_providers: [azure, google, aws]
```

## Golden Example 2 -- ElevenLabs v3 native
```yaml
---
id: p09_prs_elevenlabs_warm
kind: prosody_config
pillar: P09
version: 1.0.0
---
provider: elevenlabs
voice_settings:
  stability: 0.35          # low = expressive
  similarity_boost: 0.75
  style: 0.45              # moderate style exaggeration
  use_speaker_boost: true
model_id: eleven_multilingual_v2
```

## Golden Example 3 -- Cartesia Sonic inline directives
```yaml
---
id: p09_prs_cartesia_excited
kind: prosody_config
pillar: P09
version: 1.0.0
---
provider: cartesia
model: sonic-english
speed: normal
text_template: "[excited] {{text}} [pause:200ms]"
language: en
```

## Anti-Example 1 -- Mixing provider settings with prosody
```yaml
---
id: p09_prs_bad_provider
prosody_config: "aggressive_sales"
tts_provider: "azure"          # FAIL: belongs in tts_provider kind
api_key: "Ak2hG..."            # FAIL: belongs in secret_config
---
```
## Why it fails
Embeds provider integration + credentials. Prosody_config defines voice characteristics only; provider wiring belongs in tts_provider, secrets in secret_config. Violates pillar boundary (P09 vs P04 vs P09).

## Anti-Example 2 -- Vague, unmeasurable parameters
```yaml
---
id: p09_prs_mysterious
emotion: "unclear"             # FAIL: not a valid emotion label
speech_rate: "fast"            # FAIL: non-numeric, non-SSML
pitch: "high-ish"              # FAIL: subjective
---
```
## Why it fails
Uses ambiguous strings. Prosody requires either SSML-compliant values (x-fast, +10%, 120Hz) OR provider-native enums (ElevenLabs sliders 0.0-1.0, Cartesia `[excited]`). No downstream system can interpret "high-ish".

## Anti-Example 3 -- SSML tags to non-SSML provider
```yaml
---
id: p09_prs_wrong_target
provider: elevenlabs
ssml: "<prosody rate='120%'>Hello</prosody>"   # FAIL: ElevenLabs ignores SSML
---
```
## Why it fails
ElevenLabs v3 does not parse SSML -- it consumes `voice_settings` JSON. Tags are silently passed through as literal text, corrupting output. Always validate emission path matches target provider (see provider matrix in KC).
