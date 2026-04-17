---
id: bld_instruction_aggregate_root
kind: instruction
pillar: P06
title: "Aggregate Root Builder -- Instruction"
version: 1.0.0
quality: 5.4
tags: [builder, aggregate_root, instruction]
llm_function: REASON
density_score: 0.81
updated: "2026-04-17"
---
# Instructions: How to Produce an aggregate_root
## Phase 1: RESEARCH
1. Identify the domain concept this aggregate owns -- what real-world entity is the root?
2. Map the cluster: which child entities and value objects fall inside this boundary?
3. Enumerate invariants: what rules must ALWAYS be true after any command executes?
4. Identify commands: what operations mutate state within this aggregate?
5. Identify domain events: what facts does this aggregate emit on state change?
6. Determine repository interface: how is this aggregate persisted and retrieved?
## Phase 2: COMPOSE
1. Read bld_schema_aggregate_root.md -- source of truth for required fields
2. Read bld_output_template_aggregate_root.md -- fill following SCHEMA constraints
3. Fill frontmatter: id pattern p06_ar_{slug}, kind: aggregate_root, quality: null
4. Write Identity section: root entity name, bounded context, and cluster members
5. Write Invariants section: numbered hard rules, each concrete and verifiable
6. Write Commands section: allowed mutations with preconditions and postconditions
7. Write Events section: domain events emitted, their payloads and triggers
8. Write Repository section: find-by-id + save interface, no query methods
9. Write Boundaries section: what is inside vs outside this aggregate
## Phase 3: VALIDATE
1. Check bld_quality_gate_aggregate_root.md -- run all HARD gates
2. HARD gates: id matches `p06_ar_[a-z][a-z0-9_]+`, kind == aggregate_root, quality == null
3. Invariants are concrete not aspirational, commands have pre/postconditions
4. Aggregate does not reference other aggregates by object -- only by ID
5. If score < 8.0: revise before outputting
