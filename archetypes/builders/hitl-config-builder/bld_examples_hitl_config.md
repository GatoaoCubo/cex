---
kind: examples
id: bld_examples_hitl_config
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of hitl_config artifacts
pattern: few-shot learning -- LLM reads these before producing
quality: 9.2
title: "Examples Hitl Config"
version: "1.0.0"
author: n03_builder
tags: [hitl_config, builder, examples, P11]
tldr: "Golden and anti-examples for hitl_config construction: confidence-gated content review vs broken no-timeout/single-reviewer configs."
domain: "hitl_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
---

# Examples: hitl-config-builder
## Golden Example
INPUT: "Configure human review for AI-generated marketing copy before publishing"
OUTPUT:
```yaml
id: p11_hitl_marketing_copy_review
kind: hitl_config
pillar: P11
version: "1.0.0"
created: "2026-04-13"
updated: "2026-04-13"
author: "builder_agent"
workflow: "marketing_copy_generation"
review_trigger: "confidence < 0.85 OR brand_risk_score > 0.6"
escalation_chain:
  - "content_reviewer"
  - "brand_lead"
  - "legal_counsel"
approval_flow: "edit"
timeout_seconds: 7200
fallback_action: "reject"
quality: null
tags: [hitl_config, marketing, content-review, P11]
tldr: "Marketing copy HITL: review when confidence < 0.85 or brand risk > 0.6, 3-level escalation, 2h timeout"
description: "Human review gate for AI-generated marketing copy: brand safety, legal compliance, tone accuracy"
max_queue_depth: 50
notification_channel: "slack"
priority_rules:
  - "brand_risk_score > 0.8 THEN priority critical"
  - "campaign_type = launch THEN priority high"
feedback_loop: "Rejected outputs + reviewer edits written to p11_reward_marketing_copy.md for fine-tuning"
```
## Overview
AI-generated marketing copy requires human review before publication to ensure brand voice consistency,
legal compliance, and accuracy of product claims.
Human judgment is required because brand safety and legal risk cannot be reliably scored by automated
metrics alone; a human reviewer catches edge cases that confidence scores miss.
Approved output is published to CMS; rejected output returns to generation pipeline with reviewer notes.
## Review Trigger
Review fires when model confidence is below threshold OR brand risk score is elevated.
| Trigger | Condition | Data Source | Notes |
|---------|-----------|-------------|-------|
| Low confidence | confidence < 0.85 | model output metadata | Covers uncertain generations |
| Brand risk | brand_risk_score > 0.6 | brand safety classifier | Covers borderline brand claims |
## Escalation Chain
| Level | Role | SLA (min) | Channel | Escalates When |
|-------|------|-----------|---------|---------------|
| L1 | content_reviewer | 60 | Slack #review-queue | No response in 60 min |
| L2 | brand_lead | 60 | Slack DM + email | No response from L1 in 60 min |
| L3 | legal_counsel | 60 | Email urgent | brand_risk_score > 0.8 OR no L2 response |
## Approval Flow
Flow type: **edit** -- reviewers may modify the copy, not just accept/reject.
| Action | Meaning | Downstream Effect |
|--------|---------|-------------------|
| approve | Copy is brand-safe and accurate | Released to CMS publish queue |
| edit + approve | Reviewer corrected copy | Edited version released; diff logged for training |
| reject | Copy fails brand/legal standard | Returned to generation with rejection reason |
## Timeout and Fallback
Timeout: **7200s** (2 hours, applies to each escalation level).
Fallback: **reject** -- unreviewed marketing copy is never auto-published; safety over availability.

WHY THIS IS GOLDEN:
- quality: null (H01 pass)
- id matches p11_hitl_ pattern (H02 pass)
- kind: hitl_config (H03 pass)
- escalation_chain has 3 roles: L1, L2, L3 (H05 pass)
- approval_flow is "edit" (valid enum) (H06 pass)
- timeout_seconds: 7200 > 0 (H07 pass)
- fallback_action: "reject" (valid enum) (H08 pass)
- review_trigger is a precise evaluable expression (H09 pass)
- 5 body sections present (H10 pass)
- feedback_loop defined (S11 pass)
- priority_rules defined for high-risk routing (S08 pass)
- tags: 4 items, includes "hitl_config" (S03 pass)
- tldr: 77 chars <= 160 (S01 pass)

## Anti-Example
INPUT: "Add human review to the AI system"
BAD OUTPUT:
```yaml
id: hitl-review
kind: human_review
pillar: feedback
workflow: general
review_trigger: "when the AI is unsure"
escalation_chain: [admin]
approval_flow: yes_no
timeout_seconds: 0
fallback_action: accept
quality: 8.5
tags: [review]
```
Just have a human review the output when needed.

FAILURES:
1. id: "hitl-review" uses hyphens and no p11_hitl_ prefix -> H02 FAIL
2. kind: "human_review" not "hitl_config" -> H03 FAIL
3. pillar: "feedback" not "P11" -> H04 FAIL
4. quality: 8.5 (not null) -> H01 FAIL
5. escalation_chain has 1 role only (single point of failure) -> H05 FAIL
6. approval_flow: "yes_no" not a valid enum (binary/edit/score) -> H06 FAIL
7. timeout_seconds: 0 (pipeline can block forever) -> H07 FAIL
8. fallback_action: "accept" (silent accept of unreviewed output is safety failure) -> H08 FAIL
9. review_trigger: "when the AI is unsure" is vague, not evaluable -> H09 FAIL
10. Body missing all 5 required sections -> H10 FAIL
11. tags: 1 item, missing "hitl_config" -> S03 FAIL
12. No SLA defined for any escalation level -> S06 FAIL
