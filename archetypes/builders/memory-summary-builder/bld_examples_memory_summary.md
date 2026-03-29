---
kind: examples
id: bld_examples_memory_summary
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of memory_summary artifacts
pattern: few-shot learning — LLM reads these before producing
---

# Examples: memory-summary-builder
## Golden Example
INPUT: "Create memory summary for a customer support session — compress after 15 turns, keep entity mentions and decisions, hybrid method"
OUTPUT:
```yaml
id: p10_ms_support_session_hybrid
kind: memory_summary
pillar: P10
version: "1.0.0"
created: "2026-03-29"
updated: "2026-03-29"
author: "EDISON"
name: "Customer Support Session Summary"
source_type: session
compression_method: hybrid
quality: null
tags: [memory_summary, support, session, hybrid]
tldr: "Hybrid compression of support sessions at 15 turns; retains entities + decisions; drops filler. 8:1 ratio."
max_tokens: 512
trigger: turn_count
source_window: 15
retain_entities: true
retain_timestamps: false
freshness_decay: 0.1
description: "Compresses customer support sessions after 15 turns using hybrid method; preserves issue entities, resolutions, and commitments."
```
## Overview
Compresses customer support session conversations after 15 turns using hybrid method.
Consumed by the support agent at session resume to restore context without full transcript replay.
## Compression
Method: hybrid — abstractive narrative for conversation flow + extractive lift for issue details and resolutions
Ratio: ~8:1 (avg 4000 tokens input -> 512 tokens output)
Preserved: customer name, issue ID, product names, error codes, resolution steps agreed upon, open action items
Dropped: greetings, repeated clarification loops, acknowledgment turns ("got it", "sure", "one moment")
## Trigger
Condition: turn_count >= 15
On fire: summarize last source_window turns, prepend to context buffer, drop raw turns beyond window
## Retention
Entities: retained — customer name, product names, error codes, ticket IDs, URLs
Decisions: retained — resolution steps, escalation decisions, refund approvals
Action items: retained — pending tasks with owner (agent/customer) and deadline if stated
Timestamps: discarded — relative time ("earlier today") preserved in narrative; absolute timestamps dropped

WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches ^p10_ms_ pattern (H02 pass)
- kind: memory_summary (H04 pass)
- source_type: session (valid enum, H07 pass)
- compression_method: hybrid (valid enum, H08 pass)
- all 4 body sections present (H09 pass)
- no session_state fields present (H10 pass)
- trigger has numeric threshold: 15 (SOFT pass)
- compression ratio stated: ~8:1 (SOFT pass)
- retention fully declared per category (SOFT pass)
- max_tokens defined: 512 (SOFT pass)
- tldr: 73 chars <= 160 (SOFT pass)
- tags: 4 items, includes "memory_summary" (SOFT pass)

## Anti-Example
INPUT: "Create memory summary for agent sessions"
BAD OUTPUT:
```yaml
id: session-summary
kind: summary
pillar: memory
compression: gzip
quality: 8.5
tags: [summary]
```
Summarizes agent sessions when context gets long.
FAILURES:
1. id: "session-summary" has hyphens and no `p10_ms_` prefix -> H02 FAIL
2. kind: "summary" not "memory_summary" -> H04 FAIL
3. pillar: "memory" not "P10" -> H06 FAIL
4. compression: "gzip" not a valid enum (abstractive/extractive/hybrid/sliding_window) -> H08 FAIL
5. quality: 8.5 (not null) -> H05 FAIL
6. Missing fields: source_type, version, created, updated, author, tldr, max_tokens, trigger -> H06 FAIL
7. tags: only 1 item, missing "memory_summary" -> SOFT FAIL
8. Body missing all 4 required sections -> H09 FAIL
9. No trigger threshold defined — "when context gets long" is not a spec -> SOFT FAIL
10. No retention policy — entities/decisions/action items status unknown -> SOFT FAIL
