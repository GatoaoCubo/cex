---
kind: collaboration
id: bld_collaboration_router
pillar: P02
llm_function: COLLABORATE
purpose: How router-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.0
title: "Collaboration Router"
version: "1.0.0"
author: n03_builder
tags: [router, builder, examples]
tldr: "Golden and anti-examples for router construction, demonstrating ideal structure and common pitfalls."
domain: "router construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - router-builder
  - bld_collaboration_dispatch_rule
  - bld_collaboration_agent
  - bld_collaboration_fallback_chain
  - bld_collaboration_system_prompt
  - bld_collaboration_model_card
  - bld_collaboration_mental_model
  - p03_ins_router
  - bld_collaboration_workflow
  - bld_collaboration_model_provider
---

# Collaboration: router-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "how should tasks be routed to agents/agent_groups based on patterns and confidence?"
I produce route tables with confidence thresholds, fallback routes, and escalation policies. I do not handle simple keyword dispatch or multi-step orchestration.
## Crew Compositions
### Crew: "Task Dispatch System"
```
  1. agent-builder            -> "agent identities and capability declarations"
  2. router-builder           -> "route table mapping task patterns to agents with confidence thresholds"
  3. dispatch-rule-builder    -> "simple keyword-to-destination rules for unambiguous cases"
```
### Crew: "Resilient Routing Layer"
```
  1. router-builder           -> "primary route table with confidence scoring"
  2. fallback-chain-builder   -> "ordered fallback sequence when primary route confidence is low"
  3. runtime-rule-builder     -> "timeout and retry rules applied during routing decisions"
```
### Crew: "Multi-Agent Orchestration Pack"
```
  1. agent-card-builder   -> "agent_group capability specs that define valid routing targets"
  2. router-builder           -> "routing logic directing tasks to correct agent_groups"
  3. workflow-builder         -> "multi-step orchestration after routing resolves the first agent"
  4. spawn-config-builder     -> "spawn parameters for the resolved routing target"
```
## Handoff Protocol
### I Receive
- seeds: task domains, available agents/agent_groups, routing criteria, confidence threshold requirements
- optional: existing dispatch rules to extend, load balancing requirements, escalation policy
### I Produce
- router artifact (YAML frontmatter 14 fields + route table + fallback routes + escalation policy, max 4096 bytes)
- committed to: `cex/P02/examples/p02_router_{name}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
- agent-builder: provides agent capability declarations used as routing targets
- model-card-builder: provides LLM capability profiles that inform routing decisions
- agent-card-builder: provides agent_group domain specs that define valid route destinations
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| dispatch-rule-builder | Handles simple cases; defers confidence-based routing to me |
| fallback-chain-builder | Chains fallbacks after my route table fails to match with sufficient confidence |
| workflow-builder | Uses my routing output to determine which agent executes each workflow step |
| spawn-config-builder | Configures spawn parameters for the agent_group I resolved as the target |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[router-builder]] | related | 0.52 |
| [[bld_collaboration_dispatch_rule]] | sibling | 0.49 |
| [[bld_collaboration_agent]] | sibling | 0.45 |
| [[bld_collaboration_fallback_chain]] | sibling | 0.43 |
| [[bld_collaboration_system_prompt]] | sibling | 0.41 |
| [[bld_collaboration_model_card]] | sibling | 0.40 |
| [[bld_collaboration_mental_model]] | sibling | 0.39 |
| [[p03_ins_router]] | related | 0.38 |
| [[bld_collaboration_workflow]] | sibling | 0.38 |
| [[bld_collaboration_model_provider]] | sibling | 0.37 |
