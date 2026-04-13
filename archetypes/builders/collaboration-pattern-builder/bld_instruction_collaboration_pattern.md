---
kind: instruction
id: bld_instruction_collaboration_pattern
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for collaboration_pattern
quality: null
title: "Instruction Collaboration Pattern"
version: "1.0.0"
author: wave1_builder_gen
tags: [collaboration_pattern, builder, instruction]
tldr: "Step-by-step production process for collaboration_pattern"
domain: "collaboration_pattern construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
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
- [ ] ✅ Confirm schema compliance (SCHEMA.md).  
- [ ] ✅ Verify all agent roles and interactions are explicitly defined.  
- [ ] ✅ Ensure protocol rules align with domain constraints.  
- [ ] ✅ Test use_case_examples against OUTPUT_TEMPLATE.md.  
- [ ] ✅ Confirm edge_case_handling covers failure scenarios.
