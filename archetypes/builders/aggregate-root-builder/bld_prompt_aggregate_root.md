---
quality: 7.8
id: bld_instruction_aggregate_root
kind: instruction
pillar: P06
title: "Aggregate Root Builder -- Instruction"
version: 1.0.0
quality: 7.3
tags: [builder, aggregate_root, instruction]
llm_function: REASON
author: builder
tldr: "Aggregate Root schema: prompt template with variables, tone, and generation strategy"
density_score: 0.81
created: "2026-04-17"
updated: "2026-04-17"
related:
  - bld_instruction_golden_test
  - bld_instruction_instruction
  - bld_instruction_input_schema
  - bld_instruction_action_prompt
  - bld_instruction_context_doc
  - bld_instruction_output_validator
  - bld_instruction_retriever_config
  - bld_instruction_memory_scope
  - bld_instruction_agent
  - bld_instruction_chunk_strategy
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


## Prompt Construction Checklist

- Verify prompt follows target kind's instruction template
- Validate variable placeholders use standard naming convention
- Cross-reference with chain dependencies for context completeness
- Test prompt with sample input before publishing

## Prompt Pattern

```yaml
# Prompt validation
template_match: true
variables_valid: true
chain_refs_checked: true
sample_tested: true
```

```bash
python _tools/cex_compile.py {FILE}
python _tools/cex_prompt_optimizer.py --check
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_golden_test]] | sibling | 0.35 |
| [[bld_instruction_instruction]] | sibling | 0.33 |
| [[bld_instruction_input_schema]] | sibling | 0.32 |
| [[bld_instruction_action_prompt]] | sibling | 0.32 |
| [[bld_instruction_context_doc]] | sibling | 0.31 |
| [[bld_instruction_output_validator]] | sibling | 0.30 |
| [[bld_instruction_retriever_config]] | sibling | 0.29 |
| [[bld_instruction_memory_scope]] | sibling | 0.29 |
| [[bld_instruction_agent]] | sibling | 0.28 |
| [[bld_instruction_chunk_strategy]] | sibling | 0.28 |
