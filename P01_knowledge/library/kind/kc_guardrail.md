---
id: kc_guardrail
kind: knowledge_card
title: "LLM Safety Guardrails"
version: 1.0.0
quality: 8.8
pillar: P01
density_score: 1.0
---

# LLM Safety Guardrails

Guardrails are essential for ensuring safe, ethical, and effective use of large language models. This card covers key safety mechanisms:

## Core Guardrail Types

1. **Input Validation**
   - Filters malicious or harmful input
   - Detects format errors and invalid queries
   - Prevents prompt injection attacks

2. **Output Filtering**
   - Blocks harmful, biased, or inappropriate responses
   - Enforces content policies and guidelines
   - Removes sensitive information

3. **Content Moderation**
   - Monitors for hate speech, harassment, and violence
   - Filters explicit or graphic content
   - Enforces community standards

4. **PII Detection**
   - Identifies personally identifiable information
   - Anonymizes sensitive data
   - Protects user privacy

5. **Toxicity Filtering**
   - Detects hate speech and toxic language
   - Blocks discriminatory content
   - Promotes inclusive communication

## Guardrail Comparison

| Guardrail Type     | Purpose               | Techniques                          | Use Cases                        |
|--------------------|-----------------------|-------------------------------------|----------------------------------|
| Input Validation   | Prevent harmful input | Regex patterns, syntax checks       | Malicious query detection        |
| Output Filtering   | Block unsafe responses | Content policies, keyword filtering | Hate speech prevention           |
| Content Moderation | Enforce community standards | NLP-based moderation, classifiers | Hate speech, harassment detection |
| PII Detection      | Protect user privacy   | Anonymization, redaction            | Sensitive data handling          |
| Toxicity Filtering | Prevent toxic output   | Sentiment analysis, toxicity scores | Discriminatory content blocking  |
