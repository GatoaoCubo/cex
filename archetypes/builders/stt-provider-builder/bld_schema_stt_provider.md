---
kind: schema
id: bld_schema_stt_provider
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for stt_provider
quality: 9.1
title: "Schema Stt Provider"
version: "1.0.0"
author: wave1_builder_gen
tags: [stt_provider, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for stt_provider"
domain: "stt_provider construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_schema_reranker_config
  - bld_schema_benchmark_suite
  - bld_schema_usage_report
  - bld_schema_multimodal_prompt
  - bld_schema_dataset_card
  - bld_schema_pitch_deck
  - bld_schema_integration_guide
  - bld_schema_sandbox_config
  - bld_schema_voice_pipeline
  - bld_schema_tts_provider
---

## Frontmatter Fields  
### Required  
| Field        | Type       | Required | Default | Notes                          |  
|--------------|------------|----------|---------|--------------------------------|  
| id           | string     | yes      | -       | Unique identifier              |  
| kind         | string     | yes      | "stt_provider" | CEX kind                 |  
| pillar       | string     | yes      | "P04"    | Pillar classification          |  
| title        | string     | yes      | -       | Provider name                  |  
| version      | string     | yes      | "1.0.0"  | Semantic versioning            |  
| created      | datetime   | yes      | -       | ISO 8601 format                |  
| updated      | datetime   | yes      | -       | ISO 8601 format                |  
| author       | string     | yes      | -       | Owner/organization             |  
| domain       | string     | yes      | -       | Service domain (e.g., "health")|  
| quality      | null       | yes      | null     | MUST be null -- peer review assigns |
| tags         | array      | yes      | []      | Keywords                       |  
| tldr         | string     | yes      | -       | Summary                        |  
| language_support | array  | yes      | []      | Supported languages            |  
| accuracy_rating | number   | yes      | 0        | 0–100 accuracy score           |  

### Recommended  
| Field              | Type   | Notes                          |  
|--------------------|--------|--------------------------------|  
| description        | string | Detailed provider description  |  
| license            | string | Legal terms                    |  

## ID Pattern  
`^p04_stt_[a-zA-Z0-9]+$`  

## Body Structure  
1. **Overview**  
   - Description of the STT provider’s purpose and scope.  
2. **Technical Specifications**  
   - Language models, APIs, and integration methods.  
3. **Use Cases**  
   - Scenarios where the provider is applicable.  
4. **Compliance**  
   - Data privacy, security, and regulatory adherence.  
5. **Performance Metrics**  
   - Accuracy, latency, and scalability benchmarks.  

## Constraints  
- All required fields must be present and valid.  
- `id` must match the regex pattern `^p04_stt_[a-zA-Z0-9]+$`.  
- `language_support` must be an array of strings.  
- `accuracy_rating` must be a number between 0 and 100.  
- `version` must follow semantic versioning (e.g., "1.2.3").  
- `domain` must align with predefined categories (e.g., "health", "finance").

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_reranker_config]] | sibling | 0.72 |
| [[bld_schema_benchmark_suite]] | sibling | 0.72 |
| [[bld_schema_usage_report]] | sibling | 0.69 |
| [[bld_schema_multimodal_prompt]] | sibling | 0.69 |
| [[bld_schema_dataset_card]] | sibling | 0.69 |
| [[bld_schema_pitch_deck]] | sibling | 0.68 |
| [[bld_schema_integration_guide]] | sibling | 0.68 |
| [[bld_schema_sandbox_config]] | sibling | 0.68 |
| [[bld_schema_voice_pipeline]] | sibling | 0.68 |
| [[bld_schema_tts_provider]] | sibling | 0.68 |
