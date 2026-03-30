---
id: p12_sc_admin_orchestrator
kind: spawn_config
pillar: P12
title: Spawn Config -- N07 Orchestrator
version: 2.0.0
created: 2026-03-30
updated: 2026-03-30
author: builder_agent
domain: orchestration
quality: 9.0
tags: [spawn-config, orchestrator, N07, multi-cli]
tldr: Multi-CLI orchestration -- each nucleus uses the best LLM provider for its domain.
density_score: 0.90
---

# Spawn Config: N07 Orchestrator

## CLI Matrix (Best Tool for Each Job)

| Nucleus | CLI | Model | Context | Cost | Domain Strength |
|---------|-----|-------|---------|------|-----------------|
| N07 Orchestrator | pi + claude | opus-4-6 xhigh | 200K | 1156$ | Meta-reasoning, dispatch |
| N03 Builder | claude | opus | 200K | 1156$ | Complex construction, 8F |
| N05 Operations | codex | GPT-5.4 | 192K | 1156 | Code review, testing, debug |
| N04 Knowledge | gemini | 2.5-pro | 1M | /usr/bin/bash | Large docs, RAG, indexing |
| N01 Research | gemini | 2.5-pro | 1M | /usr/bin/bash | Papers, market analysis |
| N02 Marketing | claude | sonnet | 200K | $ | Creative writing, copy |
| N06 Commercial | claude | sonnet | 200K | $ | Persuasive copy, pricing |

## Why Multi-CLI

No single LLM is best at everything:
- **Claude opus**: Best at complex reasoning, construction, orchestration
- **Codex/GPT-5.4**: Best at code generation, testing, debugging
- **Gemini 2.5 Pro**: 1M context window, free via subscription, ideal for knowledge
- **Claude sonnet**: Best cost/quality for creative writing

## Boot Commands

| Nucleus | Command |
|---------|---------|
| N07 | boot\cex.cmd (pi + opus xhigh) |
| N03 | boot
03.cmd (claude opus) |
| N05 | boot
05.cmd (codex full-auto) |
| N04 | boot
04.cmd (gemini 2.5-pro yolo) |
| N01 | boot
01.cmd (gemini 2.5-pro yolo) |
| N02 | boot
02.cmd (claude sonnet) |
| N06 | boot
06.cmd (claude sonnet) |

## Spawn Commands (from N07)

| Mode | Command |
|------|---------|
| Solo | powershell -File _spawn/spawn_solo.ps1 -nucleus n03 -task TASK -interactive |
| Grid | powershell -File _spawn/spawn_grid.ps1 -mission NAME -interactive |
| Continuous | powershell -File _spawn/spawn_grid.ps1 -mission NAME -mode continuous |
| Monitor | powershell -File _spawn/spawn_monitor.ps1 |
| Stop | powershell -File _spawn/spawn_stop.ps1 |

## Cost Optimization

- Use gemini (N01, N04) for knowledge-heavy tasks: /usr/bin/bash cost via subscription
- Use codex (N05) for code tasks: competitive pricing
- Use sonnet (N02, N06) for creative: 5x cheaper than opus
- Reserve opus (N03, N07) for complex construction and orchestration only