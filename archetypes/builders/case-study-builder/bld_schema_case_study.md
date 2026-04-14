---
kind: schema
id: bld_schema_case_study
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for case_study
quality: null
title: "Schema Case Study"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [case_study, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for case_study"
domain: "case_study construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Frontmatter Fields  
### Required  
| Field     | Type   | Required | Default | Notes |  
|-----------|--------|----------|---------|-------|  
| id        | string | yes      |         |       |  
| kind      | string | yes      |         |       |  
| pillar    | string | yes      |         |       |  
| title     | string | yes      |         |       |  
| version   | string | yes      |         |       |  
| created   | date   | yes      |         |       |  
| updated   | date   | yes      |         |       |  
| author    | string | yes      |         |       |  
| domain    | string | yes      |         |       |  
| quality   | null   | yes      | null    | Never self-score; peer review assigns |  
| tags      | array  | yes      |         |       |  
| tldr      | string | yes      |         |       |  
| context   | string | yes      |         | Case background |  
| outcome   | string | yes      |         | Key result |  

### Recommended  
| Field              | Type   | Notes |  
|--------------------|--------|-------|  
| references         | array  |       |  
| methodology        | string |       |  
| impact_assessment  | string |       |  

## ID Pattern  
^p05_cs_[a-z][a-z0-9_]+.md$  

## Body Structure  
1. **Introduction**  
2. **Context**  
3. **Analysis**  
4. **Outcomes**  
5. **Lessons Learned**  
6. **Stakeholders**  

## Constraints  
- ID must match ^p05_cs_[a-z][a-z0-9_]+.md$  
- File size must not exceed 6144 bytes  
- All required fields must be present  
- Quality field must be peer-reviewed, not self-assigned  
- Domain-specific fields (context, outcome) must be non-empty  
- ASCII-only characters required
