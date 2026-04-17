---
id: bld_instruction_bounded_context
kind: instruction
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for bounded_context
version: 1.0.0
quality: null
tags: [bounded_context, builder, instruction]
title: "Instruction Bounded Context Builder"
---
# Instructions: How to Produce a bounded_context
## Phase 1: SCOPE
1. Name the bounded context (noun phrase from domain language, not tech terms)
2. Write the scope statement: what domain model applies HERE (not in other BCs)
3. Identify the team/squad that owns this context
4. List the key aggregates and their relationships within this BC
5. Identify neighboring BCs and their integration patterns
## Phase 2: COMPOSE
1. Read bld_schema_bounded_context.md for required fields
2. Set id: bc_{context_name} (snake_case, domain language)
3. Set domain_vocabulary reference (dv_{context}_vocabulary.md)
4. Document integration patterns with neighboring contexts:
   - ACL (Anti-Corruption Layer): protecting this BC from upstream model
   - OHS (Open Host Service): publishing a public API for consumers
   - CF (Conformist): adopting upstream model as-is
5. Set quality: null -- never self-score
## Phase 3: VALIDATE
1. HARD gates:
   - id follows pattern bc_{context}
   - kind == bounded_context
   - quality == null
   - scope_statement present (what model applies here)
   - team_owner present
   - >= 1 aggregate listed
2. SOFT gates:
   - domain_vocabulary reference present
   - integration patterns documented with rationale
   - upstream_contexts and downstream_contexts listed
   - key invariants stated (business rules that hold within this BC)
