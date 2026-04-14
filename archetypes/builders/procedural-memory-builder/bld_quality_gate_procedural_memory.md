---
kind: quality_gate
id: p10_qg_procedural_memory
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for procedural_memory
quality: null
title: "Quality Gate Procedural Memory"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [procedural_memory, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for procedural_memory"
domain: "procedural_memory construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Definition  
(Table: metric, threshold, operator, scope)  
| metric | threshold | operator | scope |  
|---|---|---|---|  
| Accuracy | 95% | >= | system-wide |  

## HARD Gates  
(Table: ID | Check | Fail Condition)  
| ID | Check | Fail Condition |  
|---|---|---|  
| H01 | YAML frontmatter valid | invalid YAML |  
| H02 | ID matches ^p10_pm_[a-z][a-z0-9_]+.md$ | invalid schema ID |  
| H03 | kind field matches 'procedural_memory' | incorrect kind |  
| H04 | Data integrity checks pass | data corruption detected |  
| H05 | Retrieval latency <= 200ms | latency exceeds threshold |  
| H06 | Error rate <= 0.1% | excessive errors |  
| H07 | Version consistency enforced | version mismatch |  
| H08 | Access control policies enforced | unauthorized access |  
| H09 | Audit logs complete | missing audit records |  
| H10 | Recovery time <= 5min | recovery timeout |  

## SOFT Scoring  
(Table: Dim | Dimension | Weight | Scoring Guide)  
| Dim | Dimension | Weight | Scoring Guide |  
|---|---|---|---|  
| D1 | Data integrity | 0.15 | 1.00 (perfect) to 0.00 (corrupted) |  
| D2 | Retrieval efficiency | 0.12 | 1.00 (fast) to 0.00 (slow) |  
| D3 | Error handling | 0.10 | 1.00 (robust) to 0.00 (none) |  
| D4 | Version control | 0.10 | 1.00 (consistent) to 0.00 (chaotic) |  
| D5 | Access security | 0.15 | 1.00 (secure) to 0.00 (exposed) |  
| D6 | Audit completeness | 0.10 | 1.00 (full) to 0.00 (missing) |  
| D7 | Recovery speed | 0.10 | 1.00 (fast) to 0.00 (slow) |  
| D8 | User feedback | 0.18 | 1.00 (positive) to 0.00 (negative) |  

## Actions  
(Table: Score | Action)  
| Score | Action |  
|---|---|  
| GOLDEN | >=9.5 | Deploy immediately |  
| PUBLISH | >=8.0 | Publish with review |  
| REVIEW | >=7.0 | Manual review required |  
| REJECT | <7.0 | Reject and fix |  

## Bypass  
(Table: conditions, approver, audit trail)  
| conditions | approver | audit trail |  
|---|---|---|  
| Critical system failure | Senior engineer | Ticket #1234, approval 2023-10-01 |
