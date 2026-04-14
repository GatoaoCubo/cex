---
kind: schema
id: bld_schema_consolidation_policy
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for consolidation_policy
quality: null
title: "Schema Consolidation Policy"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [consolidation_policy, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for consolidation_policy"
domain: "consolidation_policy construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Frontmatter Fields  
### Required  
| Field | Type | Required | Default | Notes |  
|---|---|---|---|---|  
| id | string | yes | null | Must match ID Pattern |  
| kind | string | yes | "consolidation_policy" | Fixed value |  
| pillar | string | yes | "P10" | Fixed value |  
| title | string | yes | null | Descriptive name |  
| version | string | yes | "1.0" | Semantic versioning |  
| created | date | yes | null | ISO 8601 format |  
| updated | date | yes | null | ISO 8601 format |  
| author | string | yes | null | Responsible party |  
| domain | string | yes | null | Policy scope (e.g., "data", "finance") |  
| quality | null | yes | null | Never self-score; peer review assigns |  
| tags | array | yes | [] | Keywords for categorization |  
| tldr | string | yes | null | Summary of policy intent |  
| consolidation_criteria | array | yes | [] | Rules for merging entities |  
| stakeholder_impact | string | yes | null | Affected parties and effects |  

### Recommended  
| Field | Type | Notes |  
|---|---|---|  
| related_policies | array | Links to dependent policies |  
| implementation_deadline | date | ISO 8601 format |  
| compliance_checklist | array | Steps for audit verification |  

## ID Pattern  
^p10_cp_[a-z][a-z0-9_]+.md$  

## Body Structure  
1. **Purpose**  
   Define the objective of the consolidation policy.  

2. **Scope**  
   Specify entities, systems, or data affected by the policy.  

3. **Consolidation Rules**  
   Detail criteria for merging, de-duplication, or elimination.  

4. **Stakeholder Impact**  
   Outline implications for users, teams, or external parties.  

5. **Review Cycle**  
   Schedule for policy evaluation and updates.  

6. **Compliance Requirements**  
   Mandate audit trails, documentation, or validation steps.  

## Constraints  
- ID must be unique and conform to the ID Pattern.  
- All required fields must be present and valid.  
- Dates must follow ISO 8601 (YYYY-MM-DD).  
- Quality field must be assigned by peer review, not self-assessment.  
- Tags must use lowercase alphanumeric characters and underscores.  
- Consolidation_criteria must be actionable and unambiguous.
