---
id: p12_dr_keyword_agent_node
kind: dispatch_rule
pillar: P12
description: "Keyword-to-agent_node routing rules for orchestrator auto-dispatch"
scope: stella_routing
version: 1.0.0
created: 2026-03-24
author: orchestrator
quality: 9.0
tags: [dispatch-rule, routing, keyword, agent_node]
---

# Dispatch Rule: Keyword-to-Satellite

## Rules
| Keywords | Satellite | Model | Auto |
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
| < 45% | Guide to single agent_node |
| 45-70% | Suggest pipeline A -> B |
| >= 70% | Dispatch parallel grid |

## Cost Rule
Simple (haiku 5%) < Medium (sonnet 25%) < Complex (opus 100%).
Always minimize cost: never use opus for research, never use haiku for code.
