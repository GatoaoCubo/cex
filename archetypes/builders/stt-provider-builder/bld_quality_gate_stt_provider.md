---
kind: quality_gate
id: p04_qg_stt_provider
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for stt_provider
quality: 9.0
title: "Quality Gate Stt Provider"
version: "1.0.0"
author: wave1_builder_gen
tags: [stt_provider, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for stt_provider"
domain: "stt_provider construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Definition  
| metric | threshold | operator | scope |  
|---|---|---|---|  
| Provider Integration Completeness | 95% | ≥ | All STT providers |  

## HARD Gates  
| ID | Check | Fail Condition |  
|---|---|---|  
| H01 | YAML valid | Invalid YAML syntax |  
| H02 | ID matches pattern | ID does not match `^p04_stt_[a-zA-Z0-9]+$` (schema source of truth) |  
| H03 | kind matches | kind ≠ `stt_provider` |  
| H04 | Latency ≤ 500ms | Latency > 500ms for 99% of requests |  
| H05 | Error rate ≤ 1% | Error rate > 1% |  
| H06 | Language support ≥ 10 | <10 languages supported |  
| H07 | API compliance | Missing required endpoints |  

## SOFT Scoring  
| Dim | Dimension | Weight | Scoring Guide |  
|---|---|---|---|  
| D01 | Accuracy | 0.25 | 95%+ = 1.0, 90% = 0.8, 85% = 0.6 |  
| D02 | Latency | 0.20 | ≤500ms = 1.0, 600ms = 0.7, 700ms = 0.4 |  
| D03 | Error Handling | 0.15 | 1% = 1.0, 2% = 0.7, 3% = 0.3 |  
| D04 | Language Support | 0.10 | 10+ = 1.0, 8 = 0.8, 5 = 0.5 |  
| D05 | API Compliance | 0.10 | Full = 1.0, 80% = 0.7, 50% = 0.3 |  
| D06 | Documentation | 0.10 | Complete = 1.0, Partial = 0.6, Missing = 0.2 |  
| D07 | Scalability | 0.10 | 1M+ = 1.0, 500K = 0.7, 100K = 0.3 |  

## Actions  
| Score | Action |  
|---|---|  
| ≥9.5 | GOLDEN: Auto-approve, deploy to production |  
| ≥8.0 | PUBLISH: Deploy to staging, notify team |  
| ≥7.0 | REVIEW: Manual review required |  
| <7.0 | REJECT: Fix and resubmit |  

## Bypass  
| conditions | approver | audit trail |  
|---|---|---|  
| Emergency fix for production outage | CTO | Incident ticket # |  
| Temporary workaround for critical bug | Lead Engineer | Code review log |  
| Prototype integration with limited scope | Product Manager | Prototype approval form |
