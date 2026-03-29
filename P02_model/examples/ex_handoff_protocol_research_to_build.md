---
id: p02_hp_research_to_build
kind: handoff_protocol
pillar: P02
title: Research-to-Build Handoff (SHAKA to EDISON)
version: 1.0.0
created: 2026-03-29
updated: 2026-03-29
author: EDISON
domain: orchestration
quality: 9.0
tags: [handoff-protocol, shaka, edison, research, build, satellite, a2a]
tldr: Protocolo de handoff entre SHAKA (pesquisa) e EDISON (build) — SHAKA entrega findings+sources+quality_score via arquivo .md, EDISON consome e produz build artifacts
when_to_use: Quando pesquisa SHAKA deve alimentar implementacao EDISON sem intervencao manual de STELLA
---

# Handoff Protocol: Research-to-Build (SHAKA -> EDISON)

## Overview
Define o contrato de transferencia de contexto entre SHAKA (satelite de pesquisa) e EDISON (satelite de build). SHAKA produz findings estruturados como knowledge cards ou research reports; EDISON consome esses artifacts para implementar agentes, skills, ou componentes. O handoff e assincrono via filesystem — nao requer ambos satelites ativos simultaneamente.

## Trigger
| Field | Value |
|-------|-------|
| event | `research_complete` |
| source_satellite | SHAKA |
| target_satellite | EDISON |
| trigger_mechanism | Signal file: `.claude/signals/shaka_complete_*.json` |
| detection | STELLA poll (15s interval) ou `stella_signal_monitor.py --watch` |

## Context Contract (SHAKA -> EDISON)
```yaml
handoff_file: .claude/handoffs/{MISSION}_edison.md
required_context:
  findings:
    type: list[object]
    description: Descobertas da pesquisa, cada uma com evidencia
    min_items: 3
    schema:
      - finding: string       # Descoberta principal
      - evidence: string      # URL, citacao, ou dados que suportam
      - confidence: float     # 0.0-1.0 confianca na descoberta
      - relevance: enum       # critical | high | medium | low
  sources:
    type: list[object]
    description: Fontes consultadas com metadados
    min_items: 1
    schema:
      - url: string
      - title: string
      - type: enum            # documentation | paper | repo | blog | marketplace
      - accessed_at: datetime
      - credibility: float    # 0.0-1.0
  quality_score:
    type: float
    description: Auto-avaliacao da qualidade da pesquisa (Shokunin)
    minimum: 7.0              # Abaixo de 7.0, STELLA rejeita e solicita redo
  seeds:
    type: list[string]
    description: Palavras-chave para input hydration do EDISON
    min_items: 5
optional_context:
  knowledge_card_path:
    type: string
    description: Path da KC gerada, se PYTHA ja processou
  competitor_data:
    type: object
    description: Dados de concorrentes se pesquisa foi competitiva
  raw_data_path:
    type: string
    description: Path para dados brutos (JSON/CSV) se coletados
```

## Return Contract (EDISON -> STELLA)
```yaml
signal_file: .claude/signals/edison_complete_*.json
return_artifacts:
  - type: string              # agent | skill | component | knowledge_card
  - path: string              # Caminho do artifact criado
  - quality_score: float      # 7.0+
  - tests_passed: boolean     # Se aplicavel
  - commit_sha: string        # Hash do commit com o artifact
```

## Handoff File Template
```markdown
# EDISON — {MISSION}: {Title}
**Autonomia Total** | **Quality 9.0+**
**REGRA: Commit e signal ANTES de qualquer pausa.**

## CONTEXTO
SHAKA completou pesquisa sobre {topic}. Score: {quality_score}.
Findings principais: {top_3_findings_summary}

## RESEARCH ARTIFACTS
- KC: {knowledge_card_path or "nao gerada"}
- Raw data: {raw_data_path or "nao coletado"}
- Sources: {source_count} fontes ({credibility_avg} credibilidade media)

## SEEDS
`{seed1}, {seed2}, {seed3}, {seed4}, {seed5}`

## FINDINGS (structured)
{findings_yaml_block}

## TAREFAS
### Step 1: Internalizar pesquisa
Ler KC em {knowledge_card_path}. Extrair patterns e anti-patterns.

### Step 2: Implementar
{specific_build_instructions}

### Step 3: Validar
Testar artifact contra quality gates do tipo.

## SCOPE FENCE
- SOMENTE: {allowed_paths}
- NAO TOQUE: {forbidden_paths}

## COMMIT
git add {artifact_paths} && git commit -m "EDISON[{MISSION}]: {desc}"

## SIGNAL
python -c "from records.core.python.signal_writer import write_signal; write_signal('edison', 'complete', {score})"
```

## Error Handling
| Scenario | Action |
|----------|--------|
| SHAKA signal com score < 7.0 | STELLA rejeita, solicita re-research com feedback |
| Handoff file missing required fields | EDISON solicita contexto adicional via STELLA |
| EDISON nao consegue localizar KC | Prosseguir com findings inline do handoff |
| Build falha apos 3 tentativas | EDISON sinaliza `partial` com score real e lista de bloqueios |

## Sequence Diagram
```text
STELLA                    SHAKA                     EDISON
  |                         |                         |
  |-- dispatch handoff ---->|                         |
  |                         |-- research (async) ---->|
  |                         |                         |
  |                         |<-- findings + KC -------|
  |                         |                         |
  |<-- signal: complete ----|                         |
  |    (score >= 7.0)       |                         |
  |                         |                         |
  |-- compose handoff_edison.md ----------------------|
  |                                                   |
  |-- spawn EDISON with handoff --------------------->|
  |                                                   |
  |                                   |-- read handoff |
  |                                   |-- build ------>|
  |                                   |-- commit ----->|
  |                                   |-- signal ----->|
  |                                                   |
  |<---------------- signal: complete ----------------|
```

## Real Example (2026-03-05)
Mission ISOFIX: SHAKA pesquisou 118 agents para gap analysis. Handoff para EDISON continha 47 findings com paths de ISOs faltantes. EDISON executou 7 batches em continuous mode, criando 820+ ISO files. Score final: 9.0.

## Related
- `ex_agent_gateway.md` — Gateway agent que pode intermediar handoffs
- `ex_boot_config_edison_claude.md` — Boot config do EDISON receptor
- `records/framework/docs/SPAWN_PLAYBOOK.md` — Playbook completo de spawn
