---
quality: 8.8
quality: 8.2
kind: collaboration
id: bld_collaboration_user_model
pillar: P12
llm_function: COLLABORATE
purpose: How user-model-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
title: "Collaboration: user-model-builder"
version: "1.0.0"
author: n03_builder
tags: [user_model, builder, collaboration, honcho, P12]
tldr: "user-model-builder role in crews: dialectic peer record specialist. Receives peer_id + workspace; produces cross-session user model consumed by agent builders and system prompt builders."
domain: "user model construction"
created: "2026-04-18"
updated: "2026-04-18"
density_score: 0.90
related:
  - bld_collaboration_model_card
  - bld_collaboration_session_state
  - bld_collaboration_entity_memory
  - bld_collaboration_memory_scope
  - bld_collaboration_agent
  - bld_collaboration_system_prompt
  - bld_collaboration_knowledge_card
  - bld_collaboration_context_doc
  - bld_collaboration_session_backend
  - bld_collaboration_runtime_state
---

# Collaboration: user-model-builder

## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what is the persistent, cross-session dialectic representation of this specific human peer, and how is it configured for Honcho-style insight injection?"
I do not store any-entity facts. I do not store ephemeral session data. I do not describe AI agents. I do not log raw events.
I produce compact, dialectic-configured peer records so agents can ground their responses in accumulated user context and adapt behavior across sessions without re-asking.

## Crew Compositions

### Crew: "Personalized Agent Build"
```
  1. user-model-builder -> "cross-session peer model with preferences + working_style"
  2. system-prompt-builder -> "system prompt that injects peer model context"
  3. agent-builder -> "agent wired to honcho SDK with pre/post-response insight loop"
```

### Crew: "Memory System"
```
  1. user-model-builder -> "cross-session peer model (derived facts about the human)"
  2. entity-memory-builder -> "factual records about orgs, tools, products in context"
  3. session-state-builder -> "ephemeral snapshot for current active session"
  4. episodic-memory-builder -> "raw event log for audit and replay"
```

### Crew: "Support Agent Context"
```
  1. user-model-builder -> "customer peer model with support_history + product_context collections"
  2. knowledge-card-builder -> "domain knowledge cards for product context injection"
  3. agent-builder -> "support agent with Honcho loop + KC injection"
```

## Handoff Protocol

### I Receive
- peer_id: canonical user identifier
- workspace: tenant namespace
- optional: known preferences or working style facts from prior context
- optional: domain context for custom collection names

### I Produce
- user_model artifact (.md with YAML frontmatter)
- committed to: nucleus P10 dir (e.g., `N04_knowledge/P10_memory/p10_um_{peer_id}.md`)
- kind registered in: `.cex/kinds_meta.json` (key: `user_model`)

### I Signal
- signal: complete (with quality score from quality gate)
- if quality < 8.0: signal retry with failure reasons (most common: missing collections, dialectic not configured)

## Builders I Depend On
| Builder | Why |
|---------|-----|
| knowledge-card-builder | KCs provide domain context that seeds initial Collections |
| system-prompt-builder | System prompts declare how peer.chat results are injected |
| session-state-builder | Session state provides the ephemeral context that user_model derives from |

## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| agent-builder | Agents wire Honcho SDK; need user_model spec to configure the loop |
| system-prompt-builder | System prompts reference peer.chat and session.representation outputs |
| session-state-builder | Session state may reference peer_id for cross-kind context linking |

## Conflict Resolution with Sibling Builders
| Scenario | Resolution |
|----------|-----------|
| Fact belongs in user_model vs entity_memory | user_model: derived insight about THIS human via dialectic loop. entity_memory: factual attribute about ANY named entity (org, product, tool). |
| Fact belongs in user_model vs session_state | user_model: persists cross-session, version-controlled, dialectic-derived. session_state: resets each session, never committed to version control. |
| Fact belongs in user_model vs episodic_memory | user_model: synthesized derived model of the person. episodic_memory: raw event/message log for replay. |
| Fact belongs in user_model vs agent_profile | user_model: describes the HUMAN peer. agent_profile: describes the AI agent's capabilities. |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_model_card]] | sibling | 0.39 |
| [[bld_collaboration_session_state]] | sibling | 0.39 |
| [[bld_collaboration_entity_memory]] | sibling | 0.38 |
| [[bld_collaboration_memory_scope]] | sibling | 0.37 |
| [[bld_collaboration_agent]] | sibling | 0.36 |
| [[bld_collaboration_system_prompt]] | sibling | 0.36 |
| [[bld_collaboration_knowledge_card]] | sibling | 0.35 |
| [[bld_collaboration_context_doc]] | sibling | 0.35 |
| [[bld_collaboration_session_backend]] | sibling | 0.35 |
| [[bld_collaboration_runtime_state]] | sibling | 0.34 |
