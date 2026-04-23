---
kind: instruction
id: bld_instruction_collaboration_pattern
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for collaboration_pattern
quality: 9.0
title: "Instruction Collaboration Pattern"
version: "1.0.0"
author: wave1_builder_gen
tags: [collaboration_pattern, builder, instruction]
tldr: "Step-by-step production process for collaboration_pattern"
domain: "collaboration_pattern construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - p03_sp_collaboration_pattern_builder
  - collaboration-pattern-builder
  - bld_memory_collaboration_pattern
  - p11_qg_collaboration_pattern
  - bld_tools_collaboration_pattern
  - bld_instruction_thinking_config
  - bld_instruction_output_validator
  - bld_instruction_agent
  - bld_instruction_action_paradigm
  - bld_instruction_context_doc
---

## Phase 1: RESEARCH  
1. Define collaboration objectives and agent roles within the topology.  
2. Analyze existing multi-agent coordination frameworks (e.g., consensus algorithms, task allocation).  
3. Identify stakeholder interactions and dependency chains.  
4. Map communication protocols (e.g., message formats, synchronization mechanisms).  
5. Evaluate scalability constraints (e.g., agent count, latency thresholds).  
6. Document failure modes and fallback coordination strategies.  

## Phase 2: COMPOSE  
1. Initialize artifact structure using SCHEMA.md’s `pattern_header` block.  
2. Specify `pattern_name` and `pillar` (P12) in the header.  
3. Outline agent types and their interdependencies in `agent_topology`.  
4. Define interaction rules in `protocol_rules` (e.g., voting, queuing).  
5. Embed coordination triggers (e.g., event-based, time-based).  
6. Reference OUTPUT_TEMPLATE.md’s `validation_criteria` section.  
7. Write `use_case_examples` with domain-specific scenarios.  
8. Annotate edge cases in `edge_case_handling`.  
9. Finalize metadata (author, version, revision notes).  

## Phase 3: VALIDATE  
- [ ] Confirm schema compliance (SCHEMA.md).  
- [ ] Verify all agent roles and interactions are explicitly defined.  
- [ ] Ensure topology type is declared (mesh/hierarchical/peer-to-peer/hub-and-spoke).  
- [ ] Confirm communication channels are named and directional.  
- [ ] Verify conflict resolution mechanism is documented.  
- [ ] Validate id matches pattern: p12_collab_[a-z0-9_]+  
- [ ] Run H01-H08 quality gate checks before delivering.  

## Properties

| Property | Value |
|----------|-------|
| Kind | `instruction` |
| Pillar | P03 |
| Domain | collaboration_pattern construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_collaboration_pattern_builder]] | related | 0.36 |
| [[collaboration-pattern-builder]] | downstream | 0.34 |
| [[bld_memory_collaboration_pattern]] | downstream | 0.32 |
| [[p11_qg_collaboration_pattern]] | downstream | 0.32 |
| [[bld_tools_collaboration_pattern]] | downstream | 0.29 |
| [[bld_instruction_thinking_config]] | sibling | 0.28 |
| [[bld_instruction_output_validator]] | sibling | 0.26 |
| [[bld_instruction_agent]] | sibling | 0.26 |
| [[bld_instruction_action_paradigm]] | sibling | 0.26 |
| [[bld_instruction_context_doc]] | sibling | 0.26 |
