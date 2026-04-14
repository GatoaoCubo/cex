---
kind: quality_gate
id: p05_qg_onboarding_flow
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for onboarding_flow
quality: null
title: "Quality Gate Onboarding Flow"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [onboarding_flow, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for onboarding_flow"
domain: "onboarding_flow construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Definition  
| metric                | threshold | operator | scope         |  
|-----------------------|-----------|----------|---------------|  
| User activation rate  | 85%       | >=       | All users     |  

## HARD Gates  
| ID                  | Check                          | Fail Condition                              |  
|---------------------|--------------------------------|---------------------------------------------|  
| H01                 | YAML frontmatter valid         | Invalid or missing YAML frontmatter         |  
| H02                 | ID matches pattern             | ID does not match ^p05_of_[a-z][a-z0-9_]+.md$ |  
| H03                 | Onboarding completion rate     | < 80% completion rate                       |  
| H04                 | Aha-moment engagement rate     | < 70% engagement rate                       |  
| H05                 | Error rate during onboarding   | > 5% error rate                             |  
| H06                 | Time to first transaction      | > 10 minutes                                |  
| H07                 | Milestone completion rate      | < 90% milestone completion                  |  

## SOFT Scoring  
| Dim         | Dimension               | Weight | Scoring Guide                          |  
|-------------|-------------------------|--------|----------------------------------------|  
| D01         | Completion rate         | 0.15   | 1.00 (85%+) → 0.00 (<60%)              |  
| D02         | Aha-moment engagement   | 0.15   | 1.00 (70%+) → 0.00 (<40%)              |  
| D03         | Error rate              | 0.10   | 1.00 (≤2%) → 0.00 (>10%)               |  
| D04         | Time to first transaction | 0.10   | 1.00 (≤5 min) → 0.00 (>15 min)         |  
| D05         | Milestone completion    | 0.10   | 1.00 (95%+) → 0.00 (<70%)              |  
| D06         | UX feedback score       | 0.10   | 1.00 (4.5/5+) → 0.00 (≤3.0/5)          |  
| D07         | Activation within 24h   | 0.10   | 1.00 (80%+) → 0.00 (<50%)              |  
| D08         | User satisfaction       | 0.10   | 1.00 (4.0/5+) → 0.00 (≤2.5/5)          |  

## Actions  
| Score   | Action                                      |  
|---------|---------------------------------------------|  
| GOLDEN  | No action required                          |  
| PUBLISH | Publish with notes                          |  
| REVIEW  | Review with engineering                     |  
| REJECT  | Reject and fix before resubmission          |  

## Bypass  
| conditions                          | approver | audit trail         |  
|------------------------------------|----------|---------------------|  
| Critical bug fix with CTO approval | CTO      | Ticket #PROD-12345  |
