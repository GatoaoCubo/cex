---
id: p11_qg_optimizer
kind: quality_gate
pillar: P11
title: "Gate: optimizer"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: "builder_agent"
domain: optimizer
quality: 9.0
tags: [quality-gate, optimizer, P11, governance, performance, continuous-improvement]
tldr: "Gates for optimizer artifacts — metric direction, threshold ordering, and automatable action definitions."
density_score: 0.85
llm_function: GOVERN
---
# Gate: optimizer
## Definition
| Field     | Value                                             |
|-----------|---------------------------------------------------|
| metric    | threshold coherence + action automation coverage  |
| threshold | 8.0                                               |
| operator  | >=                                                |
| scope     | all optimizer artifacts (P11)                     |
## HARD Gates
All must pass. Failure on any = final score 0.
| Gate | Check | Why |
|------|-------|-----|
| H01 | YAML frontmatter parses valid YAML | Broken YAML = optimizer never triggers |
| H02 | id matches `^p11_opt_[a-z][a-z0-9_]+$` | Namespace compliance |
| H03 | id == filename stem | Brain search relies on this |
| H04 | kind == "optimizer" | Type integrity |
| H05 | quality == null | Never self-score |
| H06 | All required fields present: id, kind, pillar, version, created, updated, author, domain, quality, tags, tldr | Completeness |
| H07 | target_metric field is non-empty string naming one measurable metric | Vague targets cannot be optimized |
| H08 | direction field is one of: minimize, maximize | Direction ambiguity reverses all logic |
| H09 | thresholds block has trigger, target, and critical numeric values | Three-level control without all three is incomplete |
| H10 | actions list has >= 2 entries, each with name and automated boolean | Optimization without defined actions is documentation, not control |
## SOFT Scoring
| Gate | Check | Weight |
|------|-------|--------|
| S01 | tldr <= 160 chars, non-empty | 1.0 |
| S02 | tags is list, len >= 3, includes "optimizer" | 0.5 |
| S03 | density_score >= 0.80 | 0.5 |
| S04 | thresholds are correctly ordered: minimize → trigger < target < critical; maximize → trigger > target > critical | 1.0 |
| S05 | At least one action has automated: true with stated trigger condition | 1.0 |
| S06 | baseline block has value and conditions (measurement context documented) | 1.0 |
| S07 | cost_risk block assesses effort and failure impact | 1.0 |
| S08 | monitoring_dashboard names where metric is visible without manual query | 0.5 |
| S09 | reporting_cadence field states review frequency | 0.5 |
| S10 | rollback_plan describes how to undo a failed optimization step | 1.0 |
| S11 | target_metric is machine-readable (query, counter, or log field) not a narrative | 1.0 |
| S12 | No filler phrases ("this optimizer", "designed to improve", "various metrics") | 0.5 |
Weights sum: 9.5. Normalize: divide each by 9.5 before scoring.
## Actions
| Score | Action |
|-------|--------|
| >= 9.5 | GOLDEN — pool as reference optimization loop |
| >= 8.0 | PUBLISH — wire to monitoring and enable automated triggers |
| >= 7.0 | REVIEW — complete baseline, rollback plan, or threshold ordering |
| < 7.0  | REJECT — rework metric definition and action list |
## Bypass
| Field | Value |
|-------|-------|
| conditions | Production incident requiring immediate threshold override without full review cycle |
| approver | p11-chief |
| audit_trail | Log in records/audits/ with current metric value, override value, and timestamp |
| expiry | 24h — must revalidate thresholds and rerun gates before expiry |
| never_bypass | H01 (YAML), H05 (quality null) |
