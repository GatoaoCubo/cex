---
kind: collaboration
id: bld_collaboration_hitl_config
pillar: P12
llm_function: COLLABORATE
purpose: How hitl-config-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.1
title: "Collaboration Hitl Config"
version: "1.0.0"
author: n03_builder
tags: [hitl_config, builder, collaboration, P12]
tldr: "hitl-config-builder role in crews: HITL gate specialist. Receives workflow + risk level. Produces review gate config. Depends on guardrail, quality_gate."
domain: "hitl_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
---

# Collaboration: hitl-config-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "under what conditions should this output pause for human judgment, who reviews it in what order, and what happens if they don't respond?"
I do not automate filtering (that is guardrail). I do not score quality automatically (that is quality_gate). I configure the gate where human eyes are required and cannot be replaced by automation.
## Crew Compositions
### Crew: "AI Output Governance"
```
  1. guardrail-builder    -> "automated safety filtering (pre-HITL block)"
  2. quality-gate-builder -> "automated scoring (post-generation quality check)"
  3. hitl-config-builder  -> "human review gate for outputs that pass auto-checks but need human judgment"
  4. learning-record-builder -> "capture review decisions for model improvement"
```
### Crew: "High-Stakes AI Deployment"
```
  1. agent-builder        -> "agent definition and capabilities"
  2. guardrail-builder    -> "safety boundaries for agent outputs"
  3. hitl-config-builder  -> "mandatory human review for regulatory/domain requirements"
  4. workflow-builder     -> "orchestrate agent steps including HITL pause node"
  5. reward-signal-builder -> "continuous quality signal from review outcomes"
```
### Crew: "Content Generation Pipeline"
```
  1. prompt-template-builder -> "generation prompt"
  2. quality-gate-builder    -> "automated quality scoring"
  3. hitl-config-builder     -> "human edit flow for below-threshold outputs"
  4. lifecycle-rule-builder  -> "archive or promote reviewed content"
```
## Handoff Protocol
### I Receive
- seeds: workflow name, output types being reviewed, risk level (high/medium/low)
- optional: existing reviewer list, SLA requirements, regulatory constraints, notification preferences
- optional: confidence score availability (determines trigger type)
### I Produce
- hitl_config artifact (.md + .yaml frontmatter)
- committed to: `P11_feedback/examples/p11_hitl_{name}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons listed
## Builders I Depend On
| Builder | Why |
|---------|-----|
| guardrail-builder | Automated filter upstream; HITL reviews what passes the guardrail |
| quality-gate-builder | Automated score; HITL escalates when score falls below threshold |
| agent-builder | Agent workflow defines where HITL pause nodes are inserted |
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| workflow-builder | Workflows embed HITL pause nodes; need hitl_config to configure them |
| learning-record-builder | Captures review decisions logged by hitl_config feedback_loop |
| reward-signal-builder | Review outcomes feed into reward signal for RLHF training |
| optimizer-builder | Optimizes review volume by tracking which triggers fire most often |
