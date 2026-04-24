---
id: n06_schema_brand_voice_contract
kind: constraint_spec
8f: F1_constrain
pillar: P06
title: "Brand Voice Contract — 5D Consistency Validation"
version: 1.0.0
created: 2026-04-01
author: n06_commercial
domain: brand-voice-validation
quality: 9.2
updated: 2026-04-07
tags: [schema, brand, voice, contract, consistency, n06]
tldr: "Validates voice consistency across channels. 5D scores within ±1 tolerance of brand_config. Tone matrix per channel. Do/Don't hard constraints."
density_score: 0.93
axioms:
  - "5D scores must stay within ±1 of brand_config values — larger deviation = brand drift."
  - "Do/Don't constraints are HARD — violating a Don't is an automatic quality failure."
linked_artifacts:
  primary: p01_kc_brand_voice_systems
  related: [n06_output_brand_voice_guide, n06_schema_brand_audit, p03_sp_commercial_nucleus]
related:
  - n06_output_brand_voice_guide
  - p01_kc_brand_voice_consistency_channels
  - p03_brand_audit_prompt
  - p03_sp_commercial_nucleus
  - p03_sp_brand_nucleus
  - spec_n06_part2
  - p03_brand_book_generator
  - brand_voice_templates
  - n06_output_brand_book
  - p03_pt_marketing_task_execution
---

# Brand Voice Contract

## 5D Voice Dimensions

Each dimension scored 1-5 in `brand_config.yaml`:

| Dimension | 1 | 2 | 3 | 4 | 5 |
|-----------|---|---|---|---|---|
| Formality | Casual/slang | Relaxed | Balanced | Professional | Formal/academic |
| Enthusiasm | Deadpan | Measured | Engaged | Energetic | Exuberant |
| Humor | None | Subtle/dry | Occasional | Frequent | Constant/playful |
| Warmth | Cold/clinical | Neutral | Friendly | Warm | Intimate/personal |
| Authority | Peer/equal | Knowledgeable | Expert | Authoritative | Commanding |

## Channel Tolerance Matrix

Voice scores may shift ±1 per channel from base brand_config values:

| Channel | Formality | Enthusiasm | Humor | Warmth | Authority |
|---------|-----------|------------|-------|--------|-----------|
| Social media | -1 | +1 | +1 | +1 | -1 |
| Blog/articles | 0 | 0 | 0 | 0 | 0 |
| Documentation | +1 | -1 | -1 | 0 | +1 |
| Email marketing | -1 | +1 | 0 | +1 | 0 |
| Sales pages | 0 | +1 | 0 | +1 | +1 |
| Customer support | -1 | 0 | 0 | +1 | -1 |
| Ads (paid) | -1 | +1 | context | +1 | 0 |

## Validation Rules

### Hard Constraints
1. No dimension may exceed bounds (1-5) after channel adjustment
2. Do's from `BRAND_VOICE_DO` must be present in ALL channel outputs
3. Don'ts from `BRAND_VOICE_DONT` must be absent from ALL channel outputs
4. `BRAND_LANGUAGE` must be consistent (no mixing pt-BR/en-US within artifact)

### Soft Constraints (warnings)
1. Voice shift > ±1 from base triggers review
2. Humor in formal contexts (docs, legal) triggers warning
3. Low authority (1-2) in sales contexts triggers warning
4. Inconsistent tone across paragraphs within same artifact

## Example Phrases (Calibration)

Brand Book Block 15 provides 10 example phrases. These serve as calibration:
- Every output should SOUND like these phrases
- Copywriters read phrases before writing
- LLMs receive phrases as few-shot examples in prompt

## Voice Injection Snippet

For LLM prompts, inject this block from brand_config:
```
Voice: {{BRAND_VOICE_TONE}}
Formality: {{BRAND_VOICE_FORMALITY}}/5
Enthusiasm: {{BRAND_VOICE_ENTHUSIASM}}/5
Humor: {{BRAND_VOICE_HUMOR}}/5
Warmth: {{BRAND_VOICE_WARMTH}}/5
Authority: {{BRAND_VOICE_AUTHORITY}}/5
DO: {{BRAND_VOICE_DO}}
DON'T: {{BRAND_VOICE_DONT}}
```

## Scoring

Voice consistency score = (matching_dimensions / total_dimensions)
- Passing: >= 0.80 (4/5 dimensions within tolerance)
- Excellent: 1.00 (all dimensions within tolerance for channel)
- Failing: < 0.60 (re-calibrate voice or retrain copy)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[n06_output_brand_voice_guide]] | upstream | 0.54 |
| [[p01_kc_brand_voice_consistency_channels]] | upstream | 0.43 |
| [[p03_brand_audit_prompt]] | upstream | 0.27 |
| [[p03_sp_commercial_nucleus]] | upstream | 0.26 |
| [[p03_sp_brand_nucleus]] | upstream | 0.25 |
| [[spec_n06_part2]] | sibling | 0.24 |
| [[p03_brand_book_generator]] | upstream | 0.24 |
| [[brand_voice_templates]] | upstream | 0.24 |
| [[n06_output_brand_book]] | upstream | 0.23 |
| [[p03_pt_marketing_task_execution]] | upstream | 0.22 |
