---
kind: examples
id: bld_examples_prosody_config
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of prosody_config artifacts
quality: null
title: "Examples Prosody Config"
version: "1.0.0"
author: wave1_builder_gen
tags: [prosody_config, builder, examples]
tldr: "Golden and anti-examples of prosody_config artifacts"
domain: "prosody_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Golden Example
```markdown
---
prosody_config: "calm_professional"
emotion: "neutral"
speech_rate: "100%"  # Normal pace
pitch: "120Hz"       # Slightly higher than default
volume: "75%"        # Moderate loudness
pauses: "0.8s"       # Short, deliberate pauses
personality: "composed, authoritative"
voice_modifiers: ["clear_articulation", "minimal_intonation"]
```

## Anti-Example 1: Mixing with provider settings
```markdown
---
prosody_config: "aggressive_sales"
tts_provider: "azure"  # ❌ Incorrect: provider integration is out of scope
emotion: "urgent"
speech_rate: "150%"
```
## Why it fails
Includes `tts_provider` which belongs to a different CEX kind. Prosody_config should only define voice characteristics, not infrastructure details.

## Anti-Example 2: Vague/missing parameters
```markdown
---
prosody_config: "mysterious"
emotion: "unclear"  # ❌ Incorrect: emotion should be specific
speech_rate: "fast"
```
## Why it fails
Uses ambiguous values ("unclear", "fast") without measurable parameters. Prosody settings require concrete numerical ranges or standardized descriptors for consistent voice generation.
