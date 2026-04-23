---
kind: instruction
id: bld_instruction_context_map
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for context_map
pattern: 3-phase pipeline (define -> compose -> validate)
quality: 8.7
title: "Instruction Context Map"
version: "1.0.0"
author: n03_builder
tags: [context_map, builder, instruction]
tldr: "3-phase: enumerate BCs and relationships, assign DDD patterns, document team coupling and integration details."
domain: "context map construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
related:
  - bld_instruction_output_validator
  - bld_instruction_retriever_config
  - bld_instruction_memory_scope
  - bld_instruction_chunk_strategy
  - bld_instruction_handoff_protocol
  - bld_instruction_prompt_version
  - bld_instruction_constraint_spec
  - bld_instruction_hook_config
  - bld_instruction_context_doc
  - bld_instruction_hitl_config
---

# Instructions: How to Produce a context_map

## Phase 1: DEFINE

1. Identify all bounded contexts in scope (name, owning team, core/supporting/generic)
2. For each pair of contexts: does one depend on the other? in what direction?
3. For each relationship: determine the integration pattern:
   - Does downstream translate upstream model? -> ACL
   - Does upstream expose formal API/protocol? -> OHS
   - Does downstream adopt upstream model directly? -> Conformist
   - Do two teams co-evolve together? -> Partnership
   - Do teams share a code subset? -> Shared Kernel
4. For each relationship: determine sync vs async vs batch integration
5. For ACL relationships: identify who owns the translation layer
6. For OHS relationships: identify the published language/API version
7. Assess team coupling level: Low/Medium/High/Very High per relationship

## Phase 2: COMPOSE

1. Read SCHEMA.md and OUTPUT_TEMPLATE.md
2. Fill frontmatter: all required fields (quality: null)
3. Set id: `p08_cm_{system_slug}` -- verify pattern `^p08_cm_[a-z][a-z0-9_]+$`
4. Set contexts_count to match the number of BCs in the body
5. Write Bounded Contexts section: table of all BCs
6. Write Relationships section: upstream/downstream table with pattern and integration_type
7. Write Integration Details section: translation layers, protocols, sync/async
8. Write Team Coupling section: coupling level, risk, mitigation per relationship
9. Verify body <= 4096 bytes

## Phase 3: VALIDATE

1. Confirm id matches `^p08_cm_[a-z][a-z0-9_]+$`
2. Confirm kind == context_map
3. Confirm contexts_count matches body count
4. Confirm all relationships have upstream, downstream, pattern
5. Confirm all 4 body sections present
6. Confirm ACL relationships have translation_layer identified
7. Confirm OHS relationships have protocol/API reference
8. Cross-check: not bounded_context (single BC), not component_map (deployment)
9. Confirm quality: null
10. Revise if score < 8.0


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_output_validator]] | sibling | 0.37 |
| [[bld_instruction_retriever_config]] | sibling | 0.37 |
| [[bld_instruction_memory_scope]] | sibling | 0.36 |
| [[bld_instruction_chunk_strategy]] | sibling | 0.36 |
| [[bld_instruction_handoff_protocol]] | sibling | 0.35 |
| [[bld_instruction_prompt_version]] | sibling | 0.35 |
| [[bld_instruction_constraint_spec]] | sibling | 0.34 |
| [[bld_instruction_hook_config]] | sibling | 0.33 |
| [[bld_instruction_context_doc]] | sibling | 0.33 |
| [[bld_instruction_hitl_config]] | sibling | 0.31 |
