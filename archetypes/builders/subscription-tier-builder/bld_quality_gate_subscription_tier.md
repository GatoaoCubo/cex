---
kind: quality_gate
id: p11_qg_subscription_tier
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for subscription_tier
quality: null
title: "Quality Gate Subscription Tier"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [subscription_tier, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for subscription_tier"
domain: "subscription_tier construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Definition  
| metric                | threshold       | operator | scope         |  
|-----------------------|------------------|----------|---------------|  
| Tier uniqueness       | 100%             | ==       | All tiers     |  
| Pricing consistency   | 0%               | <=       | All tiers     |  
| Feature completeness  | 95%              | >=       | Feature matrix|  

## HARD Gates  
| ID      | Check                     | Fail Condition                                      |  
|---------|---------------------------|-----------------------------------------------------|  
| H01     | YAML frontmatter valid    | Missing or invalid frontmatter                      |  
| H02     | ID matches pattern        | ID does not match ^p11_st_[a-z][a-z0-9_]+.yaml$    |  
| H03     | kind field matches        | kind != 'subscription_tier'                         |  
| H04     | Tier names are unique     | Duplicate tier names detected                       |  
| H05     | Pricing >= 0              | Negative or missing pricing                         |  
| H06     | Free tier exists          | No tier with 'free' in name or pricing 0            |  
| H07     | Feature matrix complete   | Missing required feature categories                 |  

## SOFT Scoring  
| Dim       | Dimension             | Weight | Scoring Guide                                      |  
|-----------|------------------------|--------|----------------------------------------------------|  
| D01       | Pricing clarity        | 0.15   | Clear, transparent pricing (1.0)                   |  
| D02       | Feature completeness   | 0.15   | All features mapped (1.0)                          |  
| D03       | Tier differentiation   | 0.15   | Clear tier distinctions (1.0)                     |  
| D04       | User experience        | 0.15   | Seamless onboarding (1.0)                          |  
| D05       | Compliance             | 0.10   | Meets legal/contractual requirements (1.0)         |  
| D06       | Scalability            | 0.15   | Supports future growth (1.0)                       |  
| D07       | Documentation          | 0.15   | Full tier documentation (1.0)                      |  

## Actions  
| Score     | Action                          |  
|-----------|----------------------------------|  
| GOLDEN    | Auto-publish                     |  
| PUBLISH   | Manual review required           |  
| REVIEW    | Escalate to product team         |  
| REJECT    | Block deployment, fix required   |  

## Bypass  
| conditions                  | approver | audit trail           |  
|-----------------------------|----------|------------------------|  
| Emergency release needed    | CTO      | Documented in JIRA     |  
| Legacy system compatibility | CTO      | Approved by legal      |
