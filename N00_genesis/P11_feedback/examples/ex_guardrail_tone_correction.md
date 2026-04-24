---
id: ex_feedback_tone_correction
kind: feedback
8f: F7_govern
pillar: P11
title: "Example — Tone Correction Feedback"
tags: [feedback, tone, correction, guardrail, learning]
tldr: "User corrects agent tone from too-formal to casual. Triggers constraint update, learning record, and future tone adjustment. Shows the feedback→learning loop."
references:
  - tpl_feedback
  - ex_agent_copywriter
quality: 9.0
updated: "2026-04-07"
domain: "feedback and quality"
version: "1.0.0"
author: n03_builder
created: "2026-04-07"
density_score: 0.94
related:
  - p01_kc_brand_voice_consistency_channels
  - brand_voice_templates
  - n06_schema_brand_voice_contract
  - bld_memory_tagline
  - bld_architecture_legal_vertical
  - p01_kc_iterative_refinement_skill
  - bld_architecture_onboarding_flow
  - bld_architecture_healthcare_vertical
  - bld_architecture_benchmark_suite
  - bld_architecture_memory_benchmark
---

# Tone Correction Feedback

## Trigger Event
User said: *"Muito formal, não gostei. Fala mais natural."*

## Feedback Analysis

| Dimension | Before | After |
|-----------|--------|-------|
| Tone | Corporate formal | Conversational casual |
| Vocabulary | "adquirir", "verificar", "destarte" | "comprar", "checar", "então" |
| Sentence length | 25+ words average | 12-15 words average |
| Voice | Passive ("foi verificado") | Active ("a gente checou") |

## Actions Triggered

### 1. Constraint Update
```yaml
# Added to bld_config for this instance
tone_constraints:
  avoid: ["adquirir", "verificar", "destarte", "outrossim", "hereby"]
  prefer: ["comprar", "checar", "então", "tipo", "olha"]
  max_sentence_words: 18
  voice: active
  formality: casual
```

### 2. Learning Record
```json
{
  "type": "tone_correction",
  "source": "user_feedback",
  "before": "formal",
  "after": "casual",
  "specific_words_rejected": ["adquirir", "verificar"],
  "timestamp": "2026-03-31T10:00:00Z",
  "confidence": 0.95
}
```

### 3. Memory Update
Next compilation reads `bld_memory` ISO which now includes:
> "User prefers casual tone. Avoid formal Portuguese. Use active voice."

## Impact Measurement
- Next 5 outputs scored by user: 4/5 "liked", 1/5 "neutral"
- Tone formality score (automated): dropped from 0.8 → 0.3
- Engagement: +40% on social posts after tone change

## Quality Gate
- [ ] Feedback captured with specific examples (not just "too formal")
- [ ] Constraint update is actionable (word lists, not vague)
- [ ] Learning record stored for future reference
- [ ] Impact measured on subsequent outputs

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_brand_voice_consistency_channels]] | upstream | 0.24 |
| [[brand_voice_templates]] | upstream | 0.22 |
| [[n06_schema_brand_voice_contract]] | upstream | 0.18 |
| [[bld_memory_tagline]] | upstream | 0.17 |
| [[bld_architecture_legal_vertical]] | upstream | 0.16 |
| [[p01_kc_iterative_refinement_skill]] | upstream | 0.16 |
| [[bld_architecture_onboarding_flow]] | upstream | 0.16 |
| [[bld_architecture_healthcare_vertical]] | upstream | 0.16 |
| [[bld_architecture_benchmark_suite]] | upstream | 0.16 |
| [[bld_architecture_memory_benchmark]] | upstream | 0.16 |
