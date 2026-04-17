---
id: bld_quality_gate_process_manager
kind: quality_gate
pillar: P12
title: "Process Manager Builder -- Quality Gate"
version: 1.0.0
quality: null
tags: [builder, process_manager, quality_gate]
llm_function: GOVERN
---
# Gate: process_manager
## Threshold
>= 7.0 to publish; >= 9.0 for reference
## HARD Gates
| ID | Check | Fail Condition |
|----|-------|----------------|
| H01 | Frontmatter parses as valid YAML | Syntax error |
| H02 | id matches `^p12_pm_[a-z][a-z0-9_]+$` | Wrong pattern |
| H03 | id equals filename stem | Mismatch |
| H04 | kind == `process_manager` | Any other value |
| H05 | quality == null | Non-null |
| H06 | correlation_key defined | Missing |
| H07 | start_event defined | Missing |
| H08 | terminal_states has >= 2 entries (success + failure) | Fewer than 2 |
| H09 | subscribed_events has >= 1 entry | Empty |
| H10 | commands_issued has >= 1 entry | Empty |
## SOFT Scoring
| Dim | Check | Weight |
|-----|-------|--------|
| S01 | Event routing table complete (event -> state + command) | 0.25 |
| S02 | Compensation actions defined for each failure path | 0.20 |
| S03 | Timeout strategy defined for waiting states | 0.15 |
| S04 | No business data in process manager (state + key only) | 0.20 |
| S05 | Idempotency key specified for commands | 0.10 |
| S06 | Persistence strategy specified | 0.10 |
**Weight sum: 1.00**
## Actions
| Score | Action |
|-------|--------|
| >= 9.0 | PUBLISH |
| >= 7.0 | REVIEW |
| < 7.0 | REJECT |
