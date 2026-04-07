---
kind: collaboration
id: bld_collaboration_multi_modal_config
pillar: P12
llm_function: COLLABORATE
purpose: How multi-modal-config-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
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
