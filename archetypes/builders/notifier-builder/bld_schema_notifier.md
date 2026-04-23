---
kind: schema
id: bld_schema_notifier
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for notifier
pattern: TEMPLATE derives from this. CONFIG restricts this.
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: builder_agent
tags: [schema, notifier, P04, P06]
quality: 9.1
title: "Schema Notifier"
tldr: "Golden and anti-examples for notifier construction, demonstrating ideal structure and common pitfalls."
domain: "notifier construction"
density_score: 0.90
related:
  - bld_schema_retriever_config
  - bld_schema_output_validator
  - bld_schema_handoff_protocol
  - bld_schema_constraint_spec
  - bld_schema_memory_scope
  - bld_schema_golden_test
  - bld_schema_chunk_strategy
  - bld_schema_smoke_eval
  - bld_schema_prompt_version
  - bld_schema_unit_eval
---
# Schema: notifier

## Frontmatter Fields
| Field             | Type                                          | Required | Default      | Notes                          |
|-------------------|-----------------------------------------------|----------|--------------|--------------------------------|
| id                | string (p04_notify_{channel_slug})            | YES      | -            | Namespace compliance           |
| kind              | literal "notifier"                            | YES      | -            | Type integrity                 |
| pillar            | literal "P04"                                 | YES      | -            | Pillar assignment              |
| version           | semver string                                 | YES      | "1.0.0"      | Artifact versioning            |
| created           | date YYYY-MM-DD                               | YES      | -            | Creation date                  |
| updated           | date YYYY-MM-DD                               | YES      | -            | Last update                    |
| author            | string                                        | YES      | -            | Producer identity              |
| name              | string                                        | YES      | -            | Human-readable notifier name   |
| channel           | enum: email, sms, slack, discord, push, in_app, teams | YES | -       | Delivery channel               |
| template          | string                                        | YES      | -            | Message template name/pattern  |
| priority          | enum: critical, high, normal, low             | YES      | normal       | Default priority level         |
| provider          | string                                        | REC      | -            | SendGrid, Twilio, Firebase, etc|
| rate_limit        | object {max_per_minute, max_per_hour}         | REC      | -            | Throttling config              |
| retry_policy      | object {max_attempts, backoff}                | REC      | -            | Retry on failure               |
| template_vars     | list[string]                                  | REC      | -            | Variables used in template     |
| delivery_guarantee| enum: at_least_once, best_effort              | REC      | best_effort  | Delivery semantics             |
| quality           | null                                          | YES      | null         | Never self-score               |
| tags              | list[string], len >= 3                        | YES      | -            | Must include "notifier"        |
| tldr              | string <= 160ch                               | YES      | -            | Dense summary                  |
| description       | string <= 200ch                               | REC      | -            | What the notifier does         |

## ID Pattern
Regex: `^p04_notify_[a-z][a-z0-9_]+$`

## Body Structure
1. `## Overview` — channel, provider, use case
2. `## Template` — message format, variables, examples per priority
3. `## Delivery` — rate limits, retry, guarantees, failure handling
4. `## Configuration` — provider credentials, channel-specific settings

## Constraints
- max_bytes: 1024 (body only)
- naming: p04_notify_{channel_slug}.md + .yaml
- machine_format: yaml
- id == filename stem
- quality: null always
- NO implementation code

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_retriever_config]] | sibling | 0.66 |
| [[bld_schema_output_validator]] | sibling | 0.66 |
| [[bld_schema_handoff_protocol]] | sibling | 0.65 |
| [[bld_schema_constraint_spec]] | sibling | 0.65 |
| [[bld_schema_memory_scope]] | sibling | 0.65 |
| [[bld_schema_golden_test]] | sibling | 0.63 |
| [[bld_schema_chunk_strategy]] | sibling | 0.63 |
| [[bld_schema_smoke_eval]] | sibling | 0.63 |
| [[bld_schema_prompt_version]] | sibling | 0.62 |
| [[bld_schema_unit_eval]] | sibling | 0.62 |
