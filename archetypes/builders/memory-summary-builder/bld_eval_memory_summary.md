---
kind: quality_gate
id: p11_qg_memory_summary
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of memory_summary artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.0
title: "Gate: memory_summary"
version: "1.0.0"
author: "builder_agent"
tags: [quality-gate, memory-summary, P10, compression, retention, freshness]
tldr: "Pass/fail gate for memory_summary artifacts: compression method, retention policy, trigger definition, boundary vs session_state and learning_record."
domain: "memory compression — summarized conversation/session memory injected at runtime"
created: "2026-03-29"
updated: "2026-03-29"
density_score: 0.90
related:
  - bld_examples_memory_summary
  - bld_instruction_memory_summary
  - memory-summary-builder
  - p03_sp_memory_summary_builder
  - p11_qg_chunk_strategy
  - p11_qg_constraint_spec
  - p11_qg_memory_scope
  - p11_qg_retriever_config
  - p11_qg_function_def
  - p11_qg_document_loader
---

## Quality Gate

# Gate: memory_summary
## Definition
| Field | Value |
|---|---|
| metric | memory_summary artifact quality score |
| threshold | 7.0 (publish >= 8.0, golden >= 9.5) |
| operator | weighted_sum |
| scope | all artifacts with `kind: memory_summary` |
## HARD Gates
All must pass (AND logic). Any single failure = REJECT.
| ID | Check | Fail Condition |
|---|---|---|
| H01 | Frontmatter parses as valid YAML | Parse error on frontmatter block |
| H02 | ID matches `^p10_ms_[a-z][a-z0-9_]+$` | ID contains uppercase, hyphens, or missing prefix |
| H03 | ID equals filename stem | `id: p10_ms_foo` but file is `p10_ms_bar.md` |
| H04 | Kind equals literal `memory_summary` | `kind: session_state` or any other value |
| H05 | Quality field is null | `quality: 8.0` or any non-null value |
| H06 | All required fields present | Missing source_type, compression_method, or tldr |
| H07 | source_type is valid enum value | `source_type: chat` (not in enum) |
| H08 | compression_method is valid enum value | `compression_method: delta` (not in enum) |
| H09 | Body contains all 4 required sections | Missing Overview, Compression, Trigger, or Retention |
| H10 | Not a session_state (no ephemeral runtime fields) | Contains `active_task`, `current_tool`, or cursor position fields |
## SOFT Scoring
Weights sum to 100%.
| Dimension | Weight | Criteria |
|---|---|---|
| Compression clarity | 1.0 | Ratio, preserved content, and dropped content all specified |
| Trigger precision | 1.0 | Threshold numeric value defined; condition unambiguous |
| Retention policy | 1.0 | Entity, decision, and action item retention all declared |
| Boundary declaration | 1.0 | Explicitly NOT session_state (ephemeral) and NOT learning_record (persistent) |
| Freshness decay | 0.5 | freshness_decay in [0,1]; value apownte for source_type |
| Source window | 0.5 | source_window integer defined; matches compression method |
| Max tokens constraint | 0.5 | max_tokens defined and reasonable for use case |
| Density | 1.0 | No filler; every field load-bearing |
| Tag completeness | 0.5 | >= 3 tags, includes "memory_summary" |
| tldr quality | 1.0 | <= 160ch, dense, captures scope and method |
| Domain specificity | 1.0 | Fields specific to memory compression domain |
| Anti-pattern avoidance | 1.0 | No lossy compression without entity retention; no over-compression warnings |
## Actions
| Score | Tier | Action |
|---|---|---|
| >= 9.5 | Golden | Publish to pool as golden reference |
| >= 8.0 | Publish | Publish to pool, add to routing index |
| >= 7.0 | Review | Flag for improvement before publish |
| < 7.0 | Reject | Return to author with specific gate failures |
## Bypass
| Field | Value |
|---|---|
| conditions | Experimental compression method under active testing, not shipped to production |
| approver | Author self-certification with comment explaining experimental scope |
| audit_trail | Bypass note in frontmatter comment with expiry date |
| expiry | 14d — experimental summaries must be promoted to >= 7.0 or removed |
| never_bypass | H01 (unparseable YAML breaks all tooling), H05 (self-scored gates corrupt quality metrics), H10 (session_state confusion corrupts memory layer) |

## Examples

# Examples: memory-summary-builder
## Golden Example
INPUT: "Create memory summary for a costmer support session — compress after 15 turns, keep entity mentions and decisions, hybrid method"
OUTPUT:
```yaml
id: p10_ms_support_session_hybrid
kind: memory_summary
pillar: P10
version: "1.0.0"
created: "2026-03-29"
updated: "2026-03-29"
author: "builder_agent"
name: "Customer Support Session Summary"
source_type: session
compression_method: hybrid
quality: 8.9
tags: [memory_summary, support, session, hybrid]
tldr: "Hybrid compression of support sessions at 15 turns; retains entities + decisions; drops filler. 8:1 ratio."
max_tokens: 512
trigger: turn_count
source_window: 15
retain_entities: true
retain_timestamps: false
freshness_decay: 0.1
description: "Compresses costmer support sessions after 15 turns using hybrid method; preserves issue entities, resolutions, and commitments."
```
## Overview
Compresses costmer support session conversations after 15 turns using hybrid method.
Consumed by the support agent at session resume to restore context without full transcript replay.
## Compression
Method: hybrid — abstractive narrative for conversation flow + extractive lift for issue details and resolutions
Ratio: ~8:1 (avg 4000 tokens input -> 512 tokens output)
Preserved: costmer name, issue ID, product names, error codes, resolution steps agreed upon, open action items
Dropped: greetings, repeated clarification loops, acknowledgment turns ("got it", "sure", "one moment")
## Trigger
Condition: turn_count >= 15
On fire: summarize last source_window turns, prepend to context buffer, drop raw turns beyond window
## Retention
Entities: retained — costmer name, product names, error codes, ticket IDs, URLs
Decisions: retained — resolution steps, escalation decisions, refund approvals
Action items: retained — pending tasks with owner (agent/costmer) and deadline if stated
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

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
