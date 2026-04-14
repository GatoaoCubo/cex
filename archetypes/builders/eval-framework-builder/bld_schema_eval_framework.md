---
kind: schema
id: bld_schema_eval_framework
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for eval_framework
quality: null
title: "Schema Eval Framework"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [eval_framework, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for eval_framework"
domain: "eval_framework construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Frontmatter Fields  
### Required  
| Field      | Type   | Required | Default | Notes |  
|------------|--------|----------|---------|-------|  
| id         | string | yes      |         | Must match ID Pattern |  
| kind       | string | yes      |         | Always "eval_framework" |  
| pillar     | string | yes      |         | Always "P07" |  
| title      | string | yes      |         | Human-readable name |  
| version    | string | yes      | "1.0"   | Semantic versioning |  
| created    | date   | yes      |         | ISO 8601 format |  
| updated    | date   | yes      |         | ISO 8601 format |  
| author     | string | yes      |         | Maintainer name |  
| domain     | string | yes      |         | Application domain (e.g., "NLP") |  
| quality    | null   | yes      | null    | Never self-score; peer review assigns |  
| tags       | array  | yes      | []      | Keywords for discovery |  
| tldr       | string | yes      |         | One-sentence summary |  
| framework_type | string | yes |         | Type of evaluation framework (e.g., "benchmark", "test_suite") |  
| evaluation_criteria | array | yes | [] | Core criteria evaluated |  

### Recommended  
| Field          | Type   | Notes |  
|----------------|--------|-------|  
| license        | string | Open source license |  
| dependencies   | array  | Required libraries/tools |  
| compatibility  | string | System/tech requirements |  
| references     | array  | Citations or links |  

## ID Pattern  
^p07_efw_[a-z][a-z0-9_]+.md$  

## Body Structure  
1. **Overview**  
   - Purpose, scope, and intended use of the framework.  

2. **Evaluation Criteria**  
   - Detailed description of metrics and success indicators.  

3. **Metrics**  
   - Quantitative and qualitative measures tracked.  

4. **Use Cases**  
   - Scenarios where the framework is applied.  

5. **Compatibility**  
   - Supported platforms, languages, or systems.  

6. **References**  
   - Documentation, papers, or tools related to the framework.  

## Constraints  
- ID must match exact regex pattern.  
- Quality field must be assigned by peer review, not self-scored.  
- Domain-specific fields (framework_type, evaluation_criteria) are mandatory.  
- Version must follow semantic versioning (e.g., "1.2.3").  
- Tags must be lowercase, alphanumeric, and underscore-separated.  
- File size must not exceed 5120 bytes.
