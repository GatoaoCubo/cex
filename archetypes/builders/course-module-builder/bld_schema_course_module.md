---
kind: schema
id: bld_schema_course_module
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for course_module
quality: null
title: "Schema Course Module"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [course_module, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for course_module"
domain: "course_module construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Frontmatter Fields  
### Required  
| Field       | Type   | Required | Default | Notes                              |  
|-------------|--------|----------|---------|------------------------------------|  
| id          | string | yes      | null    | Must match ID Pattern              |  
| kind        | string | yes      | "course_module" | Fixed value                  |  
| pillar      | string | yes      | "P05"   | Fixed value                        |  
| title       | string | yes      | null    | Human-readable name                |  
| version     | string | yes      | "1.0"   | Semantic versioning                |  
| created     | date   | yes      | null    | ISO 8601                           |  
| updated     | date   | yes      | null    | ISO 8601                           |  
| author      | string | yes      | null    | Creator                            |  
| domain      | string | yes      | null    | e.g., "math", "cs"                 |  
| quality     | null   | yes      | null    | Never self-score; peer review assigns |  
| tags        | array  | yes      | []      | Keywords for search                |  
| tldr        | string | yes      | null    | Summary (max 250 chars)            |  
| learning_outcomes | array | yes | [] | List of learning objectives        |  
| prerequisites | array | yes | [] | Required prior knowledge           |  

### Recommended  
| Field             | Type   | Notes                  |  
|-------------------|--------|------------------------|  
| difficulty_level  | string | e.g., "beginner", "advanced" |  
| estimated_time    | string | e.g., "4 hours"        |  

## ID Pattern  
^p05_cm_[a-z][a-z0-9_]+.md$  

## Body Structure  
1. **Overview**  
   Brief description of the module’s purpose and scope.  

2. **Learning Outcomes**  
   Detailed list of skills or knowledge students will gain.  

3. **Prerequisites**  
   Required background knowledge or prior modules.  

4. **Content Structure**  
   Breakdown of lessons, activities, and resources.  

5. **Assessment Methods**  
   Evaluation strategies (e.g., quizzes, projects).  

## Constraints  
- ID must match ^p05_cm_[a-z][a-z0-9_]+.md$ exactly.  
- Version must follow semantic versioning (e.g., 1.0.0).  
- All required fields must be present and non-null.  
- Domain-specific fields (learning_outcomes, prerequisites) must be arrays.  
- File size must not exceed 8192 bytes.  
- Tags must be lowercase, alphanumeric, and underscore-separated.
