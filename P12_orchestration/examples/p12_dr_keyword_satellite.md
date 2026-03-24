---
id: p12_dr_keyword_satellite
type: dispatch_rule
lp: P12
description: "Keyword-to-satellite routing rules for STELLA auto-dispatch"
scope: stella_routing
version: 1.0.0
created: 2026-03-24
author: stella
quality: 9.0
tags: [dispatch-rule, routing, keyword, satellite]
---

# Dispatch Rule: Keyword-to-Satellite

## Rules
| Keywords | Satellite | Model | Auto |
|----------|-----------|-------|------|
| pesquisar, mercado, concorrente | SHAKA | sonnet | YES |
| anuncio, marketing, copy, vender | LILY | sonnet | YES |
| criar, build, codigo, componente | EDISON | opus | YES |
| conhecimento, documentar, indexar | PYTHA | sonnet | YES |
| executar, testar, debug, deploy | ATLAS | opus | YES |
| curso, monetizar, preco, hotmart | YORK | sonnet | YES |
| browser, chrome, screenshot, scrape | CHROME | sonnet | YES |

## Score Routing
| Complexity | Action |
|-----------|--------|
| < 45% | Guide to single satellite |
| 45-70% | Suggest pipeline A -> B |
| >= 70% | Dispatch parallel grid |

## Cost Rule
Simple (haiku 5%) < Medium (sonnet 25%) < Complex (opus 100%).
Always minimize cost: never use opus for research, never use haiku for code.
