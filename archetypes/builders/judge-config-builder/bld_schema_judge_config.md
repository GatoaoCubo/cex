---
kind: schema
id: bld_schema_judge_config
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for judge_config
quality: null
title: "Schema Judge Config"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [judge_config, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for judge_config"
domain: "judge_config construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Frontmatter Fields  
### Required  
| Field | Type | Required | Default | Notes |  
|---|---|---|---|---|  
| id | string | yes |  | Must match ID Pattern |  
| kind | string | yes | "judge_config" |  |  
| pillar | string | yes | "P07" |  |  
| title | string | yes |  | Descriptive name |  
| version | string | yes | "1.0.0" | Semantic versioning |  
| created | date | yes |  | ISO 8601 format |  
| updated | date | yes |  | ISO 8601 format |  
| author | string | yes |  | Owner's identifier |  
| domain | string | yes |  | Application context |  
| quality | null | yes | null | Never self-score; peer review assigns |  
| tags | array | yes | [] | Keywords for categorization |  
| tldr | string | yes |  | Summary of purpose |  
| judgment_criteria | array | yes | [] | List of evaluation rules |  
| scoring_weights | object | yes | {} | Key-value pairs for criteria importance |  

### Recommended  
| Field | Type | Notes |  
|---|---|---|  
| example_judgment | string | Sample output for clarity |  
| reviewers | array | List of peer reviewers |  
| last_reviewed | date | Last peer review date |  
| notes | string | Additional context |  

## ID Pattern  
^p07_jc_[a-z][a-z0-9_]+.md$  

## Body Structure  
1. **Introduction**  
   Overview of the judge_config's purpose and scope.  

2. **Judgment Criteria**  
   Detailed description of evaluation rules and thresholds.  

3. **Scoring Weights**  
   Explanation of how criteria influence final scores.  

4. **Review Process**  
   Steps for peer validation and quality assurance.  

5. **Constraints**  
   Hard limits on inputs, outputs, or configurations.  

6. **Example**  
   Illustrative use case with expected outcomes.  

## Constraints  
- All judgment_criteria must be objective and quantifiable.  
- Scoring_weights must sum to 100% across all criteria.  
- File size must not exceed 4096 bytes.  
- Tags must follow domain-specific naming conventions.  
- Peer review is mandatory for quality field assignment.  
- Created and updated dates must be synchronized with versioning.
