---
kind: schema
id: bld_schema_bugloop
pillar: P11
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for bugloop
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.1
title: "Schema Bugloop"
version: "1.0.0"
author: n03_builder
tags: [bugloop, builder, examples]
tldr: "Golden and anti-examples for bugloop construction, demonstrating ideal structure and common pitfalls."
domain: "bugloop construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---
# Schema: bugloop
## Frontmatter Fields
| Field | Type | Required | Default |
|-------|------|----------|---------|
| id | string (p11_bl_{slug}) | YES | — |
| kind | literal "bugloop" | YES | — |
| pillar | literal "P11" | YES | — |
| version | semver string | YES | "1.0.0" |
| created | date YYYY-MM-DD | YES | — |
| updated | date YYYY-MM-DD | YES | — |
| author | string | YES | — |
| domain | string (system/module monitored) | YES | — |
| quality | null | YES | null |
| tags | list[string], len >= 3, includes "bugloop" | YES | — |
| tldr | string < 160ch | YES | — |
| scope | string — what the bugloop monitors | YES | — |
| detect | object | YES | — |
| detect.method | string (static_analysis/runtime_trace/test_failure/log_scan) | YES | — |
| detect.trigger | string (on_commit/on_deploy/scheduled/continuous) | YES | — |
| detect.pattern | string (regex or description of failure signature) | YES | — |
| fix | object | YES | — |
| fix.strategy | string (patch_and_retry/rollback_first/isolate_then_fix) | YES | — |
| fix.auto_fix | boolean | YES | — |
| fix.max_attempts | integer >= 1, <= 10 | YES | — |
| verify | object | YES | — |
| verify.test_suite | string (path or name of suite) | YES | — |
| verify.assertions | list[string] >= 1 | YES | — |
| verify.timeout | integer seconds > 0 | YES | — |
| cycle_count | integer max iterations before escalation | YES | — |
| auto_fix | boolean — fully automatic with no human step | YES | — |
| escalation | object | YES | — |
| escalation.threshold | integer — cycle number that triggers escalation | YES | — |
| escalation.target | string — who/what receives escalation | YES | — |
| confidence | float 0.0-1.0 — confidence in auto-fix correctness | YES | — |
| test_suite | string — canonical path/name of test suite | YES | — |
| rollback | object | YES | — |
| rollback.enabled | boolean | YES | — |
| rollback.strategy | string (git_revert/snapshot_restore/blue_green) | YES | — |
## Body Structure (required sections)
1. Detection — triggers, patterns, sources of bug signal
2. Fix Strategy — auto vs manual, strategy rationale
3. Verification — test suite, assertions, pass criteria
4. Escalation — when/how to escalate, thresholds
5. Rollback — conditions that trigger rollback, strategy
## Constraints
- max_bytes: 4096 (body only)
- naming: p11_bl_{scope}.md
- id == filename stem
- cycle_count MUST be numeric
- confidence MUST be 0.0-1.0 float
- fix.max_attempts <= cycle_count
- quality: null always
- auto_fix top-level MUST match fix.auto_fix
