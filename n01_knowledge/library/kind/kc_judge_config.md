---
id: kc_judge_config
kind: knowledge_card
title: LLM Judge Configuration for Automated Evaluation
version: 1.0.0
quality: null
pillar: P01
---

# LLM Judge Configuration for Automated Evaluation

This card defines the configuration parameters for automated evaluation systems using LLM judges. The configuration enables structured assessment of AI-generated outputs through customizable criteria and thresholds.

## Core Configuration Parameters

1. **Model Selection**  
   - `model`: Specify the LLM architecture (e.g., `claude-3`, `gpt-4`, `mixtral`)
   - `temperature`: Control randomness (0.0-1.0)
   - `max_tokens`: Limit response length

2. **Evaluation Thresholds**  
   - `quality_floor`: Minimum acceptable output score (0.0-10.0)
   - `relevance_threshold`: Minimum content relevance percentage (0-100)
   - `consistency_weight`: Weight for response consistency checks

3. **Feedback Mechanism**  
   - `feedback_types`: Array of allowed feedback categories
     - `quality`: Content quality assessment
     - `relevance`: Topic relevance verification
     - `consistency`: Logical coherence check
     - `originality`: Novelty evaluation
   - `feedback_format`: Structured JSON or free text

## Example Configuration
```yaml
judge_config:
  model: claude-3
  temperature: 0.7
  max_tokens: 2048
  quality_floor: 8.5
  relevance_threshold: 90
  consistency_weight: 0.8
  feedback_types:
    - quality
    - relevance
    - consistency
  feedback_format: structured
```

## Implementation Notes
- Configuration should be versioned with semantic versioning
- Use environment variables for sensitive parameters
- Include validation rules for parameter ranges
- Maintain audit logs for configuration changes
```