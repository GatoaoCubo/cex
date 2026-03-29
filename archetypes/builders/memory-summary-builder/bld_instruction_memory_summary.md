---
kind: instruction
id: bld_instruction_memory_summary
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for memory_summary
pattern: 3-phase pipeline (research -> compose -> validate)
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
2. Read OUTPUT_TEMPLATE.md — fill {{vars}} following SCHEMA constraints
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
