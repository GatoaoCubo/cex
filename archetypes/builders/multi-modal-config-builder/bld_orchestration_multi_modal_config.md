---
kind: collaboration
id: bld_collaboration_multi_modal_config
pillar: P12
llm_function: COLLABORATE
purpose: How multi-modal-config-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.0
title: "Collaboration Multi Modal Config"
version: "1.0.0"
author: n03_builder
tags: [multi_modal_config, builder, examples]
tldr: "Golden and anti-examples for multi modal config construction, demonstrating ideal structure and common pitfalls."
domain: "multi modal config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - multi-modal-config-builder
  - p03_sp_multi_modal_config_builder
  - bld_collaboration_model_card
  - bld_collaboration_agent
  - bld_collaboration_context_window_config
  - bld_instruction_multi_modal_config
  - bld_collaboration_boot_config
  - bld_collaboration_builder
  - bld_tools_multi_modal_config
  - bld_config_multi_modal_config
---

# Collaboration: multi-modal-config-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "how should non-text inputs be processed and routed?"
I do not implement image analysis. I do not process audio. I do not define model capabilities.
I configure the constraints, routing, and preprocessing for multi-modal inputs.
## Crew Compositions
### Crew: "Multi-Modal Agent"
```
  1. multi-modal-config-builder -> "modality constraints and routing"
  2. vision-tool-builder -> "image analysis implementation"
  3. audio-tool-builder -> "audio processing implementation"
  4. agent-card-builder -> "agent deployment with modality support"
```
### Crew: "Budget-Aware Multi-Modal"
```
  1. multi-modal-config-builder -> "token costs per modality"
  2. context-window-config-builder -> "budget allocation accounting for modalities"
  3. prompt-template-builder -> "template with multi-modal content blocks"
```
## Handoff Protocol
### I Receive
- seeds: target use case, supported modalities, target models
- optional: budget constraints, volume expectations
### I Produce
- multi_modal_config artifact (.yaml, max 2KB)
- committed to: `P04_tools/examples/p04_mmc_{capability}.yaml`
### I Signal
- signal: complete (with quality from QUALITY_GATES)
## Builders I Depend On
| Builder | Why |
|---------|-----|
| model-card-builder | Model modality capabilities |
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| vision-tool-builder | Resolution constraints from config |
| audio-tool-builder | Format/duration constraints from config |
| context-window-config-builder | Token costs per modality |
| agent-card-builder | Agent modality support spec |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[multi-modal-config-builder]] | upstream | 0.48 |
| [[p03_sp_multi_modal_config_builder]] | upstream | 0.41 |
| [[bld_collaboration_model_card]] | sibling | 0.41 |
| [[bld_collaboration_agent]] | sibling | 0.40 |
| [[bld_collaboration_context_window_config]] | sibling | 0.39 |
| [[bld_instruction_multi_modal_config]] | upstream | 0.38 |
| [[bld_collaboration_boot_config]] | sibling | 0.38 |
| [[bld_collaboration_builder]] | sibling | 0.36 |
| [[bld_tools_multi_modal_config]] | upstream | 0.36 |
| [[bld_config_multi_modal_config]] | upstream | 0.35 |
