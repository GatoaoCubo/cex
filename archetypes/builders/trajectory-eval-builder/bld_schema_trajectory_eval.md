---
kind: schema
id: bld_schema_trajectory_eval
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for trajectory_eval
quality: null
title: "Schema Trajectory Eval"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [trajectory_eval, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for trajectory_eval"
domain: "trajectory_eval construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Frontmatter Fields  
### Required  
| Field | Type | Required | Default | Notes |  
|---|---|---|---|---|  
| id | string | yes |  | Must match ID Pattern |  
| kind | string | yes |  | Fixed to 'trajectory_eval' |  
| pillar | string | yes |  | Fixed to 'P07' |  
| title | string | yes |  | Human-readable name |  
| version | string | yes |  | Semantic version (e.g., '1.0.0') |  
| created | datetime | yes |  | ISO 8601 format |  
| updated | datetime | yes |  | ISO 8601 format |  
| author | string | yes |  | Owner's identifier |  
| domain | string | yes |  | Application domain (e.g., 'robotics') |  
| quality | null | yes | null | Never self-score; peer review assigns |  
| tags | list | yes |  | Keywords for categorization |  
| tldr | string | yes |  | Summary in 1–2 sentences |  
| start_point | string | yes |  | Initial trajectory coordinate |  
| end_point | string | yes |  | Final trajectory coordinate |  

### Recommended  
| Field | Type | Notes |  
|---|---|---|  
| reference_trajectory | string | Optional baseline for comparison |  
| deviation_threshold | float | Max allowable deviation (m) |  
| evaluation_method | string | E.g., 'RMSE', 'F1-score' |  
| confidence_interval | float | Statistical confidence level (e.g., 0.95) |  

## ID Pattern  
^p07_te_[a-z][a-z0-9_]+.md$  

## Body Structure  
1. **Trajectory Overview**  
   - Description of the evaluated path and context.  
2. **Evaluation Metrics**  
   - Quantitative results (e.g., accuracy, smoothness).  
3. **Path Analysis**  
   - Breakdown of start_point → end_point progression.  
4. **Deviation Analysis**  
   - Comparison to reference_trajectory (if provided).  
5. **Constraints and Limitations**  
   - Assumptions, data gaps, or environmental factors.  
6. **Conclusion**  
   - Summary of validity and next steps.  

## Constraints  
- ID must match ^p07_te_[a-z][a-z0-9_]+.md$ exactly.  
- All required fields must be present and non-null.  
- Version must follow semantic versioning (e.g., '1.2.3').  
- Quality field must be assigned by peer review, not self-reported.  
- Domain-specific fields (start_point, end_point) must be numeric or coordinate-based.  
- Total file size must not exceed 5120 bytes.
