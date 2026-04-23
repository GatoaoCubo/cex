---
id: p01_kc_cex_lp09_config
kind: knowledge_card
pillar: P01
title: "CEX LP09 Config — Operational Control Panel for LLM Systems"
version: 1.0.0
created: 2026-03-25
updated: 2026-03-25
author: builder_agent
domain: cex_taxonomy
quality: 9.1
tags: [cex, lp09, config, env-config, feature-flag, permission, runtime-rule]
tldr: "P09 define 5 tipos de configuracao operacional: env_config, path_config, permission, feature_flag, runtime_rule"
when_to_use: "Entender como sistemas LLM separam configuracao de identidade e arquitetura"
keywords: [config, env-config, path-config, permission, feature-flag, runtime-rule]
long_tails:
  - "Como configurar variaveis de ambiente para agentes LLM"
  - "Qual a diferenca entre config P09 e boot_config P02 no CEX"
axioms:
  - "SEMPRE separar config (P09) de identidade (P02)"
  - "NUNCA hardcodar valores que pertencem a env_config"
linked_artifacts:
  primary: p01_kc_cex_lp08_architecture
  related: [p01_kc_cex_lp10_memory]
density_score: 1.0
data_source: "https://12factor.net/config"
related:
  - p01_kc_lp09_config
  - bld_architecture_env_config
  - env-config-builder
  - path-config-builder
  - bld_architecture_runtime_rule
  - bld_architecture_path_config
  - bld_examples_kind
  - runtime-rule-builder
  - bld_architecture_sso_config
  - bld_architecture_playground_config
---

## Quick Reference

topic: P09 Config | scope: operational settings | criticality: high
types: 5 | function: GOVERN | layer: runtime + governance

## Conceitos Chave

- P09 eh o painel de controle operacional do sistema
- env_config armazena variaveis de ambiente (API keys, URLs)
- path_config define caminhos do filesystem por escopo
- permission controla acesso read/write/execute por recurso
- feature_flag habilita/desabilita features com rollout
- runtime_rule define timeouts, retries e limites tecnicos
- P09 transforma arquitetura (P08) em operacao concreta
- Config NAO eh identidade: P02 define QUEM, P09 define COMO
- boot_config (P02) eh per-provider; env_config (P09) eh global
- permission (P09) controla acesso; guardrail (P11) eh safety
- runtime_rule (P09) eh tecnico; law (P08) eh inviolavel
- feature_flag usa JSON; demais tipos usam YAML
- env_config max 4096 bytes; feature_flag max 1536 bytes
- P09 configura P04 (quais tools estao habilitadas)
- P09 configura P02 (qual modelo, temperatura, tokens)
- Funcao dominante: GOVERN (governanca operacional)
- Analogia: altimetro em pes vs metros muda tudo

## Fases

1. Levantar todas as variaveis de ambiente necessarias
2. Criar env_config com valores por escopo (dev/staging/prod)
3. Definir path_config com caminhos absolutos por ambiente
4. Mapear permissions por recurso e papel (read/write/exec)
5. Isolar features experimentais com feature_flags
6. Documentar runtime_rules (timeouts, retries, rate limits)

## Regras de Ouro

- SEMPRE externalizar config (nunca inline no codigo)
- NUNCA confundir env_config com boot_config (P02)
- SEMPRE validar config na inicializacao (fail fast)
- NUNCA colocar secrets em feature_flags (usar env_config)
- SEMPRE ter defaults seguros quando config esta ausente

## Comparativo

| Tipo | Layer | Format | Max Bytes | Exemplo |
|------|-------|--------|-----------|---------|
| env_config | runtime | yaml | 4096 | API keys, URLs, secrets |
| path_config | runtime | yaml | 3072 | Dirs de agents, pool, output |
| permission | governance | yaml | 3072 | Agent_group write access |
| feature_flag | runtime | json | 1536 | Enable firecrawl enrichment |
| runtime_rule | runtime | yaml | 3072 | Timeout 30s, max 3 retries |

## Flow

```
[P09: Config Layer]
         |
    +----+----+----+----+
    |    |    |    |    |
  env  path perm  ff  rule
    |    |    |    |    |
    v    v    v    v    v
  [GOVERN]  [GOVERN]  [GOVERN]
    |          |        |
    v          v        v
 variaveis  acesso   limites
    |          |        |
    +-----+----+--------+
          |
          v
   [P04 tools habilitadas]
          |
          v
   [P02 modelo configurado]
```

## References

- source: https://12factor.net/config
- source: https://arxiv.org/abs/2308.00352
- related: p01_kc_cex_lp08_architecture
- related: p01_kc_cex_lp10_memory


## Anti-Patterns

- Applying this artifact without understanding the domain context
- Treating this as a standalone reference without checking linked artifacts
- Ignoring version constraints when integrating

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_lp09_config]] | sibling | 0.41 |
| [[bld_architecture_env_config]] | downstream | 0.38 |
| [[env-config-builder]] | downstream | 0.35 |
| [[path-config-builder]] | downstream | 0.30 |
| [[bld_architecture_runtime_rule]] | downstream | 0.27 |
| [[bld_architecture_path_config]] | downstream | 0.26 |
| [[bld_examples_kind]] | downstream | 0.25 |
| [[runtime-rule-builder]] | downstream | 0.25 |
| [[bld_architecture_sso_config]] | downstream | 0.25 |
| [[bld_architecture_playground_config]] | downstream | 0.25 |
