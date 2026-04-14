---
kind: quality_gate
id: p11_qg_enterprise_sla
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for enterprise_sla
quality: null
title: "Quality Gate Enterprise Sla"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [enterprise_sla, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for enterprise_sla"
domain: "enterprise_sla construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Definition  
| metric             | threshold     | operator | scope         |  
|--------------------|---------------|----------|---------------|  
| Uptime             | 99.9%         | >=       | Production    |  
| Latency            | 100ms         | <=       | All services  |  
| Support response   | 1 hour        | <=       | SLA team      |  
| SLA coverage       | 95%           | >=       | Enterprise    |  

## HARD Gates  
| ID           | Check                        | Fail Condition                              |  
|--------------|------------------------------|---------------------------------------------|  
| H01          | YAML frontmatter valid       | Invalid YAML syntax or missing fields       |  
| H02          | ID matches ^p11_sla_[a-z][a-z0-9_]+.md$ | ID does not conform to schema pattern      |  
| H03          | kind field matches 'enterprise_sla' | kind field is incorrect                     |  
| H04          | Uptime >=99.9%               | Uptime <99.9%                               |  
| H05          | Latency <=100ms              | Latency >100ms                              |  
| H06          | Support response <=1 hour    | Support response >1 hour                    |  
| H07          | SLA coverage >=95%           | SLA coverage <95%                           |  
| H08          | SLA documentation exists     | Missing required SLA documentation          |  

## SOFT Scoring  
| Dim       | Dimension              | Weight | Scoring Guide                              |  
|-----------|------------------------|--------|--------------------------------------------|  
| D1        | Uptime reliability     | 0.20   | 1.00=99.99%, 0.50=99.5%, 0.00=99.0%         |  
| D2        | Latency consistency    | 0.15   | 1.00=50ms, 0.50=150ms, 0.00=250ms           |  
| D3        | Support responsiveness | 0.15   | 1.00=30min, 0.50=1.5hr, 0.00=3hr            |  
| D4        | SLA coverage           | 0.15   | 1.00=100%, 0.50=90%, 0.00=80%               |  
| D5        | Documentation quality  | 0.10   | 1.00=complete, 0.50=partial, 0.00=missing    |  
| D6        | Compliance             | 0.10   | 1.00=fully compliant, 0.00=non-compliant    |  
| D7        | Review process         | 0.15   | 1.00=automated, 0.50=manual, 0.00=no review  |  

## Actions  
| Score      | Action                   |  
|------------|--------------------------|  
| GOLDEN     | Auto-publish             |  
| PUBLISH    | Manual approval required |  
| REVIEW     | Peer review required     |  
| REJECT     | Reject and fix required  |  

## Bypass  
| conditions                          | approver       | audit trail              |  
|------------------------------------|----------------|--------------------------|  
| Critical production outage         | CTO            | Emergency bypass log     |  
| Regulatory compliance override     | Legal team     | Compliance audit trail   |  
| Temporary SLA exception            | SVP Operations | Exception approval log   |
