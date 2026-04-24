---
id: p12_ho_isofix_batch
kind: handoff
8f: F8_collaborate
pillar: P12
title: "Handoff: ISOFIX Batch 1 (Edison)"
version: 1.0.0
created: 2026-03-05
updated: 2026-03-22
author: orchestrator
quality: 9.1
tags: [isofix, handoff, edison, orchestration]
tldr: "Real handoff dispatching builder_agent to complete ISO vectorstores for 9 agents — demonstrates autonomia total pattern"
density_score: 0.91
source: organization-core/.claude/handoffs/_archived_isofix/ISOFIX_batch_1_edison.md
domain: "orchestration"
related:
  - agent-builder
  - skill
  - bld_tools_agent
  - bld_config_kind
  - tpl_validation_schema
  - bld_architecture_kind
  - p01_kc_agent
  - bld_manifest_memory_type
  - research_then_build
  - kind-builder
---

# builder_agent — ISOFIX: ISO Completion Batch 1/7
**Autonomia Total** | **Quality 9.0+**
**REGRA: Commit e signal ANTES de qualquer pausa.**

## CONTEXTO

Completar o ISO pack de 9 agents para atingir o minimo de 10 arquivos ISO cada. Cada agent em `records/agents/{name}/iso_vectorstore/` precisa de MANIFEST, INSTRUCTIONS, QUICK_START, PRIME, ARCHITECTURE, ERROR_HANDLING, OUTPUT_TEMPLATE, EXAMPLES, SYSTEM_INSTRUCTION, TOOLS_AND_APIS.

## SEEDS

`iso, vectorstore, agent, manifest, instructions, architecture, completion`

## TAREFAS

### Step 1: Audit existing ISOs
Para cada agent (generated, tool-builder, tool-shed, agent_factory, voice, curso, mentor_humano, scout, access_control_auditor): contar ISOs existentes, listar tipos faltantes.

### Step 2: Generate missing ISOs
Ler README.md do agent para entender dominio. Usar `ISO_builder_agent_303_OUTPUT_TEMPLATE.md` como referencia. Gerar ISOs faltantes ate completar 10 por agent. Naming: `ISO_{AGENT_UPPER}_{ORDINAL}_{TYPE}.md`.

### Step 3: Validate completeness
Verificar que cada agent tem >= 10 ISOs. Listar any gaps remaining.

## SCOPE FENCE

1. SOMENTE: `records/agents/*/iso_vectorstore/`
2. NAO TOQUE: `README.md` de agents, ISOs existentes, outros diretorios

## COMMIT

```bash
git add records/agents/*/iso_vectorstore/
git commit -m "builder_agent[ISOFIX-1]: ISO completion for 9 agents (batch 1/7)"
```

## SIGNAL

```python
python -c "from records.core.python.signal_writer import write_signal; write_signal('edison', 'complete', 9.0)"
```

---
*Migrated from: organization-core/.claude/handoffs/_archived_isofix/ISOFIX_batch_1_edison.md*

## Pipeline Integration

1. Created via 8F pipeline from F1-Focus through F8-Furnish
2. Scored by cex_score across three structural layers
3. Compiled by cex_compile for structural validation
4. Retrieved by cex_retriever for context injection
5. Evolved by cex_evolve when quality regresses below target

## Properties

| Property | Value |
|----------|-------|
| Kind | `handoff` |
| Pillar | P12 |
| Domain |  |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[agent-builder]] | upstream | 0.30 |
| [[skill]] | upstream | 0.28 |
| [[bld_tools_agent]] | upstream | 0.27 |
| [[bld_config_kind]] | upstream | 0.27 |
| [[tpl_validation_schema]] | upstream | 0.26 |
| [[bld_architecture_kind]] | upstream | 0.26 |
| [[p01_kc_agent]] | upstream | 0.26 |
| [[bld_manifest_memory_type]] | upstream | 0.24 |
| [[research_then_build]] | upstream | 0.24 |
| [[kind-builder]] | upstream | 0.24 |
