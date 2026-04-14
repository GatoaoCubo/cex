---
id: p11_qg_director
kind: quality_gate
pillar: P11
title: "Gate: supervisor"
version: "1.0.0"
created: "2026-04-06"
updated: "2026-04-06"
author: "builder_agent"
domain: supervisor
quality: 9.0
tags: [quality-gate, supervisor, P11, P08, governance, orchestration, dispatch]
tldr: "Gates for supervisor artifacts — wave topology + dispatch config + signal protocol ready for multi-builder coordination."
density_score: 0.90
llm_function: GOVERN
---
# Gate: supervisor
## Definition
| Field     | Value                                               |
|-----------|-----------------------------------------------------|
| metric    | orchestration completeness + dispatch navigability  |
| threshold | 8.0                                                 |
| operator  | >=                                                  |
| scope     | all supervisor artifacts (P08)                        |
## HARD Gates
All must pass. Failure on any = final score 0.
| Gate | Check | Why |
|------|-------|-----|
| H01 | YAML frontmatter parses valid YAML | Broken YAML = broken dispatch |
| H02 | id matches `^ex_director_[a-z][a-z0-9_]+$` | Namespace compliance |
| H03 | id == filename stem | Mission runner relies on this |
| H04 | kind == "supervisor" | Type integrity |
| H05 | quality == null | Never self-score |
| H06 | All required fields present: id, kind, pillar, title, version, topic, builders, dispatch_mode, signal_check, quality, tags, tldr | Completeness |
| H07 | llm_function == "ORCHESTRATE" | Supervisor orchestrates, never executes |
| H08 | builders list has >= 2 entries | Single-builder supervisor is pointless — use direct spawn |
## SOFT Scoring
| Gate | Check | Weight |
|------|-------|--------|
| S01 | tldr <= 160 chars, non-empty, not filler | 1.0 |
| S02 | tags is list, len >= 3, includes "supervisor" | 0.5 |
| S03 | wave_topology defined with >= 1 wave | 1.0 |
| S04 | fallback_per_builder covers every builder in list | 1.0 |
| S05 | dispatch_mode is explicit (not defaulted) | 0.5 |
| S06 | signal_check is explicit boolean (not inferred) | 0.5 |
| S07 | body has ## Wave Topology with wave sequence documented | 1.0 |
| S08 | body has ## Routing with explicit NOT-when exclusions | 0.5 |
| S09 | density_score >= 0.85 | 0.5 |
| S10 | No task execution logic in body (purity check) | 1.0 |
Weights sum: 7.5. Normalize: divide each by 7.5 before scoring.
## Actions
| Score | Action |
|-------|--------|
| >= 9.5 | GOLDEN — pool as reference supervisor definition |
| >= 8.0 | PUBLISH — register in dispatch system, deploy supervisor |
| >= 7.0 | REVIEW — complete wave topology or sharpen builder list |
| < 7.0  | REJECT — rework orchestration plan and dispatch config |
## Bypass
| Field | Value |
|-------|-------|
| conditions | Critical mission requiring immediate multi-builder dispatch |
| approver | p08-chief |
| audit_trail | Log in records/audits/ with justification and timestamp |
| expiry | 72h — full gate pass required before expiry |
| never_bypass | H01 (YAML), H05 (quality null) |
