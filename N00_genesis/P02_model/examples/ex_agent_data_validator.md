---
id: p02_agent_data_validator
kind: agent
8f: F2_become
pillar: P02
title: Data Validator Agent
version: 1.0.0
created: 2026-03-24
updated: 2026-03-24
author: builder_agent
agent_group: operations_agent
domain: data_quality
quality: 9.1
tags: [data-validation, quality-assurance, pipeline, schema-check, anomaly-detection]
tldr: Agente autonomo que valida qualidade de dados em pipelines — detecta schema drift, anomalias estatisticas, nulls inesperados e violacoes de regras de negocio
when_to_use: Quando pipeline de dados precisa de validacao automatica antes de ingestao ou publicacao
related:
  - p02_agent_web_researcher
  - agent-builder
  - bld_collaboration_validation_schema
  - bld_collaboration_agent
  - bld_collaboration_output_validator
  - output-validator-builder
  - p01_kc_agent
  - bld_collaboration_validator
  - validator-builder
  - bld_examples_validator
---

# Data Validator Agent

## Overview
data-validator e o agente de validacao de qualidade de dados do organization. Atua quando dados entram ou saem de pipelines (ETL, API, scraping) e entrega relatorios de qualidade com score por dimensao e lista de violacoes acionaveis.

## Architecture
```text
[Data Source] -> [Schema Validator] -> [Statistical Checker] -> [Business Rules] -> [Report + Score]
                       |                       |                       |
                 [JSON Schema]          [Distribution]          [Custom Rules]
                 [Type Check]           [Outlier Z>3]           [Null Policy]
```

## File Structure
- `manifest.yaml`: Identidade, capabilities, routing keywords
- `system_instruction.md`: Persona validador rigoroso + guardrails de rejeicao
- `instructions.md`: Pipeline 4-fase (schema -> stats -> rules -> report)
- `validation_rules.yaml`: Biblioteca de regras reutilizaveis por dominio

## When to Use
| Cenario | Usar? |
|---------|-------|
| Validar CSV/JSON antes de ingestao em banco | SIM |
| Checar schema drift entre versoes de API | SIM |
| Detectar anomalias em dados de scraping | SIM |
| Validar output de outros agentes organization | SIM |
| Transformar dados (ETL) | NAO -> use builder agent |
| Monitorar metricas de sistema (CPU, RAM) | NAO -> use monitor-agent |

## Input Output
```yaml
input:
  data: object       # Dados a validar (JSON, CSV path, ou dataframe ref)
  schema: object     # Schema esperado (JSON Schema, YAML, ou inferido)
  rules: list        # Regras de negocio customizadas (opcional)
  strictness: enum   # lenient|standard|strict (default: standard)
output:
  valid: boolean     # Pass/fail global
  score: float       # 0.0-10.0 quality score
  violations: list   # [{field, rule, severity, value, expected}]
  stats: object      # Cobertura, nulls%, duplicatas%, type mismatches
```

## Integration
- Upstream: scraper-agents (pos-coleta), builder (pos-build), API endpoints (pre-ingestao)
- Downstream: qa-agent (quality aggregation), monitor-agent (alertas)
- Dependencies: JSON Schema lib, pandas (stats), Brain MCP (regras de dominio)

## Quality Gates
- Schema validation: 100% dos campos required presentes
- Type accuracy: >= 99% dos valores match tipo declarado
- Null tolerance: configurable por campo (default: < 5%)
- Outlier detection: Z-score > 3 flagged com severity warning
- Business rules: 100% pass para severity=critical

## Common Issues
- Schema inferido diverge do real -> sempre preferir schema explicito quando disponivel
- Dados de scraping com encoding misto (UTF-8/Latin1) -> normalizar encoding antes de validar
- Falsos positivos em outlier detection para distribuicoes bimodais -> usar IQR em vez de Z-score

## Invocation
```text
# Via orchestrator dispatch
/atlas "Validar dados de scraping em data/raw/products.json contra schema/products.yaml"

# Via subagent direto
Agent(subagent_type="validator", prompt="Validate output of scraper against expected schema")
```

## Related Agents
- qa-agent: Agregacao de qualidade cross-agent (usa data-validator como input)
- tester-agent: Testa codigo; data-validator testa dados
- evaluator-agent: Avalia output LLM; data-validator avalia dados estruturados

## Footer
Agent_group: operations_agent | Quality: 9.0 | Domain: data_quality

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p02_agent_web_researcher]] | sibling | 0.28 |
| [[agent-builder]] | related | 0.22 |
| [[bld_collaboration_validation_schema]] | downstream | 0.22 |
| [[bld_collaboration_agent]] | downstream | 0.22 |
| [[bld_collaboration_output_validator]] | downstream | 0.21 |
| [[output-validator-builder]] | downstream | 0.21 |
| [[p01_kc_agent]] | related | 0.21 |
| [[bld_collaboration_validator]] | downstream | 0.20 |
| [[validator-builder]] | downstream | 0.20 |
| [[bld_examples_validator]] | downstream | 0.19 |
