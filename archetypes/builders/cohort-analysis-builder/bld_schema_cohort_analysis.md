---
kind: schema
id: bld_schema_cohort_analysis
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for cohort_analysis
quality: 9.1
title: "Schema Cohort Analysis"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [cohort_analysis, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for cohort_analysis"
domain: "cohort_analysis construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Frontmatter Fields  
### Required  
| Field        | Type   | Required | Default | Notes                              |  
|--------------|--------|----------|---------|------------------------------------|  
| id           | string | yes      | null    | Unique identifier                  |  
| kind         | string | yes      | null    | Must be 'cohort_analysis'          |  
| pillar       | string | yes      | null    | Must be 'P07'                      |  
| title        | string | yes      | null    | Descriptive title                  |  
| version      | string | yes      | null    | Semantic version (e.g., 1.0.0)     |  
| created      | date   | yes      | null    | ISO 8601 date                      |  
| updated      | date   | yes      | null    | ISO 8601 date                      |  
| author       | string | yes      | null    | Primary author                     |  
| domain       | string | yes      | null    | Domain (e.g., 'health', 'finance') |  
| quality      | null   | yes      | null    | Never self-score; peer review assigns |  
| tags         | list   | yes      | null    | Keywords for categorization        |  
| tldr         | string | yes      | null    | One-sentence summary               |  
| cohort_definition | string | yes | null | Cohort selection criteria        |  
| analysis_method | string | yes | null | Statistical or analytical approach |  

### Recommended  
| Field         | Type   | Notes                          |  
|---------------|--------|--------------------------------|  
| data_source   | string | Origin of cohort data          |  
| sample_size   | int    | Number of participants         |  

## ID Pattern  
^p07_ca_[a-z][a-z0-9_]+.yaml$  

## Body Structure  
1. **Cohort Definition**  
   - Detailed criteria for cohort selection  
2. **Population Criteria**  
   - Inclusion/exclusion rules and demographics  
3. **Analysis Method**  
   - Statistical techniques and tools used  
4. **Key Findings**  
   - Summary of results and insights  
5. **Interpretation**  
   - Contextual implications and limitations  

## Constraints  
- File must adhere to ID pattern and max 3072 bytes  
- Quality field must be assigned by peer review, not self-scored  
- Version must follow semantic versioning (e.g., 1.0.0)  
- Tags must use lowercase, alphanumeric, and underscores only  
- Domain-specific fields must be populated for validity  
- Created/updated dates must be in ISO 8601 format
