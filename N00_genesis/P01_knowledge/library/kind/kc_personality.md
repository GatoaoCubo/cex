---
quality: 8.3
quality: 7.8
id: kc_personality
kind: knowledge_card
pillar: P01
nucleus: n00
title: "KC: personality"
version: 1.0.0
tags: [personality, knowledge-card, hermes_origin, hot_swap, P02, soul_md, HERMES]
density_score: 0.93
updated: "2026-04-18"
related:
  - p01_kc_mental_model
  - bld_collaboration_agent
  - agent-builder
  - p01_kc_agent
  - bld_architecture_agent
  - p01_kc_brand_voice_consistency_channels
  - agent-profile-builder
  - bld_schema_runtime_state
  - bld_knowledge_card_agent
  - bld_collaboration_system_prompt
---

<!-- 8F: F1=knowledge_card P01 F2=knowledge-card-builder F3=spec_hermes+kc_hermes F4=plan F5=scan F6=produce F7=gate F8=save -->

## Definition

A `personality` is a **hot-swappable voice/tone/values overlay** applied to an agent at
runtime. Implementing the HERMES SOUL.md pattern (NousResearch/hermes-agent), a personality
specifies HOW the agent communicates -- register, verbosity, humor, core values, tone
examples, and anti-patterns -- WITHOUT altering capabilities, memory, or routing.

## Origin: HERMES SOUL.md

NousResearch/hermes-agent introduced `SOUL.md` as a file that rides alongside a system
prompt, injecting a persistent persona layer. CEX adapts this as the `personality` kind:
a first-class artifact that can be:
1. Authored independently of any agent
2. Stored in P02 as a versioned spec
3. Activated at runtime via `/personality [name]`
4. Swapped instantly without agent restart

## Core Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| voice.register | enum | yes | Communication style: formal, casual, technical, playful |
| voice.verbosity | enum | yes | Response length: terse, balanced, verbose |
| voice.humor | enum | yes | Levity calibration: off, dry, warm |
| values | list | yes | 3-5 core principles driving persona behavior |
| tone_examples | list | yes | >= 3 verbatim sample phrases the persona would say |
| anti_patterns | list | yes | >= 3 phrases this persona would NEVER say |
| activation_cue | string | yes | `/personality {{name}}` -- hot-swap trigger |
| deactivation_cue | string | yes | `/personality default` -- revert trigger |
| hot_swap_compatible | bool | yes | true = swap without agent restart (default) |

## Boundaries

| Kind | Relationship | Key Difference |
|------|-------------|----------------|
| `agent` (P02) | Carries the active personality | agent = full spec (tools + memory + capabilities) |
| `agent_profile` (P08) | May reference active personality | agent_profile = runtime AI config (model, temperature) |
| `system_prompt` (P03) | May instruct "use personality X" | system_prompt = full prompt; personality = voice layer only |
| `lens` (P02) | Domain perspective | lens = routing rules + domain knowledge; personality = communication style |
| `user_model` (P10) | Tracks user's preferred personality | user_model = human representation; personality = agent voice |

## Hot-Swap Mechanics

```
User: /personality researcher
  -> Agent loads p02_per_researcher.md from P02 store
  -> Injects voice.register=technical, verbosity=verbose, humor=dry
  -> Applies values and tone_examples to subsequent responses

User: /personality default
  -> Agent reverts to default voice profile
  -> Session state cleared of active_personality
```

## Voice Register Reference

| Register | Communication style | Use case |
|----------|--------------------|----|
| formal | Precise, structured, no contractions | Professional, legal, academic |
| casual | Friendly, uses contractions, approachable | Support, daily chat |
| technical | Jargon-rich, assumes domain knowledge | Dev, engineering |
| playful | Wit-forward, light, pun-tolerant | Creative, social, entertainment |

## Builder
`archetypes/builders/personality-builder/` (13 ISOs)

```bash
python _tools/cex_8f_runner.py "create researcher personality" --kind personality --execute
```

## Examples
See `archetypes/builders/personality-builder/bld_examples_personality.md` for 3 complete examples:
researcher (formal/technical), coach (warm/casual), hacker (dry/playful).

## Related kinds
- `agent` -- full agent definition including capabilities, tools, memory
- `agent_profile` -- runtime AI configuration (model, temperature, token budget)
- `system_prompt` -- complete prompt text; personality is injected as one layer
- `lens` -- domain perspective with routing; personality is voice style without routing
- `user_model` -- cross-session human peer model; may store preferred_personality in Collections
- `episodic_memory` -- records personality switch events over time

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_mental_model]] | sibling | 0.35 |
| [[bld_collaboration_agent]] | downstream | 0.31 |
| [[agent-builder]] | downstream | 0.30 |
| [[p01_kc_agent]] | sibling | 0.29 |
| [[bld_architecture_agent]] | downstream | 0.27 |
| [[p01_kc_brand_voice_consistency_channels]] | sibling | 0.27 |
| [[agent-profile-builder]] | downstream | 0.26 |
| [[bld_schema_runtime_state]] | downstream | 0.26 |
| [[bld_knowledge_card_agent]] | sibling | 0.25 |
| [[bld_collaboration_system_prompt]] | downstream | 0.25 |
