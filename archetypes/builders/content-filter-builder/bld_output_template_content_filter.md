---
kind: output_template
id: bld_output_template_content_filter
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for content_filter production
quality: 9.1
title: "Output Template Content Filter"
version: "1.1.0"
author: n06_hybrid_review
tags: [content_filter, builder, output_template]
tldr: "Template for content_filter artifacts -- correct frontmatter, named harm categories, enforcement_action per stage, and latency SLA targets."
domain: "content_filter construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.92
---

# p11_cf_{{name}}.md

This ISO defines a content filter -- the moderation rules that gate output or input.

```yaml
---
id: p11_cf_{{name}}
kind: content_filter
pillar: P11
title: "{{title}}"
version: "1.0.0"
author: "{{author}}"
created: "{{date}}"
updated: "{{date}}"
domain: "{{domain}}"
quality: null
tags: [content_filter, {{scope_tag}}]
tldr: "{{one_line_purpose}}"
filter_type: "{{pre_inference|post_inference|both}}"
sensitivity_level: {{1-5}}
platform_tier: "{{consumer|enterprise|b2b_api}}"
---
```

## 1. Overview
**Purpose**: `{{what this filter intercepts and why}}`

**Filter type**: {{pre_inference (input sanitization) | post_inference (output scan) | both}}

**Platform context**: {{consumer product / enterprise API / B2B integration}} -- determines threshold strictness

**Integration point**: {{HTTP middleware / LLM output hook / webhook / SDK}}

## 2. Harm Category Configuration
Each harm category MUST reference a named taxonomy source and specify exact enforcement_action.

| Category | Source | Input Score Threshold | Output Score Threshold | Enforcement Action | Priority |
|----------|--------|-----------------------|-----------------------|-------------------|----------|
| sexual/minors | OpenAI Moderation | BLOCK always | BLOCK always | block + NCMEC report | P0 |
| hate/threatening | OpenAI Moderation | >= 0.50 | >= 0.40 | block | P1 |
| self-harm/instructions | OpenAI Moderation | BLOCK always | BLOCK always | block | P0 |
| SEVERE_TOXICITY | Perspective API | >= 0.80 | >= 0.70 | block | P1 |
| TOXICITY | Perspective API | >= 0.90 | >= 0.85 | flag | P2 |
| IDENTITY_ATTACK | Perspective API | >= 0.80 | >= 0.75 | flag | P2 |
| violence/graphic | OpenAI Moderation | >= 0.80 | >= 0.75 | block | P1 |
| sexual (adult) | OpenAI Moderation | >= 0.90 | >= 0.85 | restrict (age gate) | P2 |
| PROFANITY | Perspective API | >= 0.95 | >= 0.90 | log | P3 |

Enforcement action options: block | flag | degrade | restrict | log | escalate

## 3. Pipeline Stages

```yaml
stages:
  - name: "input_hash_check"
    type: "hash_matching"
    tool: "PhotoDNA"
    scope: "CSAM detection"
    latency_budget_ms: 2
    enforcement_action: "block + NCMEC_report"
    priority: P0

  - name: "input_ml_classify"
    type: "api_classifier"
    tool: "openai_moderation"   # or perspective_api
    endpoint: "https://api.openai.com/v1/moderations"
    latency_budget_ms: 80
    categories: [all_openai_categories]
    enforcement_action: "per_category_table_above"
    priority: P1

  - name: "output_toxicity_scan"
    type: "api_classifier"
    tool: "perspective_api"
    endpoint: "https://commentanalyzer.googleapis.com/v1alpha1/comments:analyze"
    latency_budget_ms: 100
    attributes: [TOXICITY, SEVERE_TOXICITY, IDENTITY_ATTACK, THREAT]
    enforcement_action: "per_category_table_above"
    priority: P2
```

## 4. Error Handling and Fallback
| Failure Mode | Fallback Behavior | Rationale |
|-------------|-------------------|-----------|
| Classifier API timeout (> 150ms) | FLAG + allow with degraded confidence | Prefer availability over blocking for non-critical |
| Classifier returns error 5xx | LOG + allow; alert on-call | SLA availability > safety for transient errors |
| CSAM check unavailable | BLOCK all image inputs | Safety > availability for P0 categories |
| Score NULL or NaN | Treat as score = 0.5 (uncertain); FLAG | Never silently pass uncertain inputs |

## 5. Performance SLA
| Stage | Target Latency | Max Latency | Error Rate Target |
|-------|----------------|-------------|-------------------|
| Hash matching | < 2ms | 5ms | < 0.001% |
| Input ML classify | < 80ms | 150ms | < 0.1% |
| Output toxicity scan | < 100ms | 200ms | < 0.1% |
| End-to-end pipeline | < 100ms p95 | 300ms p99 | < 0.5% |

## 6. Audit and Logging
Every enforcement decision MUST write an immutable log record:
```json
{
  "timestamp": "ISO8601",
  "request_id": "uuid",
  "stage": "input_ml_classify",
  "category": "hate/threatening",
  "score": 0.72,
  "threshold": 0.50,
  "action": "block",
  "user_id_hash": "sha256(user_id)",
  "content_hash": "sha256(content[:100])"
}
```
Retention: 90 days. PII: hash only (GDPR Art. 5(1)(c) data minimization).
