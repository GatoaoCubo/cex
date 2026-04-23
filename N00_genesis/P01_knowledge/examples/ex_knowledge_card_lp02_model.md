---
id: p01_kc_lp02_model
kind: knowledge_card
pillar: P01
title: "P02 Model: Quem o Agente Eh"
version: 1.0.0
created: 2026-03-23
updated: 2026-03-23
author: builder_agent
domain: meta-construction
quality: 9.0
tags: [model, agent, persona, ISO, capabilities]
tldr: "P02 define 8 tipos de artefato de identidade (agent, lens, boot_config, mental_model, model_card, router, fallback_chain, agent_package) com ISO vectorstore de 10-22 files por agente"
when_to_use: "Quando precisar criar agentes, definir personas ou entender o sistema ISO do CEX"
keywords: [agent, agent_package, mental_model, boot_config, router]
long_tails:
  - "como criar um agente ISO completo no CEX"
  - "qual a diferenca entre agent e agent_package em P02"
axioms:
  - "Todo agente maduro tem 10+ ISO files — 10=baseline, 17=mature, 22+=golden"
linked_artifacts:
  agent: null
  skill: p04_skill_cex_forge
density_score: 0.87
related:
  - p01_kc_agent_package
  - agent-builder
  - p02_iso_organization_agent
  - bld_instruction_agent_package
  - bld_collaboration_boot_config
  - bld_knowledge_card_agent_package
  - p01_kc_lp03_prompt
  - p01_kc_agent
  - bld_output_template_kind
  - bld_config_agent_package
---

# P02 Model: Quem o Agente Eh

## Executive Summary
P02 eh o dominio de identidade do CEX, com 8 tipos de artefato que definem quem o agente eh, como se comporta e como roteia tasks. O tipo principal (agent) tem 11 secoes padrao e um iso_vectorstore com 10 files obrigatorios. 31 golden agents validados com ISO count como proxy de maturidade.

## Spec Table
| Campo | Valor | Nota |
|-------|-------|------|
| Tipos | 8 | agent, lens, boot_config, mental_model, model_card, router, fallback_chain, agent_package |
| Agent max_bytes | 5120 | Body com 11 secoes padrao |
| ISO min_files | 10 | MANIFEST, QUICK_START, PRIME, INSTRUCTIONS, ARCHITECTURE, OUTPUT_TEMPLATE, EXAMPLES, ERROR_HANDLING, UPLOAD_KIT, SYSTEM_INSTRUCTION |
| ISO tiers | 4 | minimal(3), standard(7), complete(10), whitelabel(12) |
| Boot providers | 6 | claude, cursor, windsurf, codex, copilot, pi |
| Golden agents | 31 | Evidence base do schema |

## Patterns
- Agent body segue 11 secoes fixas: overview > architecture > file_structure > when_to_use > I/O > integration > quality_gates > common_issues > invocation > related_agents > footer
- ISO package mapeia files para LPs: manifest=P02, system_instruction=P03, architecture=P08, output_template=P05
- Router type permite keyword > agent_group routing em YAML puro
- Fallback chain garante resiliencia: model A > B > C com timeout por step

## Anti-Patterns
- Agente sem ISO vectorstore: impossivel de portar entre providers
- Boot config hardcoded para 1 provider: perde portabilidade
- Mental model sem decision_tree: routing fica ambiguo
- ISO com < 10 files: classificado como sub-baseline

## Application
organization opera 118 agentes com ISO completo, todos geraveis via forge P02. O sistema agent_package permite que qualquer agente rode em claude, cursor, windsurf ou codex sem alteracao de prompt.

## References
- P02_model/_schema.yaml (fonte de verdade)
- records/agents/ (118 agentes com ISO completo)
- DISTILL_GOLDEN_AGT_SKL_PATTERNS.md (evidence base)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_agent_package]] | sibling | 0.33 |
| [[agent-builder]] | downstream | 0.31 |
| [[p02_iso_organization_agent]] | downstream | 0.31 |
| [[bld_instruction_agent_package]] | downstream | 0.27 |
| [[bld_collaboration_boot_config]] | downstream | 0.25 |
| [[bld_knowledge_card_agent_package]] | sibling | 0.25 |
| [[p01_kc_lp03_prompt]] | sibling | 0.25 |
| [[p01_kc_agent]] | sibling | 0.24 |
| [[bld_output_template_kind]] | downstream | 0.24 |
| [[bld_config_agent_package]] | downstream | 0.24 |
