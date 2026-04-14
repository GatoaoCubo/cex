---
id: p11_qg_memory_summary
kind: quality_gate
pillar: P11
title: "Gate: memory_summary"
version: "1.0.0"
created: "2026-03-29"
updated: "2026-03-29"
author: "builder_agent"
domain: "memory compression — summarized conversation/session memory injected at runtime"
quality: 9.0
tags: [quality-gate, memory-summary, P10, compression, retention, freshness]
tldr: "Pass/fail gate for memory_summary artifacts: compression method, retention policy, trigger definition, boundary vs session_state and learning_record."
density_score: 0.90
llm_function: GOVERN
---
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
