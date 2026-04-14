---
kind: quality_gate
id: p09_qg_transport_config
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for transport_config
quality: null
title: "Quality Gate Transport Config"
version: "1.0.0"
author: wave1_builder_gen
tags: [transport_config, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for transport_config"
domain: "transport_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Definition  
| metric         | threshold     | operator | scope        |  
|----------------|---------------|----------|--------------|  
| Latency        | < 100ms       | <=       | per-connection |  
| Throughput     | > 10MB/s      | >=       | global       |  
| Reliability    | 99.9%         | >=       | per-connection |  

## HARD Gates  
| ID   | Check                  | Fail Condition                          |  
|------|------------------------|-----------------------------------------|  
| H01  | YAML valid             | Invalid YAML syntax                     |  
| H02  | ID matches pattern     | ID does not match `transport-\d+`       |  
| H03  | kind matches           | kind != `transport_config`              |  
| H04  | Protocol version       | TLS version < 1.2                       |  
| H05  | Heartbeat interval     | Heartbeat > 30s                         |  
| H06  | Certificate validity   | Certificate expires in < 30 days        |  
| H07  | Redundancy config      | < 2 endpoints defined                   |  

## SOFT Scoring  
| Dim | Dimension           | Weight | Scoring Guide                              |  
|-----|---------------------|--------|--------------------------------------------|  
| D1  | Protocol security   | 0.20   | TLS 1.3: 1.0, TLS 1.2: 0.7, <1.2: 0.0       |  
| D2  | Latency compliance  | 0.15   | 100%: 1.0, 75%: 0.5, <75%: 0.0              |  
| D3  | Throughput          | 0.15   | 100%: 1.0, 75%: 0.5, <75%: 0.0              |  
| D4  | Redundancy          | 0.10   | 2+ endpoints: 1.0, 1: 0.5, 0: 0.0           |  
| D5  | Certificate trust   | 0.10   | CA trusted: 1.0, self-signed: 0.5, invalid: 0.0 |  
| D6  | Config completeness | 0.10   | All required fields present: 1.0, missing: 0.5 |  
| D7  | Error handling      | 0.10   | Defined: 1.0, undefined: 0.5                |  
| D8  | Documentation       | 0.10   | Present: 1.0, absent: 0.5                   |  

## Actions  
| Score     | Action              |  
|-----------|---------------------|  
| >=9.5     | GOLDEN: Auto-approve |  
| >=8.0     | PUBLISH: Deploy     |  
| >=7.0     | REVIEW: Manual check |  
| <7.0      | REJECT: Rework      |  

## Bypass  
| conditions                          | approver         | audit trail              |  
|------------------------------------|------------------|--------------------------|  
| Emergency fix required             | Senior Engineer  | Log reason, timestamp    |  
| Legacy system compatibility        | Architecture Lead| Log reason, timestamp    |  
| Third-party API constraint         | CTO              | Log reason, timestamp    |
