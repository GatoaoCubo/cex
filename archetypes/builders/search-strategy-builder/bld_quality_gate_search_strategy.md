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
| latency | 50ms | <= | per query |  
| resource utilization | 80% | <= | system-wide |  
| fallback strategy | defined | == | per model |  

## HARD Gates  
| ID | Check | Fail Condition |  
|---|---|---|  
| H01 | YAML valid | syntax errors |  
| H02 | ID matches pattern | invalid ID format |  
| H03 | kind matches | kind != "search_strategy" |  
| H04 | strategy defined | strategy is null |  
| H05 | allowed types | strategy not in ["static", "dynamic"] |  
| H06 | fallback defined | fallback is null |  
| H07 | priority validation | priority < 0 or > 10 |  

## SOFT Scoring  
| Dim | Dimension | Weight | Scoring Guide |  
|---|---|---|---|  
| D01 | Efficiency | 0.20 | 1.0 (optimal) to 0.0 (inefficient) |  
| D02 | Fairness | 0.15 | 1.0 (balanced) to 0.0 (biased) |  
| D03 | Scalability | 0.15 | 1.0 (linear) to 0.0 (nonlinear) |  
| D04 | Latency consistency | 0.10 | 1.0 (stable) to 0.0 (spiky) |  
| D05 | Resource utilization | 0.10 | 1.0 (optimal) to 0.0 (wasteful) |  
| D06 | Fallback reliability | 0.10 | 1.0 (always works) to 0.0 (fails) |  
| D07 | Documentation | 0.10 | 1.0 (complete) to 0.0 (missing) |  

## Actions  
| Score | Action |  
|---|---|  
| GOLDEN >=9.5 | Auto-approve and deploy |  
| PUBLISH >=8.0 | Manual review required |  
| REVIEW >=7.0 | Senior engineer approval |  
| REJECT <7.0 | Reject and require rework |  

## Bypass  
| conditions | approver | audit trail |  
|---|---|---|  
| urgent production fix | CTO | "emergency bypass" |  
| legacy system compatibility | architecture lead | "legacy exception" |  
| experimental strategy | research lead | "R&D override" |
