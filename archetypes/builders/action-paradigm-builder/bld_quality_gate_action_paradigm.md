---
kind: quality_gate
id: p04_qg_action_paradigm
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for action_paradigm
quality: null
title: "Quality Gate Action Paradigm"
version: "1.0.0"
author: wave1_builder_gen
tags: [action_paradigm, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for action_paradigm"
domain: "action_paradigm construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Definition  
| metric             | threshold | operator | scope         |  
|--------------------|-----------|----------|---------------|  
| Action Success Rate | 95%       | ≥        | All environments |  

## HARD Gates  
| ID   | Check                  | Fail Condition                          |  
|------|------------------------|-----------------------------------------|  
| H01  | YAML valid             | Invalid YAML syntax                     |  
| H02  | ID matches pattern     | ID does not conform to `AGT-[0-9]{4}` |  
| H03  | kind matches           | Kind ≠ `action_paradigm`               |  
| H04  | Action execution time  | > 500ms per action                     |  
| H05  | Error rate             | > 5% error rate                        |  
| H06  | Resource usage         | CPU/Memory > 90% utilization           |  
| H07  | Policy compliance      | Violates environment-specific rules    |  
| H08  | Logging completeness   | Missing critical logs                  |  
| H09  | Concurrency handling   | Deadlock or race condition detected    |  
| H10  | Rollback capability    | No defined rollback mechanism          |  

## SOFT Scoring  
| Dim | Dimension           | Weight | Scoring Guide                          |  
|-----|---------------------|--------|----------------------------------------|  
| D1  | Execution Efficiency | 0.15   | 1.0 (≤100ms) → 0.0 (≥500ms)            |  
| D2  | Error Handling       | 0.15   | 1.0 (0% errors) → 0.0 (>10% errors)     |  
| D3  | Resource Management  | 0.10   | 1.0 (≤70% usage) → 0.0 (>95% usage)     |  
| D4  | Compliance           | 0.10   | 1.0 (no violations) → 0.0 (≥3 violations)|  
| D5  | Logging              | 0.10   | 1.0 (full logs) → 0.0 (missing logs)    |  
| D6  | Concurrency          | 0.10   | 1.0 (no issues) → 0.0 (deadlocks)       |  
| D7  | Rollback             | 0.10   | 1.0 (defined) → 0.0 (undefined)         |  
| D8  | User Feedback        | 0.10   | 1.0 (≥90% satisfaction) → 0.0 (≤50%)    |  

## Actions  
| Score   | Action                  |  
|---------|-------------------------|  
| ≥9.5    | Automate deployment     |  
| ≥8.0    | Schedule review         |  
| ≥7.0    | Request changes         |  
| <7.0    | Block deployment        |  

## Bypass  
| conditions                     | approver         | audit trail         |  
|------------------------------|------------------|---------------------|  
| Critical environment failure | Senior Architect | Escalation ticket # |
