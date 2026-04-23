---
id: kc_content_filter
kind: knowledge_card
title: Content Filter Pipeline Configuration
version: 1.0.0
quality: 8.6
pillar: P01
density_score: 1.0
related:
  - p03_ch_kc_to_notebooklm
  - p03_ch_content_pipeline
  - content-filter-builder
  - bld_output_template_function_def
  - bld_examples_function_def
  - p03_cs_json_output
  - bld_instruction_content_filter
  - p03_sp_content_filter_builder
  - bld_output_template_input_schema
  - bld_examples_content_filter
---

# Content Filter Pipeline Configuration

This knowledge card defines the configuration schema for content filtering pipelines. The pipeline operates in three stages:

1. **Preprocessing**  
   - Text normalization (lowercasing, tokenization)
   - Special character removal
   - HTML entity decoding

2. **Filtering**  
   - NSFW content detection (using ML model)
   - Toxicity score calculation
   - Policy rule matching

3. **Post-processing**  
   - Result categorization (safe/unsafe/unknown)
   - Contextual risk assessment
   - Automated moderation recommendations

The pipeline accepts raw text input and produces structured output containing:
- Filter decision (pass/block/flag)
- Confidence score (0.0-1.0)
- Detected patterns
- Suggested mitigation actions

Configuration parameters include:
- `threshold`: Minimum confidence for blocking (default 0.85)
- `ruleset`: Policy rules to apply (default "community_guidelines")
- `language`: Text language code (auto-detected if empty)
- `context_window`: Maximum input length (default 1024 tokens)

```yaml
pipeline:
  stages:
    - name: preprocessing
      enabled: true
    - name: filtering
      enabled: true
    - name: post-processing
      enabled: true
```

```json
output_schema:
  type: object
  properties:
    decision: {type: string, enum: ["pass", "block", "flag"]}
    confidence: {type: number, minimum: 0, maximum: 1}
    patterns: {type: array, items: {type: string}}
    recommendations: {type: array, items: {type: string}}
```
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_ch_kc_to_notebooklm]] | downstream | 0.28 |
| [[p03_ch_content_pipeline]] | downstream | 0.28 |
| [[content-filter-builder]] | downstream | 0.23 |
| [[bld_output_template_function_def]] | downstream | 0.23 |
| [[bld_examples_function_def]] | downstream | 0.22 |
| [[p03_cs_json_output]] | downstream | 0.22 |
| [[bld_instruction_content_filter]] | downstream | 0.22 |
| [[p03_sp_content_filter_builder]] | downstream | 0.22 |
| [[bld_output_template_input_schema]] | downstream | 0.22 |
| [[bld_examples_content_filter]] | downstream | 0.21 |
