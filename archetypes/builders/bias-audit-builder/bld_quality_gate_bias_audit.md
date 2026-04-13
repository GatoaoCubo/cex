---
kind: quality_gate
id: p07_qg_bias_audit
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for bias_audit
quality: null
title: "Quality Gate Bias Audit"
version: "1.0.0"
author: wave1_builder_gen
tags: [bias_audit, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for bias_audit"
domain: "bias_audit construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Definition  
| metric         | threshold | operator | scope          |  
|----------------|-----------|----------|----------------|  
| bias_score     | 0.1       | <=       | model output   |  
| data_coverage  | 95%       | >=       | training data  |  

## HARD Gates  
| ID   | Check                  | Fail Condition                          |  
|------|------------------------|-----------------------------------------|  
| H01  | YAML valid             | Invalid YAML syntax                     |  
| H02  | ID matches pattern     | ID does not match `P07-XXX`            |  
| H03  | kind matches           | Kind is not `bias_audit`              |  
| H04  | bias_score threshold   | bias_score > 0.1                      |  
| H05  | data_coverage threshold| data_coverage < 95%                   |  
| H06  | audit documentation    | Missing audit report                  |  
| H07  | stakeholder feedback   | No stakeholder sign-off               |  

## SOFT Scoring  
| Dim | Dimension             | Weight | Scoring Guide                          |  
|-----|-----------------------|--------|----------------------------------------|  
| D1  | Bias detection        | 0.15   | 0.0-1.0 based on audit severity        |  
| D2  | Data diversity        | 0.15   | 0.0-1.0 based on underrepresented groups |  
| D3  | Transparency          | 0.10   | 0.0-1.0 based on explainability        |  
| D4  | Mitigation effectiveness | 0.15 | 0.0-1.0 based on bias reduction        |  
| D5  | Stakeholder feedback  | 0.10   | 0.0-1.0 based on survey scores         |  
| D6  | Audit completeness    | 0.10   | 0.0-1.0 based on documentation         |  
| D7  | Model fairness        | 0.10   | 0.0-1.0 based on fairness metrics      |  
| D8  | Documentation quality | 0.15   | 0.0-1.0 based on clarity and depth     |  

## Actions  
| Score     | Action         |  
|-----------|----------------|  
| >=9.5     | GOLDEN         |  
| >=8.0     | PUBLISH        |  
| >=7.0     | REVIEW         |  
| <7.0      | REJECT         |  

## Bypass  
| conditions                  | approver       | audit trail              |  
|-----------------------------|----------------|--------------------------|  
| Regulatory exemption        | CTO            | Legal review document    |  
| Stakeholder override        | Board Chair    | Signed waiver            |  
| Critical system emergency   | CISO           | Incident response log    |
