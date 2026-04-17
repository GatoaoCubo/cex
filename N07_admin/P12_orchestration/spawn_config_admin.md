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
quality: 9.1
tags: [spawn-config, orchestrator, N07, multi-cli]
tldr: Multi-CLI orchestration -- each nucleus uses the best LLM provider for its domain.
density_score: 0.90
linked_artifacts:
  primary: "N07_admin/orchestration/workflow_admin.md"
  related:
    - N07_admin/orchestration/handoff_admin.md
    - N07_admin/orchestration/signal_admin.md
    - N07_admin/memory/grid_orchestration_mastery.md
---

# Spawn Config: N07 Orchestrator

## CLI Matrix (Best Tool for Each Job)

| Nucleus | CLI | Model | Context | Cost | Domain Strength |
|---------|-----|-------|---------|------|-----------------|
| N07 Orchestrator | claude | opus-4-6 xhigh | 200K | 1156$ | Meta-reasoning, dispatch |
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

Boot scripts are **generated** from `.cex/config/nucleus_models.yaml`:
```bash
python _tools/cex_boot_gen.py          # regenerate all
python _tools/cex_boot_gen.py --show   # show current matrix
```

| Nucleus | Command | Generated from config |
|---------|---------|----------------------|
| N07 | boot\cex.cmd | n07.cli + n07.model |
| N01 | boot\n01.cmd | n01.cli + n01.model |
| N02 | boot\n02.cmd | n02.cli + n02.model |
| N03 | boot\n03.cmd | n03.cli + n03.model |
| N04 | boot\n04.cmd | n04.cli + n04.model |
| N05 | boot\n05.cmd | n05.cli + n05.model |
| N06 | boot\n06.cmd | n06.cli + n06.model |

## Spawn Commands (from N07)

| Mode | Command |
|------|---------|
| Solo | powershell -File _spawn/spawn_solo.ps1 -nucleus n03 -task TASK -interactive |
| Grid | powershell -File _spawn/spawn_grid.ps1 -mission NAME -interactive |
| Continuous | powershell -File _spawn/spawn_grid.ps1 -mission NAME -mode continuous |
| Monitor | powershell -File _spawn/spawn_monitor.ps1 |
| Stop | powershell -File _spawn/spawn_stop.ps1 |

## Cost Optimization

- All nuclei upgraded to claude/opus-4-6 with 1M context (2026-04-06)
- Fallback: gemini-2.5-pro (cross-provider), then ollama/qwen3 (local)
- Config source: .cex/config/nucleus_models.yaml (regenerate boot scripts via cex_boot_gen.py)
- Reserve opus (N03, N07) for complex construction and orchestration only