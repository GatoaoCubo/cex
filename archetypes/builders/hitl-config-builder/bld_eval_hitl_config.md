---
kind: quality_gate
id: p11_qg_hitl_config
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of hitl_config artifacts
pattern: few-shot learning -- LLM reads these before producing
quality: 9.0
title: "Gate: hitl_config"
version: "1.0.0"
author: "builder_agent"
tags: [quality-gate, hitl-config, human-review, escalation, approval, P11]
tldr: "Gates for hitl_config: validates review trigger precision, escalation chain completeness, approval flow validity, timeout > 0, and safe fallback."
domain: "hitl_config -- human-in-the-loop approval flow configuration with review triggers, escalation chains, and timeout/fallback behavior"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.92
related:
  - bld_examples_hitl_config
  - bld_output_template_hitl_config
  - bld_instruction_hitl_config
  - bld_schema_hitl_config
  - hitl-config-builder
  - p03_sp_hitl_config_builder
  - p01_kc_hitl_config
  - bld_architecture_hitl_config
  - bld_knowledge_card_hitl_config
  - p11_qg_dispatch_rule
---

## Quality Gate

# Gate: hitl_config
## Definition
| Field | Value |
|-------|-------|
| metric | Composite score from SOFT dimensions + all HARD gates pass |
| threshold | >= 7.0 to publish; >= 9.5 golden |
| operator | AND (all HARD) + weighted_sum (SOFT) |
| scope | All artifacts where `kind: hitl_config` |
## HARD Gates
All must pass. Any single failure = REJECT regardless of SOFT score.
| ID | Check | Failure message |
|----|-------|----------------|
| H01 | `quality` field is `null` | "Quality must be null at authoring time" |
| H02 | `id` matches `^p11_hitl_[a-z][a-z0-9_]+$` | "ID fails hitl_config namespace regex" |
| H03 | `kind` equals literal `"hitl_config"` | "Kind is not 'hitl_config'" |
| H04 | `pillar` equals literal `"P11"` | "Pillar is not 'P11'" |
| H05 | `escalation_chain` list has >= 2 entries | "Escalation chain must have minimum 2 reviewers (single point of failure)" |
| H06 | `approval_flow` is one of: binary, edit, score | "approval_flow must be binary, edit, or score" |
| H07 | `timeout_seconds` is integer > 0 | "timeout_seconds must be > 0 (zero or missing = pipeline blocks forever)" |
| H08 | `fallback_action` is one of: reject, accept_with_flag, retry | "fallback_action must be reject, accept_with_flag, or retry (bare accept is a safety failure)" |
| H09 | `review_trigger` is present and is a non-empty string that is NOT generic prose | "review_trigger must be a precise evaluable condition, not vague prose" |
| H10 | Body contains all 5 required sections: Overview, Review Trigger, Escalation Chain, Approval Flow, Timeout and Fallback | "Missing required body section(s)" |
## SOFT Scoring
Dimensions sum to 100%. Score each 0.0-10.0; multiply by weight.
| Dimension | Weight | What to assess |
|-----------|--------|----------------|
| Trigger precision | 1.5 | Condition is numeric threshold or enum match, not vague prose |
| Escalation chain completeness | 1.5 | Each level has role, SLA, and channel defined |
| Approval flow clarity | 1.0 | Each reviewer action is defined with downstream effect |
| Timeout sizing | 1.0 | timeout_seconds is realistic for the workflow SLA (not 0, not 999999) |
| Fallback safety | 1.0 | fallback_action is appropriate for the risk level of the workflow |
| Priority routing | 0.5 | High-risk outputs have priority_rules to fast-track to senior reviewers |
| Notification channel | 0.5 | Reviewers are actively alerted (not relying on polling) |
| Feedback loop | 1.0 | Review decisions feed back to model training or quality tracking |
| Boundary clarity | 0.5 | Explicitly not guardrail (auto-block), not quality_gate (auto-score) |
| Queue management | 0.5 | max_queue_depth set to prevent unbounded backlog |
| Required vs. conditional routing | 0.5 | Distinguishes mandatory review (domain) from conditional review (confidence) |
| Documentation | 0.5 | tldr names the workflow and key trigger condition |
Weight sum: 1.5+1.5+1.0+1.0+1.0+0.5+0.5+1.0+0.5+0.5+0.5+0.5 = 10.0 (100%)
## Actions
| Score | Tier | Action |
|-------|------|--------|
| >= 9.5 | GOLDEN | Publish to pool as golden exemplar |
| >= 8.0 | PUBLISH | Publish to pool |
| >= 7.0 | REVIEW | Flag for human review before publish |
| < 7.0 | REJECT | Return to author with failure report |
## Bypass
| Field | Value |
|-------|-------|
| conditions | Prototype or exploratory workflow where escalation chain is not yet finalized |
| approver | Workflow owner approval required (written); timeout and fallback never bypassed |

## Examples

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

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
