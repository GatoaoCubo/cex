---
id: p11_qg_runtime_state
kind: quality_gate
pillar: P11
title: "Gate: Runtime State"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: builder
domain: runtime_state
quality: 9.0
density_score: 0.85
tags:
  - quality-gate
  - runtime-state
  - p11
  - agent-state
  - routing
tldr: "Quality gate for agent runtime mental state: verifies routing rules, state transitions, persistence scope, and conflict resolution."
llm_function: GOVERN
---
## Definition
A runtime state artifact captures the live decision-making configuration of an agent: its routing rules (with conditions and confidence), state transitions (with trigger events), priority ordering, and heuristics. It applies only during execution — it contains no design-time content such as capability descriptions or architectural diagrams. Persistence scope declares whether state survives across sessions or resets each time.
Scope: files with `kind: runtime_state`. Does not apply to mental models (design-time identity), system prompts (static instructions), or session state (ephemeral task context).
## HARD Gates
Failure on any single gate means REJECT regardless of soft score.
| ID  | Predicate | How to test |
|-----|-----------|-------------|
| H01 | Frontmatter parses as valid YAML | `yaml.safe_load(frontmatter)` raises no error |
| H02 | `id` matches namespace `p10_rs_*` | `id.startswith("p10_rs_")` is true |
| H03 | `id` equals filename stem | `Path(file).stem == id` |
| H04 | `kind` equals literal `runtime_state` | string equality check |
| H05 | `quality` is null at authoring time | `quality is None` |
| H06 | All required frontmatter fields present and non-empty | id, kind, pillar, title, version, created, updated, author, domain, tags, tldr, agent, persistence all present |
| H07 | Routing rules section present with >= 2 rules each having a condition | count routing rule entries >= 2; each has a condition field |
| H08 | State transitions section present with >= 1 named transition and a trigger event | count transitions >= 1; each has trigger field non-empty |
| H09 | `persistence` field is one of: within-session, cross-session | enum membership check |
## SOFT Scoring
Score each dimension 0 (absent or fails) to 1 (present and passes). Weights are 0.5 or 1.0.
| #  | Dimension | Weight |
|----|-----------|--------|
| 1  | `density_score` field present and >= 0.80 | 1.0 |
| 2  | Every routing rule has an explicit condition (not a vague keyword) | 1.0 |
| 3  | Every state transition has a named trigger event (not just a description) | 1.0 |
| 4  | Priority ordering present with rationale for each rank | 1.0 |
| 5  | Heuristics section present with at least 2 rules of thumb and their confidence levels | 1.0 |
| 6  | Domain map present with explicit boundary (what this agent handles vs. what it defers) | 1.0 |
| 7  | Tags list includes `runtime-state` | 0.5 |
| 8  | Update conditions explicit (what triggers a state change, not just that state can change) | 1.0 |
| 9  | Conflict resolution described for cases where two routing rules could both fire | 1.0 |
| 10 | No design-time content present (no capability lists, architecture notes, or setup instructions) | 1.0 |
| 11 | `tldr` is <= 160 characters | 0.5 |
**Formula**: `final_score = (sum of score_i * weight_i) / (sum of weight_i) * 10`
Weight total: 10.0. Each dimension contributes proportionally. Score range: 0.0 to 10.0.
## Actions
| Tier | Threshold | Action |
|------|-----------|--------|
| GOLDEN | >= 9.5 | Publish to pool as golden; use as reference for agent state design |
| PUBLISH | >= 8.0 | Publish to pool; mark production-ready |
| REVIEW | >= 7.0 | Return to author with scored dimension feedback; one revision cycle allowed |
| REJECT | < 7.0 | Block from pool; full rewrite required before re-evaluation |
## Bypass
| Field | Value |
|-------|-------|
| condition | Agent is in early bootstrapping and fewer than 2 routing rules have been observed in forctice |
| approver | Domain lead must approve in writing before bypass takes effect |
