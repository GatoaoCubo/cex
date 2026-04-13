---
kind: quality_gate
id: p04_qg_search_strategy
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for search_strategy
quality: null
title: "Quality Gate Search Strategy"
version: "1.0.0"
author: wave1_builder_gen
tags: [search_strategy, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for search_strategy"
domain: "search_strategy construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Definition  
| metric | threshold | operator | scope |  
|---|---|---|---|  
| Compute Allocation Efficiency | 90% | ≥ | All inference nodes |  

## HARD Gates  
| ID | Check | Fail Condition |  
|---|---|---|  
| H01 | YAML valid | Invalid YAML syntax |  
| H02 | ID matches pattern | ID does not match `P04-[A-Z]{2}-\d{3}` |  
| H03 | kind matches | kind ≠ `search_strategy` |  
| H04 | Strategy validity | Strategy not in [static, dynamic, hybrid] |  
| H05 | Resource limits defined | Missing CPU/RAM limits |  
| H06 | Allocation consistency | Inconsistent node-to-task mapping |  
| H07 | Error handling | No fallback strategy for allocation failures |  
| H08 | Performance metrics | Missing latency/throughput benchmarks |  

## SOFT Scoring  
| Dim | Dimension | Weight | Scoring Guide |  
|---|---|---|---|  
| D01 | Strategy validity | 0.15 | Valid strategy (static/dynamic/hybrid) |  
| D02 | Resource efficiency | 0.15 | CPU/RAM utilization ≤ 95% |  
| D03 | Scalability | 0.10 | Supports ≥1000 concurrent queries |  
| D04 | Error resilience | 0.10 | Fallback strategy implemented |  
| D05 | Latency | 0.15 | P99 latency ≤ 500ms |  
| D06 | Logging | 0.05 | Detailed allocation logs enabled |  
| D07 | Security | 0.10 | No unauthorized access paths |  
| D08 | Compliance | 0.10 | Meets data governance policies |  

## Actions  
| Score | Action |  
|---|---|  
| ≥9.5 | GOLDEN: Auto-approve for production |  
| ≥8.0 | PUBLISH: Deploy to staging |  
| ≥7.0 | REVIEW: Manual QA required |  
| <7.0 | REJECT: Requires redesign |  

## Bypass  
| conditions | approver | audit trail |  
|---|---|---|  
| Emergency fix for critical outage | CTO | Incident report + approval timestamp |  
| Legacy system compatibility | Architecture Lead | Legacy system waiver document |  
| Experimental feature testing | Research Lead | Lab environment approval log |
