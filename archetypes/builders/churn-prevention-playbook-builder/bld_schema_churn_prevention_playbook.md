---
kind: schema
id: bld_schema_churn_prevention_playbook
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for churn_prevention_playbook
quality: 9.1
title: "Schema Churn Prevention Playbook"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [churn_prevention_playbook, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for churn_prevention_playbook"
domain: "churn_prevention_playbook construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Frontmatter Fields  
### Required  
| Field | Type | Required | Default | Notes |  
|---|---|---|---|---|  
| id | string | yes |  | Must match ID Pattern |  
| kind | string | yes |  | Must be 'churn_prevention_playbook' |  
| pillar | string | yes |  | Must be 'P03' |  
| title | string | yes |  | Descriptive playbook name |  
| version | string | yes | 1.0 | Version control |  
| created | datetime | yes |  | ISO 8601 format |  
| updated | datetime | yes |  | ISO 8601 format |  
| author | string | yes |  | Primary contributor |  
| domain | string | yes |  | CEX-specific context |  
| quality | null | yes | null | Never self-score; peer review assigns |  
| tags | list | yes |  | Keywords for search |  
| tldr | string | yes |  | Summary of playbook purpose |  
| target_user_segment | string | yes |  | e.g., 'high-value', 'at-risk' |  
| intervention_type | string | yes |  | e.g., 'email', 'in-app' |  

### Recommended  
| Field | Type | Notes |  
|---|---|---|  
| risk_score | float | 0–100 churn risk assessment |  
| implementation_timeline | string | e.g., 'Q1 2024' |  

## ID Pattern  
^p03_cpp_[a-z][a-z0-9_]+.md$  

## Body Structure  
1. **Introduction**  
   - Purpose, scope, and objectives of the playbook.  
2. **Key Strategies**  
   - Actionable steps to reduce churn (e.g., retention campaigns, loyalty programs).  
3. **Metrics**  
   - KPIs for success (e.g., churn rate, customer lifetime value).  
4. **Implementation Steps**  
   - Workflow, tools, and responsibilities.  
5. **Success Criteria**  
   - Thresholds for evaluating playbook effectiveness.  

## Constraints  
- Quality must be assigned by peer review, not self-score.  
- ID must match exact regex: ^p03_cpp_[a-z][a-z0-9_]+.md$.  
- File size must not exceed 6144 bytes.  
- All required fields must be present and valid.  
- Domain-specific fields must align with CEX churn prevention contexts.  
- Version must follow semantic versioning (e.g., 1.0, 2.1).
