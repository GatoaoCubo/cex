---
kind: quality_gate
id: p10_qg_consolidation_policy
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for consolidation_policy
quality: null
title: "Quality Gate Consolidation Policy"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [consolidation_policy, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for consolidation_policy"
domain: "consolidation_policy construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Definition  
(Table: metric, threshold, operator, scope)  
| Metric | Threshold | Operator | Scope |  
|---|---|---|---|  
| Memory leak rate | 0.1% | <= | System-wide |  
| Allocation tracking coverage | 100% | == | All memory pools |  
| Deallocation latency | 10ms | <= | Critical paths |  
| Fragmentation ratio | 20% | <= | Heap memory |  

## HARD Gates  
(Table: ID | Check | Fail Condition)  
| ID | Check | Fail Condition |  
|---|---|---|  
| H01 | YAML frontmatter valid | Invalid YAML syntax |  
| H02 | ID matches pattern ^p10_cp_[a-z][a-z0-9_]+.md$ | Invalid schema ID |  
| H03 | kind field matches 'consolidation_policy' | Incorrect policy type |  
| H04 | Memory leak detection enabled | Missing leak detection mechanism |  
| H05 | Allocation tracking logs retained for 90 days | Logs missing or incomplete |  
| H06 | Deallocation hooks implemented for all allocators | Missing hooks in allocators |  
| H07 | Fragmentation monitoring threshold configured | No threshold defined |  
| H08 | Memory pool reuse rate >= 95% | Pool reuse below threshold |  

## SOFT Scoring  
(Table: Dim | Dimension | Weight | Scoring Guide)  
| Dim | Dimension | Weight | Scoring Guide |  
|---|---|---|---|  
| D1 | Memory safety | 0.20 | 1.0 for no leaks, 0.5 for minor leaks |  
| D2 | Allocation efficiency | 0.15 | 1.0 for 99%+ tracking, 0.25 for <80% |  
| D3 | Fragmentation control | 0.15 | 1.0 for <=15% fragmentation, 0.5 for >25% |  
| D4 | Monitoring completeness | 0.10 | 1.0 for full coverage, 0.25 for partial |  
| D5 | Documentation clarity | 0.10 | 1.0 for complete docs, 0.5 for gaps |  
| D6 | Error handling | 0.10 | 1.0 for robust handling, 0.25 for partial |  
| D7 | Scalability | 0.10 | 1.0 for 100k+ allocations, 0.5 for <10k |  
| D8 | Audit trail | 0.10 | 1.0 for full logs, 0.25 for partial |  

## Actions  
(Table: Score | Action)  
| Score | Action |  
|---|---|  
| GOLDEN >=9.5 | Auto-approve and deploy |  
| PUBLISH >=8.0 | Manual review required |  
| REVIEW >=7.0 | Escalate to senior engineers |  
| REJECT <7.0 | Reject and require rework |  

## Bypass  
(Table: conditions, approver, audit trail)  
| conditions | approver | audit trail |  
|---|---|---|  
| Critical system downtime | CTO | Incident report |  
| Emergency patch | CTO | Emergency approval log |  
| Legacy system compatibility | CTO | Compatibility review |
