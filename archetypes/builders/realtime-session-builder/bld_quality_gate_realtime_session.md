---
kind: quality_gate
id: p09_qg_realtime_session
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for realtime_session
quality: null
title: "Quality Gate Realtime Session"
version: "1.0.0"
author: wave1_builder_gen
tags: [realtime_session, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for realtime_session"
domain: "realtime_session construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Definition  
| metric | threshold | operator | scope |  
|---|---|---|---|  
| Session Configuration Validity | 100% | equals | All sessions |  

## HARD Gates  
| ID | Check | Fail Condition |  
|---|---|---|  
| H01 | YAML valid | Invalid YAML syntax |  
| H02 | ID matches pattern | ID does not match `^[a-zA-Z0-9_-]{3,20}$` |  
| H03 | kind matches | kind ≠ `realtime_session` |  
| H04 | Session timeout defined | Timeout ≤ 0s |  
| H05 | Encryption enabled | TLS version < 1.2 |  
| H06 | Bidirectional support | Missing `bidirectional: true` |  
| H07 | Heartbeat interval | Interval > 30s |  

## SOFT Scoring  
| Dim | Dimension | Weight | Scoring Guide |  
|---|---|---|---|  
| D01 | YAML structure | 0.10 | 1.0 if valid, 0.5 if partial |  
| D02 | ID pattern | 0.10 | 1.0 if valid, 0.0 otherwise |  
| D03 | Timeout | 0.15 | 1.0 if 1–60s, 0.5 if >60s |  
| D04 | Encryption | 0.15 | 1.0 if TLS 1.2+, 0.0 otherwise |  
| D05 | Bidirectional | 0.10 | 1.0 if enabled, 0.0 otherwise |  
| D06 | Heartbeat | 0.10 | 1.0 if ≤30s, 0.5 if 31–60s |  
| D07 | Authentication | 0.10 | 1.0 if mutual TLS, 0.5 if basic |  
| D08 | Logging | 0.10 | 1.0 if enabled, 0.0 otherwise |  

## Actions  
| Score | Action |  
|---|---|  
| GOLDEN (≥9.5) | Auto-approve and deploy |  
| PUBLISH (≥8.0) | Manual review required |  
| REVIEW (≥7.0) | Escalate to security team |  
| REJECT (<7.0) | Block deployment |  

## Bypass  
| conditions | approver | audit trail |  
|---|---|---|  
| Emergency deployment | CTO | Ticket #12345 |  
| Legacy system migration | Architect | Ticket #67890 |
