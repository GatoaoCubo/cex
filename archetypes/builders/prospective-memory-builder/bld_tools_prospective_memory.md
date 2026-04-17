---
kind: tools
id: bld_tools_prospective_memory
pillar: P04
llm_function: CALL
purpose: Tools for prospective_memory production
quality: 6.8
title: "Tools Prospective Memory"
version: "1.0.0"
author: n03_builder
tags: [prospective_memory, builder, tools]
tldr: "Tools for prospective_memory production."
domain: "prospective memory construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
---
# Tools: prospective-memory-builder

## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| cex_retriever.py | Find similar prospective_memory artifacts | Phase 1 | AVAILABLE |
| cex_score.py | Score artifact | Phase 3 | AVAILABLE |
| cex_compile.py | Compile to yaml | Phase 3 | AVAILABLE |

## Execution Mechanisms Reference
| Mechanism | CEX Tool | Notes |
|-----------|---------|-------|
| schedule_signal | ScheduleWakeup (Claude Code) | Native Claude Code scheduling |
| polling | cex_signal_watch.py | Polling loop for condition triggers |
| wake_notification | boot/cex.ps1 | Session-start check of pending reminders |

## Tool Permissions
| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Permitted |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | |

## Validation
id `^p10_pm_`, owner non-empty, reminders >= 1, trigger_type per reminder, action_payload non-vague, execution_mechanism declared, quality null, body <= 2048 bytes.
