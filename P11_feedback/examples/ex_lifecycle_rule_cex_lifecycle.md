---
id: p11_lc_cex_lifecycle
kind: lifecycle_rule
pillar: P11
title: "CEX Artifact Lifecycle Rules"
version: "1.0.0"
created: "2026-03-22"
updated: "2026-03-22"
author: knowledge_agent
domain: meta
quality: 9.1
tags: [lifecycle, freshness, archive, promote, anti-fragility]
tldr: "Regras de freshness (30d), promotion (>=9.5), archive (<7.0), version sync e cascade para artefatos CEX"
when_to_use: "Quando precisar validar, promover ou arquivar artefatos do sistema CEX"
keywords: [lifecycle, freshness-scan, golden-promotion, archive-policy]
long_tails:
  - como gerenciar ciclo de vida de artefatos AI
  - regras de freshness e archive para knowledge base
axioms:
  - Artefato sem revalidacao em 30 dias = potencialmente stale
  - Promotion requer 2 validacoes independentes
density_score: 0.90
---

# CEX Lifecycle Rules

## Purpose
Regras de ciclo de vida para artefatos CEX — garantem freshness, promovem qualidade, arquivam decadencia.

## Rules

### R1: Freshness (30-day re-validation)
- **Trigger**: artefato nao modificado ha 30+ dias
- **Action**: re-executar validators (`validate_schema.py`, `validate_examples.py`)
- **Pass**: atualizar `updated` no frontmatter, manter ativo
- **Fail**: mover para review queue, flag como `stale`
- **Automation**: `_tools/validate_examples.py` pode ser agendado via cron/CI

### R2: Promotion (quality >= 9.5 -> golden)
- **Trigger**: example com quality score >= 9.5 confirmado por 2+ validacoes
- **Action**: copiar para `archetypes/golden/` com prefix `GOLDEN_`
- **Criteria**:
  - density >= 0.85
  - naming 100% conforme schema
  - size dentro de constraints
  - zero issues no validator
- **Label**: adicionar `tier: golden` no frontmatter

### R3: Archive (quality < 7.0 -> archive)
- **Trigger**: example com quality < 7.0 ou 3+ issues no validator
- **Action**: mover para `archetypes/archive/{lp}/` com timestamp
- **Retention**: arquivados por 90 dias, depois deletados
- **Recovery**: se re-editado e quality >= 7.0, pode voltar ao LP

### R4: Version Sync (schema change -> re-validate)
- **Trigger**: qualquer alteracao em `_schema.yaml`
- **Action**: re-executar todos os validators no LP afetado
- **Breaking change**: se naming pattern muda, marcar examples afetados como `needs_migration`
- **Non-breaking**: se apenas constraints mudam, re-validar e reportar

### R5: Cascade Rules
- Schema change -> re-validate examples + generator
- Generator change -> re-validate examples (naming may shift)
- New example -> validate against schema + size + density
- Promotion/archive -> update `archetypes/` indexes

## Quality Tiers

| Tier | Score | Density | Action |
|------|-------|---------|--------|
| Golden | >= 9.5 | >= 0.85 | Promote to `archetypes/golden/` |
| Skilled | 8.0-9.4 | >= 0.75 | Active, pool eligible |
| Learning | 7.0-7.9 | >= 0.65 | Active, needs improvement |
| Rejected | < 7.0 | any | Archive after 30 days |

## Automation Cadence

| Check | Frequency | Tool |
|-------|-----------|------|
| Schema integrity | Every commit | `validate_schema.py` |
| Generator completeness | Weekly | `validate_generators.py` |
| Example quality | Every commit + weekly | `validate_examples.py` |
| Freshness scan | Monthly | date check on `updated` field |

---
*Lifecycle Rules v1.0 | CEX Anti-Fragility Layer | 2026-03-22*
