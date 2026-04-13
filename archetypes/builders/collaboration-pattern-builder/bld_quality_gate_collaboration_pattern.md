---
kind: quality_gate
id: p12_qg_collaboration_pattern
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for collaboration_pattern
quality: null
title: "Quality Gate Collaboration Pattern"
version: "1.0.0"
author: wave1_builder_gen
tags: [collaboration_pattern, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for collaboration_pattern"
domain: "collaboration_pattern construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Definition  
| metric | threshold | operator | scope |  
|---|---|---|---|  
| Coordination topology completeness | 80% | ≥ | All agents |  

## HARD Gates  
| ID | Check | Fail Condition |  
|---|---|---|  
| H01 | YAML valid | Invalid YAML syntax |  
| H02 | ID matches pattern | ID does not match `P[0-9]{2}-[A-Z]{3}` |  
| H03 | kind matches | kind ≠ `collaboration_pattern` |  
| H04 | All agents have defined roles | Missing agent role definition |  
| H05 | Communication channels exist | No defined channels between agents |  
| H06 | No single point of failure | Topology has single point of failure |  
| H07 | Consensus mechanism defined | No consensus algorithm specified |  
| H08 | Scalability threshold met | Agent count exceeds 100 without redundancy |  

## SOFT Scoring  
| Dim | Dimension | Weight | Scoring Guide |  
|---|---|---|---|  
| D01 | Topology Completeness | 0.2 | 1.0 (≥80%), 0.5 (50-79%), 0.0 (<50%) |  
| D02 | Role Clarity | 0.15 | 1.0 (unambiguous), 0.5 (ambiguous), 0.0 (undefined) |  
| D03 | Communication Efficiency | 0.15 | 1.0 (≤10ms latency), 0.5 (10-50ms), 0.0 (>50ms) |  
| D04 | Redundancy | 0.1 | 1.0 (≥3 paths), 0.5 (1-2 paths), 0.0 (none) |  
| D05 | Consensus | 0.1 | 1.0 (PBFT/LPBFT), 0.5 (other), 0.0 (none) |  
| D06 | Scalability | 0.1 | 1.0 (≤1000 agents), 0.5 (1000-5000), 0.0 (>5000) |  
| D07 | Security | 0.1 | 1.0 (TLS 1.3+), 0.5 (TLS 1.2), 0.0 (<TLS 1.2) |  
| D08 | Adaptability | 0.1 | 1.0 (dynamic reconfiguration), 0.5 (static), 0.0 (none) |  

## Actions  
| Score | Action |  
|---|---|  
| ≥9.5 | Automate deployment |  
| ≥8.0 | Schedule publish |  
| ≥7.0 | Manual review required |  
| <7.0 | Reject and rework |  

## Bypass  
| conditions | approver | audit trail |  
|---|---|---|  
| Emergency fix required | CTO | Signed approval form |
