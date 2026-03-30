---
id: p01_kc_lp04_tools
kind: knowledge_card
pillar: P01
title: "P04 Tools: O Que o Agente Usa"
version: 1.0.0
created: 2026-03-23
updated: 2026-03-23
author: builder_agent
domain: meta-construction
quality: 9.0
tags: [tools, skill, MCP, hook, plugin, connector]
tldr: "P04 define 9 tipos de ferramenta (skill, mcp_server, hook, plugin, client, cli_tool, scraper, connector, daemon) com skills como tipo principal — 58 golden destilados"
when_to_use: "Quando precisar criar tools, skills, hooks ou integracoes no CEX"
keywords: [skill, mcp_server, hook, plugin, connector, scraper]
long_tails:
  - "como criar uma skill reutilizavel no CEX"
  - "quais sao os 9 tipos de ferramenta em P04"
axioms:
  - "Skills com metricas reais tem confianca 2x maior que skills sem dados"
linked_artifacts:
  agent: null
  skill: p04_skill_cex_forge
density_score: 0.85
---

# P04 Tools: O Que o Agente Usa

## Executive Summary
P04 eh o dominio de ferramentas do CEX, com 9 tipos que cobrem desde skills reutilizaveis ate daemons de background. O tipo principal (skill) tem frontmatter com trigger + phases + when_to_use e body com workflow_phases numeradas. 58 golden skills validadas mostram que metricas reais dobram a confianca.

## Spec Table
| Campo | Valor | Nota |
|-------|-------|------|
| Tipos | 9 | skill, mcp_server, hook, plugin, client, cli_tool, scraper, connector, daemon |
| Skill max_bytes | 5120 | Body com phases + anti-patterns + metrics |
| MCP server max_bytes | 2048 | tools_provided + resources_provided |
| Hook max_bytes | 1024 | pre/post/stop trigger |
| Golden skills | 58 | Evidence base |
| MCP transports | 3 | stdio, sse, http |
| Hook types | 3 | pre, post, stop |

## Patterns
- Skill body: purpose > workflow_phases (numeradas com I/O) > anti_patterns > metrics
- MCP server: tools_provided + resources_provided como listas no frontmatter
- Hook: trigger_event + script_path para pre/post processing
- Metrics field (opcional) mas skills com dados reais rankeiam 2x melhor em quality

## Anti-Patterns
- Skill sem trigger: impossivel de invocar automaticamente
- Skill sem phases: vira instrucao vaga, nao workflow executavel
- MCP server sem transport: deploy ambiguo (stdio vs sse vs http)
- Hook sem script_path: hook fica inoperante

## Application
organization tem 116 skills on demand, acessiveis via Brain MCP. O forge P04 gera skill definitions completas que alimentam o catalogo. cex_forge.py eh ele mesmo uma cli_tool de P04.

## References
- P04_tools/_schema.yaml (fonte de verdade)
- DISTILL_GOLDEN_AGT_SKL_PATTERNS.md (58 golden skills)
- records/skills/ (116 skills ativas)
