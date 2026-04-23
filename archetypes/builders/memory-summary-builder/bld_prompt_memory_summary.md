---
kind: instruction
id: bld_instruction_memory_summary
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for memory_summary
pattern: 3-phase pipeline (research -> compose -> validate)
quality: 9.2
title: "Instruction Memory Summary"
version: "1.0.0"
author: n03_builder
tags: [memory_summary, builder, examples]
tldr: "Golden and anti-examples for memory summary construction, demonstrating ideal structure and common pitfalls."
domain: "memory summary construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_instruction_memory_scope
  - p11_qg_memory_summary
  - bld_instruction_output_validator
  - bld_instruction_handoff_protocol
  - bld_instruction_retriever_config
  - bld_instruction_chunk_strategy
  - memory-summary-builder
  - bld_instruction_prompt_version
  - bld_instruction_compression_config
  - bld_instruction_constraint_spec
---

# Instructions: How to Produce a memory_summary
## Phase 1: RESEARCH
1. Identify source_type: is this compressing a single conversation, a full session, multiple sessions, or a document?
2. Assess content volume: how many turns, tokens, or pages? This drives compression method selection
3. Determine fidelity requirements: does the consumer need verbatim phrasing (extractive) or semantic meaning (abstractive)?
4. Define trigger condition: when should summarization fire? Establish numeric threshold (not just "when needed")
5. Map retention requirements: which of entities / decisions / action items / timestamps must survive compression?
6. Estimate compression ratio target: what is the acceptable output size (max_tokens)?
7. Set freshness_decay: how quickly does this summary lose relevance? Match to source_type lifecycle
8. Check for existing memory_summary artifacts to avoid duplicates — same scope, same source_type
9. Confirm summary slug for id: snake_case, lowercase, descriptive of scope (e.g., session_onboarding, conv_debug_auth)
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill `{{vars}}` following SCHEMA constraints
3. Fill frontmatter: all required fields (quality: null — never self-score)
4. Set source_type from enum — must exactly match what is being compressed
5. Set compression_method from enum — justify the choice in ## Compression section
6. Write ## Overview: what this summary captures, when it fires, who consumes it
7. Write ## Compression: method, estimated ratio, explicit list of preserved content, explicit list of dropped content
8. Write ## Trigger: condition type, numeric threshold, what happens on fire (store, inject, replace buffer)
9. Write ## Retention: per-category (entities, decisions, action items, timestamps) — retained or discarded with format note
10. Verify body <= 2048 bytes
11. Verify id matches `^p10_ms_[a-z][a-z0-9_]+$`
## Phase 3: VALIDATE
1. Check QUALITY_GATES.md — verify each HARD gate manually
2. Confirm YAML frontmatter parses without errors
3. Confirm id matches `^p10_ms_` prefix
4. Confirm kind == memory_summary
5. Confirm source_type and compression_method are valid enum values
6. Confirm all 4 body sections present: Overview, Compression, Trigger, Retention
7. HARD gates: frontmatter valid, id pattern matches, enums valid, body sections complete, not a session_state
8. SOFT gates: score against QUALITY_GATES.md — compression ratio stated, trigger threshold numeric, retention fully declared
9. Cross-check boundary: is this reusable across sessions (yes = memory_summary)? Is it ephemeral per-run (no = session_state)? Is it a learned pattern (no = learning_record)?
10. Revise if score < 8.0 before outputting

## ISO Loading

```yaml
loader: cex_skill_loader
injection_point: F3_compose
priority: high
```

```bash
python _tools/cex_skill_loader.py --verify memory
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `instruction` |
| Pillar | P03 |
| Domain | memory summary construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_memory_scope]] | sibling | 0.46 |
| [[p11_qg_memory_summary]] | downstream | 0.44 |
| [[bld_instruction_output_validator]] | sibling | 0.43 |
| [[bld_instruction_handoff_protocol]] | sibling | 0.43 |
| [[bld_instruction_retriever_config]] | sibling | 0.43 |
| [[bld_instruction_chunk_strategy]] | sibling | 0.43 |
| [[memory-summary-builder]] | downstream | 0.43 |
| [[bld_instruction_prompt_version]] | sibling | 0.41 |
| [[bld_instruction_compression_config]] | sibling | 0.41 |
| [[bld_instruction_constraint_spec]] | sibling | 0.41 |
