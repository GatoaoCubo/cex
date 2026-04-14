---
kind: quality_gate
id: p08_qg_agent_computer_interface
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for agent_computer_interface
quality: null
title: "Quality Gate Agent Computer Interface"
version: "1.0.0"
author: wave1_builder_gen
tags: [agent_computer_interface, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for agent_computer_interface"
domain: "agent_computer_interface construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Definition
| metric | threshold | operator | scope |
|--------|-----------|----------|-------|
| Protocol Integrity | 100% | == | Schema |
| Command Latency | <50ms | < | Execution |
| Error Rate | <0.5% | < | Session |

## HARD Gates
| ID | Check | Fail Condition |
|----|-------|----------------|
| H01 | YAML valid | Syntax error |
| H02 | ID pattern | Non-conforming ID |
| H03 | Kind match | Not agent_computer_interface |
| H04 | Schema integrity | Missing required keys |
| H05 | Auth protocol | No auth defined |
| H06 | Command set | Empty command list |
| H07 | Error handling | No error mapping |

## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|-----|-----------|--------|---------------|
| D01 | Latency | 0.15 | <20ms: 1.0, >
