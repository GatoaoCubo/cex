---
kind: schema
id: bld_schema_interactive_demo
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for interactive_demo
quality: 9.1
title: "Schema Interactive Demo"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [interactive_demo, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for interactive_demo"
domain: "interactive_demo construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_schema_integration_guide
  - bld_schema_reranker_config
  - bld_schema_benchmark_suite
  - bld_schema_sandbox_spec
  - bld_schema_app_directory_entry
  - bld_schema_eval_metric
  - bld_schema_multimodal_prompt
  - bld_schema_audit_log
  - bld_schema_usage_report
  - bld_schema_quickstart_guide
---

## Frontmatter Fields  
### Required  
| Field      | Type   | Required | Default | Notes                              |  
|------------|--------|----------|---------|------------------------------------|  
| id         | string | yes      | null    | Must match ID Pattern              |  
| kind       | string | yes      | null    | Always "interactive_demo"          |  
| pillar     | string | yes      | null    | Always "P05"                       |  
| title      | string | yes      | null    | Descriptive title                  |  
| version    | string | yes      | "1.0"   | Semantic versioning                |  
| created    | date   | yes      | null    | ISO 8601 format                    |  
| updated    | date   | yes      | null    | ISO 8601 format                    |  
| author     | string | yes      | null    | Author name                        |  
| domain     | string | yes      | null    | Application domain (e.g., "AI")    |  
| quality    | null   | yes      | null    | Never self-score; peer review assigns |  
| tags       | list   | yes      | []      | Keywords for categorization        |  
| tldr       | string | yes      | null    | One-sentence summary               |  
| demo_url   | string | yes      | null    | Live demo link                     |  
| interactive_elements | list | yes | [] | Features like clickables, sliders |  

### Recommended  
| Field              | Type   | Notes                  |  
|--------------------|--------|------------------------|  
| demo_duration      | string | Estimated interaction time |  
| target_audience    | string | Intended user group    |  
| prerequisites      | list   | Skills/tools required  |  

## ID Pattern  
^p05_id_[a-z][a-z0-9_]+.md$  

## Body Structure  
1. **Overview**  
   - Purpose and scope of the demo  
2. **Interactive Elements**  
   - Detailed description of user-facing features  
3. **User Feedback**  
   - Mechanisms for collecting input  
4. **Technical Requirements**  
   - Hardware/software dependencies  
5. **Demo URL**  
   - Direct link to live/demo environment  

## Constraints  
- ID must match ^p05_id_[a-z][a-z0-9_]+.md$ exactly  
- File size must not exceed 6144 bytes  
- All required fields must be present and valid  
- Quality field must be assigned by peer review, not self-scored  
- Domain-specific fields (demo_url, interactive_elements) must be non-empty  
- Markdown must use ASCII characters only and stay under 80 lines

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_integration_guide]] | sibling | 0.77 |
| [[bld_schema_reranker_config]] | sibling | 0.72 |
| [[bld_schema_benchmark_suite]] | sibling | 0.72 |
| [[bld_schema_sandbox_spec]] | sibling | 0.69 |
| [[bld_schema_app_directory_entry]] | sibling | 0.69 |
| [[bld_schema_eval_metric]] | sibling | 0.68 |
| [[bld_schema_multimodal_prompt]] | sibling | 0.68 |
| [[bld_schema_audit_log]] | sibling | 0.68 |
| [[bld_schema_usage_report]] | sibling | 0.67 |
| [[bld_schema_quickstart_guide]] | sibling | 0.67 |
