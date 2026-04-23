---
kind: collaboration
id: bld_collaboration_procedural_memory
pillar: P12
llm_function: COLLABORATE
purpose: How procedural_memory-builder works in crews with other CEX builders
quality: 9.1
title: "Collaboration: procedural_memory-builder"
version: "2.0.0"
author: n06_commercial
tags: [procedural_memory, builder, collaboration]
tldr: "procedural_memory-builder consumes memory_architecture + consolidation_policy, produces skill library specs for agent-builder and knowledge-card-builder"
domain: "LLM agent procedural memory"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.90
related:
  - bld_collaboration_memory_architecture
  - bld_collaboration_consolidation_policy
  - procedural-memory-builder
  - bld_collaboration_skill
  - memory-architecture-builder
  - p03_sp_procedural_memory_builder
  - bld_instruction_procedural_memory
  - bld_knowledge_card_procedural_memory
  - bld_architecture_skill
  - bld_architecture_procedural_memory
---

## Crew Role
Defines the skill storage layer within a complete agent memory system. Consumes
memory_architecture (tier, procedural backend) and consolidation_policy (skill TTL,
versioning rules) to produce procedural_memory artifacts that specify the skill library
structure. Other builders reference procedural_memory for skill availability at runtime.

## Receives From
| Builder | What | Format |
|---------|------|--------|
| memory-architecture-builder | Tier, procedural layer backend config | memory_architecture artifact |
| consolidation-policy-builder | Skill TTL, versioning policy, eviction rules | consolidation_policy artifact |
| knowledge-card-builder | Domain research on Voyager/Reflexion/ExpeL | knowledge_card artifact |

## Produces For
| Builder | What | Format |
|---------|------|--------|
| agent-builder | Skill availability per tier for system prompt | Skill list + tier summary |
| knowledge-card-builder | Lessons from skill library patterns | Feedback on domain |
| N06 commercial review | Enterprise skill ACL + versioning config | Tier matrix |

## Boundary
Does NOT produce:
- Memory layer definitions or backend specs (-> memory_architecture kind)
- Memory lifecycle rules or eviction policies (-> consolidation_policy kind)
- Fact/entity storage (-> entity_memory or knowledge_index kinds)
- Semantic memory (-> knowledge_card or knowledge_graph kinds)
- Agent routing or tool call configs (-> agent kind, P02)

## Dispatch Pattern
In a grid dispatch building a complete agent memory system:
1. N06 (commercial) builds `memory_architecture` first (tier, layer definitions)
2. N06 (commercial) builds `consolidation_policy` (lifecycle rules)
3. N04 (knowledge) builds `procedural_memory` for each skill domain
4. N01 (intelligence) or N06 validates tier matrices are consistent across all three
5. N07 consolidates: all artifacts form the complete P10 memory cluster spec

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_memory_architecture]] | sibling | 0.65 |
| [[bld_collaboration_consolidation_policy]] | sibling | 0.63 |
| [[procedural-memory-builder]] | upstream | 0.53 |
| [[bld_collaboration_skill]] | sibling | 0.44 |
| [[memory-architecture-builder]] | upstream | 0.42 |
| [[p03_sp_procedural_memory_builder]] | upstream | 0.42 |
| [[bld_instruction_procedural_memory]] | upstream | 0.41 |
| [[bld_knowledge_card_procedural_memory]] | upstream | 0.41 |
| [[bld_architecture_skill]] | upstream | 0.38 |
| [[bld_architecture_procedural_memory]] | upstream | 0.38 |
