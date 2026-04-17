---
kind: schema
id: bld_schema_diff_strategy
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for diff_strategy
quality: 9.1
title: "Schema Diff Strategy"
version: "1.0.0"
author: wave1_builder_gen
tags: [diff_strategy, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for diff_strategy"
domain: "diff_strategy construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Frontmatter Fields  
### Required
| Field             | Type   | Required | Default         | Notes                                            |
|:------------------|:-------|:---------|:----------------|:-------------------------------------------------|
| id                | string | yes      | -               | Unique identifier                                |
| kind              | string | yes      | "diff_strategy" | CEX type                                         |
| pillar            | string | yes      | "P04"           | Pillar classification                            |
| title             | string | yes      | -               | Strategy name                                    |
| version           | string | yes      | "1.0"           | Semantic version                                 |
| created           | date   | yes      | -               | Creation date                                    |
| updated           | date   | yes      | -               | Last update date                                 |
| author            | string | yes      | -               | Author name                                      |
| domain            | string | yes      | -               | Application domain                               |
| quality           | string | yes      | null            | Quality status (null until peer review)          |
| tags              | list   | yes      | []              | Keywords                                         |
| tldr              | string | yes      | -               | Summary                                          |
| algorithm_type    | enum   | yes      | -               | Myers \| LCS \| patience \| histogram \| Ratcliff-Obershelp \| custom |
| granularity       | enum   | yes      | "line"          | line \| token \| character \| AST \| semantic    |
| comparison_basis  | string | yes      | -               | edit_distance \| unique_lines_LCS \| gestalt      |

### Recommended  
| Field              | Type   | Notes |  
|--------------------|--------|-------|  
| description        | string | Detailed strategy overview |  
| references         | list   | Supporting documents |  
| impact_assessment  | string | Risk/impact analysis |  
| approval_status    | string | Review status |  

## ID Pattern  
^p04_ds_[a-zA-Z0-9_-]+\.md$  

## Body Structure  
1. **Overview**  
   - Purpose, scope, and context of the strategy.  
2. **Strategy Components**  
   - Key elements, assumptions, and dependencies.  
3. **Comparison Metrics**  
   - Criteria for evaluating differences (e.g., performance, risk).  
4. **Implementation Steps**  
   - Workflow, tools, and validation processes.  
5. **Risk Assessment**  
   - Potential issues and mitigation plans.  
6. **Validation Criteria**  
   - Success metrics and review checkpoints.  

## Constraints  
- ID must follow naming convention and be unique.  
- Version must use semantic versioning (e.g., "1.0.0").  
- "strategy_type" and "comparison_basis" must be defined.  
- "domain" must align with CEX domain taxonomy.  
- All required fields must be present and non-empty.  
- Total markdown size must not exceed 4096 bytes.
