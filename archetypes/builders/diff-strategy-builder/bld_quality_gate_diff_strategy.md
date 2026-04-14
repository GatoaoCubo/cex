---
kind: quality_gate
id: p04_qg_diff_strategy
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for diff_strategy
quality: null
title: "Quality Gate Diff Strategy"
version: "1.0.0"
author: wave1_builder_gen
tags: [diff_strategy, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for diff_strategy"
domain: "diff_strategy construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Definition  
| metric       | threshold | operator | scope                  |  
|--------------|-----------|----------|------------------------|  
| diff_strategy | 0.1       | >        | Change application logic |  

## HARD Gates  
| ID   | Check               | Fail Condition                          |  
|------|---------------------|-----------------------------------------|  
| H01  | YAML valid          | Invalid YAML syntax                     |  
| H02  | ID matches pattern  | ID does not match `P04-\d{3}`          |  
| H03  | kind matches        | kind is not `diff_strategy`            |  
| H04  | Strategy consistency| Strategy differs by >10% from baseline |  
| H05  | Algorithm validation| Algorithm fails unit tests             |  
| H06  | Backtesting results | Backtest loss >15%                     |  
| H07  | Performance metrics | Latency >500ms                         |  
| H08  | Error handling      | Unhandled exceptions in critical paths |  
| H09  | Documentation       | Missing change impact analysis         |  

## SOFT Scoring  
| Dim | Dimension             | Weight | Scoring Guide                          |  
|-----|-----------------------|--------|----------------------------------------|  
| D1  | Strategy Consistency  | 0.15   | 1.0 (baseline) to 0.0 (divergent)      |  
| D2  | Algorithm Accuracy    | 0.15   | 1.0 (perfect) to 0.0 (invalid)         |  
| D3  | Backtesting Results   | 0.15   | 1.0 (optimal) to 0.0 (worse than baseline) |  
| D4  | Performance Metrics   | 0.10   | 1.0 (target met) to 0.0 (critical failure) |  
| D5  | Error Handling        | 0.10   | 1.0 (none) to 0.0 (unresolved)         |  
| D6  | Documentation         | 0.10   | 1.0 (complete) to 0.0 (missing)        |  
| D7  | Code Quality          | 0.10   | 1.0 (clean) to 0.0 (critical issues)   |  
| D8  | User Impact           | 0.15   | 1.0 (neutral) to 0.0 (severe disruption)|  

## Actions  
| Score     | Action                                      |  
|-----------|---------------------------------------------|  
| GOLDEN    | Auto-approve and deploy                     |  
| PUBLISH   | Manual review required before deployment    |  
| REVIEW    | Escalate to senior engineers for analysis   |  
| REJECT    | Block deployment; require rework            |  

## Bypass  
| conditions                          | approver | audit trail               |  
|------------------------------------|----------|---------------------------|  
| Critical system failure emergency  | CTO      | "Emergency Fix Approved"  |
