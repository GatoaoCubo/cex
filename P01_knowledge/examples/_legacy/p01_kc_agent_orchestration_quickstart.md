---
id: p01_kc_agent_orchestration_quickstart
type: knowledge_card
lp: P01
title: Claude Agent Orchestration - Multi-Agent Patterns
version: 1.0.0
created: 2026-03-22
updated: 2026-03-22
author: EDISON
domain: meta
quality: 9.5
tags: [orchestration, multi-agent, handoffs, routing, agent-sdk]
tldr: Multi-agent orchestration patterns - triage routing, specialist handoffs, parallel fan-out, hierarchical managers, consensus voting
when_to_use: Ao projetar sistemas multi-agente, implementar routing entre agents, ou definir handoff protocols
keywords: [multi-agent, orchestration, triage, handoff, parallel-execution]
long_tails:
  - como rotear tasks entre multiplos agentes especializados
  - qual pattern usar para orquestrar agentes em paralelo vs sequencial
axioms:
  - Um agente monolitico = gargalo (especializar, nao generalizar)
  - Handoff sem contexto = agente cego (sempre incluir conversation history)
linked_artifacts:
  agent: p02_agent_gateway
  prompt: p03_pt_satellite_orchestrator
density_score: 0.90
---

# Claude Agent Orchestration - Multi-Agent Patterns

## Executive Summary

Anthropic's agent orchestration quickstart define patterns de producao para multi-agent: triage agent classifica e roteia, specialists executam, handoffs transferem contexto completo, e shared state conecta via pool/memory. 4 patterns fundamentais: Sequential Pipeline, Parallel Fan-Out, Hierarchical, Consensus.

## Spec Table

| Campo | Valor | Nota |
|-------|-------|------|
| Triage agent | Router central | Classifica intent, delega a specialist |
| Specialist agents | 1 dominio por agent | Ferramentas + instrucoes proprias |
| Handoff protocol | 5 steps | receive > classify > transfer > process > re-route |
| Shared state | 3 mecanismos | Conversation history, external store, structured metadata |
| CODEXA mapping | STELLA = Triage | 6 satellites = Specialists |

## Orchestration Patterns

| Pattern | Flow | Quando Usar |
|---------|------|-------------|
| Sequential Pipeline | A > B > C | research > analysis > report |
| Parallel Fan-Out | Router > [A, B, C] > Aggregate | multi-perspective analysis |
| Hierarchical | Manager > Workers > Manager | complex multi-step tasks |
| Consensus | [A, B, C] independentes > Vote | critical decisions, high-stakes |

## Handoff Protocol

```
1. Triage receives request
2. Classifies intent → selects target agent
3. Full conversation context transfers to specialist
4. Specialist processes and returns result
5. Triage can re-route if specialist can't handle
```

## Shared State Mechanisms

- **Conversation history**: automatico no handoff — specialist ve tudo que triage viu
- **External state store**: database, memory tool, pool — persiste entre sessions
- **Structured metadata**: JSON passado entre agents — input/output contracts

## CODEXA Direct Mapping

| Anthropic Pattern | CODEXA Equivalent |
|-------------------|-------------------|
| Triage agent | STELLA orchestrator |
| Specialist agents | 6 satellites (SHAKA, LILY, EDISON, PYTHA, ATLAS, YORK) |
| Handoffs | satellite spawn + signal files |
| Shared state | Pool + Brain MCP |
| Tracing | Symbiosis + learning system |

## Production Patterns

- **Guardrails**: em todo agent user-facing — prevent harmful/off-topic outputs
- **Tracing**: em toda interacao — observabilidade end-to-end
- **Timeouts**: por agent — evita hang infinito
- **Fallbacks**: agent de backup para failure cases — graceful degradation
- **Circuit breaker**: desabilita agent failing — evita cascading failures

## Anti-Patterns

- **Monolito**: single agent tentando fazer tudo — nao escala, nao especializa
- **Circular handoff**: A > B > A sem termination condition — loop infinito
- **No fallback**: specialist falha = task falha — sempre ter backup
- **Mutable shared state sem coordination**: race conditions entre agents — usar locks ou event sourcing
- **No observability**: "agent decidiu X" sem log — impossivel debugar routing errado

## References

- `records/pool/knowledge/KC_EDISON_029_CLAUDE_AGENT_ORCHESTRATION_QUICKSTART.md` (fonte original)
- Anthropic Agent SDK quickstart: github.com/anthropics/claude-quickstarts/tree/main/agents
- Related: KC_EDISON_024 (Agent SDK), KC_PYTHA_098 (competitive orchestration)
