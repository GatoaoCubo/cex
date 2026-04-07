---
# TEMPLATE: Lens (P02 Model)
# Valide contra P02_model/_schema.yaml (types.lens)
# Max 2048 bytes

id: p02_lens_{{PERSPECTIVE_SLUG}}
kind: lens
perspective: {{PERSPECTIVE_NAME}}
applies_to: [{{AGENT_OR_DOMAIN_1}}, {{AGENT_OR_DOMAIN_2}}]
quality: 9.0
title: "Tpl Lens"
version: "1.0.0"
author: n03_builder
tags: [artifact, builder, examples]
tldr: "Golden and anti-examples for model config, demonstrating ideal structure and common pitfalls."
domain: "model config"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Lens: {{PERSPECTIVE_NAME}}

## Perspective
<!-- INSTRUCAO: nomear o angulo especializado e o que ele privilegia. -->
1. Focus: {{O_QUE_ESTA_LENTE_PRIORIZA}}
2. Default question: {{PERGUNTA_QUE_GUIA_A_ANALISE}}
3. Ignore by default: {{O_QUE_NAO_ENTRA_NO_ESCOPO}}

## Applies To
<!-- INSTRUCAO: listar dominios, agentes ou tarefas onde esta lente faz sentido. -->
| Target | Why |
|--------|-----|
| {{AGENT_OR_DOMAIN_1}} | {{MOTIVO_1}} |
| {{AGENT_OR_DOMAIN_2}} | {{MOTIVO_2}} |

## Heuristics
<!-- INSTRUCAO: 3-5 criterios de leitura/decisao. -->
1. {{HEURISTIC_1}}
2. {{HEURISTIC_2}}
3. {{HEURISTIC_3}}

## Output Bias
<!-- INSTRUCAO: explicar como a lente muda a resposta final. -->
1. Emphasize: {{ELEMENTO_PRIORITARIO}}
2. Tradeoff accepted: {{CUSTO_ACEITO}}
3. Escalate when: {{CONDICAO_DE_ESCALADA}}

## Metadata

```yaml
id: p02_lens_{{PERSPECTIVE_SLUG}}
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply p02-lens-{{PERSPECTIVE-SLUG}}.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `lens` |
| Pillar |  |
| Domain | model config |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## System Context

This artifact participates in the CEX typed knowledge system, a fractal
architecture with 12 pillars, 8 nuclei, and 125 specialized builders.
Artifacts flow through the 8F pipeline: Focus, Frame, Fetch, Filter,
Format, Forge, Furnish, and Feedback.

Quality is enforced via 3-layer scoring: structural (30%), rubric (30%),
and semantic (40%). All artifacts target quality >= 9.0.

| Layer | Weight | Method |
|-------|--------|--------|
| Structural | 30% | Automated count-based checks |
| Rubric | 30% | Quality gate dimension scoring |
| Semantic | 40% | LLM evaluation (when L1+L2 >= 8.5) |
