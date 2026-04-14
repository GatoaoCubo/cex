---
id: p11_qg_action_prompt
kind: quality_gate
pillar: P11
title: "Gate: action_prompt"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: "builder_agent"
domain: action_prompt
quality: 9.0
tags: [quality-gate, action-prompt, P11, P03, governance, task-execution]
tldr: "Gates for action_prompt artifacts — task-focused prompts with defined input/output contracts."
density_score: 0.87
llm_function: GOVERN
---
# Gate: action_prompt
## Definition
| Field     | Value                                        |
|-----------|----------------------------------------------|
| metric    | input/output contract clarity + edge coverage |
| threshold | 8.0                                          |
| operator  | >=                                           |
| scope     | all action_prompt artifacts (P03)            |
## HARD Gates
All must pass. Failure on any = final score 0.
| Gate | Check | Why |
|------|-------|-----|
| H01 | YAML frontmatter parses valid YAML | Broken YAML = broken prompt at runtime |
| H02 | id matches `^p03_ap_[a-z][a-z0-9_]+$` | Namespace compliance |
| H03 | id == filename stem | Brain search relies on this |
| H04 | kind == "action_prompt" | Type integrity |
| H05 | quality == null | Never self-score |
| H06 | All 21 required fields present | Completeness |
| H07 | edge_cases has >= 2 entries | Robustness requirement |
| H08 | body has all 5 required sections: Action, Input, Output, Validation, Edge Cases | Structure compliance |
## SOFT Scoring
| Gate | Check | Weight |
|------|-------|--------|
| S01 | tldr <= 160 chars, non-empty | 1.0 |
| S02 | tags is list, len >= 3, includes "action_prompt" | 0.5 |
| S03 | action field is a verb phrase (starts with verb) | 1.0 |
| S04 | input_required lists specific data items with types | 1.0 |
| S05 | output_expected describes verifiable structure | 1.0 |
| S06 | purpose explains WHY, not just WHAT | 0.5 |
| S07 | No identity or persona content (not system_prompt territory) | 1.0 |
| S08 | No step-by-step recipe with prerequisites (not instruction territory) | 1.0 |
| S09 | Validation section has verifiable, concrete criteria | 0.5 |
| S10 | Input section uses table or structured format | 0.5 |
| S11 | density_score >= 0.80 | 0.5 |
| S12 | No filler phrases ("this document", "in summary", "please note") | 1.0 |
Weights sum: 9.5. Normalize: divide each by 9.5 before scoring.
## Actions
| Score | Action |
|-------|--------|
| >= 9.5 | GOLDEN — pool as reference action_prompt |
| >= 8.0 | PUBLISH — ready for runtime injection |
| >= 7.0 | REVIEW — tighten I/O contract or add edge cases |
| < 7.0  | REJECT — rework action definition and output spec |
## Bypass
| Field | Value |
|-------|-------|
| conditions | Urgent task requiring runtime prompt before full validation cycle |
| approver | p03-chief |
| audit_trail | Log in records/audits/ with bypass reason and timestamp |
| expiry | 48h — must pass all gates before expiry |
| never_bypass | H01 (YAML), H05 (quality null) |
