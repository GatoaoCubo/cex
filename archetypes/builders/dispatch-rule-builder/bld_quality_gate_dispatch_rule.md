---
id: p11_qg_dispatch_rule
kind: quality_gate
pillar: P11
title: "Gate: dispatch_rule"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: "builder_agent"
domain: "dispatch_rule — routing rules mapping keywords to agent_groups with fallback logic"
quality: 9.0
tags: [quality-gate, dispatch-rule, routing, keyword-mapping, P11]
tldr: "Gates for dispatch_rule artifacts: validates keyword coverage, agent_group enum, fallback logic, bilingual support, and confidence thresholds."
density_score: 0.92
llm_function: GOVERN
---
# Gate: dispatch_rule
## Definition
| Field     | Value |
|-----------|-------|
| metric    | Composite score from SOFT dimensions + all HARD gates pass |
| threshold | >= 7.0 to publish; >= 9.5 golden |
| operator  | AND (all HARD) + weighted_sum (SOFT) |
| scope     | All artifacts where `kind: dispatch_rule` |
## HARD Gates
All must pass. Any single failure = REJECT regardless of SOFT score.
| ID  | Check | Failure message |
|-----|-------|----------------|
| H01 | Frontmatter parses as valid YAML | "Frontmatter YAML syntax error" |
| H02 | `id` matches `^p12_dr_[a-z][a-z0-9_]+$` | "ID fails dispatch_rule namespace regex" |
| H03 | `id` value equals filename stem | "ID does not match filename" |
| H04 | `kind` equals literal `"dispatch_rule"` | "Kind is not 'dispatch_rule'" |
| H05 | `quality` field is `null` | "Quality must be null at authoring time" |
| H06 | All required fields present: id, kind, pillar, domain, agent_group, model, priority, keywords, confidence_threshold, fallback, version, created, author, tags | "Missing required field(s)" |
| H07 | `agent_group` value is one of the defined agent_group enum (researcher, marketer, builder, knowledge-engine, executor, monetizer) | "Agent_group not in allowed enum" |
| H08 | `keywords` list is non-empty (>= 3 entries) | "Keyword list must have at least 3 entries" |
| H09 | `confidence_threshold` is a float between 0.0 and 1.0 | "Confidence threshold out of range [0.0, 1.0]" |
| H10 | `fallback` is defined and references a valid agent_group or literal `human` | "Fallback target undefined or invalid" |
## SOFT Scoring
Dimensions sum to 100%. Score each 0.0-10.0; multiply by weight.
| Dimension | Weight | What to assess |
|-----------|--------|----------------|
| Keyword breadth | 1.0 | Keywords cover the full semantic space of the domain scope |
| Bilingual coverage | 1.0 | Both PT and EN keywords present in keyword list |
| Priority rationale | 0.5 | Priority level (high/medium/low) explained or evident from domain |
| Confidence threshold calibration | 1.0 | Threshold value apownte for domain (not too strict/loose) |
| Fallback chain quality | 1.0 | Fallback agent_group is a logical second-choice for the domain |
| Scope fence clarity | 1.0 | What the rule does NOT route is explicitly stated |
| Model selection rationale | 0.5 | Model choice (sonnet/opus) justified by task complexity |
| Keyword specificity | 1.0 | No overly generic keywords that would cause routing collisions |
| Trigger phrase examples | 1.0 | 2+ example trigger sentences that would activate this rule |
| Boundary vs other rules | 0.5 | Non-overlap with adjacent dispatch rules documented |
| Domain precision | 1.0 | Domain field accurately describes the routing scope |
| Documentation | 0.5 | tldr captures routing intent in <= 160 characters |
Weight sum: 1.0+1.0+0.5+1.0+1.0+1.0+0.5+1.0+1.0+0.5+1.0+0.5 = 10.0 (100%)
## Actions
| Score | Tier | Action |
|-------|------|--------|
| >= 9.5 | GOLDEN | Publish to pool as golden exemplar |
| >= 8.0 | PUBLISH | Publish to pool |
| >= 7.0 | REVIEW | Flag for human review before publish |
| < 7.0  | REJECT | Return to author with failure report |
## Bypass
| Field | Value |
|-------|-------|
| conditions | New agent_group being piloted without full keyword corpus established |
| approver | Routing system owner approval required (written) |
| audit_trail | Bypass logged to `records/audits/dispatch_rule_bypass_{date}.md` |
| expiry | 24h; routing rules in active use must be validated quickly |
