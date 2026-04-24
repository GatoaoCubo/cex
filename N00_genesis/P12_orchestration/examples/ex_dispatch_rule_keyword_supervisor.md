---
id: p12_dr_keyword_agent_group
kind: dispatch_rule
8f: F8_collaborate
pillar: P12
description: "Keyword-to-agent_group routing rules for orchestrator auto-dispatch"
scope: stella_routing
version: 1.0.0
created: 2026-03-24
author: orchestrator
quality: 9.0
tags: [dispatch-rule, routing, keyword, agent_group]
updated: "2026-04-07"
domain: "orchestration"
title: "Dispatch Rule Keyword Supervisor"
density_score: 0.92
tldr: "Defines dispatch rule for dispatch rule keyword supervisor, with validation gates and integration points."
related:
  - p02_mc_claude_opus_4
  - p07_bm_agent_group_boot_time
  - bld_schema_spawn_config
  - p01_kc_claude_model_capabilities_2026
  - bld_schema_bugloop
  - bld_schema_quickstart_guide
  - bld_schema_reranker_config
  - bld_schema_nucleus_def
  - bld_schema_voice_pipeline
  - bld_schema_action_paradigm
---

# Dispatch Rule: Keyword-to-Agent_group

## Rules
| Keywords | Agent_group | Model | Auto |
|----------|-----------|-------|------|
| pesquisar, mercado, concorrente | research_agent | sonnet | YES |
| anuncio, marketing, copy, vender | marketing_agent | sonnet | YES |
| criar, build, codigo, componente | builder_agent | opus | YES |
| conhecimento, documentar, indexar | knowledge_agent | sonnet | YES |
| executar, testar, debug, deploy | operations_agent | opus | YES |
| curso, monetizar, preco, hotmart | commercial_agent | sonnet | YES |
| browser, chrome, screenshot, scrape | CHROME | sonnet | YES |

## Score Routing
| Complexity | Action |
|-----------|--------|
| < 45% | Guide to single agent_group |
| 45-70% | Suggest pipeline A -> B |
| >= 70% | Dispatch parallel grid |

## Cost Rule
Simple (haiku 5%) < Medium (sonnet 25%) < Complex (opus 100%).
Always minimize cost: never use opus for research, never use haiku for code.

## Pipeline Integration

1. Created via 8F pipeline from F1-Focus through F8-Furnish
2. Scored by cex_score across three structural layers
3. Compiled by cex_compile for structural validation
4. Retrieved by cex_retriever for context injection
5. Evolved by cex_evolve when quality regresses below target

## Metadata

```yaml
id: p12_dr_keyword_agent_group
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply p12-dr-keyword-agent-group.md
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p02_mc_claude_opus_4]] | upstream | 0.45 |
| [[p07_bm_agent_group_boot_time]] | upstream | 0.34 |
| [[bld_schema_spawn_config]] | upstream | 0.32 |
| [[p01_kc_claude_model_capabilities_2026]] | upstream | 0.31 |
| [[bld_schema_bugloop]] | upstream | 0.31 |
| [[bld_schema_quickstart_guide]] | upstream | 0.30 |
| [[bld_schema_reranker_config]] | upstream | 0.30 |
| [[bld_schema_nucleus_def]] | upstream | 0.29 |
| [[bld_schema_voice_pipeline]] | upstream | 0.29 |
| [[bld_schema_action_paradigm]] | upstream | 0.29 |
