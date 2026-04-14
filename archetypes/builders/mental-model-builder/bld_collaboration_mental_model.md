---
kind: collaboration
id: bld_collaboration_mental_model
pillar: P02
llm_function: COLLABORATE
purpose: How mental-model-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.0
title: "Collaboration Mental Model"
version: "1.0.0"
author: n03_builder
tags: [mental_model, builder, examples]
tldr: "Golden and anti-examples for mental model construction, demonstrating ideal structure and common pitfalls."
domain: "mental model construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Collaboration: mental-model-builder

This ISO operationalizes a mental model -- a compact analogy or abstraction that guides reasoning.
## My Role in Crews
I am a COGNITIVE ARCHITECT. I answer ONE question: "how does this agent route tasks, make decisions, and prioritize work?"
I produce cognitive maps with routing rules, decision trees, priorities, heuristics, and domain boundaries. I do NOT define agent identity and capabilities (agent-builder), implement runtime routing infrastructure (router-builder), or manage runtime state (session-state-builder).
## Crew Compositions
### Crew: "Agent Design" (standard)
```
  1. knowledge-card-builder -> "domain facts that inform routing rules and heuristics"
  2. mental-model-builder   -> "cognitive blueprint: routing, decisions, priorities, boundaries"
  3. agent-builder          -> "complete agent definition integrating the mental model"
```
### Crew: "Full Agent Pipeline"
```
  1. knowledge-card-builder  -> "domain facts"
  2. model-card-builder      -> "LLM capabilities and constraints for routing decisions"
  3. mental-model-builder    -> "cognitive blueprint with routing and decision trees"
  4. system-prompt-builder   -> "assembles identity, mental model, and persona"
  5. agent-builder           -> "complete agent definition"
  6. boot-config-builder     -> "provider initialization and MCP wiring"
```
### Crew: "Cognitive Audit"
```
  1. mental-model-builder (read mode) -> "parse existing routing rules and decisions"
  2. quality-gate-builder             -> "score routing coverage and decision completeness"
  3. learning-record-builder          -> "capture findings and improvement patterns"
```
## Handoff Protocol
### I Receive
- seeds: agent name, domain, task types handled, routing keywords, decision branches, domain boundaries
- optional: knowledge_cards for domain context, agent artifact for identity scoping, prior mental model to upgrade
### I Produce
- mental_model artifact (YAML, 14 required + 9 recommended frontmatter fields, routing rules with confidence thresholds, decision trees with if/then/else, max 5KB)
- committed to: `cex/P02_model/examples/p02_mm_{agent_slug}.yaml`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with specific gate failures
## Builders I Depend On
- knowledge-card-builder: domain facts inform routing rules and heuristics
- agent-builder: agent identity and capabilities scope what routing rules are valid (optional)
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| agent-builder        | integrates mental model as the agent's cognitive component |
| system-prompt-builder | embeds routing rules and decision trees into agent instructions |
| boot-config-builder  | uses routing constraints from mental model for initialization |
| quality-gate-builder | validates routing coverage and decision tree completeness |
