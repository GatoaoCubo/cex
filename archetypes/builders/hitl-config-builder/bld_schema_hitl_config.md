---
kind: schema
id: bld_schema_hitl_config
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for hitl_config
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.1
title: "Schema Hitl Config"
version: "1.0.0"
author: n03_builder
tags: [hitl_config, builder, schema, P11]
tldr: "Formal field definitions for hitl_config artifacts: review triggers, escalation chains, approval flows, timeout, fallback."
domain: "hitl_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
---

# Schema: hitl_config
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p11_hitl_{name}) | YES | - | Namespace compliance |
| kind | literal "hitl_config" | YES | - | Type integrity |
| pillar | literal "P11" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Artifact versioning |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| workflow | string | YES | - | Name of the workflow or scope this gate applies to |
| review_trigger | string | YES | - | Condition that routes output to human (e.g., "confidence < 0.8") |
| escalation_chain | list[string] | YES | - | Ordered reviewer roles: [L1_reviewer, L2_reviewer] |
| approval_flow | enum: binary/edit/score | YES | binary | How reviewers respond |
| timeout_seconds | integer | YES | 3600 | Seconds before fallback fires |
| fallback_action | enum: reject/accept_with_flag/retry | YES | reject | Action when timeout expires |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "hitl_config" |
| tldr | string <= 160ch | YES | - | Dense summary |
| description | string <= 200ch | REC | - | What workflow this gate covers |
| max_queue_depth | integer | REC | 100 | Max pending reviews before backlog alert |
| notification_channel | string | REC | email | How reviewers are alerted (email/slack/webhook) |
| priority_rules | list[string] | OPT | [] | Conditions that promote review priority |
| feedback_loop | string | OPT | - | How review decisions feed back to model training |
## ID Pattern
Regex: `^p11_hitl_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Overview` -- what workflow, why human review is needed, who is affected
2. `## Review Trigger` -- exact condition(s) that activate the HITL gate
3. `## Escalation Chain` -- table: level, role, SLA, contact channel
4. `## Approval Flow` -- how reviewers respond and what each action means
5. `## Timeout and Fallback` -- what happens when no reviewer responds in time
## Constraints
- max_bytes: 3072 (body only)
- naming: p11_hitl_{name}.yaml
- machine_format: yaml (compiled artifact)
- id == filename stem
- escalation_chain list MUST match roles in ## Escalation Chain table
- quality: null always
- approval_flow MUST be one of: binary, edit, score
- fallback_action MUST be one of: reject, accept_with_flag, retry
