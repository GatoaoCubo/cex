---
quality: 7.8
id: bld_instruction_event_stream
kind: instruction
pillar: P04
title: "Event Stream Builder -- Instruction"
version: 1.0.0
quality: 7.3
tags: [builder, event_stream, instruction]
llm_function: REASON
author: builder
density_score: 0.83
created: "2026-04-17"
updated: "2026-04-17"
related:
  - bld_instruction_interface
  - bld_instruction_instruction
  - bld_instruction_input_schema
  - bld_instruction_golden_test
  - bld_instruction_action_prompt
  - bld_instruction_context_doc
  - bld_instruction_client
  - bld_instruction_handoff
  - bld_instruction_output_validator
  - bld_instruction_memory_scope
---
# Instructions: How to Produce an event_stream
## Phase 1: RESEARCH
1. Identify the domain events flowing through this stream -- what facts are being published?
2. Determine the producer: which service or aggregate emits events to this stream?
3. Determine consumers: which services subscribe and what consumer groups do they form?
4. Decide partitioning strategy: what is the partition key? (orderId, userId, etc.)
5. Set retention policy: how long must events be retained? (reprocessing, audit, replay)
6. Choose delivery semantics: at-most-once, at-least-once, or exactly-once?
7. Define schema: what is the event envelope format (Avro, Protobuf, JSON Schema)?
## Phase 2: COMPOSE
1. Read bld_schema_event_stream.md -- source of truth for required fields
2. Fill frontmatter: id pattern p04_es_{slug}, kind: event_stream, quality: null
3. Write Producer section: who writes to this stream, at what rate
4. Write Consumer Groups section: each group with offset policy and lag tolerance
5. Write Partitioning section: key, count, ordering guarantee
6. Write Retention section: time + bytes, replay window
7. Write Schema section: format, registry, compatibility mode
8. Write Operations section: monitoring, alerting, lag thresholds
## Phase 3: VALIDATE
1. HARD gates: id matches `p04_es_[a-z][a-z0-9_]+`, kind == event_stream, quality == null
2. Producer and at least one consumer group defined
3. Partition key and count specified
4. Retention policy defined (time AND bytes)
5. Delivery semantics specified


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
| [[bld_instruction_interface]] | sibling | 0.32 |
| [[bld_instruction_instruction]] | sibling | 0.32 |
| [[bld_instruction_input_schema]] | sibling | 0.30 |
| [[bld_instruction_golden_test]] | sibling | 0.29 |
| [[bld_instruction_action_prompt]] | sibling | 0.28 |
| [[bld_instruction_context_doc]] | sibling | 0.28 |
| [[bld_instruction_client]] | sibling | 0.26 |
| [[bld_instruction_handoff]] | sibling | 0.26 |
| [[bld_instruction_output_validator]] | sibling | 0.25 |
| [[bld_instruction_memory_scope]] | sibling | 0.25 |
