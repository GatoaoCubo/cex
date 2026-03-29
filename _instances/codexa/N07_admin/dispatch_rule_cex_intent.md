---
id: p12_dr_cex_intent
kind: dispatch_rule
pillar: P12
title: "Dispatch Rule: CEX Intent Router"
version: 1.0.0
created: 2026-03-29
updated: 2026-03-29
author: stella
quality: null
tags: [dispatch-rule, intent, routing, cex, orchestration]
tldr: "Routes natural language intents to CEX kinds and 8F runner commands"
density_score: 0.90
---

# Dispatch Rule: CEX Intent Router

## Purpose
Translate user intent into executable `cex_8f_runner.py` commands.

## Rule Table
| Intent Pattern | Kind | Runner Command |
|---------------|------|----------------|
| "create/build/define agent" | agent | `--kind agent --topic {name}` |
| "create/write system prompt" | system_prompt | `--kind system_prompt --topic {name}` |
| "create/write instructions" | instruction | `--kind instruction --topic {name}` |
| "create knowledge card" | knowledge_card | `--kind knowledge_card --topic {name}` |
| "define workflow" | workflow | `--kind workflow --topic {name}` |
| "define/create quality gate" | quality_gate | `--kind quality_gate --topic {name}` |
| "create/define tool" | mcp_server | `--kind mcp_server --topic {name}` |
| "create/define skill" | skill | `--kind skill --topic {name}` |
| "create dispatch rule" | dispatch_rule | `--kind dispatch_rule --topic {name}` |
| "create agent card" | agent_card | `--kind agent_card --topic {name}` |
| "create/define guardrail" | guardrail | `--kind guardrail --topic {name}` |
| "create/define pattern" | pattern | `--kind pattern --topic {name}` |
| "create spawn config" | spawn_config | `--kind spawn_config --topic {name}` |
| "create/define eval" | unit_eval | `--kind unit_eval --topic {name}` |
| "create schema" | input_schema | `--kind input_schema --topic {name}` |
| "check health" | — | `python _tools/cex_doctor.py` |
| "decompose intent" | — | `python _tools/cex_8f_motor.py --intent "{text}"` |

## Fallback
If intent doesn't match: run `cex_8f_motor.py --intent "{text}"` to decompose into kinds.

## Multi-Kind Intents
Some intents produce multiple artifacts:
| Compound Intent | Kinds Produced |
|----------------|---------------|
| "create full agent" | agent + system_prompt + instruction + knowledge_card |
| "define complete workflow" | workflow + dispatch_rule + signal + quality_gate |
| "build nucleus" | agent_card + agent + system_prompt + workflow + dispatch_rule |

For multi-kind: run `cex_8f_runner.py` sequentially, one per kind.
