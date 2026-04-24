---
id: p09_kc_prosody_config
kind: knowledge_card
8f: F3_inject
type: kind
pillar: P09
title: "Prosody Config -- Deep Knowledge for prosody_config"
version: 1.0.0
created: 2026-04-15
updated: 2026-04-15
author: n05_selfheal
quality: 9.1
tags: []
density_score: 1.0
related:
  - prosody-config-builder
  - bld_schema_prosody_config
  - p03_sp_prosody_config_builder
  - bld_collaboration_prosody_config
  - p10_lr_prosody_config_builder
  - bld_examples_prosody_config
  - kc_voice_pipeline
  - tts-provider-builder
  - bld_tools_prosody_config
  - bld_output_template_tts_provider
---

# Prosody Configuration Guide

## Introduction
Prosody configuration defines how speech synthesis systems modulate pitch, stress, and intonation to create natural-sounding speech. This guide explains key parameters, best practices, and use cases for configuring prosody in text-to-speech (TTS) systems.

## Key Concepts
### 1. Prosody Parameters
- **Pitch**: Vertical position of the voice (measured in Hz)
- **Intonation**: Rise/fall pattern of pitch across phrases
- **Stress**: Emphasis on syllables or words
- **Rhythm**: Timing and duration of speech segments
- **Pause**: Silence between words or phrases

### 2. Configuration Scope
- **Global**: Applies to all text
- **Sentence-level**: Applies to entire sentences
- **Word-level**: Applies to specific words
- **Phoneme-level**: Applies to individual speech sounds

## Configuration Parameters
| Parameter | Description | Data Type | Default | Example |
|----------|-------------|-----------|---------|---------|
| pitch | Base pitch frequency in Hz | float | 120.0 | 150.0 |
| pitchRange | Pitch variation range (Hz) | float | 20.0 | 30.0 |
| intonation | Intonation pattern (up/down/flat) | string | "neutral" | "rising" |
| stress | Stress level (0-100) | integer | 50 | 75 |
| pause | Pause duration in seconds | float | 0.5 | 1.2 |
| rhythm | Rhythm pattern (fast/normal/slow) | string | "normal" | "fast" |

## Example Configurations
### 1. Basic Configuration
```yaml
prosody:
  pitch: 120.0
  pitchRange: 20.0
  intonation: neutral
  stress: 50
  pause: 0.5
  rhythm: normal
```

### 2. Sentence-Level Configuration
```yaml
prosody:
  sentence:
    pitch: 130.0
    intonation: rising
    stress: 70
    pause: 1.0
```

### 3. Word-Level Configuration
```yaml
prosody:
  words:
    - word: "important"
      stress: 90
      pitch: 140.0
    - word: "never"
      stress: 60
      pitchRange: 25.0
```

## Best Practices
1. **Use context-aware parameters**: Adjust pitch based on sentence structure
2. **Balance stress and pause**: Avoid over-stressing words
3. **Match intonation to content**: Use rising intonation for questions
4. **Test with different rhythms**: Find optimal pacing for content
5. **Use phoneme-level controls for precision**: For technical documentation

## Use Cases
### 1. News Broadcasting
```yaml
prosody:
  pitch: 140.0
  pitchRange: 15.0
  intonation: flat
  stress: 40
  pause: 0.8
  rhythm: fast
```

### 2. Educational Content
```yaml
prosody:
  pitch: 130.0
  pitchRange: 25.0
  intonation: rising
  stress: 60
  pause: 0.6
  rhythm: normal
```

### 3. Customer Service
```yaml
prosody:
  pitch: 125.0
  pitchRange: 10.0
  intonation: neutral
  stress: 50
  pause: 0.7
  rhythm: slow
```

## Advanced Techniques
### 1. Dynamic Parameter Adjustment
```yaml
prosody:
  dynamic:
    pitch: 
      question: 150.0
      statement: 120.0
    intonation:
      question: "rising"
      statement: "flat"
```

### 2. Phoneme-Level Control
```yaml
prosody:
  phonemes:
    - phoneme: "V"
      pitch: 140.0
      stress: 90
    - phoneme: "R"
      pitchRange: 30.0
      pause: 0.3
```

## Troubleshooting
| Issue | Solution |
|-------|----------|
| Monotone speech | Increase pitchRange and add intonation variation |
| Too fast speech | Reduce rhythm speed and increase pause duration |
| Unnatural stress | Adjust stress levels and use phoneme-level controls |
| Poor intonation | Use dynamic intonation settings based on sentence type |

## References
- [ISO 20463:2020 - Speech synthesis parameters](https://www.iso.org/standard/76244.html)
- [CMU Sphinx Documentation](https://cmusphinx.github.io/)
- [MaryTTS Configuration Guide](https://marytts.readthedocs.io/en/latest/)

## Appendix
### 1. Parameter Units
- Pitch: Hertz (Hz)
- PitchRange: Hertz (Hz)
- Pause: Seconds (s)
- Stress: Percentage (0-100)
- Rhythm: Relative speed (fast/normal/slow)

### 2. Configuration File Structure
```yaml
prosody:
  global:
    pitch: 120.0
    pitchRange: 20.0
    intonation: neutral
    stress: 50
    pause: 0.5
    rhythm: normal
  sentence:
    pitch: 130.0
    intonation: rising
    stress: 7
    pause: 1.0
  words:
    - word: "important"
      stress: 90
      pitch: 140.0
    - word: "never"
      stress: 60
      pitchRange: 25.0
```

### 3. Version History
- 1.0.0 (2023-10-15): Initial release
- 1.1.0 (2023-10-20): Added dynamic parameter adjustment
- 1.2.0 (2023-10-25): Enhanced phoneme-level controls

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[prosody-config-builder]] | related | 0.40 |
| [[bld_schema_prosody_config]] | upstream | 0.32 |
| [[p03_sp_prosody_config_builder]] | upstream | 0.29 |
| [[bld_collaboration_prosody_config]] | downstream | 0.29 |
| [[p10_lr_prosody_config_builder]] | downstream | 0.24 |
| [[bld_examples_prosody_config]] | upstream | 0.21 |
| [[kc_voice_pipeline]] | sibling | 0.20 |
| [[tts-provider-builder]] | upstream | 0.19 |
| [[bld_tools_prosody_config]] | upstream | 0.19 |
| [[bld_output_template_tts_provider]] | upstream | 0.19 |
