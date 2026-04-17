---
id: p11_qg_instruction
kind: quality_gate
pillar: P11
title: "Gate: Instruction"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: "builder_agent"
domain: "instruction — step-by-step operational recipes for agent task execution"
quality: 9.0
tags: [quality-gate, instruction, steps, recipe, procedure, idempotency]
tldr: "Gates ensuring instruction artifacts decompose tasks into atomic verifiable steps with prerequisites, completion criteria, and rollback procedures."
density_score: 0.90
llm_function: GOVERN
---
# Gate: Instruction
## Definition
| Field     | Value |
|-----------|-------|
| metric    | weighted soft score + all hard gates pass |
| threshold | 7.0 to publish; 8.0 for pool; 9.5 for golden |
| operator  | AND (all hard) + weighted average (soft) |
| scope     | any artifact with `kind: instruction` |
## HARD Gates
All must pass. Any failure = immediate reject.
| ID  | Check | Fail Condition |
|-----|-------|----------------|
| H01 | Frontmatter parses as valid YAML | Parse error on any field |
| H02 | ID matches `^[a-z][a-z0-9_-]+$` | Uppercase, spaces, or leading digit |
| H03 | ID equals filename stem | `id: deploy_service` in file `restart_service.md` |
| H04 | Kind equals literal `instruction` | Any other kind value |
| H05 | Quality field is `null` | Any non-null value |
| H06 | All required fields present | Missing: steps, prerequisites, or completion_criteria |
| H07 | Steps are numbered and count >= 2 | Single undivided step or unnumbered list |
| H08 | `idempotent` field is a boolean | Missing field or non-boolean value |
## SOFT Scoring
Total weights sum to 100%.
| ID  | Dimension | Weight | 10 pts | 5 pts | 0 pts |
|-----|-----------|--------|--------|-------|-------|
| S01 | Step atomicity | 1.0 | Every step performs exactly one action and is independently verifiable | Most steps atomic; some compound | Steps are multi-action paragraphs |
| S02 | Prerequisites completeness | 1.0 | All tools, permissions, files, and env vars listed | Some prerequisites listed | No prerequisites section |
| S03 | Completion criteria | 1.0 | Each step has explicit success signal (exit code, file exists, output pattern) | Overall completion defined but not per-step | No success criteria |
| S04 | Rollback procedures | 1.0 | Undo steps defined for each destructive action | Partial rollback notes present | No rollback |
| S05 | Idempotency declaration | 0.5 | `idempotent: true/false` with explanation of why | Field present, no rationale | Field absent |
| S06 | Dependency ordering | 1.0 | Steps reference their predecessors explicitly when order matters | Steps ordered but dependencies implicit | Unordered; any sequence implied |
| S07 | Atomicity classification | 0.5 | `atomic` field classifies instruction as atomic or composable | Classification present but unexplained | Field missing |
| S08 | Error handling per step | 1.0 | Each step lists what to do on failure | Some steps have error notes | No error handling |
| S09 | Tool list | 0.5 | `tools_required` lists every CLI, SDK, or API the steps invoke | Partial tool list | No tool list |
| S10 | Distinction from action_prompt | 0.5 | No I/O prompt framing — pure procedural steps | Minimal prompt framing leakage | Reads as a prompt, not a recipe |
| S11 | Example run | 0.5 | At least one example showing input values substituted into steps | Example mentioned but sparse | No example |
**Score = sum(pts * weight) / sum(max_pts * weight) * 10**
## Actions
| Score | Tier | Action |
|-------|------|--------|
| >= 9.5 | Golden | Publish to pool as golden operational runbook |
| >= 8.0 | Skilled | Publish to pool + log pattern |
| >= 7.0 | Learning | Use but flag for improvement |
| < 7.0 | Rejected | Return to author with gate report |
## Bypass
| Field | Value |
|-------|-------|
| Conditions | Novel procedure being executed for the first time; rollback path not yet known |
| Approver | Task owner + one peer reviewer |
| Audit trail | `bypass_reason` required; note which gates are bypassed and why |
