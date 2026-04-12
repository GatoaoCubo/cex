---
id: bench_f
kind: knowledge_card
title: LLM Guardrails
version: 1.0.0
quality: null
---

# LLM Safety Guardrails

## 4 Core Types
1. **Input Validation**  
   - Blocks harmful inputs via regex, keyword checks, and schema validation  
   - Prevents toxic language, malware, and format attacks  

2. **Output Filtering**  
   - Sanitizes responses with profanity filters, code injectors, and bias detectors  
   - Ensures compliance with content policies and ethical guidelines  

3. **Rate Limiting**  
   - Caps request frequency per user/IP to prevent abuse  
   - Implements token bucket and sliding window algorithms  

4. **Content Moderation**  
   - Uses policy-based filters for harmful content detection  
   - Integrates with third-party moderation APIs and human review  

## Comparison Table

| Guardrail Type       | Purpose               | Key Techniques                  | Use Cases                     |
|----------------------|-----------------------|---------------------------------|-------------------------------|
| Input Validation     | Block harmful inputs  | Regex, keyword checks, schemas  | Toxic language detection      |
| Output Filtering     | Sanitize responses    | Profanity filters, code injectors | Bias detection, code safety   |
| Rate Limiting        | Prevent abuse         | Token bucket, sliding window    | DDoS protection, API throttling |
| Content Moderation   | Enforce policies      | Policy rules, moderation APIs   | Hate speech detection, NSFW filtering |
