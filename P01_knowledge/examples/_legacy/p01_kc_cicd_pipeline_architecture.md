---
id: p01_kc_cicd_pipeline_architecture
kind: knowledge_card
pillar: P01
title: CI/CD Pipeline Architecture - Multi-Satellite Systems
version: 1.0.0
created: 2026-03-22
updated: 2026-03-22
author: ATLAS
domain: execution
quality: 9.0
tags: [cicd, pipeline, github-actions, deployment, testing, automation]
tldr: CI/CD para multi-satellite - trunk-based + feature branches, 7-stage pipeline (lint>type>unit>integration>build>staging>prod), quality gates em CI, auto-rollback em health check fail
when_to_use: Ao configurar CI/CD, definir branch strategy, ou debugar pipeline de deploy
keywords: [cicd, pipeline, deployment, branch-strategy, rollback, quality-gates]
long_tails:
  - como configurar CI/CD pipeline para sistema multi-agente
  - qual branch strategy usar com trunk-based development
axioms:
  - CI que nao bloqueia merge em falha = nao e CI (enforcement obrigatorio)
  - Deploy sem health check = roleta russa (auto-rollback obrigatorio em prod)
linked_artifacts:
  agent: p02_agent_atlas
  skill: p04_skill_ship
density_score: 0.87
---

# CI/CD Pipeline Architecture - Multi-Satellite Systems

## Executive Summary

CODEXA usa trunk-based development com feature branches. Pipeline de 7 stages (Lint > Type Check > Unit > Integration > Build > Staging > Production) com quality gates automaticos. Cada satellite pode ter CI steps domain-specific. Rollback automatico em health check failure em producao.

## Spec Table

| Campo | Valor | Nota |
|-------|-------|------|
| Model | Trunk-based | main = production-ready |
| Branches | main, feature/*, fix/*, wave-* | Protection rules por tipo |
| Pipeline stages | 7 | ~15min total |
| Coverage threshold | 80% | Bloqueia merge se abaixo |
| Max lint warnings | 0 | Zero tolerance |
| Required reviewers | 1 | Para merge em main |
| Rollback | Auto em prod | Health check < 60s |

## Branch Strategy

| Branch | Proposito | Protection | Deploy |
|--------|-----------|------------|--------|
| `main` | Production-ready | Reviews + CI pass | Production |
| `feature/*` | New features | CI required | Preview |
| `fix/*` | Bug fixes | CI required | Preview |
| `wave-*` | Consolidation waves | CI required | Staging |

## Pipeline Stages

| Stage | Duracao | Falha = |
|-------|---------|---------|
| Lint + Format | ~30s | Block merge |
| Type Check | ~45s | Block merge |
| Unit Tests | ~2min | Block merge |
| Integration Tests | ~5min | Block merge + notify |
| Build | ~3min | Block merge |
| Deploy Staging | ~2min | Manual rollback |
| Deploy Production | ~2min | Auto-rollback em health check fail |

## Quality Gates CI

```yaml
quality_gates:
  coverage_threshold: 80
  max_bundle_size_kb: 500
  max_lint_warnings: 0
  required_reviewers: 1
  ci_must_pass: true
```

## Environment Promotion

```
Development --> Staging --> Production
    |              |            |
  Auto           Auto       Manual gate
 (on push)    (on merge)  (approval required)
```

## Satellite-Specific CI

| Satellite | CI Step Adicional |
|-----------|-------------------|
| SHAKA | Validar schemas de research output |
| LILY | Checar quality scores de copy |
| EDISON | Build + bundle analysis |
| PYTHA | Frontmatter validation de KCs |
| ATLAS | Full test suite + deploy validation |
| YORK | Course content completeness check |

## Anti-Patterns

- **CI sem enforcement**: warnings ignorados, merge sem review — todo gate deve bloquear
- **Deploy prod sem health check**: issue so aparece quando user reclama — auto-rollback < 60s
- **Branches long-lived**: feature branch de 3 semanas = merge hell — trunk-based, PRs pequenos
- **Skip integration tests**: "unit ta passando" — integration testa o que unit nao cobre (DB, API)

## Rollback Procedure

1. Detectar falha via health check (automatico, < 60s)
2. Trigger rollback para deployment anterior
3. Notificar team via signal file
4. Post-mortem apos estabilizacao

## References

- `records/pool/knowledge/KC_ATLAS_007_CI_CD_PIPELINE_ARCHITECTURE.md` (fonte original)
- `records/framework/docs/SPAWN_PLAYBOOK.md` (deploy protocol)
- GitHub Actions documentation
