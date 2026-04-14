---
id: p11_qg_computer_use
kind: quality_gate
pillar: P11
title: "Gate: computer_use"
version: "1.0.0"
created: "2026-03-28"
updated: "2026-03-28"
author: "builder_agent"
domain: "GUI control interfaces enabling LLMs to interact with graphical environments via screenshots and coordinate-based actions"
quality: 9.0
tags: [quality-gate, computer-use, P04, gui, screen-control, automation]
tldr: "Pass/fail gate for computer_use artifacts: action listing, resolution format, coordinate system, safety constraints, and screenshot policy."
density_score: 0.90
llm_function: GOVERN
---
# Gate: computer_use

This ISO governs computer use: screen capture, mouse, and keyboard actions taken on behalf of the agent.
## Definition
| Field | Value |
|---|---|
| metric | computer_use artifact quality score |
| threshold | 7.0 (publish >= 8.0, golden >= 9.5) |
| operator | weighted_sum |
| scope | all artifacts with `kind: computer_use` |
## HARD Gates
All must pass (AND logic). Any single failure = REJECT.
| ID | Check | Fail Condition |
|---|---|---|
| H01 | Frontmatter parses as valid YAML | Parse error on frontmatter block |
| H02 | ID matches `^p04_cu_[a-z][a-z0-9_]+$` | ID contains uppercase, hyphens, or no p04_cu_ prefix |
| H03 | ID equals filename stem | ID does not match filename |
| H04 | Kind equals literal `computer_use` | `kind: tool` or `kind: gui` or any other value |
| H05 | Quality field is null | `quality: 9.0` or any non-null value |
| H06 | All required fields present | Missing `target`, `resolution`, or `actions_supported` |
| H07 | Resolution is WxH format | `resolution: "high"` or missing dimensions |
| H08 | Actions supported list is non-empty | `actions_supported: []` or field absent |
| H09 | Target is valid enum | `target: screen` or unrecognized value |
| H10 | Body has required sections | Missing Overview, Actions, Coordinate System, or Safety |
## SOFT Scoring
Weights sum to 100%.
| Dimension | Weight | Criteria |
|---|---|---|
| Action documentation | 1.5 | Each action has parameters with types documented |
| Coordinate system clarity | 1.0 | Origin, direction, units, and resolution explicitly stated |
| Safety constraints | 1.0 | No-credential policy, sandbox requirement documented |
| Screenshot policy | 1.0 | screenshot_mode defined with rationale |
| Resolution justification | 0.5 | Resolution apownte for target with cost consideration |
| Observe-act loop | 0.5 | Loop described in overview |
| Action parameter types | 0.5 | Each action parameter has type and valid values |
| Boundary clarity | 1.0 | Explicitly not a browser_tool, cli_tool, or vision_tool |
| Target specificity | 1.0 | Tool optimized for declared target environment |
| Domain specificity | 1.0 | Actions and resolution specific to the declared use case |
| Safety depth | 0.5 | Multiple safety constraints beyond minimum |
| Error handling | 0.5 | What happens when action fails (element not found, etc.) |
## Actions
| Score | Tier | Action |
|---|---|---|
| >= 9.5 | Golden | Publish to pool as golden reference |
| >= 8.0 | Publish | Publish to pool, add to routing index |
| >= 7.0 | Review | Flag for improvement before publish |
| < 7.0 | Reject | Return to author with specific gate failures |
## Bypass
| Field | Value |
|---|---|
| conditions | Internal testing tool for automation development |
| approver | Author self-certification with test-only scope comment |
| audit_trail | Bypass note in frontmatter with expiry date |
| expiry | 14d — test tools must be promoted or removed |
| never_bypass | H01 (unparseable YAML), H05 (self-scored gates), H08 (no actions = no tool) |
