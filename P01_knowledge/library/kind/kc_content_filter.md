---
id: kc_content_filter
kind: knowledge_card
title: Content Filter Pipeline Configuration
version: 1.0.0
quality: 8.6
pillar: P01
density_score: 1.0
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