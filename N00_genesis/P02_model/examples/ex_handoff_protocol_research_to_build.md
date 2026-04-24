---
id: p02_hp_research_to_build
kind: handoff_protocol
8f: F8_collaborate
pillar: P02
title: Research-to-Build Handoff (research_agent to builder_agent)
version: 1.0.0
created: 2026-03-29
updated: 2026-03-29
author: builder_agent
domain: orchestration
quality: 9.1
tags: [handoff-protocol, shaka, edison, research, build, agent_group, a2a]
tldr: Protocolo de handoff entre research_agent (pesquisa) e builder_agent (build) — research_agent entrega findings+sources+quality_score via arquivo .md, builder_agent consome e produz build artifacts
when_to_use: Quando pesquisa research_agent deve alimentar implementacao builder_agent sem intervencao manual de orchestrator
related:
  - bld_examples_handoff_protocol
  - p06_iface_agent_group_handoff
  - p03_ch_content_pipeline
  - bld_examples_workflow
  - p12_wf_creation_pipeline
  - p06_is_creation_data
  - bld_schema_model_registry
  - p03_pv_pesquisa_system_v2
  - p06_is_knowledge_data_model
  - p03_ch_kc_to_notebooklm
---

# Handoff Protocol: Research-to-Build (research_agent -> builder_agent)

## Overview
Define o contrato de transferencia de contexto entre research_agent (agent_group de pesquisa) e builder_agent (agent_group de build). research_agent produz findings estruturados como knowledge cards ou research reports; builder_agent consome esses artifacts para implementar agentes, skills, ou componentes. O handoff e assincrono via filesystem — nao requer ambos agent_groups ativos simultaneamente.

## Trigger
| Field | Value |
|-------|-------|
| event | `research_complete` |
| source_agent_group | research_agent |
| target_agent_group | builder_agent |
| trigger_mechanism | Signal file: `.claude/signals/shaka_complete_*.json` |
| detection | orchestrator poll (15s interval) ou `stella_signal_monitor.py --watch` |

## Context Contract (research_agent -> builder_agent)
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
    minimum: 7.0              # Abaixo de 7.0, orchestrator rejeita e solicita redo
  seeds:
    type: list[string]
    description: Palavras-chave para input hydration do builder_agent
    min_items: 5
optional_context:
  knowledge_card_path:
    type: string
    description: Path da KC gerada, se knowledge_agent ja processou
  competitor_data:
    type: object
    description: Dados de concorrentes se pesquisa foi competitiva
  raw_data_path:
    type: string
    description: Path para dados brutos (JSON/CSV) se coletados
```

## Return Contract (builder_agent -> orchestrator)
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
# builder_agent — {MISSION}: {Title}
**Autonomia Total** | **Quality 9.0+**
**REGRA: Commit e signal ANTES de qualquer pausa.**

## CONTEXTO
research_agent completou pesquisa sobre {topic}. Score: {quality_score}.
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
git add {artifact_paths} && git commit -m "builder_agent[{MISSION}]: {desc}"

## SIGNAL
python -c "from records.core.python.signal_writer import write_signal; write_signal('edison', 'complete', {score})"
```

## Error Handling
| Scenario | Action |
|----------|--------|
| research_agent signal com score < 7.0 | orchestrator rejeita, solicita re-research com feedback |
| Handoff file missing required fields | builder_agent solicita contexto adicional via orchestrator |
| builder_agent nao consegue localizar KC | Prosseguir com findings inline do handoff |
| Build falha apos 3 tentativas | builder_agent sinaliza `partial` com score real e lista de bloqueios |

## Sequence Diagram
```text
orchestrator                    research_agent                     builder_agent
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
  |-- spawn builder_agent with handoff --------------------->|
  |                                                   |
  |                                   |-- read handoff |
  |                                   |-- build ------>|
  |                                   |-- commit ----->|
  |                                   |-- signal ----->|
  |                                                   |
  |<---------------- signal: complete ----------------|
```

## Real Example (2026-03-05)
Mission ISOFIX: research_agent pesquisou 118 agents para gap analysis. Handoff para builder_agent continha 47 findings com paths de ISOs faltantes. builder_agent executou 7 batches em continuous mode, criando 820+ ISO files. Score final: 9.0.

## Related
- `ex_agent_gateway.md` — Gateway agent que pode intermediar handoffs
- `ex_boot_config_edison_claude.md` — Boot config do builder_agent receptor
- `records/framework/docs/SPAWN_PLAYBOOK.md` — Playbook completo de spawn

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_handoff_protocol]] | downstream | 0.34 |
| [[p06_iface_agent_group_handoff]] | downstream | 0.33 |
| [[p03_ch_content_pipeline]] | downstream | 0.32 |
| [[bld_examples_workflow]] | downstream | 0.31 |
| [[p12_wf_creation_pipeline]] | downstream | 0.29 |
| [[p06_is_creation_data]] | downstream | 0.29 |
| [[bld_schema_model_registry]] | downstream | 0.28 |
| [[p03_pv_pesquisa_system_v2]] | downstream | 0.27 |
| [[p06_is_knowledge_data_model]] | downstream | 0.27 |
| [[p03_ch_kc_to_notebooklm]] | downstream | 0.26 |
