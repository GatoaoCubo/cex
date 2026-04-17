---
id: kc_judge_config
kind: knowledge_card
title: LLM Judge Configuration for Automated Evaluation
version: 1.0.0
quality: 8.7
pillar: P01
density_score: 0.87
---

# LLM Judge Configuration for Automated Evaluation

This configuration defines parameters for automated evaluation of AI-generated content using LLM judges. Key settings include:

1. **Judge Models**  
   - `model`: Primary evaluation model (e.g., `claude-3-5-sonnet`)
   - `fallback_models`: List of backup models for redundancy
   - `model_version`: Required API version for model compatibility

2. **Evaluation Parameters**  
   - `temperature`: Controls randomness (0.7-1.1)
   - `top_p`: Limits highest possible token probability
   - `max_tokens`: Maximum response length (1024-4096)
   - `presence_penalty`: Penalizes new topics (0-2.0)
   - `frequency_penalty`: Penalizes repeated phrases (0-2.0)

3. **Scoring System**  
   - `quality_floor`: Minimum acceptable score (8.0-10.0)
   - `score_weights`: Weighted average for multi-criteria evaluation
   - `passing_score`: Threshold for successful evaluation

4. **Operational Settings**  
   - `timeout`: Maximum evaluation duration (seconds)
   - `retry_attempts`: Number of failed attempts before abandonment
   - `concurrency_limit`: Maximum parallel evaluations

5. **Security Constraints**  
   - `content_filter`: Enables/disables harmful content detection
   - `safety_rating`: Enables/disables safety score calculation
   - `audit_log`: Enables/disables evaluation process logging

6. **Integration Options**  
   - `api_key`: Authentication token for external services
   - `endpoint`: Custom API endpoint for model hosting
   - `proxy`: HTTP proxy configuration for network routing

7. **Performance Optimization**  
   - `batch_size`: Number of evaluations per batch
   - `cache_ttl`: Time-to-live for cached evaluation results
   - `prefetch`: Preloads models for faster sequential evaluations

8. **Compliance Settings**  
   - `data_retention`: Controls evaluation data storage duration
   - `audit_trail`: Enables/disables historical evaluation tracking
   - `regulatory_compliance`: Specifies applicable legal standards

This configuration enables systematic, repeatable evaluation of AI outputs while maintaining flexibility for specialized use cases. All parameters support dynamic adjustment through the CEX governance framework.
