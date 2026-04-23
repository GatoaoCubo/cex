---
kind: schema
id: bld_schema_visual_workflow
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for visual_workflow
quality: 9.1
title: "Schema Visual Workflow"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [visual_workflow, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for visual_workflow"
domain: "visual_workflow construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_schema_reranker_config
  - bld_schema_benchmark_suite
  - bld_schema_integration_guide
  - bld_schema_prompt_technique
  - bld_schema_multimodal_prompt
  - bld_schema_eval_metric
  - bld_schema_usage_report
  - bld_schema_app_directory_entry
  - bld_schema_sandbox_spec
  - bld_schema_nps_survey
---

## Frontmatter Fields  
### Required  
| Field | Type | Required | Default | Notes |  
|---|---|---|---|---|  
| id | string | yes | null | Must match ID Pattern |  
| kind | string | yes | "visual_workflow" | Fixed value |  
| pillar | string | yes | "P12" | Fixed value |  
| title | string | yes | null | Descriptive name |  
| version | string | yes | "1.0" | Semantic versioning |  
| created | datetime | yes | null | ISO 8601 format |  
| updated | datetime | yes | null | ISO 8601 format |  
| author | string | yes | null | Owner's identifier |  
| domain | string | yes | null | Application context |  
| quality | null | yes | null | Never self-score; peer review assigns |  
| tags | list | yes | [] | Keywords for search |  
| tldr | string | yes | null | Summary in 1 sentence |  
| diagram_type | string | yes | null | E.g., flowchart, UML |  
| input_output | string | yes | null | Data flow description |  

### Recommended  
| Field | Type | Notes |  
|---|---|---|  
| tooling | string | Software used for creation |  
| revision_history | list | Track changes |  

## ID Pattern  
^p12_vw_[a-z][a-z0-9_]+.md$  

## Body Structure  
1. **Overview**  
   - Purpose, scope, and audience.  
2. **Diagram Specification**  
   - Type, symbols, and conventions.  
3. **Input/Output**  
   - Data sources, formats, and transformations.  
4. **Tooling**  
   - Software, libraries, and dependencies.  
5. **Version History**  
   - Changes, approvals, and authors.  
6. **Access Control**  
   - Permissions and usage policies.  

## Constraints  
- ID must match ^p12_vw_[a-z][a-z0-9_]+.md$ exactly.  
- File size must not exceed 5120 bytes.  
- `quality` field must be assigned by peer review, not self-scored.  
- `diagram_type` must be one of: flowchart, UML, ERD, sequence.  
- `input_output` must describe data flow explicitly.  
- All required fields must be present and valid.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_reranker_config]] | sibling | 0.76 |
| [[bld_schema_benchmark_suite]] | sibling | 0.74 |
| [[bld_schema_integration_guide]] | sibling | 0.74 |
| [[bld_schema_prompt_technique]] | sibling | 0.70 |
| [[bld_schema_multimodal_prompt]] | sibling | 0.70 |
| [[bld_schema_eval_metric]] | sibling | 0.69 |
| [[bld_schema_usage_report]] | sibling | 0.69 |
| [[bld_schema_app_directory_entry]] | sibling | 0.69 |
| [[bld_schema_sandbox_spec]] | sibling | 0.69 |
| [[bld_schema_nps_survey]] | sibling | 0.69 |
