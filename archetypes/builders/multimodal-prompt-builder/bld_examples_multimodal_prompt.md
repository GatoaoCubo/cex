---
kind: examples
id: bld_examples_multimodal_prompt
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of multimodal_prompt artifacts
quality: 8.8
title: "Examples Multimodal Prompt"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [multimodal_prompt, builder, examples]
tldr: "Golden and anti-examples of multimodal_prompt artifacts"
domain: "multimodal_prompt construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Golden Example
```yaml
model: "Salesforce/blip"
modalities: [image, text, audio]
task: "Generate a caption for an image and describe the corresponding audio"
prompt: |
  [Image: A cat sitting on a windowsill]
  [Audio: Meowing sound]
  Describe this scene and the audio in detail.
```

## Anti-Example 1: Text-only prompt
```yaml
model: "Salesforce/blip"
modalities: [text]
task: "Generate a caption"
prompt: "Describe this image of a cat on a windowsill"
```
## Why it fails
Excludes required non-text modalities (image/audio) despite claiming to be multimodal. Fails to integrate cross-modal elements.

## Anti-Example 2: Model configuration
```yaml
model: "Salesforce/blip"
modalities: [image, text]
task: "Generate caption"
prompt: |
  [Image: Cat on windowsill]
  max_tokens: 50
  temperature: 0.7
```
## Why it fails
Includes model parameters (max_tokens, temperature) which belong to multi_modal_config, not the actual multimodal prompt content.
