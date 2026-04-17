---
kind: quality_gate
id: p04_qg_tts_provider
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for tts_provider
quality: 9.1
title: "Quality Gate Tts Provider"
version: "1.0.0"
author: wave1_builder_gen
tags: [tts_provider, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for tts_provider"
domain: "tts_provider construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Definition  
| Metric                | Threshold | Operator | Scope      |  
|-----------------------|-----------|----------|------------|  
| Latency               | <500ms    | <=       | Per-call   |  
| Accuracy              | >95%      | >=       | Per-provider |  
| Supported Languages   | >=5       | >=       | Per-provider |  
| Error Rate            | <1%       | <=       | Per-hour   |  

## HARD Gates  
| ID   | Check               | Fail Condition                          |  
|------|---------------------|-----------------------------------------|  
| H01  | YAML valid          | Invalid YAML syntax                     |  
| H02  | ID matches pattern  | ID does not match `^p04_tts_[a-zA-Z0-9_-]+$` |  
| H03  | Kind matches        | Kind != `tts_provider`                  |  
| H04  | Provider registered | Provider not in approved list           |  
| H05  | API key present     | Missing or invalid API key              |  
| H06  | Endpoint reachable  | API endpoint unreachable                |  
| H07  | Language codes valid| Language codes not ISO 639-1 compliant  |  

## SOFT Scoring  
| Dim | Dimension         | Weight | Scoring Guide                          |  
|-----|-------------------|--------|----------------------------------------|  
| D1  | Latency           | 0.15   | 1.0 (<=200ms), 0.5 (<=500ms)           |  
| D2  | Accuracy          | 0.15   | 1.0 (>98%), 0.5 (>95%)                 |  
| D3  | Language support  | 0.10   | 1.0 (>=10), 0.5 (>=5)                  |  
| D4  | Error handling    | 0.10   | 1.0 (0% errors), 0.5 (<1%)             |  
| D5  | Documentation     | 0.10   | 1.0 (complete), 0.5 (partial)          |  
| D6  | API stability     | 0.10   | 1.0 (no downtime), 0.5 (<1h/month)     |  
| D7  | Scalability       | 0.10   | 1.0 (10k+ RPS), 0.5 (1k+ RPS)          |  
| D8  | Security          | 0.10   | 1.0 (TLS 1.2+), 0.5 (no TLS)           |  

## Actions  
| Score     | Action                          |  
|-----------|---------------------------------|  
| GOLDEN    | >=9.5: No action required       |  
| PUBLISH   | >=8.0: Deploy to production     |  
| REVIEW    | >=7.0: Require QA review        |  
| REJECT    | <7.0: Rework and resubmit       |  

## Bypass  
| Conditions                          | Approver   | Audit Trail                   |  
|-------------------------------------|------------|-------------------------------|  
| Critical bug fix (SLA violation)    | CTO        | Note: "Urgent SLA fix approved" |  
| New provider onboarding (first time)| Architect  | Note: "Initial provider setup"  |  
| Temporary demo environment          | Manager    | Note: "Demo bypass approved"    |
