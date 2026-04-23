---
kind: architecture
id: bld_architecture_handoff
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of handoff — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Handoff"
version: "1.0.0"
author: n03_builder
tags: [handoff, builder, examples]
tldr: "Golden and anti-examples for handoff construction, demonstrating ideal structure and common pitfalls."
domain: "handoff construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - handoff-builder
  - bld_collaboration_handoff
  - p01_kc_handoff
  - handoff-protocol-builder
  - bld_collaboration_handoff_protocol
  - p03_sp_handoff_builder
  - bld_knowledge_card_handoff
  - bld_schema_handoff
  - bld_instruction_handoff
  - bld_architecture_dispatch_rule
---

## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| task_description | Core body of work the receiver must complete | author | required |
| context_block | Background information the receiver needs to act | author | required |
| scope_fence | Explicit allowed/forbidden paths and operations | author | required |
| commit_rules | How and when to commit work before stopping | author | required |
| signal_instruction | How to emit completion status after finishing | author | required |
| seed_keywords | Domain terms guiding retrieval and search | author | optional |
| dependency_refs | Upstream artifacts this handoff depends on | author | optional |
| naming_convention | File naming pattern (`{MISSION}_{sat}.md`) | system | required |
## Dependency Graph
```
dispatch_rule --produces--> handoff
dag           --produces--> handoff
handoff       --> execution
execution     --produces--> signal
handoff       --referenced_by--> spawn_config
handoff       --referenced_by--> workflow
```
| From | To | Type | Data |
|------|----|------|------|
| dispatch_rule | handoff | data_flow | agent_group selection, mission name |
| dag | handoff | data_flow | task node context, dependency order |
| handoff | execution | data_flow | task, context, scope fence, commit rules |
| execution | signal | data_flow | status (complete/error), score |
| handoff | spawn_config | data_flow | agent_group id, model params |
| handoff | workflow | data_flow | step instructions within larger orchestration |
## Boundary Table
| handoff IS | handoff IS NOT |
|------------|----------------|
| Complete delegation package for one receiver | Conversational prompt with persona |
| Carries task + context + scope + commit rules | Status or event report |
| One handoff per agent_group per mission | Routing policy (who receives what type) |
| Pre-execution artifact (written before spawn) | Dependency graph of tasks |
| Scoped to a single execution unit | Multi-agent orchestration runtime |
| Source of truth for what to do and how to commit | Boot configuration (model, flags, MCPs) |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Routing | dispatch_rule, dag | Decide which agent_group and in what order |
| Delegation | task_description, context_block, seed_keywords | Define the work and its background |
| Boundary | scope_fence, dependency_refs | Constrain what may be touched |
| Commit | commit_rules, signal_instruction | Enforce artifact persistence and status reporting |
| Instantiation | spawn_config, workflow | Consume handoff to launch or sequence execution |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[handoff-builder]] | downstream | 0.51 |
| [[bld_collaboration_handoff]] | downstream | 0.50 |
| [[p01_kc_handoff]] | downstream | 0.43 |
| [[handoff-protocol-builder]] | upstream | 0.41 |
| [[bld_collaboration_handoff_protocol]] | downstream | 0.38 |
| [[p03_sp_handoff_builder]] | upstream | 0.36 |
| [[bld_knowledge_card_handoff]] | upstream | 0.34 |
| [[bld_schema_handoff]] | upstream | 0.34 |
| [[bld_instruction_handoff]] | upstream | 0.33 |
| [[bld_architecture_dispatch_rule]] | sibling | 0.33 |
