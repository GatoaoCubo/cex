---
kind: schema
id: bld_schema_planning_strategy
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for planning_strategy
quality: null
title: "Schema Planning Strategy"
version: "1.0.0"
author: wave1_builder_gen
tags: [planning_strategy, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for planning_strategy"
domain: "planning_strategy construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Frontmatter Fields  
### Required  
| Field        | Type   | Required | Default | Notes |  
|--------------|--------|----------|---------|-------|  
| id           | string | yes      |         | Regex: ^p03_ps_[a-zA-Z0-9_-]+\.md$ |  
| kind         | string | yes      |         | "planning_strategy" |  
| pillar       | string | yes      |         | "P03" |  
| title        | string | yes      |         | Strategy name |  
| version      | string | yes      | "1.0"   | Semantic versioning |  
| created      | date   | yes      |         | ISO 8601 |  
| updated      | date   | yes      |         | ISO 8601 |  
| author       | string | yes      |         | Owner name |  
| domain       | string | yes      |         | "CEX" |  
| quality      | string | yes      | "draft" | "draft", "review", "approved" |  
| tags         | array  | yes      | []      | Keywords |  
| tldr         | string | yes      |         | Summary (≤250 chars) |  
| strategy_type| string | yes      |         | "operational", "tactical", "strategic" |  
| scope        | string | yes      |         | Geographic, functional, or temporal boundaries |  

### Recommended  
| Field              | Type   | Notes |  
|--------------------|--------|-------|  
| impact_assessment  | string | Risk/benefit analysis |  
| stakeholders       | array  | Involved parties |  

## ID Pattern  
^p03_ps_[a-zA-Z0-9_-]+\.md$  

## Body Structure  
1. **Objectives**  
   - Clear, measurable goals aligned with organizational priorities.  
2. **Scope**  
   - Defined boundaries (geographic, functional, temporal).  
3. **Key Initiatives**  
   - Actionable steps, timelines, and responsible parties.  
4. **Risk Assessment**  
   - Identified risks, mitigation plans, and contingency measures.  
5. **Success Metrics**  
   - KPIs, evaluation criteria, and review intervals.  
6. **Stakeholder Engagement**  
   - Communication plans and collaboration mechanisms.  

## Constraints  
- Strategy_type must be one of: "operational", "tactical", "strategic".  
- Scope must specify at least one boundary type (geographic, functional, temporal).  
- All dates must use ISO 8601 format (YYYY-MM-DD).  
- Tags must be lowercase, alphanumeric, and separated by commas.  
- TLDR must be ≤250 characters.  
- At least two stakeholders must be listed in the stakeholders array.
