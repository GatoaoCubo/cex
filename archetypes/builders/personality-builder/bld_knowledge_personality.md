---
kind: knowledge_card
id: bld_knowledge_card_personality
pillar: P01
llm_function: INJECT
purpose: Linked knowledge card for personality-builder (F3 INJECT source)
quality: 8.8
title: "KC: personality (builder-linked)"
version: "1.0.0"
author: n03_builder
tags: [personality, knowledge-card, hermes_origin, hot_swap, P02, soul_md]
tldr: "personality = hot-swappable voice/tone/values layer (HERMES SOUL.md). Activated via /personality [name]. NOT agent, NOT system_prompt."
domain: "persona construction"
created: "2026-04-18"
updated: "2026-04-18"
density_score: 0.90
related:
  - bld_collaboration_agent
  - agent-profile-builder
  - agent-builder
  - p01_kc_agent
  - p01_kc_mental_model
  - bld_architecture_agent
  - bld_knowledge_card_agent
  - bld_collaboration_system_prompt
  - p03_sp_agent_profile_builder
  - bld_instruction_agent
---

# KC: personality

## Definition
A `personality` is a hot-swappable voice/tone/values overlay applied to an agent at runtime.
Implementing the HERMES SOUL.md pattern (NousResearch/hermes-agent), a personality specifies
HOW the agent communicates -- its register, verbosity, humor, core values, sample phrases,
and forbidden phrases -- WITHOUT altering what the agent can do or how its memory works.

## Origin
**HERMES SOUL.md pattern** -- NousResearch/hermes-agent introduced the concept of a
`SOUL.md` file that rides alongside an agent's system prompt, injecting a persistent persona.
CEX adapts this as the `personality` kind: a lightweight, swappable spec that can be
activated or deactivated at runtime without restarting the agent.

## Core Concepts

| Concept | Description |
|---------|-------------|
| register | Communication style: formal, casual, technical, playful |
| verbosity | Response length preference: terse, balanced, verbose |
| humor | Levity calibration: off, dry, warm |
| values | 3-5 core principles driving persona behavior |
| tone_examples | Verbatim sample phrases the persona would say |
| anti_patterns | Phrases this persona would NEVER say |
| hot_swap | Instantaneous persona change via /personality command |

## When to use
- When an agent must adapt voice for different audiences (technical vs. casual)
- When building multi-persona systems (researcher mode, coach mode, hacker mode)
- When implementing SOUL.md-style persona override in a HERMES-pattern agent
- When separating "who the agent is" (agent kind) from "how it speaks right now" (personality kind)

## Boundaries
| Kind | Relationship | Boundary |
|------|-------------|----------|
| agent | Carries the active personality | agent = full spec; personality = voice only |
| agent_profile | May reference active personality | agent_profile = runtime AI config; personality = voice override |
| system_prompt | May instruct "use personality X" | system_prompt = full prompt; personality = one injected layer |
| lens | Domain perspective | lens = routing + domain knowledge; personality = voice style |

## Activation Pattern
```
User: /personality researcher
Agent: loads p02_per_researcher.md
       injects voice.register=technical, verbosity=verbose, humor=dry
       applies values and tone_examples to next responses
User: /personality default
Agent: reverts to default voice profile
```

## Builder
`archetypes/builders/personality-builder/`
Full canonical KC: `N00_genesis/P01_knowledge/library/kind/kc_personality.md`

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_agent]] | downstream | 0.35 |
| [[agent-profile-builder]] | downstream | 0.34 |
| [[agent-builder]] | downstream | 0.34 |
| [[p01_kc_agent]] | sibling | 0.33 |
| [[p01_kc_mental_model]] | sibling | 0.32 |
| [[bld_architecture_agent]] | downstream | 0.30 |
| [[bld_knowledge_card_agent]] | sibling | 0.28 |
| [[bld_collaboration_system_prompt]] | downstream | 0.27 |
| [[p03_sp_agent_profile_builder]] | downstream | 0.24 |
| [[bld_instruction_agent]] | downstream | 0.24 |
