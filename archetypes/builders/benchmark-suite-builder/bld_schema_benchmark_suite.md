---
kind: schema
id: bld_schema_benchmark_suite
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for benchmark_suite
quality: 9.1
title: "Schema Benchmark Suite"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [benchmark_suite, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for benchmark_suite"
domain: "benchmark_suite construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Frontmatter Fields  
### Required  
| Field | Type | Required | Default | Notes |  
|---|---|---|---|---|  
| id | string | yes | null | Must match ID Pattern |  
| kind | string | yes | "benchmark_suite" | Fixed value |  
| pillar | string | yes | "P07" | Fixed value |  
| title | string | yes | null | Human-readable name |  
| version | string | yes | "1.0.0" | Semantic versioning |  
| created | datetime | yes | null | ISO 8601 format |  
| updated | datetime | yes | null | ISO 8601 format |  
| author | string | yes | null | Primary contributor |  
| domain | string | yes | null | Application domain (e.g., "NLP") |  
| quality | null | yes | null | Never self-score; peer review assigns |  
| tags | list | yes | [] | Keywords for categorization |  
| tldr | string | yes | null | One-sentence summary |  
| benchmark_type | string | yes | null | E.g., "performance", "accuracy" |  
| metrics | list | yes | [] | Quantitative evaluation criteria |  
| reference_dataset | string | yes | null | Dataset used for benchmarking |  
| implementation_language | string | yes | null | E.g., "Python", "Rust" |  

### Recommended  
| Field | Type | Notes |  
|---|---|---|  
| license | string | Legal terms for reuse |  
| dependencies | list | Required libraries/frameworks |  
| notes | string | Additional context or limitations |  
| citation | string | Academic or technical reference |  

## ID Pattern  
^p07_bs_[a-z][a-z0-9_]+.md$  

## Body Structure  
1. **Overview**  
   - Purpose, scope, and intended use cases.  
2. **Benchmark Metrics**  
   - Detailed description of each metric and its significance.  
3. **Reference Dataset**  
   - Source, structure, and preprocessing steps.  
4. **Implementation Details**  
   - Code structure, dependencies, and execution environment.  
5. **Usage Instructions**  
   - Steps to reproduce results and validate benchmarks.  
6. **Evaluation Criteria**  
   - Success thresholds, comparison baselines, and validation methods.  

## Constraints  
- ID must conform to regex: ^p07_bs_[a-z][a-z0-9_]+.md$  
- All required fields must be present and non-null  
- Version must follow semantic versioning (e.g., "1.2.3")  
- Metrics and tags must be human-readable and machine-parsable  
- File size must not exceed 5120 bytes  
- Quality field must be assigned by peer review, not self-reported
