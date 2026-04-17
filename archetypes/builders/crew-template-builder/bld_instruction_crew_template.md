---
kind: instruction
id: bld_instruction_crew_template
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for crew_template
quality: 8.9
title: "Instruction Crew Template"
version: "1.0.0"
author: n03_wave8_builder
tags: [crew_template, builder, instruction, composable, crewai]
tldr: "Step-by-step production process for crew_template"
domain: "crew_template construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.87
---

## Phase 1: RESEARCH
1. Identify crew purpose and task boundary (what the team will produce).
2. Decompose task into role responsibilities; each responsibility maps to a role_assignment.
3. Analyze dependency graph across roles (which outputs feed which inputs).
4. Pick process topology: sequential (linear), hierarchical (manager-workers), consensus (peer-voting).
5. Determine memory-scope per role: private (no leakage), shared (team-visible), persistent (cross-session).
6. Research CrewAI Process, AutoGen GroupChat, or OpenAI Swarm pattern matching closest to this crew.

## Phase 2: COMPOSE
1. Reference SCHEMA.md for required fields (crew_name, purpose, roles, process, memory_scope, success_criteria).
2. Populate OUTPUT_TEMPLATE.md with crew blueprint from design.
3. Reference each role via its role_assignment id (p02_ra_{role}.md); do NOT inline role identity.
4. Define process block: for sequential list order, hierarchical name manager role, consensus set voting rule.
5. Define handoff_protocol: message format (A2A Task, OpenAI transfer function, or composable-crew native).
6. Set memory_scope: map each role to private|shared|persistent with retention hint.
7. Encode success_criteria as measurable post-conditions (quality threshold, artifact count, gate pass).
8. Add metadata: crewai_equivalent, autogen_equivalent, swarm_equivalent (for taxonomy mapping).
9. Proofread: all role refs valid, process topology matches dependency graph.

## Phase 3: VALIDATE
- [ ] All roles referenced exist as role_assignment artifacts.
- [ ] Process topology matches task dependency structure.
- [ ] Memory-scope defined for every role.
- [ ] Handoff-protocol named and compatible with all participating roles.
- [ ] success_criteria measurable and checkable post-run.
- [ ] File size <= 4096 bytes.
