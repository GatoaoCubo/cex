---
id: p11_qg_hitl_config
kind: quality_gate
pillar: P11
title: "Gate: hitl_config"
version: "1.0.0"
created: "2026-04-13"
updated: "2026-04-13"
author: "builder_agent"
domain: "hitl_config -- human-in-the-loop approval flow configuration with review triggers, escalation chains, and timeout/fallback behavior"
quality: 9.0
tags: [quality-gate, hitl-config, human-review, escalation, approval, P11]
tldr: "Gates for hitl_config: validates review trigger precision, escalation chain completeness, approval flow validity, timeout > 0, and safe fallback."
density_score: 0.92
llm_function: GOVERN
---
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
