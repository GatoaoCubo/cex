---
kind: schema
id: bld_schema_vad_config
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for vad_config
quality: 9.1
title: "Schema Vad Config"
version: "1.0.0"
author: wave1_builder_gen
tags: [vad_config, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for vad_config"
domain: "vad_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_schema_reranker_config
  - bld_schema_search_strategy
  - bld_schema_thinking_config
  - bld_schema_usage_report
  - bld_schema_voice_pipeline
  - bld_schema_dataset_card
  - bld_schema_quickstart_guide
  - bld_schema_rl_algorithm
  - bld_schema_sandbox_config
  - bld_schema_benchmark_suite
---

## Frontmatter Fields  
### Required  
| Field      | Type   | Required | Default | Notes |  
|------------|--------|----------|---------|-------|  
| id         | string | yes      | -       | Unique identifier |  
| kind       | string | yes      | "vad_config" | Configuration type |  
| pillar     | string | yes      | "P09"   | Pillar classification |  
| title      | string | yes      | -       | Configuration title |  
| version    | string | yes      | "1.0"   | Schema version |  
| created    | date   | yes      | -       | Creation date |  
| updated    | date   | yes      | -       | Last update date |  
| author     | string | yes      | -       | Author name |  
| domain     | string | yes      | -       | Application domain |  
| quality    | null   | yes      | null    | Never self-score; peer review assigns value |  
| tags       | list   | yes      | []      | Metadata tags |  
| tldr       | string | yes      | -       | Summary |  
| sensitivity| float  | yes      | 0.5     | Detection sensitivity |  
| threshold  | float  | yes      | 0.7     | Activation threshold |  

### Recommended  
| Field         | Type   | Notes |  
|---------------|--------|-------|  
| description   | string | Optional details |  
| use_case      | string | Target application |  
| validation    | string | Validation method |  
| references    | list   | External links |  

## ID Pattern  
`^p09_vad_[a-zA-Z0-9_]+\.yaml$`  

## Body Structure  
1. **Configuration Parameters**  
   - Define core VAD settings  
2. **Sensitivity Settings**  
   - Dynamic adjustment rules  
3. **Language Support**  
   - Supported languages and dialects  
4. **Validation Rules**  
   - Input/output validation criteria  
5. **Sample Rate**  
   - Audio processing requirements  
6. **Use Case**  
   - Specific application context  

## Constraints  
- Max file size: 2048 bytes  
- All required fields must be present  
- ID must follow naming convention  
- Version must use semantic format  
- Sensitivity range: 0.1-1.0 (probability score; 0.5 = 50% confidence floor)
- Threshold (energy): -70 to -10 dBFS (noise floor reference, NOT a 0-1 probability)
- aggressiveness: integer {0, 1, 2, 3} per WebRTC VAD standard
- frame_size_ms: {10, 20, 30} for WebRTC compatibility; 20ms default

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_reranker_config]] | sibling | 0.70 |
| [[bld_schema_search_strategy]] | sibling | 0.69 |
| [[bld_schema_thinking_config]] | sibling | 0.69 |
| [[bld_schema_usage_report]] | sibling | 0.69 |
| [[bld_schema_voice_pipeline]] | sibling | 0.68 |
| [[bld_schema_dataset_card]] | sibling | 0.66 |
| [[bld_schema_quickstart_guide]] | sibling | 0.66 |
| [[bld_schema_rl_algorithm]] | sibling | 0.66 |
| [[bld_schema_sandbox_config]] | sibling | 0.65 |
| [[bld_schema_benchmark_suite]] | sibling | 0.65 |
