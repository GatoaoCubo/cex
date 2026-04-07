---
id: p01_kc_lp09_config
kind: knowledge_card
pillar: P01
title: "P09 Config: Como Configura"
version: 1.0.0
created: 2026-03-23
updated: 2026-03-23
author: builder_agent
domain: meta-construction
quality: 9.0
tags: [config, env, permissions, feature_flag, runtime]
tldr: "P09 define 5 tipos de configuracao (env_config, path_config, permission, feature_flag, runtime_rule) que controlam ambiente, caminhos, permissoes e comportamento em runtime"
when_to_use: "Quando precisar definir configuracoes de ambiente, permissoes ou feature flags no CEX"
keywords: [env_config, path_config, permission, feature_flag, runtime_rule]
long_tails:
  - "como definir variaveis de ambiente no CEX"
  - "como criar um feature flag com rollout gradual"
axioms:
  - "Configuracao deve ser declarativa em YAML — nunca hardcoded em codigo"
linked_artifacts:
  agent: null
  skill: null
density_score: 0.84
---

# P09 Config: Como Configura

## Executive Summary
P09 centraliza toda configuracao do CEX em 5 tipos de artefato YAML. Env configs definem variaveis de ambiente, path configs mapeiam caminhos do sistema, permissions controlam read/write/execute, feature flags habilitam rollout gradual, e runtime rules definem timeouts/retries/limits.

## Spec Table
| Campo | Valor | Nota |
|-------|-------|------|
| Tipos | 5 | env_config, path_config, permission, feature_flag, runtime_rule |
| env_config max_bytes | 4096 | Variaveis de ambiente |
| path_config max_bytes | 3072 | Caminhos do sistema |
| permission max_bytes | 3072 | read/write/execute |
| feature_flag max_bytes | 1536 | Menor tipo — on/off simples |
| runtime_rule max_bytes | 3072 | timeouts, retries, limits |

## Patterns
- Env config agrupa variaveis por scope (dev, staging, prod)
- Path config centraliza caminhos — agents nao hardcodam paths
- Permission com 3 niveis: read, write, execute per scope
- Feature flag com gradual rollout: 0% > 10% > 50% > 100%
- Runtime rule com defaults + overrides por agent_group

## Anti-Patterns
- Hardcoded paths em agentes: quebra ao mudar ambiente
- Feature flag sem fallback: crash se flag nao existe
- Permission sem scope: tudo eh global, sem granularidade
- Runtime rule sem timeout: processo pode travar indefinidamente

## Application
No organization, P09 manifesta como .claude/settings.json, .mcp-{sat}.json, e boot scripts. O CEX formaliza esses configs como artefatos versionaveis e validaveis, permitindo diff e rollback de configuracao.

## References
- P09_config/_schema.yaml (fonte de verdade)
- .claude/settings.json (instancia real de P09)
