---
kind: architecture
id: bld_architecture_mental_model
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of mental_model — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Mental Model"
version: "1.0.0"
author: n03_builder
tags: [mental_model, builder, examples]
tldr: "Golden and anti-examples for mental model construction, demonstrating ideal structure and common pitfalls."
domain: "mental model construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - mental-model-builder
  - p03_ins_mental_model
  - bld_knowledge_card_mental_model
  - bld_collaboration_mental_model
  - p01_kc_mental_model
  - bld_architecture_system_prompt
  - bld_architecture_agent
  - bld_architecture_router
  - p11_qg_mental_model
  - p03_sp_mental_model_builder
---

# Architecture: mental_model in the CEX

This ISO operationalizes a mental model -- a compact analogy or abstraction that guides reasoning.
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| frontmatter block | 23-field metadata header (id, kind, pillar, domain, target_agent, etc.) | mental-model-builder | active |
| routing_rules | Keyword-to-action mappings with confidence thresholds | author | active |
| decision_trees | If/then/else branching logic for complex routing decisions | author | active |
| priorities | Ordered list of objectives the agent optimizes for | author | active |
| heuristics | Rules of thumb for ambiguous situations without clear routing | author | active |
| domain_map | Boundaries defining what the agent knows and does not know | author | active |
| personality_traits | Behavioral tendencies that shape tone and approach | author | active |
## Dependency Graph
```
knowledge_card  --produces-->  mental_model  --consumed_by-->  agent
domain_context  --produces-->  mental_model  --referenced_by-> router
mental_model    --signals-->   routing_decision
```
| From | To | Type | Data |
|------|----|------|------|
| knowledge_card (P01) | mental_model | data_flow | domain facts informing routing rules and heuristics |
| context_doc (P01) | mental_model | data_flow | domain context shaping boundary definitions |
| mental_model | agent (P02) | consumes | agent loads mental model as cognitive operating system |
| mental_model | router (P02) | data_flow | routing rules referenced by dispatch logic |
| mental_model | routing_decision | produces | specific route selected for incoming task |
| system_prompt (P03) | mental_model | dependency | system prompt identity constrains mental model scope |
## Boundary Table
| mental_model IS | mental_model IS NOT |
|-----------------|---------------------|
| A design-time cognitive map with routing and decisions | A runtime-accumulated state (runtime_state P10) |
| Defines how an agent routes, prioritizes, and decides | An agent identity with capabilities (agent P02) |
| Static until explicitly updated by author | A task-routing dispatch table (router P02) |
| Composed of rules, trees, heuristics, and domain maps | An evaluation framework with scoring (scoring_rubric P07) |
| Scoped to one agent or one domain | A universal routing system for all agents |
| Declared personality traits, not emergent behavior | A learned behavioral pattern (learning_record P10) |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Context | knowledge_card, context_doc, system_prompt | Supply domain knowledge and identity constraints |
| Routing | routing_rules, decision_trees | Define how tasks are classified and directed |
| Judgment | priorities, heuristics | Guide decisions when routing rules are ambiguous |
| Identity | domain_map, personality_traits | Scope boundaries and behavioral tendencies |
| Output | routing_decision, agent | Produce routing decisions consumed by the agent |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[mental-model-builder]] | upstream | 0.54 |
| [[p03_ins_mental_model]] | upstream | 0.49 |
| [[bld_knowledge_card_mental_model]] | upstream | 0.47 |
| [[bld_collaboration_mental_model]] | upstream | 0.46 |
| [[p01_kc_mental_model]] | upstream | 0.46 |
| [[bld_architecture_system_prompt]] | sibling | 0.44 |
| [[bld_architecture_agent]] | sibling | 0.43 |
| [[bld_architecture_router]] | sibling | 0.41 |
| [[p11_qg_mental_model]] | downstream | 0.40 |
| [[p03_sp_mental_model_builder]] | upstream | 0.40 |
